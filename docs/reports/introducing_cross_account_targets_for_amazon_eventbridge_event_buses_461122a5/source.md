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

# Introducing cross-account targets for Amazon EventBridge Event Buses

by Chris McPeek on 21 JAN 2025 in [Amazon EventBridge](https://aws.amazon.com/blogs/compute/category/application-integration/amazon-eventbridge/ "View all posts in Amazon EventBridge"), [Amazon Simple Notification Service (SNS)](https://aws.amazon.com/blogs/compute/category/messaging/amazon-simple-notification-service-sns/ "View all posts in Amazon Simple Notification Service (SNS)"), [Amazon Simple Queue Service (SQS)](https://aws.amazon.com/blogs/compute/category/messaging/amazon-simple-queue-service-sqs/ "View all posts in Amazon Simple Queue Service (SQS)"), [AWS Identity and Access Management (IAM)](https://aws.amazon.com/blogs/compute/category/security-identity-compliance/aws-identity-and-access-management-iam/ "View all posts in AWS Identity and Access Management (IAM)"), [AWS Lambda](https://aws.amazon.com/blogs/compute/category/compute/aws-lambda/ "View all posts in AWS Lambda"), [AWS Serverless Application Model](https://aws.amazon.com/blogs/compute/category/compute/aws-serverless-application-model/ "View all posts in AWS Serverless Application Model"), [Serverless](https://aws.amazon.com/blogs/compute/category/serverless/ "View all posts in Serverless") [Permalink](https://aws.amazon.com/blogs/compute/introducing-cross-account-targets-for-amazon-eventbridge-event-buses/) Share

*This post is written by Anton Aleksandrov, Principal Solutions Architect, Serverless and Alexander Vladimirov, Senior Solutions Architect, Serverless*

Today, [Amazon EventBridge](https://aws.amazon.com/eventbridge/) is announcing support for cross-account targets for Event Buses. This new capability allows you to send events directly to targets, such as [Amazon Simple Queue Service (Amazon SQS](https://aws.amazon.com/sqs/)), [AWS Lambda](https://aws.amazon.com/lambda/), and [Amazon Simple Notification Service (Amazon SNS](https://aws.amazon.com/sns/)), located in other accounts.

Previously, EventBridge supported cross-account event delivery from an event bus in one account to an event bus in another account. This launch extends that capability and allows you to configure the source event bus to deliver events directly to all EventBridge supported targets in other accounts, not just event buses. This removes the need for an additional event bus in the target account.

**Overview**

Event-driven architectures built with EventBridge allow you to create solutions spanning many company departments and business domains, while remaining asynchronous and loosely coupled. As solutions grow, you may need to send events across account boundaries.

For example, you may have a set of event buses hosted in multiple accounts that are dispatching security-related events to an Amazon SQS queue hosted in a centralized account for further asynchronous processing and analysis.

Previously, EventBridge rules allowed you to define targets in the same account. The only target type that supported cross-account event delivery was another event bus. If you wanted to send events across account boundaries, you had to create event buses in both source and target accounts. After, you would configure a rule on the source event bus to send events to the target bus, and another rule on the target event bus to deliver the event to a desired target in the target account. Alternatively, a Lambda function or SNS topic could be used as a bridging mechanism to send events across accounts.

The following diagram illustrates what an architecture of cross-account event delivery looked like before the new capability. A “bridging” component, like another event bus, SNS topic, or Lambda function, was required to send events from one account to another.

[![Delivering cross-account events from source bus to target bus.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/1-cross-account-targets.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/1-cross-account-targets.png)

*Figure 1: Delivering cross-account events from source bus to target bus*

With this new EventBridge feature, you can deliver events from the source event bus to the desired targets in different accounts directly. This simplifies the architecture and persmission model. It also reduces latency in your event-driven solutions by having fewer components processing events along the path from source to targets.

[![Delivering cross-account events to target directly.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/2-cross-account-targets.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/2-cross-account-targets.png)

*Figure 2: Delivering cross-account events to target directly*

## Configuring EventBridge delivery rule targets for cross-account event delivery

Enabling cross-account event delivery should be done with security in mind. You must establish mutual trust between the source and the target. Source event bus rules must have an [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam) role that allows them to send events to specific targets. This is achieved by attaching an execution role to the delivery rule targets.

Event delivery targets hosted in different accounts must have a resource access policy attached that explicitly allows receiving events from the execution role used in the source account. Due to this requirement, you can enable cross-account event delivery only for targets that support resource access policies, such as Amazon SQS queues, Amazon SNS topics, and AWS Lambda functions.

Having both an IAM role in the source account and resource policy in the target account allows you to have fine-grained control over which principals are allowed to use the PutEvents action and under which conditions. You can define [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCPs) to set organizational boundaries determining who can send and receive events in your organization.

As illustrated in the following diagram, consider Team A owns the source account (Account A). Team A is responsible for setting up the source event bus, its execution role, rules, and targets. Teams B and C own the target accounts (Account B and Account C, accordingly). Both teams manage their respective target accounts. For example, creating delivery targets, such as SQS queues, and granting permissions to accept events from the event bus in the source account. This approach enables Team A to manage the centralized source event bus for other teams, and Teams B and C to control who can send events to their targets. It provides high degree of overall control and governance.

[![A cross-team collaboration sending events from source account to target account targets.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/3-cross-account-targets.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/3-cross-account-targets.png)

*Figure 3: A cross-team collaboration sending events from source account to target account targets*

The following example describes setting up cross-account event delivery to an SQS queue. You can apply the same technique to other target types as well, such as Lambda functions or SNS topics.

See the following diagram for a conceptual architectural layout and resource creation order.

[![Permissions required for cross-account event delivery.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/4-cross-account-targets.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/4-cross-account-targets.png)

*Figure 4: Permissions required for cross-account event delivery*

Assuming the source event bus already exists, there are three general steps in setting up cross-account event delivery:

1. Target account – create the delivery target, such as an SQS queue.
2. Source account – configure a rule for cross-account event delivery. Set the target SQS queue ARN as rule target, and attach an execution role with permissions to send messages to the target SQS Queue.
3. Target account – apply a resource policy to the target SQS queue allowing the source event bus execution role to send events.

## Showing cross-account delivery in action

Follow the instructions in this [GitHub](https://github.com/aws-samples/eventbridge-cross-account-targets) repository for provisioning the sample in your AWS accounts using [AWS Serverless Application Model (AWS SAM)](https://aws.amazon.com/serverless/sam/). An event bus rule in the source account sends events directly to an SQS queue, a Lambda function, and an SNS topic in a target account. You must have two accounts for the sample to work.

[![The sample project architecture, delivering events cross-account to Lambda, SQS, and SNS. ](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/5-cross-account-targets.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/5-cross-account-targets.png)

*Figure 5: The sample project architecture, delivering events cross-account to Lambda, SQS, and SNS.*

Make sure you enter a valid email address as SnsSubscriptionEmail value and confirm your email subscription once target stack is deployed.

After deployment, open the EventBridge console in the source account. Navigate to the newly created event bus, which has “SourceEventBus” in its name. Use the *Send Events* functionality to publish sample events, as shown in the following screenshot. Make sure that the *Source* of your events is set to “test”.

[![Sending test event.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/6-cross-account-targets.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/6-cross-account-targets.png)

*Figure 6: Sending test event*

Validate that the events are successfully delivered to all three cross-account targets. Open the target account in a different browser or an incognito window:

1. Navigate to the SQS console. Open the newly created queue, which has “TargetSqsQueue” in its name.
2. Choose **Send and Receive messages** then choose **Poll for messages**. You can see the events sent in the previous step.[![Receiving test event with SQS.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/7-cross-account-targets.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/7-cross-account-targets.png)**Figure 7: Receiving test event with SQS**
3. Navigate to [Amazon CloudWatch Logs](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html). Open the Log Group for the newly created Lambda function, which has “TargetLambdaFunction” in its name. It shows events sent in the previous step.

   [![Receiving test event with Lambda.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/8-cross-account-targets.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/8-cross-account-targets.png)**Figure 8: Receiving test event with Lambda**
4. Check your email. If you have confirmed the SNS topic subscription during the sample code deployment, it shows the events sent in the previous step.[![Receiving test event with SNS.](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/9-cross-account-targets.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2024/11/20/9-cross-account-targets.png)*Figure 9: Receiving test event with SNS*

## Conclusion

The new EventBridge capability allows you to deliver events directly to targets across account boundaries. This capability helps to simplify your event-driven architectures, as well as improve latency by reducing the number of components processing your events as they travel from event buses to their destinations.

Refer to the [EventBridge pricing page](https://aws.amazon.com/eventbridge/pricing/) to learn more about cross-account events delivery costs.

For additional documentation, refer to [Amazon EventBridge documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html). Get the sample code used in this blog from this [GitHub](https://github.com/aws-samples/eventbridge-cross-account-targets) repository.

For more serverless learning resources, visit [Serverless Land](https://serverlessland.com/).

TAGS: [serverless](https://aws.amazon.com/blogs/compute/tag/serverless/)

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