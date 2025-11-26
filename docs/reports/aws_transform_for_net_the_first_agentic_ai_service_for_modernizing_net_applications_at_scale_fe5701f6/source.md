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

# AWS Transform for .NET, the first agentic AI service for modernizing .NET applications at scale

by Prasad Rao on 15 MAY 2025 in [.NET](https://aws.amazon.com/blogs/aws/category/programing-language/dot-net/ "View all posts in .NET"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS Transform](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/generative-ai/aws-transform/ "View all posts in AWS Transform"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Generative AI](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch") [Permalink](https://aws.amazon.com/blogs/aws/aws-transform-for-net-the-first-agentic-ai-service-for-modernizing-net-applications-at-scale/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

I started my career as a .NET developer and have seen .NET evolve over the last couple of decades. Like many of you, I also developed multiple enterprise applications in .NET Framework that ran only on Windows. I fondly remember building my first enterprise application with .NET Framework. Although it served us well, the technology landscape has significantly shifted. Now that there is an open source and cross-platform version of .NET that can run on Linux, these legacy enterprise applications built on .NET Framework need to be ported and modernized.

The benefits of porting to Linux are compelling: applications cost 40 percent less to operate because they save on Windows licensing costs, run 1.5–2 times faster with improved performance, and handle growing workloads with 50 percent better scalability. Having helped port several applications, I can say the effort is worth the rewards.

However, porting .NET Framework applications to cross-platform .NET is a labor-intensive and error-prone process. You have to perform multiple steps, such as analyzing the codebase, detecting incompatibilities, implementing fixes while porting the code, and then validating the changes. For enterprises, the challenge becomes even more complex because they might have hundreds of .NET Framework applications in their portfolio.

At re:Invent 2024, we previewed this capability as [Amazon Q Developer transformation capabilities](https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-q-developer-transformation-net-porting-preview/) for .NET to help port your .NET applications at scale. The experience is available as a [unified web experience](https://aws.amazon.com/blogs/aws/announcing-amazon-q-developer-transformation-capabilities-for-net-mainframe-and-vmware-workloads-preview/) for at-scale transformation and [within your integrated development environment (IDE)](https://aws.amazon.com/blogs/aws/announcing-amazon-q-developer-transformation-capabilities-for-net-preview/) for individual project and solution porting.

Now that we’ve incorporated your valuable feedback and suggestions, we’re excited to announce today the general availability of [AWS Transform for .NET](https://aws.amazon.com/transform/net). We’ve also added new capabilities to support projects with private NuGet packages, port model-view-controller (MVC) Razor views to ASP .NET Core Razor views, and execute the ported unit tests.

I’ll expand on the key new capabilities in a moment, but let’s first take a quick look at the two porting experiences of AWS Transform for .NET.

**Large-scale porting experience for .NET applications**

Enterprise digital transformation is typically driven by central teams responsible for modernizing hundreds of applications across multiple business units. Different teams have ownership of different applications and their respective repositories. Success requires close coordination between these teams and the application owners and developers across business units. To accelerate this modernization at scale, AWS Transform for .NET provides a web experience that enables teams to connect directly to source code repositories and efficiently transform multiple applications across the organization. For select applications requiring dedicated developer attention, the same agent capabilities are available to developers as an extension for Visual Studio IDE.

Let’s start by looking at how the web experience of AWS Transform for .NET helps port hundreds of .NET applications at scale.

**Web experience of AWS Transform for .NET**

To get started with the web experience of AWS Transform, I onboard using the steps outlined in the [documentation](https://docs.aws.amazon.com/transform/latest/userguide/dotnet-quick-start.html), sign in using my credentials, and create a job for .NET modernization.

[![Create a new job for .NET Transformation](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/12/CreateJob.gif)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/12/CreateJob.gif)

AWS Transform for .NET creates a job plan, which is a sequence of steps that the agent will execute to assess, discover, analyze, and transform applications at scale. It then waits for me to [set up a connector](https://docs.aws.amazon.com/transform/latest/userguide/dotnet-creating-repo-connector.html) to connect to my source code repositories.

[![Setup connector to connect to source code repository ](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/15/connectrepo.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/15/connectrepo.png)

After the connector is in place, AWS Transform begins discovering repositories in my account. It conducts an assessment focused on three key areas: repository dependencies, required private packages and third-party libraries, and supported project types within your repositories.

Based on this assessment, it generates a recommended transformation plan. The plan orders repositories according to their last modification dates, dependency relationships, private package requirements, and the presence of supported project types.

AWS Transform for .NET then prepares for the transformation process by requesting specific inputs, such as the target branch destination, target .NET version, and the repositories to be transformed.

To select the repositories to transform, I have two options: use the recommended plan or customize the transformation plan by selecting repositories manually. For selecting repositories manually, I can use the UI or download the repository mapping and upload the customized list.

[![select the repositories to transform ](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/15/SelectRepos1-1.gif)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/15/SelectRepos1-1.gif)

AWS Transform for .NET automatically ports the application code, builds the ported code, executes unit tests, and commits the ported code to a new branch in my repository. It provides a comprehensive transformation summary, including modified files, test outcomes, and suggested fixes for any remaining work.

While the web experience helps accelerate large-scale porting, some applications may require developer attention. For these cases, the same agent capabilities are available in the Visual Studio IDE.

**Visual Studio IDE experience of AWS Transform for .NET**

Now, let’s explore how AWS Transform for .NET works within Visual Studio.

To get started, I install the latest version of [AWS Toolkit extension for Visual Studio](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022) and set up the [prerequisites](https://docs.aws.amazon.com/transform/latest/userguide/dotnet-ide-vs.html#transform-dotnet-prerequisites).

I open a .NET Framework solution, and in the **Solution Explorer**, I see the context menu item **Port project with AWS Transform** for an individual project.

[![Context menu for Port project with AWS Transform in Visual Studio](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/15/VSExten2.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/15/VSExten2.png)

I provide the required inputs, such as the target .NET version and the approval for the agents to autonomously transform code, execute unit tests, generate a transformation summary, and validate Linux-readiness.

[![Transformation summary after the project is transformed in Visual Studio](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/13/trans-summary.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/13/trans-summary.png)

I can review the code changes made by the agents locally and continue updating my codebase.

Let’s now explore some of the key new capabilities added to AWS Transform for .NET.

**Support for projects with private NuGet package dependencies**

During preview, only projects with public NuGet package dependencies were supported. With general availability, we now support projects with private NuGet package dependencies. This has been one of the most requested features during the preview.

The feature I really love is that AWS Transform can detect cross-repository dependencies. If it finds the source code of my private NuGet package, it automatically transforms that as well. However, if it can’t locate the source code, in the web experience, it provides me the flexibility to upload the required NuGet packages.

AWS Transform displays the missing package dependencies that need to be resolved. There are two ways to do this: I can either [use the provided PowerShell script](https://docs.aws.amazon.com/transform/latest/userguide/dotnet-resolving-dependencies.html#upload-missing-packages) to create and upload packages, or I can build the application locally and upload the NuGet packages from the packages folder in the solution directory.

[![Upload packages to resolve missing dependencies ](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/15/nugetupload.gif)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/15/nugetupload.gif)

After I upload the missing NuGet packages, AWS Transform is able to resolve the dependencies. It’s best to provide both the .NET Framework and cross platform .NET versions of the NuGet packages. If the cross platform .NET version is not available, then at a minimum the .NET Framework version is required for AWS Transform to add it as an assembly reference and proceed for transformation.

**Unit test execution**

During preview, we supported porting unit tests from .NET Framework to cross-platform .NET. With general availability, we’ve also added support for executing unit tests after the transformation is complete.

After the transformation is complete and the unit tests are executed, I can see the results in the dashboard and view the status of the tests at each individual test project level.

[![Dashboard after successful transformation in web showing exectuted unit tests ](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/15/UnitTests1.gif)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/15/UnitTests1.gif)

**Transformation visibility and summary**

After the transformation is complete, I can download a detailed report in JSON format that gives me a list of transformed repositories, details about each repository, and the status of the transformation actions performed for each project within a repository. I can view the natural language transformation summary at the project level to understand AWS Transform output with project-level granularity. The summary provides me with an overview of updates along with key technical changes to the codebase.

[![detailed report of transformed project highlighting transformation summary of one of the project](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/15/trans-sum.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/15/trans-sum.png)

**Other new features**

Let’s have a quick look at other new features we’ve added with general availability:

* **Support for porting UI layer** – During preview, you could only port the business logic layers of MVC applications using AWS Transform, and you had to port the UI layer manually. With general availability, you can now use AWS Transform to port MVC Razor views to ASP.NET Core Razor views.
* **Expanded connector support** – During preview, you could connect only to GitHub repositories. Now with general availability, you can connect to GitHub, GitLab, and Bitbucket repositories.
* **Cross repository dependency** – When you select a repository for transformation, dependent repositories are automatically selected for transformation.
* **Download assessment report** – You can download a detailed assessment report of the identified repositories in your account and private NuGet packages referenced in these repositories.
* **Email notifications with deep links** – You’ll receive email notifications when a job’s status changes to completed or stopped. These notifications include deep links to the transformed code branches for review and continued transformation in your IDE.

**Things to know**

Some additional things to know are:

* **Regions** – AWS Transform for .NET is generally available today in the Europe (Frankfurt) and US East (N. Virginia) [Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region).
* **Pricing** – Currently, there is [no additional charge](https://aws.amazon.com/transform/pricing/) for AWS Transform. Any resources you create or continue to use in your AWS account using the output of AWS Transform will be billed according to their standard pricing. For limits and quotas, refer to the [documentation](https://docs.aws.amazon.com/transform/latest/userguide/load-balancer-limits.html).
* **.NET versions supported** – AWS Transform for .NET supports transforming applications written using .NET Framework versions 3.5+, .NET Core 3.1, and .NET 5+, and the cross-platform .NET version, .NET 8.
* **Application types supported** – AWS Transform for .NET supports porting C# code projects of the following types: console application, class library, unit tests, WebAPI, Windows Communication Foundation (WCF) service, MVC, and single-page application (SPA).
* **Getting started** – To get started, visit AWS Transform for .NET [User Guide](https://docs.aws.amazon.com/transform/latest/userguide/dotnet.html).
* **Webinar** – Join the webinar [Accelerate .NET Modernization with Agentic AI](https://pages.awscloud.com/NAMER-field-OE-AWS-Transform-NET-2025-reg-event.html) to experience AWS Transform for .NET through a live demonstration.

– [Prasad](https://www.linkedin.com/in/kprasadrao/)

---

How is the News Blog doing? Take this [1 minute survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi)!

*(This [survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi) is hosted by an external company. AWS handles your information as described in the [AWS Privacy Notice](https://aws.amazon.com/privacy/?trk=4b29643c-e00f-4ab6-ab9c-b1fb47aa1708&sc_channel=blog). AWS will own the data gathered via this survey and will not share the information collected with survey respondents.)*

![Prasad Rao](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2020/08/20/pic.jpg)

### Prasad Rao

Prasad Rao is a Principal Partner Solutions Architect at AWS based out of UK. His focus areas are .NET Application Modernization and Windows Workloads on AWS. He leverages his experience to help AWS Partners across EMEA for their long term technical enablement to build scalable architecture on AWS. He also mentors diverse people who are new to cloud and would like to get started on AWS.

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