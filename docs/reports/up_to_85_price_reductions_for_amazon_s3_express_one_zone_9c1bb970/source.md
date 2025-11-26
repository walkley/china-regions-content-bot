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

# Announcing up to 85% price reductions for Amazon S3 Express One Zone

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 10 APR 2025 in [Amazon Simple Storage Service (S3)](https://aws.amazon.com/blogs/aws/category/storage/amazon-simple-storage-services-s3/ "View all posts in Amazon Simple Storage Service (S3)"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Price Reduction](https://aws.amazon.com/blogs/aws/category/price-reduction/ "View all posts in Price Reduction"), [Storage](https://aws.amazon.com/blogs/aws/category/storage/ "View all posts in Storage") [Permalink](https://aws.amazon.com/blogs/aws/up-to-85-price-reductions-for-amazon-s3-express-one-zone/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

At re:Invent 2023, we [introduced](https://aws.amazon.com/blogs/aws/new-amazon-s3-express-one-zone-high-performance-storage-class/) [Amazon S3 Express One Zone](https://aws.amazon.com/s3/storage-classes/express-one-zone/), a high-performance, single-Availability Zone (AZ) storage class purpose-built to deliver consistent single-digit millisecond data access for your most frequently accessed data and latency-sensitive applications.

S3 Express One Zone delivers data access speed up to 10 times faster than S3 Standard, and it can support up to 2 million `GET` transactions per second (TPS) and up to 200,000 `PUT` TPS per directory bucket. This makes it ideal for performance-intensive workloads such as interactive data analytics, data streaming, media rendering and transcoding, high performance computing (HPC), and AI/ML trainings. Using S3 Express One Zone, customers like [Fundrise](https://aws.amazon.com/blogs/storage/fundrise-uses-amazon-s3-express-one-zone-to-accelerate-investment-data-processing/), [Aura](https://aws.amazon.com/blogs/storage/how-aura-improves-database-performance-using-amazon-s3-express-one-zone-for-caching/), [Lyrebird](https://aws.amazon.com/blogs/storage/lyrebird-improves-performance-and-reduces-costs-for-generative-ai-workloads-using-amazon-s3-express-one-zone/), [Vivian Health](https://aws.amazon.com/blogs/storage/how-vivian-health-is-using-amazon-s3-express-one-zone-to-accelerate-healthcare-hiring/), and [Fetch](https://aws.amazon.com/blogs/storage/how-fetch-reduces-latency-on-image-uploads-using-amazon-s3-express-one-zone/) improved the performance and reduced the costs of their data-intensive workloads.

Since launch, we’ve introduced [a number of features](https://aws.amazon.com/about-aws/whats-new/storage/?whats-new-content.q=S3%2BExpress%2BOne%2BZone) for our customers using S3 Express One Zone. For example, S3 Express One Zone started to support [object expiration using S3 Lifecycle](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-s3-express-one-zone-s3-lifecycle-expirations/) to expire objects based on age to help you automatically optimize storage costs. In addition, your log-processing or media-broadcasting applications can directly [append new data to the end of existing objects](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-s3-express-one-zone-append-data-object/) and then immediately read the object, all within S3 Express One Zone.

Today we’re announcing that, effective April 10, 2025, S3 Express One Zone has reduced storage prices by 31 percent, `PUT` request prices by 55 percent, and `GET` request prices by 85 percent. In addition, S3 Express One Zone has reduced the per-GB charges for data uploads and retrievals by 60 percent, and these charges now apply to all bytes transferred rather than just portions of requests greater than 512 KB.

Here is a price reduction table in the US East (N. Virginia) Region:

|  |  |  |  |
| --- | --- | --- | --- |
| **Price** | **Previous** | **New** | **Price reduction** |
| **Storage** (per GB-Month) | $0.16 | $0.11 | 31% |
| **Writes** (`PUT` requests) | $0.0025 per 1,000 requests up to 512 KB | $0.00113 per 1,000 requests | 55% |
| **Reads** (`GET` requests) | $0.0002 per 1,000 requests up to 512 KB | $0.00003 per 1,000 requests | 85% |
| **Data upload** (per GB) | $0.008 | $0.0032 | 60% |
| **Data retrievals** (per GB) | $0.0015 | $0.0006 | 60% |

For S3 Express One Zone pricing examples, go to the [S3 billing FAQs](https://aws.amazon.com/s3/faqs/#S3_Express_One_Zone) or use the [AWS Pricing Calculator](https://calculator.aws/).

These pricing reductions apply to [S3 Express One Zone in all AWS Regions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Endpoints.html) where the storage class is available: US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Europe (Ireland), and Europe (Stockholm) Regions. To learn more, visit the [Amazon S3 pricing page](https://aws.amazon.com/s3/pricing/) and [S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-high-performance.html) in the AWS Documentation.

Give S3 Express One Zone a try in the [S3 console](https://console.aws.amazon.com/s3) today and send feedback to [AWS re:Post for Amazon S3](https://repost.aws/tags/TADSTjraA0Q4-a1dxk6eUYaw/amazon-simple-storage-service) or through your usual AWS Support contacts.

— [Channy](https://x.com/channyun)

---

How is the News Blog doing? Take this [1 minute survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi)!

*(This [survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi) is hosted by an external company. AWS handles your information as described in the [AWS Privacy Notice](https://aws.amazon.com/privacy/?trk=4b29643c-e00f-4ab6-ab9c-b1fb47aa1708&sc_channel=blog). AWS will own the data gathered via this survey and will not share the information collected with survey respondents.)*

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