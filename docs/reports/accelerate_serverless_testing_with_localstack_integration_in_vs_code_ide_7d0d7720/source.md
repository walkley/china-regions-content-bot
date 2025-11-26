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

# Accelerate serverless testing with LocalStack integration in VS Code IDE

by Micah Walter on 11 SEP 2025 in [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS Lambda](https://aws.amazon.com/blogs/aws/category/compute/aws-lambda/ "View all posts in AWS Lambda"), [AWS Serverless Application Model](https://aws.amazon.com/blogs/aws/category/compute/aws-serverless-application-model/ "View all posts in AWS Serverless Application Model"), [Developer Tools](https://aws.amazon.com/blogs/aws/category/developer-tools/ "View all posts in Developer Tools"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Serverless](https://aws.amazon.com/blogs/aws/category/serverless/ "View all posts in Serverless") [Permalink](https://aws.amazon.com/blogs/aws/accelerate-serverless-testing-with-localstack-integration-in-vs-code-ide/)  [Comments](https://aws.amazon.com/blogs/aws/accelerate-serverless-testing-with-localstack-integration-in-vs-code-ide/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing [LocalStack](https://localstack.cloud/) integration in the [AWS Toolkit for Visual Studio Code](https://aws.amazon.com/visualstudiocode/) that makes it easier than ever for developers to test and debug serverless applications locally. This enhancement builds upon our [recent improvements to the AWS Lambda development experience](https://aws.amazon.com/blogs/compute/accelerating-local-serverless-development-with-console-to-ide-and-remote-debugging-for-aws-lambda/), including the [console to IDE integration and remote debugging](https://aws.amazon.com/blogs/aws/simplify-serverless-development-with-console-to-ide-and-remote-debugging-for-aws-lambda/) capabilities we launched in July 2025, continuing our commitment to simplify serverless development on Amazon Web Services (AWS).

When building serverless applications, developers typically focus on three key areas to streamline their testing experience: unit testing, integration testing, and debugging resources running in the cloud. Although [AWS Serverless Application Model Command Line Interface (AWS SAM CLI)](https://aws.amazon.com/serverless/sam/) provides excellent local unit testing capabilities for individual Lambda functions, developers working with event-driven architectures that involve multiple AWS services, such as [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/), [Amazon EventBridge](https://aws.amazon.com/eventbridge/), and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), need a comprehensive solution for local integration testing. Although LocalStack provided local emulation of AWS services, developers had to previously manage it as a standalone tool, requiring complex configuration and frequent context switching between multiple interfaces, which slowed down the development cycle.

**LocalStack integration in AWS Toolkit for VS Code** To address these challenges, we’re introducing LocalStack integration so developers can connect AWS Toolkit for VS Code directly to LocalStack endpoints. With this integration, developers can test and debug serverless applications without switching between tools or managing complex LocalStack setups. Developers can now emulate end-to-end event-driven workflows involving services such as Lambda, Amazon SQS, and EventBridge locally, without needing to manage multiple tools, perform complex endpoint configurations, or deal with service boundary issues that previously required connecting to cloud resources.

The key benefit of this integration is that AWS Toolkit for VS Code can now connect to custom endpoints such as LocalStack, something that wasn’t possible before. Previously, to point AWS Toolkit for VS Code to their LocalStack environment, developers had to perform manual configuration and context switching between tools.

Getting started with LocalStack in VS Code is straightforward. Developers can begin with the LocalStack **Free** version, which provides local emulation for core AWS services ideal for early-stage development and testing. Using the guided application walkthrough in VS Code, developers can install LocalStack directly from the toolkit interface, which automatically installs the LocalStack extension and guides them through the setup process. When it’s configured, developers can deploy serverless applications directly to the emulated environment and test their functions locally, all without leaving their IDE.

**Let’s try it out** First, I’ll update my copy of the AWS Toolkit for VS Code to the latest version. Once, I’ve done this, I can see a new option when I go to **Application Builder** and click on **Walkthrough of Application Builder**. This allows me to install LocalStack with a single click.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/05/image-01-1024x756.png)

Once I’ve completed the setup for LocalStack, I can start it up from the status bar and then I’ll be able to select LocalStack from the list of my [configured AWS profiles](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-configure.html). In this illustration, I am using Application Composer to build a simple serverless architecture using [Amazon API Gateway](https://aws.amazon.com/api-gateway/), Lambda, and DynamoDB. Normally, I’d deploy this to AWS using AWS SAM. In this case, I’m going to use the same AWS SAM command to deploy my stack locally.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/11/image-02-1.png)

I just do `sam deploy –guided –profile localstack` from the command line and follow the usual prompts. Deploying to LocalStack using AWS SAM CLI provides the exact same experience I’m used to when deploying to AWS. In the screenshot below, I can see the standard output from AWS SAM, as well as my new LocalStack resources listed in the AWS Toolkit Explorer.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/11/image-03-1.png)

I can even go in to a Lambda function and edit the function code I’ve deployed locally!

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/11/image-04-1.png)

Over on the LocalStack website, I can login and take a look at all the resources I have running locally. In the screenshot below, you can see the local DynamoDB table I just deployed.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/05/image-05-1024x363.png)

**Enhanced development workflow** These new capabilities complement our recently launched console-to-IDE integration and remote debugging features, creating a comprehensive development experience that addresses different testing needs throughout the development lifecycle. AWS SAM CLI provides excellent local testing for individual Lambda functions, handling unit testing scenarios effectively. For integration testing, the LocalStack integration enables testing of multiservice workflows locally without the complexity of AWS Identity and Access Management (IAM) permissions, Amazon Virtual Private Cloud (Amazon VPC) configurations, or service boundary issues that can slow down development velocity.

When developers need to test using AWS services in development environments, they can use our remote debugging capabilities, which provide full access to Amazon VPC resources and IAM roles. This tiered approach frees up developers to focus on business logic during early development phases using LocalStack, then seamlessly transition to cloud-based testing when they need to validate against AWS service behaviors and configurations. The integration eliminates the need to switch between multiple tools and environments, so developers can identify and fix issues faster while maintaining the flexibility to choose the right testing approach for their specific needs.

**Now available** You can start using these new features through the AWS Toolkit for VS Code by updating to v3.74.0. The LocalStack integration is available in all commercial [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) except [AWS GovCloud (US)](https://aws.amazon.com/govcloud-us/) Regions. To learn more, visit the [AWS Toolkit for VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/lambda-localstack.html) and [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) documentation.

For developers who need broader service coverage or advanced capabilities, LocalStack offers additional tiers with expanded features. There are no additional costs from AWS for using this integration.

These enhancements represent another significant step forward in our ongoing commitment to simplifying the serverless development experience. Over the past year, we’ve focused on making VS Code the tool of choice for serverless developers, and this LocalStack integration continues that journey by providing tools for developers to build and test serverless applications more efficiently than ever before.

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