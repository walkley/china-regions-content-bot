# Medidata’s journey to a modern lakehouse architecture on AWS

by Mike Araujo, Ashley Chen, Ian Beatty, and Sandeep Adwankar on 26 NOV 2025 in Amazon Kinesis, Amazon Managed Streaming for Apache Kafka (Amazon MSK), Amazon Simple Storage Service (S3), Analytics, AWS Glue, Case Study, Customer Solutions Permalink  Comments   Share

*This post was co-authored by Mike Araujo Principal Engineer at Medidata Solutions.*

The life sciences industry is transitioning from fragmented, standalone tools towards integrated, platform-based solutions. [Medidata](https://www.medidata.com/en/), a Dassault Systèmes company, is building a next-generation data platform that addresses the complex challenges of modern clinical research. In this post, we show you how Medidata created a unified, scalable, real-time data platform that serves thousands of clinical trials worldwide with AWS services, [Apache Iceberg](https://iceberg.apache.org/), and a modern lakehouse architecture.

## Challenges with legacy architecture

As the Medidata clinical data repository expanded, the team recognized the shortcomings of the legacy data solution to provide quality data products to their customers across their growing portfolio of data offerings. Several data tenants began to erode. The following diagram shows Medidata’s legacy extract, transform, and load (ETL) architecture.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/26/BDB-5644-1.png)

Built upon a series of scheduled batch jobs, the legacy system proved ill-equipped to provide a unified view of the data across the entire ecosystem. Batch jobs ran at different intervals, often requiring a sufficient degree of scheduling buffer to make sure upstream jobs completed within the expected window. As the data volume expanded, the jobs and their schedules continued to inflate, introducing a latency window between ingestion and processing for dependent consumers. Different consumers operating from various underlying data services further magnified the problem as pipelines had to be continuously built across a variety of data delivery stacks.

The expanding portfolio of pipelines began to overwhelm existing maintenance operations. With more operations, the opportunity for failure expanded and recovery efforts further complicated. Existing observability systems were inundated with operational data, and identifying the root cause of data quality issues became a multi-day endeavor. Increases in the data volume required scaling considerations across the entire data estate.

Additionally, the proliferation of data pipelines and copies of the data in different technologies and storage systems necessitated expanding access controls with enhanced security features to make sure only the correct users had access to the subset of data to which they were permitted. Making sure access control changes were correctly propagated across all systems added a further layer of complexity to consumers and producers.

## Solution overview

With the advent of Clinical Data Studio (Medidata’s unified data management and analytics solution for clinical trials) and Data Connect (Medidata’s data solution for acquiring, transforming, and exchanging electronic health record (EHR) data across healthcare organizations), Medidata introduced a new world of data discovery, analysis, and integration to the life sciences industry powered by open source technologies and hosted on AWS. The following diagram illustrates the solution architecture.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/26/BDB-5644-2.png)

