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

# Amazon Elastic Kubernetes Service gets independent affirmation of its zero operator access design

by Manuel Mazarredo, Tariro Dongo, Lukonde Mwila, and Micah Hausler on 12 NOV 2025 in [Amazon Elastic Kubernetes Service](https://aws.amazon.com/blogs/security/category/compute/amazon-kubernetes-service/ "View all posts in Amazon Elastic Kubernetes Service"), [Announcements](https://aws.amazon.com/blogs/security/category/post-types/announcements/ "View all posts in Announcements"), [Containers](https://aws.amazon.com/blogs/security/category/containers/ "View all posts in Containers"), [Foundational (100)](https://aws.amazon.com/blogs/security/category/learning-levels/foundational-100/ "View all posts in Foundational (100)"), [Security](https://aws.amazon.com/blogs/security/category/security-identity-compliance/security/ "View all posts in Security"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/security/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance") [Permalink](https://aws.amazon.com/blogs/security/amazon-elastic-kubernetes-service-gets-independent-affirmation-of-its-zero-operator-access-design/)  [Comments](https://aws.amazon.com/blogs/security/amazon-elastic-kubernetes-service-gets-independent-affirmation-of-its-zero-operator-access-design/#Comments)  Share

Today, we’re excited to announce the independent affirmation of our [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) zero operator access posture.

Because [security is our top priority](https://aws.amazon.com/security/culture-of-security/) at [Amazon Web Services (AWS)](https://aws.amazon.com/), we designed an operational architecture to meet the data privacy posture our regulated and most stringent customers want in a managed Kubernetes service, giving them continued confidence to run their most critical and data-sensitive workloads on AWS services. Our services are designed to prevent AWS personnel from having technical pathways to read, copy, extract, modify, or otherwise access customer content in the management of Amazon EKS.

At AWS, earning trust isn’t only a goal, it’s one of the core [Leadership Principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles) that guides every decision we make. Customers choose AWS because they trust us to provide the most secure global cloud infrastructure on which to build, migrate, and run their workloads, and to store their data. To build on this trust, we launched the [AWS Trust Center](https://aws.amazon.com/trust-center/) to make information about how we secure our customers’ assets in the AWS Cloud more accessible. Along with this launch, we’re describing how we approach [operator access](https://aws.amazon.com/trust-center/operator-access/) to demonstrate an industry leading data privacy posture, and how we fulfill our part of the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) in the AWS Cloud.

Many of the AWS core systems and services are designed with zero operator access, meaning they operate based on an architecture and model that, at the minimum, prevents any form of access to customer content in the management of the service. Instead, their systems and services are administered through automation and secure APIs that protect customer content from inadvertent or even coerced disclosure. Some of these services are [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/), [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2) (through the [AWS Nitro System](https://aws.amazon.com/ec2/nitro/)), [AWS Lambda](https://aws.amazon.com/lambda/), [Amazon EKS](https://aws.amazon.com/eks/), and [AWS Wickr.](https://aws.amazon.com/wickr/)

When AWS made its [Digital Sovereignty Pledge](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/), we committed to providing greater transparency and assurance to customers about how AWS services are designed and operated, especially when it comes to handling customer content. As part of that increased transparency, we engaged NCC Group, a leading cybersecurity consulting firm based in the United Kingdom, to conduct an independent architecture review of Amazon EKS, and the security assurances we provide to our customers. NCC Group has now issued its report and affirmed our claims. The report states:

> “NCC Group found no architectural gaps that would directly compromise the security claims asserted by AWS.”

Specifically, the report validates the following statements about the Amazon EKS security posture:

* There are no technical means for AWS personnel to gain interactive access to a managed Kubernetes control plane instance.
* There are no technical means available to AWS personnel to read, copy, extract, modify, or otherwise access customer content in a managed Kubernetes control plane instance.
* Internal administrative APIs used by AWS personnel to manage the Kubernetes control plane instances cannot access customer content in the Kubernetes data plane.
* Changes to internal administrative APIs used to manage the Kubernetes control plane always requires multi-party review and approval.
* There are no technical means available to AWS personnel to access customer content in backup storage for the *etcd* database. No AWS personnel can access any plaintext encryption keys used for securing data in the *etcd* database.
* AWS personnel can only interact with the Kubernetes cluster API endpoint using internal administrative APIs without access to customer content in the managed Kubernetes control plane or the Kubernetes data plane. All actions performed on the Kubernetes cluster API endpoint by AWS personnel are visible to customers through customer enabled audit logs.
* Access to internal administrative APIs always requires authentication and authorization. All operational actions performed by internal administrative APIs are logged and audited.
* A managed Kubernetes control plane instance can only run tested software that has been deployed by a trusted pipeline. No AWS personnel can deploy software to a managed Kubernetes control plane instance outside of this pipeline.

The detailed NCC Group report examines each of these claims, including the scope, methodology, and steps that NCC Group used to evaluate the claims.

## How Amazon EKS is designed for zero operator access

AWS has always used a least privilege model to minimize the number of humans that have access to systems processing [customer content](https://aws.amazon.com/compliance/data-privacy-faq/#topic-0). This means that we design our products and services to provide each Amazonian access to only the minimum set of systems required to do their assigned task or responsibility and limit that access to when it’s needed. Any access to systems that store or process customer data is logged, monitored for anomalies, and audited. AWS designs all of its systems to prevent access by AWS personnel to customer content for unauthorized purposes. We commit to that in our [AWS Customer Agreement](https://aws.amazon.com/agreement/) and [AWS Service Terms](https://aws.amazon.com/service-terms/). AWS operations never require us to access, copy, or move a customer’s content without that customer’s knowledge and authorization.

Our operational architecture includes the exclusive use of [AWS Nitro System](https://aws.amazon.com/ec2/nitro/)-based instances to provide a confidential compute baseline for the managed Kubernetes control plane.

We use a set of restricted administrative APIs to enable precise control of access so our operators can conduct precise, allow-listed actions for troubleshooting and diagnostics without requiring direct or interactive access to the Kubernetes control plane instances. These APIs have been purposefully engineered without technical means to access customer content in the Kubernetes control plane or the customer’s Kubernetes data plane.

Following our standard change management mechanisms, we enforce a built-in, multi-party review and approval process for modifications to these restricted administrative APIs, and the accompanied policies that further strengthen the guardrails of how we operate the service. This model is implemented consistently across Amazon EKS clusters, regardless of the customer’s chosen launch mode for the Kubernetes data plane.

Additionally, every interaction with these restricted administrative APIs generates logs, with mandatory authentication and authorization, following the least privilege principle. By enabling their cluster’s audit logs, customers can maintain visibility into all actions performed by AWS personnel on the cluster’s API endpoint.

By default, we [envelope encrypt all Kubernetes API data](https://docs.aws.amazon.com/eks/latest/userguide/envelope-encryption.html) before it is stored at rest in the [etcd](https://etcd.io/)database, and further secure backup storage of the *etcd* databaseto add multi-layered protection to prevent access to customer content in cluster snapshots. Furthermore, our system is designed so that no AWS personnel can access any of the plaintext encryption keys used to secure data in the *etcd* database and its backups.

These operator access controls apply uniformly to the Amazon EKS control plane, regardless of how you run your worker nodes—whether self-managed, through [Amazon EKS Auto Mode](https://aws.amazon.com/eks/auto-mode/), or with [AWS Fargate](https://aws.amazon.com/fargate/). As stated in the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/), customers remain responsible for securing the configurations of the Kubernetes worker nodes, with the exception of Amazon EKS Auto Mode and Fargate launch modes. For more information about the security of these AWS managed data plane launch modes in Amazon EKS, see the relevant links in the [Learn more](#LearnMore) section.

## Conclusion

Amazon EKS is designed and built to make sure that no AWS employee can read, copy, modify, or otherwise access customer content in Amazon EKS. By using AWS Nitro System‑based confidential compute, tightly‑scoped administrative APIs, multi‑party change‑approval processes, and end‑to‑end encryption, AWS avoids technical pathways for operator access. Independent validation from the NCC Group found no architectural gaps that would undermine these guarantees. In short, Amazon EKS delivers a zero operator access model that can meet the strictest regulatory and sovereignty requirements, giving organizations the confidence to run their most sensitive, mission‑critical workloads on AWS.

## Learn more

* [NCC Group report](https://www.nccgroup.com/research-blog/public-report-aws-eks-security-claims/)
* [Amazon EKS documentation](https://aws.amazon.com/eks/)
* [Security Overview of Amazon EKS Auto Mode](https://d1.awsstatic.com/whitepapers/compliance/Security_Overview_of_Amazon_EKS_Auto_Mode.pdf)
* [Security Overview of AWS Fargate](https://d1.awsstatic.com/whitepapers/AWS_Fargate_Security_Overview_Whitepaper.pdf)
* [AWS Digital Sovereignty Pledge](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/)
* [AWS continuous delivery practices and safe pipelines automation](https://aws.amazon.com/builders-library/cicd-pipeline/)

If you have feedback about this post, submit comments in the **Comments** section below. If you have questions about this post, [contact AWS Support](https://console.aws.amazon.com/support/home).

![Micah Hausler](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/10/Micah-Hausler.jpeg)

### Micah Hausler

Micah is a Principal Software Engineer at AWS and focuses on Kubernetes and container security.

![Lukonde Mwila](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/10/Lukonde-Mwila.jpg)

### Lukonde Mwila

Lukonde is a Senior Product Manager at AWS in the Amazon EKS team, focusing on networking, resiliency, and operational security. He has years of experience in application development, solution architecture, cloud engineering, and DevOps workflows.

![Manuel Mazarredo](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2022/08/16/mazaredo.jpg)

### Manu Mazarredo

Manu is a program manager at AWS based in Amsterdam, the Netherlands. Manu leads compliance and security assurance audits and engagements across AWS Regions and industries. For the past 20 years, he has worked in information systems audits, ethical hacking, project management, quality assurance, and vendor management

![Tari Dongo](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/10/dongot.jpg)

### Tari Dongo

Tari is a Security Assurance Program Manager at AWS, based in London. Tari is responsible for third-party and customer audits, attestations, certifications, and assessments across EMEA. Previously, Tari worked in Security Assurance and Technology Risk in the big four and financial services industry.

TAGS: [Amazon EKS](https://aws.amazon.com/blogs/security/tag/amazon-eks/), [Containers](https://aws.amazon.com/blogs/security/tag/containers/), [Security Blog](https://aws.amazon.com/blogs/security/tag/security-blog/)

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