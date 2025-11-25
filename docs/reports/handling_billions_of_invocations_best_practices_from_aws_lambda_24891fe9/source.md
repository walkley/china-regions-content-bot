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

# Handling billions of invocations – best practices from AWS Lambda

by Chris McPeek on 17 MAR 2025 in [AWS Lambda](https://aws.amazon.com/blogs/compute/category/compute/aws-lambda/ "View all posts in AWS Lambda"), [Messaging](https://aws.amazon.com/blogs/compute/category/messaging/ "View all posts in Messaging") [Permalink](https://aws.amazon.com/blogs/compute/handling-billions-of-invocations-best-practices-from-aws-lambda/) Share

*This post is written by Anton Aleksandrov, Principal Solution Architect, AWS Serverless and Rajesh Kumar Pandey, Principal Engineer, AWS Lambda*

[AWS Lambda](https://aws.amazon.com/lambda/) is a highly scalable and resilient serverless compute service. With over 1.5 million monthly active customers and tens of trillions of invocations processed, scalability and reliability are two of the most important service tenets. This post provides recommendations and insights for implementing highly distributed applications based on the Lambda service team’s experience building its robust asynchronous event processing system. It dives into challenges you might face, solution techniques, and best practices for handling noisy neighbors.

## Overview

Developers building serverless applications create Lambda functions to run their code in the cloud. After uploading the code, the functions are invoked using synchronous or asynchronous mode.

[Synchronous invocations](https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html) are commonly used for interactive applications that expect immediate responses, such as web APIs. The Lambda service receives the invocation request, invokes the function handler, waits for the handler response, and returns it in response to the original request. With synchronous invocations, the client waits for the function handler to return, and is responsible for managing timeouts and retries for failed invocations.

[![Synchronous invocation sequence diagram.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-1.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-1.png)

Figure 1. Synchronous invocation sequence diagram

[Asynchronous invocations](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html) enable decoupled function executions. Clients submit payloads for processing without expecting immediate responses. This is used for scenarios like asynchronous data processing or order/job submissions. The Lambda service immediately returns a confirmation for accepted invocation and proceeds to manage further handler invocation, timeouts, and retries asynchronously.

[![Asynchronous invocation sequence diagram.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-2.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-2.png)

Figure 2. Asynchronous invocation sequence diagram

## Asynchronous invocations under-the-hood

To accommodate asynchronous invocations, the Lambda service places requests into its internal queue and immediately returns HTTP 202 back to the client. After that, a separate internal poller component reads messages from the queue and synchronously invokes the function.

[![Asynchronous invocations workflow high-level topology.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-3.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-3.png)

Figure 3. Asynchronous invocations workflow high-level topology

The same system also takes care of timeouts and retries in case of handler exceptions. When code execution completes, the system sends handler response to either [**onSuccess** or **onFailure** destination](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html#invocation-async-destinations), if configured.

[![Asynchronous invocations workflow detailed sequence diagram.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-4.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-4.png)

Figure 4. Asynchronous invocations workflow detailed sequence diagram

Scaling highly distributed systems for billions of asynchronous requests presents unique challenges, such as managing [noisy neighbors](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/noisy-neighbor.html) and potential traffic spikes to prevent system overload. Solutions vary by scale – what works for millions of requests may not suite billions. As workload size increases, solutions typically become more complex and costly, so right-sizing the approach is critical and should evolve with changing needs.

## Simple queueing

A simple implementation of an asynchronous architecture can start with a single shared queue. This is a common approach for many asynchronous systems, particularly in early stages. It is effective when you’re not concerned about tenant isolation and when capacity planning indicates that a single queue can handle estimated incoming traffic efficiently.

[![Asynchronous workflow with a single queue.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-5.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-5.png)

Figure 5. Asynchronous workflow with a single queue

Even with this simple setup, it is critical to instrument your solution for observability to detect potential issues as soon as possible. You should [monitor key metrics](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/) like queue backlog size, processing time, and errors, to indicate insufficient processing capacity early. Periods of unexpected traffic spikes and degraded performance may be a signal you have noisy neighbors impacting other tenants.

To address this, you can scale your solution horizontally. You can implement random request placement across multiple queues to spread the load. Using a serverless service like [Amazon SQS](https://aws.amazon.com/sqs/) allows you to easily add and remove queues on-demand. One notable benefit of this approach is its simplicity – you do not need to introduce any complex routing mechanisms; requests are evenly spread across the queues. The downside is that you still do not have tenant boundaries. As your system grows, high-volume tenants and noisy neighbors can potentially affect all queues, thus impacting all tenants.

[![Asynchronous workflow with multiple queues and random request placement.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-6.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-6.png)

Figure 6. Asynchronous workflow with multiple queues and random request placement

## Intelligent partitioning with consistent hashing

In order to further reduce potential impact, you can partition your tenants using sticky tenant-to-partition assignment with a hashing technique such as [consistent hashing](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/consistent-hashing.html). This method uses a hash function to assign each tenant to a queue on a [consistent hash ring](https://en.wikipedia.org/wiki/Consistent_hashing).

[![Asynchronous workflow with multiple queues and consistent hashing placement.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-7.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-7.png)

Figure 7. Asynchronous workflow with multiple queues and consistent hashing placement

This technique ensures individual tenants stay in their queue partitions without the risk of disturbing the whole system. It helps to solve the problem where a few noisy neighbors have the potential to overflow all queues and as such impact all other tenants.

The consistent hashing approach proved to be efficient and enabled Lambda to offer robust asynchronous invocation performance to customers. As the volume of traffic and number of customers continued to grow, the Lambda service team came up with an innovative shuffle-sharding technique to further optimize the experience, and proactively eliminate any potential noisy-neighbor issues.

## Shuffle-sharding

Drawing inspiration from the [“The Power of Two Random Choices” paper](https://www.eecs.harvard.edu/~michaelm/postscripts/handbook2001.pdf), the Lambda team explored the [shuffle-sharding technique](https://aws.amazon.com/blogs/architecture/shuffle-sharding-massive-and-magical-fault-isolation/) for its asynchronous invocations processing. Using this technique, you shuffle-shard tenants into several randomly assigned queues. Upon receiving an asynchronous invocation, you place the message in the queue with the smallest backlog to optimize load distribution. This approach helps to minimize the likelihood of assigning tenants to a busy queue.

[![Asynchronous workflow with multiple queues and shuffle-sharding placement.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-8.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-8.png)

Figure 8. Asynchronous workflow with multiple queues and shuffle-sharding placement

To illustrate the benefit of this approach, consider a scenario where you’re using а 100 queues. The following formula helps to calculate the number of unique queue shards (combinations), where *n* is the total number of queues and *r* is the shard size (the number of queues you’re assigning per tenant).

[![Formula to show queue shard calculation.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-9.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-9.png)

With n=100, r=2 (each tenant is assigned randomly to 2 out of 100 queues), you get 4,950 unique combinations (shards). The probability of two tenants assigned to exactly the same shard is 0.02%. In case of *r=3*, the number of combinations spikes to 161,700. The probability of two tenants assigned to exactly the same shard drops to 0.0006%.

The shuffle-sharding technique proved remarkably effective. By distributing tenants across shards, the approach ensures that only a very small subset of tenants could be affected by a noisy neighbor. The potential impact is also minimized since each affected tenant maintains access to unaffected queues. As your workloads grow, increasing the number of queues enhances resilience and further reduces the probability of multiple tenants being assigned to the same shard. This significantly lowers the risk of a single point of failure, making shuffle sharding a robust strategy for workload isolation and fault tolerance.

## Proactive detection, automated isolation, sidelining

Many distributed services will have a cohort of tenants with legitimate spiky asynchronous invocation traffic. This can be driven by seasonal factors, such as holiday shopping, or periodical batch processing. Recognizing these as real business needs, not malicious actions, you want to improve service quality for these tenants as well, while maintaining the overall system stability. For example, you can further improve solution performance by continuously monitoring queue depth to detect traffic spikes and route traffic to dynamically allocated dedicated queues. When you use Lambda asynchronous invocations, this internal complexity is managed for you by the service, ensuring seamless consumption experience.

[![Tenant D is automatically reallocated to a dedicated queue.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-10.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-10.png)

Figure 9. Tenant D is automatically reallocated to a dedicated queue

## Resilience and failure handling

“Everything fails, all the time” is a [famous quote](https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html) from Amazon’s Chief Technology Officer Werner Vogels. Lambda’s distributed and resilient architecture is built to withstand potential outages of its dependencies and internal components to limit the fallout for customers. Specifically for asynchronous invocation processing, the frontend service builds a processing backlog during an outage, allowing the backend to gradually recover without losing any in-flight messages.

[![Lambda service maintains resilience during component outage.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-11.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/03/17/billioninvokes-11.png)

Figure 10. Lambda service maintains resilience during component outage

Upon recovery, the service gradually ramps up the traffic to process the accumulated backlog. During this time, automated mechanisms are in place to coordinate between system components, preventing inadvertently [DDoSing](https://en.wikipedia.org/wiki/Denial-of-service_attack) itself.

To further improve the recovery ramp-up process and provide a smooth restoration of normal operations, the Lambda service uses [load-shedding technique](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/) to ensure fair resource allocation during recovery. While trying to drain the backlog as fast as possible, the service ensures that no single customer ends up consuming an outsized share of the available resources. Adopting such techniques can help you to improve your mean-time-to-recovery ([MTTR](https://en.wikipedia.org/wiki/Mean_time_to_recovery)).

## Observability for asynchronous invocations processing

When using the Lambda service for asynchronous processing, you want to monitor your invocations for situational awareness and potential slowdowns. Use [metrics](https://aws.amazon.com/blogs/compute/introducing-new-asynchronous-invocation-metrics-for-aws-lambda/) such as **AsyncEventReceived, AsyncEventAge**, and **AsyncEventDropped** to get insights about internal processing.

**AsyncEventReceived** tracks the number of async invocations the Lambda service was able to successfully queue for processing. A drop in this metric indicates that invocations are not being delivered to the Lambda service and you should check your invocation source. Potential issues include misconfigurations, invalid [access permissions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-permissions.html), or throttling. Check your invocation source configuration, logs, and the [function resource policy](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) for further analysis.

**AsyncEventAge** tracks how long has a message spent in the internal queue before being processed by a function. This metric increases when async invocations processing is delayed due to insufficient concurrency, execution failures, or throttles. Increase your function concurrency to process more asynchronous invocations at a time and optimize function performance for better throughput, i.e. by increasing memory allocation to add more vCPU capacity. Experiment with adjusting batch size to enable functions to process more messages at a time. Use [invocation logs](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html) to identify whether the problem is caused by function code throwing exceptions. Check [Throttles and Errors](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#invocation-metrics) metrics for further analysis.

**AsyncEventDropped** tracks the number of messages in the internal queue that were dropped because Lambda could not process them. This can be due to throttling, exceeding number of retries, exceeding maximum message age, or function code throwing an exception. [Configure OnFailure destination or a dead-letter queue](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html) to avoid losing data and save dropped messages for re-processing. Use function logs and metrics described above to investigate whether you can address the issue by increasing function concurrency or allocating more memory.

By monitoring these metrics and addressing the underlying issues, you can ensure that your Lambda functions run smoothly, with minimal event processing delays and failures. You can also [enable AWS X-Ray tracing](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html) to capture Lambda service traces. The **AWS::Lambda** trace segment captures the breakdown of the time that Lambda service spends routing requests to internal queues, the time a message spends in a queue, and the time before a function is invoked. This is a powerful tool to get insights into Lambda’s internal processing.

## Conclusion

AWS Lambda processes tens of trillions of monthly invocations across more than 1.5 million active customers, demonstrating its exceptional scalability and resilience. Gaining an understanding of the underlying mechanisms of AWS services like Lambda enables you to proactively address potential challenges in your own applications. By learning how these services handle traffic, manage resources, and recover from failures, you can incorporate similar capabilities into your own solutions. For instance, leveraging Lambda’s asynchronous invocation metrics allows you to optimize workflow performance. This knowledge empowers you to implement strategies such as automated scaling, proactive monitoring, and graceful recovery during outages.

See below resources to learn about using queues and shuffle sharding at scale at Amazon

* [Avoiding insurmountable queue backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/)
* [Workload isolation using shuffle-sharding in Route53](https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding)
* [Improve workload resiliency using shuffle sharding](https://d1.awsstatic.com/events/reinvent/2021/Improve_workload_resiliency_using_shuffle_sharding_ARC308.pdf)
* [Shuffle Sharding: Massive and Magical Fault Isolation](https://aws.amazon.com/blogs/architecture/shuffle-sharding-massive-and-magical-fault-isolation/)

To learn more about Serverless architectures and asynchronous Lambda invocation patterns, see [Serverless Land](https://serverlessland.com/).

TAGS: [contributed](https://aws.amazon.com/blogs/compute/tag/contributed/), [serverless](https://aws.amazon.com/blogs/compute/tag/serverless/)

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