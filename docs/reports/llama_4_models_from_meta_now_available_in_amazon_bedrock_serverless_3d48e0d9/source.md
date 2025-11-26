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

# Llama 4 models from Meta now available in Amazon Bedrock serverless

by [Danilo Poccia](https://aws.amazon.com/blogs/aws/author/danilop/ "Posts by Danilo Poccia") on 28 APR 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Machine Learning](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Foundation models](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/generative-ai/foundation-models/ "View all posts in Foundation models"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/llama-4-models-from-meta-now-available-in-amazon-bedrock-serverless/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

The newest AI models from Meta, [Llama 4 Scout 17B and Llama 4 Maverick 17B](https://aws.amazon.com/bedrock/llama/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), are now available as a fully managed, serverless option in [Amazon Bedrock](https://aws.amazon.com/bedrock/). These new [foundation models (FMs)](https://aws.amazon.com/what-is/foundation-models/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) deliver natively multimodal capabilities with early fusion technology that you can use for precise image grounding and extended context processing in your applications.

Llama 4 uses an innovative mixture-of-experts (MoE) architecture that provides enhanced performance across reasoning and image understanding tasks while optimizing for both cost and speed. This architectural approach enables Llama 4 to offer improved performance at lower cost compared to Llama 3, with expanded language support for global applications.

The models were already [available on Amazon SageMaker JumpStart](https://aws.amazon.com/blogs/machine-learning/llama-4-family-of-models-from-meta-are-now-available-in-sagemaker-jumpstart/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), and you can now use them in Amazon Bedrock to streamline building and scaling [generative AI](https://aws.amazon.com/ai/generative-ai/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) applications with [enterprise-grade security and privacy](https://aws.amazon.com/bedrock/security-compliance/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el).

**Llama 4 Maverick 17B** – A natively multimodal model featuring 128 experts and 400 billion total parameters. It excels in image and text understanding, making it suitable for versatile assistant and chat applications. The model supports a 1 million token context window, giving you the flexibility to process lengthy documents and complex inputs.

**Llama 4 Scout 17B** – A general-purpose multimodal model with 16 experts, 17 billion active parameters, and 109 billion total parameters that delivers superior performance compared to all previous Llama models. Amazon Bedrock currently supports a 3.5 million token context window for Llama 4 Scout, with plans to expand in the near future.

**Use cases for Llama 4 models**

You can use the advanced capabilities of Llama 4 models for a wide range of use cases across industries:

**Enterprise applications** – Build intelligent agents that can reason across tools and workflows, process multimodal inputs, and deliver high-quality responses for business applications.

**Multilingual assistants** – Create chat applications that understand images and provide high-quality responses across multiple languages, making them accessible to global audiences.

**Code and document intelligence** – Develop applications that can understand code, extract structured data from documents, and provide insightful analysis across large volumes of text and code.

**Customer support** – Enhance support systems with image analysis capabilities, enabling more effective problem resolution when customers share screenshots or photos.

**Content creation** – Generate creative content across multiple languages, with the ability to understand and respond to visual inputs.

**Research** – Build research applications that can integrate and analyze multimodal data, providing insights across text and images.

**Using Llama 4 models in Amazon Bedrock** To use these new serverless models in Amazon Bedrock, I first need to request access. In the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), I choose **Model access** from the navigation pane to toggle access to **Llama 4 Maverick 17B** and **Llama 4 Scout 17B** models.

[![Console screenshot.](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/23/bedrock-llama4-model-access.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/23/bedrock-llama4-model-access.png)

The Llama 4 models can be easily integrated into your applications using the [Amazon Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), which provides a unified interface for conversational AI interactions.

Here’s an example of how to use the [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/) with Llama 4 Maverick for a multimodal conversation:

```
import boto3
import json
import os

AWS_REGION = "us-west-2"
MODEL_ID = "us.meta.llama4-maverick-17b-instruct-v1:0"
IMAGE_PATH = "image.jpg"

def get_file_extension(filename: str) -> str:
    """Get the file extension."""
    extension = os.path.splitext(filename)[1].lower()[1:] or 'txt'
    if extension == 'jpg':
        extension = 'jpeg'
    return extension

def read_file(file_path: str) -> bytes:
    """Read a file in binary mode."""
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except Exception as e:
        raise Exception(f"Error reading file {file_path}: {str(e)}")

bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name=AWS_REGION
)

request_body = {
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": "What can you tell me about this image?"
                },
                {
                    "image": {
                        "format": get_file_extension(IMAGE_PATH),
                        "source": {"bytes": read_file(IMAGE_PATH)},
                    }
                },
            ],
        }
    ]
}

response = bedrock_runtime.converse(
    modelId=MODEL_ID,
    messages=request_body["messages"]
)

print(response["output"]["message"]["content"][-1]["text"])
```

This example demonstrates how to send both text and image inputs to the model and receive a conversational response. The Converse API abstracts away the complexity of working with different model input formats, providing a consistent interface across models in Amazon Bedrock.

For more interactive use cases, you can also use the streaming capabilities of the Converse API:

```
response_stream = bedrock_runtime.converse_stream(
    modelId=MODEL_ID,
    messages=request_body['messages']
)

stream = response_stream.get('stream')
if stream:
    for event in stream:

        if 'messageStart' in event:
            print(f"\nRole: {event['messageStart']['role']}")

        if 'contentBlockDelta' in event:
            print(event['contentBlockDelta']['delta']['text'], end="")

        if 'messageStop' in event:
            print(f"\nStop reason: {event['messageStop']['stopReason']}")

        if 'metadata' in event:
            metadata = event['metadata']
            if 'usage' in metadata:
                print(f"Usage: {json.dumps(metadata['usage'], indent=4)}")
            if 'metrics' in metadata:
                print(f"Metrics: {json.dumps(metadata['metrics'], indent=4)}")
```

With streaming, your applications can provide a more responsive experience by displaying model outputs as they are generated.

**Things to know**

The Llama 4 models are available today with a fully managed, serverless experience in [Amazon Bedrock](https://aws.amazon.com/bedrock/) in the US East (N. Virginia) and US West (Oregon) [AWS Regions.](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) You can also access Llama 4 in US East (Ohio) via [cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el).

As usual with Amazon Bedrock, you pay for what you use. For more information, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el).

These models support 12 languages for text (English, French, German, Hindi, Italian, Portuguese, Spanish, Thai, Arabic, Indonesian, Tagalog, and Vietnamese) and English when processing images.

To start using these new models today, visit the [Meta Llama models section in the Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-meta.html?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el). You can also explore how our Builder communities are using Amazon Bedrock in their solutions in the generative AI section of our [community.aws](https://community.aws/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) site.

— [Danilo](https://x.com/danilop)

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