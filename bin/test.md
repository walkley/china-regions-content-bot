# Optimize Your AWS Spend with New Cost Savings Features in AWS Trusted Advisor

by Logan Kleier
on 05 JUN 2025
in Announcements, AWS Cloud Financial Management, AWS Compute Optimizer, AWS Trusted Advisor

In response to customer requests for a more consistent cost savings experience and broader set of recommendations, [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor) is expanding its capabilities. We’re excited to announce the integration of 15 new checks from [AWS Cost Optimization Hub](https://aws.amazon.com/aws-cost-management/cost-optimization-hub/) into Trusted Advisor. This significant update provides more actionable insights to help you optimize your AWS spend.

You can learn more about the new checks in the [Trusted Advisor Check Reference Guide](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html).

## Why you should use the new cost optimization checks from Cost Optimization Hub?

These new checks and recommendations provide Trusted Advisor customers with:

- More customized and specific cost optimization recommendations.
- A broader array of cost savings optimization checks than previously available.
- Improved alignment of cost savings estimates and recommendations between Trusted Advisor and Cost Optimization Hub.

## How can you get started with the new Trusted Advisor checks and recommendations?

To get these checks and recommendations in Trusted Advisor, you’ll want to:

1. Opt in to Cost Optimization Hub, see [Getting Started with Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).
2. Opt in to Compute Optimizer, see [Opting in to AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).

AWS Trusted Advisor customers need to opt in to Cost Optimization Hub and Compute Optimizer to receive the full benefits of these Cost Optimization Hub checks and recommendations. Customers will also need to opt in to Compute Optimizer, because Cost Optimization Hub uses data from Compute Optimizer to provide rightsizing and idle recommendations. Both of these optimization products are free of charge, unless you configure 93 day lookback periods for EC2 and RDS rightsize recommendations. See [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) and [AWS Compute Optimizer pricing](https://aws.amazon.com/compute-optimizer/pricing/) for more details.

Once you opt in to Cost Optimization Hub and Compute Optimizer, it will take up to 24 hours before you start seeing recommendations for the new Trusted Advisor checks that use Cost Optimization Hub.

Customers who have already opted in to Cost Optimization Hub and AWS Compute Optimizer and have AWS Business Support or higher will automatically receive the newer Trusted Advisor checks and recommendations.

## What is Cost Optimization Hub and why is Trusted Advisor integrating with it?

Cost Optimization Hub, a feature of AWS Billing and Cost Management, consolidates and prioritizes cost optimization recommendations across AWS Organizations member accounts and AWS Regions. It allows you to easily identify, filter, and aggregate over 16 types of AWS cost optimization recommendations through a single dashboard. These recommendations come from Cost Explorer for Reservation and Savings Plan recommendations, and AWS Compute Optimizer for rightsizing and idle recommendations.

Cost Optimization Hub helps you quantify and aggregate estimated savings when you implement cost optimization recommendations. Cost Optimization Hub accounts for your specific commercial terms with AWS, such as Reserved Instances and Savings Plans, so you can easily compare and prioritize recommendations. By integrating these checks and recommendations into Trusted Advisor, Trusted Advisor provides more actionable insights to customers.

## What is the list of new Trusted Advisor checks?

We are introducing 15 new checks. Table 1 below describes the current Trusted Advisor checks, their IDs, as well as the new Trusted Advisor checks from Cost Optimization Hub recommendations:

| Trusted Advisor Check Name | CheckID | Cost Optimization Hub Check Name | CheckID |
| --- | --- | --- | --- |
| [Low Utilization Amazon EC2 Instances](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#low-utilization-amazon-ec2-instances) | Qch7DwouX1 | [Amazon EC2 Cost Optimization recommendations for instances](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#ec2-cost-opt-for-instances) | c1z7kmr00n |
| [Underutilized Amazon EBS Volumes](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#underutilized-amazon-ebs-volumes) | DAvU99Dc4C | [Amazon EBS cost optimization recommendations for volumes](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#ebs-cost-opt-for-volumes) | c1z7kmr02n |
| [Amazon EBS over-provisioned volumes](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#amazon-ebs-over-provisioned-volumes) | COr6dfpM03 | [Amazon EBS cost optimization recommendations for volumes](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#ebs-cost-opt-for-volumes) | c1z7kmr02n |
| [Amazon RDS Idle DB Instances](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#amazon-rds-idle-dbs-instances) | Ti39halfu8 | [Amazon RDS cost optimization recommendations for DB instances](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#rds-cost-opt-for-db-instances) | c1z7kmr03n |
| [AWS Lambda over-provisioned functions for memory size](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#aws-lambda-over-provisioned-functions-memory-size) | COr6dfpM05 | [AWS Lambda cost optimization recommendations for functions](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#lambda-cost-opt-for-functions) | c1z7kmr05n |
| [Savings Plan](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#savings-plan) | vZ2c2W1srf | [AWS Savings Plan purchase recommendations for compute](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#savings-plans-purchase-recommendations-compute) | c1z7kmr09n |
| [Amazon Relational Database Service (RDS) Reserved Instance Optimization](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#amazon-rds-reserved-instance-optimization) | 1qazXsw23e | [Amazon RDS Reserved Instance purchase recommendations](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#rds-ri-purchase-recommendations) | c1z7kmr11n |
| [Amazon Redshift Reserved Node Optimization](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#amazon-redshift-reserved-node-optimization) | 1qw23er45t | [Amazon RedShift reserved node purchase recommendations](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#redshift-reserved-node-purchase-recommendations) | c1z7kmr12n |
| [Amazon ElastiCache Reserved Node Optimization](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#amazon-elasticache-reserved-node-optimization) | h3L1otH3re | [Amazon ElastiCache reserved node purchase recommendations](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#elasticache-reserved-node-purchase-recommendations) | c1z7kmr13n |
| [Amazon OpenSearch Service Reserved Instance Optimization](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#amazon-opensearch-reserved-instance-optimization) | 7ujm6yhn5t | [Amazon OpenSearch Service Reserved Instance purchase recommendations](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#os-ri-purchase-recommendations) | c1z7kmr14n |

*Table 1: List of Current Trusted Advisor Cost Optimization Checks and Ones from Cost Optimization Hub*

Note: The two Trusted EBS utilization checks listed above (Underutilized Amazon EBS Volumes and Amazon EBS over-provisioned volumes) are being replaced by one newer check (Amazon EBS Cost Optimization Recommendations for Volumes).

Table 2 below describes the 7 new Trusted Advisor checks and recommendations from Cost Optimization Hub and their respective check IDs:

| Cost Optimization Hub Check Name | Check ID |
| --- | --- |
| [Amazon EC2 cost optimization recommendations for Amazon EC2 Auto Scaling groups](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#ec2-cost-opt-for-autoscaling) | c1z7kmr01n |
| [Amazon RDS cost optimization recommendations for DB instance storage](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#rds-cost-opt-for-db-instance-storage) | c1z7kmr04n |
| [AWS Fargate cost optimization recommendations for Amazon ECS](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#fargate-cost-opt-for-ecs) | c1z7kmr06n |
| [AWS Savings Plan purchase recommendations for Amazon SageMaker AI](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#savings-plans-purchase-recommendations-sagemaker) | c1z7kmr08n |
| [Amazon DynamoDB reserved capacity purchase recommendations](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#dynamodb-reserved-capacity-purchase-rec) | c1z7kmr15n |
| [Amazon MemoryDB reserved node purchase recommendations](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#memorydb-reserved-node-purchase-recommendations) | c1z7kmr16n |
| Amazon Aurora cost optimization recommendations for DB cluster storage | c1z7kmr17n |

*Table 2: List of New Cost Optimization Checks within Trusted Advisor*

## Which cost optimization checks and recommendations should you use?

You should use the newer checks and recommendations from Cost Optimization Hub listed above in Table 1, Column 3 and 4. These checks and recommendations provide more accurate cost savings estimates and personalized recommendations based on your resource utilization than the Trusted Advisor checks and recommendations listed above in Table 1, Column 1 and 2.

## Will you have access to both existing Trusted Advisor checks and new Cost Optimization Hub checks?

Yes, we will continue to provide access to both sets of checks. However, the older Trusted Advisor checks are considered to be legacy checks and we encourage you to use the newer checks. We will add a banner in the older legacy checks to indicate that these are legacy checks and recommend you use the newer, replacement ones.

## What are the differences between the older Trusted Advisor checks and the newer ones from Cost Optimization Hub?

The newer Cost Optimization Hub checks provide improved accuracy in terms of cost savings estimates. these checks account for your specific commercial terms with AWS, such as Reserved Instances and Savings Plans, so you can easily compare and prioritize recommendations. Additionally, the cost optimization recommendations take into account more contextual and historical information on how your resources are being used. In the example below (Figure 1), we can examine how the current [Qch7DwouX1 TA check](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#low-utilization-amazon-ec2-instances) would show for a cost savings estimate and recommendation for achieving this cost savings. This check result shows a savings estimate and recommends that you stop or terminate the instance in order to achieve the cost savings.

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/06/05/ta1.png)

Figure 1: Current Trusted Advisor cost optimization check

In Figure 2 below, you can see the same type of check produces different recommendations on how to achieve these cost savings. Figure 2 shows how the newer Trusted Advisor cost optimization check (check ID c1z7kmr00n) shows different types of recommendations such as Migrating to Graviton or Right Sizing the instance versus the check above which shows only the option to stop or terminate the instance in order to achieve cost savings.

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/06/05/ta2.png)

Figure 2: New Cost Optimization Hub Check in Trusted Advisor

With the new Trusted Advisor cost optimization checks and recommendations from Cost Optimization Hub, you’ll get more accurate and personalized cost optimization opportunities to save money on your AWS bill. Opt in to Cost Optimization Hub and Compute Optimizer and let us know what you think. Submit feedback for the new Trusted Advisor checks or for new cost optimization features in the AWS console by opening the service’s console, and then choose Feedback in the lower right hand corner or, use [AWS re:Post](https://repost.aws/).