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

## [AWS Cloud Enterprise Strategy Blog](https://aws.amazon.com/blogs/enterprise-strategy/)

# Quantifying the Impact of Developer Experience: Amazon’s 15.9% Breakthrough

by Jim Haughwout on 10 JUL 2025 in [Best Practices](https://aws.amazon.com/blogs/enterprise-strategy/category/post-types/best-practices/ "View all posts in Best Practices"), [DevOps](https://aws.amazon.com/blogs/enterprise-strategy/category/devops/ "View all posts in DevOps"), [Technical How-to](https://aws.amazon.com/blogs/enterprise-strategy/category/post-types/technical-how-to/ "View all posts in Technical How-to"), [Thought Leadership](https://aws.amazon.com/blogs/enterprise-strategy/category/post-types/thought-leadership/ "View all posts in Thought Leadership") [Permalink](https://aws.amazon.com/blogs/enterprise-strategy/business-value-of-developer-experience-improvements-amazons-15-9-breakthrough/)  [Comments](https://aws.amazon.com/blogs/enterprise-strategy/business-value-of-developer-experience-improvements-amazons-15-9-breakthrough/#Comments)  Share

![Financial Outcomes](https://d2908q01vomqb2.cloudfront.net/cb7a1d775e800fd1ee4049f7dca9e041eb9ba083/2025/07/04/Financial-Outcomes-scaled.jpeg)

For 25 years, I have worked to improve developer experiences. Every leader I work with recognizes that doing so is valuable, yet one question remains: How do these improvements translate into concrete, measurable business value?

AWS customers often ask me how Amazon thinks about this question. In December 2023, when I was presenting my team’s year-end results and upcoming plans to Amazon’s senior leadership team, I was asked directly. Luckily we had been thinking about the problem and already had an approach in mind.

Traditional measures of development productivity fall short. Only measuring velocity, for example, ignores the benefits of reduced risk and improved quality and availability. Adding up the time saved on discrete activities does not translate directly to business value. Measures tied too closely to specific activities are at risk of being gamed.

We needed a metric for the entire software delivery process that matched our desired results: (1) bringing new builders up to speed quickly; (2) delivering valuable software to customers rapidly, safely, regularly, and with low overhead; and (3) managing services with high availability and low operational load. We already had KPIs for each outcome (similar to those used in [DORA](https://dora.dev/) or [SPACE](https://queue.acm.org/detail.cfm?id=3454124)), but we needed to translate their cumulative effect into a business outcome measurement.

Enter Amazon’s cost to serve (CTS) framework. We use it to continually adjust the physical supply chain in our retail business, improving customer experiences. CEO Andy Jassy described its successes in his [annual shareholder letter in 2024](https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-2023-letter-to-shareholders).

Our team adapted this framework to devise a cost to serve software (CTS-SW) metric. It revealed that our improvements in the end-to-end software delivery process reduced costs by 15.9% YoY in 2024. This was not simply a velocity improvement. It was an economic return that we could relate to cost avoidance and [return on invested capital (ROIC)](https://www.investopedia.com/terms/r/returnoninvestmentcapital.asp).

Here’s the framework and why it works. I hope that it helps you not only measure the value they return but also target improvements to your software delivery processes.

## The Cost to Serve Software Framework

In retail, CTS measures the cost of all aspects of delivery (fulfillment centers, deliveries, returns, compute costs, software) divided by the total number of units fulfilled to customers (where each unit is a purchased item). [Reducing CTS drives improvements across many dimensions of the supply chain](https://www.aboutamazon.com/news/operations/doug-herrington-amazon-prime-delivery-speed-2024-updates), including delivery frequency, speed, friction, and quality. Removing delays reduces CTS. Delivering items together reduces CTS. Reducing defects and returns reduces CTS.

Similarly, CTS-SW measures the total cost of delivering a unit of software. AWS has a large variety of software development activities (e.g., some teams have barriers to immediate release, such as periodic mobile app release cycles). So the delivery unit differs by team. It represents their chosen socio-technical unit of work—i.e., what the team deems valuable enough to review, merge, deploy, and support for customers. For microservices the units are deployments; for monoliths and mobile apps, we use pull request completions.

You can use improvements in CTS-SW to calculate cost avoidance in dollars and cents, which informs other financial metrics, like ROIC. We always pair CTS-SW with supporting tension metrics to ensure the improvements do not compromise any pillar of delivery effectiveness, like security or resilience.

![](https://d2908q01vomqb2.cloudfront.net/cb7a1d775e800fd1ee4049f7dca9e041eb9ba083/2025/07/04/CTS-SW.png)

Amazon’s federated model to software development allows us to understand the improvements centralized developer tooling can provide for teams. Measuring CTS-SW encourages teams to target improvements that tie most directly to economic value. CTS-SW provides a concrete measure of software development economics, accounting for both cost avoidance and efficiency gains.

Particularly important to us is giving developers back their most valuable resource—time. Developers come to Amazon to build and deliver software for customers. Maximizing their ability to do so offers concrete returns for the business. Our improvements to reduce CTS gave developers that time and reduced toilsome work.

Amazon invests in tools that allow teams to develop, deploy, and operate safely at tremendous scale. Our scale provided unique insights into how we might reduce CTS-SW. By using data from developer repositories, weekly deployments, tickets, and documentation, we identified patterns where we could remove friction from the developer experience and lower CTS-SW. It was clear that streamlining how teams build and test software gives them more time and improves quality. Improving the code review process has the same effect. When you can onboard new builders more easily, your teams start building faster. Centralizing updates and upgrades reduces toil and boosts quality. Providing tools that make CI/CD safe and easy eliminates manual work, reduces defects and consequent rollbacks, and increases velocity. And by reducing technical debt and removing common sources of defects, teams spend less time chasing down problems.

These improvements give teams more effective capacity. And we demonstrate their economic value through CTS-SW.

## CTS-SW and Amazon Culture

CTS-SW also supports the [principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles) that differentiate Amazon as a company.

We obsess over customer outcomes. CTS-SW directly links investments in the developer experience to those outcomes by assessing how frequently we deliver new or better experiences. Some organizations fall into the anti-pattern of calculating minutes saved to measure value, but that approach isn’t customer-centered and doesn’t prove value creation. We start with the goal of delivering more for customers, and then we determine what process improvements support that goal.

CTS-SW advances our end-to-end ownership culture at Amazon. It shows how both central and distributed teams impact customer outcomes with their improvements. It prevents the siloing that happens when teams only focus on what is under their direct control. At Amazon, every developer owns their software, understands their customers, and works backward from their customers’ needs. By freeing developers’ time, CTS-SW helps them own their value delivery.

CTS-SW also improves our conversations by translating our efforts and results into business outcome language. Each business unit maintains a sophisticated model for quantifying the value that software delivers to customers. CTS-SW complements that model by determining the cost of *delivering* the value.

In 2024, our developer experience improvements helped increase our weekly production deployments per builder by 18.3% YoY. Automation reduced the number of human interventions per deployment by 30.4% YoY. We deployed software updates centrally and automatically to manage risks. As a result, the number of incident-related tickets per deployment has decreased by 32.5% since 2022. Last year we migrated production applications from older Java versions [to Java 17 with AI assistance from Amazon Q Developer](https://aws.amazon.com/blogs/devops/amazon-q-developer-just-reached-a-260-million-dollar-milestone/). We’ve also started [using Amazon Q Business to get developers answers to questions](https://aws.amazon.com/blogs/devops/reducing-time-spent-waiting-with-amazon-q/), summarize log data in tickets, and improve onboarding for new hires—further reducing CTS-SW.

## Applying CTS-SW Across Industries

The principles we used at AWS are applicable across other companies and industries. In today’s tech-centric business environment, development productivity is not just an operational metric; it is a competitive differentiator.

Let’s say you are a CIO or CTO at a bank with 1K developers, each with an annual cost of $130K (including tooling), totaling $130M in developer expenses. By implementing developer experience solutions that drive a 15% CTS-SW improvement, you can achieve $20M in cost avoidance. The solution, costing $2M, would generate a 10x return on investment. So for every dollar you invest, you generate $10 in return. This enables you as CIO or CTO to demonstrate return on investment for improvements to how developers support the larger enterprise’s business.

That’s for an industry where software supports the business. Another scenario is a tech company, where developers create the business’s actual product. Consider a hypergrowth technology company with 400 software developers. If software development costs represent 60% of its revenue, a 15% improvement in CTS-SW will improve gross margin by 9 percentage points. With a 15% profit margin, this 9-point increase results in a 60% boost in profit (assuming software delivery drives revenue and excluding tax implications). In technology companies where developers are the key driver of business success, the impact is most dramatic.

## Pulling it Together

I am sharing this framework because I believe it is vital to continuously improve the developer experience. I hope it helps demonstrate the business value your investments in the builder experience generate.

CTS-SW has allowed us at AWS to showcase how improvements across the full software development lifecycle create efficiencies and remove points of friction. By understanding the return on these investments, we can more readily see the value from developer experience improvements.

Remember the goal of reducing CTS-SW is to free your teams to do what they do best: innovate for your customers. Whether you are looking to optimize your CI/CD pipelines, integrate generative AI into your development workflow, or reduce operational load through managed services, CTS-SW can help you focus your efforts and translate improvements into business results.

For detailed implementation guidance and technical insights, see our [CTS-SW framework](//www.amazon.science/blog/measuring-the-effectiveness-of-software-development-tools-and-practices?trk=978e2360-0301-4378-811c-f852c28be62d&sc_channel=el) research on the Amazon Science blog, or connect with an AWS Solutions Architect. We are committed to helping teams achieve measurable improvements in their software delivery efficiency while maintaining the high standards that AWS customers expect..

TAGS: [Business Value](https://aws.amazon.com/blogs/enterprise-strategy/tag/business-value/), [cloud economics](https://aws.amazon.com/blogs/enterprise-strategy/tag/cloud-economics/), [Cost Optimization](https://aws.amazon.com/blogs/enterprise-strategy/tag/cost-optimization/), [DevOps](https://aws.amazon.com/blogs/enterprise-strategy/tag/devops/), [digital innovation](https://aws.amazon.com/blogs/enterprise-strategy/tag/digital-innovation/), [Global Deployment](https://aws.amazon.com/blogs/enterprise-strategy/tag/global-deployment/), [Innovation](https://aws.amazon.com/blogs/enterprise-strategy/tag/innovation/), [IT Operations](https://aws.amazon.com/blogs/enterprise-strategy/tag/it-operations/)

![Jim Haughwout](https://d2908q01vomqb2.cloudfront.net/cb7a1d775e800fd1ee4049f7dca9e041eb9ba083/2025/07/10/haugwout-headshot.jpg)

### Jim Haughwout

Jim Haughwout is the Vice President of Software Builder Experience at Amazon. In this role, he is responsible for tools, training, knowledge, and best practices used by tens of thousands of engineers to build and operate software for all Amazon customers. An early leader in the developer experience domain, Jim led creation of the Golden Path model, donated the opensource Backstage developer portal, and co-sponsored the creation of the Linux FinOps Foundation. A graduate of MIT and Harvard University, Jim has held executive and senior roles in leading companies for media, streaming, biotech, and defense and has been a member of advisory boards supporting multiple US administrations.

Loading comments…

### Resources

* [AWS Executive Insights](https://aws.amazon.com/executive-insights/)
* [Conversations with Leaders Podcast](https://aws.amazon.com/executive-insights/podcast/)
* [Conversations with Leaders Video Series](https://www.youtube.com/playlist?list=PLhr1KZpdzukfBEPOoB1RHGgOzzSsBGxiX)
* [AWS Executive Connection on LinkedIn](https://www.linkedin.com/showcase/aws-executive-connection/)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [RSS Feed](http://feeds.feedburner.com/AmazonWebServicesBlog)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=enterprise-resources)

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