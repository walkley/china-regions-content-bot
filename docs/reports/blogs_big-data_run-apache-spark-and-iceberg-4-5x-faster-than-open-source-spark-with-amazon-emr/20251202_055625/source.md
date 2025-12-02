# Run Apache Spark and Iceberg 4.5x faster than open source Spark with Amazon EMR

by Atul Payapilly, Akshaya KP, Giovanni Matteo Fumarola, and Hari Kishore Chaparala on 26 NOV 2025 in Advanced (300), Amazon EMR, Announcements, Technical How-to Permalink  Comments   Share

This post shows how Amazon EMR 7.12 can make your Apache Spark and Iceberg workloads up to 4.5x faster performance.

The [Amazon EMR runtime for Apache Spark](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark.html) provides a high-performance runtime environment with full API compatibility with open source [Apache Spark](https://spark.apache.org/) and [Apache Iceberg](https://iceberg.apache.org/). [Amazon EMR on EC2](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html), [Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html), [Amazon EMR on Amazon EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks.html), [Amazon EMR on AWS Outposts](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-outposts.html) and [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) use the optimized runtimes.

Our benchmarks show Amazon EMR 7.12 runs TPC-DS 3 TB workloads 4.5x faster than open source Spark 3.5.6 with Iceberg 1.10.0.

Performance improvements include optimizations for metadata caching, parallel I/O, adaptive query planning, data type handling, and fault tolerance. There were also some Iceberg specific regressions around data scans that we identified and fixed.

These optimizations let you match Parquet performance on Amazon EMR while keeping the key features of Iceberg key features: ACID transactions, time travel, and schema evolution.

## Benchmark results compared to open source

To assess the performance of the Spark engine with the Iceberg table format, we performed benchmark tests using the [3 TB TPC-DS dataset, version 2.13](https://www.tpc.org/tpc_documents_current_versions/pdf/tpc-ds_v2.13.0.pdf), a popular industry standard benchmark. Benchmark tests for the Amazon EMR runtime for Apache Spark and Apache Iceberg were conducted on Amazon EMR 7.12 EC2 clusters compared to open source Apache Spark 3.5.6 and Apache Iceberg 1.10.0 on EC2 clusters.

**Note**: Our results derived from the TPC-DS dataset are not directly comparable to the official TPC-DS results due to setup differences.

The setup instructions and technical details are available in our [GitHub repository](https://github.com/aws-samples/emr-on-eks-benchmark/tree/tpcds-v2.13_iceberg?tab=readme-ov-file#benchmark-for-emr-on-ec2-with-spark--iceberg). To minimize the influence of external catalogs like [AWS Glue](https://aws.amazon.com/glue) and Hive, we used the Hadoop catalog for the Iceberg tables. This uses the underlying file system, specifically Amazon S3, as the catalog. We can define this setup by configuring the property `spark.sql.catalog.<catalog_name>.type`. The fact tables used the default partitioning by the date column, which vary from 200–2,100 partitions. No precalculated statistics were used for these tables.

We ran a total of 104 SparkSQL queries in 3 sequential rounds, and the average runtime of each query across these rounds was taken for comparison. The average runtime for the 3 rounds on Amazon EMR 7.12 with Iceberg enabled was 0.37 hours, demonstrating a 4.5x speed increase compared to open source Spark 3.5.6 and Iceberg 1.10.0. The following figure presents the total runtimes in seconds.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/27/bdb5630i1.png)

The following table summarizes the metrics.

|  |  |  |  |
| --- | --- | --- | --- |
| **Metric** | **Amazon EMR 7.12 on EC2** | **Amazon EMR 7.5 on EC2** | **Open source Apache Spark 3.5.6 and Apache Iceberg 1.10.0** |
| Average runtime in seconds | 1349.62 | 1535.62 | 6113.92 |
| Geometric mean over queries in seconds | 7.45910 | 8.30046 | 22.31854 |
| Cost\* | $4.81 | $5.47 | $17.65 |

\*Detailed cost estimates are discussed later in this post.

The following chart demonstrates the per-query performance improvement of Amazon EMR 7.12 relative to open source Spark 3.5.6 and Iceberg 1.10.0. The extent of the speedup varies from one query to another, with the fastest up to 13.6x faster for q23b, with Amazon EMR outperforming open source Spark with Iceberg tables. The horizontal axis arranges the TPC-DS 3TB benchmark queries in descending order based on the performance improvement seen with Amazon EMR, and the vertical axis depicts the magnitude of this speedup as a ratio.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/27/bdb5630i2.png)

## Cost comparison breakdown

Our benchmark provides the total runtime and geometric mean data to assess the performance of Spark and Iceberg in a complex, real-world decision support scenario. For additional insights, we also examine the cost aspect. We calculate cost estimates using formulas that account for EC2 On-Demand instances, [Amazon Elastic Block Store](http://aws.amazon.com/ebs) (Amazon EBS), and Amazon EMR expenses.

- Amazon EC2 cost (includes SSD cost) = number of instances \* r5d.4xlarge hourly rate \* job runtime in hours
- 4xlarge hourly rate = $1.152 per hour
- Root Amazon EBS cost = number of instances \* Amazon EBS per GB-hourly rate \* root EBS volume size \* job runtime in hours
- Amazon EMR cost = number of instances \* r5d.4xlarge Amazon EMR cost \* job runtime in hours
- 4xlarge Amazon EMR cost = $0.27 per hour
- Total cost = Amazon EC2 cost + root Amazon EBS cost + Amazon EMR cost

The calculations reveal that the Amazon EMR 7.12 benchmark yields a 3.6x cost efficiency improvement over open source Spark 3.5.6 and Iceberg 1.10.0 in running the benchmark job.

|  |  |  |  |
| --- | --- | --- | --- |
| **Metric** | **Amazon EMR 7.12** | **Amazon EMR 7.5** | **Open source Apache Spark 3.5.6 and Apache Iceberg 1.10.0** |
| Runtime in seconds | 1349.62 | 1535.62 | 6113.92 |
| Number of EC2 instances  (Includes primary node) | 9 | 9 | 9 |
| Amazon EBS Size | 20gb | 20gb | 20gb |
| Amazon EC2  (Total runtime cost) | $3.89 | $4.42 | $17.61 |
| Amazon EBS cost | $0.01 | $0.01 | $0.04 |
| Amazon EMR cost | $0.91 | $1.04 | $0 |
| Total cost | $4.81 | $5.47 | $17.65 |
| Cost savings | Amazon EMR 7.12 is 3.6x better | Amazon EMR 7.5 is 3.2x better | Baseline |

In addition to the time-based metrics discussed so far, data from Spark event logs show that Amazon EMR scanned approximately 4.3x less data from Amazon S3 and 5.3x fewer records than the open source version in the TPC-DS 3 TB benchmark. This reduction in Amazon S3 data scanning contributes directly to cost savings for Amazon EMR workloads.

## Run open source Apache Spark benchmarks on Apache Iceberg tables

We used separate EC2 clusters, each equipped with 9 r5d.4xlarge instances, for testing both open source Spark 3.5.6 and Amazon EMR 7.12 for Iceberg workload. The primary node was equipped with 16 vCPU and 128 GB of memory, and the 8 worker nodes together had 128 vCPU and 1024 GB of memory. We conducted tests using the Amazon EMR default settings to showcase the typical user experience and minimally adjusted the settings of Spark and Iceberg to maintain a balanced comparison.

The following table summarizes the Amazon EC2 configurations for the primary node and 8 worker nodes of type r5d.4xlarge.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **EC2 Instance** | **vCPU** | **Memory (GiB)** | **Instance storage (GB)** | **EBS root volume (GB)** |
| [r5d.4xlarge](https://aws.amazon.com/ec2/instance-types/r5/) | 16 | 128 | 2 x 300 NVMe SSD | 20 GB |

### Prerequisites

The following prerequisites are required to run the benchmarking:

1. Using the instructions in the [emr-spark-benchmark GitHub repository](https://github.com/aws-samples/emr-spark-benchmark?tab=readme-ov-file#pre-requisites), set up the TPC-DS source data in your S3 bucket and on your local computer.
2. Build the benchmark application following the steps provided in [Steps to build spark-benchmark-assembly application](https://github.com/aws-samples/emr-spark-benchmark/blob/main/build-instructions.md) and copy the benchmark application to your S3 bucket. Alternatively, copy [spark-benchmark-assembly-3.5.6.jar](https://aws-blogs-artifacts-public.s3.us-east-1.amazonaws.com/artifacts/BDB-5630/spark-benchmark-assembly-3.5.6.jar) to your S3 bucket.
3. Create Iceberg tables from the TPC-DS source data. Follow the instructions on [GitHub](https://github.com/aws-samples/emr-on-eks-benchmark/tree/tpcds-v2.13_iceberg?tab=readme-ov-file#benchmark-for-emr-on-ec2-with-spark--iceberg) to create Iceberg tables using the Hadoop catalog. For example, the following code uses an Amazon EMR 7.12 cluster with [Iceberg enabled](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-spark-cluster.html#emr-iceberg-create-cluster) to create the tables:

```
aws emr add-steps --cluster-id <cluster-id> --steps Type=Spark,Name="Create Iceberg Tables",
Args=[--class,com.amazonaws.eks.tpcds.CreateIcebergTables,--conf,spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions,
--conf,spark.sql.catalog.hadoop_catalog=org.apache.iceberg.spark.SparkCatalog,
--conf,spark.sql.catalog.hadoop_catalog.type=hadoop,
--conf,spark.sql.catalog.hadoop_catalog.warehouse=s3://<bucket>/<warehouse_path>/,
--conf,spark.sql.catalog.hadoop_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO,
s3://<bucket>/<jar_location>/spark-benchmark-assembly-3.5.6.jar,s3://blogpost-sparkoneks-us-east-1/blog/BLOG_TPCDS-TEST-3T-partitioned/,
/home/hadoop/tpcds-kit/tools,parquet,3000,true,<database_name>,true,true],ActionOnFailure=CONTINUE --region <AWS region>
```

**Note**: The Hadoop catalog warehouse location and database name from the preceding step. We use the same Iceberg tables to run benchmarks with Amazon EMR 7.12 and open source Spark.

This benchmark application is built from the branch [tpcds-v2.13\_iceberg](https://github.com/aws-samples/emr-on-eks-benchmark/tree/tpcds-v2.13_iceberg). If you’re building a new benchmark application, switch to the correct branch after downloading the source code from the GitHub repository.

### Create and configure a YARN cluster on Amazon EC2

To compare Iceberg performance between Amazon EMR on Amazon EC2 and open source Spark on Amazon EC2, follow the instructions in the [emr-spark-benchmark GitHub repository](https://github.com/aws-samples/emr-spark-benchmark?tab=readme-ov-file#steps-to-setup-oss-spark-benchmarking) to create an open source Spark cluster on Amazon EC2 using Flintrock with 8 worker nodes.

Based on the cluster selection for this test, the following configurations are used:

- [yaml](https://aws-blogs-artifacts-public.s3.us-east-1.amazonaws.com/artifacts/BDB-5630/yaml.txt)
- [yarn-site.xml](https://aws-blogs-artifacts-public.s3.amazonaws.com/BDB-4277/yarn-site.xml)
- [enable-yarn.sh](https://aws-blogs-artifacts-public.s3.us-east-1.amazonaws.com/artifacts/BDB-5630/enable-yarn.sh)

Make sure to replace the placeholder `<private ip of primary node>`, in the yarn-site.xml file, with the primary node’s IP address of your Flintrock cluster.

### Run the TPC-DS benchmark with Apache Spark 3.5.6 and Apache Iceberg 1.10.0

Complete the following steps to run the TPC-DS benchmark:

1. Log in to the open source cluster primary node using `flintrock login $CLUSTER_NAME`.
2. Submit your Spark job:
1. Choose the correct Iceberg catalog warehouse location and database that has the created Iceberg tables.
2. The results are created in `s3://<YOUR_S3_BUCKET>/benchmark_run`.
3. You can track progress in `/media/ephemeral0/spark_run.log`.

```
spark-submit \
--master yarn \
--deploy-mode client \
--class com.amazonaws.eks.tpcds.BenchmarkSQL \
--conf spark.driver.cores=4 \
--conf spark.driver.memory=10g \
--conf spark.executor.cores=16 \
--conf spark.executor.memory=100g \
--conf spark.executor.instances=8 \
--conf spark.network.timeout=2000 \
--conf spark.executor.heartbeatInterval=300s \
--conf spark.dynamicAllocation.enabled=false \
--conf spark.shuffle.service.enabled=false \
--conf spark.hadoop.fs.s3a.aws.credentials.provider=com.amazonaws.auth.InstanceProfileCredentialsProvider \
--conf spark.hadoop.fs.s3.impl=org.apache.hadoop.fs.s3a.S3AFileSystem \
--conf spark.jars.packages=org.apache.hadoop:hadoop-aws:3.3.4,org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.10.0,org.apache.iceberg:iceberg-aws-bundle:1.10.0 \
--conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions   \
--conf spark.sql.catalog.local=org.apache.iceberg.spark.SparkCatalog    \
--conf spark.sql.catalog.local.type=hadoop  \
--conf spark.sql.catalog.local.warehouse=s3a://<YOUR_S3_BUCKET>/<warehouse_path>/ \
--conf spark.sql.defaultCatalog=local   \
--conf spark.sql.catalog.local.io-impl=org.apache.iceberg.aws.s3.S3FileIO   \
spark-benchmark-assembly-3.5.6.jar   \
s3://<YOUR_S3_BUCKET>/benchmark_run 3000 1 false  \
q1-v2.13,q10-v2.13,q11-v2.13,q12-v2.13,q13-v2.13,q14a-v2.13,q14b-v2.13,q15-v2.13,q16-v2.13,\
q17-v2.13,q18-v2.13,q19-v2.13,q2-v2.13,q20-v2.13,q21-v2.13,q22-v2.13,q23a-v2.13,q23b-v2.13,\
q24a-v2.13,q24b-v2.13,q25-v2.13,q26-v2.13,q27-v2.13,q28-v2.13,q29-v2.13,q3-v2.13,q30-v2.13,\
q31-v2.13,q32-v2.13,q33-v2.13,q34-v2.13,q35-v2.13,q36-v2.13,q37-v2.13,q38-v2.13,q39a-v2.13,\
q39b-v2.13,q4-v2.13,q40-v2.13,q41-v2.13,q42-v2.13,q43-v2.13,q44-v2.13,q45-v2.13,q46-v2.13,\
q47-v2.13,q48-v2.13,q49-v2.13,q5-v2.13,q50-v2.13,q51-v2.13,q52-v2.13,q53-v2.13,q54-v2.13,\
q55-v2.13,q56-v2.13,q57-v2.13,q58-v2.13,q59-v2.13,q6-v2.13,q60-v2.13,q61-v2.13,q62-v2.13,\
q63-v2.13,q64-v2.13,q65-v2.13,q66-v2.13,q67-v2.13,q68-v2.13,q69-v2.13,q7-v2.13,q70-v2.13,\
q71-v2.13,q72-v2.13,q73-v2.13,q74-v2.13,q75-v2.13,q76-v2.13,q77-v2.13,q78-v2.13,q79-v2.13,\
q8-v2.13,q80-v2.13,q81-v2.13,q82-v2.13,q83-v2.13,q84-v2.13,q85-v2.13,q86-v2.13,q87-v2.13,\
q88-v2.13,q89-v2.13,q9-v2.13,q90-v2.13,q91-v2.13,q92-v2.13,q93-v2.13,q94-v2.13,q95-v2.13,\
q96-v2.13,q97-v2.13,q98-v2.13,q99-v2.13,ss_max-v2.13    \
true <database> > /media/ephemeral0/spark_run.log 2>&1 &!
```

### Summarize the results

After the Spark job finishes, retrieve the test result file from the output S3 bucket at `s3://<YOUR_S3_BUCKET>/benchmark_run/timestamp=xxxx/summary.csv/xxx.csv`. This can be done either through the Amazon S3 console by navigating to the specified bucket location or by using the [Amazon Command Line Interfac](https://aws.amazon.com/cli/)e (AWS CLI). The Spark benchmark application organizes the data by creating a timestamp folder and placing a summary file within a folder labeled `summary.csv`. The output CSV files contain 4 columns without headers:

- Query name
- Median time
- Minimum time
- Maximum time

With the data from 3 separate test runs with 1 iteration each time, we can calculate the average and geometric mean of the benchmark runtimes.

## Run the TPC-DS benchmark with Amazon EMR runtime for Apache Spark

Most of the instructions are similar to [Steps to run Spark Benchmarking](https://github.com/aws-samples/emr-spark-benchmark#steps-to-setup-emr-benchmarking) with a few Iceberg-specific details.

### Prerequisites

Complete the following prerequisite steps:

1. Run `aws configure` to configure the AWS CLI shell to point to the benchmarking AWS account. Refer to [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) for instructions.
2. Upload the benchmark application JAR file to Amazon S3.

### Deploy Amazon EMR cluster and run the benchmark job

Complete the following steps to run the benchmark job:

1. Use the AWS CLI command as shown in [Deploy EMR on EC2 Cluster and run benchmark job](https://github.com/aws-samples/emr-spark-benchmark?tab=readme-ov-file#deploy-emr-on-ec2-cluster-and-run-benchmark-job) to deploy an Amazon EMR on EC2 cluster. Make sure to enable Iceberg. See [Create an Iceberg cluster](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-spark-cluster.html#emr-iceberg-create-cluster) for more details. Choose the correct Amazon EMR version, root volume size, and same resource configuration as the open source Flintrock setup. Refer to [create-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-cluster.html) for a detailed description of the AWS CLI options.
2. Store the cluster ID from the response. We need this for the next step.
3. Submit the benchmark job in Amazon EMR using `add-steps` from the AWS CLI:
2. Replace `<cluster ID>` with the cluster ID from Step 2.
3. The benchmark application is at `s3://<your-bucket>/spark-benchmark-assembly-3.5.6.jar`.
4. Choose the correct Iceberg catalog warehouse location and database that has the created Iceberg tables. This should be the same as the one used for the open source TPC-DS benchmark run.
5. The results will be in `s3://<your-bucket>/benchmark_run`.

```
aws emr add-steps   --cluster-id <cluster-id>
--steps Type=Spark,Name="SPARK Iceberg EMR TPCDS Benchmark Job",
Args=[--class,com.amazonaws.eks.tpcds.BenchmarkSQL,
--conf,spark.driver.cores=4,
--conf,spark.driver.memory=10g,
--conf,spark.executor.cores=16,
--conf,spark.executor.memory=100g,
--conf,spark.executor.instances=8,
--conf,spark.network.timeout=2000,
--conf,spark.executor.heartbeatInterval=300s,
--conf,spark.dynamicAllocation.enabled=false,
--conf,spark.shuffle.service.enabled=false,
--conf,spark.sql.iceberg.data-prefetch.enabled=true,
--conf,spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions,
--conf,spark.sql.catalog.local=org.apache.iceberg.spark.SparkCatalog,
--conf,spark.sql.catalog.local.type=hadoop,
--conf,spark.sql.catalog.local.warehouse=s3://<your-bucket>/<warehouse-path>,
--conf,spark.sql.defaultCatalog=local,
--conf,spark.sql.catalog.local.io-impl=org.apache.iceberg.aws.s3.S3FileIO,
s3://<your-bucket>/spark-benchmark-assembly-3.5.6.jar,
s3://<your-bucket>/benchmark_run,3000,1,false,
'q1-v2.13\,q10-v2.13\,q11-v2.13\,q12-v2.13\,q13-v2.13\,q14a-v2.13\,q14b-v2.13\,q15-v2.13\,q16-v2.13\,q17-v2.13\,q18-v2.13\,q19-v2.13\,q2-v2.13\,q20-v2.13\,q21-v2.13\,q22-v2.13\,q23a-v2.13\,q23b-v2.13\,q24a-v2.13\,q24b-v2.13\,q25-v2.13\,q26-v2.13\,q27-v2.13\,q28-v2.13\,q29-v2.13\,q3-v2.13\,q30-v2.13\,q31-v2.13\,q32-v2.13\,q33-v2.13\,q34-v2.13\,q35-v2.13\,q36-v2.13\,q37-v2.13\,q38-v2.13\,q39a-v2.13\,q39b-v2.13\,q4-v2.13\,q40-v2.13\,q41-v2.13\,q42-v2.13\,q43-v2.13\,q44-v2.13\,q45-v2.13\,q46-v2.13\,q47-v2.13\,q48-v2.13\,q49-v2.13\,q5-v2.13\,q50-v2.13\,q51-v2.13\,q52-v2.13\,q53-v2.13\,q54-v2.13\,q55-v2.13\,q56-v2.13\,q57-v2.13\,q58-v2.13\,q59-v2.13\,q6-v2.13\,q60-v2.13\,q61-v2.13\,q62-v2.13\,q63-v2.13\,q64-v2.13\,q65-v2.13\,q66-v2.13\,q67-v2.13\,q68-v2.13\,q69-v2.13\,q7-v2.13\,q70-v2.13\,q71-v2.13\,q72-v2.13\,q73-v2.13\,q74-v2.13\,q75-v2.13\,q76-v2.13\,q77-v2.13\,q78-v2.13\,q79-v2.13\,q8-v2.13\,q80-v2.13\,q81-v2.13\,q82-v2.13\,q83-v2.13\,q84-v2.13\,q85-v2.13\,q86-v2.13\,q87-v2.13\,q88-v2.13\,q89-v2.13\,q9-v2.13\,q90-v2.13\,q91-v2.13\,q92-v2.13\,q93-v2.13\,q94-v2.13\,q95-v2.13\,q96-v2.13\,q97-v2.13\,q98-v2.13\,q99-v2.13\,ss_max-v2.13',
true,<database>],ActionOnFailure=CONTINUE --region <aws-region>
```

### Summarize the results

After the step is complete, you can see the summarized benchmark result at `s3://<YOUR_S3_BUCKET>/benchmark_run/timestamp=xxxx/summary.csv/xxx.csv` in the same way as the previous run and compute the average and geometric mean of the query runtimes.

## Clean up

To help prevent future charges, delete the resources you created by following the instructions provided in the [Cleanup section of the GitHub repository](https://github.com/aws-samples/emr-spark-benchmark#cleanup).

## Summary

Amazon EMR optimizes the runtime for Spark when used with Iceberg tables, achieving 4.5x faster performance than open source Apache Spark 3.5.6 and Apache Iceberg 1.10.0 with Amazon EMR 7.12 on TPC-DS 3 TB, v2.13. This represents a significant advancement from Amazon EMR 7.5, which delivered 3.6x faster performance and closes the gap to parquet performance on Amazon EMR so customers can use the benefits of Iceberg without a performance penalty.

We encourage you to keep up to date with the latest Amazon EMR releases to fully benefit from ongoing performance improvements.

To stay informed, subscribe to the [RSS feed for the AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/feed/), where you can find updates on the Amazon EMR runtime for Spark and Iceberg, as well as tips on configuration best practices and tuning recommendations.

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/27/atul.jpg)Atul Felix Payapilly** is a software development engineer for Amazon EMR at Amazon Web Services.

**![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/27/apatta.jpeg)Akshaya KP** is a software development engineer for Amazon EMR at Amazon Web Services.

**[![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2024/08/17/BDB-4467-kishoha.jpeg)](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2024/08/17/BDB-4467-kishoha.jpeg)Hari Kishore Chaparala** is a software development engineer for Amazon EMR at Amazon Web Services.

**![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/27/giovanni.jpeg)Giovanni Matteo** is the Senior Manager for the Amazon EMR Spark and Iceberg group.