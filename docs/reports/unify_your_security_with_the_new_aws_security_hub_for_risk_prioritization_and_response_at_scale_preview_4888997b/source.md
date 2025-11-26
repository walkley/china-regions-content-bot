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

# Unify your security with the new AWS Security Hub for risk prioritization and response at scale (Preview)

by [Donnie Prakoso](https://aws.amazon.com/blogs/aws/author/donnie/ "Posts by Donnie Prakoso") on 17 JUN 2025 in [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS re:Inforce](https://aws.amazon.com/blogs/aws/category/events/aws-reinforce/ "View all posts in AWS re:Inforce"), [AWS Security Hub](https://aws.amazon.com/blogs/aws/category/security-identity-compliance/aws-security-hub/ "View all posts in AWS Security Hub"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/aws/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance") [Permalink](https://aws.amazon.com/blogs/aws/unify-your-security-with-the-new-aws-security-hub-for-risk-prioritization-and-response-at-scale-preview/)  [Comments](https://aws.amazon.com/blogs/aws/unify-your-security-with-the-new-aws-security-hub-for-risk-prioritization-and-response-at-scale-preview/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

AWS Security Hub has been a central place for you to view and aggregate security alerts and compliance status across Amazon Web Services (AWS) accounts. Today, we are announcing the preview release of the new AWS Security Hub which offers additional correlation, contextualization, and visualization capabilities. This helps you prioritize critical security issues, respond at scale to reduce risks, improve team productivity, and better protect your cloud environment.

Here’s a quick look at the new AWS Security Hub.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/13/news_2025-06_security-hub-17-1.png?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el)

With this new enhancement, AWS Security Hub integrates security capabilities like [Amazon GuardDuty](https://aws.amazon.com/guardduty/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el), [Amazon Inspector](https://aws.amazon.com/inspector/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el), [AWS Security Hub Cloud Security Posture Management (CSPM)](https://aws.amazon.com/security-hub/cspm/features/), [Amazon Macie](https://aws.amazon.com/macie/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el), and other AWS security capabilities to help you gain visibility across your cloud environment through centralized management in a unified cloud security solution.

**Getting started with the new AWS Security Hub**

Let me walk you through how to get started with AWS Security Hub.

If you’re a new customer to AWS Security Hub, you need to navigate to the AWS Security Hub console to enable AWS security capabilities and capabilities and start assessing risk across your organization. You can learn more on the [Documentation page](https://docs.aws.amazon.com/securityhub/latest/userguide/security-hub-adv-getting-started-enable.html?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el).

After you have AWS Security Hub enabled, it will automatically consume data from supporting security capabilities you’ve enabled, such as Amazon GuardDuty, Amazon Inspector, Amazon Macie, and AWS Security Hub CSPM. You can navigate to the AWS Security Hub console to view these findings and benefit from insights created through correlation of findings across these capabilities.

As security risks are uncovered, they’re presented in a redesigned Security Hub summary dashboard. The new Security Hub summary dashboard provides a comprehensive, unified view of your AWS security posture. The dashboard organizes security findings into distinct categories, making it easier to identify and prioritize risks.

The new **Exposure summary** widget helps you identify and prioritize security exposures by analyzing resource relationships and signals from Amazon Inspector, AWS Security Hub CSPM, and Amazon Macie. These exposure findings are automatically generated and are a key part of the new solution, highlighting where your critical security exposures are located. You can learn more about exposure on the [Documentation page](https://docs.aws.amazon.com/securityhub/latest/userguide/exposure-fidnings-adv.html?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el).

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/11/news_2025-06_security-hub-06.png?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el)

AWS Security Hub now provides a **Security coverage** widget designed to help you identify potential coverage gaps. You can use this widget to identify where you’re missing coverage by the security capabilities that power Security Hub. This visibility helps you identify which capabilities, accounts, and features you need to address to improve your security coverage.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/11/news_2025-06_security-hub-04-1.png?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el)

As you can see on the navigation menu, AWS Security Hub is organized into five key areas to streamline security management:

* **Exposure**: Provides visibility into all exposure findings, a security vulnerability or misconfiguration that could potentially expose an AWS resource or system to unauthorized access or compromise, generated by Security Hub, helping you identify resources that might be accessible from outside your environment
* **Threats**: Consolidates all threat findings generated by Amazon GuardDuty, showing potential malicious activities and intrusion attempts
* **Vulnerabilities**: Displays all vulnerabilities detected by Amazon Inspector, highlighting software flaws and configuration issues
* **Posture management**: Shows all posture management findings from AWS Security Hub Cloud Security Posture Management (CSPM), helping provide compliance with security best practices
* **Sensitive data**: Presents all sensitive data findings identified by Amazon Macie, helping you track and protect your sensitive information

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/13/news_2025-06_security-hub-18.png?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el)

