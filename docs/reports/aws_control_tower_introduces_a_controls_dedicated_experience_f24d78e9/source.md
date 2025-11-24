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

# AWS Control Tower introduces a Controls Dedicated experience

by Veliswa Boya on 19 NOV 2025 in [AWS Config](https://aws.amazon.com/blogs/aws/category/management-tools/aws-config/ "View all posts in AWS Config"), [AWS Control Tower](https://aws.amazon.com/blogs/aws/category/management-tools/aws-control-tower/ "View all posts in AWS Control Tower"), [AWS Organizations](https://aws.amazon.com/blogs/aws/category/security-identity-compliance/aws-organizations/ "View all posts in AWS Organizations"), [Management Tools](https://aws.amazon.com/blogs/aws/category/management-tools/ "View all posts in Management Tools") [Permalink](https://aws.amazon.com/blogs/aws/aws-control-tower-introduces-a-controls-dedicated-experience/)  [Comments](https://aws.amazon.com/blogs/aws/aws-control-tower-introduces-a-controls-dedicated-experience/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing a [Controls Dedicated experience in AWS Control Tower](https://aws.amazon.com/controltower/). With this feature, you can use Amazon Web Services (AWS) managed controls without the need to set up resources you don’t need, which means you get started faster if you already have an established multi-account environment and want to use AWS Control Tower only for its managed controls. The Controls Dedicated experience gives you seamless access to the comprehensive collection of managed controls in the [Control Catalog](https://docs.aws.amazon.com/controlcatalog/latest/userguide/what-is-controlcatalog.html) to incrementally enhance your governance stance.

Until now, customers were required to adopt and configure many recommended best practices which meant implementing a full [AWS landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.html) at the time of setting up a multi-account environment. This setup included defining the prescribed organizational structure, required services, and more, in AWS Control Tower to start using landing zone. This approach is helpful to ensure a well-architected multi-account environment, however, for customers who already have an established, well-architected multi-account environment and only want to use AWS managed controls, it was more challenging for them to adopt AWS Control Tower. The new Controls Dedicated experience provides a faster and more flexible way of using AWS Control Tower.

**How it works**

Here’s how I define managed controls using the Controls Dedicated experience in AWS Control Tower in one of my accounts.

I start by choosing **Enable AWS Control Tower** on the AWS Control Tower landing page.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/03/Screenshot-2025-10-30-142542-1024x159.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/03/Screenshot-2025-10-30-142542.png)

I have the option to set up a full environment, or only set up controls using the Controls Dedicated experience. I opt to set up controls by choosing **I have an existing environment and want to enable AWS Managed Controls**. Next, I set up the rest of the information, such as choosing the **Home Region** from the dropdown list so that AWS Control Tower resources are provisioned in this Region during enablement. I also select **Turn on automatic account enrollment** for AWS Control Tower to enroll accounts automatically when I move them into a registered organization unit. The rest of the information is optional; I choose **Enable AWS Control Tower** to finalize the process, and the landing zone setup begins.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/03/Screenshot-2025-10-30-150947-2-954x1024.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/03/Screenshot-2025-10-30-150947-2.png)

The dashboard gives a summary of the environment such as the organizational units that were created, the shared accounts, the selected IAM configuration, the preventive controls to enforce policies, and detective controls to detect configuration violations.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/03/Screenshot-2025-10-30-155801-1024x655.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/03/Screenshot-2025-10-30-155801.png)

I choose **View enabled controls** for a list of all controls that were installed during this process.

The setup is completed, and now I have all the infrastructure required to use the controls in this account.

**Good to know**

Usually, an existing [AWS Organizations](https://aws.amazon.com/organizations/) account is required before you can use AWS Control Tower. If you’re using the console to create controls and don’t already have an Organizations account, one will be set up on your behalf.

**Now available**

Controls Dedicated experience in AWS Control Tower is available today in all [AWS Regions](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-supported-regions.html) where AWS Control Tower is available.

To learn more, visit our [AWS Control Tower page](https://aws.amazon.com/controltower/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el). For more information related to pricing, refer to [AWS Control Tower pricing](https://aws.amazon.com/controltower/pricing/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el). Send feedback to [AWS re:Post for AWS Control Tower](https://repost.aws/tags/TA8lQh6CBhTq6yxP2OZEkWVg/aws-control-tower) or through your usual AWS Support contacts.

– [Veliswa](https://linkedin.com/veliswa-boya).

![Veliswa Boya](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2021/07/09/vby-photo_300x300.jpg)

### Veliswa Boya

Veliswa Boya is a Senior Developer Advocate, based in South Africa and working closely with the builder community in Sub-Saharan Africa. She has fulfilled many roles in tech, which range from developer to analyst, architect to cloud engineer, and now a developer advocate. Veliswa especially enjoys working with those who are new to tech—and those getting started with AWS.

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