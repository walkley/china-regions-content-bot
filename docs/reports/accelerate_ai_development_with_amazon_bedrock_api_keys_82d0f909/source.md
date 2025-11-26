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

## [Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/)

# Accelerate AI development with Amazon Bedrock API keys

by Sofian Hamiti, Ajit Mahareddy, Massimiliano Angelino, Huong Nguyen, and Nakul Vankadari Ramesh on 08 JUL 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Machine Learning](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Announcements](https://aws.amazon.com/blogs/machine-learning/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Foundation models](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/generative-ai/foundation-models/ "View all posts in Foundation models") [Permalink](https://aws.amazon.com/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/)  [Comments](https://aws.amazon.com/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/#Comments)  Share

Today, we’re excited to announce a significant improvement to the developer experience of [Amazon Bedrock](https://aws.amazon.com/bedrock/): API keys. API keys provide a new way to access the Amazon Bedrock APIs, streamlining the authentication process so that developers can focus on building rather than configuration.

CamelAI is an open-source, modular framework for building intelligent multi-agent systems for data generation, world simulation, and task automation.

> *“As a startup with limited resources, streamlined customer onboarding is critical to our success. The Amazon Bedrock API keys enable us to onboard enterprise customers in minutes rather than hours. With Bedrock, our customers can quickly provision access to leading AI models and seamlessly integrate them into CamelAI,”*
>
> said Miguel Salinas, CTO, CamelAI.

In this post, explore how API keys work and how you can start using them today.

## API key authentication

Amazon Bedrock now provides API key access to streamline integration with tools and frameworks that expect API key-based authentication. The Amazon Bedrock and Amazon Bedrock runtime SDKs support API key authentication for methods including on-demand inference, provisioned throughput inference, model fine-tuning, distillation, and evaluation.

The diagram compares the default authentication process to Amazon Bedrock (in orange) with the API keys approach (in blue). In the default process, you must create an identity in [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) or [AWS IAM](https://aws.amazon.com/iam/), attach IAM policies to provide permissions to perform API operations, and generate credentials, which you can then use to make API calls. The grey boxes in the diagram highlight the steps that Amazon Bedrock now streamlines when generating an API key. Developers can now authenticate and access Amazon Bedrock APIs with minimal setup overhead.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/08/12/REVBLOG-949-img1.png)

You can generate API keys in the Amazon Bedrock console, choosing between two types.

**Short-term API keys** use the IAM permissions from your current IAM principal and expire when your account’s session ends or can last up to 12 hours, whichever ends first. Short-term API keys use [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) for authentication. For continuous application use, you can implement API key refreshing following [those examples](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-generate.html) and using your [credential provider of choice](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html#credentialProviderChain).

When you create a **long-term API key**, Amazon Bedrock automatically creates an IAM user and associates the key with it. You can set expiration times ranging from 1 day to no expiration. Amazon Bedrock attaches the [AmazonBedrockLimitedAccess](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonBedrockLimitedAccess) managed policy to the IAM user, and you can modify permissions as needed through the IAM service. These keys are specific to Amazon Bedrock and cannot be used with other AWS services. We recommend using [temporary AWS IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-workloads-use-roles) or short-term API keys for setups that require a higher level of security, and long-term keys with expiration dates for exploring Amazon Bedrock.

## Making Your First API Call

Once you [have access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) to foundation models, getting started with Amazon Bedrock API key is straightforward. Here’s how to make your first API call using the [AWS SDK for Python](https://aws.amazon.com/sdk-for-python/) (Boto3 SDK) and API keys:

### Generate an API key

To generate an API key, follow these steps:

1. Sign in to the AWS Management Console and open the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/)
2. In the left navigation panel, select **API keys**
3. Choose either **Generate short-term API key** or **Generate long-term API key**
4. For long-term keys, set your desired expiration time and optionally configure advanced permissions
5. Choose **Generate** and copy your API key

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/30/ML-19021-image-2.gif)

### Set Your API Key as Environment Variable

You can set your API key as an environment variable so that it’s automatically recognized when you make API requests:

```
# To set the API key as an environment variable, you can open a terminal and run the following command:
export AWS_BEARER_TOKEN_BEDROCK=<YOUR API KEY HERE>
```

The Boto3 and AWS JavaScript SDKs automatically detect your environment variable when you create an Amazon Bedrock client. Make sure you use the latest SDK version.

### Make Your First API Call

You can now make API calls to Amazon Bedrock in multiple ways:

1. Using curl

   ```
   curl -X POST "https://bedrock-runtime.us-east-1.amazonaws.com/model/us.anthropic.claude-3-5-haiku-20241022-v1:0/converse" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $AWS_BEARER_TOKEN_BEDROCK" \
     -d '{
       "messages": [
           {
               "role": "user",
               "content": [{"text": "Hello"}]
           }
       ]
     }'
   ```
2. Using the Boto3 SDK for Amazon Bedrock:

   ```
   import boto3

   # Create an Amazon Bedrock client
   client = boto3.client(
       service_name="bedrock-runtime",
       region_name="us-east-1"     # If you've configured a default region, you can omit this line
   )

   # Define the model and message
   model_id = "us.anthropic.claude-3-5-haiku-20241022-v1:0"
   messages = [{"role": "user", "content": [{"text": "Hello"}]}]

   response = client.converse(
       modelId=model_id,
       messages=messages,
   )

   # Print the response
   print(response['output']['message']['content'][0]['text'])
   ```
3. You can also use native libraries like Python Requests:

   ```
   import requests
   import os

   url = "https://bedrock-runtime.us-east-1.amazonaws.com/model/us.anthropic.claude-3-5-haiku-20241022-v1:0/converse"

   payload = {
       "messages": [
           {
               "role": "user",
               "content": [{"text": "Hello"}]
           }
       ]
   }

   headers = {
       "Content-Type": "application/json",
       "Authorization": f"Bearer {os.environ['AWS_BEARER_TOKEN_BEDROCK']}"
   }

   response = requests.request("POST", url, json=payload, headers=headers)

   print(response.text)
   ```

## Bridging developer experience and enterprise security requirements

As an administrator, you can enable short-term API keys to streamline user onboarding for Amazon Bedrock foundation models while ensuring a higher level of security. These keys leverage AWS Signature Version 4 and existing IAM principals, maintaining your established access controls.

For audit and compliance purposes, all API calls are logged in [AWS CloudTrail](https://aws.amazon.com/cloudtrail/). API keys are passed as authorization headers to API requests and are not logged.

**Controlling permissions for API keys**

You can use Service Control Policies (SCPs) with [Amazon Bedrock condition keys](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-permissions.html) to customize API key generation and usage to meet your organization’s requirements.

For example, you can deny API key usage with the following policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "bedrock:CallWithBearerToken",
      "Resource": "*"
    }
  ]
}
```

You can also enforce expiration limits on long-term API keys to ensure regular rotation. The following SCP prevents creation of keys with lifespans exceeding 30 days:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "iam:CreateServiceSpecificCredential",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:ServiceSpecificCredentialServiceName": "bedrock.amazonaws.com"
                },
                "NumericGreaterThanEquals": {
                    "iam:ServiceSpecificCredentialAgeDays": "30"
                }
            }
        }
    ]
}
```

Refer to the [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-permissions.html) for additional SCP examples.

## Conclusion

Amazon Bedrock API keys can be used in the commercial AWS regions Amazon Bedrock is available. To learn more about API keys in Amazon Bedrock, visit the API Keys documentation in the [Amazon Bedrock user guide](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html).

Give API keys a try in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) today and send feedback to [AWS re:Post for Amazon Bedrock](https://repost.aws/tags/TAQeKlaPaNRQ2tWB6P7KrMag/amazon-bedrock) or through your usual AWS Support contacts.

---

### About the Authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/30/Sofian2.png)Sofian Hamiti** is a technology leader with over 10 years of experience building AI solutions, and leading high-performing teams to maximize customer outcomes. He is passionate in empowering diverse talent to drive global impact and achieve their career aspirations.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/30/ajit.png)Ajit Mahareddy** is an experienced Product and Go-To-Market (GTM) leader with over 20 years of experience in product management, engineering, and go-to-market. Prior to his current role, Ajit led product management building AI/ML products at leading technology companies, including Uber, Turing, and eHealth. He is passionate about advancing generative AI technologies and driving real-world impact with generative AI.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/30/nakud.png)Nakul Vankadari Ramesh** is a Software Development Engineer with over 7 years of experience building large-scale distributed systems. He currently works on the Amazon Bedrock team, helping accelerate the development of generative AI capabilities. Previously, he contributed to Amazon Managed Blockchain, focusing on scalable and reliable infrastructure.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2020/11/03/Huong-Nguyen.jpg)Huong Nguyen** is a Principal Product Manager at AWS. She is a product leader at Amazon Bedrock, with 18 years of experience building customer-centric and data-driven products. She is passionate about democratizing responsible machine learning and generative AI to enable customer experience and business innovation. Outside of work, she enjoys spending time with family and friends, listening to audiobooks, traveling, and gardening.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/30/Massimiliano.png)Massimiliano Angelino** is Lead Architect for the EMEA Prototyping team. During the last 3 and half years he has been an IoT Specialist Solution Architect with a particular focus on edge computing, and he contributed to the launch of AWS IoT Greengrass v2 service and its integration with Amazon SageMaker Edge Manager. Based in Stockholm, he enjoys skating on frozen lakes.

Loading comments…

### Resources

* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=machine-learning-resources)
* [What's New](https://aws.amazon.com/new?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=machine-learning-resources)

---

### Blog Topics

* [Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/)
* [Amazon Comprehend](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-comprehend/)
* [Amazon Kendra](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-kendra/)
* [Amazon Lex](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-lex/)
* [Amazon Polly](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-polly/)
* [Amazon Q](https://aws.amazon.com/blogs/machine-learning/category/amazon-q/)
* [Amazon Rekognition](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-rekognition/)
* [Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/sagemaker/)
* [Amazon Textract](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-textract/)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=maching-learning-social)

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