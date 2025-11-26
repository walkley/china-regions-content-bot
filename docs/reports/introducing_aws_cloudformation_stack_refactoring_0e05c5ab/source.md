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

## [AWS DevOps & Developer Productivity Blog](https://aws.amazon.com/blogs/devops/)

# Introducing AWS CloudFormation Stack Refactoring

by Kevin DeJong on 06 FEB 2025 in [AWS CloudFormation](https://aws.amazon.com/blogs/devops/category/management-tools/aws-cloudformation/ "View all posts in AWS CloudFormation"), [DevOps](https://aws.amazon.com/blogs/devops/category/devops/ "View all posts in DevOps"), [Management Tools](https://aws.amazon.com/blogs/devops/category/management-tools/ "View all posts in Management Tools") [Permalink](https://aws.amazon.com/blogs/devops/introducing-aws-cloudformation-stack-refactoring/) Share

## Introduction

As your cloud infrastructure grows and evolves, you may find the need to reorganize your [AWS CloudFormation](https://aws.amazon.com/cloudformation/) stacks for better management, for improved modularity, or to align with changing business requirements. CloudFormation now offers a powerful feature that allows you to move resources between stacks. In this post, we’ll explore the process of [stack refactoring](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-refactoring.html) and how it can help you maintain a well-organized and efficient cloud infrastructure.

## Understanding Stack Refactoring

Stack refactoring is the process of restructuring your CloudFormation stacks by moving resources from one stack to another or renaming a resource with a new logical ID within the same stack. This capability is particularly useful when you want to:

* Split a large, monolithic stack into smaller, more manageable stacks
* Reorganize resources to better align with your application architecture or organizational structure
* Rename the logical IDs of resources to make templates more readable

## Example Scenario

To demonstrate this capability, you are going to create a stack and then move some of its resources into a new stack. You will evaluate the new CLI commands that you need to leverage to make this possible. For this example, you are going to have an SNS topic with a lambda function subscribed to your SNS topic. As your usage of the SNS topic expands, you want to break apart the subscriptions into a different stack.

1. Create a new template called `before.yaml` with your starting template:

   ```
   AWSTemplateFormatVersion: "2010-09-09"

   Resources:
     Topic:
       Type: AWS::SNS::Topic

     MyFunction:
       Type: AWS::Lambda::Function
       Properties:
         FunctionName: my-function
         Handler: index.handler
         Runtime: python3.12
         Code:
           ZipFile: |
             import json
             def handler(event, context):
               print(json.dumps(event))
               return event
         Role: !GetAtt FunctionRole.Arn
         Timeout: 30

     Subscription:
       Type: AWS::SNS::Subscription
       Properties:
         Endpoint: !GetAtt MyFunction.Arn
         Protocol: lambda
         TopicArn: !Ref Topic

     FunctionInvokePermission:
       Type: AWS::Lambda::Permission
       Properties:
         Action: lambda:InvokeFunction
         Principal: sns.amazonaws.com
         FunctionName: !GetAtt MyFunction.Arn
         SourceArn: !Ref Topic

     FunctionRole:
       Type: AWS::IAM::Role
       Properties:
         AssumeRolePolicyDocument:
           Version: "2012-10-17"
           Statement:
             - Action:
                 - sts:AssumeRole
               Effect: Allow
               Principal:
                 Service:
                   - lambda.amazonaws.com
               Condition:
                 StringEquals:
                   aws:SourceAccount: !Ref AWS::AccountId
                 ArnLike:
                   aws:SourceArn: !Sub "arn:${AWS::Partition}:lambda:${AWS::Region}:${AWS::AccountId}:function:my-function"
         Policies:
           - PolicyName: LambdaPolicy
             PolicyDocument:
               Version: "2012-10-17"
               Statement:
                 - Action:
                     - logs:CreateLogGroup
                     - logs:CreateLogStream
                     - logs:PutLogEvents
                   Resource:
                     - arn:aws:logs:*:*:*
                   Effect: Allow
   ```
2. Create a new stack using the `before.yaml` template.

   ```
   aws cloudformation create-stack --stack-name MySns --template-body file://before.yaml --capabilities CAPABILITY_IAM
   ```
3. Create a new template called `afterSns.yaml` with the content below. This template has your SNS topic in it and has a new export in it that will export the SNS topic ARN. This export will be used by your other templates to get the required SNS topic ARN.

   ```
   AWSTemplateFormatVersion: "2010-09-09"
   Resources:
     Topic:
       Type: AWS::SNS::Topic
   Outputs:
     TopicArn:
       Value: !Ref Topic
       Export:
         Name: TopicArn
   ```
4. Create a new template called `afterLambda.yaml` with the content below. This template includes all the resources to create a Lambda subscription to your SNS topic. This template switched the `!Ref Topic` to use the exported valued by using `!ImportValue TopicArn`.

   ```
   AWSTemplateFormatVersion: "2010-09-09"
   Resources:
     Function:
       Type: AWS::Lambda::Function
       Properties:
         FunctionName: my-function
         Handler: index.handler
         Runtime: python3.12
         Code:
           ZipFile: |
             import json
             def handler(event, context):
               print(json.dumps(event))
               return event
         Role: !GetAtt FunctionRole.Arn
         Timeout: 30
     Subscription:
       Type: AWS::SNS::Subscription
       Properties:
         Endpoint: !GetAtt Function.Arn
         Protocol: lambda
         TopicArn: !ImportValue TopicArn
     FunctionInvokePermission:
       Type: AWS::Lambda::Permission
       Properties:
         Action: lambda:InvokeFunction
         Principal: sns.amazonaws.com
         FunctionName: !GetAtt Function.Arn
         SourceArn: !ImportValue TopicArn
     FunctionRole:
       Type: AWS::IAM::Role
       Properties:
         AssumeRolePolicyDocument:
           Version: "2012-10-17"
           Statement:
             - Action:
                 - sts:AssumeRole
               Effect: Allow
               Principal:
                 Service:
                   - lambda.amazonaws.com
               Condition:
                 StringEquals:
                   aws:SourceAccount: !Ref AWS::AccountId
                 ArnLike:
                   aws:SourceArn: !Sub "arn:${AWS::Partition}:lambda:${AWS::Region}:${AWS::AccountId}:function:my-function"
         Policies:
           - PolicyName: LambdaPolicy
             PolicyDocument:
               Version: "2012-10-17"
               Statement:
                 - Action:
                     - logs:CreateLogGroup
                     - logs:CreateLogStream
                     - logs:PutLogEvents
                   Resource:
                     - arn:aws:logs:*:*:*
                   Effect: Allow
   ```
5. Create a resource mappings file called `refactor.json` to rename the logical ID of a resource. This file defines the source and destination stack names and logical IDs for resources being refactored. If the logical IDs don’t change, this file doesn’t need to be specified.

   ```
   [
       {
           "Source": {
               "StackName": "MySns",
               "LogicalResourceId": "MyFunction"
           },
           "Destination": {
               "StackName": "MyLambdaSubscription",
               "LogicalResourceId": "Function"
           }
       }
   ]
   ```
6. Create a stack refactor task. You are using enable-stack-creation to tell the refactoring capability to create the destination stack for us. If the destination stack already exists you don’t have to provide this option.

   ```
   aws cloudformation create-stack-refactor --stack-definitions StackName=MySns,TemplateBody@=file://afterSns.yaml StackName=MyLambdaSubscription,TemplateBody@=file://afterLambda.yaml --enable-stack-creation --resource-mappings file://refactor.json
   ```

   Results:

   ```
   {
       "StackRefactorId": "56b06a9a-72ff-4f87-8205-32111bff83f9"
   }
   ```

   Capture the stack refactor ID for the following steps.
7. Evaluate the stack refactor task.

   ```
   aws cloudformation describe-stack-refactor --stack-refactor-id 56b06a9a-72ff-4f87-8205-32111bff83f9
   ```

   results:

   ```
   {
       "StackRefactorId": "56b06a9a-72ff-4f87-8205-32111bff83f9",
       "StackIds": [
           "arn:aws:cloudformation:<<AWS::Region>>:<<AWS::AccountId>>:stack/MySns/a10bfd30-cc67-11ef-877a-023cc5780193",
           "arn:aws:cloudformation:<<AWS::Region>>:<<AWS::AccountId>>:stack/MyLambdaSubscription/6d117360-cc68-11ef-ba33-06338dcc9d39"
       ],
       "ExecutionStatus": "AVAILABLE",
       "Status": "CREATE_COMPLETE"
   }
   ```

   If you forgot to capture the stack refactor ID you can run:

   ```
   aws cloudformation list-stack-refactors
   ```

   You can list stack the actions that the refactor did by running:

   ```
   aws cloudformation list-stack-refactor-actions —stack-refactor-id 56b06a9a-72ff-4f87-8205-32111bff83f9
   ```

   You will see that the refactor will create a new stack and what resources are being moved.

   ```
   {
       "StackRefactorActions": [
           {
               "Action": "Move",
               "Entity": "Resource",
               "PhysicalResourceId": "MySns-FunctionRole-BMO7ohLu4S6a",
               "Description": "No configuration changes detected.",
               "Detection": "Auto",
               "TagResources": [],
               "UntagResources": [],
               "ResourceMapping": {
                   "Source": {
                       "StackName": "arn:aws:cloudformation:<<AWS::Region>>:<<AWS::AccountId>>:stack/MySns/a10bfd30-cc67-11ef-877a-023cc5780193",
                       "LogicalResourceId": "FunctionRole"
                   },
                   "Destination": {
                       "StackName": "arn:aws:cloudformation:<<AWS::Region>>:<<AWS::AccountId>>:stack/MyLambdaSubscription/6d117360-cc68-11ef-ba33-06338dcc9d39",
                       "LogicalResourceId": "FunctionRole"
                   }
               }
           },
           {
               "Action": "Create",
               "Entity": "Stack",
               "Description": "Stack arn:aws:cloudformation:<<AWS::Region>>:<<AWS::AccountId>>:stack/MyLambdaSubscription/6d117360-cc68-11ef-ba33-06338dcc9d39 created.",
               "Detection": "Manual",
               "TagResources": [],
               "UntagResources": [],
               "ResourceMapping": {
                   "Source": {},
                   "Destination": {}
               }
           },
   ...
   ```
8. Execute the stack refactor

   ```
   aws cloudformation execute-stack-refactor --stack-refactor-id 56b06a9a-72ff-4f87-8205-32111bff83f9
   ```
9. Wait for the stack refactor to complete. Evaluate the stack refactor status by executing:

   ```
   aws cloudformation describe-stack-refactor --stack-refactor-id 56b06a9a-72ff-4f87-8205-32111bff83f9
   ```

   ```
   {
       "StackRefactorId": "56b06a9a-72ff-4f87-8205-32111bff83f9",
       "StackIds": [
           "arn:aws:cloudformation:<<AWS::Region>>:<<AWS::AccountId>>:stack/MySns/a10bfd30-cc67-11ef-877a-023cc5780193",
           "arn:aws:cloudformation:<<AWS::Region>>:<<AWS::AccountId>>:stack/MyLambdaSubscription/6d117360-cc68-11ef-ba33-06338dcc9d39"
       ],
       "ExecutionStatus": "EXECUTE_COMPLETE",
       "Status": "CREATE_COMPLETE"
   }
   ```

## Conclusion

Stack refactoring in AWS CloudFormation represents a significant advancement in infrastructure management, offering a safer and more efficient way to reorganize your cloud resources without disruption. This feature eliminates the traditional need to remove the resource, with a retain policy, and then import the resource when restructuring stacks, helping you reduce misconfiguration risk and save time. Through the example demonstrated in this post, you’ve seen how to split a monolithic stack into smaller, focused stacks while using exports and imports to maintain dependencies between stacks. You’ve also explored the new CloudFormation CLI commands that make stack refactoring possible while maintaining resource stability during reorganization.

As your infrastructure evolves, stack refactoring provides the flexibility needed to adapt your CloudFormation stack organization to changing requirements while maintaining the integrity of your cloud resources. This capability is particularly valuable for teams looking to improve their infrastructure maintainability and align their resource organization with evolving architectural patterns. Remember to thoroughly test your refactoring plans in a non-production environment first, and always ensure your new stack structure maintains the necessary security and access controls.

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2024/04/18/kddejong.jpg)

### Kevin DeJong

Kevin DeJong is a Software Development Engineer – Infrastructure as Code at AWS. He is creator and maintainer of cfn-lint. Kevin has been working with the CloudFormation service for over 10 years.

TAGS: [AWS CloudFormation](https://aws.amazon.com/blogs/devops/tag/aws-cloudformation/)

### Resources

* [AWS Developer Tools Blog](https://aws.amazon.com/blogs/developer)
* [AWS Frontend Web & Mobile Blog](https://aws.amazon.com/blogs/mobile/)
* [AWS Developers YouTube](https://www.youtube.com/%40awsdevelopers)
* [Amazon Q Developer](https://aws.amazon.com/q/developer/)
* [AWS CDK](https://aws.amazon.com/cdk/)
* [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
* [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
* [AWS CodeBuild](https://aws.amazon.com/codebuild/)

---

### Follow

* [AWS .NET on Twitter](https://twitter.com/dotnetonaws)
* [AWS Cloud on Twitter](https://twitter.com/awscloud)
* [AWS on Reddit](https://www.reddit.com/user/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
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