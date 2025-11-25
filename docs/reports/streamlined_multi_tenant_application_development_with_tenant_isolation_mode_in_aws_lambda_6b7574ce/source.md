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

# Streamlined multi-tenant application development with tenant isolation mode in AWS Lambda

by [Donnie Prakoso](https://aws.amazon.com/blogs/aws/author/donnie/ "Posts by Donnie Prakoso") on 19 NOV 2025 in [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS Lambda](https://aws.amazon.com/blogs/aws/category/compute/aws-lambda/ "View all posts in AWS Lambda"), [Compute](https://aws.amazon.com/blogs/aws/category/compute/ "View all posts in Compute"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/streamlined-multi-tenant-application-development-with-tenant-isolation-mode-in-aws-lambda/)  [Comments](https://aws.amazon.com/blogs/aws/streamlined-multi-tenant-application-development-with-tenant-isolation-mode-in-aws-lambda/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Multi-tenant applications often require strict isolation when processing tenant-specific code or data. Examples include software-as-a-service (SaaS) platforms for workflow automation or code execution where customers need to ensure that execution environments used for individual tenants or end users remain completely separate from one another. Traditionally, developers have addressed these requirements by deploying separate Lambda functions for each tenant or implementing custom isolation logic within shared functions which increased architectural and operational complexity.

Today, [AWS Lambda](https://aws.amazon.com/lambda/) introduces a new tenant isolation mode that extends the existing isolation capabilities in Lambda. Lambda already provides isolation at the function level, and this new mode extends isolation to the individual tenant or end-user level within a single function. This built-in capability processes function invocations in separate execution environments for each tenant, enabling you to meet strict isolation requirements without additional implementation effort to manage tenant-specific resources within function code.

Here’s how you can enable tenant isolation mode in the [AWS Lambda console](https://console.aws.amazon.com/lambda):

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/18/news-2025-11-lambda-tenant-isolation-rev-3.png)

When using the new tenant isolation capability, Lambda associates function execution environments with customer-specified tenant identifiers. This means that execution environments for a particular tenant aren’t used to serve invocation requests from other tenants invoking the same Lambda function.

The feature addresses strict security requirements for SaaS providers processing sensitive data or running untrusted tenant code. You maintain the pay-per-use and performance characteristics of AWS Lambda while gaining execution environment isolation. Additionally, this approach delivers the security benefits of per-tenant infrastructure without the operational overhead of managing dedicated Lambda functions for individual tenants, which can quickly grow as customers adopt your application.

**Getting started with AWS Lambda tenant isolation**Let me walk you through how to configure and use tenant isolation for a multi-tenant application.

First, on the **Create function** page in the AWS Lambda console, I choose **Author from scratch** option.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/10/news-2025-11-lambda-tenant-isolation-1.png)

Then, under **Additional configurations**, I select **Enable** under **Tenant isolation mode**. Note that, tenant isolation mode can only be set during function creation and can’t be modified for existing Lambda functions.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/18/news-2025-11-lambda-tenant-isolation-rev-4.png)

Next, I write Python code to demonstrate this capability. I can access the tenant identifier in my function code through the context object. Here’s the full Python code:

```
import json
import os
from datetime import datetime

def lambda_handler(event, context):
    tenant_id = context.tenant_id
    file_path = '/tmp/tenant_data.json'

    # Read existing data or initialize
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
    else:
        data = {
            'tenant_id': tenant_id,
            'request_count': 0,
            'first_request': datetime.utcnow().isoformat(),
            'requests': []
        }

    # Increment counter and add request info
    data['request_count'] += 1
    data['requests'].append({
        'request_number': data['request_count'],
        'timestamp': datetime.utcnow().isoformat()
    })

    # Write updated data back to file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

    # Return file contents to show isolation
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'File contents for {tenant_id} (isolated per tenant)',
            'file_data': data
        })
    }
```

When I’m finished, I choose **Deploy**. Now, I need to test this capability by choosing **Test**. I can see on the **Create new test event** panel that there’s a new setting called **Tenant ID**.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/10/news-2025-11-lambda-tenant-isolation-3.png)

If I try to invoke this function without a tenant ID, I’ll get the following error “Add a valid tenant ID in your request and try again.”

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/12/news-2025-11-lambda-tenant-isolation-rev-1.png)

Let me try to test this function with a tenant ID called `tenant-A`.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/12/news-2025-11-lambda-tenant-isolation-rev-2.png)

I can see the function ran successfully and returned `request_count: 1`. I’ll invoke this function again to get `request_count: 2`.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/10/news-2025-11-lambda-tenant-isolation-6.png)

Now, let me try to test this function with a tenant ID called `tenant-B`.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/10/news-2025-11-lambda-tenant-isolation-7.png)

The last invocation returned `request_count: 1` because I never invoked this function with `tenant-B`. Each tenant’s invocations will use separate execution environments, isolating the cached data, global variables, and any files stored in `/tmp`.

This capability transforms how I approach multi-tenant serverless architecture. Instead of wrestling with complex isolation patterns or managing hundreds of tenant-specific Lambda functions, I let AWS Lambda automatically handle the isolation. This keeps tenant data isolated across tenants, giving me confidence in the security and separation of my multi-tenant application.

**Additional things to know**Here’s a list of additional things you need to know:

* **Performance —** Same-tenant invocations can still benefit from warm execution environment reuse for optimal performance.
* **Pricing —** You’re charged when Lambda creates a new tenant-aware execution environment, with the price depending on the amount of memory you allocate to your function and the CPU architecture you use. For more details, view [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/).
* **Availability —** Available now in all commercial [AWS Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region) except Asia Pacific (New Zealand), AWS GovCloud (US), and China Regions.

This launch simplifies building multi-tenant applications on AWS Lambda, such as SaaS platforms for workflow automation or code execution. Learn more about how to configure tenant isolation for your next multi-tenant Lambda function in the [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/).

Happy building!

— [Donnie](https://www.linkedin.com/in/donnieprakoso)

![Donnie Prakoso](https://d2908q01vomqb2.cloudfront.net/667be543b02294b7624119adc3a725473df39885/2023/05/30/donnie_profile_400x400.jpeg)

### [Donnie Prakoso](https://aws.amazon.com/blogs/aws/author/donnie/ "Posts by Donnie Prakoso")

Donnie Prakoso is a software engineer, self-proclaimed barista, and Principal Developer Advocate at AWS. With more than 17 years of experience in the technology industry, from telecommunications, banking to startups. He is now focusing on helping the developers to understand varieties of technology to transform their ideas into execution. He loves coffee and any discussion of any topics from microservices to AI / ML.

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