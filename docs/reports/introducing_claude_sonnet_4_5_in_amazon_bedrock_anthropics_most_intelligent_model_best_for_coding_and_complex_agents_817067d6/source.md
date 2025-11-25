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

# Introducing Claude Sonnet 4.5 in Amazon Bedrock: Anthropic’s most intelligent model, best for coding and complex agents

by Matheus Guimaraes on 29 SEP 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Machine Learning](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/introducing-claude-sonnet-4-5-in-amazon-bedrock-anthropics-most-intelligent-model-best-for-coding-and-complex-agents/)  [Comments](https://aws.amazon.com/blogs/aws/introducing-claude-sonnet-4-5-in-amazon-bedrock-anthropics-most-intelligent-model-best-for-coding-and-complex-agents/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re excited to announce that [Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5), powered by Anthropic, is now available in [Amazon Bedrock](https://aws.amazon.com/bedrock/), a fully managed service that offers a choice of high- performing foundation models from leading AI companies. This new model builds upon Claude 4’s foundation to achieve state-of-the-art performance in coding and complex agentic applications.

Claude Sonnet 4.5 demonstrates advancements in agent capabilities, with enhanced performance in tool handling, memory management, and context processing. The model shows marked improvements in code generation and analysis, from identifying optimal improvements to exercising stronger judgment in refactoring decisions. It particularly excels at autonomous long-horizon coding tasks, where it can effectively plan and execute complex software projects spanning hours or days while maintaining consistent performance and reliability throughout the development cycle.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/29/Sonnet_4-5_Eval_Blog.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/29/Sonnet_4-5_Eval_Blog.png)

Source: <https://www.anthropic.com/news/claude-sonnet-4-5>

By using Claude Sonnet 4.5 in Amazon Bedrock, developers gain access to a fully managed service that not only provides a unified API for foundation models but ensures their data stays under complete control with enterprise-grade tools for security, and optimization.

Claude Sonnet 4.5 also seamlessly integrates with [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el), enabling developers to maximize the model’s capabilities for building complex agents. AgentCore’s purpose-built infrastructure complements the model’s enhanced abilities in tool handling, memory management, and context understanding. Developers can leverage complete session isolation, 8-hour long-running support, and comprehensive observability features to deploy and monitor production-ready agents from autonomous security operations to complex enterprise workflows.

**Business applications and use cases** Beyond its technical capabilities, Sonnet 4.5 delivers practical business value through consistent performance and advanced problem-solving abilities. The model excels at producing and editing business documents while maintaining reliable performance across complex workflows.

The model demonstrates strength in several key industries:

* Cybersecurity – Claude Sonnet 4.5 can be used to deploy agents that autonomously patch vulnerabilities before exploitation, shifting from reactive detection to proactive defense.
* Finance – Sonnet 4.5 handles everything from entry-level financial analysis to advanced predictive analysis, helping transform manual audit preparation into intelligent risk management.
* Research – Sonnet 4.5 can better handle tools, context, and deliver ready-to-go office files to drive expert analysis into final deliverables and actionable insights.

**Sonnet 4.5 features in the Amazon Bedrock API**

Here are some highlights of Sonnet 4.5 in the Amazon Bedrock API:

**Smart Context Window Management** – The new API introduces intelligent handling when AI models reach their maximum capacity. Instead of returning errors when conversations get too long, Claude Sonnet 4.5 will now generate responses up to the available limit and clearly indicate why it stopped. This eliminates frustrating interruptions and allows users to maximize their available context window.

**Tool Use Clearing for Efficiency** – Claude Sonnet 4.5 enables automatic cleanup of tool interaction history during long conversations. When conversations involve multiple tool calls, the system can automatically remove older tool results while preserving recent ones. This keeps conversations efficient and prevents unnecessary token consumption, reducing costs while maintaining conversation quality.

**Cross-Conversation Memory** – A new memory capability enables Sonnet 4.5 to remember information across different conversations through the use of a local memory file. Users can explicitly ask the model to remember preferences, context, or important information that persists beyond a single chat session. This creates more personalized and contextually aware interactions while keeping the information safe within the local file.

With these new capabilities for managing context, developers can build AI agents capable of handling long-running tasks at higher intelligence without hitting context limits or losing critical information as frequently.

