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

# OpenAI open weight models now available on AWS

by [Danilo Poccia](https://aws.amazon.com/blogs/aws/author/danilop/ "Posts by Danilo Poccia") on 05 AUG 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Machine Learning](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Amazon SageMaker](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/sagemaker/ "View all posts in Amazon SageMaker"), [Amazon SageMaker JumpStart](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/sagemaker/amazon-sagemaker-jumpstart/ "View all posts in Amazon SageMaker JumpStart"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Open Source](https://aws.amazon.com/blogs/aws/category/open-source/ "View all posts in Open Source") [Permalink](https://aws.amazon.com/blogs/aws/openai-open-weight-models-now-available-on-aws/)  [Comments](https://aws.amazon.com/blogs/aws/openai-open-weight-models-now-available-on-aws/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

***September 3, 2025: The sample code has been updated to use streaming and tools.***

***September 18, 2025: Removing the model access request section because no longer required.***

AWS is committed to bringing you the most advanced [foundation models (FMs)](https://aws.amazon.com/what-is/foundation-models/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) in the industry, continuously expanding our selection to include groundbreaking models from leading AI innovators so that you always have access to the latest advancements to drive your business forward.

Today, I am happy to announce the availability of two new [OpenAI models with open weights](https://aws.amazon.com/bedrock/openai/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) in [Amazon Bedrock](https://aws.amazon.com/bedrock/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) and [Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker-ai/jumpstart/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el). OpenAI [**gpt-oss-120b** and **gpt-oss-20b**](https://openai.com/index/introducing-gpt-oss) models are designed for text generation and reasoning tasks, offering developers and organizations new options to build AI applications with complete control over their infrastructure and data.

These open weight models excel at coding, scientific analysis, and mathematical reasoning, with performance comparable to leading alternatives. Both models support a 128K context window and provide adjustable reasoning levels (low/medium/high) to match your specific use case requirements. The models support external tools to enhance their capabilities and can be used in an agentic workflow, for example, using a framework like [Strands Agents](https://strandsagents.com/).

With Amazon Bedrock and Amazon SageMaker JumpStart, AWS gives you the freedom to innovate with access to hundreds of FMs from leading AI companies, including OpenAI open weight models. With our comprehensive selection of models, you can match your AI workloads to the perfect model every time.

Through Amazon Bedrock, you can seamlessly experiment with different models, mix and match capabilities, and switch between providers without rewriting code—turning [model choice](https://aws.amazon.com/bedrock/model-choice/) into a strategic advantage that helps you continuously evolve your AI strategy as new innovations emerge. These new models are available in Bedrock via an OpenAI-compatible endpoint. You can point the OpenAI SDK to this endpoint or use the Bedrock [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) and [Converse API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html).

With SageMaker JumpStart, you can quickly evaluate, compare, and customize models for your use case. You can then deploy the original or the customized model in production with the SageMaker AI console or using the [SageMaker Python SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-python-sdk.html).

Let’s see how these work in practice.

**Getting started with OpenAI open weight models in Amazon Bedrock** In the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), I use the **Chat/Test** playground to test and evaluate the models. I select **OpenAI** as the category and then the **gpt-oss-120b** model.

![Console screenshot](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/08/05/openai-gpt-model-selection.png)

Using this model, I run the following sample prompt:

*A family has $5,000 to save for their vacation next year. They can place the money in a savings account earning 2% interest annually or in a certificate of deposit earning 4% interest annually but with no access to the funds until the vacation. If they need $1,000 for emergency expenses during the year, how should they divide their money between the two options to maximize their vacation fund?*

This prompt generates an output that includes the chain of thought used to produce the result.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/08/06/2025-openai-models-bedrock-chat-playground-1.jpg)

I can use these models with the OpenAI SDK by configuring the API endpoint (base URL) and using an [Amazon Bedrock API key](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) for authentication. For example, I set this environment variables to use the US West (Oregon) AWS Region endpoint (`us-west-2`) and my Amazon Bedrock API key:

```
export OPENAI_API_KEY="<my-bedrock-api-key>"
export OPENAI_BASE_URL="https://bedrock-runtime.us-west-2.amazonaws.com/openai/v1"
```

Now I invoke the model using the OpenAI Python SDK.

```
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    messages=[{ "role": "user", "content": "Tell me the square root of 42 ^ 3" }],
    model="openai.gpt-oss-120b-1:0",
    stream=True
)

for item in response:
    print(item)
```

I save the code (`test-openai.py` file), install the dependencies, and run the agent locally:

```
pip install openai
python test-openai.py
```

To build an AI agent, I can choose any framework that supports the Amazon Bedrock API or the OpenAI API. For example, here’s the starting code for Strands Agents using the Amazon Bedrock API:

```
from strands import Agent
from strands.models import BedrockModel
from strands_tools import calculator

bedrock_model = BedrockModel(
    model_id="openai.gpt-oss-120b-1:0",
    region_name="us-west-2"
)

agent = Agent(
    model=bedrock_model,
    tools=[calculator]
)

agent("Tell me the square root of 42 ^ 3")
```

I save the code (`test-strands.py` file), install the dependencies, and run the agent locally:

```
pip install strands-agents strands-agents-tools
python test-strands.py
```

When I am satisfied with the agent, I can deploy in production using the [capabilities offered by Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), including a fully managed serverless runtime and memory and identity management.

**Getting started with OpenAI open weight models in Amazon SageMaker JumpStart** In the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), you can use OpenAI open weight models in the [SageMaker Studio](https://aws.amazon.com/sagemaker-ai/studio/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el). The first time I do this, I need to set up a SageMaker domain. There are options to set it up for a single user (simpler) or an organization. For these tests, I use a single user setup.

In the **SageMaker JumpStart** model view, I have access to a detailed description of the **gpt-oss-120b** or **gpt-oss-20b** model.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/08/06/2025-openai-models-sagemaker-js-model.jpg)

I choose the **gpt-oss-20b model** and then deploy the model. In the next steps, I select the instance type and the initial instance count. After a few minutes, the deployment creates an endpoint that I can then invoke in SageMaker Studio and using any [AWS SDKs](https://aws.amazon.com/tools/).

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/08/06/2025-openai-models-sagemaker-js.jpg)

To learn more, visit [GPT OSS models from OpenAI are now available on SageMaker JumpStart](https://aws.amazon.com/blogs/machine-learning/gpt-oss-models-from-openai-are-now-available-on-sagemaker-jumpstart/) in the AWS Artificial Intelligence Blog.

**Things to know** The new [OpenAI open weight models](https://aws.amazon.com/bedrock/openai/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) are now available in [Amazon Bedrock](https://aws.amazon.com/bedrock/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) in the US West (Oregon) [AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), while [Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker-ai/jumpstart/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) supports these models in US East (Ohio, N. Virginia) and Asia Pacific (Mumbai, Tokyo).

Each model comes equipped with full chain-of-thought output capabilities, providing you with detailed visibility into the model’s reasoning process. This transparency is particularly valuable for applications requiring high levels of interpretability and validation. These models give you the freedom to modify, adapt, and customize them to your specific needs. This flexibility allows you to fine-tune the models for your unique use cases, integrate them into your existing workflows, and even build upon them to create new, specialized models tailored to your industry or application.

Security and safety are built into the core of these models, with comprehensive evaluation processes and safety measures in place. The models maintain compatibility with the standard GPT-4 tokenizer.

Both models can be used in your preferred environment, whether that’s through the serverless experience of Amazon Bedrock or the extensive [machine learning (ML)](https://aws.amazon.com/ai/machine-learning/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) development capabilities of SageMaker JumpStart. For information about the costs associated with using these models and services, visit the [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) and [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker-ai/pricing/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) pages.

To learn more, see the [parameters for the models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-openai.html) and [how to invoke a model with the OpenAI Chat Completions API](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-chat-completions.html) in the Amazon Bedrock documentation.

Get started today with OpenAI open weight models on AWS in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) or in [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el).

– [Danilo](https://x.com/danilop)

![Danilo Poccia](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2018/11/22/danilo.png)

### [Danilo Poccia](https://aws.amazon.com/blogs/aws/author/danilop/ "Posts by Danilo Poccia")

Danilo works with startups and companies of any size to support their innovation. In his role as Chief Evangelist (EMEA) at Amazon Web Services, he leverages his experience to help people bring their ideas to life, focusing on serverless architectures and event-driven programming, and on the technical and business impact of machine learning and edge computing. He is the author of AWS Lambda in Action from Manning.

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