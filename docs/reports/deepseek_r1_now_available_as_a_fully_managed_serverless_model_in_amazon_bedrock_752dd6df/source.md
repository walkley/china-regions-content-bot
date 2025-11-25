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

# DeepSeek-R1 now available as a fully managed serverless model in Amazon Bedrock

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 10 MAR 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Machine Learning](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/deepseek-r1-now-available-as-a-fully-managed-serverless-model-in-amazon-bedrock/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

As of January 30, DeepSeek-R1 models became [available in Amazon Bedrock](https://aws.amazon.com/blogs/aws/deepseek-r1-models-now-available-on-aws/) through the [Amazon Bedrock Marketplace](https://aws.amazon.com/bedrock/marketplace/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and [Amazon Bedrock Custom Model Import](https://aws.amazon.com/bedrock/custom-model-import/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). Since then, thousands of customers have deployed these models in Amazon Bedrock. Customers value the robust guardrails and comprehensive tooling for safe AI deployment. Today, we’re making it even easier to use [DeepSeek in Amazon Bedrock](https://aws.amazon.com/bedrock/deepseek?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) through an expanded range of options, including a new serverless solution.

The fully managed DeepSeek-R1 model is now generally available in Amazon Bedrock. [Amazon Web Services (AWS)](https://aws.amazon.com/) is the first cloud service provider (CSP) to deliver DeepSeek-R1 as a fully managed, generally available model. You can accelerate innovation and deliver tangible business value with DeepSeek on AWS without having to manage infrastructure complexities. You can power your [generative AI](https://aws.amazon.com/generative-ai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) applications with DeepSeek-R1’s capabilities using a [single API](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the Amazon Bedrock’s fully managed service and get the benefit of its extensive features and tooling.

According to [DeepSeek](https://www.deepseek.com/), their model is publicly available under MIT license and offers strong capabilities in reasoning, coding, and natural language understanding. These capabilities power intelligent decision support, software development, mathematical problem-solving, scientific analysis, data insights, and comprehensive knowledge management systems.

As is the case for all AI solutions, give careful consideration to data privacy requirements when implementing in your production environments, check for bias in output, and monitor your results. When implementing publicly available models like DeepSeek-R1, consider the following:

* **Data security** – You can access the [enterprise-grade security](https://aws.amazon.com/bedrock/security-compliance/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), monitoring, and cost control features of Amazon Bedrock that are essential for [deploying AI responsibly at scale](https://aws.amazon.com/ai/responsible-ai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), all while retaining complete control over your data. Users’ inputs and model outputs aren’t shared with any model providers. You can use these [key security features](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) by default, including data encryption at rest and in transit, fine-grained access controls, secure connectivity options, and download [various compliance certifications](https://aws.amazon.com/compliance/services-in-scope/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) while communicating with the DeepSeek-R1 model in Amazon Bedrock.
* **Responsible AI** – You can implement safeguards customized to your application requirements and responsible AI policies with [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/). This includes key features of content filtering, sensitive information filtering, and customizable security controls to prevent hallucinations using contextual grounding and [Automated Reasoning checks](https://aws.amazon.com/blogs/aws/prevent-factual-errors-from-llm-hallucinations-with-mathematically-sound-automated-reasoning-checks-preview/). This means you can control the interaction between users and the DeepSeek-R1 model in Bedrock with your defined set of policies by filtering undesirable and harmful content in your generative AI applications.
* **Model evaluation** – You can evaluate and compare models to identify the optimal model for your use case, including DeepSeek-R1, in a few steps through either automatic or human evaluations by using [Amazon Bedrock model evaluation tools](https://aws.amazon.com/blogs/aws/amazon-bedrock-model-evaluation-is-now-generally-available/). You can choose automatic evaluation with predefined metrics such as accuracy, robustness, and toxicity. Alternatively, you can choose human evaluation workflows for subjective or custom metrics such as relevance, style, and alignment to brand voice. Model evaluation provides built-in curated datasets, or you can bring in your own datasets.

We strongly recommend integrating Amazon Bedrock Guardrails and using Amazon Bedrock model evaluation features with your DeepSeek-R1 model to add robust protection for your generative AI applications. To learn more, visit [Protect your DeepSeek model deployments with Amazon Bedrock Guardrails](https://aws.amazon.com/blogs/machine-learning/protect-your-deepseek-model-deployments-with-amazon-bedrock-guardrails/) and [Evaluate the performance of Amazon Bedrock resources](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

**Get started with the DeepSeek-R1 model in Amazon Bedrock**

If you’re new to using DeepSeek-R1 models, go to the [Amazon Bedrock console](https://us-west-2.console.aws.amazon.com/bedrock/home?region=us-west-2#modelaccess&trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), choose **Model access** under **Bedrock configurations** in the left navigation pane. To access the fully managed DeepSeek-R1 model, request access for **DeepSeek-R1** in **DeepSeek**. You’ll then be granted access to the model in Amazon Bedrock.

![1. Access DeepSeek-R1 model](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/03/11/2025-deepseek-r1-on-bedrock-1-model-access-1.jpg)

Next, to test the DeepSeek-R1 model in Amazon Bedrock, choose **Chat/Text** under **Playgrounds** in the left menu pane. Then choose **Select model** in the upper left, and select **DeepSeek** as the category and **DeepSeek-R1** as the model. Then choose **Apply**.

![2. Select DeepSeek-R1 model](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/03/11/2025-deepseek-r1-on-bedrock-2-select-model.jpg)

Using the selected **DeepSeek-R1** model, I run the following prompt example:

`A family has $5,000 to save for their vacation next year. They can place the money in a savings account earning 2% interest annually or in a certificate of deposit earning 4% interest annually but with no access to the funds until the vacation. If they need $1,000 for emergency expenses during the year, how should they divide their money between the two options to maximize their vacation fund?`

This prompt requires a complex chain of thought and produces very precise reasoning results.

![3. Test DeepSeek-R1 in the Chat Playground](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/03/11/2025-deepseek-r1-on-bedrock-3-chat-playground-1.gif)

To learn more about usage recommendations for prompts, refer to the [DeepSeek-R1 model prompt guide](https://api-docs.deepseek.com/guides/reasoning_model.html).

By choosing **View API request**, you can also access the model using code examples in the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and [AWS SDK](https://aws.amazon.com/developer/tools/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). You can use `us.deepseek.r1-v1:0` as the model ID.

Here is a sample of the AWS CLI command:

```
aws bedrock-runtime invoke-model \
       --model-id us.deepseek.r1-v1:0 \
       --body "{\"prompt\": \"<｜begin_of_sentence｜><｜User｜>Type_Your_Prompt_Here<｜Assistant｜><think>\n\", \"max_tokens\": 512, \"temperature\": 0.5, \"top_p\": 0.9}" \
       --cli-binary-format raw-in-base64-out \
       --region us-west-2 \
       invoke-model-output.txt
```

The model supports both the `InvokeModel` and `Converse` API. The following Python code examples show how to send a text message to the DeepSeek-R1 model using the [Amazon Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for text generation. To learn more, visit [DeepSeek model inference parameters and responses](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-deepseek.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the AWS documentation.

```
import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-west-2")

# Set the model ID, e.g., DeepSeek-R1 Model.
model_id = "us.deepseek.r1-v1:0"

# Start a conversation with the user message.
user_message = "Type_Your_Prompt_Here"
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```

To enable Amazon Bedrock Guardrails on the DeepSeek-R1 model, select **Guardrails** under **Safeguards** in the left navigation pane, and create a guardrail by configuring as many filters as you need. For example, if you filter for “politics” word, your guardrails will recognize this word in the prompt and show you the blocked message.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/03/11/2025-deepseek-r1-on-bedrock-4-guardrails.png)

You can test the guardrail with different inputs to assess the guardrail’s performance. You can refine the guardrail by setting denied topics, word filters, sensitive information filters, and blocked messaging until it matches your needs.

To learn more about Amazon Bedrock Guardrails, visit [Stop harmful content in models using Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the AWS documentation or other [deep dive blog posts about Amazon Bedrock Guardrails](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-bedrock-guardrails/) on the AWS Machine Learning Blog channel.

Here’s a [demo walkthrough](https://www.youtube.com/watch?v=W3FbSYFevZ4) highlighting how you can take advantage of the fully managed DeepSeek-R1 model in Amazon Bedrock:

**Now available**

DeepSeek-R1 is now available fully managed in Amazon Bedrock in the US East (N. Virginia), US East (Ohio), and US West (Oregon) AWS Regions through [cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html). Check the [full Region list](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for future updates. To learn more, check out the [DeepSeek in Amazon Bedrock product page](https://aws.amazon.com/bedrock/deepseek?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and the [Amazon Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/).

Give the DeepSeek-R1 model a try in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) today and send feedback to [AWS re:Post for Amazon Bedrock](https://repost.aws/tags/TAQeKlaPaNRQ2tWB6P7KrMag/amazon-bedrock) or through your usual AWS Support contacts.

— [Channy](https://twitter.com/channyun)

***Updated on March 10, 2025** — Fixed screenshots of model selection and model ID.*

***Updated on March 13, 2025** — Added guide links of [DeepSeek-R1 model prompts](https://api-docs.deepseek.com/guides/reasoning_model.html) and [model inference parameters and responses](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-deepseek.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).*

![Channy Yun (윤석찬)](https://d2908q01vomqb2.cloudfront.net/7b52009b64fd0a2a49e6d8a939753077792b0554/2020/06/05/channyun_400x400.jpg)

### [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)")

Channy is a Lead Blogger of AWS News Blog and Principal Developer Advocate for AWS Cloud. As an open web enthusiast and blogger at heart, he loves community-driven learning and sharing of technology.

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