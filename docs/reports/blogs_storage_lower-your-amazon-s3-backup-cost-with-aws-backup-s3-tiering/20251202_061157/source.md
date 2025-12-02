# Lower your Amazon S3 backup costs with AWS Backup S3 tiering

by Stuart Lupton and Sravan Rachiraju on 26 NOV 2025 in Advanced (300), Amazon Simple Storage Service (S3), AWS Backup, Best Practices, Cloud Cost Optimization, Storage, Technical How-to Permalink  Comments   Share

Organizations face a critical challenge in data protection: how to retain ever-increasing volumes of backup data for extended periods while maintaining cost efficiency. Regulatory mandates, internal governance policies, and comprehensive disaster recovery strategies often necessitate preserving backups for months or even years. At the same time, the threat landscape continues to evolve, with sophisticated ransomware attacks making secure, tamper-resistant backups more critical than ever. This creates a trade-off between maintaining robust long-term data protection and managing costs effectively, often forcing organizations to choose between comprehensive protection capabilities and budget constraints.

To address this, [AWS Backup](https://aws.amazon.com/backup/) has introduced a low-cost warm storage tier for [Amazon S3](https://aws.amazon.com/s3/) backup data that can reduce long-term storage costs by up to 30% while maintaining all protection capabilities and performance. This new tier is integrated into the unified data protection service from AWS Backup, giving organizations access to the same enterprise-grade security, intelligent storage options, and comprehensive capabilities they rely on, including point-in-time recovery, ransomware protection and recovery, and compliance controls.

In this post, we demonstrate how to configure AWS Backup’s low-cost warm storage tier to reduce your Amazon S3 backup storage costs without compromising protection. We walk through setting up automatic tiering that transitions backup data after at least 60 days in the vault, share best practices for when to use tiering, and show how to maintain comprehensive data protection over extended retention periods—all with minimal operational overhead.

## Introducing low-cost warm storage for Amazon S3 backups

AWS Backup now offers a low-cost warm storage tier for long-lived Amazon S3 backup data that transitions eligible backups to lower-cost warm storage. This feature maintains all the enterprise-grade protection capabilities of AWS Backup and can reduce storage costs for long-term retention.

You can enable tiering on your backup vault so AWS Backup automatically transitions eligible S3 backup data to the low-cost warm storage tier. Initially, all backed-up S3 objects are stored in the vault’s standard tier. AWS Backup determines eligibility based on how long objects have been in the backup vault. Objects become eligible for transition after residing in the vault for at least 60 days (or your configured threshold). Once per day, AWS Backup evaluates eligibility and moves eligible objects to the low-cost warm storage tier, incurring a one-time, nominal transition fee. These transitions are independent of recovery-point retention settings and backup schedules.

The low-cost warm storage tier provides the same restore performance and features as the standard tier, including ransomware protection, recovery workflows, and auditing. Tiering is configured at the backup vault level. You can configure automatic tiering for all Amazon S3 backups across all vaults in an account, for a specific vault, or for specific buckets within a vault by setting an age threshold of at least 60 days. This vault-level model lets you manage cost optimization independently of backup schedules and retention policies, and it keeps tiering clearly separated from retention. The configuration is compatible with AWS Backup security features, including [Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html), [restore testing](https://aws.amazon.com/blogs/storage/implementing-restore-testing-for-recovery-validation-using-aws-backup/), [search and item-level recovery](https://aws.amazon.com/blogs/storage/streamline-search-and-item-level-recovery-with-aws-backup/), and [logically air-gapped vault](https://docs.aws.amazon.com/aws-backup/latest/devguide/logicallyairgappedvault.html), so your data protection posture is unchanged.

Once a tiering configuration is applied to a backup vault, AWS Backup evaluates S3 objects in the vault against the configuration during daily evaluations and transitions objects that meet the age threshold. When tiering is enabled, objects in existing backup data beyond the threshold are identified and moved to the low-cost warm storage tier during the next evaluation, with subsequent storage billed at the lower-cost warm storage tier rate. If you later modify the configuration, for example by removing a vault from the configuration, deleting the configuration, or adjusting resource assignments, new transitions stop, but objects already in the low-cost warm storage tier remain there until they expire under the retention policy or are deleted. For cross-Region and cross-account copies, copies land in the standard tier of the destination vault. The destination vault’s tiering configuration determines when they become eligible to transition.

## Understanding S3 tiering operational behavior

AWS Backup S3 tiering operates with the following characteristics:

**Daily evaluation**: AWS Backup evaluates object eligibility once per day. Objects that have reached the threshold transition automatically during this evaluation.

**Standard tier first**: All objects are initially stored in the standard tier. You can’t write directly to the lower-cost tier.

**Configuration changes**: If you modify your tiering configuration by removing a vault, deleting the configuration, or changing resource assignments, then new transitions stop. However, objects already in the lower-cost tier remain there until they expire by retention policy or are deleted.

**Handling configuration conflicts**: When multiple tiering configurations could apply to the same Amazon S3 resource in a vault, AWS Backup uses this resolution rule: more specific configurations override general ones (for example a configuration targeting specific Amazon S3 resources takes precedence over one targeting all resources).

## Pricing and cost savings

The low-cost warm storage tier introduces a cost-optimized pricing model with two components:

1. **Storage costs**: Data in the low-cost warm storage tier is charged at approximately 30% less than the standard tier. For example, if the standard tier costs $0.05 per GB-month, then the low-cost warm storage tier would be approximately $0.035 per GB-month (pricing varies by AWS Region).

2. **One-time tiering fee**: A nominal fee is charged when objects transition from the standard tier to the lower-cost tier. This fee is based on the number of objects being tiered, charged at approximately $0.01 per 1,000 objects (pricing varies by AWS Region).

### Cost savings example

In this section we look at a practical example for a customer with a 500 TB bucket with 1 billion objects with an average object size of 500 kb in the US East (Virginia) Region:

**Without S3 tiering:**

Storage costs per month before tiering: 500 TB\*1024\*0.05 GB/month = $25,600/month

**With S3 tiering (assuming 80% of objects would be tiered down after 60 days):**

Storage costs per month after tiering: 500 TB\*1024\*20%\*0.05 GB/month + 500 TB\*1024\*80%\*0.035 GB/month = **$19,456/month**

One-time transition fee as data moves to the low-cost warm storage tier: 1 B\*80%\*0.01/1000 = **$8000**

Total savings in subsequent months: **$6144/month**

To obtain data insights on your Amazon S3 resources such as object age information, which can be used to calculate your tiering configurations, we recommend [Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_basics_metrics_recommendations.html#storage_lens_basics_data_queries).

For the most current pricing information, visit the [AWS Backup pricing page](https://aws.amazon.com/backup/pricing/).

## Configuring S3 backup tiering

In this section we walk through how to implement S3 tiering in your environment. The process is direct and needs minimal ongoing management when it’s configured.

### Creating a tiering configuration

1. Navigate to the tiering section: Sign in to the [AWS Management Console](https://aws.amazon.com/console/), open the AWS Backup console, in the left navigation pane choose **S3 backup tiering** and choose **Create configuration**.

*![](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/11/26/image-5-13.png)*

*Figure 1: Choosing **Create configuration***

2. Define your configuration name: Enter a descriptive name that helps you identify this configuration (for example “ComplianceData-60days” or “GlobalDefault-S3Tiering”).

3. Choose your resource scope: You have two options for determining the Amazon S3 resources to which this tiering configuration applies:

**Option 1: All Amazon S3 resources in all vaults:** This creates a default configuration that applies to all Amazon S3 resources backed up in your account. Specify the time threshold (minimum 60 days) after which objects become eligible for tiering. This option provides a direct way to implement consistent tiering across your entire Amazon S3 backup.

![console screenshot showing an example tiering configuration with all Amazon S3 resources in all vaults selected](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/11/26/image-2-14.png)

*Figure 2: Example tiering configuration with all Amazon S3 resources in all vaults selected*

**Option 2: Amazon S3 resources in a specific vault**: This allows more granular control by targeting a specific vault. If you choose this option, then you first choose a specific backup vault from the dropdown menu and choose whether to apply tiering to all Amazon S3 resources in that vault or only to specific Amazon S3 resources. For specific resources, you can configure up to 5 different tiering settings, with each setting applicable to multiple resources. A maximum of 100 specific resources can be protected within a specific vault. This approach enables different tiering thresholds for different groups of resources within the same vault, giving you precise control over when different objects transition to the low-cost warm storage tier.

![console screenshot showing example tiering configuration with specific Amazon S3 resources within a specific vault](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/11/26/image-3-12.png)

*Figure 3: Example tiering configuration with specific Amazon S3 resources within a specific vault*

4. Add optional tags: Apply tags to your tiering configuration for organizational purposes. These tags can help with resource management, cost allocation, and automation.

5. Complete the configuration: Review your settings and choose **Create configuration**.

When your tiering configuration is created, it’s applied to the specified vaults. AWS Backup begins evaluating object eligibility as part of its regular processing cycle. Objects in the vault that meet the age threshold are identified for transition to the lower-cost tier, while new objects are tracked and transitioned when they reach the specified age.

## Best practices

Implementing an effective S3 backup tiering strategy necessitates balancing cost optimization with operational requirements. Use these best practices to maximize value while making sure that your data protection needs are met.

### When to implement the low-cost warm storage tier

**Compliance and long-term data preservation**: Organizations that retain their data in S3 buckets for extended periods benefit from implementing tiering for the backups of those buckets. This is particularly valuable for datasets with low deletion rates where most objects persist for months or years.

**Data lakes and analytics repositories**: Large Amazon S3 datasets with predictable growth patterns—such as append-only data stores, historical analytics data, and partitioned datasets—often contain a high percentage of objects eligible for tiering, maximizing cost savings.

### When to exercise caution

**High data churn**: Environments where S3 objects are frequently deleted or replaced within the first 60 days may see limited benefit from tiering, because objects must remain in the standard tier for at least 60 days before transition.

**Small object workloads**: Consider both storage savings and transition costs in your planning. The one-time transition fee (charged per 1,000 objects) is designed to be nominal, but for workloads with millions of small objects, it’s worth analyzing your object count and size distribution to optimize your savings. Furthermore, objects smaller than 128 KB are billed at 128 KB even in the low-cost warm storage tier. For most customers, the long-term storage savings significantly outweigh the one-time transition costs, but performing this analysis helps make sure that you maximize the benefits of tiering for your specific workload characteristics.

### Implementation guidance

**Analyze your source data**: Understanding how long objects typically remain in your buckets without being deleted provides valuable insight when determining if tiering is appropriate for your workloads. This analysis helps you make an informed decision about which resources would benefit from tiering and which transition threshold makes the most sense for your environment

**Start with a pilot**: Begin by enabling tiering on a single Amazon S3 resource, containing data with predictable object retention patterns.

**Monitor cost impact**: After implementing tiering, closely monitor your AWS bill to validate the cost benefits and identify opportunities for further optimization.

**Review transition timing**: Although 60 days is the minimum transition period, consider your specific access patterns and recovery requirements when determining the optimal timing for your environment.

You can carefully apply these best practices to implement an S3 tiering strategy that reduces your backup storage costs while maintaining the robust protection capabilities needed by your organization.

## Conclusion

The AWS Backup low-cost warm storage tier represents a significant advancement in optimizing the cost of long-term data protection. Organizations can automatically transition older Amazon S3 backup data to a lower-cost warm storage tier after at least 60 days on the vault, reducing ongoing backup storage costs while maintaining all the enterprise-grade protection features of AWS Backup. This is particularly valuable for organizations with regulatory requirements to retain backup data for extended periods. The implementation is straightforward and requires minimal operational overhead, and it lowers storage charges as eligible data transitions.

As data volumes continue to grow and retention requirements extend, cost-effective data protection becomes increasingly important. AWS Backup low-cost warm tier removes the need to choose between comprehensive protection and cost management, so that organizations can achieve both objectives simultaneously.

To get started with the AWS Backup low-cost warm tier, visit the AWS Backup console today and create your first tiering configuration.