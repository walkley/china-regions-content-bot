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

# Introducing Oracle Database@AWS for simplified Oracle Exadata migrations to the AWS Cloud

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 08 JUL 2025 in [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS Marketplace](https://aws.amazon.com/blogs/aws/category/software/aws-marketplace/ "View all posts in AWS Marketplace"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Oracle Database@AWS](https://aws.amazon.com/blogs/aws/category/database/oracle-database-at-aws/ "View all posts in Oracle Database@AWS") [Permalink](https://aws.amazon.com/blogs/aws/introducing-oracle-databaseaws-for-simplified-oracle-exadata-migrations-to-the-aws-cloud/)  [Comments](https://aws.amazon.com/blogs/aws/introducing-oracle-databaseaws-for-simplified-oracle-exadata-migrations-to-the-aws-cloud/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing the general availability of [Oracle Database@AWS](https://aws.amazon.com/marketplace/featured-seller/oracle/), a new offering for Oracle Exadata workloads, including Oracle Real Application Clusters (RAC) within AWS.

In the past 14 years, customers had the choice of self-managing Oracle database workloads in the cloud using [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2) or using fully managed [Amazon Relational Database Service (Amazon RDS) for Oracle](https://aws.amazon.com/rds/oracle/). Now, you have an additional option for your workloads that require Oracle RAC or Oracle Exadata for quicker and simpler migrations to the cloud. You also get a single invoice through AWS Marketplace, which counts towards AWS commitments and Oracle license benefits, including Bring Your Own License (BYOL) and discount programs such as Oracle Support Rewards.

With Oracle Database@AWS, you can migrate your Oracle Exadata workloads to Oracle Exadata Database Service on Dedicated Infrastructure or Oracle Autonomous Database on Dedicated Exadata Infrastructure within AWS with minimal changes. You can purchase, provision, and manage your Oracle Database@AWS deployments through familiar AWS tools and interfaces such as [AWS Management Console](https://console.aws.amazon.com), [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli), or [AWS APIs](https://aws.amazon.com/developer/tools/) for applications running on AWS. The AWS APIs call the corresponding Oracle Cloud Infrastructure (OCI) APIs necessary to provision and manage the resources.

Since its [preview](https://aws.amazon.com/about-aws/whats-new/2024/12/oracle-database-aws-limited-preview/) last December, we’ve improved or added features to help run production workloads at general availability:

* **Regional expansion** – You can now use Oracle Database@AWS in the U.S. East (N. Virginia) and U.S. West (Oregon) Regions today. We are also announcing plans to expand to 20 AWS Regions globally. This broader availability supports the diverse needs of our customers across various geographical areas so more enterprises can benefit from this option. You can choose from different Exadata system sizes to match your workload requirements in your AWS Region.
* **Zero-ETL and S3 backups** – You can now benefit from [zero-ETL integration](https://aws.amazon.com/what-is/zero-etl/) with [Amazon Redshift](https://aws.amazon.com/redshift) for analytics to remove the need to build and manage data pipelines for extract, transform, and load operations. With zero-ETL, you can unify your data on AWS without incurring cross network data transfer costs. We’re providing [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3) backups with up to eleven nines of data durability.
* **Autonomous VM cluster** – You can now provision an Autonomous VM Cluster in addition to an Exadata VM cluster on the Exadata Dedicated Infrastructure. You can run Oracle Autonomous Database on Dedicated Exadata Infrastructure, a fully managed database environment using committed hardware and software resources.

Oracle Database@AWS also integrates with other AWS services such as [Amazon Virtual Private Cloud (Amazon VPC) Lattice](https://aws.amazon.com/vpc) for configuring network paths to AWS services such as S3 and Redshift directly, [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam) for authentication and authorization, [Amazon EventBridge](https://aws.amazon.com/eventbridge/) for monitoring database lifecycle events, [AWS CloudFormation](https://aws.amazon.com/cloudformation) for infrastructure automation, [Amazon CloudWatch](https://aws.amazon.com/cloudwatch) for collecting and monitoring metrics, and [AWS CloudTrail](https://aws.amazon.com/cloudtrail) for logging API operations.

**Getting started with Oracle Database@AWS**

Oracle Database@AWS supports two key services: Oracle Exadata Database Service on Dedicated Infrastructure and Oracle Autonomous Database on Dedicated Exadata Infrastructure within AWS data centers.

These services physically reside within an Availability Zone in an AWS Region and logically reside in an OCI region, enabling seamless integration with AWS services through high-speed, low-latency connections.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/23/2025-odb-aws-1-how-it-works.jpg)

You create an ODB network, a private, isolated network that hosts Oracle Exadata VM Clusters within an Availability Zone. Then, you use ODB peering accessible to EC2 application servers running in a VPC. To learn more, visit [How Oracle Database@AWS works](https://docs.aws.amazon.com/odb/latest/UserGuide/how-it-works.html) in the AWS documentation.

**Request a private offer in AWS Marketplace**

To begin your journey with Oracle Database@AWS, visit the [AWS console](https://console.aws.amazon.com/odb/home) or request the [AWS Marketplace private offer](https://aws.amazon.com/marketplace/pp/prodview-qks5dl3hr7nfw). Your AWS and Oracle sales team will receive your request, then contact you to find the best option for your workloads, and activate your account.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/23/2025-odb-aws-2-private-offer.jpg)

When you activate and get access to Oracle Database@AWS, you can use the **Dashboard** to create an ODB network, Exadata infrastructure, and Exadata VM cluster or Autonomous VM cluster, and ODB peering connection.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/23/2025-odb-aws-3-dashboard.jpg)

To learn more, visit the [Onboarding to Oracle Database@AWS](https://docs.aws.amazon.com/odb/latest/UserGuide/setting-up.html) and [AWS Marketplace buyer private offers](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-private-offers.html) in the AWS documentation.

**Create an ODB network**

An ODB network is a private isolated network that hosts OCI infrastructure on AWS. The ODB network maps directly to the network that exists within the OCI child site, thus serving as the means of communication between AWS and OCI.

In the **Dashboard**, choose **Create ODB network**, enter a network name, choose the Availability Zone, and specify a CIDR ranges for client connections established by applications and backup connections used for taking automated backups. You can also enter a name to use as a prefix to your domain fixed as `oraclevcn.com`. For example, if you enter `myhost`, the fully qualified domain name is `myhost.oraclevcn.com`.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/23/2025-odb-aws-2-create-odb-network.jpg)

Optionally, you can configure ODB network access to perform automated backups to Amazon S3 and zero-ETL for near real-time analytics and ML on your Oracle data using Amazon Redshift.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/23/2025-odb-aws-2-create-odb-network-integrations.jpg)

After you create your ODB network, update your VPC route tables of your EC2 application servers with the client connection CIDR in the ODB network. To learn more, visit [ODB network](https://docs.aws.amazon.com/odb/latest/UserGuide/how-it-works.html#how-it-works.odb-network), [ODB peering](https://docs.aws.amazon.com/odb/latest/UserGuide/how-it-works.html#how-it-works.peering), and [Configuring VPC route tables for ODB peering](https://docs.aws.amazon.com/odb/latest/UserGuide/configuring.html#configure-routes) in the AWS documentation.

**Create Exadata infrastructure**

The Oracle Exadata infrastructure is the underlying architecture of your database servers, storage servers, and networking that run your Oracle Exadata databases.

Choose **Create Exadata infrastructure**, enter a name, and use the default Availability Zone. In the next step, you can choose `Exadata.X11M` for the Exadata system model. You can also set a default of 2 or up to 32 database servers and 3 or up to 64 storage servers with 80 TB storage capacity per server.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/23/2025-odb-aws-3-create-exadata-intra.jpg)

Finally, you can configure system maintenance preferences, such as scheduling, patching mode, and OCI maintenance notification contacts. You can’t modify an infrastructure after you create it from the AWS console. But, you can navigate to the OCI console and modify it.

To delete an Exadata infrastructure, visit [Deleting an Oracle Exadata infrastructure in Oracle Database@AWS](https://docs.aws.amazon.com/odb/latest/UserGuide/managing.html#deleting_infra) in the AWS documentation.

**Create an Exadata VM cluster or Autonomous VM cluster**

You can create VM clusters on Exadata infrastructure and deploy multiple VM clusters with different Oracle Exadata infrastructures in the same ODB network.

Here are two types of VM clusters:

* An Exadata VM cluster is a set of virtual machines that has a complete Oracle database installation that includes all features of Oracle Enterprise Edition.
* An Autonomous VM cluster is a set of fully managed databases that automate key management tasks using AI/ML with no human intervention required.

Choose **Create Exadata VM cluster**, enter a VM cluster name and a time zone, choose Bring Your Own License (BYOL) or license included for license options. In the next step, you can choose your Exadata infrastructure, grid infrastructure version, and Exadata image version. For database servers, you can choose the CPU core count, memory, and local storage for each VM or accept the defaults.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/23/2025-odb-aws-4-create-vm-cluster-infra.png)

In the next step, you can configure the connectivity setting by choosing your ODB network and entering a prefix for the VM cluster. You can enter a port number for TCP access to the single client access name (SCAN) listener. The default port is 1521 or you can enter a custom SCAN port in the range 1024–8999. For SSH key pairs, enter the public key portion of one or more key pairs used for SSH access to the VM cluster.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/23/2025-odb-aws-4-create-vm-cluster-connection.png)

Then, you can choose diagnostics and tags, review your settings, and create a VM cluster. The creation process can take up to 6 hours, depending on the size of the VM cluster.

**Create and manage an Oracle database**

When the VM cluster is ready, you can create and manage your Oracle Exadata databases in the OCI console. Choose **Manage in OCI** in the details page of the Exadata VM cluster. You will be redirected to the OCI console.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/23/2025-odb-aws-5-manage-oracle-database.jpg)

When you create an Oracle Database in the OCI console, you can select Oracle Database 19c or 23ai. When enabling automatic backups for your provisioned databases, you can use an S3 bucket or OCI Object Storage in the OCI region. To learn more, visit [Provision Oracle Exadata Database Service in Oracle Database@AWS](https://docs.oracle.com/en/learn/exadb-provisioning-aws/#task-4-create-oracle-database) in the OCI documentation.

**Things to know** Here are a couple of things to know about Oracle Database@AWS:

* **Monitoring** – You can monitor Oracle Database@AWS using Amazon CloudWatch metrics in the `AWS/ODB` namespaces for VM clusters, container databases, and pluggable databases. AWS CloudTrail captures all AWS API calls for Oracle Database@AWS as events. Using CloudTrail logs, you can determine the request that was made to Oracle Database@AWS, the IP address from which the request was made, when it was made, and additional details. To learn more, visit [Monitoring Oracle Database@AWS](https://docs.aws.amazon.com/odb/latest/UserGuide/monitoring-overview.html).
* **Security** – You can use IAM to assign permissions that determine who is allowed to manage Oracle Database@AWS resources and SSL/TLS encrypted connections to secure data. You can also use [Amazon EventBridge](https://aws.amazon.com/eventbridge/) for seamless event-driven database operations—all working together to maintain security standards while enabling efficient cloud operations. To learn more, visit [Security in Oracle Database@AWS](https://docs.aws.amazon.com/odb/latest/UserGuide/security.html).
* **Compliance** – Your compliance responsibility when using Oracle Database@AWS is determined by the sensitivity of your data, your company’s compliance objectives, and applicable laws and regulations. Customers can find information on Oracle’s Cloud Compliance on the [Oracle website](https://www.oracle.com/corporate/cloud-compliance/#attestations). Oracle Database@AWS integrates with AWS Services that are in scope for AWS compliance programs, including SOC 1, SOC 2, SOC 3, HIPAA, C5, CSA STAR Attest, CSA STAR Cert, HDS (France), ISO Series (ISO/IEC 9001, 20000-1, 27001, 27017, 27018, 27701, 22301), PCI DSS, and HITRUST.
* **Support** – Your AWS or Oracle sales account team can help you evaluate your current database infrastructure, determine how Oracle Database@AWS can best serve your organization’s requirements, and develop a tailored migration strategy and timeline. You can also get help from [AWS Oracle Competency Partners](https://aws.amazon.com/partners/competencies/oracle/) specialized to architect, deploy, and manage Oracle-based workloads running in the AWS Cloud.

**Now available and coming soon** Oracle Database@AWS is now available in the U.S. East (N. Virginia) and U.S. West (Oregon) Regions through the AWS Marketplace. Oracle Database@AWS pricing and any AWS Marketplace private offers are set by Oracle. You can see specific details around pricing on [Oracle’s pricing page](https://www.oracle.com/cloud/aws/pricing) for the offering.

Oracle Database@AWS will expand to 20 more AWS Regions across the Americas, Europe, and Asia-Pacific including: US East (Ohio), US West (N. California), Asia Pacific (Hyderabad), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), and South America (São Paulo).

You can get started with Oracle Database@AWS with using [AWS console](https://console.aws.amazon.com/odb). To learn more, visit the [Oracle Database@AWS User Guide](https://docs.aws.amazon.com/odb/latest/UserGuide) and [OCI documentation](https://docs.oracle.com/iaas/Content/database-at-aws/oaaws.htm) and send feedback through your usual AWS Support contacts or [OCI support](https://cloud.oracle.com/support).

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