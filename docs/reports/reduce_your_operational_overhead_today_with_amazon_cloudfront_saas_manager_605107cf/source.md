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

# Reduce your operational overhead today with Amazon CloudFront SaaS Manager

by Veliswa Boya and [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 28 APR 2025 in [Amazon CloudFront](https://aws.amazon.com/blogs/aws/category/networking-content-delivery/amazon-cloudfront/ "View all posts in Amazon CloudFront"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [Networking & Content Delivery](https://aws.amazon.com/blogs/aws/category/networking-content-delivery/ "View all posts in Networking & Content Delivery"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [SaaS](https://aws.amazon.com/blogs/aws/category/saas/ "View all posts in SaaS") [Permalink](https://aws.amazon.com/blogs/aws/reduce-your-operational-overhead-today-with-amazon-cloudfront-saas-manager/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, I’m happy to announce the general availability of [Amazon CloudFront](https://aws.amazon.com/cloudfront/) SaaS Manager, a new feature that helps [software-as-a-service (SaaS)](https://aws.amazon.com/what-is/saas/) providers, web development platform providers, and companies with multiple brands and websites efficiently manage delivery across multiple domains. Customers already use CloudFront to securely deliver content with low latency and high transfer speeds. CloudFront SaaS Manager addresses a critical challenge these organizations face: managing tenant websites at scale, each requiring TLS certificates, distributed denial-of-service (DDoS) protection, and performance monitoring.

With CloudFront Saas Manager, web development platform providers and enterprise SaaS providers who manage a large number of domains will use simple APIs and reusable configurations that use CloudFront edge locations worldwide, [AWS WAF](https://aws.amazon.com/waf/), and [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/). CloudFront SaaS Manager can dramatically reduce operational complexity while providing high-performance content delivery and enterprise-grade security for every customer domain.

**How it works**

In CloudFront, you can use [multi-tenant SaaS deployments](https://aws.amazon.com/developer/application-security-performance/articles/saas/), a strategy where a single CloudFront distribution serves content for multiple distinct tenants (users or organizations). CloudFront SaaS Manager uses a new template-based distribution model called a multi-tenant distribution to serve content across multiple domains while sharing configuration and infrastructure. However, if supporting single websites or application, a standard distribution would be better or recommended.

A template distribution defines the base configuration that will be used across domains such as origin configurations, cache behaviors, and security settings. Each template distribution has a distribution tenant to represent domain-specific origin paths or origin domain names including web access control list (ACL) overrides and custom TLS certificates.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/27/2025-cloudfront-saas-manager-template-model.jpg)

Optionally, multiple distribution tenants can use the same connection group that provides the CloudFront routing endpoint that serves content to viewers. [DNS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html) records point to the CloudFront endpoint of the connection group using a [Canonical Name Record (CNAME)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#CNAMEFormat).

To learn more, visit [Understand how multi-tenant distributions work](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html) in the Amazon CloudFront Developer Guide.

**CloudFront SaaS Manager in action**

I’d like to give you an example to help you understand the capabilities of CloudFront SaaS Manager. You have a company called MyStore, a popular e-commerce platform that helps your customer easily set up and manage an online store. MyStore’s tenants already enjoy outstanding customer service, security, reliability, and ease-of-use with little setup required to get a store up and running, resulting in 99.95 percent uptime for the last 12 months.

Customers of MyStore are unevenly distributed across three different pricing tiers: Bronze, Silver, and Gold, and each customer is assigned a persistent `mystore.app` subdomain. You can apply these tiers to different customer segments, customized settings, and operational Regions. For example, you can add AWS WAF service in the Gold tier as an advanced feature. In this example, MyStore has decided not to maintain their own web servers to handle TLS connections and security for a growing number of applications hosted on their platform. They are evaluating CloudFront to see if that will help them reduce operational overhead.

Let’s find how as MyStore you configure your customer’s websites distributed in multiple tiers with the CloudFront SaaS Manager. To get started, you can create a multi-tenant distribution that acts as a template corresponding to each of the three pricing tiers the MyStore offers: Bronze, Sliver, and Gold shown in **Multi-tenant distribution** under the **SaaS** menu on the [Amazon CloudFront console](https://console.aws.amazon.com/cloudfront).

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/20/2025-cf-saas-manager-1-multi-tenant-distribution.png)

To create a multi-tenant distribution, choose **Create distribution** and select **Multi-tenant architecture** if you have multiple websites or applications that will share the same configuration. Follow the steps to provide basic details such as a name for your distribution, tags, and wildcard certificate, specify origin type and location for your content such as a website or app, and enable security protections with AWS WAF web ACL feature.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/20/2025-cf-saas-manager-2-create-multi-tenants.png)

When the multi-tenant distribution is created successfully, you can create a distribution tenant by choosing **Create tenant** in the **Distribution tenants** menu in the left navigation pane. You can create a distribution tenant to add your active customer to be associated with the Bronze tier.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/20/2025-cf-saas-manager-3-create-tenants.png)

Each tenant can be associated with up to one multi-tenant distribution. You can add one or more domains of your customers to a distribution tenant and assign custom parameter values such as origin domains and origin paths. A distribution tenant can inherit the TLS certificate and security configuration of its associated multi-tenant distribution. You can also attach a new certificate specifically for the tenant, or you can override the tenant security configuration.

When the distribution tenant is created successfully, you can finalize this step by updating a DNS record to route traffic to the domain in this distribution tenant and creating a CNAME pointed to the CloudFront application endpoint. To learn more, visit [Create a distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.html) in the Amazon CloudFront Developer Guide.

Now you can see all customers in each distribution tenant to associate multi-tenant distributions.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/20/2025-cf-saas-manager-4-tentants.png)

By increasing customers’ business needs, you can upgrade your customers from Bronze to Silver tiers by moving those distribution tenants to a proper multi-tenant distribution.

During the monthly maintenance process, we identify domains associated with inactive customer accounts that can be safely decommissioned. If you’ve decided to deprecate the Bronze tier and migrate all customers who are currently in the Bronze tier to the Silver tier, then you can delete a multi-tenant distribution to associate the Bronze tier. To learn more, visit [Update a distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToUpdateDistribution.html) or [Distribution tenant customizations](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/tenant-customization.html) in the Amazon CloudFront Developer Guide.

By default, your AWS account has one connection group that handles all your CloudFront traffic. You can enable **Connection group** in the **Settings** menu in the left navigation pane to create additional connection groups, giving you more control over traffic management and tenant isolation.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/28/2025-cf-saas-manager-5-connection-group-1.png)

