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

# AWS Weekly Roundup: OpenAI partnership, Jane Goodall Institute research archive, and more (November 10, 2025)

by Esra Kayabali on 10 NOV 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon EC2](https://aws.amazon.com/blogs/aws/category/compute/amazon-ec2/ "View all posts in Amazon EC2"), [Amazon S3 Tables](https://aws.amazon.com/blogs/aws/category/storage/amazon-s3-tables/ "View all posts in Amazon S3 Tables"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Regions](https://aws.amazon.com/blogs/aws/category/regions/ "View all posts in Regions") [Permalink](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-s3-amazon-ec2-and-more-november-10-2025/)  [Comments](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-s3-amazon-ec2-and-more-november-10-2025/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/08/wir-oai-aws-hero-300x169.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/08/wir-oai-aws-hero.png)[AWS re:Invent 2025](https://reinvent.awsevents.com/) is only 3 weeks away and I’m already looking forward to the new launches and announcements at the conference. Last year brought 60,000 attendees from across the globe to Las Vegas, Nevada, and the atmosphere was amazing. [Registration](https://registration.awsevents.com/flow/awsevents/reinvent2025/reg/createaccount?trk=aws-blogs-prod.amazon.com) is still open for AWS re:Invent 2025. We hope you’ll join us in Las Vegas December 1–5 for keynotes, breakout sessions, chalk talks, interactive learning opportunities, and networking with cloud practitioners from around the world.

AWS and OpenAI [announced](http://aboutamazon.com/news/aws/aws-open-ai-workloads-compute-infrastructure?utm_source=ecsocial&utm_medium=linkedin&utm_term=36) a multi-year strategic partnership that provides OpenAI with immediate access to AWS infrastructure for running advanced AI workloads. The $38 billion agreement spans 7 years and includes access to AWS compute resources comprising hundreds of thousands of NVIDIA GPUs, with the ability to scale to tens of millions of CPUs for agentic workloads. The infrastructure deployment that AWS is building for OpenAI features a sophisticated architectural design optimized for maximum AI processing efficiency and performance. Clustering the NVIDIA GPUs—both GB200s and GB300s—using Amazon EC2 UltraServers on the same network enables low-latency performance across interconnected systems, allowing OpenAI to efficiently run workloads with optimal performance. The clusters are designed to support various workloads, from serving inference for ChatGPT to training next generation models, with the flexibility to adapt to OpenAI’s evolving needs.

AWS [committed $1 million through its Generative AI Innovation Fund](https://www.aboutamazon.com/news/aws/jane-goodall-institute-research-archive-aws-ai) to digitize the Jane Goodall Institute’s 65 years of primate research archives. The project will transform handwritten field notes, film footage, and observational data on chimpanzees and baboons from analog to digital formats using [Amazon Bedrock](https://aws.amazon.com/bedrock/) and [Amazon SageMaker](https://aws.amazon.com/sagemaker/). The digital transformation will employ multimodal [large language models (LLMs)](https://aws.amazon.com/what-is/large-language-model/) and embedding models to make the research archives searchable and accessible to scientists worldwide for the first time. AWS is collaborating with Ode to build the user experience, helping the Jane Goodall Institute adopt AI technologies to advance research and conservation efforts. I was deeply saddened when I heard that world-renowned primatologist Jane Goodall had passed away. Learning that this project will preserve her life’s work and make it accessible to researchers around the world brought me comfort. It’s a fitting tribute to her remarkable legacy.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/08/wir-download.jpeg)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/08/wir-download.jpeg)

Transforming decades of research through cloud and AI. Dr. Jane Goodall and field staff observe Goblin at Gombe National Park, Tanzania. CREDIT: the Jane Goodall Institute

**Last week’s launches**

Let’s look at last week’s new announcements:

* [Amazon S3 now supports tags on S3 Tables](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-s3-tags-s3-tables/) – Amazon S3 now supports tags on S3 Tables for attribute-based access control (ABAC) and cost allocation. You can use tags for ABAC to automatically manage permissions for users and roles accessing table buckets and tables, eliminating frequent AWS Identity and Access Management (IAM) or S3 Tables resource-based policy updates and simplifying access governance at scale. Additionally, tags can be added to individual tables to track and organize AWS costs using AWS Billing and Cost Management.

* [Amazon EC2 R8a Memory-Optimized Instances now generally available](https://aws.amazon.com/about-aws/whats-new/2025/11/memory-optimized-amazon-ec2-r8a-instances/) – R8a instances feature 5th Gen AMD EPYC processors (formerly code named Turin) with a maximum frequency of 4.5 GHz, and they deliver up to 30% higher performance and up to 19% better price-performance compared to R7a instances, with 45% more memory bandwidth. Built on the AWS Nitro System using sixth-generation Nitro Cards, these instances are designed for high-performance, memory-intensive workloads, including SQL and NoSQL databases, distributed web scale in-memory caches, in-memory databases, real-time big data analytics, and electronic design automation (EDA) applications. R8a instances are SAP certified and offer 12 sizes, including two bare metal sizes.

* [EC2 Auto Scaling announces warm pool support for mixed instances policies](https://aws.amazon.com/about-aws/whats-new/2025/11/ec2-auto-scaling-warm-pool-mixed-instances-policies/) – EC2 Auto Scaling groups now support warm pools for Auto Scaling groups configured with mixed instances policies. Warm pools create a pool of pre-initialized EC2 instances ready to quickly serve application traffic, improving application elasticity. The feature benefits applications with lengthy initialization processes, such as writing large amounts of data to disk or running complex custom scripts. By combining warm pools with instance type flexibility, Auto Scaling groups can rapidly scale out to maximum size while deploying applications across multiple instance types to enhance availability. The feature works with Auto Scaling groups configured for multiple On-Demand Instance types through manual instance type lists or attribute-based instance type selection.

* [Amazon Bedrock AgentCore Runtime now supports direct code deployment](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-bedrock-agentcore-runtime-code-deployment/) – Amazon Bedrock AgentCore Runtime now offers two deployment methods for AI agents: container-based deployment and direct code upload. You can choose between direct code–zip file upload for rapid prototyping and iteration or container-based options for complex use cases requiring custom configurations. AgentCore Runtime provides a serverless framework and model agnostic runtime for running agents and tools at scale. The direct code–zip upload feature includes drag-and-drop functionality, enabling faster iteration cycles for prototyping while maintaining enterprise security and scaling capabilities for production deployments.

* [AWS Capabilities by Region now available for Regional planning](https://aws.amazon.com/blogs/aws/introducing-aws-capabilities-by-region-for-easier-regional-planning-and-faster-global-deployments/) – AWS Capabilities by Region helps discover and compare AWS services, features, APIs, and AWS CloudFormation resources across Regions. This planning tool provides an interactive interface to explore service availability, compare multiple Regions side by side, and view forward-looking roadmap information. You can search for specific services or features, view API operations availability, verify CloudFormation resource type support, and check EC2 instance type availability including specialized instances. The tool displays availability states including Available, Planning, Not Expanding, and directional launch planning by quarter. The AWS Capabilities by Region data is also accessible through the AWS Knowledge MCP server, enabling automation of Region expansion planning and integration into development workflows and continuous integration and continuous delivery (CI/CD) pipelines.

**Upcoming AWS events**

Check your calendar and sign up for upcoming AWS events:

* [AWS re:Invent 2025](https://reinvent.awsevents.com/) – Join us in Las Vegas December 1–5 as cloud pioneers gather from across the globe for the latest AWS innovations, peer-to-peer learning, expert-led discussions, and invaluable networking opportunities. Don’t forget to explore the [event catalog](https://registration.awsevents.com/flow/awsevents/reinvent2025/eventcatalog/page/eventcatalog?trk=aws-blogs-prod.amazon.com).
* [AWS Builder Loft](https://builder.aws.com/connect/events/builder-loft) – A tech hub in San Francisco where builders share ideas, learn, and collaborate. The space offers industry expert sessions, hands-on workshops, and community events covering topics from AI to emerging technologies. Browse the [upcoming sessions](https://luma.com/aws-builder-loft-events) and join the events that interest you.
* [AWS Skills Center Seattle 4th Anniversary Celebration](https://pulse.aws/survey/LOLZYMRD?p=0) – A free, public event on November 20 with a keynote, learning panels, recruiter insights, raffles, and virtual participation options.

Join the [AWS Builder Center](https://builder.aws.com/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) to connect with builders, share solutions, and access content that supports your development. Browse here for upcoming [AWS led in-person and virtual events](https://aws.amazon.com/events/explore-aws-events/?refid=e61dee65-4ce8-4738-84db-75305c9cd4fe), [developer-focused events](https://builder.aws.com/connect/events?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), and [events for startups](https://aws.amazon.com/startups/events?tab=upcoming&region=EMEA).

That’s all for this week. Check back next Monday for another Weekly Roundup!

[— Esra](https://www.linkedin.com/in/esrakayabali/)

*This post is part of our Weekly Roundup series. Check back each week for a quick roundup of interesting news and announcements from AWS!*

TAGS: [Week in Review](https://aws.amazon.com/blogs/aws/tag/week-in-review/)

![Esra Kayabali](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/03/24/esrakayabali11-400x400-1.jpg)

### Esra Kayabali

Esra Kayabali is a Senior Solutions Architect at AWS, specialising in analytics, including data warehousing, data lakes, big data analytics, batch and real-time data streaming, and data integration. She has more than ten years of software development and solution architecture experience. She is passionate about collaborative learning, knowledge sharing, and guiding community in their cloud technologies journey.

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