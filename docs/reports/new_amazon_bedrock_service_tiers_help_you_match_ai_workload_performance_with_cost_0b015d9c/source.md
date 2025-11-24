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

# New Amazon Bedrock service tiers help you match AI workload performance with cost

by [Sébastien Stormacq](https://aws.amazon.com/blogs/aws/author/stormacq/ "Posts by Sébastien Stormacq") on 18 NOV 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/new-amazon-bedrock-service-tiers-help-you-match-ai-workload-performance-with-cost/)  [Comments](https://aws.amazon.com/blogs/aws/new-amazon-bedrock-service-tiers-help-you-match-ai-workload-performance-with-cost/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, [Amazon Bedrock](https://aws.amazon.com/bedrock/) introduces new service tiers that give you more control over your AI workload costs while maintaining the performance levels your applications need.

I’m working with customers building AI applications. I’ve seen firsthand how different workloads require different performance and cost trade-offs. Many organizations running AI workloads face challenges balancing performance requirements with cost optimization. Some applications need rapid response times for real-time interactions, whereas others can process data more gradually. With these challenges in mind, today we’re announcing additional options pricing that give you more flexibility in matching your workload requirements with cost optimization.

Amazon Bedrock now offers three service tiers for workloads: Priority, Standard, and Flex. Each tier is designed to match specific workload requirements. Applications have varying response time requirements based on the use case. Some applications—such as financial trading systems—demand the fastest response times, others need rapid response times to support business processes like content generation, and applications such as content summarization can process data more gradually.

The **Priority** tier processes your requests ahead of other tiers, providing preferential compute allocation for mission-critical applications like customer-facing chat-based assistants and real-time language translation services, though at a premium price point. The **Standard** tier provides consistent performance at regular rates for everyday AI tasks, ideal for content generation, text analysis, and routine document processing. For workloads that can handle longer latency, the **Flex** tier offers a more cost-effective option with lower pricing, which is well suited for model evaluations, content summarization, and multistep analysis and agentic workflows.

You can now optimize your spending by matching each workload to the most appropriate tier. For example, if you’re running a customer service chat-based assistant that needs quick responses, you can use the Priority tier to get the fastest processing times. For content summarization tasks that can tolerate longer processing times, you can use the Flex tier to reduce costs while maintaining reliable performance. For most models that support Priority Tier, customers can realize up to 25% better output tokens per second (OTPS) latency compared to standard tier.

Check the [Amazon Bedrock documentation for an up-to-date list of models supported for each service tier.](https://docs.aws.amazon.com/bedrock/latest/userguide/service-tiers-inference.html)

**Choosing the right tier for your workload**

Here is a mental model to help you choose the right tier for your workload.

| Category | Recommended service tier | Description |
| --- | --- | --- |
| Mission-critical | Priority | Requests are handled ahead of other tiers. Lower latency responses for user-facing apps (for example, customer service chat assistants, real-time language translation, interactive AI assistants) |
| Business-standard | Standard | Responsive performance for important workloads (for example, content generation, text analysis, routine document processing) |
| Business-noncritical | Flex | Cost-efficient for less urgent workloads (for example, model evaluations, content summarization, multistep agentic workflows) |

Start by reviewing with application owners your current usage patterns. Next, identify which workloads need immediate responses and which ones can process data more gradually. You can then begin routing a small portion of your traffic through different tiers to test performance and cost benefits.

The [AWS Pricing Calculator](https://calculator.aws/#/createCalculator/bedrock) helps you estimate costs for different service tiers by entering your expected workload for each tier. You can estimate your budget based on your specific usage patterns.

To monitor your usage and costs, you can use the [AWS Service Quotas console](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/bedrock/quotas) or [turn on model invocation logging in Amazon Bedrock](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/model-invocations.html) and observe the metrics with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/). These tools provide visibility into your token usage and help you track performance across different tiers.

[![Amazon Bedrock invocations observability](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/17/2025-10-17_13-49-02-1024x651.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/17/2025-10-17_13-49-02.png)

You can start using the new service tiers today. You choose the tier on a per-API call basis. Here is an example using the `ChatCompletions` OpenAI API, but you can pass the same `service_tier` parameter in the body of `InvokeModel`, `InvokeModelWithResponseStream`, `Converse`, and`ConverseStream` APIs (for supported models):

```
from openai import OpenAI

client = OpenAI(
    base_url="https://bedrock-runtime.us-west-2.amazonaws.com/openai/v1",
    api_key="$AWS_BEARER_TOKEN_BEDROCK" # Replace with actual API key
)

completion = client.chat.completions.create(
    model= "openai.gpt-oss-20b-1:0",
    messages=[
        {
            "role": "developer",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
    service_tier= "priority"  # options: "priority | default | flex"
)

print(completion.choices[0].message)
```

To learn more, check out the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) or contact your AWS account team for detailed planning assistance.

I’m looking forward to hearing how you use these new pricing options to optimize your AI workloads. Share your experience with me online on social networks or connect with me at AWS events.

[— seb](https://linktr.ee/sebsto)

![Sébastien Stormacq](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2023/01/13/AWS-59-cropped.jpg)

### [Sébastien Stormacq](https://aws.amazon.com/blogs/aws/author/stormacq/ "Posts by Sébastien Stormacq")

Seb has been writing code since he first touched a Commodore 64 in the mid-eighties. He inspires builders to unlock the value of the AWS cloud, using his secret blend of passion, enthusiasm, customer advocacy, curiosity and creativity. His interests are software architecture, developer tools and mobile computing. If you want to sell him something, be sure it has an API. Follow @sebsto on Bluesky, X, Mastodon, and others.

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