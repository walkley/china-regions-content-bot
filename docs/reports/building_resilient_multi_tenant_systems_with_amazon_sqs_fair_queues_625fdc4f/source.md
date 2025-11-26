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

## [AWS Compute Blog](https://aws.amazon.com/blogs/compute/)

# Building resilient multi-tenant systems with Amazon SQS fair queues

by Maximilian Schellhorn and Dirk Fröhner on 21 JUL 2025 in [Amazon Simple Queue Service (SQS)](https://aws.amazon.com/blogs/compute/category/messaging/amazon-simple-queue-service-sqs/ "View all posts in Amazon Simple Queue Service (SQS)"), [Announcements](https://aws.amazon.com/blogs/compute/category/post-types/announcements/ "View all posts in Announcements"), [Intermediate (200)](https://aws.amazon.com/blogs/compute/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [Serverless](https://aws.amazon.com/blogs/compute/category/serverless/ "View all posts in Serverless"), [Technical How-to](https://aws.amazon.com/blogs/compute/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/compute/building-resilient-multi-tenant-systems-with-amazon-sqs-fair-queues/) Share

Today, AWS introduced [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) fair queues, a new feature that mitigates [noisy neighbor](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/noisy-neighbor.html) impact in multi-tenant systems. With fair queues, your applications become more resilient and easier to operate, reducing operational overhead while improving quality of service for your customers.

In distributed architectures, message queues have become the backbone of resilient system design. They act as buffers between components, allowing services to process work asynchronously and at their own pace. When a sudden traffic spike hits your application, queues prevent cascading failures by buffering work and ensuring that downstream services aren’t overwhelmed. Amazon SQS has long been a go-to solution for developers building scalable applications because it’s a fully managed serverless solution that can seamlessly scale to ingest millions of messages per second.

In this post, you learn how to use Amazon SQS fair queues and understand their inner workings through a practical example.

## Overview

Many modern applications follow a multi-tenant architecture, where a single application instance serves multiple tenants. A tenant is any entity that shares resources with others. It could be a customer, client application, or request type. This approach reduces operational costs and simplifies maintenance through efficient resource utilization. One example of such shared resources are queues and their associated consumer capacity.

However, multi-tenant systems face challenges when one tenant becomes a noisy neighbor. This tenant impacts others by overutilizing your system’s resources. With queues, this tenant causes a backlog by sending a large volume of messages or by requiring longer processing time. Regular queues deliver older messages first, which increases message dwell time for all tenants in such scenarios. This makes it difficult to maintain quality of service and forces teams to over-provision resources or build complex custom solutions.

Amazon SQS fair queues help maintain low dwell time for other tenants when there is a noisy neighbor. This happens transparently without requiring changes to your existing message processing logic. You define what constitutes a tenant in your system, and Amazon SQS handles the complex orchestration of mitigating noisy neighbor impact.

## How it works

Amazon SQS continually monitors the distribution of messages received but not yet deleted (in-flight) by consumers across all tenants. When the system detects an imbalance:

1. It identifies the noisy tenant, the one causing the queue to build a backlog.
2. It automatically adjusts message delivery order to prioritize messages belonging to quiet (non-noisy) tenants.
3. It maintains overall queue throughput.

Consider the following example that consists of a multi-tenant queue and four different tenants (A, B, C, and D).

In the steady state condition, the queue has no backlog, and in-flight messages are evenly distributed among tenants. All messages are consumed immediately when they land in the queue. The dwell time of messages is low for all tenants. Notice that not all consumer capacity is fully utilized in this steady state. The steady state condition is illustrated in the following diagram.

[![Figure 1: A multi-tenant queue in steady state condition](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/07/18/image-1-20.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/07/18/image-1-20.png)

Figure 1: A multi-tenant queue in steady state condition

Now consider a noisy tenant scenario in which the number of messages of tenant A increases significantly and creates a backlog in the queue. Consumers are busy processing the messages mostly from tenant A, and messages from other tenants are waiting in the backlog, leading to a higher dwell time for all tenants. This noisy tenant scenario is illustrated in the following screenshot.

[![Figure 2: A multi-tenant queue with a noisy tenant](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/07/18/image-2-15.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/07/18/image-2-15.png)

Figure 2: A multi-tenant queue with a noisy tenant

When a single tenant starts to occupy a significant portion of consumer resources, Amazon SQS fair queues considers this tenant as a noisy neighbor and prioritizes returning messages belonging to other tenants. This prioritization helps maintain low dwell times for quiet tenants (B, C, D), while the dwell time for tenant A’s messages will be elevated until the queue backlog is consumed—but without impacting other tenants. Fair queues are illustrated in the following diagram.

[![Figure 3: A multi-tenant queue with fair queues](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/07/18/image-3-13.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/07/18/image-3-13.png)

Figure 3: A multi-tenant queue with fair queues

Amazon SQS doesn’t limit the consumption rate per tenant. Consumers can receive messages from noisy neighbor tenants when there is consumer capacity and the queue has no other messages to return. Like Amazon SQS standard queues, fair queues allow virtually unlimited throughput, and there are no limits on the number of tenants you can have in your queue.

## How to use

The following is a quick overview of how to get started with Amazon SQS fair queues in your applications. See the [feature documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fair-queues.html) for a detailed walkthrough. These are the high-level steps the walkthrough follows:

1. Enable Amazon SQS fair queues by adding a tenant identifier (`MessageGroupId`) to your messages
2. Configure [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics to monitor Amazon SQS fair queues behavior
3. You can use the example application to observe the Amazon SQS fair queues behavior with varying message volumes

### Enable Amazon SQS fair queues by adding a tenant identifier (MessageGroupId) to your messages

Your message producers can add a tenant identifier by setting a `MessageGroupId` on an outgoing message:

```
// Send message with tenant identifier
SendMessageRequest request = new SendMessageRequest()
    .withQueueUrl(queueUrl)
    .withMessageBody(messageBody)
    .withMessageGroupId("tenant-123");  // Tenant identifier
sqs.sendMessage(request);
```

The new fairness capability will be applied automatically in all Amazon SQS standard queues for messages with the `MessageGroupId` property. It’s important to mention that it doesn’t require any change in the consumer code. It has no impact on API latency and doesn’t come with any throughput limitations.

### Configure Amazon CloudWatch metrics to monitor Amazon SQS fair queues behavior

You can monitor Amazon SQS fair queues with [Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html). The following terms are important in this context:

* **Noisy groups** – A noisy message group represents a noisy neighbor tenant of a multi-tenant queue.
* **Quiet groups** – Message groups excluding noisy groups.

Amazon SQS now emits the following additional metrics:

* `ApproximateNumberOfNoisyGroups`
* `ApproximateNumberOfMessagesVisibleInQuietGroups`
* `ApproximateNumberOfMessagesNotVisibleInQuietGroups`
* `ApproximateNumberOfMessagesDelayedInQuietGroups`
* `ApproximateAgeOfOldestMessageInQuietGroups`

The new `ApproximateNumberOfNoisyGroups` metric gives the number of message groups (tenants) that are considered noisy in a fair queue. This metric helps identify the number of potential noisy neighbors in multi-tenant environments by tracking message groups consuming disproportionate resources. Use this metric to set alarms that trigger when the number of noisy groups exceeds your acceptable threshold, indicating potential queue fairness issues.

Amazon SQS already provides several standard queue-level metrics that offer approximate insights into the queue’s state, message processing, and potential bottlenecks. These metrics look at all messages in a queue. With fair queues, there’s a new set of four equivalent metrics, shown in the preceding list, that allow the exclusion of messages from noisy neighbor groups and target only quiet groups (non-noisy tenants). Hence, they all have the `InQuietGroups` suffix.

To monitor the effect of Amazon SQS fair queues you can compare metrics that have the `InQuietGroups` suffix with standard queue-level metrics. During traffic surges for a specific tenant, the general queue-level metrics might reveal increasing backlogs or older message ages. However, looking at the quiet groups in isolation, you can identify that most non-noisy message groups or tenants aren’t impacted, and you can estimate the total number of impacted message groups.

The following graph shows how the standard queue backlog metric (`ApproximateNumberOfMessagesVisible`) increases due to a noisy tenant while the backlog for non-noisy tenants (`ApproximateNumberOfMessagesVisibleInQuietGroups`) remains low.

[![Figure 4: Queue backlog for noisy and quiet groups](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/07/18/image-4-12.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/07/18/image-4-12.png)

Figure 4: Queue backlog for noisy and quiet groups

While these new metrics provide a good overview of Amazon SQS fair queues behavior, it can be beneficial to understand which specific tenant is causing the load. Use [Amazon CloudWatch Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) to see metrics about the top-N contributors, the total number of unique contributors, and their usage. This is especially helpful in scenarios where you’re dealing with thousands of tenants that would otherwise lead to high-cardinality data (and cost) when emitting traditional metrics. The following screenshot shows an example of a Contributor Insights dashboard on the AWS console that visualizes the top 10 contributors based on `MessageGroupId`.

[![Figure 5: Container Insights ReceivedMessagesPerMessageGroupId dashboard](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/07/18/image-5-10.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/07/18/image-5-10.png)

Figure 5: Contributor Insights ReceivedMessagesPerMessageGroupId dashboard

Contributor Insights creates these metrics based on data from your application log output. Let your code log the number of messages being processed, and the corresponding `MessageGroupId` within your application. You can find a full example in the sample application in the next section.

## Example application

To make it even more straightforward to get started, we’ve prepared an example application that you can use to observe the Amazon SQS fair queues behavior with varying message volumes. You can find the source code repository, infrastructure as code (IaC), and the instructions to run the sample on the [sqs-fair-queues repository](https://github.com/aws-samples/sample-amazon-sqs-fair-queues) on GitHub.

The example application includes a load generator to simulate multi-tenant traffic and provides an [Amazon CloudWatch dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) that displays the most important metrics to visualize fair queue behavior. The following screenshot shows an example of the dashboard.

[![](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/07/18/image-6-10.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/07/18/image-6-10.png)

Figure 6: CloudWatch FairQueuesDashboard

## Conclusion

Amazon SQS fair queues automatically mitigates the noisy neighbor impact in multi-tenant queues. Even when one tenant generates high message volumes or requires longer processing times (that is, becomes a noisy neighbor), the feature maintains consistent message dwell times for other tenants. When you add a tenant identifier to your messages, Amazon SQS fair queues will automatically detect and mitigate noisy neighbor impact, providing fair access to the queue for other tenants.

We recommend reviewing the [Amazon SQS Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) to get started and exploring the sample applications to test the behavior with varying message volumes.

### Resources

[Serverless Computing and Applications](https://aws.amazon.com/serverless?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=compute-resources)  [Amazon Container Services](https://aws.amazon.com/containers?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=compute-resources)  [AWS Messaging](https://aws.amazon.com/messaging?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=compute-resources)  [Cloud Compute with AWS](https://aws.amazon.com/products/compute?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=compute-resources)  [Desktop and Application Streaming](https://aws.amazon.com/products/desktopsandapps?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=compute-resources)

---

### Follow

[Twitter](https://twitter.com/awscloud)  [Facebook](https://www.facebook.com/amazonwebservices)  [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)  [Twitch](https://www.twitch.tv/aws)  [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-social)

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