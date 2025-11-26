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

## [AWS News Blog](https://aws.amazon.com/blogs/aws/)

# Amazon Aurora DSQL, the fastest serverless distributed SQL database is now generally available

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 27 MAY 2025 in [Amazon Aurora](https://aws.amazon.com/blogs/aws/category/database/amazon-aurora/ "View all posts in Amazon Aurora"), [Database](https://aws.amazon.com/blogs/aws/category/database/ "View all posts in Database"), [DSQL](https://aws.amazon.com/blogs/aws/category/database/amazon-aurora/dsql/ "View all posts in DSQL"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/amazon-aurora-dsql-is-now-generally-available/)  [Comments](https://aws.amazon.com/blogs/aws/amazon-aurora-dsql-is-now-generally-available/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing the general availability of [Amazon Aurora DSQL](https://aws.amazon.com/rds/aurora/dsql/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), the fastest serverless distributed SQL database with virtually unlimited scale, the highest availability, and zero infrastructure management for always available applications. You can remove the operational burden of patching, upgrades, and maintenance downtime and count on an easy-to-use developer experience to create a new database in a few quick steps.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/13/2025-aurora-dsql-1-werner-keynote-1.jpg)When we introduced the [preview of Aurora DSQL](https://aws.amazon.com/blogs/database/introducing-amazon-aurora-dsql/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) at AWS re:Invent 2024, our customers were excited by this innovative solution to simplify complex relational database challenges. In his keynote, Dr. Werner Vogels, CTO of Amazon.com, talked about managing complexity upfront in the design of Aurora DSQL. Unlike most traditional databases, Aurora DSQL is disaggregated into multiple independent components such as a query processor, adjudicator, journal, and crossbar.

These components have high cohesion, communicate through well-specified APIs, and scale independently based on your workloads. This architecture enables multi-Region strong consistency with low latency and globally synchronized time. To learn more about how Aurora DSQL works behind the scenes, watch [Dr. Werner Vogels’ keynote](https://youtu.be/aim5x73crbM?si=Ur3aLJQdxnsL6RmC&t=5162) and read about [an Aurora DSQL story](https://www.allthingsdistributed.com/2025/05/just-make-it-scale-an-aurora-dsql-story.html).

**The architecture of Amazon Aurora DSQL**

Your application can use the fastest distributed SQL reads and writes and scale to meet any workload demand without any database sharding or instance upgrades. With Aurora DSQL, its active-active distributed architecture is designed for 99.99 percent availability in a single Region and 99.999 percent availability across multiple Regions. This means your applications can continue to read and write with strong consistency, even in the rare case an application is unable to connect to a Region cluster endpoint.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/13/2025-aurora-dsql-2-architecture.jpg)

In a single-Region configuration, Aurora DSQL commits all write transactions to a distributed transaction log and synchronously replicates all committed log data to user storage replicas in three Availability Zones. Cluster storage replicas are distributed across a storage fleet and automatically scale to ensure optimal read performance.

Multi-Region clusters provide the same resilience and connectivity as single-Region clusters while improving availability through two Regional endpoints, one for each peered cluster Region. Both endpoints of a peered cluster present a single logical database and support concurrent read and write operations with strong data consistency. A third Region acts as a log-only witness which means there is is no cluster resource or endpoint. This means you can balance applications and connections for geographic locations, performance, or resiliency purposes, making sure readers consistently see the same data.

Aurora DSQL is an ideal choice to support applications using microservices and event-driven architectures, and you can design highly scalable solutions for industries such as banking, ecommerce, travel, and retail. It’s also ideal for multi-tenant software as a service (SaaS) applications and data-driven services like payment processing, gaming platforms, and social media applications that require multi-Region scalability and resilience.

**Getting started with Amazon Aurora DSQL**

Aurora DSQL provides a easy-to-use experience, starting with a simple console experience. You can use familiar SQL clients to leverage existing skillsets, and integration with other AWS services to improve managing databases.

To create an Aurora DSQL cluster, go to the [Aurora DSQL console](https://console.aws.amazon.com/dsql/clusters/home?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and choose **Create cluster**. You can choose either **Single-Region** or **Multi-Region** configuration options to help you establish the right database infrastructure for your needs.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/16/2025-aurora-dsql-3-1-create-single-cluster.jpg)

**1. Create a single-Region cluster**

To create a single-Region cluster, you only choose **Create cluster**. That’s all.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/16/2025-aurora-dsql-3-1-create-single-cluster.png)

In a few minutes, you’ll see your Aurora DSQL cluster created. To connect your cluster, you can use your favorite SQL client such as [PostgreSQL interactive terminal](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/getting-started.html#accessing-sql-clients-psql),  [DBeaver](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/getting-started.html#accessing-sql-clients-dbeaver), [JetBrains DataGrip](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/getting-started.html#accessing-sql-clients-datagrip), or you can take [various programmable approaches](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/programming-with.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) with a database endpoint and authentication token as a password.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/16/2025-aurora-dsql-3-1-list-single-cluster.png)

To get the authentication token, choose **Connect** and **Get Token** in your cluster detail page. Copy the endpoint from **Endpoint (Host)** and the generated authentication token after **Connect as admin** is chosen in the **Authentication token (Password)** section.

Then, choose **Open in CloudShell**, and with a few clicks, you can seamlessly connect to your cluster.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/16/2025-aurora-dsql-4-connect-cluster.png)

After you connect the Aurora DSQL cluster, test your cluster by running [sample SQL statements](https://github.com/aws-samples/aurora-dsql-samples/tree/main/quickstart_data). You can also query SQL statements for your applications using [your favorite programming languages](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/aws-sdks.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el): Python, Java, JavaScript, C++, Ruby, .NET, Rust, and Golang. You can build sample applications using a Django, Ruby on Rails, and AWS Lambda application to interact with Amazon Aurora DSQL.

**2. Create a multi-Region cluster**

To create a multi-Region cluster, you need to add the other cluster’s [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) to peer the clusters.

To create the first cluster, choose **Multi-Region** in the console. You will also be required to choose the **Witness Region**, which receives data written to any peered Region but doesn’t have an endpoint. Choose **Create cluster**. If you already have a remote Region cluster, you can optionally enter its ARN.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/16/2025-aurora-dsql-3-1-create-cluster.png)

Next, add an existing remote cluster or create your second cluster in another Region by choosing **Create cluster**.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/16/2025-aurora-dsql-3-1-create-multi-cluster.png)

