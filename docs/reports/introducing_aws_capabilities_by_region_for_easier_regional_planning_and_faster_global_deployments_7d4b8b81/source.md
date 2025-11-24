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

# Introducing AWS Capabilities by Region for easier Regional planning and faster global deployments

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 06 NOV 2025 in [Developer Tools](https://aws.amazon.com/blogs/aws/category/developer-tools/ "View all posts in Developer Tools"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Regions](https://aws.amazon.com/blogs/aws/category/regions/ "View all posts in Regions") [Permalink](https://aws.amazon.com/blogs/aws/introducing-aws-capabilities-by-region-for-easier-regional-planning-and-faster-global-deployments/)  [Comments](https://aws.amazon.com/blogs/aws/introducing-aws-capabilities-by-region-for-easier-regional-planning-and-faster-global-deployments/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

At AWS, a common question we hear is: “Which AWS capabilities are available in different [Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)?” It’s a critical question whether you’re planning Regional expansion, ensuring compliance with data residency requirements, or architecting for disaster recovery.

Today, I’m excited to introduce [AWS Capabilities by Region](https://builder.aws.com/capabilities/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), a new planning tool that helps you discover and compare AWS services, features, APIs, and [AWS CloudFormation](https://aws.amazon.com/cloudformation/) resources across Regions. You can explore service availability through an interactive interface, compare multiple Regions side-by-side, and view forward-looking roadmap information. This detailed visibility helps you make informed decisions about global deployments and avoid project delays and costly rework.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/04/2025-aws-capabilities-service-and-features-header.png)

**Getting started with Regional comparison**

To get started, go to [AWS Builder Center](https://builder.aws.com) and choose **AWS Capabilities** and **Start Exploring**. When you select **Services and features**, you can choose the AWS Regions you’re most interested in from the dropdown list. You can use the search box to quickly find specific services or features. For example, I chose US (N. Virginia), Asia Pacific (Seoul), and Asia Pacific (Taipei) Regions to compare [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) features.

Now I can view the availability of services and features in my chosen Regions and also see when they’re expected to be released. Select **Show only common features** to identify capabilities consistently available across all selected Regions, ensuring you design with services you can use everywhere.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/06/2025-aws-capabilities-service-and-features-1.png)

The result will indicate availability using the following states: **Available** (live in the region); **Planning** (evaluating launch strategy); **Not Expanding** (will not launch in region); and **2026 Q1** (directional launch planning for the speciﬁed quarter).

In addition to exploring services and features, AWS Capabilities by Region also helps you explore available APIs and CloudFormation resources. As an example, to explore **API operations**, I added Europe (Stockholm) and Middle East (UAE) Regions to compare [Amazon DynamoDB](https://aws.amazon.com/dynamodb/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) features across different geographies. The tool lets you view and search the availability of API operations in each Region.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/07/2025-aws-capabilities-api-operations-1.png)

The **CloudFormation resources** tab helps you verify Regional support for specific resource types before writing your templates. You can search by `Service`, `Type`, `Property`, and `Config.`For instance, when planning an [Amazon API Gateway](https://aws.amazon.com/api-gateway/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) deployment, you can check the availability of resource types like `AWS::ApiGateway::Account`.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/06/2025-aws-capabilities-cloudformation-resources.png)

You can also search detailed resources such as [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) instance type availability, including specialized instances such as Graviton-based, GPU-enabled, and memory-optimized variants. For example, I searched 7th generation compute-optimized metal instances and could find `c7i.metal-24xl` and `c7i.metal-48xl` instances are available across all targeted Regions.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/06/2025-aws-capabilities-cloudformation-resources-property-1.png)

Beyond the interactive interface, the AWS Capabilities by Region data is also accessible through the [AWS Knowledge MCP Server](https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server/). This allows you to automate Region expansion planning, generate AI-powered recommendations for Region and service selection, and integrate Regional capability checks directly into your development workflows and CI/CD pipelines.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/22/2025-aws-inventory-cloud-mcp.png)

**Now available** You can begin exploring [AWS Capabilities by Region in AWS Builder Center](https://builder.aws.com/capabilities/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) immediately. The Knowledge MCP server is also publicly accessible at no cost and does not require an AWS account. Usage is subject to rate limits. Follow the [getting started guide](https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server/) for setup instructions.

You have the opportunity to connect with the team that built the tool at [AWS re:Invent 2025](https://reinvent.awsevents.com/). You can also explore AWS Infrastructure innovations at Kiosk C42 and C49 within the AWS Village (booth 750) on the Expo floor.

We would love to hear your feedback, so please send us any suggestions through the [Builder Support](https://builder.aws.com/support/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) page.

11/18/25 Editor’s Note: Re:Invent information added.

— [Channy](https://linkedin.com/in/channy/)

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