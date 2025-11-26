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

# Introducing Amazon Application Recovery Controller Region switch: A multi-Region application recovery service

by [Sébastien Stormacq](https://aws.amazon.com/blogs/aws/author/stormacq/ "Posts by Sébastien Stormacq") on 01 AUG 2025 in [Amazon Application Recovery Controller (ARC)](https://aws.amazon.com/blogs/aws/category/networking-content-delivery/amazon-application-recovery-controller/ "View all posts in Amazon Application Recovery Controller (ARC)"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Resilience](https://aws.amazon.com/blogs/aws/category/resilience/ "View all posts in Resilience") [Permalink](https://aws.amazon.com/blogs/aws/introducing-amazon-application-recovery-controller-region-switch-a-multi-region-application-recovery-service/)  [Comments](https://aws.amazon.com/blogs/aws/introducing-amazon-application-recovery-controller-region-switch-a-multi-region-application-recovery-service/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

As a developer advocate at AWS, I’ve worked with many enterprise organizations who operate critical applications across multiple [AWS Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region). A key concern they often share is the lack of confidence in their Region failover strategy—whether it will work when needed, whether all dependencies have been identified, and whether their teams have practiced the procedures enough. Traditional approaches often leave them uncertain about their readiness for Regional switch.

Today, I’m excited to announce [Amazon Application Recovery Controller (ARC)](https://aws.amazon.com/application-recovery-controller/) Region switch, a fully managed, highly available capability that enables organizations to plan, practice, and orchestrate Region switches with confidence, eliminating the uncertainty around cross-Region recovery operations. Region switch helps you orchestrate recovery for your multi-Region applications on AWS. It gives you a centralized solution to coordinate and automate recovery tasks across AWS services and accounts when you need to switch your application’s operations from one AWS Region to another.

Many customers deploy business-critical applications across multiple AWS Regions to meet their availability requirements. When an operational event impacts an application in one Region, switching operations to another Region involves coordinating multiple steps across different AWS services, such as compute, databases, and DNS. This coordination typically requires building and maintaining complex scripts that need regular testing and updates as applications evolve. Additionally, orchestrating and tracking the progress of Region switches across multiple applications and providing evidence of successful recovery for compliance purposes often involves manual data gathering.

Region switch is built on a Regional data plane architecture, where Region switch plans are executed from the Region being activated. This design eliminates dependencies on the impacted Region during the switch, providing a more resilient recovery process since the execution is independent of the Region you’re switching from.

**Building a recovery plan with ARC Region switch** With ARC Region switch, you can create recovery plans that define the specific steps needed to switch your application between Regions. Each plan contains execution blocks that represent actions on AWS resources. At launch, Region switch supports nine types of execution blocks:

* ARC Region switch plan execution block–let you orchestrate the order in which multiple applications switch to the Region you want to activate by referencing other Region switch plans.
* [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) execution block–Scales Amazon EC2 compute resources in your target Region by matching a specified percentage of your source Region’s capacity.
* ARC [routing controls](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html) execution block–Changes routing control states to redirect traffic using DNS health checks.
* [Amazon Aurora](https://aws.amazon.com/rds/aurora/) global database execution block–Performs database failover with potential data loss or switchover with zero data loss for [Aurora Global Database](https://aws.amazon.com/rds/aurora/global-database/).
* Manual approval execution block–Adds approval checkpoints in your recovery workflow where team members can review and approve before proceeding.
* Custom Action [AWS Lambda](https://aws.amazon.com/lambda/) execution block–Adds custom recovery steps by executing Lambda functions in either the activating or deactivating Region.
* [Amazon Route 53](https://aws.amazon.com/route53/) health check execution block–Let you to specify which Regions your application’s traffic will be redirected to during failover. When executing your Region switch plan, the Amazon Route 53 health check state is updated and traffic is redirected based on your DNS configuration.
* [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/) resource scaling execution block–Scales Kubernetes pods in your target Region during recovery by matching a specified percentage of your source Region’s capacity.
* [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/) resource scaling execution block–Scales ECS tasks in your target Region by matching a specified percentage of your source Region’s capacity.

Region switch continually validates your plans by checking resource configurations and [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) permissions every 30 minutes. During execution, Region switch monitors the progress of each step and provides detailed logs. You can view execution status through the Region switch dashboard and at the bottom of the execution details page.

To help you balance cost and reliability, Region switch offers flexibility in how you prepare your standby resources. You can configure the desired percentage of compute capacity to target in your destination Region during recovery using Region switch scaling execution blocks. For critical applications expecting surge traffic during recovery, you might choose to scale beyond 100 percent capacity, and setting a lower percentage can help achieve faster overall execution times. However, it’s important to note that using one of the scaling execution blocks does not guarantee capacity, and actual resource availability depends on the capacity in the destination Region at the time of recovery. To facilitate the best possible outcomes, we recommend regularly testing your recovery plans and maintaining appropriate [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) in your standby Regions.

ARC Region switch includes a global dashboard you can use to monitor the status of Region switch plans across your enterprise and Regions. Additionally, there’s a Regional executions dashboard that only displays executions within the current console Region. This dashboard is designed to be highly available across each Region so it can be used during operational events.

Region switch allows resources to be hosted in an account that is separate from the account that contains the Region switch plan. If the plan uses resources from an account that is different from the account that hosts the plan, then Region switch uses the `executionRole` to assume the `crossAccountRole` to access those resources. Additionally, Region switch plans can be centralized and shared across multiple accounts using [AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html), enabling efficient management of recovery plans across your organization.

**Let’s see how it works** Let me show you how to create and execute a Region switch plan. There are three parts in this demo. First, I create a Region switch plan. Then, I define a workflow. Finally, I configure the triggers.

**Step 1: Create a plan**

I navigate to the Application Recovery Controller section of the [AWS Management Console](https://console.aws.amazon.com). I choose **Region switch** in the left navigation menu. Then, I choose **Create Region switch plan**.

[![ARC Region switch - 1](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_10-15-47.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_10-15-47.png)

After I give a name to my plan, I specify a **Multi-Region recovery approach** (active/passive or active/active). In Active/Passive mode, two application replicas are deployed into two Regions, with traffic routed into the active Region only. The replica in the passive Region can be activated by executing the Region switch plan.

Then, I select the **Primary Region** and **Standby Region**. Optionally, I can enter a **Desired recovery time objective (RTO)**. The service will use this value to provide insight into how long Region switch plan executions take in relation to my desired RTO.

[![ARC Region switch - create plan](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_10-17-29.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_10-17-29.png)

I enter the **Plan execution IAM role**. This is the role that allows Region switch to call AWS services during execution. I make sure the role I choose has permissions to be invoked by the service and contains the minimum set of permissions allowing ARC to operate. Refer to the [IAM permissions section of the documentation](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_service-with-iam.html) for the details.

[![ARC Region switch - create plan 2](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_10-18-09.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_10-18-09.png)**Step 2: Create a workflow**

When the two **Plan evaluation status** notifications are green, I create a workflow. I choose **Build workflows** to get started.

[![ARC Region switch - status](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_10-18-32.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_10-18-32.png)

Plans enable you to build specific workflows that will recover your applications using Region switch execution blocks. You can build workflows with execution blocks that run sequentially or in parallel to orchestrate the order in which multiple applications or resources recover into the activating Region. A plan is made up of these workflows that allow you to activate or deactivate a specific Region.

For this demo, I use the graphical editor to create the workflow. But you can also define the workflow in JSON. This format is better suited for automation or when you want to store your workflow definition in a source code management system (SCMS) and your infrastructure as code (IaC) tools, such as [AWS CloudFormation](https://aws.amazon.com/cloudformation/).

[![ARC - define workflows](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_10-49-22.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_10-49-22.png)

I can alternate between the **Design** and the **Code** views by selecting the corresponding tab next to the **Workflow builder** title. The JSON view is read-only. I designed the workflow with the graphical editor and I copied the JSON equivalent to store it alongside my IaC project files.

[![ARC - define workflows as code](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_10-49-35.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_10-49-35.png)

Region switch launches an evaluation to validate your recovery strategy every 30 minutes. It regularly checks that all actions defined in your workflows will succeed when executed. This proactive validation assesses various elements, including IAM permissions and resource states across accounts and Regions. By continually monitoring these dependencies, Region switch helps ensure your recovery plans remain viable and identifies potential issues before they impact your actual switch operations.

However, just as an untested backup is not a reliable backup, an untested recovery plan cannot be considered truly validated. While continuous evaluation provides a strong foundation, we strongly recommend regularly executing your plans in test scenarios to verify their effectiveness, understand actual recovery times, and ensure your teams are familiar with the recovery procedures. This hands-on testing is essential for maintaining confidence in your disaster recovery strategy.

**Step 3: Create a trigger**

A trigger defines the conditions to activate the workflows just created. It’s expressed as a set of CloudWatch alarms. Alarm-based triggers are optional. You can also use Region switch with manual triggers.

From the Region switch page in the console, I choose the **Triggers** tab and choose **Add triggers**.

[![ARC - Trigger](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_11-12-54.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_11-12-54.png)

For each Region defined in my plan, I choose **Add trigger** to define the triggers that will activate the Region.[![ARC - Trigger 2](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_11-13-21.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_11-13-21.png)Finally, I choose the alarms and their state (OK or Alarm) that Region switch will use to trigger the activation of the Region.

[![ARC - Trigger 3](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_11-15-20.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/17/2025-07-17_11-15-20.png)

I’m now ready to test the execution of the plan to switch Regions using Region switch. It’s important to execute the plan from the Region I’m activating (the target Region of the workflow) and use the data plane in that specific Region.

Here is how to execute a plan using the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/):

```
aws arc-region-switch start-plan-execution \
--plan-arn arn:aws:arc-region-switch::111122223333:plan/resource-id \
--target-region us-west-2 \
--action activate
```

**Pricing and availability** Region switch is available in all commercial AWS Regions at $70 per month per plan. Each plan can include up to 100 execution blocks, or you can create parent plans to orchestrate up to 25 child plans.

Having seen firsthand the engineering effort that goes into building and maintaining multi-Region recovery solutions, I’m thrilled to see how Region switch will help automate this process for our customers. To get started with ARC Region switch, [visit the ARC console and create your first Region switch plan](https://console.aws.amazon.com/route53recovery/home). For more information about Region switch, visit the [Amazon Application Recovery Controller (ARC) documentation](https://docs.aws.amazon.com/amazonarc/). You can also reach out to your AWS account team with questions about using Region switch for your multi-Region applications.

I look forward to hearing about how you use Region switch to strengthen your multi-Region applications’ resilience.

[— seb](https://linktr.ee/sebsto)

![Sébastien Stormacq](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2023/01/13/AWS-59-cropped.jpg)

### [Sébastien Stormacq](https://aws.amazon.com/blogs/aws/author/stormacq/ "Posts by Sébastien Stormacq")

Seb has been writing code since he first touched a Commodore 64 in the mid-eighties. He inspires builders to unlock the value of the AWS cloud, using his secret blend of passion, enthusiasm, customer advocacy, curiosity and creativity. His interests are software architecture, developer tools and mobile computing. If you want to sell him something, be sure it has an API. Follow @sebsto on Bluesky, X, Mastodon, and others.

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