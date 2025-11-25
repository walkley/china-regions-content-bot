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

# AWS Lambda standardizes billing for INIT Phase

by Shubham Gupta and Jeff Gebhart on 29 APR 2025 in [Announcements](https://aws.amazon.com/blogs/compute/category/post-types/announcements/ "View all posts in Announcements"), [AWS Lambda](https://aws.amazon.com/blogs/compute/category/compute/aws-lambda/ "View all posts in AWS Lambda"), [Intermediate (200)](https://aws.amazon.com/blogs/compute/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [Serverless](https://aws.amazon.com/blogs/compute/category/serverless/ "View all posts in Serverless") [Permalink](https://aws.amazon.com/blogs/compute/aws-lambda-standardizes-billing-for-init-phase/) Share

Effective August 1, 2025, AWS will standardize billing for the initialization (INIT) phase across all [AWS Lambda](https://aws.amazon.com/lambda/) function configurations. This change specifically affects on-demand invocations of Lambda functions packaged as ZIP files that use managed runtimes, for which the INIT phase duration was previously unbilled. This update standardizes billing of the INIT phase across all runtime types, deployment packages, and invocation modes. Most users will see minimal impact on their overall Lambda bill from this change, as the INIT phase typically occurs for a very small fraction of function invocations. In this post, we discuss the Lambda Function Lifecycle and upcoming changes to INIT phase billing. You will learn what happens in the INIT phase and when it occurs, how to monitor your INIT phase duration, and strategies to optimize this phase and minimize costs.

## Understanding the Lambda function execution lifecycle

The [Lambda function execution lifecycle](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html#runtimes-lifecycle) consists of three distinct phases: INIT, INVOKE, and SHUTDOWN. The INIT phase is triggered during a “cold start” when Lambda creates a new execution environment for a function in response to an invocation. This is followed by the INVOKE phase where the request is processed, and finally, the SHUTDOWN phase where the execution environment is terminated. For a summary of the execution lifecycle, watch [AWS Lambda execution environment lifecycle](https://www.youtube.com/watch?v=E20B8Izr5fI).

During the INIT phase, Lambda performs a series of preparatory steps within a maximum duration of 10 seconds. The service retrieves the function code from an internal [Amazon S3](https://aws.amazon.com/s3/) bucket, or from [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) (Amazon ECR) for functions using container packaging. Then, it configures an environment with the specified memory, runtime, and other settings. When the execution environment is prepared, Lambda executes four key tasks in sequence:

1. Initiate any extensions configured (Extension INIT)
2. Bootstrap the runtime (Runtime INIT)
3. Execute the function’s static code (Function INIT)
4. Run any before-checkpoint runtime hooks (applicable only for Lambda SnapStart)

[![](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/04/28/ComputeBlog-2339-img1.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/04/28/ComputeBlog-2339-img1.png)

## Understanding the billing changes

Lambda charges are based on the number of requests and the duration it takes for the code to run. The duration is calculated from the moment the function [code begins running until it completes or terminates](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/), rounded up to the nearest millisecond. Duration cost depends on the amount of memory that you allocate to your function.

Previously, the INIT phase duration wasn’t included in the Billed Duration for functions using managed runtimes with ZIP archive packaging, as evidenced in [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) logs:

```
REPORT RequestId: xxxxx   Duration: 250.06 ms  Billed Duration: 251 ms  Memory Size: 1024 MB
Max Memory Used: 350 MB   Init Duration: 100.77 ms
```

However, functions configured with [custom runtimes](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html), [Provisioned Concurrency (PC)](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html), or [OCI packaging](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html) already included the INIT phase duration in their Billed Duration. Effective August 1, 2025, INIT phase will be billed across all configuration types and the INIT phase duration will be included in the Billed Duration for on-demand invocations of functions using managed runtimes with ZIP archive packaging as well. After this change, the REPORT Request ID log line will show the following:

```
REPORT RequestId: xxxxx   Duration: 250.06 ms  Billed Duration: 351 ms  Memory Size: 1024 MB
Max Memory Used: 350 MB   Init Duration: 100.77 ms
```

The further INIT phase duration charges will follow the standard on-demand duration pricing that is specific to each [AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), which can be found on the [Lambda pricing page](https://aws.amazon.com/lambda/pricing/). For [AWS Lambda@Edge](https://aws.amazon.com/lambda/edge/) functions, the INIT phase duration will be billed according to Lambda@Edge duration rates.

## Finding the INIT phase duration and impact to Lambda billing

You can already monitor the time spent in the INIT phase of your function invocations through the “REPORT RequestId” log line within CloudWatch Logs, which includes the “Init Duration” value. Alternatively, if Lambda Insights is enabled, you can use the “init\_duration” CloudWatch metric. These tools offer valuable insights into the INIT time of Lambda functions, which will now be factored into billing calculations.

For a more comprehensive analysis, you can use the following CloudWatch Log Insights query to generate a detailed report estimating the previously unbilled duration of the INIT phase. The query helps you understand the proportion of the unbilled INIT phase time relative to your overall Lambda usage, enabling more accurate cost projections following this billing change.

```
filter @type = "REPORT"
| stats
    sum((@memorySize/1000000/1024) * (@billedDuration/1000)) as BilledGBs,
    sum((@memorySize/1000000/1024) * ((@duration + @initDuration - @billedDuration)/1000)) as UnbilledInitGBs,
    UnbilledInitGBs / (UnbilledInitGBs + BilledGBs) as UnbilledInitRatio
```

The CloudWatch Log Insights query provides three essential metrics:

1. **BilledGBs**: Represents the total GB-s (gigabyte-seconds) currently being billed for the chosen log groups.
2. **UnbilledInitGBs**: Shows the total GB-s consumed during INIT phase that was previously not included in billing.
3. **Ratio**: Indicates the percentage of total GB-s attributed to previously unbilled INIT phase duration.

[![](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/04/28/ComputeBlog-2339-img2-v2.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/04/28/ComputeBlog-2339-img2-v2.png)

Using these existing monitoring capabilities allows you to proactively assess and optimize your Lambda function INIT times, potentially minimizing the impact of the new billing structure on your overall costs.

## Understanding and optimizing Lambda INIT phase

The Lambda INIT phase is triggered in two specific scenarios: during the creation of a new execution environment and when a function scales up to meet demand. This INIT code runs only during these “cold starts” and is bypassed during subsequent invocations that use existing warm environments. After the INIT phase, Lambda runs the function handler code to process the invocation.

Following the handler execution, Lambda freezes the execution environment. To improve resource management and performance, the Lambda service retains the execution environment for a non-deterministic period of time. During this time, if another request arrives for the same function, then the service may reuse the environment. This second request typically finishes faster, because the execution environment already exists and it isn’t necessary to download the code and run the INIT code. This is called a “warm start.”

Developers can use the INIT phase to create, initialize, and configure objects expected to be reused across multiple invocations during function INIT instead of doing it in the handler. Initializing the dependencies/shared objects upfront reduces the latency of subsequent invocations. For example:

* Download more libraries or dependencies
* Establish client connections to other AWS services such as Amazon S3 or [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
* Create database connections to be shared across invocations
* Retrieve application parameters or secrets from [Amazon Systems Manager](https://aws.amazon.com/systems-manager/) Parameter Store or [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)

When developing Lambda functions, it’s important to strategically decide what code runs during the INIT phase as opposed to the handler phase, because it affects both performance and costs.

### Optimizing package/library size

The INIT phase includes creating an execution environment, downloading the function code and initializing it. Three main factors influence its performance:

1. The size of the function package, in terms of imported libraries and dependencies, and Lambda layers.
2. The amount of code and INIT work.
3. The performance of libraries and other services in setting up connections and other resources.

Larger function packages increase code download times. You can decrease INIT phase duration by reducing package size, resulting in faster cold starts and lower INIT costs. Furthermore, optimizing loading of libraries can also significantly impact package size. Tools such as [esbuild](https://esbuild.github.io/) can further optimize performance by minifying and bundling packages. For details, read [Reduce Lambda cold start times: migrate to AWS SDK for JavaScript v3](https://aws.amazon.com/blogs/developer/reduce-lambda-cold-start-times-migrate-to-aws-sdk-for-javascript-v3/).

### Optimizing INIT phase execution and cost efficiency

The frequency of INIT phase executions (or cold starts) directly impacts both performance and cost efficiency. According to an analysis of production Lambda workloads, INITs (cold starts) typically occur in under 1% of invocations—meaning code in the INIT phase may execute just once per hundred invocations.

You can use the INIT phase to perform one-time operations that benefit subsequent invocations. Common optimization patterns include pre-calculating lookup tables or transforming static datasets. For example, downloading static data from Amazon S3 or DynamoDB during INIT, making it available for all subsequent function invocations without repeated downloads.

### Lambda SnapStart

[Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) provides an effective solution for reducing cold start latency and INIT phase costs. When it’s enabled, SnapStart creates a snapshot during the first function INIT and reuses it for subsequent cold starts, eliminating the need for repeated INIT phase executions. This approach is particularly valuable for functions with longer INIT times due to loading module dependencies/frameworks, initializing the runtime, or executing one-time INIT code. SnapStart is supported for Java, .NET, and Python runtimes. You can implement SnapStart through the Lambda console or [AWS Command Line Interface (AWS CLI),](https://aws.amazon.com/cli/) making sure that your code adheres to the [AWS serialization guidelines](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-uniqueness.html) for snapshot restoration compatibility. Using SnapStart allows you to significantly improve function startup times and optimize costs across multiple popular programming languages.

### Provisioned Concurrency

Provisioned Concurrency is a Lambda feature that pre-initializes execution environments before any invocations occur. This proactive approach effectively eliminates the performance impact of the INIT phase on individual function calls, because the INIT is completed in advance.

Although all functions using the Provisioned Concurrency benefit from reduced startup times as compared to on-demand execution, the impact is particularly pronounced for certain runtime environments. For example, C# and Java functions—which typically experience slower INIT but faster execution times as compared to Node.js or Python—can achieve significant performance gains through this feature. Implementing Provisioned Concurrency allows you to effectively manage both consistent traffic patterns and expected usage spikes, thereby minimizing cold start latency across your serverless applications. This optimization strategy is particularly valuable for functions with complex INIT requirements or those serving latency-sensitive workloads. From a cost optimization perspective, Provisioned Concurrency is most suitable for workloads with sustained usage patterns above 60% usage, because this typically provides better cost efficiency compared to on-demand execution.

## Conclusion

Effective August 1, 2025, AWS is standardizing the INIT phase billing for AWS Lambda. AWS provides multiple ways for you to optimize both the performance and costs of your Lambda functions. Whether you’re using SnapStart, implementing Provisioned Concurrency, or optimizing INIT code, we recommend working closely with AWS support teams to identify the most suitable optimization approach for your specific workload requirements.

For more support and guidance, consider participating in [AWS Cost Optimization workshops](https://workshops.aws/categories/Cost%20Optimization) or consulting the [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).

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