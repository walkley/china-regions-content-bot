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

# New Amazon EC2 P6-B200 instances powered by NVIDIA Blackwell GPUs to accelerate AI innovations

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 15 MAY 2025 in [Amazon EC2](https://aws.amazon.com/blogs/aws/category/compute/amazon-ec2/ "View all posts in Amazon EC2"), [Compute](https://aws.amazon.com/blogs/aws/category/compute/ "View all posts in Compute"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/new-amazon-ec2-p6-b200-instances-powered-by-nvidia-blackwell-gpus-to-accelerate-ai-innovations/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing the general availability of [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) [P6-B200 instances](https://aws.amazon.com/ec2/instance-types/p6?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) accelerated by NVIDIA Blackwell GPUs to address customer needs for high performance and scalability in [artificial intelligence (AI)](https://aws.amazon.com/ai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [machine learning (ML)](https://aws.amazon.com/ai/machine-learning/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and [high performance computing (HPC)](https://aws.amazon.com/hpc/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) applications.

Amazon EC2 P6-B200 instances accelerate a broad range of GPU-enabled workloads but are especially well-suited for large-scale distributed AI training and inferencing for [foundation models (FMs)](https://aws.amazon.com/what-is/foundation-models/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) with reinforcement learning (RL) and distillation, multimodal training and inference, and HPC applications such as climate modeling, drug discovery, seismic analysis, and insurance risk modeling.

When combined with [Elastic Fabric Adapter](https://aws.amazon.com/hpc/efa/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) (EFAv4) networking, hyperscale clustering by [EC2 UltraClusters](https://aws.amazon.com/ec2/ultraclusters/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and advanced virtualization and security capabilities by [AWS Nitro System](https://aws.amazon.com/ec2/nitro/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), you can train and serve FMs with increased speed, scale, and security. These instances also deliver up to two times the performance for AI training (time to train) and inference (tokens/sec) compared to [EC2 P5en instances](https://aws.amazon.com/ec2/instance-types/p5/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

You can accelerate time-to-market for training FMs and deliver faster inference throughput, which lowers inference cost and helps increase adoption of generative AI applications as well as increased processing performance for HPC applications.

**EC2 P6-B200 instances specifications**

New EC2 P6-B200 instances provide eight NVIDIA Blackwell GPUs with 1440 GB of high bandwidth GPU memory, 5th Generation Intel Xeon Scalable processors (Emerald Rapids), 2 TiB of system memory, and 30 TB of local NVMe storage.

Here are the specs for EC2 P6-B200 instances:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Instance size** | **GPUs (NVIDIA B200)** | **GPU   memory (GB)** | **vCPUs** | **GPU Peer to peer (GB/s)** | **Instance storage (TB)** | **Network bandwidth (Gbps)** | **EBS bandwidth (Gbps)** |
| **P6-b200.48xlarge** | 8 | 1440 HBM3e | 192 | 1800 | 8 x 3.84 NVMe SSD | 8 x 400 | 100 |

These instances feature up to 125 percent improvement in GPU TFLOPs, 27 percent increase in GPU memory size, and 60 percent increase in GPU memory bandwidth compared to P5en instances.

**P6-B200 instances in action**

You can use P6-B200 instances in the US West (Oregon) [AWS Region](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region) through [EC2 Capacity Blocks for ML](https://aws.amazon.com/ec2/capacityblocks/). To reserve your EC2 Capacity Blocks, choose **Capacity Reservations** on the [Amazon EC2 console](https://us-east-2.console.aws.amazon.com/ec2/home?region=us-east-2#CapacityReservations:?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/15/2025-ec2-p6-b200-instance-capacity-block.jpg)

Select **Purchase Capacity Blocks for ML** and then choose your total capacity and specify how long you need the EC2 Capacity Block for **p6-b200.48xlarge** instances. The total number of days that you can reserve EC2 Capacity Blocks is 1-14 days, 21 days, 28 days, or multiples of 7 up to 182 days. You can choose your earliest start date for up to 8 weeks in advance.

Now, your EC2 Capacity Block will be scheduled successfully. The total price of an EC2 Capacity Block is charged up front, and the price doesn’t change after purchase. The payment will be billed to your account within 12 hours after you purchase the EC2 Capacity Blocks. To learn more, visit [Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the Amazon EC2 User Guide.

When launching P6-B200 instances, you can use [AWS Deep Learning AMIs](https://aws.amazon.com/machine-learning/amis/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) (DLAMI) to support EC2 P6-B200 instances. DLAMI provides ML practitioners and researchers with the infrastructure and tools to quickly build scalable, secure, distributed ML applications in preconfigured environments.

To run instances, you can use [AWS Management Console](https://console.aws.amazon.com/ec2?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) or [AWS SDKs](http://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/EC2.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

You can integrate EC2 P6-B200 instances seamlessly with various AWS managed services such as [Amazon Elastic Kubernetes Services (Amazon EKS)](https://aws.amazon.com/eks/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). Support for [Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker-ai/hyperpod/) is also coming soon.

**Now available**

Amazon EC2 P6-B200 instances are available today in the US West (Oregon) Region and can be purchased as [EC2 Capacity blocks for ML](https://aws.amazon.com/ec2/capacityblocks/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

Give Amazon EC2 P6-B200 instances a try in the [Amazon EC2 console](https://console.aws.amazon.com/ec2/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). To learn more, refer to the [Amazon EC2 P6 instance page](https://aws.amazon.com/ec2/instance-types/p6/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and send feedback to [AWS re:Post for EC2](https://repost.aws/tags/TAO-wqN9fYRoyrpdULLa5y7g/amazon-ec-2) or through your usual AWS Support contacts.

— [Channy](https://twitter.com/channyun)

---

How is the News Blog doing? Take this [1 minute survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi)!

*(This [survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi) is hosted by an external company. AWS handles your information as described in the [AWS Privacy Notice](https://aws.amazon.com/privacy/?trk=4b29643c-e00f-4ab6-ab9c-b1fb47aa1708&sc_channel=blog). AWS will own the data gathered via this survey and will not share the information collected with survey respondents.)*

![Channy Yun (윤석찬)](https://d2908q01vomqb2.cloudfront.net/7b52009b64fd0a2a49e6d8a939753077792b0554/2020/06/05/channyun_400x400.jpg)

### [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)")

Channy is a Lead Blogger of AWS News Blog and Principal Developer Advocate for AWS Cloud. As an open web enthusiast and blogger at heart, he loves community-driven learning and sharing of technology.

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