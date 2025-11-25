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

# Writer Palmyra X5 and X4 foundation models are now available in Amazon Bedrock

by [Danilo Poccia](https://aws.amazon.com/blogs/aws/author/danilop/ "Posts by Danilo Poccia") on 28 APR 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Machine Learning](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Generative AI](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/writer-palmyra-x5-and-x4-foundation-models-are-now-available-in-amazon-bedrock/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

One thing we’ve witnessed in recent months is the expansion of context windows in [foundation models (FMs)](https://aws.amazon.com/what-is/foundation-models/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), with many now handling sequence lengths that would have been unimaginable just a year ago. However, building AI-powered applications that can process vast amounts of information while maintaining the reliability and security standards required for enterprise use remains challenging.

For these reasons, we’re excited to announce that [Writer Palmyra X5 and X4](https://aws.amazon.com/bedrock/writer/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) models are available today in [Amazon Bedrock](https://aws.amazon.com/bedrock/) as a fully managed, serverless offering. AWS is the first major cloud provider to deliver fully managed models from Writer. Palmyra X5 is a new model launched today by Writer. Palmyra X4 was previously available in [Amazon Bedrock Marketplace](https://aws.amazon.com/bedrock/marketplace/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el).

Writer Palmyra models offer robust reasoning capabilities that support complex agent-based workflows while maintaining enterprise security standards and reliability. Palmyra X5 features a one million token context window, and Palmyra X4 supports a 128K token context window. With these extensive context windows, these models remove some of the traditional constraints for app and agent development, enabling deeper analysis and more comprehensive task completion.

With this launch, Amazon Bedrock continues to bring access to the most advanced models and the tools you need to build generative AI applications with security, privacy, and [responsible AI](https://aws.amazon.com/ai/responsible-ai/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el).

As a pioneer in FM development, Writer trains and fine-tunes its industry leading models on [Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker-ai/hyperpod/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el). With its optimized distributed training environment, Writer reduces training time and brings its models to market faster.

**Palmyra X5 and X4 use cases** Palmyra X5 and X4 models excel in various enterprise use cases across multiple industries:

**Financial services** – Palmyra models power solutions across investment banking and asset and wealth management, including deal transaction support, 10-Q, 10-K and earnings transcript highlights, fund and market research, and personalized client outreach at scale.

**Healthcare and life science** – Payors and providers use Palmyra models to build solutions for member acquisition and onboarding, appeals and grievances, case and utilization management, and employer request for proposal (RFP) response. Pharmaceutical companies use these models for commercial applications, medical affairs, R&D, and clinical trials.

**Retail and consumer goods** – Palmyra models enable AI solutions for product description creation and variation, performance analysis, SEO updates, brand and compliance reviews, automated campaign workflows, and RFP analysis and response.

**Technology** – Companies across the technology sector implement Palmyra models for personalized and account-based marketing, content creation, campaign workflow automation, account preparation and research, knowledge support, job briefs and candidate reports, and RFP responses.

Palmyra models support a comprehensive suite of enterprise-grade capabilities, including:

**Adaptive thinking** – Hybrid models combining advanced reasoning with enterprise-grade reliability, excelling at complex problem-solving and sophisticated decision-making processes.

**Multistep tool-calling** – Support for advanced tool-calling capabilities that can be used in complex multistep workflows and agentic actions, including interaction with enterprise systems to perform tasks like updating systems, executing transactions, sending emails, and triggering workflows.

**Enterprise-grade reliability** – Consistent, accurate results while maintaining strict quality standards required for enterprise use, with models specifically trained on business content to align outputs with professional standards.

**Using Palmyra X5 and X4 in Amazon Bedrock** As for all new serverless models in Amazon Bedrock, I need to request access first. In the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), I choose **Model access** from the navigation pane to enable access to **Palmyra X5** and **Palmyra X4** models.

[![Console screenshot](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/22/bedrock-writer-model-access.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/22/bedrock-writer-model-access.png)

When I have access to the models, I can start building applications with any [AWS SDKs](https://aws.amazon.com/tools/) using the [Amazon Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el). The models use [cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) with these inference profiles:

* For Palmyra X5: `us.writer.palmyra-x5-v1:0`
* For Palmyra X4: `us.writer.palmyra-x4-v1:0`

Here’s a sample implementation with the [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el). In this scenario, there is a new version of an existing product. I need to prepare a detailed comparison of what’s new. I have the old and new product manuals. I use the large input context of Palmyra X5 to read and compare the two versions of the manual and prepare a first draft of the comparison document.

```
import sys
import os
import boto3
import re

AWS_REGION = "us-west-2"
MODEL_ID = "us.writer.palmyra-x5-v1:0"
DEFAULT_OUTPUT_FILE = "product_comparison.md"

def create_bedrock_runtime_client(region: str = AWS_REGION):
    """Create and return a Bedrock client."""
    return boto3.client('bedrock-runtime', region_name=region)

def get_file_extension(filename: str) -> str:
    """Get the file extension."""
    return os.path.splitext(filename)[1].lower()[1:] or 'txt'

def sanitize_document_name(filename: str) -> str:
    """Sanitize document name."""
    # Remove extension and get base name
    name = os.path.splitext(filename)[0]

    # Replace invalid characters with space
    name = re.sub(r'[^a-zA-Z0-9\s\-\(\)\[\]]', ' ', name)

    # Replace multiple spaces with single space
    name = re.sub(r'\s+', ' ', name)

    # Strip leading/trailing spaces
    return name.strip()

def read_file(file_path: str) -> bytes:
    """Read a file in binary mode."""
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except Exception as e:
        raise Exception(f"Error reading file {file_path}: {str(e)}")

def generate_comparison(client, document1: bytes, document2: bytes, filename1: str, filename2: str) -> str:
    """Generate a markdown comparison of two product manuals."""
    print(f"Generating comparison for {filename1} and {filename2}")
    try:
        response = client.converse(
            modelId=MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": "Please compare these two product manuals and create a detailed comparison in markdown format. Focus on comparing key features, specifications, and highlight the main differences between the products."
                        },
                        {
                            "document": {
                                "format": get_file_extension(filename1),
                                "name": sanitize_document_name(filename1),
                                "source": {
                                    "bytes": document1
                                }
                            }
                        },
                        {
                            "document": {
                                "format": get_file_extension(filename2),
                                "name": sanitize_document_name(filename2),
                                "source": {
                                    "bytes": document2
                                }
                            }
                        }
                    ]
                }
            ]
        )
        return response['output']['message']['content'][0]['text']
    except Exception as e:
        raise Exception(f"Error generating comparison: {str(e)}")

def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        cmd = sys.argv[0]
        print(f"Usage: {cmd} <manual1_path> <manual2_path> [output_file]")
        sys.exit(1)

    manual1_path = sys.argv[1]
    manual2_path = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) == 4 else DEFAULT_OUTPUT_FILE
    paths = [manual1_path, manual2_path]

    # Check each file's existence
    for path in paths:
        if not os.path.exists(path):
            print(f"Error: File does not exist: {path}")
            sys.exit(1)

    try:
        # Create Bedrock client
        bedrock_runtime = create_bedrock_runtime_client()

        # Read both manuals
        print("Reading documents...")
        manual1_content = read_file(manual1_path)
        manual2_content = read_file(manual2_path)

        # Generate comparison directly from the documents
        print("Generating comparison...")
        comparison = generate_comparison(
            bedrock_runtime,
            manual1_content,
            manual2_content,
            os.path.basename(manual1_path),
            os.path.basename(manual2_path)
        )

        # Save comparison to file
        with open(output_file, 'w') as f:
            f.write(comparison)

        print(f"Comparison generated successfully! Saved to {output_file}")

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

To learn how to use Amazon Bedrock with AWS SDKs, browse the [code samples in the Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples.html).

**Things to know**

[Writer Palmyra X5 and X4 models](https://aws.amazon.com/bedrock/writer/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) are available in [Amazon Bedrock](https://aws.amazon.com/bedrock/) today in the US West (Oregon) [AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) with [cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el). For the most up-to-date information on model support by Region, refer to the [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el). For information on pricing, visit [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el).

These models support English, Spanish, French, German, Chinese, and multiple other languages, making them suitable for global enterprise applications.

Using the expansive context capabilities of these models, developers can build more sophisticated applications and agents that can process extensive documents, perform complex multistep reasoning, and handle sophisticated agentic workflows.

To start using Writer Palmyra X5 and X4 models today, visit the Writer model section in the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el). You can also explore how our Builder communities are using Amazon Bedrock in their solutions in the generative AI section of our [community.aws](https://community.aws/generative-ai?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) site.

Let us know what you build with these powerful new capabilities!

— [Danilo](https://x.com/danilop)

---

How is the News Blog doing? Take this [1 minute survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi)!

*(This [survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi) is hosted by an external company. AWS handles your information as described in the [AWS Privacy Notice](https://aws.amazon.com/privacy/?trk=4b29643c-e00f-4ab6-ab9c-b1fb47aa1708&sc_channel=blog). AWS will own the data gathered via this survey and will not share the information collected with survey respondents.)*

*Update 4/29/25: Sentence removed regarding enterprise security use cases.*

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