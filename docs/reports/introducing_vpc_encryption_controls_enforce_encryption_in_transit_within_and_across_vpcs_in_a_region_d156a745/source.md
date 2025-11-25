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

# Introducing VPC encryption controls: Enforce encryption in transit within and across VPCs in a Region

by [Sébastien Stormacq](https://aws.amazon.com/blogs/aws/author/stormacq/ "Posts by Sébastien Stormacq") on 21 NOV 2025 in [Amazon VPC](https://aws.amazon.com/blogs/aws/category/compute/amazon-vpc/ "View all posts in Amazon VPC"), [Amazon VPC](https://aws.amazon.com/blogs/aws/category/networking-content-delivery/amazon-vpc-networking-content-delivery/ "View all posts in Amazon VPC"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/introducing-vpc-encryption-controls-enforce-encryption-in-transit-within-and-across-vpcs-in-a-region/)  [Comments](https://aws.amazon.com/blogs/aws/introducing-vpc-encryption-controls-enforce-encryption-in-transit-within-and-across-vpcs-in-a-region/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing virtual private cloud (VPC) encryption controls, a new capability of [Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/) that helps you audit and enforce encryption in transit for all traffic within and across VPCs in a Region.

Organizations across financial services, healthcare, government, and retail face significant operational complexity in maintaining encryption compliance across their cloud infrastructure. Traditional approaches require piecing together multiple solutions and managing complex public key infrastructure (PKI), while manually tracking encryption across different network paths using spreadsheets—a process prone to human error that becomes increasingly challenging as infrastructure scales.

Although [AWS Nitro](https://aws.amazon.com/ec2/nitro/) based instances automatically encrypt traffic at the hardware layer without affecting performance, organizations need simple mechanisms to extend these capabilities across their entire VPC infrastructure. This is particularly important for demonstrating compliance with regulatory frameworks such as Health Insurance Portability and Accountability (HIPAA), Payment Card Industry Data Security Standard (PCI DSS), and Federal Risk and Authorization Management Program (FedRAMP), which require proof of end-to-end encryption across environments. Organizations need centralized visibility and control over their encryption status, without having to manage performance trade-offs or complex key management systems.

VPC encryption controls address these challenges by providing two operational modes: monitor and enforce. In monitor mode, you can audit the encryption status of your traffic flows and identify resources that allow plaintext traffic. The feature adds a new encryption-status field to VPC flow logs, giving you visibility into whether traffic is encrypted using Nitro hardware encryption, application-layer encryption (TLS), or both.

After you’ve identified resources that need modification, you can take steps to implement encryption. AWS services, such as [Network Load Balancer](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/), [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), and [AWS Fargate](https://aws.amazon.com/fargate/) tasks, will automatically and transparently migrate your underlying infrastructure to Nitro hardware without any action required from you and with no service interruption. For other resources, such as the previous generation of [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) instances, you will need to switch to [modern Nitro based](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) [instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit) or configure TLS encryption at application level.

You can switch to enforce mode after all resources have been migrated to encryption-compliant infrastructure. This migration to encryption-compliant hardware and communication protocols is a prerequisite for enabling enforce mode. You can configure specific exclusions for resources such as [internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) or [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html), that don’t support encryption (because the traffic flows outside of the AWS network).

Other [resources](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) must be encryption-compliant and can’t be excluded. After activation, enforce mode provides that all future resources are only created on compatible Nitro instances, and unencrypted traffic is dropped when incorrect protocols or ports are detected.

**Let me show you how to get started**

For this demo, I started three EC2 instances. I use one as a web server with Nginx installed on port 80, serving a clear text HTML page. The other two are continuously making HTTP GET requests to the server. This generates clear text traffic in my VPC. I use the `m7g.medium` instance type for the web server and one of the two clients. This instance type uses the underlying Nitro System hardware to automatically encrypt in-transit traffic between instances. I use a `t4g.medium` instance for the other web client. The network traffic of that instance is not encrypted at the hardware level.

To get started, I enable encryption controls in monitor mode. In the [AWS Management Console](https://console.aws.amazon.com), I select **Your VPCs** in the left navigation pane, then I switch to the **VPC encryption controls** tab. I choose **Create encryption control** and select the VPC I want to create the control for.

Each VPC can have only one VPC encryption control associated with it, creating a one-to-one relationship between the VPC ID and the VPC encryption control Id. When creating VPC encryption controls, you can add tags to help with resource organization and management. You can also activate VPC encryption control when you create a new VPC.

[![VPC Encryption Control - create EC 1](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/17/2025-10-17_14-40-56-1024x419.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/17/2025-10-17_14-40-56.png)

I enter a **Name** for this control. I select the **VPC** I want to control. For existing VPCs, I have to start in **Monitor mode,** and I can turn on **Enforce mode** when I’m sure there is no unencrypted traffic. For new VPCs, I can enforce encryption at the time of creation.

Optionally, I can define tags when creating encryption controls for an existing VPC. However, when enabling encryption controls during VPC creation, separate tags can’t be created for VPC encryption controls—because they automatically inherit the same tags as the VPC. When I’m ready, I choose **Create encryption control.**

[![VPC Encryption Control - create EC 2](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/17/2025-10-17_14-41-16-1024x625.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/17/2025-10-17_14-41-16.png)Alternatively, I can use the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/):

```
aws ec2 create-vpc-encryption-control --vpc-id vpc-123456789
```

Next, I audit the encryption status of my VPC using the console, command line, or flow logs:

```
aws ec2 create-flow-logs \
  --resource-type VPC \
  --resource-ids vpc-123456789 \
  --traffic-type ALL \
  --log-destination-type s3 \
  --log-destination arn:aws:s3:::vpc-flow-logs-012345678901/vpc-flow-logs/ \
  --log-format '${flow-direction} ${traffic-path} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${encryption-status}'
{
    "ClientToken": "F7xmLqTHgt9krTcFMBHrwHmAZHByyDXmA1J94PsxWiU=",
    "FlowLogIds": [
        "fl-0667848f2d19786ca"
    ],
    "Unsuccessful": []
}
```

After a few minutes, I see this traffic in my logs:

```
flow-direction traffic-path srcaddr dstaddr srcport dstport encryption-status
ingress - 10.0.133.8 10.0.128.55 43236 80 1 # <-- HTTP between web client and server. Encrypted at hardware-level
egress 1 10.0.128.55 10.0.133.8 80 43236 1
ingress - 10.0.133.8 10.0.128.55 36902 80 1
egress 1 10.0.128.55 10.0.133.8 80 36902 1
ingress - 10.0.130.104 10.0.128.55 55016 80 0 # <-- HTTP between web client and server. Not encrypted at hardware-level
egress 1 10.0.128.55 10.0.130.104 80 55016 0
ingress - 10.0.130.104 10.0.128.55 60276 80 0
egress 1 10.0.128.55 10.0.130.104 80 60276 0
```

* `10.0.128.55` is the web server with hardware-encrypted traffic, serving clear text traffic at application level.
* `10.0.133.8` is the web client with hardware-encrypted traffic.
* `10.0.130.104` is the web client with no encryption at the hardware level.

The `encryption-status` field tells me the status of the encryption for the traffic between the source and destination address:

* 0 means the traffic is in clear text
* 1 means the traffic is encrypted at the network layer (Level 3) by the Nitro system
* 2 means the traffic is encrypted at the application layer (Level7, TCP Port 443 and TLS/SSL)
* 3 means the traffic is encrypted both at the application layer (TLS) and the network layer (Nitro)
* “-” means VPC encryption controls are not enabled, or AWS Flow Logs don’t have the status information.

The traffic originating from the web client on the instance that isn’t Nitro based (`10.0.130.104`), is flagged as `0`. The traffic initiated from the web client on the Nitro- ased instance (`10.0.133.8`) is flagged as `1`.

I also use the console to identify resources that need modification. It reports two nonencrypted resources: the internet gateway and the [elastic network interface (ENI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) of the instance that isn’t based on Nitro.

[![VPC Encryption Control - list of exclusions](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/07/2025-11-07_21-53-27-1024x327.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/07/2025-11-07_21-53-27.png)I can also check for nonencrypted resources using the CLI:

```
aws ec2 get-vpc-resources-blocking-encryption-enforcement --vpc-id vpc-123456789
```

After updating my resources to support encryption, I can use the console or the CLI to switch to enforce mode.

In the console, I select the VPC encryption control. Then, I select **Actions** and **Switch mode**.

[![VPC Encryption Control - switch mode](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/07/2025-11-07_22-01-13-1024x481.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/07/2025-11-07_22-01-13.png)Or the equivalent CLI:

```
aws ec2 modify-vpc-encryption-control --vpc-id vpc-123456789 --mode enforce
```

**How to modify the resources that are identified as nonencrypted?**

All your VPC resources must support traffic encryption, either at the hardware layer or at the application layer. For most resources, you don’t need to take any action.

AWS services accessed through [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) and [gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html) automatically enforce encryption at the application layer. These services only accept TLS-encrypted traffic. AWS will automatically drop any traffic that isn’t encrypted at the application layer.

When you enable monitor mode, we automatically and gradually migrate your Network Load Balancers, Application Load Balancers, [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) clusters, and [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/) clusters to hardware that inherently supports encryption. This migration happens transparently without any action required from you.

Some VPC resources require you to select the underlying instances that support modern Nitro hardware-layer encryption. These include EC2 Instances, [Auto Scaling groups,](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html) [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) databases (including [Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html)), [Amazon ElastiCache node-based clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/designing-elasticache-cluster.html), [Amazon Redshift provisioned clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html), [EKS clusters](https://docs.aws.amazon.com/eks/latest/userguide/clusters.html), [ECS with EC2 capacity](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch-type-ec2.html), [MSK Provisioned](https://docs.aws.amazon.com/msk/latest/developerguide/msk-provisioned.html), [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-comparison.html), and [Amazon EMR](https://aws.amazon.com/emr). To migrate your Redshift clusters, you must create a new cluster or namespace from a snapshot.

If you use newer-generation instances, you likely already have encryption-compliant infrastructure because all recent instance types support encryption. For older-generation instances that don’t support encryption-in transit, you’ll need to upgrade to supported instance types.

**Things to know when using AWS Transit Gateway**

When your VPCs with encryption controls enabled are connected via a [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html), you’ll need to manually activate encryption controls on the Transit Gateway to encrypt traffic between the VPCs. This can be done using the AWS console, the `modify-transit-gateway` command or API. Enabling encryption on an existing Transit Gateway won’t disrupt the traffic flowing between VPCs attached to the Transit Gateway.

When a Transit Gateway and its attached VPCs have encryption controls in enforce mode (with no exclusions), traffic is encrypted end-to-end.

When creating a [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) through [AWS CloudFormation](https://aws.amazon.com/cloudformation/) with encryption support enabled, you need one additional [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) permission: `ec2:ModifyTransitGateway`. This permission is required because CloudFormation uses a two-step process to create a Transit Gateway. It first creates the Transit Gateway with basic configuration, then calls `ModifyTransitGateway` to enable encryption support. Without this permission, your CloudFormation stack will fail during creation when attempting to apply the encryption configuration, even if you’re only performing what appears to be a create operation.

**Pricing and availability**

You can start using VPC encryption controls today in these AWS Regions: US East (Ohio, N. Virginia), US West (N. California, Oregon), Africa (Cape Town), Asia Pacific (Hong Kong, Hyderabad, Jakarta, Melbourne, Mumbai, Osaka, Singapore, Sydney, Tokyo), Canada (Central), Canada West (Calgary), Europe (Frankfurt, Ireland, London, Milan, Paris, Stockholm, Zurich), Middle East (Bahrain, UAE), and South America (São Paulo).

VPC encryption controls is free of cost until March 1, 2026. The [VPC pricing page](https://aws.amazon.com/vpc/pricing/) will be updated with details as we get closer to that date.

To learn more, visit the [VPC encryption controls documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) or try it out in your AWS account. I look forward to hearing how you use this feature to strengthen your security posture and help you meet compliance standards.

[— seb](https://linktr.ee/sebsto)

![Sébastien Stormacq](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2023/01/13/AWS-59-cropped.jpg)

### [Sébastien Stormacq](https://aws.amazon.com/blogs/aws/author/stormacq/ "Posts by Sébastien Stormacq")

Seb has been writing code since he first touched a Commodore 64 in the mid-eighties. He inspires builders to unlock the value of the AWS cloud, using his secret blend of passion, enthusiasm, customer advocacy, curiosity and creativity. His interests are software architecture, developer tools and mobile computing. If you want to sell him something, be sure it has an API. Follow @sebsto on Bluesky, X, Mastodon, and others.

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