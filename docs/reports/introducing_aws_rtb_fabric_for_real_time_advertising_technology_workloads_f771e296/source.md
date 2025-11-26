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

# Introducing AWS RTB Fabric for real-time advertising technology workloads

by Betty Zheng (郑予彬) on 23 OCT 2025 in [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Marketing & Advertising](https://aws.amazon.com/blogs/aws/category/industries/marketing-and-advertising/ "View all posts in Marketing & Advertising"), [Media & Entertainment](https://aws.amazon.com/blogs/aws/category/industries/entertainment/ "View all posts in Media & Entertainment"), [Networking & Content Delivery](https://aws.amazon.com/blogs/aws/category/networking-content-delivery/ "View all posts in Networking & Content Delivery") [Permalink](https://aws.amazon.com/blogs/aws/introducing-aws-rtb-fabric-for-real-time-advertising-technology-workloads/)  [Comments](https://aws.amazon.com/blogs/aws/introducing-aws-rtb-fabric-for-real-time-advertising-technology-workloads/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing AWS RTB Fabric, a fully managed service purpose built for real-time bidding (RTB) advertising workloads. The service helps advertising technology (AdTech) companies seamlessly connect with their supply and demand partners, such as [Amazon Ads](https://advertising.amazon.com/lp/build-your-business-with-amazon-advertising?tag=googhydr-20&ref=pd_sl_32yvxwiyd_e_ps_gg_b_au_en_d_core_e_646005230145&k_amazon%20ads&group_145097256426), [GumGum](https://gumgum.com/), [Kargo](https://www.kargo.com/), [MobileFuse](https://mobilefuse.com/), [Sovrn](https://www.sovrn.com/), [TripleLift](https://triplelift.com/), [Viant](https://www.viantinc.com/), [Yieldmo](https://yieldmo.com/) and more, to run high-volume, latency-sensitive RTB workloads on [Amazon Web Services (AWS)](https://aws.amazon.com/) with consistent single-digit millisecond performance and up to 80% lower networking costs compared to standard networking costs.

AWS RTB Fabric provides a dedicated, high-performance network environment for RTB workloads and partner integrations without requiring colocated, on-premises infrastructure or upfront commitments. The following diagram shows the high-level architecture of RTB Fabric.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/20/Screenshot-2025-10-20-at-14.05.49.png)

