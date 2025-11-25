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

# Announcing Amazon ECS Managed Instances for containerized applications

by Micah Walter on 30 SEP 2025 in [Amazon EC2](https://aws.amazon.com/blogs/aws/category/compute/amazon-ec2/ "View all posts in Amazon EC2"), [Amazon Elastic Container Service](https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-service/ "View all posts in Amazon Elastic Container Service"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/announcing-amazon-ecs-managed-instances-for-containerized-applications/)  [Comments](https://aws.amazon.com/blogs/aws/announcing-amazon-ecs-managed-instances-for-containerized-applications/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing Amazon ECS Managed Instances, a new compute option for [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/) that enables developers to use the full range of [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2) capabilities while offloading infrastructure management responsibilities to [Amazon Web Service (AWS)](https://aws.amazon.com). This new offering combines the operational simplicity of offloading infrastructure with the flexibility and control of Amazon EC2, which means customers can focus on building applications that drive innovation, while reducing total cost of ownership (TCO) and maintaining AWS best practices.

Amazon ECS Managed Instances provides a fully managed container compute environment that supports a broad range of EC2 instance types and deep integration with AWS services. By default, it automatically selects the most cost-optimized EC2 instances for your workloads, but you can specify particular instance attributes or types when needed. AWS handles all aspects of infrastructure management, including provisioning, scaling, security patching, and cost optimization, enabling you to concentrate on building and running your applications.

**Let’s try it out**

Looking at the [AWS Management Console](https://aws.amazon.com/console/) experience for creating a new Amazon ECS cluster, I can see the new option for using ECS Managed Instances. Let’s take a quick tour of all the new options.

![Creating a ECS cluster with Managed Instances](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/24/Screenshot-2025-09-24-at-10.51.19 AM-1024x502.png)

After I’ve selected **Fargate and Managed Instances**, I’m presented with two options. If I select **Use ECS default**, Amazon ECS will choose general purpose instance types based on grouping together pending Tasks, and picking the optimum instance type based on cost and resilience metrics. This is the most straightforward and recommended way to get started. Selecting **Use custom – advanced** opens up additional configuration parameters, where I can fine-tune the attributes of instances Amazon ECS will use.

![Creating a ECS cluster with Managed Instances](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/24/Screenshot-2025-09-24-at-12.59.44 PM-1024x593.png)

By default, I see **CPU** and **Memory** as attributes, but I can select from 20 additional attributes to continue to filter the list of available instance types Amazon ECS can access.

![ECS Managed Instances](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/30/Screenshot-2025-09-30-at-4.05.55 PM-1024x735.png)

After I’ve made my attribute selections, I see a list of all the instance types that match my choices.

![Creating a ECS cluster with Managed Instances](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/24/Screenshot-2025-09-24-at-12.59.57 PM-1-1024x466.png)

From here, I can create my ECS cluster as usual and Amazon ECS will provision instances for me on my behalf based on the attributes and criteria I’ve defined in the previous steps.

**Key features of Amazon ECS Managed Instances**

With Amazon ECS Managed Instances, AWS takes full responsibility for infrastructure management, handling all aspects of instance provisioning, scaling, and maintenance. This includes implementing regular security patches initiated every 14 days (due to instance connection draining, the actual lifetime of the instance may be longer), with the ability to schedule maintenance windows using Amazon EC2 event windows to minimize disruption to your applications.

The service provides exceptional flexibility in instance type selection. Although it automatically selects cost-optimized instance types by default, you maintain the power to specify desired instance attributes when your workloads require specific capabilities. This includes options for GPU acceleration, CPU architecture, and network performance requirements, giving you precise control over your compute environment.

To help optimize costs, Amazon ECS Managed Instances intelligently manages resource utilization by automatically placing multiple tasks on larger instances when appropriate. The service continually monitors and optimizes task placement, consolidating workloads onto fewer instances to dry up, utilize and terminate idle (empty) instances, providing both high availability and cost efficiency for your containerized applications.

Integration with existing AWS services is seamless, particularly with Amazon EC2 features such as EC2 pricing options. This deep integration means that you can maximize existing capacity investments while maintaining the operational simplicity of a fully managed service.

Security remains a top priority with Amazon ECS Managed Instances. The service runs on Bottlerocket, a purpose-built container operating system, and maintains your security posture through automated security patches and updates. You can see all the updates and patches applied to the Bottlerocket OS image on the [Bottlerocket website](https://bottlerocket.dev/en/os/). This comprehensive approach to security keeps your containerized applications running in a secure, maintained environment.

**Available now**

Amazon ECS Managed Instances is available today in US East (North Virginia), US West (Oregon), Europe (Ireland), Africa (Cape Town), Asia Pacific (Singapore), and Asia Pacific (Tokyo) AWS Regions. You can start using Managed Instances through the AWS Management Console, AWS Command Line Interface (AWS CLI), or infrastructure as code (IaC) tools such as AWS Cloud Development Kit (AWS CDK) and AWS CloudFormation. You pay for the EC2 instances you use plus a management fee for the service.

To learn more about Amazon ECS Managed Instances, visit the [documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ManagedInstances.html) and get started simplifying your container infrastructure today.

![Micah Walter](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/03/05/micawal.jpg)

### Micah Walter

Micah Walter is a Sr. Solutions Architect supporting enterprise customers in the New York City region and beyond. He advises executives, engineers, and architects at every step along their journey to the cloud, with a deep focus on sustainability and practical design. In his free time, Micah enjoys the outdoors, photography, and chasing his kids around the house.

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