Fragmented batch ETL jobs were replaced by real-time [Apache Flink](https://flink.apache.org/) streaming pipelines, an open source, distributed engine for stateful processing, and powered by [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS), a fully managed Kubernetes service. The Flink jobs write to Apache Kafka running in [Amazon Managed Apache Kafka](https://aws.amazon.com/msk/) (Amazon MSK), a streaming data service that manages Kafka infrastructure and operations, before landing in Iceberg tables backed by the [AWS Glue Data Catalog](https://aws.amazon.com/glue/), a centralized metadata repository for data assets. From this collection of Iceberg tables, a central, single source of data is now accessible from a variety of consumers without additional downstream processing, alleviating the need for custom pipelines to satisfy the requirements of downstream consumers. Through these fundamental architectural changes, the team at Medidata solved the issues presented by the legacy solution.

## Data availability and consistency

With the introduction of the Flink jobs and Iceberg tables, the team was able to deliver a consistent view of their data across the Medidata data experience. Pipeline latency was reduced from days to minutes, helping Medidata customers realize a 99% performance gain from the data ingestion to the data analytics layers. Due to Iceberg’s interoperability, Medidata users saw the same view of the data regardless of where they viewed that data, minimizing the need for consumer-driven custom pipelines because Iceberg could plug into existing consumers.

## Maintenance and durability

Iceberg’s interoperability provided a single copy of the data to satisfy their use cases, so the Medidata team could focus its observation and maintenance efforts on a five-times smaller subset of operations than previously required. Observability was enhanced by tapping into the various metadata components and metrics exposed by Iceberg and the Data Catalog. Quality management transformed from cross-system traces and queries to a single analysis of unified pipelines, with an added benefit of point in time data queries thanks to the [Iceberg snapshot feature](https://iceberg.apache.org/spec/#overview). Data volume increases are handled with out-of-box scaling supported by the entire infrastructure stack and AWS Glue Iceberg optimization features that include [compaction](https://docs.aws.amazon.com/glue/latest/dg/compaction-management.html), [snapshot retention](https://docs.aws.amazon.com/glue/latest/dg/snapshot-retention-management.html), and [orphan file deletion](https://docs.aws.amazon.com/glue/latest/dg/orphan-file-deletion.html), which provide a set-and-forget experience for solving a number of common Iceberg frustrations, such as the small file problem, orphan file retention, and query performance.

## Security

With Iceberg at the center of its solution architecture, the Medidata team no longer had to spend the time building custom access control layers with enhanced security features at each data integration point. Iceberg on AWS centralizes the authorization layer using familiar systems such as [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM), providing a single and durable control for data access. The data also stays entirely within the Medidata virtual private cloud (VPC), further reducing the opportunity for unintended disclosures.

## Conclusion

In this post, we demonstrated how legacy universe of consumer-driven custom ETL pipelines can be replaced with a scalable, high-performant streaming lakehouses. By putting Iceberg on AWS at the center of data operations, you can have a single source of data for your consumers.

To learn more about Iceberg on AWS, refer to [Optimizing Iceberg tables](https://docs.aws.amazon.com/glue/latest/dg/table-optimizers.html) and [Using Apache Iceberg on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.html).

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/27/mike.png)

### Mike Araujo

[Mike](https://www.linkedin.com/in/mike-araujo-200628112/) is a Principal Engineer at Medidata Solutions, working on building a next generation data and AI platform for clinical data and trials. By using the power of open source technologies such as Apache Kafka, Apache Flink, and Apache Iceberg, Mike and his team have enabled the delivery of billions of clinical events and data transformations in near real time to downstream consumers, applications, and AI agents. His core skills focus on architecting and building big data and ETL solutions at scale as well as their integration in agentic workflows.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2022/10/13/Sandeep.jpg)

### Sandeep Adwankar

[Sandeep](https://www.linkedin.com/in/adwankar/) is a Senior Product Manager at AWS, who has driven feature launches across Amazon SageMaker, AWS Glue, and AWS Lake Formation. He has led initiatives in Amazon S3 Tables analytics, Iceberg compaction strategies, and AWS Glue Iceberg optimizations. His recent work focuses on generative AI and autonomous systems, including the AWS Glue Data Catalog model context protocol and Amazon Bedrock structured knowledge bases. Based in the California Bay Area, he works with customers around the globe to translate business and technical requirements into products that accelerate their business outcomes.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/27/ibeatty.jpg)

### Ian Beatty

[Ian](https://www.linkedin.com/in/ian-beatty-02373459/) is a Technical Account Manager at AWS, where he specializes in supporting independent software vendor (ISV) customers in the healthcare and life sciences (HCLS) and financial services industry (FSI) sectors. Based in the Rochester, NY area, Ian helps ISV customers navigate their cloud journey by maintaining resilient and optimized workloads on AWS. With over a decade of experience building on AWS since 2014, he brings deep technical expertise from his previous roles as an AWS Architect and DevSecOps team lead for SaaS ISVs before joining AWS more than 3 years ago.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/27/ashchenn-1.jpg)

### Ashley Chen

[Ashley](https://www.linkedin.com/in/ashley-hy-chen/) is a Solutions Architect at AWS based in Washington D.C. She supports independent software vendor (ISV) customers in the healthcare and life sciences industries, focusing on customer enablement, generative AI applications, and container workloads.