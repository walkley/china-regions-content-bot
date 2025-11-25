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

# Preventing unintended encryption of Amazon S3 objects

by Steve de Vera and Jennifer Paz on 15 JAN 2025 in [Advanced (300)](https://aws.amazon.com/blogs/security/category/learning-levels/advanced-300/ "View all posts in Advanced (300)"), [Best Practices](https://aws.amazon.com/blogs/security/category/post-types/best-practices/ "View all posts in Best Practices"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/security/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance") [Permalink](https://aws.amazon.com/blogs/security/preventing-unintended-encryption-of-amazon-s3-objects/)  [Comments](https://aws.amazon.com/blogs/security/preventing-unintended-encryption-of-amazon-s3-objects/#Comments)  Share

> **March 18, 2025:** This post was updated to include additional guidance around monitoring and detection.

> **January 17, 2025:** We updated this post to highlight the importance of using short-term credentials to mitigate the risk of unauthorized techniques such as the one detailed in this blog.

---

At [Amazon Web Services (AWS)](https://aws.amazon.com/), the security of our customers’ data is our top priority, and it always will be. Recently, the [AWS Customer Incident Response Team (CIRT)](https://aws.amazon.com/blogs/security/welcoming-the-aws-customer-incident-response-team/) and our automated security monitoring systems identified an increase in unusual encryption activity associated with [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) buckets.

It’s important to note that these actions do not take advantage of a vulnerability within an AWS service—but rather require valid credentials that an unauthorized user uses in an unintended way. Although these actions occur in the customer domain of the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), AWS recommends steps that customers can use to prevent or reduce the impact of such activity.

Working with customers, our security teams detected an increase of data encryption events in S3 that used an encryption method known as *server-side encryption using client-provided keys (SSE-C)*. While this is a feature used by many customers, we detected a pattern where a large number of S3 `CopyObject` operations using SSE-C began to overwrite objects, which has the effect of re-encrypting customer data with a new encryption key. Our analysis uncovered that this was being done by malicious actors who had obtained valid customer credentials, and were using them to re-encrypt objects.

Using [active defense tools](https://aws.amazon.com/blogs/security/how-aws-uses-active-defense-to-help-protect-customers-from-security-threats/), we have implemented automatic mitigations that will help prevent this type of unauthorized activity in many cases. These mitigations have already prevented a high percentage of attempts from succeeding, without our customers having to take steps to protect themselves. However, the threat actors used valid credentials, and it is difficult for AWS to reliably distinguish valid usage from malicious use. Therefore, we recommend that customers follow best practices to mitigate risk.

We recommend that customers implement these four security best practices to protect against the unauthorized use of SSE-C:

1. Implement short-term credentials
2. Implement data recovery procedures
3. Monitor AWS resources for unexpected access patterns
4. Block the use of SSE-C unless required by an application

## 1. Implement short-term credentials

While the above technique makes use of SSE-C encryption, the root cause of this and a large portion of security events is the compromise of long-term access keys. The most effective approach to mitigating the risk of compromised credentials is to never create long-term credentials in the first place. Credentials that do not exist cannot be exposed or stolen, and AWS provides a rich set of capabilities that alleviate the need to ever store credentials in source code or in configuration files.

[IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) enable applications to securely make signed API requests from [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) instances, [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/), or [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/) containers, or Lambda functions by using short-term credentials. Even systems outside the AWS Cloud can make authenticated calls without long-term AWS credentials by using the [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) feature. Additionally, [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) enables developer workstations to obtain short-term credentials backed by their longer-term user identities that are protected by multi-factor authentication (MFA).

These technologies rely on the [AWS Security Token Service (AWS STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) to issue temporary security credentials that can control access to AWS resources without distributing or embedding long-term AWS security credentials within an application, whether in code or in configuration files.

## 2. Implement data recovery procedures

Without data protection mechanisms in place, data recovery times can be longer. As a data protection best practice, we recommend that you protect against data being overwritten and that you maintain a second copy of critical data.

Enable [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) to keep multiple versions of an object in a bucket, so that you can restore objects that are accidentally deleted or overwritten. It is important to note that versioning may increase storage costs, especially for applications that frequently overwrite objects in a bucket. In this case, consider implementing [S3 Lifecycle policies](https://aws.amazon.com/blogs/storage/reduce-storage-costs-with-fewer-noncurrent-versions-using-amazon-s3-lifecycle/) to manage older versions and control storage costs.

Additionally, copy or take backups of critical data to a different bucket and perhaps to a different AWS account or AWS Region. To do this, you can use [S3 replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) to automatically copy objects between buckets. These buckets can reside in the same or in different AWS accounts, as well in the same or in different AWS Regions. S3 replication also offers an [SLA](https://aws.amazon.com/s3/sla-rtc/) for customers that have more stringent RPO (Recovery Point Objective) and RTO (Recovery Time Objective) requirements. Alternatively, you can use [AWS Backup for S3](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html), which is a managed service that automates periodic backup of S3 buckets.

## 3. Monitor AWS resources for unexpected access patterns

Without monitoring, unauthorized actions on S3 buckets may go unnoticed. We recommend that you use tools such as [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) or [S3 server access logs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html) to monitor access to your data.

You can use AWS CloudTrail to log events across AWS services (including Amazon S3) and even combine logs into a single account to make them available to your security teams to access and monitor. You can also create [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) based on [specific S3 metrics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metrics-dimensions.html#s3-request-cloudwatch-metrics) or logs to alert on unusual activity. These alerts can help you identify anomalous behavior quickly. You can also set up automation that uses [Amazon EventBridge](https://aws.amazon.com/eventbridge/) and [AWS Lambda](https://aws.amazon.com/lambda/) to automatically take corrective measures. You can find an example implementation of a setup used to scan all buckets across an organization and apply [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html).  This [blog post](https://aws.amazon.com/blogs/storage/auditing-amazon-s3-server-side-encryption-methods-for-object-uploads/) shows you how to audit encryption methods for object uploads in real time.

You can also baseline whether this technique is being used by inspecting CloudTrail for the `requestParameters.x-amz-server-side-encryption-customer-algorithm` value in the request parameters of logged S3 data events. If you want to see which buckets are currently using SSE-C encryption, this [re:Post](https://repost.aws/articles/ARhGC12rOiTBCKHcAe9GZXCA/how-to-detect-existing-use-of-sse-c-in-your-amazon-s3-buckets) article guides you through the configuration of S3 Inventory.

Another approach is to configure [Amazon GuardDuty](https://aws.amazon.com/guardduty/) and enable [S3 Protection with Extended Threat Detection](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-extended-threat-detection.html#extended-threat-detection-related-gdu-protection-plans). This allows GuardDuty to expand its threat detection scope and detect potential data exfiltration activities that may occur after S3 bucket access becomes more permissive. It also allows GuardDuty to detect potential ransomware attempts conducted with SSE-C encryption.

## 4. Block the use of SSE-C encryption

If your applications don’t use SSE-C as an encryption method, you can block the use of SSE-C with a resource policy applied to an S3 bucket, or by a resource control policy (RCP) applied to an organization in [AWS Organizations](https://aws.amazon.com/organizations/).

Resource policies for S3 buckets are commonly referred to as bucket policies and allow customers to specify permissions for individual buckets in S3. A bucket policy can be applied using the S3 `PutBucketPolicy` API operation, the AWS Command Line Interface (CLI), or through the AWS Management Console. Learn more about how bucket policies work in the [S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html). The following example shows a bucket policy that blocks SSE-C request for a bucket called `<your-bucket-name>`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RestrictSSECObjectUploads",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::<your-bucket-name>/*",
            "Condition": {
                "Null": {
                    "s3:x-amz-server-side-encryption-customer-algorithm": "false"
                }
            }
        }
    ]
 }
```

RCPs allow customers to specify the maximum available permissions that apply to resources across an entire organization in AWS Organizations. An RCP can be applied by using the AWS Organizations `UpdatePolicy` API operation, the AWS Command Line Interface (CLI), or through the AWS Management Console. Learn more about how RCPs work in the [AWS Organizations documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html). The following example shows an RCP that blocks SSE-C requests for buckets in the organization.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RestrictSSECObjectUploads",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "*",
      "Condition": {
        "Null": {
          "s3:x-amz-server-side-encryption-customer-algorithm": "false"
        }
      }
    }
  ]
 }
```

## Summary

The single most valuable thing you can do to protect yourself against common threats against your AWS environment is to eliminate or minimize the use of long-term credentials (access key/secret key). After that, work on reducing privileges for all principals to the minimum necessary (“least-privilege” analysis). Beyond that, for the particular threat pattern discussed in this blog, we have highlighted the most common indicators to look for. As your security teams work to constantly protect your environment, know that a number of teams at AWS—including the [AWS Customer Incident Response Team](https://aws.amazon.com/blogs/security/welcoming-the-aws-customer-incident-response-team/) (CIRT), Amazon Threat Intelligence, and services teams like the [Amazon S3](https://aws.amazon.com/s3/) team—are working diligently to innovate, collaborate, and share insights to help protect your valuable data.

In this post, we provided an update on this recent threat to customer data and highlighted four security best practices that customers can use to protect against the risk of bad actors using SSE-C to encrypt data by using lost or stolen AWS credentials.

As threat actor tactics evolve, our commitment to customer security remains unwavering. Together, we are building a more secure cloud environment, allowing you to innovate with confidence.

If you ever suspect unauthorized activity, please don’t hesitate to contact [AWS Support](https://aws.amazon.com/contact-us/) immediately.

![Steve de Vera](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2024/10/28/Steve-de-vera-author.jpg) Steve de Vera

Steve is a manager in the AWS Customer Incident Response Team (CIRT) with a focus on threat research and threat intelligence. He is passionate about American-style BBQ and is a certified competition BBQ judge. He has a dog named Brisket.

![Jennifer Paz](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/01/16/jennpaz.jpg) Jennifer Paz

Jennifer is a Security Engineer with over a decade of experience, currently serving on the AWS Customer Incident Response Team (CIRT). Jennifer enjoys helping customers tackle security challenges and implementing complex solutions to enhance their security posture. When not at work, Jennifer is an avid walker, jogger, pickleball enthusiast, traveler, and foodie, always on the hunt for new culinary adventures.

TAGS: [Incident response](https://aws.amazon.com/blogs/security/tag/incident-response/), [ransomware](https://aws.amazon.com/blogs/security/tag/ransomware/), [S3](https://aws.amazon.com/blogs/security/tag/s3/), [Security](https://aws.amazon.com/blogs/security/tag/security/), [Security Blog](https://aws.amazon.com/blogs/security/tag/security-blog/), [threat detection](https://aws.amazon.com/blogs/security/tag/threat-detection/)

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