AWS RTB Fabric also includes modules, a capability that helps customers bring their own and partner applications securely into the compute environment used for real-time bidding. Modules support containerized applications and [foundation models (FMs)](https://aws.amazon.com/what-is/foundation-models/) that can enhance transaction efficiency and bidding effectiveness. At launch, AWS RTB Fabric includes modules for optimizing traffic management, improving bid efficiency, and increasing bid response rates, all running inline within the service for consistent low-latency execution.

The growth of programmatic advertising has created a need for low-latency, cost-efficient infrastructure to support RTB workloads. AdTech companies process millions of bid requests per second across publishers, supply-side platforms (SSPs), and demand-side platforms (DSPs). These workloads are highly sensitive to latency because most RTB auctions must complete within 200–300 milliseconds and require reliable, high-speed exchange of OpenRTB requests and responses among multiple partners. Many companies have addressed this by deploying infrastructure in colocation data centers near key partners, which reduces latency but adds operational complexity, long provisioning cycles, and high costs. Others have turned to cloud infrastructure to gain elasticity and scale, but they often face complex provisioning, partner-specific connectivity, and long-term commitments to achieve cost efficiency. These gaps add operational overhead and limit agility. AWS RTB Fabric solves these challenges by providing a managed private network built for RTB workloads that delivers consistent performance, simplifies partner onboarding, and achieves predictable cost efficiency without the burden of maintaining colocation or custom networking setups.

**Key capabilities**

AWS RTB Fabric introduces a managed foundation for running RTB workloads at scale. The service provides the following key capabilities:

* **Simplified connectivity to AdTech partners** – When you register an RTB Fabric gateway, the service automatically generates secure endpoints that can be shared with selected partners. Using the AWS RTB Fabric API, you can create optimized, private connections to exchange RTB traffic securely across different environments. External Links are also available to connect with partners who aren’t using RTB Fabric, such as those operating on premises or in third-party cloud environments. This approach shortens integration time and simplifies collaboration among AdTech participants.
* **Dedicated network for low-latency advertising transactions –** AWS RTB Fabric provides a managed, high-performance network layer optimized for OpenRTB communication. It connects AdTech participants such as SSPs, DSPs, and publishers through private, high-speed links that deliver consistent single-digit millisecond latency. The service automatically optimizes routing paths to maintain predictable performance and reduce networking costs, without requiring manual peering or configuration.
* **Pricing model aligned with RTB economics –** AWS RTB Fabric uses a transaction-based pricing model designed to align with programmatic advertising economics. Customers are billed per billion transactions, providing predictable infrastructure costs that align with how advertising exchanges, SSPs, and DSPs operate.
* **Built-in traffic management modules** – AWS RTB Fabric includes configurable modules that help AdTech workloads operate efficiently and reliably. Modules such as Rate Limiter, OpenRTB Filter, and Error Masking help you control request volume, validate message formats, and manage response handling directly in the network path. These modules execute inline within the AWS RTB Fabric environment, maintaining network-speed performance without adding application-level latency. All configurations are managed through the AWS RTB Fabric API, so you can define and update rules programmatically as your workloads scale.

**Getting started**

Today, you can start building with AWS RTB Fabric using the [AWS Management Console](https://aws.amazon.com/console/?nc2=type_a), [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/), or [infrastructure-as-code (IaC)](https://aws.amazon.com/what-is/iac/) tools such as [AWS CloudFormation](https://aws.amazon.com/cloudformation/?nc2=type_a) and [Terraform](https://docs.aws.amazon.com/prescriptive-guidance/latest/choose-iac-tool/terraform.html).

The console provides a visual entry point to view and manage RTB gateways and links, as shown on the **Dashboard** of the [AWS RTB Fabric console](https://console.aws.amazon.com/rtbfabric/home).

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/23/2025-rtb-fabric-dashboard.png)

You can also use the AWS CLI to configure gateways, create links, and manage traffic programmatically. When I started building with AWS RTB Fabric, I used the AWS CLI to configure everything from gateway creation to link setup and traffic monitoring. The setup ran inside my [Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/) endpoint while AWS managed the low-latency infrastructure that connected workloads.

To begin, I created a **requester gateway** to send bid requests and a **responder gateway** to receive and process bid responses. These gateways act as secure communication points within the AWS RTB Fabric.

```
# Create a requester gateway with required parameters
aws rtbfabric create-requester-gateway \
  --description "My RTB requester gateway" \
  --vpc-id vpc-12345678 \
  --subnet-ids subnet-abc12345 subnet-def67890 \
  --security-group-ids sg-12345678 \
  --client-token "unique-client-token-123"
```

```
# Create a responder gateway with required parameters
aws rtbfabric create-responder-gateway \
  --description "My RTB responder gateway" \
  --vpc-id vpc-01f345ad6524a6d7 \
  --subnet-ids subnet-abc12345 subnet-def67890 \
  --security-group-ids sg-12345678 \
  --dns-name responder.example.com \
  --port 443 \
  --protocol HTTPS
```

After both gateways were active, I created a link from the requester to the responder to establish a private, low-latency communication path for OpenRTB traffic. The link handled routing and load balancing automatically.

```
# Requester account creating a link from requester gateway to a responder gateway
aws rtbfabric create-link \
  --gateway-id rtb-gw-requester123 \
  --peer-gateway-id rtb-gw-responder456 \
  --log-settings '{"applicationLogs:{"sampling":"errorLog":10.0,"filterLog":10.0}}'
```

```
# Responder account accepting a link from requester gateway to responder gateway
aws rtbfabric accept-link \
  --gateway-id rtb-gw-responder456 \
  --link-id link-reqtoresplink789 \
  --log-settings '{"applicationLogs:{"sampling":"errorLog":10.0,"filterLog":10.0}}'
```

I also connected with external partners using **External Links**, which extended my RTB workloads to on-premises or third-party environments while maintaining the same latency and security characteristics.

```
# Create an inbound external link endpoint for an external partner to send bid requests to
aws rtbfabric create-inbound-external-link \
  --gateway-id rtb-gw-responder456
```

```
# Create an outbound external link for sending bid requests to an external partner
aws rtbfabric create-outbound-external-link \
  --gateway-id rtb-gw-requester123 \
  --public-endpoint "https://my-external-partner-responder.com"
```

To manage traffic efficiently, I added modules directly into the data path. The Rate Limiter module controlled request volume, and the OpenRTB Filter validated message formats inline at network speed.

```
# Attach a rate limiting module
aws rtbfabric update-link-module-flow \
  --gateway-id rtb-gw-responder456 \
  --link-id link-toresponder789 \
  --modules '{"name":"RateLimiter":"moduleParameters":{"rateLimiter":{"tps":10000}}}'
```

Finally, I used [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/?nc2=type_a) to monitor throughput, latency, and module performance, and I exported logs to [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) for auditing and optimization.

All configurations can also be automated with AWS CloudFormation or Terraform, allowing consistent, repeatable deployment across multiple environments. With RTB Fabric, I could focus on optimizing bidding logic while AWS maintained predictable, single-digit millisecond performance across my AdTech partners.

For more details, refer to the [AWS RTB Fabric User Guide](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/what-is-rtb-fabric.html).

**Now available**

AWS RTB Fabric is available today in the following [AWS Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region): US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Tokyo), Europe (Frankfurt), and Europe (Ireland).

AWS RTB Fabric is continually evolving to address the changing needs of the AdTech industry. The service expands its capabilities to support secure integration of advanced applications and AI-driven optimizations in real-time bidding workflows that help customers simplify operations and improve performance on AWS. To learn more about AWS RTB Fabric, visit the [AWS RTB Fabric page](http://aws.amazon.com/rtb-fabric).

– [Betty](https://www.linkedin.com/in/zhengyubin714/)

![Betty Zheng (郑予彬)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2024/06/12/形象照-betty-0181-scaled-e1718178653724.jpg)

### Betty Zheng (郑予彬)

Betty Zheng is a Senior Developer Advocate at AWS, focusing on developer-centric content across Cloud Native, Cloud Security, and Generative AI technologies. With over 20 years of experience in the ICT industry and 18 years as an application architect and cloud infrastructure expert, she actively engages with the Chinese developer community, helping developers understand AWS technologies and transform their ideas into execution.

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