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

## [Networking & Content Delivery](https://aws.amazon.com/blogs/networking-and-content-delivery/)

# Introducing flat-rate pricing plans with no overages

by Cristian Graziano on 18 NOV 2025 in [Amazon CloudFront](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/amazon-cloudfront/ "View all posts in Amazon CloudFront"), [Amazon CloudWatch](https://aws.amazon.com/blogs/networking-and-content-delivery/category/management-tools/amazon-cloudwatch/ "View all posts in Amazon CloudWatch"), [Amazon Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/amazon-route-53/ "View all posts in Amazon Route 53"), [Amazon Simple Storage Service (S3)](https://aws.amazon.com/blogs/networking-and-content-delivery/category/storage/amazon-simple-storage-services-s3/ "View all posts in Amazon Simple Storage Service (S3)"), [Announcements](https://aws.amazon.com/blogs/networking-and-content-delivery/category/post-types/announcements/ "View all posts in Announcements"), [AWS WAF](https://aws.amazon.com/blogs/networking-and-content-delivery/category/security-identity-compliance/aws-waf/ "View all posts in AWS WAF"), [Networking & Content Delivery](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/ "View all posts in Networking & Content Delivery") [Permalink](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-flat-rate-pricing-plans-with-no-overages/) Share

Today, Amazon Web Services (AWS) is launching [flat-rate pricing plans](https://aws.amazon.com/cloudfront/pricing/) with no overages for website delivery and security. The pricing plans, available with [Amazon CloudFront](https://aws.amazon.com/cloudfront/), combine global content delivery (CDN) with multiple AWS services and features into a **monthly price with no overage charges, regardless of whether your website or application goes viral or faces a DDoS attack**.

Flat-rate pricing plans include the following features for a simple monthly price:

* CloudFront CDN
* [AWS WAF](https://aws.amazon.com/waf/) and DDoS protection
* Bot management and analytics
* [Amazon Route 53](https://aws.amazon.com/route53/) DNS
* [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) Logs ingestion
* Serverless edge compute
* Monthly [Amazon S3](https://aws.amazon.com/s3/) storage credits

Flat-rate pricing plans are now available in Free ($0/month), Pro ($15/month), Business ($200/month), and Premium ($1,000/month) tiers to match your application’s needs. Plans do not require an annual commitment to get the best available rates. Select the plan tier with the features and usage allowances matching your application’s needs. Upgrade to access more capabilities as your needs evolve.

![Flat-rate pricing compared to pay-as-you-go pricing](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/11/17/cloudfront-flat-rate-pricing-comparison-1024x392.jpg)

## Why predictable pricing matters

CloudFront, the high-speed, low-latency global AWS content delivery network, has grown with our customers since its introduction in 2008, helping customers scale millions of applications from idea to global success. Our pay-as-you-go pricing, including a 1TB perpetual free tier, eliminates upfront costs and commitments, giving customers complete flexibility to innovate and expand. Customers choose the features they need and pay only for what they use, with costs that scale naturally as they grow.

Pay-as-you-go pricing works well for most customers. However, customers have asked us to help them address two challenges with internet-facing applications. First, customers tell us it can be difficult to predict costs upfront. Estimating costs means navigating pricing dimensions across multiple services needed to deliver applications. Second, more critically, costs can spike as a result of external factors that can be beyond the customer’s control. A successful product launch, viral content, or targeted DDoS attack can multiply traffic instantly, turning what should be a moment of triumph or resilience into a financial concern.

We’ve made significant improvements to help customers address these challenges. Last year, [we removed charges for requests blocked by AWS WAF](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-cloudfront-charges-requests-blocked-aws-waf/), and in June we introduced [affordable DDoS protection](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-the-aws-waf-application-layer-ddos-protection/) to make sure that attack traffic doesn’t impact your security bill. These are major steps toward more predictable costs. As we discussed these changes with customers, many asked us to deliver pricing without overages for all traffic, both legitimate and malicious, including downstream services such as logging that can be affected by traffic spikes. They also wanted confidence that their personal websites and educational projects with minimal usage could run on AWS without the risk of overages, even if traffic unexpectedly spikes.

That’s why we’re now launching flat-rate pricing plans: to give you simplified pricing across essential services with no overages, regardless of traffic spikes or attacks, including a $0/month Free tier.

## Everything you need to deliver fast and secure applications

Each plan includes a CloudFront distribution with one domain that combines essential features and services into one price.

Start with the Free tier ($0/month) to build and learn, then upgrade to Pro ($15/month) when you need added security capabilities and insights. Business ($200/month) adds advanced protection and control for commercial applications, while Premium ($1,000/month) adds increased performance, application load reduction, and failover capabilities for mission-critical workloads.

## Transparent usage allowances

When customers talk to us about flat-rate pricing, they tell us that how the offering is structured matters just as much as the final bill. They want to know exactly what usage is included and how the service behaves as they grow. Transparency helps customers confidently plan their growth with clear visibility into usage allowances.

### How CloudFront plan usage allowances work

Each CloudFront plan includes a clear, published usage allowance designed to maintain optimal performance for that tier. The Free tier supports 1M requests and 100 GB of data transfer monthly (up to three Free tier plans per AWS account). All paid tiers include up to 50 TB of data transfer with increasing request allowances: Pro at 10M requests, Business at 125M requests, and Premium at 500M requests monthly. Accounts can have up to 100 plans total. You can upgrade anytime to access more features and increased usage allowances.

You may experience reduced performance if you exceed your allowance, but you won’t incur overage charges. We’ll notify you as you approach your allowance at 50%, 80%, and 100%, and you can monitor your usage in the console anytime.

![CloudFront usage allowance notifications](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/11/18/cloudfront-flat-rate-plans-usage-allowance-1024x856.jpg)

Plans give you the ability to shape your usage allowance with the requests you want. **Blocked requests and DDoS attacks never count against your allowance**, ensuring that defending your application against threats won’t impact performance or cost. You can also configure security rules to exclude unwanted traffic from your usage allowance, such as blocking requests from certain countries or with specific characteristics.

## Extend flat-rate pricing to your AWS applications

If you’re running internet-facing applications on AWS but don’t use CloudFront today, then these flat-rate CloudFront plans can make your AWS data transfer costs more predictable while improving your application’s security, availability, and performance. CloudFront CDN works as a reverse proxy, receiving all incoming traffic at its 750+ Points of Presence (PoPs) and forwarding requests not served from cache to your application. Data transfer from AWS applications running on services such as Amazon S3, [AWS Application Load Balancer (ALB)](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/), or [Amazon API Gateway](https://aws.amazon.com/api-gateway/) to CloudFront continues to be free. When you serve your AWS applications through CloudFront instead of directly to the internet, your flat-rate plan covers the data transfer costs between your applications and your viewers for a simple monthly price without the worry of overages.

**Better performance for every application—even without caching**: Although CDNs are known for caching static content, CloudFront improves performance for any application with a public endpoint whether it’s a dynamic API, a complex web application, or a static site. Here’s how:

1. **Faster connections**: Every time a user visits your application, their browser or user agent needs to establish a secure (TLS) connection. Without CloudFront, this means multiple round trips across the internet to your application to complete the encryption handshake. With CloudFront, this happens at the optimal PoP near your users, shortening the round trip time by potentially hundreds of milliseconds per request (depending on where your users and application are located).
2. **Optimized traffic flow**: CloudFront maintains persistent connections to your origin, eliminating the time needed to establish new connections for every request. This makes your requests faster. Your users first connect to a nearby CloudFront PoP. If the response cannot be served from the CloudFront cache, then traffic to your applications flows over the AWS private backbone network instead of the public internet. This avoids congestion and routing issues that can add unpredictable latency to your requests.
3. **Lower total costs**: This architecture reduces costs throughout your stack. Security rules block unwanted traffic at the edge before they reach your infrastructure. CloudFront collapses duplicate requests to reduce load on your application. And when content can be cached, it serves directly from CloudFront PoPs instead of your application. This ultimately reduces your costs from services that bill based on usage such as your compute, database, and other AWS services.

## Getting started

Whether you’re building new applications or running existing ones on AWS, you can get started now with flat-rate plans. Visit the CloudFront console to opt into a plan. Start with a new CloudFront distribution or migrate existing distributions to flat-rate pricing. You can mix pay-as-you-go and flat-rate plans across different distributions, giving you the flexibility to choose the right pricing model for each application. The CloudFront 1TB perpetual free tier will continue to apply to any pay-as-you-go usage, and you can also have up to three Free pricing plans per account.

Plans do not require an annual commitment to get the best available rates. Plans are purchased for the current billing period (month) and automatically renew until canceled.

Ready to get started? View [Plans and Pricing](https://aws.amazon.com/cloudfront/pricing/), visit the [CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.html) to learn about plans, or get started today in the [CloudFront console](https://us-east-1.console.aws.amazon.com/cloudfront/v4/home?region=us-east-1#/distributions).

TAGS: [Amazon CloudFront](https://aws.amazon.com/blogs/networking-and-content-delivery/tag/amazon-cloudfront/), [Amazon CloudWatch](https://aws.amazon.com/blogs/networking-and-content-delivery/tag/amazon-cloudwatch/), [Amazon Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/tag/amazon-route-53/), [Amazon Simple Storage Service (S3)](https://aws.amazon.com/blogs/networking-and-content-delivery/tag/amazon-simple-storage-service-s3/), [AWS WAF](https://aws.amazon.com/blogs/networking-and-content-delivery/tag/aws-waf/)

### Resources

* [Networking Products](https://aws.amazon.com/products/networking?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=networking-resources)
* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=networking-resources)
* [Amazon CloudFront](https://aws.amazon.com/cloudfront?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=networking-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
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