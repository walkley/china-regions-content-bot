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

# Simplify serverless development with console to IDE and remote debugging for AWS Lambda

by Micah Walter on 17 JUL 2025 in [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS Lambda](https://aws.amazon.com/blogs/aws/category/compute/aws-lambda/ "View all posts in AWS Lambda"), [AWS Serverless Application Model](https://aws.amazon.com/blogs/aws/category/compute/aws-serverless-application-model/ "View all posts in AWS Serverless Application Model"), [Developer Tools](https://aws.amazon.com/blogs/aws/category/developer-tools/ "View all posts in Developer Tools"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Serverless](https://aws.amazon.com/blogs/aws/category/serverless/ "View all posts in Serverless") [Permalink](https://aws.amazon.com/blogs/aws/simplify-serverless-development-with-console-to-ide-and-remote-debugging-for-aws-lambda/)  [Comments](https://aws.amazon.com/blogs/aws/simplify-serverless-development-with-console-to-ide-and-remote-debugging-for-aws-lambda/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing two significant enhancements to [AWS Lambda](https://aws.amazon.com/lambda) that make it easier than ever for developers to build and debug serverless applications in their local development environments: console to IDE integration and remote debugging. These new capabilities build upon our recent improvements to the Lambda development experience, including the [enhanced in-console editing experience](https://aws.amazon.com/blogs/compute/introducing-an-enhanced-in-console-editing-experience-for-aws-lambda/) and the [improved local integrated development environment (IDE) experience](https://aws.amazon.com/blogs/compute/introducing-an-enhanced-local-ide-experience-for-aws-lambda-developers/) launched in late 2024.

When building serverless applications, developers typically focus on two areas to streamline their workflow: local development environment setup and cloud debugging capabilities. While developers can bring functions from the console to their IDE, they’re looking for ways to make this process more efficient. Additionally, as functions interact with various AWS services in the cloud, developers want enhanced debugging capabilities to identify and resolve issues earlier in the development cycle, reducing their reliance on local emulation and helping them optimize their development workflow.

**Console to IDE integration**

To address the first challenge, we’re introducing console to IDE integration, which streamlines the workflow from the [AWS Management Console](https://aws.amazon.com/console/) to [Visual Studio Code (VS Code)](https://code.visualstudio.com/). This new capability adds an **Open in Visual Studio Code** button to the Lambda console, enabling developers to quickly move from viewing their function in the browser to editing it in their IDE, eliminating the time-consuming setup process for local development environments.

The console to IDE integration automatically handles the setup process, checking for VS Code installation and the [AWS Toolkit for VS Code](https://aws.amazon.com/visualstudiocode/). For developers that have everything already configured, choosing the button immediately opens their function code in VS Code, so they can continue editing and deploy changes back to Lambda in seconds. If VS Code isn’t installed, it directs developers to the download page, and if the AWS Toolkit is missing, it prompts for installation.

To use console to IDE, look for the **Open in VS Code** button in either the Getting Started popup after creating a new function or the **Code** tab of existing Lambda functions. After selecting, VS Code opens automatically (installing AWS Toolkit if needed). Unlike the console environment, you now have access to a full development environment with integrated terminal – a significant improvement for developers who need to manage packages (npm install, pip install), run tests, or use development tools like linters and formatters. You can edit code, add new files/folders, and any changes you make will trigger an automatic deploy prompt. When you choose to deploy, the AWS Toolkit automatically deploys your function to your AWS account.

![Screenshot showing Console to IDE](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/18/console-to-ide-01-1024x683.png)

**Remote debugging**

Once developers have their functions in their IDE, they can use remote debugging to debug Lambda functions deployed in their AWS account directly from VS Code. The key benefit of remote debugging is that it allows developers to debug functions running in the cloud while integrated with other AWS services, enabling faster and more reliable development.

With remote debugging, developers can debug their functions with complete access to [Amazon Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/) resources and [AWS Identity and Access Management (AWS IAM)](https://aws.amazon.com/iam/) roles, eliminating the gap between local development and cloud execution. For example, when debugging a Lambda function that interacts with an [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) database in a VPC, developers can now debug the [execution environment](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) of the function running in the cloud within seconds, rather than spending time setting up a local environment that might not match production.

Getting started with remote debugging is straightforward. Developers can select a Lambda function in VS Code and enable debugging in seconds. AWS Toolkit for VS Code automatically downloads the function code, establishes a secure debugging connection, and enables breakpoint setting. When debugging is complete, AWS Toolkit for VS Code automatically cleans up the debugging configuration to prevent any impact on production traffic.

**Let’s try it out**

To take remote debugging for a spin, I chose to start with a basic “hello world” example function, written in Python. I had previously created the function using the [AWS Management Console](https://console.aws.amazon.com/) for AWS Lambda. Using the AWS Toolkit for VS Code, I can navigate to my function in the **Explorer** pane. Hovering over my function, I can right-click (ctrl-click in Windows) to download the code to my local machine to edit the code in my IDE. Saving the file will ask me to decide if I want to deploy the latest changes to Lambda.

![Screenshot view of the Lambda Debugger in VS Code](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/18/lambda-debug-01-1024x679.png)

From here, I can select the play icon to open the **Remote invoke configuration** page for my function. This dialog will now display a **Remote debugging** option, which I configure to point at my local copy of my function handler code. Before choosing **Remote invoke**, I can set breakpoints on the left anywhere I want my code to pause for inspection.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/18/lambda-debug-02-1024x680.png)

My code will be running in the cloud after it’s invoked, and I can monitor its status in real time in VS Code. In the following screenshot, you can see I’ve set a breakpoint at the print statement. My function will pause execution at this point in my code, and I can inspect things like local variable values before either continuing to the next breakpoint or stepping into the code line by line.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/18/lambda-debug-03-1024x681.png)

Here, you can see that I’ve chosen to step into the code, and as I go through it line by line, I can see the context and local and global variables displayed on the left side of the IDE. Additionally, I can follow the logs in the **Output** tab at the bottom of the IDE. As I step through, I’ll see any log messages or output messages from the execution of my function in real time.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/18/lambda-debug-04-1024x680.png)

**Enhanced development workflow**

These new capabilities work together to create a more streamlined development experience. Developers can start in the console, quickly transition to VS Code using the console to IDE integration, and then use remote debugging to debug their functions running in the cloud. This workflow eliminates the need to switch between multiple tools and environments, helping developers identify and fix issues faster.

**Now available**

You can start using these new features through the AWS Management Console and VS Code with the AWS Toolkit for VS Code (v3.69.0 or later) installed. Console to IDE integration is available in all commercial [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) where Lambda is available, except AWS GovCloud (US) Regions. Learn more about it in [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/foundation-iac-local-development.html) and [AWS Toolkit for VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/lambda-console-ide.html) documentation. To learn more about remote debugging capability, including AWS Regions it is available in, visit the [AWS Toolkit for VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/lambda-remote-debug.html) and [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/debugging.html) documentation.

Console to IDE and remote debugging are available to you at no additional cost. With remote debugging, you pay only for the standard Lambda execution costs during debugging sessions. Remote debugging will support Python, Node.js, and Java runtimes at launch, with plans to expand support to additional runtimes in the future.

These enhancements represent a significant step forward in simplifying the serverless development experience, which means developers can build and debug Lambda functions more efficiently than ever before.

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