Now, you can create the second cluster with your peer cluster ARN as the first cluster.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/16/2025-aurora-dsql-3-1-create-peer-cluster-1.png)

When the second cluster is created, you must peer the cluster in `us-east-1` in order to complete the multi-Region creation.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/16/2025-aurora-dsql-3-1-peering-clusters.png)

Go to the first cluster page and choose **Peer** to confirm cluster peering for both clusters.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/16/2025-aurora-dsql-3-1-peering-clusters-2.png)

Now, your multi-Region cluster is created successfully. You can see details about the peers that are in other Regions in the **Peers** tab.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/16/2025-aurora-dsql-3-1-peering-clusters-3.png)

To get hands-on experience with Aurora DSQL, you can use this [step-by-step workshop](https://catalog.workshops.aws/aurora-dsql/). It walks through the architecture, key considerations, and best practices as you build a sample retail rewards point application with active-active resiliency.

You can use the [AWS SDKs](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/programming-with-sdk-crud.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [AWS Comand Line Interface (AWS CLI)](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/programming-with-cli-crud.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and [Aurora DSQL APIs](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/CHAP_api_reference.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) to create and manage Aurora DSQL programmatically. To learn more, visit [Setting up Aurora DSQL clusters](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/setting-up-dsql.html) in the Amazon Aurora DSQL User Guide.

**What did we add after the preview?** We used your feedback and suggestions during the preview period to add new capabilities. We’ve highlighted a few of the new features and capabilities:

* **Console experience** –We improved your cluster management experience to create and peer multi-Region clusters as well as easily connect using AWS CloudShell.
* **PostgreSQL features** – We added support for views, unique secondary indexes for tables with existing data and launched Auto-Analyze which removes the need to manually maintain accurate table statistics. Learn about Aurora DSQL [PostgreSQL-compatible](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-postgresql-compatibility.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) features.
* **Integration with AWS services** –We integrated various AWS services such as [AWS Backup](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for a full snapshot backup and Aurora DSQL cluster restore, [AWS PrivateLink](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/privatelink-managing-clusters.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for private network connectivity, [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DSQL.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for managing Aurora DSQL resources, and [AWS CloudTrail](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/logging-using-cloudtrail.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for logging Aurora DSQL operations.

Aurora DSQL now provides a Model Context Protocol (MCP) server to improve developer productivity by making it easy for your generative AI models and database to interact through natural language. For example, install [Amazon Q Developer CLI](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and configure [Aurora DSQL MCP server](https://awslabs.github.io/mcp/servers/aurora-dsql-mcp-server). Amazon Q Developer CLI now has access to an Aurora DSQL cluster. You can easily explore the schema of your database, understand the structure of the tables, and even execute complex SQL queries, all without having to write any additional integration code.

**Now available** Amazon Aurora DSQL is available today in the AWS US East (N. Virginia), US East (Ohio), US West (Oregon) Regions for single- and multi-Region clusters (two peers and one witness Region), Asia Pacific (Osaka) and Asia Pacific (Tokyo) for single-Region clusters, and Europe (Ireland), Europe (London), and Europe (Paris) for single-Region clusters.

You’re billed on a monthly basis using a single normalized billing unit called Distributed Processing Unit (DPU) for all request-based activity such as read/write. Storage is based on the total size of your database and measured in GB-months. You are only charged for one logical copy of your data per single-Region cluster or multi-Region peered cluster. As a part of the AWS Free Tier, your first 100,000 DPUs and 1 GB-month of storage each month is free. To learn more, visit [Amazon Aurora DSQL Pricing](https://aws.amazon.com/rds/aurora/dsql/pricing/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

Give Aurora DSQL a try for free in the [Aurora DSQL console](https://console.aws.amazon.com/dsql/clusters/home?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). For more information, visit the [Aurora DSQL User Guide](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/what-is-aurora-dsql.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and send feedback to [AWS re:Post for Aurora DSQL](https://repost.aws/tags/TAqcUIxZXVTL6iyn1gF_ugSQ) or through your usual AWS support contacts.

— [Channy](https://twitter.com/channyun)

![Channy Yun (윤석찬)](https://d2908q01vomqb2.cloudfront.net/7b52009b64fd0a2a49e6d8a939753077792b0554/2020/06/05/channyun_400x400.jpg)

### [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)")

Channy is a Lead Blogger of AWS News Blog and Principal Developer Advocate for AWS Cloud. As an open web enthusiast and blogger at heart, he loves community-driven learning and sharing of technology.

Loading comments…

### Resources

* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [What's New](https://aws.amazon.com/new?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [Top Posts](https://aws.amazon.com/blogs?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [Official AWS Podcast](https://aws.amazon.com/podcasts/aws-podcast?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [Case Studies](https://aws.amazon.com/solutions/case-studies?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [AWS re:Post](https://repost.aws/ "https://repost.aws/")

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [RSS Feed](https://aws.amazon.com/blogs/aws/feed/)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-social)

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