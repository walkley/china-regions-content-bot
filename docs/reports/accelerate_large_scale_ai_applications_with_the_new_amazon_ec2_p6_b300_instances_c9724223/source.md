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

# Accelerate large-scale AI applications with the new Amazon EC2 P6-B300 instances

by Veliswa Boya on 18 NOV 2025 in [Amazon EC2](https://aws.amazon.com/blogs/aws/category/compute/amazon-ec2/ "View all posts in Amazon EC2"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Compute](https://aws.amazon.com/blogs/aws/category/compute/ "View all posts in Compute"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/accelerate-large-scale-ai-applications-with-the-new-amazon-ec2-p6-b300-instances/)  [Comments](https://aws.amazon.com/blogs/aws/accelerate-large-scale-ai-applications-with-the-new-amazon-ec2-p6-b300-instances/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing the general availability of [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/pm/ec2/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) P6-B300 instances, our next-generation GPU platform accelerated by NVIDIA Blackwell Ultra GPUs. These instances deliver 2 times more networking bandwidth, and 1.5 times more GPU memory compared to previous generation instances, creating a balanced platform for large-scale AI applications.

With these improvements, P6-B300 instances are ideal for training and serving large-scale [AI models](https://aws.amazon.com/ai/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el), particularly those employing sophisticated techniques such as [Mixture of Experts (MoE)](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2-expert-parallelism.html?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) and multimodal processing. For organizations working with trillion-parameter models and requiring distributed training across thousands of GPUs, these instances provide the perfect balance of compute, memory, and networking capabilities.

**Improvements made compared to predecessors**

The P6-B300 instances deliver 6.4Tbps [Elastic Fabric Adapter (EFA) networking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) bandwidth, supporting efficient communication across large GPU clusters. These instances feature 2.1TB of GPU memory, allowing large models to reside within a single NVIDIA NVLink domain, which significantly reduces model sharding and communication overhead. When combined with EFA networking and the advanced virtualization and security capabilities of [AWS Nitro System](https://aws.amazon.com/ec2/nitro/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el), these instances provide unprecedented speed, scale, and security for AI workloads.

The specs for the EC2 P6-B300 instances are as follows.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Instance size** | **VCPUs** | **System memory** | **GPUs** | **GPU memory** | **GPU-GPU interconnect** | **EFA network bandwidth** | **ENA bandwidth** | **EBS bandwidth** | **Local storage** |
| **P6-B300.48xlarge** | 192 | 4TB | 8x NVIDIA B300 GPU | 2144GB HBM3e | 1800 GB/s | 6.4 Tbps | 300 Gbps | 100 Gbps | 8x 3.84TB |

**Good to know**

In terms of persistent storage, AI workloads primarily use a combination of high performance persistent storage options such as [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el), [Amazon S3 Express One Zone](https://aws.amazon.com/s3/storage-classes/express-one-zone/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el), and [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el), depending on price performance considerations. For illustration, the dedicated 300Gbps [Elastic Network Adapter (ENA) networking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) on P6-B300 enables high-throughput hot storage access with S3 Express One Zone, supporting large-scale training workloads. If you’re using FSx for Lustre, you can now use EFA with NVIDIA GPUDirect Storage (GDS) to achieve up to 1.2Tbps of throughput to the Lustre file system on the P6-B300 instances to quickly load your models.

**Available now**

The P6-B300 instances are now available through [Amazon EC2 Capacity Blocks for ML](https://aws.amazon.com/ec2/capacityblocks/) and Savings Plans in the US West (Oregon) [AWS Region](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region).

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/12/p6b300screen.png)

For on-demand reservation of P6-B300 instances, please reach out to your account manager. As usual with Amazon EC2, you pay only for what you use. For more information, refer to [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el). Check out the full collection of [accelerated computing instances](https://aws.amazon.com/ec2/instance-types/) to help you start migrating your applications.

To learn more, visit our [Amazon EC2 P6-B300 instances page](https://aws.amazon.com/ec2/instance-types/p6/). Send feedback to [AWS re:Post for EC2](https://repost.aws/tags/TAO-wqN9fYRoyrpdULLa5y7g/amazon-ec-2/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) or through your usual AWS Support contacts.

– [Veliswa](https://www.linkedin.com/in/veliswa-boya/)

![Veliswa Boya](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2021/07/09/vby-photo_300x300.jpg)

### Veliswa Boya

Veliswa Boya is a Senior Developer Advocate, based in South Africa and working closely with the builder community in Sub-Saharan Africa. She has fulfilled many roles in tech, which range from developer to analyst, architect to cloud engineer, and now a developer advocate. Veliswa especially enjoys working with those who are new to tech—and those getting started with AWS.

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