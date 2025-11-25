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

# Anthropic’s Claude 3.7 Sonnet hybrid reasoning model is now available in Amazon Bedrock

by Esra Kayabali on 24 FEB 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/anthropics-claude-3-7-sonnet-the-first-hybrid-reasoning-model-is-now-available-in-amazon-bedrock/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

[Amazon Bedrock](https://aws.amazon.com/bedrock/) is expanding its foundation model (FM) offerings as the generative AI field evolves. Today, we’re excited to announce the availability of Anthropic’s [Claude 3.7 Sonnet](https://www.anthropic.com/news/claude-3-7-sonnet?utm_source=partner-aws&utm_medium=referral&utm_campaign=sonnet_3-7_launch) foundation model in Amazon Bedrock. As Anthropic’s most intelligent model to date, Claude 3.7 Sonnet stands out as their first hybrid reasoning model capable of producing quick responses or *extended thinking*, meaning it can work through difficult problems using careful, step-by-step reasoning. Additionally, today we are adding Claude 3.7 Sonnet to the list of models used by [Amazon Q Developer](https://aws.amazon.com/q/developer/). Amazon Q is built on Bedrock, and with Amazon Q you can use the most appropriate model for a specific task such as Claude 3.7 Sonnet, for more advanced coding workflows that enable developers to accelerate building across the entire software development lifecycle.

**Key highlights of Claude 3.7 Sonnet**

Here are several notable features and capabilities of Claude 3.7 Sonnet in Amazon Bedrock.

**The first Claude model with hybrid reasoning –** Claude 3.7 Sonnet takes a different approach to how models think. Instead of using separate models—one for quick answers and another for solving complex problems—Claude 3.7 Sonnet integrates reasoning as a core capability within a single model. This combination is more similar to how the human brain works. After all, we use the same brain whether we’re answering a simple question or solving a difficult puzzle.

The model has two modes—*standard* and *extended thinking* mode—which can be toggled in Amazon Bedrock. In *standard* mode, Claude 3.7 Sonnet is an improved version of Claude 3.5 Sonnet. In *extended thinking* mode, Claude 3.7 Sonnet takes additional time to analyze problems in detail, plan solutions, and consider multiple perspectives before providing a response, allowing it to make further gains in performance. You can control speed and cost by choosing when to use reasoning capabilities. Extended thinking tokens count towards the context window and are billed as output tokens.

**Anthropic’s most powerful model for coding** – Claude 3.7 Sonnet is state-of-the art for coding, excelling in understanding context and creative problem solving, and according to Anthropic, achieves an industry-leading 70.3% for *standard* mode on [SWE-bench Verified](https://www.swebench.com/#verified). Claude 3.7 Sonnet also performs better than Claude 3.5 Sonnet across the majority of benchmarks. These enhanced capabilities make Claude 3.7 Sonnet ideal for powering AI agents and complex workflows.

[![Claude 3.7 Sonnet benchmarks](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/02/24/3-7_benchmarks.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/02/24/3-7_benchmarks.png)

*Source: <https://www.anthropic.com/news/claude-3-7-sonnet>*

**Over 15x longer output capacity than its predecessor** – Compared to [Claude 3.5 Sonnet](https://aws.amazon.com/blogs/aws/anthropics-claude-3-5-sonnet-model-now-available-in-amazon-bedrock-the-most-intelligent-claude-model-yet/), this model offers significantly expanded output length. This enhanced capacity is particularly useful when you explicitly request more detail, ask for multiple examples, or request additional context or background information. To achieve long outputs, try asking for a detailed outline (for writing use cases, you can specify outline detail down to the paragraph level and include word count targets). Then, ask for the response to index its paragraphs to the outline and reiterate the word counts. Claude 3.7 Sonnet supports outputs up to 128K tokens long (up to 64K as generally available and up to 128K as a beta).

**Adjustable reasoning budget –** You can control the budget for thinking when you use Claude 3.7 Sonnet in Amazon Bedrock. This flexibility helps you weigh the trade-offs between speed, cost, and performance. By allocating more tokens to reasoning for complex problems or limiting tokens for faster responses, you can optimize performance for your specific use case.

**Claude 3.7 Sonnet in action**

As for any new model, I have to request access in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/). In the navigation pane, I choose **Model access** under Bedrock configurations. Then, I choose **Modify model access** to request access for Claude 3.7 Sonnet.

[![Base-models-showing-3-7-cross-region-inference](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/02/24/Base-models-showing-3-7-cross-region-inf.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/02/24/Base-models-showing-3-7-cross-region-inf.png)

To try Claude 3.7 Sonnet, I choose **Chat / Text** under **Playgrounds** in the navigation pane. Then I choose **Select model** and choose **Anthropic** under the **Categories** and **Claude 3.7 Sonnet** under the **Models**. To enable the *extended thinking* mode, I toggle **Model reasoning** under **Configurations**. I type the following prompt, and choose **Run**:

```
You're the manager of a small restaurant facing these challenges:

Three staff members called in sick for tonight's dinner service
You're expecting a full house (80 seats)
There's a large party of 20 coming at 7 PM
Your main chef is available but two kitchen helpers are among those who called in sick
You have 2 regular servers and 1 trainee available
How would you:

Reorganize the available staff to handle the situation
Prioritize tasks and service
Determine if you need to make any adjustments to reservations
Handle the large party while maintaining service quality
Minimize negative impact on customer experience
Explain your reasoning for each decision and discuss potential trade-offs
```

[![Chat / Text playground](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/02/22/2-LM1517.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/02/22/2-LM1517.png)

Here’s the result with an animated image showing the reasoning process of the model.

![Testing Claude 3.7 Sonnet reasoning](https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2025/LaunchMarketingIntake-1517.gif)

To test image-to-text vision capabilities, I upload an image of a detailed architectural site plan created using Amazon Bedrock. I receive a detailed analysis and reasoned insights of this site plan.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/02/23/output2-LM1517.gif)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/02/23/output2-LM1517.gif)

Claude 3.7 Sonnet can also be accessed through [AWS SDK](https://aws.amazon.com/developer/tools/) by using [Amazon Bedrock API](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html). To learn more about Claude 3.7 Sonnet’s features and capabilities, visit the [Anthropic’s Claude in Amazon Bedrock](https://aws.amazon.com/bedrock/claude/) product detail page.

**Get started with Claude 3.7 Sonnet today**

Claude 3.7 Sonnet’s enhanced capabilities can benefit multiple industry use cases. Businesses can create advanced AI assistants and agents that interact directly with customers. In fields such as healthcare, it can assist in medical imaging analysis and research summarization, and financial services can benefit from its abilities to solve complex financial modeling problems. For developers, it serves as a coding companion that can review code, explain technical concepts, and suggest improvements across different languages.

Anthropic’s Claude 3.7 Sonnet is available today in the US East (N. Virginia), US East (Ohio), and US West (Oregon) Regions. Check the [full Region list](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) for future updates.

Claude 3.7 Sonnet is priced competitively and matches the price of Claude 3.5 Sonnet. For pricing details, refer to the [Amazon Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/).

To get started with Claude 3.7 Sonnet in Amazon Bedrock, visit the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/) and [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html#acessing-api).

[— Esra](https://www.linkedin.com/in/esrakayabali/)

*2/24/2025: Base models screenshot updated.*

![Esra Kayabali](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/03/24/esrakayabali11-400x400-1.jpg)

### Esra Kayabali

Esra Kayabali is a Senior Solutions Architect at AWS, specialising in analytics, including data warehousing, data lakes, big data analytics, batch and real-time data streaming, and data integration. She has more than ten years of software development and solution architecture experience. She is passionate about collaborative learning, knowledge sharing, and guiding community in their cloud technologies journey.

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