[Skip to Main Content](#aws-page-content-main)

* Filter: All

* English
* [Contact us](https://aws.amazon.com/contact-us/?nc2=h_ut_cu)
* [AWS Marketplace](https://aws.amazon.com/marketplace/?nc2=h_utmp)
* Support
* My account

* Search

  Filter: All
* [Sign in to console](https://console.aws.amazon.com/console/home/?nc2=h_si&src=header-signin)
* [Create account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_su&src=header_signup)

AWS Blogs

* [Home](https://aws.amazon.com/blogs/)
* Blogs
* Editions

## [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/)

# Manage concurrent write conflicts in Apache Iceberg on the AWS Glue Data Catalog

by Sotaro Hikita and Noritaka Sekiyama on 08 APR 2025 in [Analytics](https://aws.amazon.com/blogs/big-data/category/analytics/ "View all posts in Analytics"), [AWS Big Data](https://aws.amazon.com/blogs/big-data/category/big-data/ "View all posts in AWS Big Data"), [AWS Glue](https://aws.amazon.com/blogs/big-data/category/analytics/aws-glue/ "View all posts in AWS Glue") [Permalink](https://aws.amazon.com/blogs/big-data/manage-concurrent-write-conflicts-in-apache-iceberg-on-the-aws-glue-data-catalog/)  [Comments](https://aws.amazon.com/blogs/big-data/manage-concurrent-write-conflicts-in-apache-iceberg-on-the-aws-glue-data-catalog/#Comments)  Share

In modern data architectures, Apache Iceberg has emerged as a popular table format for data lakes, offering key features including ACID transactions and concurrent write support. Although these capabilities are powerful, implementing them effectively in production environments presents unique challenges that require careful consideration.

Consider a common scenario: A streaming pipeline continuously writes data to an Iceberg table while scheduled maintenance jobs perform compaction operations. Although Iceberg provides built-in mechanisms to handle concurrent writes, certain conflict scenarios—such as between streaming updates and compaction operations—can lead to transaction failures that require specific handling patterns.

This post demonstrates how to implement reliable concurrent write handling mechanisms in Iceberg tables. We will explore Iceberg’s concurrency model, examine common conflict scenarios, and provide practical implementation patterns of both automatic retry mechanisms and situations requiring custom conflict resolution logic for building resilient data pipelines. We will also cover the pattern with automatic compaction through [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) table optimization.

## Common conflict scenarios

The most frequent data conflicts occur in several specific operational scenarios that many organizations encounter in their data pipelines, which we discuss in this section.

### Concurrent UPDATE/DELETE on overlapping partitions

When multiple processes attempt to modify the same partition simultaneously, data conflicts can arise. For example, imagine a data quality process updating customer records with corrected addresses while another process is deleting outdated customer records. Both operations target the same partition based on `customer_id`, leading to potential conflicts because they’re modifying an overlapping dataset. These conflicts are particularly common in large-scale data cleanup operations.

### Compaction vs. streaming writes

A classic conflict scenario occurs during table maintenance operations. Consider a streaming pipeline ingesting real-time event data while a scheduled compaction job runs to optimize file sizes. The streaming process might be writing new records to a partition while the compaction job is attempting to combine existing files in the same partition. This scenario is especially common with Data Catalog table optimization, where automatic compaction can run concurrently with continuous data ingestion.

### Concurrent MERGE operations

MERGE operations are particularly susceptible to conflicts because they involve both reading and writing data. For instance, an hourly job might be merging customer profile updates from a source system while a separate job is merging preference updates from another system. If both jobs attempt to modify the same customer records, they can conflict because each operation bases its changes on a different view of the current data state.

### General concurrent table updates

When multiple transactions occur simultaneously, some transactions might fail to commit to the catalog due to interference from other transactions. Iceberg has mechanisms to handle this scenario, so it can adapt to concurrent transactions in many cases. However, commits can still fail if the latest metadata is updated after the base metadata version is established. This scenario applies to any type of updates on an Iceberg table.

## Iceberg’s concurrency model and conflict type

Before diving into specific implementation patterns, it’s essential to understand how Iceberg manages concurrent writes through its table architecture and transaction model. Iceberg uses a layered architecture to manage table state and data:

* **Catalog layer** – Maintains a pointer to the current table metadata file, serving as the single source of truth for table state. The Data Catalog provides the functionality as the Iceberg catalog.
* **Metadata layer** – Contains metadata files that track table history, schema evolution, and snapshot information. These files are stored on [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3).
* **Data layer** – Stores the actual data files and delete files (for Merge-on-Read operations). These files are also stored on Amazon S3.

The following diagram illustrates this architecture.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/04/04/BDB-5015-1-refined-1024x777.png)

This architecture is fundamental to Iceberg’s optimistic concurrency control, where multiple writers can proceed with their operations simultaneously, and conflicts are detected at commit time.

### Write transaction flow

A typical write transaction in Iceberg follows these key steps:

1. Read current state. In many operations (like OVERWRITE, MERGE, and DELETE), the query engine needs to know which files or rows are relevant, so it reads the current table snapshot. This is optional for operations like INSERT.
2. Determine the changes in transaction, and write new data files.
3. Load the table’s latest metadata, and determine which metadata version is used as the base for the update.
4. Check if the change prepared in Step 2 is compatible with the latest table data in Step 3. If the check failed, the transaction must stop.
5. Generate new metadata files.
6. Commit the metadata files to the catalog. If the commit failed, retry from Step 3. The number of retries depends on the configuration.

The following diagram illustrates this workflow.

![Iceberg write transaction flow](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/04/02/BDB-5015-2.jpg)

Conflicts can occur at two critical points:

* **Data update conflicts** – During validation when checking for data conflicts (Step 4)
* **Catalog commit conflicts** – During the commit when attempting to update the catalog pointer (Step 6)

When working with Iceberg tables, understanding the types of conflicts that can occur and how they’re handled is crucial for building reliable data pipelines. Let’s examine the two primary types of conflicts and their characteristics.

### Catalog commit conflicts

Catalog commit conflicts occur when multiple writers attempt to update the table metadata simultaneously. When a commit conflict occurs, Iceberg will automatically retry the operation based on the table’s write properties. The retry process only repeats the metadata commit, not the entire transaction, making it both safe and efficient. When the retries fail, the transaction fails with `CommitFailedException`.

In the following diagram, two transactions run concurrently. Transaction 1 successfully updates the table’s latest snapshot in the Iceberg catalog from 0 to 1. Meanwhile, transaction 2 attempts to update from Snapshot 0 to 1, but when it tries to commit the changes to the catalog, it finds that the latest snapshot has already been changed to 1 by transaction 1. As a result, transaction 2 needs to retry from Step 3.

![Catalog commit conflicts1](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/04/02/BDB-5015-3.jpg)

These conflicts are typically transient and can be automatically resolved through retries. You can optionally configure write properties controlling commit retry behavior. For more detailed configuration, refer to [Write properties](https://iceberg.apache.org/docs/latest/configuration/#write-properties) in the Iceberg documentation.

The metadata used when reading the current state (Step 1) and the snapshot used as base metadata for updates (Step 3) can be different. Even if another transaction updates the latest snapshot between Steps 1 and 3, the current transaction can still commit changes to the catalog as long as it passes the data conflict check (Step 4). This means that even when computing changes and writing data files (Step 1 to 2) take a long time, and other transactions make changes during this period, the transaction can still attempt to commit to the catalog. This demonstrates Iceberg’s intelligent concurrency control mechanism.

The following diagram illustrates this workflow.

![Catalog commit conflicts2](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/04/02/BDB-5015-4.jpg)

### Data update conflicts

Data update conflicts are more complex and occur when concurrent transactions attempt to modify overlapping data. During a write transaction, the query engine checks consistency between the snapshot being written and the latest snapshot according to transaction isolation rules. When incompatibility is detected, the transaction fails with a `ValidationException`.

In the following diagram, two transactions run concurrently on an employee table containing `id`, `name`, and `salary` columns. Transaction 1 attempts to update a record based on Snapshot 0 and successfully commits this change, making the latest snapshot version 1. Meanwhile, transaction 2 also attempts to update the same record based on Snapshot 0. When transaction 2 initially scanned the data, the latest snapshot was 0, but it has since been updated to 1 by transaction 1. During the data conflict check, transaction 2 discovers that its changes conflict with Snapshot 1, resulting in the transaction failing.

![data conflict](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/04/02/BDB-5015-5.jpg)

These conflicts can’t be automatically retried by Iceberg’s library because when data conflicts occur, the table’s state has changed, making it uncertain whether retrying the transaction would maintain overall data consistency. You need to handle this type of conflict based on your specific use case and requirements.

The following table summarizes how different write patterns have varying likelihood of conflicts.

|  |  |  |
| --- | --- | --- |
| **Write Pattern** | **Catalog Commit Conflict (Automatically retryable)** | **Data Conflict (Non-retryable)** |
| INSERT ([AppendFiles](https://iceberg.apache.org/javadoc/latest/org/apache/iceberg/AppendFiles.html)) | Yes | Never |
| UPDATE/DELETE with Copy-on-Write or Merge-on-Read ([OverwriteFiles](https://iceberg.apache.org/javadoc/latest/org/apache/iceberg/OverwriteFiles.html)) | Yes | Yes |
| Compaction ([RewriteFiles](https://iceberg.apache.org/javadoc/latest/org/apache/iceberg/RewriteFiles.html)) | Yes | Yes |

**Iceberg table’s isolation levels**

Iceberg tables support two isolation levels: **Serializable** and **Snapshot isolation**. Both provide a read consistent view of the table and ensure readers see only committed data. Serializable isolation guarantees that concurrent operations run as if they were performed in some sequential order. Snapshot isolation provides weaker guarantees but offers better performance in environments with many concurrent writers. Under snapshot isolation, data conflict checks can pass even when concurrent transactions add new files with records that potentially match its conditions.

By default, Iceberg tables use serializable isolation. You can configure isolation levels for specific operations using table properties:

```
tbl_properties = {
    'write.delete.isolation-level' = 'serializable',
    'write.update.isolation-level' = 'serializable',
    'write.merge.isolation-level' = 'serializable'
}
```

You must choose the appropriate isolation level based on your use case. Note that for conflicts between streaming ingestion and compaction operations, which is one of the most common scenarios, snapshot isolation does not provide any additional benefits to the default serializable isolation. For more detailed configuration, see [IsolationLevel](https://iceberg.apache.org/javadoc/latest/org/apache/iceberg/IsolationLevel.html).

## Implementation patterns

Implementing robust concurrent write handling in Iceberg requires different strategies depending on the conflict type and use case. In this section, we share proven patterns for handling common scenarios.

### Manage catalog commit conflicts

Catalog commit conflicts are relatively straightforward to handle through table properties. The following configurations serve as initial baseline settings that you can adjust based on your specific workload patterns and requirements.

For frequent concurrent writes (for example, streaming ingestion):

```
tbl_properties = {
    'commit.retry.num-retries': '10',
    'commit.retry.min-wait-ms': '100',
    'commit.retry.max-wait-ms': '10000',
    'commit.retry.total-timeout-ms': '1800000'
}
```

For maintenance operations (for example, compaction):

```
tbl_properties = {
    'commit.retry.num-retries': '4',
    'commit.retry.min-wait-ms': '1000',
    'commit.retry.max-wait-ms': '60000',
    'commit.retry.total-timeout-ms': '1800000'
}
```

### Manage data update conflicts

For data update conflicts, which can’t be automatically retried, you need to implement a custom retry mechanism with proper error handling. A common scenario is when stream UPSERT ingestion conflicts with concurrent compaction operations. In such cases, the stream ingestion job should typically implement retries to handle incoming data. Without proper error handling, the job will fail with a `ValidationException`.

We show two example scripts demonstrating a practical implementation of error handling for data conflicts in Iceberg streaming jobs. The code specifically catches `ValidationException` through `Py4JJavaError` handling, which is essential for proper Java-Python interaction. It includes [exponential backoff and jitter strategy](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) by adding a random delay of 0–25% to each retry interval. For example, if the base exponential backoff time is 4 seconds, the actual retry delay will be between 4–5 seconds, helping prevent immediate retry storms while maintaining reasonable latency.

In this example, we create a scenario with frequent MERGE operations on the same records by using `'value'` as a unique identifier and artificially limiting its range. By applying a modulo operation (`value % 20`), we constrain all values to fall within 0–19, which means multiple updates will target the same records. For instance, if the original stream contains values 0, 20, 40, and 60, they will all be mapped to 0, resulting in multiple MERGE operations targeting the same record. We then use `groupBy` and max aggregation to simulate a typical UPSERT pattern where we keep the latest record for each value. The transformed data is stored in a temporary view that serves as the source table in the MERGE statement, allowing us to perform UPDATE operations using `'value'` as the matching condition. This setup helps demonstrate how our retry mechanism handles `ValidationExceptions` that occur when concurrent transactions attempt to modify the same records.

The first example uses Spark Structured Streaming using a rate source with a 20-second trigger interval to demonstrate the retry mechanism’s behavior when concurrent operations cause data conflicts. Replace `<database_name>` with your database name, `<table_name>` with your table name, `amzn-s3-demo-bucket` with your S3 bucket name.

```
import time
import random
from pyspark.sql import SparkSession
from py4j.protocol import Py4JJavaError
from pyspark.sql.functions import max as max_

CATALOG = "glue_catalog"
DATABASE = "<database_name>"
TABLE = "<table_name>"
BUCKET = "amzn-s3-demo-bucket"

spark = SparkSession.builder \
    .appName("IcebergUpsertExample") \
    .config(f"spark.sql.catalog.{CATALOG}", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.extensions","org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config(f"spark.sql.catalog.{CATALOG}.io-impl","org.apache.iceberg.aws.s3.S3FileIO") \
    .config("spark.sql.defaultCatalog", CATALOG) \
    .config(f"spark.sql.catalog.{CATALOG}.type", "glue") \
    .config(f"spark.sql.catalog.{CATALOG}.cache-enabled", "false") \
	.getOrCreate()

spark.sql(f"""
    CREATE TABLE IF NOT EXISTS {DATABASE}.{TABLE} (
        timestamp TIMESTAMP,
        value LONG
    )
    USING iceberg
    LOCATION 's3://{BUCKET}/warehouse'
""")

def backoff(attempt):
    """Exponential backoff with jitter"""
    exp_backoff = min(2 ** attempt, 60)
    jitter = random.uniform(0, 0.25 * exp_backoff)
    return exp_backoff + jitter

def is_validation_exception(java_exception):
    """Check if exception is ValidationException"""
    cause = java_exception
    while cause is not None:
        if "org.apache.iceberg.exceptions.ValidationException" in str(cause.getClass().getName()):
            return True
        cause = cause.getCause()
    return False

def upsert_with_retry(microBatchDF, batchId):
    max_retries = 5
    attempt = 0

    # Use a narrower key range to intentionally increase updates for the same value in MERGE
    transformedDF = microBatchDF \
        .selectExpr("timestamp", "value % 20 AS value") \
        .groupBy("value") \
        .agg(max_("timestamp").alias("timestamp"))

    view_name = f"incoming_data_{batchId}"
    transformedDF.createOrReplaceGlobalTempView(view_name)

    while attempt < max_retries:
        try:
            spark.sql(f"""
                MERGE INTO {DATABASE}.{TABLE} AS t
                USING global_temp.{view_name} AS i
                ON t.value = i.value
                WHEN MATCHED THEN
                  UPDATE SET
                    t.timestamp = i.timestamp,
                    t.value     = i.value
                WHEN NOT MATCHED THEN
                  INSERT (timestamp, value)
                  VALUES (i.timestamp, i.value)
            """)

            print(f"[SUCCESS] Batch {batchId} processed successfully")
            return

        except Py4JJavaError as e:
            if is_validation_exception(e.java_exception):
                attempt += 1
                if attempt < max_retries:
                    delay = backoff(attempt)
                    print(f"[RETRY] Batch {batchId} failed with ValidationException. "
                          f"Retrying in {delay} seconds. Attempt {attempt}/{max_retries}")
                    time.sleep(delay)
                else:
                    print(f"[FAILED] Batch {batchId} failed after {max_retries} attempts")
                    raise

# Sample streaming query setup
df = spark.readStream \
    .format("rate") \
    .option("rowsPerSecond", 10) \
    .load()

# Start streaming query
query = df.writeStream \
    .trigger(processingTime="20 seconds") \
    .option("checkpointLocation", f"s3://{BUCKET}/checkpointLocation") \
    .foreachBatch(upsert_with_retry) \
    .start()

query.awaitTermination()
```

The second example uses `GlueContext.forEachBatch` available on AWS Glue Streaming jobs. The implementation pattern for the retry mechanism remains the same, but the main differences are the initial setup using `GlueContext` and how to create a streaming DataFrame. Although our example uses `spark.readStream` with a rate source for demonstration, in actual AWS Glue Streaming jobs, you would typically create your streaming DataFrame using `glueContext.create_data_frame.from_catalog` to read from sources like [Amazon Kinesis](https://aws.amazon.com/kinesis/) or Kafka. For more details, see [AWS Glue Streaming connections](https://docs.aws.amazon.com/glue/latest/dg/glue-streaming-connections.html). Replace `<database_name>` with your database name, `<table_name>` with your table name, `amzn-s3-demo-bucket` with your S3 bucket name.

```
import time
import random
from py4j.protocol import Py4JJavaError
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import max as max_

CATALOG = "glue_catalog"
DATABASE = "<database_name>"
TABLE = "<table_name>"
BUCKET = "amzn-s3-demo-bucket"

spark = SparkSession.builder \
    .appName("IcebergUpsertExample") \
    .config(f"spark.sql.catalog.{CATALOG}", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.extensions","org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config(f"spark.sql.catalog.{CATALOG}.io-impl","org.apache.iceberg.aws.s3.S3FileIO") \
    .config("spark.sql.defaultCatalog", CATALOG) \
    .config(f"spark.sql.catalog.{CATALOG}.type", "glue") \
    .getOrCreate()

sc = spark.sparkContext
glueContext = GlueContext(sc)

spark.sql(f"""
    CREATE TABLE IF NOT EXISTS {DATABASE}.{TABLE} (
        timestamp TIMESTAMP,
        value LONG
    )
    USING iceberg
    LOCATION 's3://{BUCKET}/warehouse'
""")

def backoff(attempt):
    exp_backoff = min(2 ** attempt, 60)
    jitter = random.uniform(0, 0.25 * exp_backoff)
    return exp_backoff + jitter

def is_validation_exception(java_exception):
    cause = java_exception
    while cause is not None:
        if "org.apache.iceberg.exceptions.ValidationException" in str(cause.getClass().getName()):
            return True
        cause = cause.getCause()
    return False

def upsert_with_retry(batch_df, batchId):
    max_retries = 5
    attempt = 0
    transformedDF = batch_df.selectExpr("timestamp", "value % 20 AS value") \
                           .groupBy("value") \
                           .agg(max_("timestamp").alias("timestamp"))

    view_name = f"incoming_data_{batchId}"
    transformedDF.createOrReplaceGlobalTempView(view_name)

    while attempt < max_retries:
        try:
            spark.sql(f"""
                MERGE INTO {DATABASE}.{TABLE} AS t
                USING global_temp.{view_name} AS i
                ON t.value = i.value
                WHEN MATCHED THEN
                  UPDATE SET
                    t.timestamp = i.timestamp,
                    t.value     = i.value
                WHEN NOT MATCHED THEN
                  INSERT (timestamp, value)
                  VALUES (i.timestamp, i.value)
            """)
            print(f"[SUCCESS] Batch {batchId} processed successfully")
            return
        except Py4JJavaError as e:
            if is_validation_exception(e.java_exception):
                attempt += 1
                if attempt < max_retries:
                    delay = backoff(attempt)
                    print(f"[RETRY] Batch {batchId} failed with ValidationException. "
                          f"Retrying in {delay} seconds. Attempt {attempt}/{max_retries}")
                    time.sleep(delay)
                else:
                    print(f"[FAILED] Batch {batchId} failed after {max_retries} attempts")
                    raise

# Sample streaming query setup
streaming_df = spark.readStream \
    .format("rate") \
    .option("rowsPerSecond", 10) \
    .load()

# In actual Glue Streaming jobs, you would typically create a streaming DataFrame like this:
"""
streaming_df = glueContext.create_data_frame.from_catalog(
    database = "database",
    table_name = "table_name",
    transformation_ctx = "streaming_df",
    additional_options = {
        "startingPosition": "TRIM_HORIZON",
        "inferSchema": "false"
    }
)
"""

glueContext.forEachBatch(
    frame=streaming_df,
    batch_function=upsert_with_retry,
    options={
        "windowSize": "20 seconds",
        "checkpointLocation": f"s3://{BUCKET}/checkpointLocation"
    }
)
```

### Minimize conflict possibility by scoping your operations

When performing maintenance operations like compaction or updates, it’s recommended to narrow down the scope to minimize overlap with other operations. For example, consider a table partitioned by date where a streaming job continuously upserts data for the latest date. The following is the example script to run the [rewrite\_data\_files](https://iceberg.apache.org/docs/latest/spark-procedures/#rewrite_data_files) procedure to compact the entire table:

```
# Example of broad scope compaction
spark.sql("""
   CALL catalog_name.system.rewrite_data_files(
       table => 'db.table_name'
   )
""")
```

By narrowing the compaction scope with a date partition filter in the `where` clause, you can avoid conflicts between streaming ingestion and compaction operations. The streaming job can continue to work with the latest partition while compaction processes historical data.

```
# Narrow down the scope by partition
spark.sql("""
    CALL catalog_name.system.rewrite_data_files(
        table => 'db.table_name',
        where => 'date_partition < current_date'
    )
""")
```

## Conclusion

Successfully managing concurrent writes in Iceberg requires understanding both the table architecture and various conflict scenarios. In this post, we explored how to implement reliable conflict handling mechanisms in production environments.

The most critical concept to remember is the distinction between catalog commit conflicts and data conflicts. Although catalog commit conflicts can be handled through automatic retries and table properties configuration, data conflicts require careful implementation of custom handling logic. This becomes particularly important when implementing maintenance operations like compaction, where using the `where` clause in `rewrite_data_files` can significantly minimize conflict potential by reducing the scope of operations.

For streaming pipelines, the key to success lies in implementing proper error handling that can differentiate between conflict types and respond appropriately. This includes configuring suitable retry settings through table properties and implementing backoff strategies that align with your workload characteristics. When combined with well-timed maintenance operations, these patterns help build resilient data pipelines that can handle concurrent writes reliably.

By applying these patterns and understanding the underlying mechanisms of Iceberg’s concurrency model, you can build robust data pipelines that effectively handle concurrent write scenarios while maintaining data consistency and reliability.

---

### About the Authors

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2024/07/08/sotaro.png)**Sotaro Hikita** is an Analytics Solutions Architect. He supports customers across a wide range of industries in building and operating analytics platforms more effectively. He is particularly passionate about big data technologies and open source software.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2024/11/06/sekiyama.jpg)**Noritaka Sekiyama** is a Principal Big Data Architect on the AWS Glue team. He works based in Tokyo, Japan. He is responsible for building software artifacts to help customers. In his spare time, he enjoys cycling with his road bike.

TAGS: [Apache Iceberg](https://aws.amazon.com/blogs/big-data/tag/apache-iceberg/)

Loading comments…

### Resources

* [Amazon Athena](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-athena?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon EMR](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-emr?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon Kinesis](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-kinesis?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon MSK](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-managed-streaming-for-apache-kafka/)
* [Amazon QuickSight](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-quicksight?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon Redshift](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-redshift-analytics?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [AWS Glue](https://aws.amazon.com/blogs/big-data/category/analytics/aws-glue?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-social)

[Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc1=f_ct&src=footer_signup)

## Learn

* [What Is AWS?](/what-is-aws/?nc1=f_cc)
* [What Is Cloud Computing?](/what-is-cloud-computing/?nc1=f_cc)
* [What Is Agentic AI?](/what-is/agentic-ai/?nc1=f_cc)
* [Cloud Computing Concepts Hub](/what-is/?nc1=f_cc)
* [AWS Cloud Security](/security/?nc1=f_cc)
* [What's New](/new/?nc1=f_cc)
* [Blogs](/blogs/?nc1=f_cc)
* [Press Releases](https://press.aboutamazon.com/press-releases/aws)

## Resources

* [Getting Started](/getting-started/?nc1=f_cc)
* [Training](/training/?nc1=f_cc)
* [AWS Trust Center](/trust-center/?nc1=f_cc)
* [AWS Solutions Library](/solutions/?nc1=f_cc)
* [Architecture Center](/architecture/?nc1=f_cc)
* [Product and Technical FAQs](/faqs/?nc1=f_dr)
* [Analyst Reports](/resources/analyst-reports/?nc1=f_cc)
* [AWS Partners](/partners/work-with-partners/?nc1=f_dr)

## Developers

* [Builder Center](/developer/?nc1=f_dr)
* [SDKs & Tools](/developer/tools/?nc1=f_dr)
* [.NET on AWS](/developer/language/net/?nc1=f_dr)
* [Python on AWS](/developer/language/python/?nc1=f_dr)
* [Java on AWS](/developer/language/java/?nc1=f_dr)
* [PHP on AWS](/developer/language/php/?nc1=f_cc)
* [JavaScript on AWS](/developer/language/javascript/?nc1=f_dr)

## Help

* [Contact Us](/contact-us/?nc1=f_m)
* [File a Support Ticket](https://console.aws.amazon.com/support/home/?nc1=f_dr)
* [AWS re:Post](https://repost.aws/?nc1=f_dr)
* [Knowledge Center](https://repost.aws/knowledge-center/?nc1=f_dr)
* [AWS Support Overview](/premiumsupport/?nc1=f_dr)
* [Get Expert Help](https://iq.aws.amazon.com/?utm=mkt.foot/?nc1=f_m)
* [AWS Accessibility](/accessibility/?nc1=f_cc)
* [Legal](/legal/?nc1=f_cc)

English

Back to top

Amazon is an Equal Opportunity Employer: Minority / Women / Disability / Veteran / Gender Identity / Sexual Orientation / Age.

[x](https://twitter.com/awscloud) [facebook](https://www.facebook.com/amazonwebservices) [linkedin](https://www.linkedin.com/company/amazon-web-services/) [instagram](https://www.instagram.com/amazonwebservices/) [twitch](https://www.twitch.tv/aws) [youtube](https://www.youtube.com/user/AmazonWebServices/Cloud/) [podcasts](/podcasts/?nc1=f_cc) [email](https://pages.awscloud.com/communication-preferences?trk=homepage)

* [Privacy](/privacy/?nc1=f_pr)
* [Site terms](/terms/?nc1=f_pr)
* Cookie Preferences

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved.