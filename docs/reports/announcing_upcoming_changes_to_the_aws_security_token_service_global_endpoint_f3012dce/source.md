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

## [AWS Security Blog](https://aws.amazon.com/blogs/security/)

# Announcing upcoming changes to the AWS Security Token Service global endpoint

by Palak Arora and Liam Wadman on 27 JAN 2025 in [Announcements](https://aws.amazon.com/blogs/security/category/post-types/announcements/ "View all posts in Announcements"), [AWS Identity and Access Management (IAM)](https://aws.amazon.com/blogs/security/category/security-identity-compliance/aws-identity-and-access-management-iam/ "View all posts in AWS Identity and Access Management (IAM)"), [AWS Security Token Service](https://aws.amazon.com/blogs/security/category/security-identity-compliance/aws-security-token-service/ "View all posts in AWS Security Token Service"), [Intermediate (200)](https://aws.amazon.com/blogs/security/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [Resilience](https://aws.amazon.com/blogs/security/category/resilience/ "View all posts in Resilience"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/security/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance") [Permalink](https://aws.amazon.com/blogs/security/announcing-upcoming-changes-to-the-aws-security-token-service-global-endpoint/)  [Comments](https://aws.amazon.com/blogs/security/announcing-upcoming-changes-to-the-aws-security-token-service-global-endpoint/#Comments)  Share

> **April 18, 2025:** AWS has made changes to the AWS Security Token Service (AWS STS) global endpoint (`sts.amazonaws.com`) in Regions [enabled by default](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) to enhance its resiliency and performance. AWS STS requests to the global endpoint are automatically served in the same AWS Region as your workloads. These changes will not be deployed to opt-in Regions. We recommend that you use the appropriate AWS STS regional endpoints. For more information, see [AWS STS global endpoint changes](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_region-endpoints.html#reference_sts_global_endpoint_changes) in the IAM User Guide.

---

AWS launched [AWS Security Token Service (AWS STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) in August 2011 with a single global endpoint `(https://sts.amazonaws.com)`, hosted in the US East (N. Virginia) AWS Region. To reduce dependency on a single Region, STS launched [AWS STS Regional endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sts-regionalized-endpoints.html) (`https://sts.{Region_identifier}.{partition_domain}`) in February 2015. These Regional endpoints allow you to use STS in the same Region as your workloads, which improves both performance and reliability.

However, many customers and third-party tools continue to call the STS global endpoint, and as a result, these customers don’t get the benefits of STS Regional endpoints. To help improve the resiliency and performance of your applications, we are making changes to the STS global endpoint, with no action required from customers. These changes will be released in the coming weeks.

In this blog post, we discuss the upcoming changes to the STS global endpoint and their benefits, and provide our recommendation on which STS endpoint to use going forward.

## Upcoming changes to the STS global endpoint

The changes being made to the STS global endpoint will help enhance resiliency and improve performance. Today, all the requests to the STS global endpoint are served by the US East (N. Virginia) Region. Starting in early 2025, requests to the STS global endpoint will be automatically served in the same Region as your AWS deployed workloads. For example, if your application calls `sts.amazonaws.com` from the US West (Oregon) Region, your calls will be served locally in the US West (Oregon) Region instead of being served by the US East (N. Virginia) Region.

With this change, requests to the STS global endpoint will be served locally if your request originated from [AWS Regions that are enabled by default](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html).1 However, requests to the STS global endpoint will continue to be served in US East (N. Virginia) Region if your request originated from opt-in Regions or if you used STS from outside AWS, such as in your on-premises network or data centers.

We will gradually roll out this change to AWS Regions that are enabled by default by mid-2025, starting with the Europe (Stockholm) Region.

We’ve taken the following measures to help avoid disruptions to your existing processes:

* [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) logs for requests made to the STS global endpoints will be sent to the US East (N. Virginia) Region. CloudTrail logs for requests handled by STS Regional endpoints will continue to be logged to their respective Region in CloudTrail, even if the requests are served locally.
* CloudTrail logs for operations performed by the STS global and Regional endpoints will have the additional fields `endpointType` and `awsServingRegion` to clarify which endpoint and Region served the request.
* Requests made to the `sts.amazonaws.com` endpoints will have a value of `us-east-1` for the `aws:RequestedRegion` condition key, regardless of which Region served the request.
* Requests handled by the `sts.amazonaws.com` endpoints will not share a request quota with the Regional STS endpoints.

1. In addition, for your requests to be served locally, your DNS request for `sts.amazonaws.com` must be handled by an Amazon DNS Server in Amazon Virtual Private Cloud (Amazon VPC).

## Our recommendation

We continue to recommend that you use the appropriate [STS Regional endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sts-regionalized-endpoints.html) whenever possible. If you’re using STS from outside AWS, such as in your on-premises networks or data centers, we recommend you use the STS Regional endpoint that is hosted in the same Region as the AWS resource that you need STS credentials to access. If you’re building in opt-in Regions such as Asia Pacific (Hong Kong) or Asia Pacific (Jakarta), we recommend that you use the STS endpoint from the opt-in Region that is hosting your workload. By following the steps in the blog post [How to use Regional AWS STS endpoints](https://aws.amazon.com/blogs/security/how-to-use-regional-aws-sts-endpoints/), you can identify workloads that are still using the global STS endpoint and get insights into how to reconfigure them when required.

If you have feedback about this blog post, submit comments in the **Comments** section below. If you have questions about this post, [contact AWS Support](https://console.aws.amazon.com/support/home).

![Palak Arora](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2023/01/30/pkarora.jpg) Palak Arora

Palak is a Senior Product Manager at AWS Identity. She has over eight years of cybersecurity experience, with a specialization in the Identity and Access Management (IAM) domain. She has helped various customers across different sectors define their enterprise and customer IAM roadmaps and strategies, and improve their overall technology risk landscape.

![Liam Wadman](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2022/11/01/liwadman.jpg) Liam Wadman

Liam is a Principal Solutions Architect with the AWS Identity team. When he’s not building exciting solutions on AWS or helping customers, he’s often found in the hills of British Columbia on his mountain bike. Liam points out that you cannot spell LIAM without IAM.

TAGS: [AWS Identity and Access Management (IAM)](https://aws.amazon.com/blogs/security/tag/aws-identity-and-access-management-iam/), [AWS STS](https://aws.amazon.com/blogs/security/tag/aws-sts/), [Security Blog](https://aws.amazon.com/blogs/security/tag/security-blog/)

Loading comments…

### Resources

* [AWS Cloud Security](https://aws.amazon.com/security?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-resources)
* [AWS Compliance](https://aws.amazon.com/compliance?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-resources)
* [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html?secd_ip5)
* [Best Practices](https://aws.amazon.com/architecture/security-identity-compliance)
* [Data Protection at AWS](https://aws.amazon.com/compliance/data-protection/)
* [Zero Trust on AWS](https://aws.amazon.com/security/zero-trust/)
* [Cryptographic Computing](https://aws.amazon.com/security/cryptographic-computing/)

---

### Follow

* [Twitter](https://twitter.com/AWSsecurityinfo)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-social)

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