When you navigate to the [**Exposure**](https://console.aws.amazon.com/securityhub/v2/home#/exposure?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) page, you’ll see findings grouped by title, with severity levels clearly indicated to help you focus on critical issues first.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/11/news_2025-06_security-hub-07.png?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el)

To explore specific exposures, you can select any finding to see affected resources. The panel includes key information about the implicated resource, account, Region, and when the issue was detected.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/11/news_2025-06_security-hub-08.png?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el)

In this panel, you’ll also find an attack path visualization that is particularly useful for understanding complex security relationships. For network exposure paths, you can see all components involved in the path—including virtual private clouds (VPCs), subnets, security groups, network access control lists (ACLs), and load balancers—helping you identify exactly where to implement security controls. The visualization also highlights Identity and Access Management (IAM) relationships, showing how permission configurations might allow privilege escalation or data access. Resources with multiple contributing traits are clearly marked so you can quickly identify which components represent the greatest risk.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/11/news_2025-06_security-hub-10.png?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el)

The [**Threats**](https://console.aws.amazon.com/securityhub/v2/home#/threats?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) dashboard provides actionable insights into potential malicious activities detected by Amazon GuardDuty, organizing findings by severity so you can quickly identify critical issues like unusual API calls, suspicious network traffic, or potential credential compromises. The dashboard includes [GuardDuty Extended Threat Detection](https://aws.amazon.com/blogs/aws/introducing-amazon-guardduty-extended-threat-detection-aiml-attack-sequence-identification-for-enhanced-cloud-security/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) findings, with all “Critical” severity threats representing these Extended Threat Detections that require immediate attention.

Similarly, the [**Vulnerabilities**](https://console.aws.amazon.com/securityhub/v2/home#/vulnerabilities?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) dashboard from Amazon Inspector provides a comprehensive view of software vulnerabilities and network exposure risks. The dashboard highlights vulnerabilities with known exploits, packages requiring urgent updates, and resources with the highest numbers of vulnerabilities.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/11/news_2025-06_security-hub-14.png?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el)

Another valuable new feature is the [**Resources**](https://console.aws.amazon.com/securityhub/v2/home#/resources?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) view, which provides an inventory of all resources deployed in your organization covered by AWS Security Hub. You can use this view to quickly identify which resources have findings against them and filter by resource type or finding severity. Selecting any resource provides detailed configuration information without needing to pivot to other consoles, streamlining your investigation workflow.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/11/news_2025-06_security-hub-12.png?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el)

The new Security Hub also offers integration capabilities to help you comprehensively monitor your cloud environments and connect with third-party security solutions. This gives you the flexibility to create a unified security solution tailored to your organization’s specific needs.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/12/news_2025-06_security-hub-15.png?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el)

For example, with integration capability, when viewing a security finding, you can select the **Create ticket** option and choose your preferred ticketing integration.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/12/news_2025-06_security-hub-16.png?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el)

**Additional things to know**

Here are a couple of things to note:

* **Availability** – During this preview period, the new AWS Security Hub is available in following AWS Regions: US East (N. Virginia, Ohio), US West (N. California, Oregon), Africa (Cape Town), Asia Pacific (Hong Kong, Jakarta, Mumbai, Osaka, Seoul, Singapore, Sydney, Tokyo), Canada (Central), Europe (Frankfurt, Ireland, London, Milan, Paris, Stockholm), Middle East (Bahrain), and South America (São Paulo).
* **Pricing** – The new AWS Security Hub is available at no additional charge during the preview period. However, you will still incur costs for the integrated capabilities including Amazon GuardDuty, Amazon Inspector, Amazon Macie, and AWS Security Hub CSPM.
* **Integration with existing AWS security capabilities** – Security Hub integrates with Amazon GuardDuty, Amazon Inspector, AWS Security Hub CSPM, and Amazon Macie, providing a comprehensive security posture without additional operational overhead.
* **Enhanced data interoperability** – The new Security Hub uses the [Open Cybersecurity Schema Framework (OCSF)](https://github.com/ocsf), enabling seamless data exchange across your security capabilities with normalized data formats.

To learn more about the enhanced AWS Security Hub and join the preview, visit the [AWS Security Hub](https://aws.amazon.com/security-hub/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) product page.

Happy building!

— [Donnie](https://linkedin.com/in/donnieprakoso)

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