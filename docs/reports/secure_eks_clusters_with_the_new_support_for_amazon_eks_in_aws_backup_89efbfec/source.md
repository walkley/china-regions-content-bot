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

# Secure EKS clusters with the new support for Amazon EKS in AWS Backup

by Veliswa Boya on 10 NOV 2025 in [Amazon Elastic Kubernetes Service](https://aws.amazon.com/blogs/aws/category/compute/amazon-kubernetes-service/ "View all posts in Amazon Elastic Kubernetes Service"), [AWS Backup](https://aws.amazon.com/blogs/aws/category/storage/aws-backup/ "View all posts in AWS Backup"), [Compute](https://aws.amazon.com/blogs/aws/category/compute/ "View all posts in Compute"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Storage](https://aws.amazon.com/blogs/aws/category/storage/ "View all posts in Storage") [Permalink](https://aws.amazon.com/blogs/aws/secure-eks-clusters-with-the-new-support-for-amazon-eks-in-aws-backup/)  [Comments](https://aws.amazon.com/blogs/aws/secure-eks-clusters-with-the-new-support-for-amazon-eks-in-aws-backup/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing [support for Amazon EKS in AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources-console.html?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) to provide the capability to secure Kubernetes applications using the same centralized platform you trust for your other [Amazon Web Services (AWS)](https://aws.amazon.com/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) services. This integration eliminates the complexity of protecting containerized applications while providing enterprise-grade backup capabilities for both cluster configurations and application data. [AWS Backup](https://aws.amazon.com/backup/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) is a fully managed service to centralize and automate data protection across AWS and on-premises workloads. [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/pm/eks/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) is a fully managed Kubernetes service to manage availability and scalability of the Kubernetes clusters. With this new capability, you can centrally manage and automate data protection across your Amazon EKS environments alongside other AWS services.

Until now, for backups, customers relied on custom solutions or third-party tools to back up their EKS clusters, requiring complex scripting and maintenance for each cluster. The support for Amazon EKS in AWS Backup eliminates this overhead by providing a single, centralized, and policy-driven solution that protects both EKS clusters (Kubernetes deployments and resources) and stateful data (stored in [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el), [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el), and [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/pm/serv-s3/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) only) without the need to manage custom scripts across clusters. For restores, customers were previously required to restore their EKS backups to a target EKS cluster which was either the source EKS cluster, or a new EKS cluster, requiring that an EKS cluster infrastructure is provisioned ahead of time prior to the restore. With this new capability, during a restore of EKS cluster backups, customers also have the option to create a new EKS cluster based on previous EKS cluster configuration settings and restore to this new EKS cluster, with AWS Backup managing the provisioning of the EKS cluster on the customer’s behalf.

This support includes policy-based automation for protecting single or multiple EKS clusters. This single data protection policy provides a consistent experience across all services AWS Backup supports. It allows creation of immutable backups to prevent malicious or inadvertent changes, helping customers meet their regulatory compliance needs. In case there is a customer data loss or cluster downtime event, customers can easily recover their EKS cluster data from encrypted, immutable backups using an easy-to-use interface and maintain business continuity of running their EKS clusters at scale.

**How it works**

Here’s how I set up support for on-demand backup of my EKS cluster in AWS Backup. First, I’ll show a walkthrough of the backup process, then demonstrate a restore of the EKS cluster.

**Backup**

In the [AWS Backup console](https://console.aws.amazon.com/backup/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el), in the left navigation pane, I choose **Settings** and then **Configure resources** to opt in to enable protection of EKS clusters in AWS Backup.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/22/awsbackupEKS1-2-1024x400.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/22/awsbackupEKS1-2.png)

Now that I’ve enabled Amazon EKS, in **Protected resources** I choose **Create on-demand backup** to create a backup for my already existing EKS cluster `floral-electro-unicorn`.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/22/awsbackupEKS2-1-1024x239.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/22/awsbackupEKS2-1.png)

Enabling EKS in Settings ensures that it shows up as a **Resource type** when I create on-demand backup for the EKS cluster. I proceed to select the EKS resource type and the cluster.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/22/awsbackupEKS3-2-1024x437.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/22/awsbackupEKS3-2.png)