**Getting started** To begin working with Claude Sonnet 4.5, you can access it through Amazon Bedrock using the correct model ID. A good practice is to use the [Amazon Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) to write code once and seamlessly switch between different models, making it easier to experiment with Sonnet 4.5 or any of the other models available in Amazon Bedrock.

Let’s see this in action with a simple example. I’m going to use the Amazon Bedrock Converse API to send a prompt to Sonnet 4.5. I start by importing the modules I’m going to use. For this short example, I only need [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) so I can create a BedrockRuntimeClient. I’m also importing the rich package so I can format my output nicely later on.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/23/import-modules.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/23/import-modules.png)

Following best practices, I create a boto3 session and create an Amazon Bedrock client from it instead of creating one directly. This gives you explicit control over configuration, improves thread safety, and makes your code more predictable and testable compared to relying on the default session.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/23/creating-bedrock-client.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/23/creating-bedrock-client.png)

I want to give the model something with a bit of complexity instead of asking a simple question to demonstrate the power of Sonnet 4.5. So I’m going to give the model the current state of an imaginary legacy monolithic application written in Java with a single database and ask for a digital transformation plan which includes a migration strategy, risk assessment, estimated timeline and key milestones and specific AWS services recommendations.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/23/full-prompt-2.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/23/full-prompt-2.png)

Because the prompt is quite long I put it in a text file locally and just load it up in code. I then set up the Amazon Bedrock converse payload setting the role to “user” to indicate that this is a message by the user of the application and add the prompt to the content.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/23/converse-request-payload.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/23/converse-request-payload.png)

This is where the magic happens! We put it all together and call Claude Sonnet 4.5 using its model ID. Well, kind of. You can only access Sonnet 4.5 through an inference profile. This defines which AWS Regions will process your model requests and helps manage throughput and performance.

For this demo, I’ll be using one of Amazon Bedrock’s system-defined cross-Region inference profiles, which automatically routes requests across multiple Regions for optimal performance.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/29/sonnet-4.5-inference-profile-marked.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/29/sonnet-4.5-inference-profile-marked.png)

Now I just need to print to the screen to see the results. This is where I use the rich package I imported earlier just so we may have a nicely formatted output as I’m expecting a long response for this one. I also save the output to a file so I can have it handy as something to share with my teams.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/23/printing-results.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/23/printing-results.png)

Ok, let’s check the results! As expected, Sonnet 4.5 worked through my requirements and provided extensive and deep guidance for my digital transformation plan that I could start putting into practice. It included an executive summary, a step-by-step migration strategy split into phases with time estimates, and even some code samples to seed the development process and start breaking things down into microservices. It also provided the business cases for introducing technology and recommended the correct AWS services for each scenario. Here are some highlights from the report.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/23/output-highlights.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/23/output-highlights.png)

Claude Sonnet 4.5 is able to maintain consistency while delivering creative solutions making it an ideal choice for businesses seeking to use AI for complex problem-solving and development tasks. Its enhanced capabilities in following directions and using tools effectively translate into more reliable and innovative solutions across various business contexts.

**Things to know** Claude Sonnet 4.5 represents a significant step forward in agent capabilities, particularly excelling in areas where consistent performance and creative problem-solving are essential. Its enhanced abilities in tool handling, memory management, and context processing make it particularly valuable across key industries such as finance, research, and cybersecurity. Whether handling complex development lifecycles, executing long-running tasks, or tackling business-critical workflows, Claude Sonnet 4.5 combines technical excellence with practical business value.

Claude Sonnet 4.5 is available today. For [detailed information about its availability](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) please visit the documentation.

To learn more about Amazon Bedrock explore our self-paced [Amazon Bedrock Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/a4bdb007-5600-4368-81c5-ff5b4154f518/en-US?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) and discover how to use available models and their capabilities in your applications.

![Matheus Guimaraes](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/16/me_standing_outdoor-square-2.jpg)

### Matheus Guimaraes

Matheus Guimaraes (@codingmatheus) is a digital transformation specialist focused on AI adoption and microservices architecture. An international keynote speaker with over 20 years in tech, he’s worn many hats: from junior game programmer to CTO and tech co-founder. Matheus has helped companies of all sizes modernize and scale their systems, leading transformation programs and designing cloud-native, AI-ready architectures. Today, he shares his expertise globally through talks, blogs, and videos, passionate about helping others grow in the industry. Outside his professional life, he’s a gamer, swimmer, musician, and firm believer in the powerful intersection of creativity and technology.

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