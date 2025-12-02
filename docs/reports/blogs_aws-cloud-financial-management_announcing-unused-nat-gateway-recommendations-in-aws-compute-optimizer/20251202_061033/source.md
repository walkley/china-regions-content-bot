# Announcing Unused NAT Gateway Recommendations in AWS Compute Optimizer

by Nathan Yuan on 26 NOV 2025 in AWS Cloud Financial Management, AWS Compute Optimizer, Launch, Networking & Content Delivery, News Permalink  Share

Starting today, AWS Compute Optimizer expands its idle resource detection capabilities to include [NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html). Building on our recent launch of idle recommendations for compute, storage, and database resources, you can now identify and clean up unused NAT Gateway resources to drive additional cost savings while maintaining application reliability.

## Why should you use unused NAT Gateway recommendations?

Network infrastructure resources like NAT Gateways represent a substantial portion of cloud spending, yet optimizing these costs presents unique challenges. Unlike compute resources, NAT Gateways often play critical roles in high availability and disaster recovery architectures, making it difficult to confidently identify which ones are truly unused versus those serving as disaster recovery or backup components.

With Compute Optimizer’s NAT Gateway recommendations, we not only analyze utilization patterns but also examine architectural context like route table associations. The additional context helps distinguish between truly unused resources and those maintained for disaster recovery purposes. This enables you to optimize network costs while protecting your high-availability setups.

## How are NAT Gateways detected as unused?

Compute Optimizer analyzes [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics over a 32-day period to determine if a NAT Gateway meets the following unused conditions:

- No active connections (`ActiveConnectionCount` = 0)
- No incoming packets from clients in your [Amazon Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/) (`PacketsInFromSource` = 0)
- No incoming packets from the destination (`PacketsInFromDestination` = 0)

To protect backup configurations, we also examine whether the NAT Gateway is associated with any route table. NAT Gateways with zero traffic, but active route table associations, often serve as standby components in networking architectures. By checking for route table associations, we avoid recommending the removal of these critical backup components.

For NAT Gateways that are truly unused, we recommend checking if they’re part of disaster recovery setups. For example, some organizations use [AWS Lambda](https://aws.amazon.com/lambda/) functions that programmatically update route tables during failover events, redirecting traffic to a backup NAT Gateway only when the primary fails. In these cases, the backup NAT Gateway shows zero traffic and has no route table association during normal operations, making it appear unused to automated detection. This is why manual verification of your high-availability and disaster recovery architectures is essential before removing any flagged NAT Gateway.

## How can you get started?

After opting into Compute Optimizer, you’ll automatically begin receiving unused NAT Gateway recommendations within 24 hours. These recommendations appear alongside your existing idle resource findings in the Compute Optimizer console.

On the dashboard, navigate to the “Idle resources” page to see a consolidated view of all idle or unused resources, including your NAT Gateways. The table displays estimated monthly savings, resource details, and tags to help you prioritize actions:

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/11/24/idle_nat.png)

Figure 1. Recommendation by resource type table

When you select an individual unused NAT Gateway, you’ll see a detailed view with utilization metrics that demonstrate why the resource was identified as unused. You’ll see graphs of `ActiveConnectionCount`, `PacketsInFromSource`, and `PacketsInFromDestination` over the 32-day analysis period, allowing you to verify the unused condition before taking action:

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/11/24/idle_nat2.png)

Figure 2. Recommendation by resource type table

You can also access these recommendations programmatically using the Compute Optimizer API. The existing `GetIdleRecommendations` API now includes NAT Gateway resources. Read the [user guide](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html) for details.

## Integration with AWS Cost Optimization Hub

Unused NAT Gateway recommendations are also integrated with AWS Cost Optimization Hub, providing multiple ways to incorporate network optimization into your existing workflows.

In Cost Optimization Hub, these NAT Gateway recommendations appear alongside your commitment and rightsizing recommendations, giving you a complete view of optimization opportunities across your organization. Cost Optimization Hub automatically deduplicates savings across overlapping recommendations to give you an accurate view of total potential savings.

## Conclusion

With AWS Compute Optimizer’s expanded unused resource detection for NAT Gateways, you can now implement a more comprehensive cost optimization strategy that addresses network infrastructure alongside compute, storage, and database resources. The service’s architectural awareness helps you identify unused resources while protecting your disaster recovery and failover configurations, enabling you to optimize with confidence.

Get started today by visiting the [Compute Optimizer console](https://console.aws.amazon.com/compute-optimizer/) or learn more in the [user guide](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html).