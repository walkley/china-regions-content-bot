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

# Amazon Q Developer elevates the IDE experience with new agentic coding experience

by Elizabeth Fuentes on 02 MAY 2025 in [Amazon Q Developer](https://aws.amazon.com/blogs/aws/category/amazon-q/amazon-q-developer/ "View all posts in Amazon Q Developer"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS CLI](https://aws.amazon.com/blogs/aws/category/programing-language/aws-cli/ "View all posts in AWS CLI"), [Developer Tools](https://aws.amazon.com/blogs/aws/category/developer-tools/ "View all posts in Developer Tools"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/amazon-q-developer-elevates-the-ide-experience-with-new-agentic-coding-experience/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, [Amazon Q Developer](https://aws.amazon.com/q/developer/?trk=4f1e9f0e-7b21-4369-8925-61f67341d27c&sc_channel=el) introduces a new, interactive, agentic coding experience that is now available in the [integrated development environments (IDE)](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE.html?trk=4f1e9f0e-7b21-4369-8925-61f67341d27c&sc_channel=el) for [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode). This experience brings interactive coding capabilities, building upon existing prompt-based features. You now have a natural, real-time collaborative partner working alongside you while writing code, creating documentation, running tests, and reviewing changes.

Amazon Q Developer transforms how you write and maintain code by providing transparent reasoning for its suggestions and giving you the choice between automated modifications or step-by-step confirmation of changes. As a daily user of [Amazon Q Developer command line interface (CLI) agent](https://aws.amazon.com/q/developer/build/), I’ve experienced firsthand how Amazon Q Developer chat interface makes software development a more efficient and intuitive process. Having an AI-powered assistant only a `q chat` away in CLI has streamlined my daily development workflow, enhancing the coding process.

The new agentic coding experience in Amazon Q Developer in the IDE seamlessly interacts with your local development environment. You can read and write files directly, execute bash commands, and engage in natural conversations about your code. Amazon Q Developer comprehends your codebase context and helps complete complex tasks through natural dialog, maintaining your workflow momentum while increasing development speed.

**Let’s see it in action**

To begin using Amazon Q Developer for the first time, follow the steps in the [Getting Started with Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/getting-started-q-dev.html) guide to access Amazon Q Developer. When using Amazon Q Developer, you can choose between [Amazon Q Developer Pro](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-pro-tier.html), a paid subscription service, or [Amazon Q Developer Free tier](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-free-tier.html) with [AWS Builder ID](https://community.aws/builderid?trk=4f1e9f0e-7b21-4369-8925-61f67341d27c&sc_channel=el) user authentication.

For existing users, update to the new version. Refer to [Using Amazon Q Developer in the IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE.html) for activation instructions.

To start, I select the Amazon Q icon in my IDE to open the chat interface. For this demonstration, I’ll create a web application that transforms Jupiter notebooks from the [Amazon Nova sample repository](https://github.com/aws-samples/amazon-nova-samples?trk=4f1e9f0e-7b21-4369-8925-61f67341d27c&sc_channel=code) into interactive applications.

I send the following prompt: `In a new folder, create a web application for video and image generation that uses the notebooks from multimodal-generation/workshop-sample as examples to create the applications. Adapt the code in the notebooks to interact with models. Use existing model IDs`

Amazon Q Developer then examines the ﬁles: the README file, notebooks, notes, and everything that is in the folder where the conversation is positioned. In our case it’s at the root of the repository.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/02/AWSNEWS-2205_01-1024x740.jpg)

After completing the repository analysis, Amazon Q Developer initiates the application creation process. Following the prompt requirements, it requests permission to execute the bash command for creating necessary folders and files.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/02/AWSNEWS-2205_03-1024x908.jpg)

With the folder structure in place, Amazon Q Developer proceeds to build the complete web application.

In a few minutes, the application is complete. Amazon Q Developer provides the application structure and deployment instructions, which can be converted into a README file upon request in the chat.

![](https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2025/AWSNEWS-2205_03.gif)

During my initial attempt to run the application, I encountered an error. I described it in Spanish using Amazon Q chat.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/02/AWSNEWS-2205_04-1024x737.jpg)

Amazon Q Developer responded in Spanish and gave me the solutions and code modifications in Spanish! I loved it!

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/02/AWSNEWS-2205_05-1-1024x742.jpg)

After implementing the suggested fixes, the application ran successfully. Now I can create, modify, and analyze images and videos using [Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/) through this newly created interface.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/24/Screenshot-2025-04-24-at-6.12.02 PM-1024x696.png)

The preceding images showcase my application’s output capabilities. Because I asked to modify the video generation code in Spanish, it gave me the message in Spanish.

| ![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/24/generated-video-1024x704.jpg) | ![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/24/image-1024x702.jpg) |
| --- | --- |

**Things to know**

**Chatting in natural languages** – Amazon Q Developer IDE supports many languages, including English, Mandarin, French, German, Italian, Japanese, Spanish, Korean, Hindi, and Portuguese. For detailed information, visit the [Amazon Q Developer User Guide page](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html).

**Collaboration and understanding** – The system examines your repository structure, files, and documentation while giving you the flexibility to interact seamlessly through natural dialog with your local development environment. This deep comprehension allows for more accurate and contextual assistance during development tasks.

**Control and transparency** – Amazon Q Developer provides continuous status updates as it works through tasks and lets you choose between automated code modifications or step-by-step review, giving you complete control over the development process.

**Availability –** Amazon Q Developer interactive, agentic coding experience is now available in the IDE for Visual Studio Code.

**Pricing**– Amazon Q Developer agentic chat is available in the IDE at no additional cost to both [Amazon Q Developer Pro Tier](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-pro-tier.html) and [Amazon Q Developer Free tier](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-free-tier.html) users. For detailed pricing information, visit the [Amazon Q Developer pricing page](https://aws.amazon.com/q/developer/pricing).

To learn more about getting started visit the [Amazon Q Developer product web page](https://aws.amazon.com/q/developer/).

— [Eli](https://www.linkedin.com/in/lizfue/)

---

How is the News Blog doing? Take this [1 minute survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi)!

*(This [survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi) is hosted by an external company. AWS handles your information as described in the [AWS Privacy Notice](https://aws.amazon.com/privacy/?trk=4b29643c-e00f-4ab6-ab9c-b1fb47aa1708&sc_channel=blog). AWS will own the data gathered via this survey and will not share the information collected with survey respondents.)*

![Elizabeth Fuentes](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2024/06/03/Elizabeth-Fuentas.jpeg)

### Elizabeth Fuentes

My mission is to break down complex concepts into easily digestible explanations, inspiring developers to continually expand their skills and knowledge. Through conferences, tutorials, and online resources, I share my expertise with the global developer community, providing them with the tools and confidence to reach their full potential. With a hands-on approach and a commitment to simplifying the complex, I strive to be a catalyst for growth and learning in the world of AWS technology.

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