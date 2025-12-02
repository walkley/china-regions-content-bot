# Accelerate data lake operations with Apache Iceberg V3 deletion vectors and row lineage

by Ron Ortloff on 26 NOV 2025 in Amazon EMR, Amazon SageMaker, Amazon Simple Storage Service (S3), Announcements, AWS Glue, Intermediate (200), Technical How-to Permalink  Comments   Share

Organizations building petabyte-scale data lakes face increasing challenges as their data grows. Batch updates and compliance deletes create a proliferation of positional delete files, slowing downstream data pipelines and driving up storage costs. Tracking data changes for audit trails and incremental processing requires custom, engine-specific implementations that add complexity and maintenance burden. As data volumes scale, these challenges compound, leaving data teams juggling custom solutions and increasing operational costs just to maintain data freshness and compliance.

Apache Iceberg V3 addresses these challenges with two new capabilities: deletion vectors and row lineage. AWS now delivers these capabilities across [Apache Spark on Amazon EMR 7.12](https://aws.amazon.com/emr/), [AWS Glue](https://aws.amazon.com/glue/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/unified-studio/) notebooks, [Amazon S3 Tables](https://aws.amazon.com/s3/features/tables/), and the [AWS Glue Data Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html), giving you a complete, integrated V3 experience without custom implementation. This means faster writes, lower storage costs, comprehensive audit trails, and efficient incremental processing, all working seamlessly across your entire data lake architecture.

In this post, we walk you through the new capabilities in Iceberg V3, explain how deletion vectors and row lineage address these challenges, explore real-world use cases across industries, and provide practical guidance on implementing Iceberg V3 features across AWS analytics, catalog, and storage services.

## What’s new in Iceberg V3

Iceberg V3 introduces new capabilities and data types. Two key capabilities that address the challenges discussed earlier are deletion vectors and row lineage.

Deletion vectors replace positional delete files with an efficient binary format stored as [Puffin files](https://iceberg.apache.org/puffin-spec/). Instead of creating separate delete files for each delete operation, the deletion vector consolidates these delete references to a single delete vector per data file, rather than a delete reference file per deleted row. During query execution, engines efficiently filter out deleted rows using these compact vectors, maintaining query performance while removing the need to merge multiple delete files.

This avoids write amplification from random batch updates and GDPR compliance deletes, significantly reducing the overhead of maintaining fresh data. High-frequency update workloads can see immediate improvements in write performance and reduced storage costs from fewer small delete files. Additionally, having fewer small delete files reduces table maintenance costs for compaction operations.

Row lineage enables precise change tracking at the row level with full auditability. Row lineage adds metadata fields to each data file that track when rows were created and last modified. The `_row_id` field uniquely identifies each row, and the `_last_updated_sequence_number` field tracks the snapshot when the row was last modified. These fields enable efficient change tracking queries without scanning entire tables, and they’re automatically maintained by the Iceberg specification without requiring custom code.

Before row lineage, change tracking in Iceberg provided only the net changes between snapshots, making it difficult to track individual record modifications. Row lineage metadata fields can now be queried to return all incremental changes, giving you full fidelity for auditing data modifications and regulatory compliance. For data transformations, your downstream systems can process changes incrementally, speeding up data pipelines and reducing compute costs for change data capture (CDC) workflows. Row lineage is engine agnostic, interoperable, and built into the Iceberg V3 specification, alleviating the need for custom, engine-specific change tracking implementations.

## Real-world use cases

The new Iceberg V3 capabilities address critical challenges across multiple industries:

- **Marketing and advertising services organizations** – You can now efficiently handle GDPR right-to-be-forgotten requests and regulatory compliance deletes without the write amplification that previously degraded pipeline performance. Row lineage provides complete audit trails for data modifications, meeting strict regulatory requirements for data governance.
- **Ecommerce platforms processing millions of product updates and inventory changes daily** – You can maintain data freshness while reducing storage costs. Deletion vectors enable faster upsert operations, helping teams meet aggressive SLA requirements during peak shopping periods.
- **Healthcare and life sciences companies** – You can track patient data modifications with precision for compliance purposes while efficiently processing large-scale genomic datasets. Row lineage provides the detailed change history required for clinical trial audits and regulatory submissions.
- **Media and entertainment providers managing large catalogs of user viewing data** – You can efficiently process incremental changes for recommendation engines. Row lineage enables downstream analytics systems to process only changed records, reducing compute costs in incremental processing scenarios.

## Get started with Iceberg V3

To take advantage of deletion vectors for optimized writes and row lineage for built-in change tracking in Iceberg V3, set the table property `format-version = 3` during table creation. Alternatively, setting this property on an existing Iceberg V2 table atomically upgrades the table without data rewrites. Before creating or upgrading V3 tables, make sure the Iceberg engines in your solution are V3-compatible. Refer to [Apache Iceberg V3 on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/table-spec-v3.html) for more details.

### Create a new V3 table with Apache Spark on Amazon EMR 7.12

The following code creates a new table named `customer_data`. Setting the table property `format-version = 3` creates a V3 table. If the `format-version` table property is not explicitly set, a V2 table is created. V2 is currently the Iceberg default table version. Setting `write.delete.mode`, `write.update.mode`, and `write.merge.mode` to `merge-on-read` configures Spark to write deletion vectors for delete, update, or merge statements performed on the table.

```
CREATE TABLE customer_data (
customer_id bigint,
name string,
email string,
last_purchase timestamp,
total_spent decimal(10,2)
)
USING iceberg
TBLPROPERTIES (
'format-version' = '3',
'write.delete.mode' = 'merge-on-read',
'write.update.mode' = 'merge-on-read',
'write.merge.mode' = 'merge-on-read'
)
```

Run the following code to insert records into the `customer_data` table:

```
INSERT INTO customer_data VALUES
(1, 'Alejandro Rosalez', 'alejandro_rosalez@example.org', TIMESTAMP '2025-11-24 18:55:27', 42.97)
,(2, 'Akua Mansa', 'akua_mansa@example.org', TIMESTAMP '2025-11-24 17:55:27', 25.02)
,(3, 'Ana Carolina Silva','anacarolina_silva@example.org', TIMESTAMP '2025-11-24 16:55:27', 43.67)
,(4, 'Arnav Desai','arnav_desai@example.org', TIMESTAMP '2025-11-24 15:55:27', 98.32)
,(5, 'Carlos Salazar','carlos_salazar@example.org', TIMESTAMP '2025-11-24 12:55:27', 76.45)
```

Delete a record where `customer_id = 5` to generate a delete file:

```
DELETE
FROM customer_data
WHERE customer_id = 5
```

Updating a record with the following update statement also generates a delete file:

```
UPDATE customer_data
SET name = 'Mansa Akua'
WHERE customer_id = 2
```

The last part of this example queries the manifest’s metadata table to verify delete files were produced:

```
SELECT added_snapshot_id
,sum(added_delete_files_count) as added_delete_files_count
FROM customer_data.manifests
GROUP BY added_snapshot_id
ORDER BY added_snapshot_id
```

This query will result in three records returned, as shown in the following screenshot. The `added_delete_files_count` for the first snapshot that inserts records should be `0`. The next two snapshots for the corresponding delete and update statements should have `1` each for `added_delete_files_count` value.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/26/BDB-5676-1.png)

### Query row lineage for change tracking

Row lineage is automatically enabled on V3 tables. The following example includes row lineage metadata fields and an example of how to query table changes after a row lineage sequence number:

```
SELECT
customer_id,
name,
email,
_row_id,
_last_updated_sequence_number
FROM customer_data
WHERE _last_updated_sequence_number > 0
ORDER BY _last_updated_sequence_number, _row_id
```

Running this query after the previous insert, update, and delete statements returns four records, as shown in the following screenshot. The deleted record is removed. The `_last_updated_sequence_number` is `3` for the update to `customer_id = 2`.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/26/BDB-5676-2.png)

