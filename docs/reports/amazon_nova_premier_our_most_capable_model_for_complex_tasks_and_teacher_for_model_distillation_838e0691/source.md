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

# Amazon Nova Premier: Our most capable model for complex tasks and teacher for model distillation

by [Danilo Poccia](https://aws.amazon.com/blogs/aws/author/danilop/ "Posts by Danilo Poccia") on 30 APR 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Nova](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-nova/ "View all posts in Amazon Nova"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/amazon-nova-premier-our-most-capable-model-for-complex-tasks-and-teacher-for-model-distillation/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today we’re [expanding the Amazon Nova family of foundation models announced at AWS re:Invent](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-frontier-intelligence-and-industry-leading-price-performance/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) with the general availability of [Amazon Nova Premier](https://aws.amazon.com/ai/generative-ai/nova/understanding/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), our most capable model for complex tasks and teacher for model distillation.

Nova Premier joins the existing [Amazon Nova understanding models](https://aws.amazon.com/ai/generative-ai/nova/understanding/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) available in [Amazon Bedrock](https://aws.amazon.com/bedrock/). Similar to Nova Lite and Pro, Premier can process input text, images, and videos (excluding audio). With its advanced capabilities, Nova Premier excels at complex tasks that require deep understanding of context, multistep planning, and precise execution across multiple tools and data sources. With a context length of one million tokens, Nova Premier can process extremely long documents or large code bases.

With Nova Premier and [Amazon Bedrock Model Distillation](https://aws.amazon.com/bedrock/model-distillation/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), you can create highly capable, cost-effective, and low-latency versions of Nova Pro, Lite, and Micro, for your specific needs. For example, we used Nova Premier to distill Nova Pro for complex tool selection and API calling. The distilled Nova Pro had a 20% higher accuracy for API invocations compared to the base model and consistently matched the performance of the teacher, with the speed and cost benefits of Nova Pro.

**Amazon Nova Premier benchmark evaluation** We evaluated Nova Premier on a broad range of benchmarks across text intelligence, visual intelligence, and agentic workflows. Nova Premier is the most capable model in the Nova family as measured across 17 benchmarks as shown in the table below.

[![Amazon Nova Premier Benchmark Evaluations](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/30/nova-premier-pro-benchmark-evaluations2-538x1024.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/30/nova-premier-pro-benchmark-evaluations2.png)

Nova Premier is also comparable to the best non-reasoning models in the industry and is equal or better on approximately half of these benchmarks when compared to other models in the same intelligence tier. Details of these evaluations are in the [technical report](http://amazon.science/publications/amazon-nova-premier-technical-report-and-model-card).

Nova Premier is also the fastest and the most cost-effective model in Amazon Bedrock for its intelligence tier. For further details and comparison on pricing, please refer to the [Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/).

Nova Premier can also be used as a teacher model for distillation, which means you can transfer its advanced capabilities for a specific use case into smaller, faster, and more efficient models like Nova Pro, Micro, and Lite for production deployments.

**Using Amazon Nova Premier**

To get started with Nova Premier, you first need to request access to the model in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el). Navigate to **Model access** in the navigation pane, find**Nova Premier**, and toggle access.

[![Console screenshot.](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/28/nova-premier-model-access-2.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/28/nova-premier-model-access-2.png)

Once you have access, you can use Nova Premier through the [Amazon Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) providing in input a list of messages from the `user` and the `assistant`. Messages can include text, images, and videos. Here’s an example of a straightforward invocation using the [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el):

```
import boto3
import json

AWS_REGION = "us-east-1"
MODEL_ID = "us.amazon.nova-premier-v1:0"

bedrock_runtime = boto3.client('bedrock-runtime', region_name=AWS_REGION)
messages = [
    {
        "role": "user",
        "content": [
            {
                "text": "Explain the differences between vector databases and traditional relational databases for AI applications."
            }
        ]
    }
]

response = bedrock_runtime.converse(
    modelId=MODEL_ID,
    messages=messages
)

response_text = response["output"]["message"]["content"][-1]["text"]

print(response_text)
```

This example shows how Nova Premier can provide detailed explanations for complex technical questions. But the real power of Premier comes with its ability to handle sophisticated workflows.

**Multi-agent collaboration use case** Let’s explore a more complex scenario that showcases how Nova Premier works a multi-agent collaboration architecture for investment research.

The equity research process typically involves multiple stages: identifying relevant data sources for specific investments, retrieving required information from those sources, and synthesizing the data into actionable insights. This process becomes increasingly complex when dealing with different types of financial instruments like stock indices, individual equities, and currencies.

We can build this type of application using [multi-agent collaboration in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-announces-general-availability-of-multi-agent-collaboration/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), with Nova Premier powering the supervisor agent that orchestrates the entire workflow. The supervisor agent analyzes the initial query (for example, “What are the emerging trends in renewable energy investments?”), breaks it down into logical steps, determines which specialized subagents to engage, and synthesizes the final response.

For this scenario, I’ve created a system with the following components:

1. A supervisor agent powered by Nova Premier
2. Multiple specialized subagents powered by Nova Pro, each focusing on different financial data sources
3. Tools that connect to financial databases, market analysis tools, and other relevant information sources

[![Multi-agent architectural diagram](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/16/nova-premier-lauch-post.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/16/nova-premier-lauch-post.png)

When I submit a query about emerging trends in renewable energy investments, the supervisor agent powered by Nova Premier does the following:

1. Analyzes the query to determine the underlying topics and sources to cover
2. Selects the appropriate subagents specific to those topics and sources
3. Each subagent retrieves their relevant economic indicators, technical analysis, and market sentiment data
4. The supervisor agent synthesizes this information into a comprehensive report for review by a financial professional

Utilizing Nova Premier in a multi-agent collaboration architecture such as this streamlines the financial professional’s work and helps them formulate their investment analysis faster. The following video provides a visual description of this scenario.

The key advantage of using Nova Premier for the supervisor role is its accuracy in coordinating complex workflows, so that the right data sources are consulted in the optimal sequence and each subagent receives in input the correct information for their work, resulting in higher quality insights.

**Multi-agent collaboration with model distillation**

Although Nova Premier provides the highest level of accuracy of its family of models, you might want to optimize latency and cost in production environments. This is where the strength of Nova Premier as a teacher model for distillation becomes interesting. Using [Amazon Bedrock Model Distillation](https://aws.amazon.com/bedrock/model-distillation/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), we can customize Nova Micro from the results of Nova Premier for this specific investment research use case.

Unlike traditional fine-tuning that requires human feedback and labeled examples, with model distillation you can generate high-quality training data by having a teacher model produce the desired outputs, streamlining the data acquisition process.

[![Amazon Bedrock Model Distillation diagram](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/16/nova-premier-bedrock-model-distillation-diagram.jpg)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/16/nova-premier-bedrock-model-distillation-diagram.jpg)

The process to [distill a model](https://aws.amazon.com/blogs/aws/build-faster-more-cost-efficient-highly-accurate-models-with-amazon-bedrock-model-distillation-preview/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) involves:

1. Generating synthetic training data by capturing input and output from Nova Premier runs across multiple financial instruments
2. Using this data as a reference to train a customized version of Nova Micro through custom fine-tuning tools
3. Evaluating the difference in latency and performance of the customized Micro model
4. Deploying the customized Micro model as the supervisor agent in production

With Amazon Bedrock, you can further streamline the process and [use invocation logs for data preparation](https://docs.aws.amazon.com/bedrock/latest/userguide/distillation-data-prep-option-2.html?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el). To do that, you need to set the model invocation logging on and set up an [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) bucket as the destination for the logs.

**Customer voices** Some of our customers had early access to Nova Premier. This is what they shared with us:

“Amazon Nova Premier has been outstanding in its ability to execute interactive analysis workflows, while still being faster and nearly half the cost compared to other leading models in our tests,” said [Curtis Allen](https://www.linkedin.com/in/curtis-allen-68425566/), Senior Staff Engineer at [Slack](https://slack.com/), a company bringing conversations, apps, and customers together in one place.

“Implementing new solutions built on top of Amazon Nova has helped us with our mission of democratizing finance for all,” said [Dev Tagare](https://www.linkedin.com/in/dev-tagare/), Head of AI and Data at [Robinhood Markets](https://robinhood.com/), a company on a mission to democratize finance for all. “We’re particularly excited about the ability to explore new avenues like complex multi-agent collaborations that are not just highly performing but also cost effective and fast. The intelligence of Nova Premier and what it can transfer to the other models like Nova Micro, Nova Lite, and Nova Pro unlocks multi-agent collaboration at a performance, price, and speed that will make it accessible to everyday customers.”

“Accelerating real-world AI deployments—not just prototypes—requires the ability to build models that are specialized for the unique needs of real world applications,” said [Henry Ehrenberg](https://www.linkedin.com/in/henry-kiss-ehrenberg-70049872/), co-founder of [Snorkel AI](https://snorkel.ai/), a technology company that empowers data scientists and developers to quickly turn data into accurate and adaptable AI applications. “We’re excited to see AWS pushing efficient model customization forward with Amazon Bedrock Model Distillation and Amazon Nova Premier. These new model capabilities have the potential to accelerate our enterprise customers in building production AI applications, including Q&A applications with multimodal data and more.”

**Things to know** Nova Premier is available in Amazon Bedrock in the US East (N. Virginia), US East (Ohio), and US West (Oregon) [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) today via [cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html). With Amazon Bedrock, you only pay for what you use. For more information, visit [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el).

Customers in the US can also access Amazon Nova models at [https://nova.amazon.com](https://nova.amazon.com?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), a website to easily explore our FMs.

Nova Premier is our best teacher for distilling custom variants of Nova Pro, Micro, and Lite, which means you can capture the capabilities offered by Premier in smaller, faster models for production deployment.

Nova Premier includes built-in safety controls to promote [responsible AI](https://aws.amazon.com/ai/responsible-ai/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) use, with content moderation capabilities that help maintain appropriate outputs across a wide range of applications.

To get started with Nova Premier, visit the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) today. For more information, see the [Amazon Nova User Guide](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) and send feedback to [AWS re:Post for Amazon Bedrock](https://repost.aws/tags/TAQeKlaPaNRQ2tWB6P7KrMag/amazon-bedrock?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el). Explore the generative AI section of our [community.aws](https://community.aws/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) site to see how our Builder communities are using Amazon Bedrock in their solutions.

– [Danilo](https://x.com/danilop)

---

How is the News Blog doing? Take this [1 minute survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi)!

*(This [survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi) is hosted by an external company. AWS handles your information as described in the [AWS Privacy Notice](https://aws.amazon.com/privacy/?trk=4b29643c-e00f-4ab6-ab9c-b1fb47aa1708&sc_channel=blog). AWS will own the data gathered via this survey and will not share the information collected with survey respondents.)*

![Danilo Poccia](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2018/11/22/danilo.png)

### [Danilo Poccia](https://aws.amazon.com/blogs/aws/author/danilop/ "Posts by Danilo Poccia")

Danilo works with startups and companies of any size to support their innovation. In his role as Chief Evangelist (EMEA) at Amazon Web Services, he leverages his experience to help people bring their ideas to life, focusing on serverless architectures and event-driven programming, and on the technical and business impact of machine learning and edge computing. He is the author of AWS Lambda in Action from Manning.

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