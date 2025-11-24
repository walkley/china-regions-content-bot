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

# AWS Lambda enhances event processing with provisioned mode for SQS event-source mapping

by Micah Walter on 14 NOV 2025 in [Amazon Simple Queue Service (SQS)](https://aws.amazon.com/blogs/aws/category/messaging/amazon-simple-queue-service-sqs/ "View all posts in Amazon Simple Queue Service (SQS)"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS Lambda](https://aws.amazon.com/blogs/aws/category/compute/aws-lambda/ "View all posts in AWS Lambda"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Serverless](https://aws.amazon.com/blogs/aws/category/serverless/ "View all posts in Serverless") [Permalink](https://aws.amazon.com/blogs/aws/aws-lambda-enhances-sqs-processing-with-new-provisioned-mode-3x-faster-scaling-16x-higher-capacity/)  [Comments](https://aws.amazon.com/blogs/aws/aws-lambda-enhances-sqs-processing-with-new-provisioned-mode-3x-faster-scaling-16x-higher-capacity/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing the general availability of provisioned mode for [AWS Lambda](https://aws.amazon.com/lambda) with [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) [Event Source Mapping (ESM)](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html), a new feature that customers can use to optimize the throughput of their event-driven applications by configuring dedicated polling resources. Using this new capability, which provides 3x faster scaling, and 16x higher concurrency, you can process events with lower latency, handle sudden traffic spikes more effectively, and maintain precise control over your event processing resources.

Modern applications increasingly rely on event-driven architectures where services communicate through events and messages. Amazon SQS is commonly used as an event source for Lambda functions, so developers can build loosely coupled, scalable applications. Although the SQS ESM automatically handles queue polling and function invocation, customers with stringent performance requirements have asked for more control over the polling behavior to handle spiky traffic patterns and maintain low processing latency.

Provisioned mode for SQS ESM addresses these needs by introducing event pollers, which are dedicated resources that remain ready to handle expected traffic patterns. These event pollers can auto scale up to 1000 per concurrent executions per minute, more than three times faster than before to handle sudden spikes in event traffic and provide up to 20,000 concurrency–16 times higher capacity to process millions of events with Lambda functions. This enhanced scaling behavior helps customers maintain predictable low latency even during traffic surges.

Enterprises across various industries, from financial services to gaming companies, are using AWS Lambda with Amazon SQS to process real-time events for their mission-critical applications. These organizations, which include some of the largest online gaming platforms and financial institutions, require consistent subsecond processing times for their event-driven workloads, particularly during periods of peak usage. Provisioned mode for SQS ESM is a capability you can use to meet your stringent performance requirements while maintaining cost controls.

**Enhanced control and performance**

With provisioned mode, you can configure both minimum and maximum numbers of event pollers for your SQS ESM. Each event poller represents a unit of compute that handles queue polling, event batching, and filtering before invoking Lambda functions. Each event poller can handle up to 1 MB/sec of throughput, up to 10 concurrent invokes, or up to 10 SQS polling API calls per second. By setting a minimum number of event pollers, you enable your application to maintain a baseline processing capacity that can immediately handle sudden traffic increases. We recommend that you set the minimum event pollers required to handle your known peak workload requirements. The optional maximum setting helps prevent overloading downstream systems by limiting the total processing throughput.

The new mode delivers significant improvements in how your event-driven applications handle varying workloads. When traffic increases, your ESM detects the growing backlog within seconds and dynamically scales event pollers between your configured minimum and maximum values three times faster than before. This enhanced scaling capability is complemented by a substantial increase in processing capacity, with support for up to 2 GBps of aggregate traffic, and up to 20K concurrent requests—16x higher than previously possible. By maintaining a minimum number of ready-to-use event pollers, your application achieves predictable performance, handling sudden traffic spikes without the delay typically associated with scaling up resources. During low traffic periods, your ESM automatically scales down to your configured minimum number of event pollers, which means you can optimize costs while maintaining responsiveness.

**Let’s try it out**

Enabling provisioned mode is straightforward in the [AWS Management Console](https://aws.amazon.com/console/). You need to already have an SQS queue configured and a Lambda function. To get started, in the **Configuration** tab for your Lambda function, choose **Triggers**, then **Add trigger**. This will bring up a user interface where you can configure your trigger. Choose **SQS** from the dropdown menu for source and then select the **SQS queue** you want to use.

Under **Event poller configuration**, you will now see a new option called **Provisioned mode**. Select **Configure** to reveal settings for **Minimum event pollers** and **Maximum event pollers**, each with defaults and minimum and maximum values displayed.

![Configuration panel for SQS provisioned Mode](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/07/sqs-provision-01-1024x541.png)

After you have configured **Provisioned mode**, you can save your trigger. If you need to make changes later, you can find the current configuration under the **Triggers** tab in the AWS Lambda configuration section, and you can modify your current settings there.

![SQS Provisioned Poller confiig](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/07/sqs-provision-02-1024x475.png)

**Monitoring and observability**

You can monitor your provisioned mode usage through Amazon CloudWatch metrics. The ProvisionedPollers metric shows the number of active event pollers processing events in one-minute windows.

**Now available**

Provisioned mode for Lambda SQS ESM is available today in all commercial [AWS Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region). You can start using this feature through the AWS Management Console, [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/), or [AWS SDKs](https://aws.amazon.com/developer/tools/). Pricing is based on the number of event pollers provisioned and the duration they’re provisioned for, measured in Event Poller Units (EPUs). Each EPU supports up to 1 MB per second throughput capacity per event poller, with minimum 2 event pollers per ESM. See the [AWS pricing page](https://aws.amazon.com/lambda/pricing/) for more information on EPU charges.

To learn more about provisioned mode for SQS ESM, visit the AWS Lambda [documentation](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html). Start building more responsive event-driven applications today with enhanced control over your event processing resources.

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