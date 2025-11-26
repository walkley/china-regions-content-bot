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

## [AWS Contact Center](https://aws.amazon.com/blogs/contact-center/)

# Analyze customer satisfaction scores with post-contact surveys using Amazon Connect Tasks

by Aurelien Plancque and Enid Zambrano on 12 NOV 2025 in [\*Post Types](https://aws.amazon.com/blogs/contact-center/category/post-types/ "View all posts in *Post Types"), [Amazon Connect](https://aws.amazon.com/blogs/contact-center/category/messaging/amazon-connect/ "View all posts in Amazon Connect"), [Contact Lens for Amazon Connect](https://aws.amazon.com/blogs/contact-center/category/messaging/amazon-connect/contact-lens/ "View all posts in Contact Lens for Amazon Connect"), [Messaging](https://aws.amazon.com/blogs/contact-center/category/messaging/ "View all posts in Messaging"), [Technical How-to](https://aws.amazon.com/blogs/contact-center/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/contact-center/analyze-customer-satisfaction-scores-with-post-contact-surveys-using-amazon-connect-tasks/) Share

Customer satisfaction (CSAT) is one of the top metrics used to measure the customer’s perceptions after an interaction in your contact center. CSAT post-call surveys are important as a diagnostic tool to fine-tune the experience and service delivered in a contact center. They not only assess perceptions of experiences, but also help an organization understand customer motivations and intentions following the experience.

Amazon Connect is an omnichannel contact center offering voice, chat, and tasks. Amazon Connect Tasks allow you to create activities and integrate with external applications or services to prioritize, assign, and track agent tasks to completion. Using Amazon Connect Tasks can ensure that customer issues are quickly resolved, leading to increased customer satisfaction.

In this blog post, you will learn how to configure a post contact survey for your Amazon Connect contact center, assign a task with the survey results to a supervisor queue, and administer your surveys with a secure web application. Contact center managers can then identify customer issues in nearly real-time, and act in a timely manner to improve customer satisfaction.

## Overview of solution

![architecture](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/05/Architecture-1024x677.png)

The architecture and flow diagram of this solution shows the offering of a post-call survey to a customer, and sharing the survey results using a Task to a supervisor:

1. [Amazon S3](https://aws.amazon.com/s3/) stores and serves the frontend static content through [Amazon CloudFront](https://aws.amazon.com/cloudfront/) and restricted by [Amazon Cognito](https://aws.amazon.com/cognito/) for user management
2. The required [Contact Flow Module](https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-flows.html) is deployed in the Amazon Connect instance
3. Administrators use the web application to define contact surveys according to their needs
4. The configuration of the surveys is stored in [Amazon DynamoDB](https://aws.amazon.com/dynamodb)
5. When required, the [Contact Flow Module](https://docs.aws.amazon.com/connect/latest/adminguide/contact-flow-modules.html) is invoked for a contact, with a contact attribute set to identify the survey to be offered
6. The Contact Flow Module retrieves the configuration of the survey for the contact.
7. The contact is offered the survey, and the survey is answered
8. Results are stored in an Amazon DynamoDB table for the individual contact and if required, an [Amazon Connect Task](https://docs.aws.amazon.com/connect/latest/adminguide/tasks.html) is created

Post contact surveys can be played reactively after a customer contact (inbound voice, outbound voice), or proactively, in combination with the [StartOutboundContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundVoiceContact.html) API.

The source code of this solution can be found on GitHub: [Contact Surveys for Amazon Connect](https://github.com/aws-samples/amazon-connect-contact-surveys).

### Prerequisites

For this blog post, you should have knowledge or and access to the following AWS Services and features:

* [AWS account](https://console.aws.amazon.com/console/home) with permission to create and modify AWS Identity and Access Management (IAM) roles
* [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)
* An existing [Amazon Connect](https://aws.amazon.com/connect/) instance with at least one agent configured
* [Amazon Lex](https://aws.amazon.com/lex/)
* [Amazon S3](https://aws.amazon.com/s3/)
* [Amazon DynamoDB](https://aws.amazon.com/dynamodb)
* [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
* [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
* [Amazon Cognito](https://aws.amazon.com/cognito/)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [AWS CloudFormation](https://aws.amazon.com/cloudformation/)

## Setting up the solution

1. Click on the “Launch Stack” button to deploy the solution in your preferred Region. This will be the same Region that was used to deploy your Amazon Connect instance.[![launch stack](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/05/cloudformation-launch-stack-1.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-contact-center-blog.s3.us-west-2.amazonaws.com/amazon-connect-post-call-surveys/contact-surveys-amazon-connect.yaml&stackName=amazon-connect-surveys-solution)
2. **Provide** the required parameters:

   – **Stack name**

   – **Email address** for the initial user of the solution

   – **ARN of the Amazon Connect instance** you want to use with this solution

   – **Alias of the Amazon Connect instance** you want to use with this solution

   – **Id of the Contact Flow** to which tasks created by this solution will be sent**Note:** If you are unsure about which Contact Flow to choose to process the tasks generated by the solution, use the ID of the Sample inbound flow (first contact experience) available by default in your Amazon Connect instance.![cloudformation](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/05/Picture-1.png)
3. Choose **Next**.
4. Proceed with the stack creation steps, and choose **Next**.
5. **Review** your stack summary. Select **“I acknowledge that AWS CloudFormation might create IAM resources”**.
6. Choose **Submit**.

   **Note:** It will take approximately 5 minutes for the stack to complete the deployment. You will receive an email containing your username and a temporary password.![cloudformation deploy](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/05/Picture-2.png)

   ![email](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/05/Picture-3.png)
7. Once the stack is deployed, in the Output tab, note the value of the AdminUser and the URL of the application.![cloudformation output](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/05/Picture-4.png)
8. Navigate the URL noted previously from the Output tab. Log in to the application with the AdminUser collected previously, and the password received via email during the stack deployment.
9. Choose Login.

   Note: You will be required to change your password at first login.![login screen](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/05/Picture-5.png)
10. If you see the following screen, the solution has been successfully deployed.![application](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/05/Picture-6.png)

### Test your Solution

The following examples will help you understand how you can use this solution for typical use cases.

#### Basic post contact survey, with low score flagged for review

In this example, you will learn to implement a basic post-contact survey that alerts a supervisor through an Amazon Connect Task every time a customer replies to a given question with a low score.

1. **Create a new survey** using the Contact Surveys for Amazon Connect application deployed with the solution:![Survey Configuration](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/10/Picture-11.png)
2. Add a couple of questions to your survey:![survey questions](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/10/Picture-12.png)
3. For one of these questions, select **Additional settings**.
4. Select **Flag for review**, and define the threshold:![adding question flag](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/10/Picture-13.png)

   Any contact that inputs a score lower than the defined threshold to that question will initiate a task in Amazon Connect. This task will be routed through the Contact Flow defined when the solution was deployed.
5. Choose **Save**.
6. Refresh the list, and note the **Id** of your new survey.![survey id](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/10/Picture-14.png)

   **Note:** The Id of your survey will be different than the one on the screenshot.
7. In your Amazon Connect instance, create a new Contact Flow.
8. Import the **Survey Example Disconnect** flow.
9. Before publishing, make sure that the **Invoke module** block is pointing to the **Contact Survey** module available in your Amazon Connect instance.![survey module](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/10/Picture-15.png)
10. Repeat the previous three steps to import the **Simple Survey with flag** flow. Do not publish it yet, you must first make some configuration adjustments.
11. Locate the **Set Disconnect Flow** block. Configure this block to set the disconnect flow to the **Survey Example Disconnect** flow imported previously.![Disconnect Flow](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/10/Picture-16.png)
12. Locate the **Set Contact Attributes** block. This block sets a single **surveyId** contact attribute.
13. Paste the **id** of your survey (noted previously) in the **Value** field of the **surveyId** contact attribute.![survey id](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/10/Picture-17.png)

    **Note:** By setting a surveyId statically, the choice of survey will be static. Alternatively, you could also set this attribute dynamically based on, for example, a value stored in a contact attribute.
14. Choose **Save**.
15. **Publish** the flow.**Note:** Contacts processed by this flow will be queued on the BasicQueue, which is available in your Amazon Connect instance. If you want to run the test with a different queue, adjust the **Set working queue** block accordingly.
16. Associate the **Simple Survey Example** contact flow to any available DID for testing.
17. Call the number that you have selected for testing. Make sure you have an agent available in the queue where the call is going to be directed.
18. While the customer stays on the line, the agent must disconnect the call. The customer will be directed to the survey.
19. The customer hears the first survey question, and must answer 3 (a score lower or equal to the threshold defined previously).
20. For the second question, the customer **enters any digit between 0 and 5**.
21. Since the customer has given a low score to the first question, a task is created for a supervisor to review. This task is processed by the Contact Flow defined during the deployment of the solution.
22. The task is received by a supervisor and contains the details of the interaction that was poorly rated.![task](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/10/Picture-18.png)

#### Visualizing survey results

You can visualize the aggregated results for your survey using the Contact Surveys for Amazon Connect application.

1. Navigate to the URL noted when the solution was deployed and login using the username and password defined earlier.
2. To view a survey’s results, select it from the list, and select the **Results** tab:![results](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/10/Picture-19.png)

   The aggregated results for each question will be available in a pie chart. These can be filtered by date range if necessary.![aggregated results](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/10/Picture-20.png)
3. To export the individual results for a survey, click the **Export** button to generate a csv file containing the individual results for each survey offered to customers, along with the contactId of the interaction.

## Cleaning up

1. Navigate to CloudFormation, and select the stack you created when deploying the solution
2. Select **Delete**
3. If a new DID was claimed to test the solution, release the DID in Amazon Connect to avoid future charges

## Conclusion

Post call survey is one of the most important metrics to measure customer satisfaction (CSAT) in a contact center, as it gathers feedback from a customer immediately after their interaction with your contact center. It is critical to present the post call survey immediately after the customer interaction in order to capture the customer experience while it is still fresh. Also, incorporating Amazon Tasks allows you to present in nearly real time the results of a post-call survey to a supervisor to take immediate action on the customer experience. In this blog, we have presented a solution to create a post-call survey and alert on negative responses in near real-time. To find other AWS solutions that will help you deliver better customer experiences, subscribe today to the following GitHub repositories:

* <https://github.com/aws-samples/>
* <https://github.com/amazon-connect>

|  |  |
| --- | --- |
| ![](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/10/ap.png) | Aurelien Plancque is a Solutions Architect, specialising in Amazon Connect / Customer Experience at AWS, with over 12 years of experience in designing and building software for contact center solutions. |
| ![](https://d2908q01vomqb2.cloudfront.net/af3e133428b9e25c55bc59fe534248e6a0c0f17b/2023/04/10/ez.png) | Enid Zambrano is an Amazon Connect Specialist Solution Architect at AWS. Enid is based in Canada with over 25 years optimizing and building contact centers. |

TAGS: [agent](https://aws.amazon.com/blogs/contact-center/tag/agent/), [amazon](https://aws.amazon.com/blogs/contact-center/tag/amazon/), [CCaaS](https://aws.amazon.com/blogs/contact-center/tag/ccaas/), [center](https://aws.amazon.com/blogs/contact-center/tag/center/), [Connect](https://aws.amazon.com/blogs/contact-center/tag/connect/), [contact](https://aws.amazon.com/blogs/contact-center/tag/contact/), [customer](https://aws.amazon.com/blogs/contact-center/tag/customer/), [service](https://aws.amazon.com/blogs/contact-center/tag/service/)

### Resources

* [Getting Started](https://aws.amazon.com/connect?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=contactcenter-resources#Getting_Started_with_Amazon_Connect)
* [Amazon Connect User Guide](https://github.com/awsdocs/amazon-connect-user-guide)
* [Amazon Connect Admin Guide](https://github.com/awsdocs/amazon-connect-admin-guide)
* [Amazon Connect Streams API](https://github.com/aws/amazon-connect-streams)
* [Amazon Connect Partners](https://aws.amazon.com/solutionspace/contact-center?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=contactcenter-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=contactcenter-social)

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