To learn more, visit [Create custom connection group](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-connection-group.html) in the Amazon CloudFront Developer Guide.

**Now available**

Amazon CloudFront SaaS Manager is available today. To learn about, visit [CloudFront SaaS Manager product page](http://aws.amazon.com/cloudfront/features/saas-manager) and [documentation page](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html). To learn about SaaS on AWS, visit [AWS SaaS Factory](https://aws.amazon.com/partners/programs/saas-factory).

Give CloudFront SaaS Manager a try in the [CloudFront console](https://console.aws.amazon.com/cloudfront) today and send feedback to [AWS re:Post for Amazon CloudFront](https://repost.aws/tags/TA8pHF0m5aQdawzT2gwPcVYQ) or through your usual AWS Support contacts.

— [Veliswa](https://www.linkedin.com/in/veliswa-boya/).

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

How is the News Blog doing? Take this [1 minute survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi)!

(*This [survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi) is hosted by an external company. AWS handles your information as described in the [AWS Privacy Notice](https://aws.amazon.com/privacy/). AWS will own the data gathered via this survey and will not share the information collected with survey respondents.*)

![Veliswa Boya](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2021/07/09/vby-photo_300x300.jpg)

### Veliswa Boya

Veliswa Boya is a Senior Developer Advocate, based in South Africa and working closely with the builder community in Sub-Saharan Africa. She has fulfilled many roles in tech, which range from developer to analyst, architect to cloud engineer, and now a developer advocate. Veliswa especially enjoys working with those who are new to tech—and those getting started with AWS.

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