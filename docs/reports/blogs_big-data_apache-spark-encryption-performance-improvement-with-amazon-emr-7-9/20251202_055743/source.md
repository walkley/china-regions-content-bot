# Apache Spark encryption performance improvement with Amazon EMR 7.9

by Sonu Kumar Singh, Roshin Babu, Polaris Jhandi, and Zheng Yuan on 26 NOV 2025 in Advanced (300), Amazon EMR, Announcements Permalink  Comments   Share

The [Amazon EMR](https://aws.amazon.com/emr) runtime for Apache Spark is a performance-optimized runtime for Apache Spark that is 100% API compatible with [open source Apache Spark](https://spark.apache.org/). With Amazon EMR release 7.9.0, the EMR runtime for Apache Spark introduces significant performance improvements for encrypted workloads, supporting Spark version 3.5.5.

For compliance and security requirements, many customers need to enable Apache Spark’s local storage encryption (`spark.io.encryption.enabled = true`) in addition to [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) encryption (such as server-side encryption (SSE) or [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms)). This feature encrypts shuffle files, cached data, and other intermediate data written to local disk during Spark operations, protecting sensitive data at rest on Amazon EMR cluster instances.

Industries subject to regulations such as the Health Insurance Portability and Accountability Act (HIPAA) for healthcare, Payment Card Industry Data Security Standard (PCI-DSS) for financial services, General Data Protection Regulation (GDPR) for personal data, and Federal Risk and Authorization Management Program (FedRAMP) for government often require encryption of all data at rest, including temporary files on local storage. While Amazon S3 encryption protects data in object storage, [Spark’s I/O encryption](https://spark.apache.org/docs/latest/security.html#encryption) secures the intermediate shuffle and spill data that Spark writes to local disk during distributed processing—data that never reaches Amazon S3 but might contain sensitive information extracted from source datasets. Generally, encrypted operations require additional computational overhead that can impact overall job performance.

With the built-in encryption optimizations of Amazon EMR 7.9.0, customers might see significant performance improvements in their Apache Spark applications without requiring any application changes. In our performance benchmark tests, derived from TPC-DS performance tests at 3 TB scale, we observed up to 20% faster performance with the EMR 7.9 optimized Spark runtime compared to Spark without these optimizations. Individual results may vary depending on specific workloads and configurations.

In this post, we analyze the results from our benchmark tests comparing the Amazon EMR 7.9 optimized Spark runtime against Spark 3.5.5 without encryption optimizations. We walk through a detailed cost analysis and provide step-by-step instructions to reproduce the benchmark.

## Results observed

To evaluate the performance improvements, we used an open source Spark performance test utility derived from the TPC-DS performance test toolkit. We ran the tests on two nine-node (eight core nodes and one primary node) r5d.4xlarge Amazon EMR 7.9.0 clusters, comparing two configurations:

- **Baseline**: EMR 7.9.0 cluster with a bootstrap action installing Spark 3.5.5 without encryption optimizations
- **Optimized**: EMR 7.9.0 cluster using the EMR Spark 3.5.5 runtime with encryption optimizations

Both tests used data stored in [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3). All data processing was configured identically except for the Spark runtime version.

To maintain benchmarking consistency and ensure a consistent, equivalent comparison, we disabled Dynamic Resource Allocation (DRA) in both test configurations. This approach eliminates variability from dynamic scaling and so we can measure pure computational performance improvements.

The following table shows the total job runtime for all queries (in seconds) in the 3 TB query dataset between the baseline and Amazon EMR 7.9 optimized configurations:

|  |  |  |  |
| --- | --- | --- | --- |
| **Configuration** | **Total runtime (seconds)** | **Geometric mean (seconds)** | **Performance improvement** |
| Baseline (Spark 3.5.5 without optimization) | 1,485 | 10.24 |  |
| EMR 7.9 (with encryption optimization) | 1,176 | 8.15 | 20% faster |

We observed that our TPC-DS tests with the Amazon EMR 7.9 optimized Spark runtime completed about 20% faster based on total runtime and 20% faster based on geometric mean compared to the baseline configuration.

The encryption optimizations in Amazon EMR 7.9 deliver performance benefits through:

- **Improved shuffle and decryption operations** reducing overhead during data exchange without compromising security
- **Better memory management** for intermediate results

## Cost analysis

The performance improvements of the Amazon EMR 7.9 optimized Spark runtime directly translate to lower costs. We realized an approximately 20% cost savings running the benchmark application with encryption optimizations compared to the baseline configuration, because of reduced hours of EMR, [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) and [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/) using General Purpose SSD (gp2).

The following table summarizes the cost comparison in the us-east-1 AWS Region:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Configuration** | **Runtime (hours)** | **Estimated cost** | **Total EC2 instances** | **Total vCPU** | **Total memory (GiB)** | **Root device (EBS)** |
| Baseline: Spark 3.5.5 without optimization, 1 primary and 8 core nodes | 0.41 | $5.28 | 9 | 144 | 1152 | 64 GiB gp2 |
| Amazon EMR 7.9 with optimization, 1 primary and 8 core nodes | 0.33 | $4.25 | 9 | 144 | 1152 | 64 GiB gp2 |

### Cost breakdown

**Formulas used:**

- **Amazon EMR cost** – Number of instances × EMR hourly rate × Runtime hours
- **Amazon EC2 cost** – Number of instances × EC2 hourly rate × Runtime hour)
- **Amazon EBS cost** – **(EBS cost per GB per month ÷ hours in a month) × EBS volume size × number of instances × runtime hours**

**Note**: EBS is [*priced monthly*](https://aws.amazon.com/ebs/pricing/) ($0.1 per GB per month), so we divide by 730 hours to convert to an hourly rate. EMR and EC2 are already priced hourly, so no conversion is needed.

**Baseline configuration (0.41 hours):**

- **Amazon EMR cost** – 9 × $0.27 × 0.41 = $1.00
- **Amazon EC2 cost** – 9 × $1.152 × 0.41 = $4.25
- **Amazon EBS cost** – ($0.1/730 × 64 × 9 × 0.41) = $0.032
- **Total cost** – $5.28

**EMR 7.9 optimized configuration (0.33 hours):**

- **Amazon EMR cost** – (9 × $0.27 × 0.33) = $0.80
- **Amazon EC2 cost** – (9 × $1.152 × 0.33) = $3.42
- **Amazon EBS cost** – ($0.1/730 × 64 × 9 × 0.33) = $0.025
- **Total cost: $4.25**

**Total cost savings:** 20% per benchmark run, which scales linearly with your production workload frequency.

## Set up EMR benchmarking

For detailed instructions and scripts, see the companion [GitHub repository](https://github.com/aws-samples/emr-spark-benchmark).

### Prerequisites

To set up Amazon EMR benchmarking, start by completing the following prerequisite steps:

1. Configure your [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli) by running `aws configure` to point to your benchmarking account,
2. Create an S3 bucket for test data and results.
3. Copy the TPC-DS 3TB source data from a publicly available dataset to your S3 bucket using the following command:

```
aws s3 cp s3://blogpost-sparkoneks-us-east-1/blog/BLOG_TPCDS-TEST-3T-partitioned s3://<YOUR-BUCKET-NAME>/BLOG_TPCDS-TEST-3T-partitioned --recursive
```

Replace `<YOUR-BUCKET-NAME>` with the name of the S3 bucket you created in step 2.
4. Build or download the benchmark application JAR file ([spark-benchmark-assembly-3.3.0.jar](https://aws-bigdata-blog.s3.amazonaws.com/artifacts/oss-spark-benchmarking/spark-benchmark-assembly-3.3.0.jar))
5. Ensure you have appropriate [AWS Identity Access Management (IAM)](https://aws.amazon.com/iam) roles for EMR cluster creation and Amazon S3 access

### Deploy the baseline EMR cluster (without optimization)

**Step 1: Launch EMR 7.9.0 cluster with bootstrap action**

The baseline configuration uses a bootstrap action to install Spark 3.5.5 without encryption optimizations. We have made the bootstrap script publicly available in an S3 bucket for your convenience.

Create the default Amazon EMR roles:

```
aws emr create-default-roles
```

Now create the cluster:

```
aws emr create-cluster \
--name "EMR-7.9-Baseline-Spark-3.5.5" \
--release-label emr-7.9.0 \
--applications Name=Spark \
--ec2-attributes SubnetId=<YOUR-SUBNET-ID>,InstanceProfile=EMR_EC2_DefaultRole  \
--service-role EMR_DefaultRole
--instance-groups \
InstanceGroupType=MASTER,InstanceCount=1,InstanceType=r5d.4xlarge \
InstanceGroupType=CORE,InstanceCount=8,InstanceType=r5d.4xlarge \
--bootstrap-actions \
Path=s3://spark-ba/install-spark-3-5-5-no-encryption.sh,Name="install spark 3.5.5 without encryption optimization" \
--use-default-roles \
--log-uri s3://<YOUR-BUCKET-NAME>/logs/baseline/
```

**Note**: The bootstrap script is available in a public S3 bucket at `s3://spark-ba/install-spark-3-5-5-no-encryption.sh`. This script installs Apache Spark 3.5.5 without the encryption optimizations present in the Amazon EMR runtime.

**Step 2: Submit the benchmark job to the baseline cluster**

Next submit the Spark job using the following commands:

```
aws emr add-steps \
--cluster-id <YOUR-BASELINE-CLUSTER-ID> \
--steps 'Type=Spark,Name="EMR-7.9-Baseline-Spark-3.5.5 Step",ActionOnFailure=CONTINUE,Args=["--deploy-mode","client","--conf","spark.io.encryption.enabled=false","--class","com.amazonaws.eks.tpcds.BenchmarkSQL","s3://<YOUR-BUCKET-NAME>/jar/spark-benchmark-assembly-3.3.0.jar","s3://<YOUR-BUCKET-NAME>/blog/BLOG_TPCDS-TEST-3T-partitioned","s3://<YOUR-BUCKET-NAME>/blog/BASELINE_TPCDS-TEST-3T-RESULT","/opt/tpcds-kit/tools","parquet","3000","3","false","q1-v2.4,q10-v2.4,q11-v2.4,q12-v2.4,q13-v2.4,q14a-v2.4,q14b-v2.4,q15-v2.4,q16-v2.4,q17-v2.4,q18-v2.4,q19-v2.4,q2-v2.4,q20-v2.4,q21-v2.4,q22-v2.4,q23a-v2.4,q23b-v2.4,q24a-v2.4,q24b-v2.4,q25-v2.4,q26-v2.4,q27-v2.4,q28-v2.4,q29-v2.4,q3-v2.4,q30-v2.4,q31-v2.4,q32-v2.4,q33-v2.4,q34-v2.4,q35-v2.4,q36-v2.4,q37-v2.4,q38-v2.4,q39a-v2.4,q39b-v2.4,q4-v2.4,q40-v2.4,q41-v2.4,q42-v2.4,q43-v2.4,q44-v2.4,q45-v2.4,q46-v2.4,q47-v2.4,q48-v2.4,q49-v2.4,q5-v2.4,q50-v2.4,q51-v2.4,q52-v2.4,q53-v2.4,q54-v2.4,q55-v2.4,q56-v2.4,q57-v2.4,q58-v2.4,q59-v2.4,q6-v2.4,q60-v2.4,q61-v2.4,q62-v2.4,q63-v2.4,q64-v2.4,q65-v2.4,q66-v2.4,q67-v2.4,q68-v2.4,q69-v2.4,q7-v2.4,q70-v2.4,q71-v2.4,q72-v2.4,q73-v2.4,q74-v2.4,q75-v2.4,q76-v2.4,q77-v2.4,q78-v2.4,q79-v2.4,q8-v2.4,q80-v2.4,q81-v2.4,q82-v2.4,q83-v2.4,q84-v2.4,q85-v2.4,q86-v2.4,q87-v2.4,q88-v2.4,q89-v2.4,q9-v2.4,q90-v2.4,q91-v2.4,q92-v2.4,q93-v2.4,q94-v2.4,q95-v2.4,q96-v2.4,q97-v2.4,q98-v2.4,q99-v2.4,ss_max-v2.4","true"]'
```

### Deploy the optimized EMR cluster (with encryption optimization)

**Step 1: Launch EMR 7.9.0 cluster with Spark runtime**

The optimized configuration uses the EMR 7.9.0 Spark runtime without any bootstrap actions:

```
aws emr create-cluster \
--name "EMR-7.9-Optimized-Native-Spark" \
--release-label emr-7.9.0 \
--applications Name=Spark \
--ec2-attributes SubnetId=<YOUR-SUBNET-ID>,InstanceProfile=EMR_EC2_DefaultRole \
--service-role EMR_DefaultRole
--instance-groups \
InstanceGroupType=MASTER,InstanceCount=1,InstanceType=r5d.4xlarge \
InstanceGroupType=CORE,InstanceCount=8,InstanceType=r5d.4xlarge \
--use-default-roles \
--log-uri s3://<YOUR-BUCKET-NAME>/logs/optimized/
```

Example:

```
aws emr create-cluster \
--name "EMR-7.9-Optimized-Native-Spark" \
--release-label emr-7.9.0 \
--applications Name=Spark \
--ec2-attributes SubnetId=subnet-08a5f71f92bc8a801 \
--instance-groups \
InstanceGroupType=MASTER,InstanceCount=1,InstanceType=r5d.4xlarge \
InstanceGroupType=CORE,InstanceCount=8,InstanceType=r5d.4xlarge \
--bootstrap-actions \
Path=s3://spark-ba/install-spark-3-5-5-no-encryption.sh,Name="install spark 3.5.5 without encryption optimization" \
--use-default-roles \
--log-uri s3://aws-logs-123456789012-us-west-2/elasticmapreduce/
```

**Step 2: Submit the benchmark job to optimized cluster**

ext submit the Spark job using the following commands:

```
aws emr add-steps \
--cluster-id <YOUR-OPTIMIZED-CLUSTER-ID> \
--steps 'Type=Spark,Name="EMR-7.9-Optimized-Native-Spark Step",ActionOnFailure=CONTINUE,Args=["--deploy-mode","client","--conf","spark.io.encryption.enabled=true","--class","com.amazonaws.eks.tpcds.BenchmarkSQL","s3://<YOUR-BUCKET-NAME>/jar/spark-benchmark-assembly-3.3.0.jar","s3://<YOUR-BUCKET-NAME>/blog/BLOG_TPCDS-TEST-3T-partitioned","s3://<YOUR-BUCKET-NAME>/blog/BASELINE_TPCDS-TEST-3T-RESULT","/opt/tpcds-kit/tools","parquet","3000","3","false","q1-v2.4,q10-v2.4,q11-v2.4,q12-v2.4,q13-v2.4,q14a-v2.4,q14b-v2.4,q15-v2.4,q16-v2.4,q17-v2.4,q18-v2.4,q19-v2.4,q2-v2.4,q20-v2.4,q21-v2.4,q22-v2.4,q23a-v2.4,q23b-v2.4,q24a-v2.4,q24b-v2.4,q25-v2.4,q26-v2.4,q27-v2.4,q28-v2.4,q29-v2.4,q3-v2.4,q30-v2.4,q31-v2.4,q32-v2.4,q33-v2.4,q34-v2.4,q35-v2.4,q36-v2.4,q37-v2.4,q38-v2.4,q39a-v2.4,q39b-v2.4,q4-v2.4,q40-v2.4,q41-v2.4,q42-v2.4,q43-v2.4,q44-v2.4,q45-v2.4,q46-v2.4,q47-v2.4,q48-v2.4,q49-v2.4,q5-v2.4,q50-v2.4,q51-v2.4,q52-v2.4,q53-v2.4,q54-v2.4,q55-v2.4,q56-v2.4,q57-v2.4,q58-v2.4,q59-v2.4,q6-v2.4,q60-v2.4,q61-v2.4,q62-v2.4,q63-v2.4,q64-v2.4,q65-v2.4,q66-v2.4,q67-v2.4,q68-v2.4,q69-v2.4,q7-v2.4,q70-v2.4,q71-v2.4,q72-v2.4,q73-v2.4,q74-v2.4,q75-v2.4,q76-v2.4,q77-v2.4,q78-v2.4,q79-v2.4,q8-v2.4,q80-v2.4,q81-v2.4,q82-v2.4,q83-v2.4,q84-v2.4,q85-v2.4,q86-v2.4,q87-v2.4,q88-v2.4,q89-v2.4,q9-v2.4,q90-v2.4,q91-v2.4,q92-v2.4,q93-v2.4,q94-v2.4,q95-v2.4,q96-v2.4,q97-v2.4,q98-v2.4,q99-v2.4,ss_max-v2.4","true"]'
```

### Benchmark command parameters explained

The Amazon EMR Spark step uses the following parameters:

- **EMR step configuration:**
- **Type=Spark**: Specifies this is a Spark application step
- **Name=”EMR-7.9-Baseline-Spark-3.5.5″**: Human-readable name for the step
- **ActionOnFailure=CONTINUE**: Continue with other steps if this one fails
- **Spark submit arguments:**
- **–deploy-mode client**: Run the driver on the master node (not cluster mode)
- **–class com.amazonaws.eks.tpcds.BenchmarkSQL**: Main class for the TPC-DS benchmark
- **Application parameters:**
- **JAR file**: `s3://<YOUR-BUCKET-NAME>/jar/spark-benchmark-assembly-3.3.0.jar`
- **Input data**`: s3://<YOUR-BUCKET-NAME>/blog/BLOG_TPCDS-TEST-3T-partitioned` (3 TB TPC-DS dataset)
- **Output location**: `s3://<YOUR-BUCKET-NAME>/blog/BASELINE_TPCDS-TEST-3T-RESULT` (S3 path for results)
- **TPC-DS tools path**: `/opt/tpcds-kit/tools`(local path on EMR nodes)
- **Format**: `parquet` (output format)
- **Scale factor**: `3000` (3 TB dataset size)
- **Iterations**: `3` (run each query 3 times for averaging)
- **Collect results**: false (don’t collect results to driver)
- **Query list**: `"q1-v2.4,q10-v2.4,...,ss_max-v2.4"` (all 104 TPC-DS queries)
- **Final parameter**: `true` (enable detailed logging and metrics)
- **Query coverage:**
- All 104 standard TPC-DS benchmark queries (`q1-v2.4` through `q99-v2.4`)
- Plus the `ss_max-v2.4` query for additional testing
- Each query runs 3 times to calculate average performance

### Summarize the results

1. Download the test result files from both output S3 locations:

```
# Baseline results
aws s3 cp s3://<YOUR-BUCKET-NAME>/blog/BASELINE_TPCDS-TEST-3T-RESULT/timestamp=xxxx/summary.csv/xxx.csv ./baseline-results.csv

# Optimized results
aws s3 cp s3://<YOUR-BUCKET-NAME>/blog/OPTIMIZED_TPCDS-TEST-3T-RESULT/timestamp=xxxx/summary.csv/xxx.csv ./optimized-results.csv
```
2. The CSV files contain four columns (without headers):
- Query name
- Median time (seconds)
- Minimum time (seconds)
- Maximum time (seconds)
3. Calculate performance metrics for comparison:
- **Average time per query**: `AVERAGE(median, min, max)` for each query
- **Total runtime**: Sum of all median times
- **Geometric mean**: `GEOMEAN(average times)` across all queries
- **Speedup**: Calculate the ratio between baseline and optimized for each query
4. Create comparison analysis:`Speedup = (Baseline Time - Optimized Time) / Baseline Time * 100%`

## Testing configuration details

The following table summarizes the test environment used for this post:

|  |  |
| --- | --- |
| **Parameter** | **Value** |
| **EMR release** | emr-7.9.0 (both configurations) |
| **Baseline Spark version** | 3.5.5 (installed through bootstrap action) |
| **Baseline bootstrap script** | s3://spark-ba/install-spark-3-5-5-no-encryption.sh (public) |
| **Optimized spark version** | Amazon EMR Spark runtime |
| **Cluster size** | 9 nodes (1 primary and 8 core) |
| **Instance type** | r5d.4xlarge |
| **vCPUs per node** | 16 |
| **Memory per node** | 128 GB |
| **Instance storage** | 600 GB SSD |
| **EBS volume** | 64 GB gp2 (2 volumes per instance) |
| **Total vCPUs** | 144 (9 × 16) |
| **Total memory** | 1152 GB (9 × 128) |
| **Dataset** | TPC-DS 3TB (Parquet format) |
| **Queries** | 104 queries (TPC-DS v2.4) |
| **Iterations** | 3 runs per query |
| **DRA** | Disabled for consistent benchmarking |

## Clean up

To avoid incurring future charges, delete the resources you created:

1. **Terminate both EMR clusters:**

```
aws emr terminate-clusters --cluster-ids <YOUR-BASELINE-CLUSTER-ID> <YOUR-OPTIMIZED-CLUSTER-ID>
```
2. **Delete S3 test results** if no longer needed:

```
aws s3 rm s3://<YOUR-BUCKET-NAME>/blog/BASELINE_TPCDS-TEST-3T-RESULT/ --recursive
aws s3 rm s3://<YOUR-BUCKET-NAME>/blog/OPTIMIZED_TPCDS-TEST-3T-RESULT/ --recursive
aws s3 rm s3://<YOUR-BUCKET-NAME>/logs/ --recursive
```
3. **Remove IAM roles** if created specifically for testing

### Key findings

- **Up to 20% performance improvement** using the Amazon EMR 7.9’s Spark runtime with no code changes required
- **20% cost savings** because of reduced runtime
- **Significant gains** for shuffle-heavy, join-intensive workloads
- **100% API compatibility** with open source Apache Spark
- **Simple migration** from custom Spark builds to EMR runtime
- **Easy benchmarking** using publicly available bootstrap scripts

## Conclusion

You can run your Apache Spark workloads up to 20% faster and at lower cost without making any changes to your applications by using the Amazon EMR 7.9.0 optimized Spark runtime. This improvement is achieved through numerous optimizations in the EMR Spark runtime, including enhanced encryption handling, improved data serialization, and optimized shuffle operations.

To learn more about Amazon EMR 7.9 and best practices, see the [EMR documentation](https://docs.aws.amazon.com/emr/). For configuration guidance and tuning advice, subscribe to the [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/category/big-data/).

**Related resources:**

- [EMR 7.x Migration Guide](https://d1.awsstatic.com/whitepapers/amazon_emr_migration_guide.pdf)
- [EMR Release Guide](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/)
- [Best Practices for EMR](https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-emr-hardware/best-practices.html)

If you’re running Spark workloads on Amazon EMR today, we encourage you to test the EMR 7.9 Spark runtime with your production workloads and measure the improvements specific to your use case.

---

### About the authors

![Sonu Kumar Singh](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/27/BDB-5446-1.jpeg)

### Sonu Kumar Singh

[Sonu](https://www.linkedin.com/in/singh-sonukumar/) is a Senior Solutions Architect with more than 13 years of experience, with a specialization in Analytics and Healthcare domain. He has been instrumental in catalyzing transformative shifts in organizations by enabling data-driven decision-making thereby fueling innovation and growth. He enjoys it when something he designed or created brings a positive impact.

![Roshin Babu](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/27/BDB-5446-3.png)

### Roshin Babu

[Roshin](https://www.linkedin.com/in/roshinbabu/) is a Sr. Specialist Solutions architect at AWS, where he collaborates with the sales team to support public sector clients. His role focuses on developing innovative solutions that solve complex business challenges while driving increased adoption of AWS analytics services. When he’s not working, Roshin is passionate about exploring new destinations, discovering great food, and enjoying soccer both as a player and fan.Polaris Jhandi

![Polaris Jhandi](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/27/BDB-5446-4.png)

### Polaris Jhandi

[Polaris](https://www.linkedin.com/in/polarisjhandi/) is a Cloud Application Architect with AWS Professional Services. He has a background in AI/ML and big data. He is currently working with customers to migrate their legacy mainframe applications to the AWS Cloud.Zheng Yuan

![Zheng Yuan](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/27/BDB-5446-5.jpeg)

### Zheng Yuan

[Zheng](https://www.linkedin.com/in/zheng-yuan-3a1538122/) is a Software Engineer on the Amazon EMR Spark team, where he focuses on improving the performance of the Spark execution engine across various use cases.