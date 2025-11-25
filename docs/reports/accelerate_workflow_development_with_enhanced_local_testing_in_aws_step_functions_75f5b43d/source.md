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

# Accelerate workflow development with enhanced local testing in AWS Step Functions

by [Donnie Prakoso](https://aws.amazon.com/blogs/aws/author/donnie/ "Posts by Donnie Prakoso") on 19 NOV 2025 in [Application Integration](https://aws.amazon.com/blogs/aws/category/application-integration/ "View all posts in Application Integration"), [Application Services](https://aws.amazon.com/blogs/aws/category/application-services/ "View all posts in Application Services"), [AWS Step Functions](https://aws.amazon.com/blogs/aws/category/application-services/aws-step-functions/ "View all posts in AWS Step Functions"), [Developer Tools](https://aws.amazon.com/blogs/aws/category/developer-tools/ "View all posts in Developer Tools"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/accelerate-workflow-development-with-enhanced-local-testing-in-aws-step-functions/)  [Comments](https://aws.amazon.com/blogs/aws/accelerate-workflow-development-with-enhanced-local-testing-in-aws-step-functions/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, I’m excited to announce enhanced local testing capabilities for [AWS Step Functions](https://aws.amazon.com/step-functions/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) through the [TestState API](https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el), our testing API.

These enhancements are available through the API, so you can build automated test suites that validate your workflow definitions locally on your development machines, test error handling patterns, data transformations, and mock service integrations using your preferred testing frameworks. This launch introduces an API-based approach for local unit testing, providing programmatic access to comprehensive testing capabilities without deploying to [Amazon Web Services (AWS)](https://aws.amazon.com/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el).

There are three key capabilities introduced in this enhanced TestState API:

* **Mocking support** – Mock state outputs and errors without invoking downstream services, enabling true unit testing of state machine logic. TestState validates mocked responses against AWS API models with three validation modes: STRICT (this is the default and validates all required fields), PRESENT (validates field types and names), and NONE (no validation), providing high-fidelity testing.
* **Support for all state types** – All state types, including advanced states such as Map states (inline and distributed), Parallel states, activity-based Task states, .sync service integration patterns, and .waitForTaskToken service integration patterns, can now be tested. This means you can use TestState API across your entire workflow definition and write unit tests to verify control flow logic, including state transitions, error handling, and data transformations.
* **Testing individual states** – Test specific states within a full state machine definition using the new stateName parameter. You can provide the complete state machine definition one time and test each state individually by name. You can control execution context to test specific retry attempts, Map iteration positions, and error scenarios.

**Getting started with enhanced TestState**

Let me walk you through these new capabilities in enhanced TestState.

**Scenario 1: Mock successful results**

The first capability is mocking support, which you can use to test your workflow logic without invoking actual AWS services or even external HTTP requests. You can either mock service responses for fast unit testing or test with actual AWS services for integration testing. When using mocked responses, you don’t need AWS Identity and Access Management (IAM) permissions.

Here’s how to mock a successful AWS Lambda function response:

```
aws stepfunctions test-state --region us-east-1 \
--definition '{
  "Type": "Task",
  "Resource": "arn:aws:states:::lambda:invoke",
  "Parameters": {"FunctionName": "process-order"},
  "End": true
}' \
--mock '{"result":"{\"orderId\":\"12345\",\"status\":\"processed\"}"}' \
--inspection-level DEBUG
```

This command tests a Lambda invocation state without actually calling the function. TestState validates your mock response against the Lambda service API model so your test data matches what the real service would return.

The response shows the successful execution with detailed inspection data (when using DEBUG inspection level):

```
{
    "output": "{\"orderId\":\"12345\",\"status\":\"processed\"}",
    "inspectionData": {
        "input": "{}",
        "afterInputPath": "{}",
        "afterParameters": "{\"FunctionName\":\"process-order\"}",
        "result": "{\"orderId\":\"12345\",\"status\":\"processed\"}",
        "afterResultSelector": "{\"orderId\":\"12345\",\"status\":\"processed\"}",
        "afterResultPath": "{\"orderId\":\"12345\",\"status\":\"processed\"}"
    },
    "status": "SUCCEEDED"
}
```

When you specify a mock response, TestState validates it against the AWS service’s API model so your mocked data conforms to the expected schema, maintaining high-fidelity testing without requiring actual AWS service calls.

**Scenario 2: Mock error conditions**You can also mock error conditions to test your error handling logic:

```
aws stepfunctions test-state --region us-east-1 \
--definition '{
  "Type": "Task",
  "Resource": "arn:aws:states:::lambda:invoke",
  "Parameters": {"FunctionName": "process-order"},
  "End": true
}' \
--mock '{"errorOutput":{"error":"Lambda.ServiceException","cause":"Function failed"}}' \
--inspection-level DEBUG
```

This simulates a Lambda service exception so you can verify how your state machine handles failures without triggering actual errors in your AWS environment.

The response shows the failed execution with error details:

```
{
    "error": "Lambda.ServiceException",
    "cause": "Function failed",
    "inspectionData": {
        "input": "{}",
        "afterInputPath": "{}",
        "afterParameters": "{\"FunctionName\":\"process-order\"}"
    },
    "status": "FAILED"
}
```

**Scenario 3: Test Map states**The second capability adds support for previously unsupported state types. Here’s how to test a Distributed Map state:

```
aws stepfunctions test-state --region us-east-1 \
--definition '{
  "Type": "Map",
  "ItemProcessor": {
    "ProcessorConfig": {"Mode": "DISTRIBUTED", "ExecutionType": "STANDARD"},
    "StartAt": "ProcessItem",
    "States": {
      "ProcessItem": {
        "Type": "Task",
        "Resource": "arn:aws:states:::lambda:invoke",
        "Parameters": {"FunctionName": "process-item"},
        "End": true
      }
    }
  },
  "End": true
}' \
--input '[{"itemId":1},{"itemId":2}]' \
--mock '{"result":"[{\"itemId\":1,\"status\":\"processed\"},{\"itemId\":2,\"status\":\"processed\"}]"}' \
--inspection-level DEBUG
```

The mock result represents the complete output from processing multiple items. In this case, the mocked array must match the expected Map state output format.

The response shows successful processing of the array input:

```
{
    "output": "[{\"itemId\":1,\"status\":\"processed\"},{\"itemId\":2,\"status\":\"processed\"}]",
    "inspectionData": {
        "input": "[{\"itemId\":1},{\"itemId\":2}]",
        "afterInputPath": "[{\"itemId\":1},{\"itemId\":2}]",
        "afterResultSelector": "[{\"itemId\":1,\"status\":\"processed\"},{\"itemId\":2,\"status\":\"processed\"}]",
        "afterResultPath": "[{\"itemId\":1,\"status\":\"processed\"},{\"itemId\":2,\"status\":\"processed\"}]"
    },
    "status": "SUCCEEDED"
}
```

**Scenario 4: Test Parallel states**Similarly, you can test Parallel states that execute multiple branches concurrently:

```
aws stepfunctions test-state --region us-east-1 \
--definition '{
  "Type": "Parallel",
  "Branches": [
    {"StartAt": "Branch1", "States": {"Branch1": {"Type": "Pass", "End": true}}},
    {"StartAt": "Branch2", "States": {"Branch2": {"Type": "Pass", "End": true}}}
  ],
  "End": true
}' \
--mock '{"result":"[{\"branch1\":\"data1\"},{\"branch2\":\"data2\"}]"}' \
--inspection-level DEBUG
```

The mock result must be an array with one element per branch. By using TestState, your mock data structure matches what a real Parallel state execution would produce.

The response shows the parallel execution results:

```
{
    "output": "[{\"branch1\":\"data1\"},{\"branch2\":\"data2\"}]",
    "inspectionData": {
        "input": "{}",
        "afterResultSelector": "[{\"branch1\":\"data1\"},{\"branch2\":\"data2\"}]",
        "afterResultPath": "[{\"branch1\":\"data1\"},{\"branch2\":\"data2\"}]"
    },
    "status": "SUCCEEDED"
}
```

**Scenario 5: Test individual states within complete workflows**You can test specific states within a full state machine definition using the stateName parameter. Here’s an example testing a single state, though you would typically provide your complete workflow definition and specify which state to test:

```
aws stepfunctions test-state --region us-east-1 \
--definition '{
  "Type": "Task",
  "Resource": "arn:aws:states:::lambda:invoke",
  "Parameters": {"FunctionName": "validate-order"},
  "End": true
}' \
--input '{"orderId":"12345","amount":99.99}' \
--mock '{"result":"{\"orderId\":\"12345\",\"validated\":true}"}' \
--inspection-level DEBUG
```

This tests a Lambda invocation state with specific input data, showing how TestState processes the input and transforms it through the state execution.

The response shows detailed input processing and validation:

```
{
    "output": "{\"orderId\":\"12345\",\"validated\":true}",
    "inspectionData": {
        "input": "{\"orderId\":\"12345\",\"amount\":99.99}",
        "afterInputPath": "{\"orderId\":\"12345\",\"amount\":99.99}",
        "afterParameters": "{\"FunctionName\":\"validate-order\"}",
        "result": "{\"orderId\":\"12345\",\"validated\":true}",
        "afterResultSelector": "{\"orderId\":\"12345\",\"validated\":true}",
        "afterResultPath": "{\"orderId\":\"12345\",\"validated\":true}"
    },
    "status": "SUCCEEDED"
}
```

These enhancements bring the familiar local development experience to Step Functions workflows, helping me to get instant feedback on changes before deploying to my AWS account. I can write automated test suites to validate all Step Functions features with the same reliability as cloud execution, providing confidence that my workflows will work as expected when deployed.

**Things to know**Here are key points to note:

* **Availability** – Enhanced TestState capabilities are available in all [AWS Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) where Step Functions is supported.
* **Pricing** – TestState API calls are included with AWS Step Functions at no additional charge.
* **Framework compatibility** – TestState works with any testing framework that can make HTTP requests, including Jest, pytest, JUnit, and others. You can write test suites that validate your workflows automatically in your continuous integration and continuous delivery (CI/CD) pipeline before deployment.
* **Feature support** – Enhanced TestState supports all Step Functions features including Distributed Map, Parallel states, error handling, and JSONata expressions.
* **Documentation** – For detailed options for different configurations, refer to the [TestState documentation](https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) and [API reference](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TestState.html?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) for the updated request and response model.

Get started today with enhanced local testing by integrating TestState into your development workflow.

Happy building!

— [Donnie](https://www.linkedin.com/in/donnieprakoso)

![Donnie Prakoso](https://d2908q01vomqb2.cloudfront.net/667be543b02294b7624119adc3a725473df39885/2023/05/30/donnie_profile_400x400.jpeg)

### [Donnie Prakoso](https://aws.amazon.com/blogs/aws/author/donnie/ "Posts by Donnie Prakoso")

Donnie Prakoso is a software engineer, self-proclaimed barista, and Principal Developer Advocate at AWS. With more than 17 years of experience in the technology industry, from telecommunications, banking to startups. He is now focusing on helping the developers to understand varieties of technology to transform their ideas into execution. He loves coffee and any discussion of any topics from microservices to AI / ML.

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