### Upgrade an existing V2 table

You can upgrade your existing V2 tables to V3 with the following command:

```
ALTER TABLE existing_customer_data
SET TBLPROPERTIES ('format-version' = '3')
```

When you upgrade a table from V2 to V3, several important operations occur atomically:

- A new metadata snapshot is created atomically, resulting in no data loss.
- Existing Parquet data files are reused without modification.
- Row-lineage fields (`_row_id` and `_last_updated_sequence_number`) are added to the table metadata.
- The next compaction operation will remove old V2 positional delete files. If new deletion vector files are generated before compaction runs, they will merge existing V2 positional delete files.
- New modifications will automatically use V3’s deletion vector files.
- The upgrade does not perform a historical backfill of row-lineage change tracking records.

The upgrade process is synchronous and completes in seconds for most tables. If the upgrade fails, an error message is returned immediately, and the table remains in its V2 state.

## Getting the most from Iceberg V3

In this section, we share the key things we’ve learned from customers already using these features.

### Know your workload pattern

Deletion vectors work best when you’re doing lots of writes, such as high-frequency updates, batch deletes, or CDC workloads making random non-append-only updates. If you’re writing more than you’re reading, deletion vectors will deliver immediate performance gains. To unlock these benefits, set your table to merge-on-read mode for delete, update, and merge operations.

### Let AWS handle compaction

Enable automatic compaction through the Data Catalog or use S3 Tables (on by default). You will get hands-free optimization without building custom maintenance jobs. Deletion vectors produce fewer delete files than positional deletes in Iceberg V2. Given a similar pattern and amount of modified records, V3 compaction should be quicker and cost less than V2.

### Understand the importance of row lineage when using the V2 changelog

With the Spark [changelog](https://iceberg.apache.org/docs/1.10.0/docs/spark-procedures/?h=changelog#change-data-capture) procedure in Iceberg V2, if a row gets inserted and then deleted between snapshots, it disappears from your change feed—you never see it. Iceberg V3 row lineage captures both operations because `_last_updated_sequence_number` updates on each modification. This full fidelity is important for audit trails and regulatory compliance where you need to prove what happened to every record. Performance-wise, the V2 changelog requires scanning and merging delete files to compute changes—that’s compute you’re paying for on every read. V3 row lineage stores metadata fields directly on each row, so filtering by `_last_updated_sequence_number` is a simple metadata scan.

### Test before you upgrade

Iceberg V3 upgrades are atomic and fast, but test in dev first. Make sure all your query engines support Iceberg V3 before upgrading shared tables—mixing V2 and V3 engines causes headaches. After upgrading, keep a few V2 snapshots around temporarily for time-travel queries while you validate performance.

## Conclusion

Iceberg V3 support across AWS analytics, catalog, and storage services marks a significant advancement in data lake capabilities. By combining deletion vectors’ write optimization with row lineage’s comprehensive change tracking, you can build more efficient, auditable, and cost-effective data lakes at scale. The seamless interoperability across AWS services makes sure your data lake architecture remains flexible and future-proof.

To learn more about AWS support for Iceberg V3, refer to [Using Apache Iceberg on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/table-spec-v3.html).

To learn more about building modern data lakes with Iceberg on AWS, refer to [Analytics on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/).

---

### About the authors

![Ron Ortloff](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/26/rortloff.jpg)

### Ron Ortloff

[Ron](https://www.linkedin.com/in/ron-ortloff/) is a Principal Product Manager at AWS.