I leave the rest of the information as default, then select **Choose an IAM role** to select a role (`test-eks-backup`) that I’ve created and customized with the [necessary permissions for AWS Backup to assume when creating and managing backups on my behalf](https://docs.aws.amazon.com/aws-backup/latest/devguide/iam-service-roles.html?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el). I choose **Create on-demand backup** to finalize the process.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/22/awsbackupEKS5-1024x303.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/22/awsbackupEKS5.png)

The job is initiated, and it will start running to back up both the EKS cluster state and the persistent volumes. If Amazon S3 buckets are attached to the backup, you’ll need to [add the additional Amazon S3 backup permissions `AWSBackupServiceRolePolicyForS3Backup` to your role](https://docs.aws.amazon.com/aws-backup/latest/devguide/security-iam-awsmanpol.html#AWSBackupServiceRolePolicyForS3Backup). This policy contains the permissions necessary for AWS Backup to back up any Amazon S3 bucket, including access to all objects in a bucket and any associated AWS KMS key.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/05/awsbackupEKS8-1-1024x389.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/05/awsbackupEKS8-1.png)

The job is completed successfully and now EKS cluster`floral-electro-unicorn` is backed up by AWS Backup.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/22/awsbackupEKS7-1-1024x263.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/22/awsbackupEKS7-1.png)

**Restore**

Using the AWS Backup Console, I choose the EKS backup composite recovery point to start the process of restoring the EKS cluster backups, then choose **Restore**.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/04/restore2-1-1024x512.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/04/restore2-1.png)

I choose **Restore full EKS cluster** to restore the full EKS backup. To restore to an existing cluster, I **Choose an existing cluster** then select the cluster from the drop-down list. I choose the **Default order** as the order in which individual Kubernetes resources will be restored.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/05/restore4-3-1024x374.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/05/restore4-3.png)

I then configure the restore for the persistent storage resources, that will be restored alongside my EKS clusters.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/05/backup_storage-1024x325.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/05/backup_storage.png)

Next, I **Choose an IAM role** to execute the restore action. The **Protected resource tags** checkbox is selected by default and I’ll leave it as is, then choose **Next**.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/05/restore7-2-1024x255.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/05/restore7-2.png)

I review all the information before I finalize the process by choosing **Restore,** to start the job.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/05/restore8-2-1024x344.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/05/restore8-2.png)

Selecting the drop-down arrow gives details of the restore status for both the EKS cluster state and persistent volumes attached. In this walkthrough, all the individual recovery points are restored successfully. If portions of the backup fail, it’s possible to restore the successfully backed up persistent stores (for example, Amazon EBS volumes) and cluster configuration settings individually. However, it’s not possible to restore full EKS backup. The successfully backed up resources will be available for restore, listed as nested recovery points under the EKS cluster recovery point. If there’s a partial failure, there will be a notification of the portion(s) that failed.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/05/restore9-2-1024x266.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/05/restore9-2.png)

**Benefits**

Here are some of the benefits provided by the support for Amazon EKS in AWS Backup:

* A fully managed multi-cluster backup experience, removing the overhead associated with managing custom scripts and third-party solutions.
* Centralized, policy-based backup management that simplifies backup lifecycle management and makes it seamless to back up and recover your application data across AWS services, including EKS.
* The ability to store and organize your backups with [backup vaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/vaults.html?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el). You assign policies to the backup vaults to grant access to users to create backup plans and on-demand backups but limit their ability to delete recovery points after they’re created.

**Good to know** The following are some helpful facts to know:

* Use either the [AWS Backup Console](https://console.aws.amazon.com/backup/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el), API, or [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) to protect EKS clusters using AWS Backup. Alternatively, you can create an on-demand backup of the cluster after it has been created.
* You can create secondary copies of your EKS backups across different accounts and [AWS Regions](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#supported-services-by-region/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) to minimize risk of accidental deletion.
* Restoration of EKS backups is available using the AWS Backup Console, API, or AWS CLI.
* Restoring to an existing cluster will not override the Kubernetes versions, or any data as restores are non-destructive. Instead, there will be a restore of the delta between the backup and source resource.
* Namespaces can only be restored to an existing cluster to ensure a successful restore as Kubernetes resources may be scoped at the cluster level.

**Voice of the customer**

Srikanth Rajan, Sr. Director of Engineering at Salesforce said “Losing a Kubernetes control plane because of software bugs or unintended cluster deletion can be catastrophic without a solid backup and restore plan. That’s why it’s exciting to see AWS rolling out the new EKS Backup and Restore feature, it’s a big step forward in closing a critical resiliency gap for Kubernetes platforms.”

**Now available**

Support for Amazon EKS in AWS Backup is available today in all AWS commercial [Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region) (except China) and in the [AWS GovCloud (US)](https://aws.amazon.com/govcloud-us/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) where AWS Backup and Amazon EKS are available. Check the [full Region list](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#supported-services-by-region/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) for future updates.

To learn more, check out the [AWS Backup product page](https://aws.amazon.com/backup/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) and the [AWS Backup pricing page](https://aws.amazon.com/backup/pricing/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el).

Try out this capability for protecting your EKS clusters in AWS Backup and let us know what you think by sending feedback to [AWS re:Post for AWS Backup](https://repost.aws/tags/TAEq_tyFmxTri2axdF_HfATg/aws-backup/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el) or through your usual AWS Support contacts.

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