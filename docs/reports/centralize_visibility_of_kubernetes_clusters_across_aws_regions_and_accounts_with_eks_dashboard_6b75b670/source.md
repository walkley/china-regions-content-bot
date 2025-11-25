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

# Centralize visibility of Kubernetes clusters across AWS Regions and accounts with EKS Dashboard

by Micah Walter on 21 MAY 2025 in [Amazon Elastic Kubernetes Service](https://aws.amazon.com/blogs/aws/category/compute/amazon-kubernetes-service/ "View all posts in Amazon Elastic Kubernetes Service"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/centralize-visibility-of-kubernetes-clusters-across-aws-regions-and-accounts-with-eks-dashboard/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/) [Dashboard](https://docs.aws.amazon.com/eks/latest/userguide/cluster-dashboard.html), a centralized display that enables cloud architects and cluster administrators to maintain organization-wide visibility across their Kubernetes clusters. With EKS Dashboard, customers can now monitor clusters deployed across different AWS Regions and accounts through a unified view, making it easier to track cluster inventory, assess compliance, and plan operational activities like version upgrades.

As organizations scale their Kubernetes deployments, they often run multiple clusters across different environments to enhance availability, ensure business continuity, or maintain data sovereignty. However, this distributed approach can make it challenging to maintain visibility and control, especially in decentralized setups spanning multiple Regions and accounts. Today, many customers resort to third-party tools for centralized cluster visibility, which adds complexity through identity and access setup, licensing costs, and maintenance overhead.

EKS Dashboard simplifies this experience by providing native dashboard capabilities within the [AWS Console](https://aws.amazon.com/console/). The Dashboard provides insights into 3 different resources including clusters, managed node groups, and EKS add-ons, offering aggregated insights into cluster distribution by Region, account, version, support status, forecasted extended support EKS control plane costs, and cluster health metrics. Customers can drill down into speciﬁc data points with automatic ﬁltering, enabling them to quickly identify and focus on clusters requiring attention.

**Setting up EKS Dashboard** You can access the Dashboard in EKS console through AWS Organizations’ [management](https://docs.aws.amazon.com/organizations/latest/userguide/orgs-manage_accounts_management.html) and [delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_delegated_admin.html) accounts. The setup process is straightforward and includes simply enabling trusted access as a one-time setup in the Amazon EKS console’s organizations settings page. Trusted access is available from the **Dashboard settings** page. Enabling trusted access will allow the management account to view the Dashboard. For more information on setup and configuration, see the official [AWS Documentation](https://docs.aws.amazon.com/eks/latest/userguide/cluster-dashboard.html).

![Screenshot of EKS Dashboard settings](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/21/eks-dashboard-settings-1-1024x728.png)

**A quick tour of EKS Dashboard**

The dashboard provides both graphical, tabular, and map views of your Kubernetes clusters, with advanced filtering, and search capabilities. You can also export data for further analysis or custom reporting.

![Screenshot of EKS Dashboard interface](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/19/eks-dashboard-01-1024x854.png)

EKS Dashboard overview with key info about your clusters.

![Screenshot of EKS Dashboard interface](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/19/eks-dashboard-02-1024x807.png)

There is a wide variety of available widgets to help visualize your clusters.

![Screenshot of EKS Dashboard interface](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/19/eks-dashboard-03-1024x743.png)

You can visualize your managed node groups by instance type distribution, launch templates, AMI versions, and more

![Screenshot of EKS Dashboard interface](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/19/eks-dashboard-04-1024x795.png)

There is even a map view where you can see all of your clusters across the globe.

**Beyond EKS clusters**

EKS Dashboard isn’t limited to just Amazon EKS clusters; it can also provide visibility into connected Kubernetes clusters running on-premises or on other cloud providers. While connected clusters may have limited data fidelity compared to native Amazon EKS clusters, this capability enables truly unified visibility for organizations running hybrid or multi-cloud environments.

**Available now**

Amazon EKS Dashboard is available today in the US East (N. Virginia) Region and is able to aggregate data from all commercial AWS Regions. There is no additional charge for using the EKS Dashboard. To learn more, visit the [Amazon EKS documentation](https://docs.aws.amazon.com/eks/latest/userguide/cluster-dashboard.html).

This new capability demonstrates our continued commitment to simplifying Kubernetes operations for our customers, enabling them to focus on building and scaling their applications rather than managing infrastructure. We’re excited to see how customers use EKS Dashboard to enhance their Kubernetes operations.

[— Micah;](https://linktr.ee/micahwalter)

![Micah Walter](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/03/05/micawal.jpg)

### Micah Walter

Micah Walter is a Sr. Solutions Architect supporting enterprise customers in the New York City region and beyond. He advises executives, engineers, and architects at every step along their journey to the cloud, with a deep focus on sustainability and practical design. In his free time, Micah enjoys the outdoors, photography, and chasing his kids around the house.

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