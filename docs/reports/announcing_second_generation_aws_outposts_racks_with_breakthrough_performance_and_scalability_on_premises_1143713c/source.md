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

# Announcing second-generation AWS Outposts racks with breakthrough performance and scalability on-premises

by Micah Walter on 29 APR 2025 in [Amazon EC2](https://aws.amazon.com/blogs/aws/category/compute/amazon-ec2/ "View all posts in Amazon EC2"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS Outposts](https://aws.amazon.com/blogs/aws/category/compute/aws-outposts/ "View all posts in AWS Outposts"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/announcing-second-generation-aws-outposts-racks-with-breakthrough-performance-and-scalability-on-premises/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today we’re announcing the general availability of second-generation [AWS Outposts racks](https://aws.amazon.com/outposts/rack/), which marks the latest innovation from AWS for edge computing. This new generation includes support for the latest x86-powered [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2) (Amazon EC2) instances, new simplified network scaling and configuration, and accelerated networking instances designed specifically for ultra-low latency and high-throughput workloads. These enhancements deliver greater performance for a broad range of on-premises workloads, such as core trading systems of financial services and telecom 5G Core workloads.

Customers like athenahealth, FanDuel, First Abu Dhabi Bank, Mercado Libre, Liberty Latin America, Riot Games, Vector Limited, and Wiwynn are already using Outposts racks for workloads that need to stay on-premises. The second-generation Outposts rack can provide low latency, local data processing, or data residency needs, such as game servers for multi-player online games, customer transaction data, medical records, industrial and manufacturing control systems, telecom Business Support Systems (BSS), and edge inference of a variety of machine learning (ML) models. Customers can now take advantage of the latest generation of processors and more advanced configurations of Outposts racks to support faster processing, higher memory capacity, and increased network bandwidth.

**Latest generation EC2 instances**

We’re excited to announce local support for the latest generation (7th generation) of x86-powered Amazon EC2 instances on AWS Outposts racks, starting with C7i compute-optimized instances, M7i general-purpose instances, and R7i memory-optimized instances. These new instances deliver twice the vCPU, memory, and network bandwidth while providing up to 40% better performance compared to C5, M5, and R5 instances on previous generation Outposts racks.

They are powered by 4th Gen Intel Xeon Scalable processors and are ideal for a broad range of on-premises workloads requiring enhanced performance such as larger databases, more memory-intensive applications, advanced real-time big data analytics, high-performance video encoding and streaming, and CPU-based edge inference with more sophisticated ML models. Support for more latest generation EC2 instances, including GPU-enabled instances, is coming soon.

This [video](https://www.youtube.com/watch?v=Mu231AhT1AE) walks you through the major advancements in the new AWS Outposts racks.

**Simplified network scaling and configuration**

![Image of an AWS Outposts rack device](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/25/LUR04269-200x300.jpg)We’ve completely reimagined networking in our latest Outposts generation, making it simpler and more scalable than ever. At the heart of this upgrade is our new Outposts network rack, which acts as a central hub for all your compute and storage traffic.

This new design brings three major benefits to the table.

First, you can now scale your compute resources independently from your networking infrastructure, giving you more flexibility and cost efficiency as your workloads grow. Second, we’ve built in network resilience from the ground up, with the network rack automatically handling device failures to keep your systems running smoothly. Third, connecting to your on-premises environment and AWS Regions is now a breeze – you can configure everything from IP addresses to VLAN and BGP settings through straightforward APIs or our updated console interface.

**Specialized Amazon EC2 instances with accelerated networking**

We’re introducing a new category of specialized Amazon EC2 instances on Outposts racks with accelerated networking. These instances are purpose built for the most latency-sensitive, compute-intensive, and throughput-intensive mission-critical workloads on-premises. To deliver the best possible performance, in addition to the Outpost logical network, these instances feature a secondary physical network with network accelerator cards connected to top-of-rack (TOR) switches.

First in this category are **bmn-sf2e** instances, designed for ultra-low latency with deterministic performance. The new instances run on Intel’s latest Sapphire Rapids processors (4th Gen Xeon Scalable), delivering 3.9 GHz sustained performance across all cores with generous memory allocation – 8GB of RAM for every CPU core. We’ve equipped **bmn-sf2e** instances with AMD Solarflare X2522 network cards that connect directly to top-of-rack switches.

For financial services customers, especially capital market firms, these instances offer deterministic networking through native Layer 2 (L2) multicast, precision time protocol (PTP), and equal cable lengths. This enables customers to meet regulatory requirements around fair trading and equal access while easily connecting to their existing trading infrastructure.

| Instance Name | vCPUs | Memory (DDR5) | Network Bandwidth | NVMe SSD Storage | Accelerated Network Cards | Accelerated Bandwidth (Gbps) |
| --- | --- | --- | --- | --- | --- | --- |
| **bmn-sf2e.metal-16xl** | 64 | 512 GiB | 25 Gbps | 2 x 8 TB (16 TB) | 2 | 100 |
| **bmn-sf2e.metal-32xl** | 128 | 1024 GiB | 50 Gbps | 4 x 8 TB (32 TB) | 4 | 200 |

The second instance type, **bmn-cx2**, is optimized for high throughput and low latency. This instance features NVIDIA ConnectX-7 400G NICs physically connected to high-speed top-of-rack switches, delivering up to 800 Gbps bare metal network bandwidth operating at near line rate. With native Layer 2 (L2) multicast and hardware PTP support, this instance is ideal for high-throughput workloads like real-time market data distribution, risk analytics, and telecom 5G core network applications.

| Instance Name | vCPUs | Memory (DDR5) | Network Bandwidth | NVMe SSD Storage | Accelerated Network Cards | Accelerated Bandwidth (Gbps) |
| --- | --- | --- | --- | --- | --- | --- |
| **bmn-cx2.metal-48xl** | 192 | 1024 GiB | 50 Gbps | 4 x 4 TB (16 TB) | 2 | 800 |

Bottom line, the new generation of Outposts racks deliver enhanced performance, scalability, and resiliency for a broad range of on-premises workloads, even for mission-critical workloads with the most stringent latency and throughput requirements. You can make your selection and initiate your order from the [AWS Management Console](https://aws.amazon.com/console/). The new instances maintain consistency with regional deployments by supporting the same APIs, AWS Management Console, automation, governance policies, and security controls in the cloud and on-premises, improving developer productivity and IT efficiency.

**Things to know**

At launch, second-generation Outposts racks can be shipped to US and Canada and be parented back to 6 AWS Regions including US East (N. Virginia and Ohio), US West (Oregon), EU West (London and France) and Asia Pacific (Singapore). Support for more countries and territories and AWS Regions is coming soon. At launch, second-generation Outposts racks locally support a subset of AWS services found in previous generation Outposts racks. Support for more EC2 instance types and more AWS services is coming soon.

To learn more, visit the [AWS Outposts racks](https://aws.amazon.com/outposts/rack/) product page and [user guide](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html). You can also talk to an [Outposts expert](https://pages.awscloud.com/GLOBAL_PM_LN_outposts-features_2020084_7010z000001Lpcl_01.LandingPage.html) if you are ready to discuss your on-premises needs.

[— Micah;](https://linktr.ee/micahwalter)

*5/1/2025: Memory (DDR5) capacity updated in table for 48xl instance.*

---

How is the News Blog doing? Take this [1 minute survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi)!

*(This [survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi) is hosted by an external company. AWS handles your information as described in the [AWS Privacy Notice](https://aws.amazon.com/privacy/?trk=4b29643c-e00f-4ab6-ab9c-b1fb47aa1708&sc_channel=blog). AWS will own the data gathered via this survey and will not share the information collected with survey respondents.)*

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