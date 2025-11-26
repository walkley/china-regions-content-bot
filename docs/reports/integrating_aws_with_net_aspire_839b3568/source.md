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

## [AWS Developer Tools Blog](https://aws.amazon.com/blogs/developer/)

# Integrating AWS with .NET Aspire

by Norm Johanson on 11 FEB 2025 in [.NET](https://aws.amazon.com/blogs/developer/category/programing-language/dot-net/ "View all posts in .NET") [Permalink](https://aws.amazon.com/blogs/developer/integrating-aws-with-net-aspire/) Share

.NET Aspire is a new way of building cloud-ready applications. In particular, it provides an orchestration for local environments in which to run, connect, and debug the components of distributed applications. Those components can be .NET projects, databases, containers, or executables. .NET Aspire is designed to have integrations with common components used in distributed applications. These integrations reduce the amount of glue code that has to be written for each component to tie them all together.

Seeing how .NET Aspire helps to improve the inner dev loop for cloud ready applications, the .NET team at AWS have been working on integrations for connecting your .NET applications to AWS resources. The integrations released to date are utilized within the .NET Aspire AppHost project. These integrations can be included by adding the [Aspire.Hosting.AWS](https://www.nuget.org/packages/Aspire.Hosting.AWS) NuGet package to the .NET Aspire AppHost project.

Using our [Aspire.Hosting.AWS](https://www.nuget.org/packages/Aspire.Hosting.AWS) NuGet package, AWS application resources can be automatically provisioned with [AWS CloudFormation](https://aws.amazon.com/cloudformation/) as part of the .NET Aspire application startup. The provisioned resources can be connected to the code using the AWS SDK for .NET in .NET applications. This eliminates the need for developers to perform extra steps to set up their local dev environment.

For Amazon DynamoDB users who want to avoid the cost and networking for accessing the real DynamoDB service for local debugging, there is [Amazon DynamoDB local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html). The [Aspire.Hosting.AWS](https://www.nuget.org/packages/Aspire.Hosting.AWS) NuGet package has integrated DynamoDB local into .NET Aspire, taking care of the process of installing, configuring and connecting the AWS SDK for .NET to DynamoDB local.

## .NET Aspire AppHost

Before diving into the AWS features, let’s provide some background on .NET Aspire. Going into depth on all of .NET Aspire is too large a topic for this blog post. If you’re unfamiliar with .NET Aspire, I recommend checking out the [.NET Aspire documentation](https://learn.microsoft.com/en-us/dotnet/aspire/get-started/aspire-overview). What’s most relevant for the AWS integrations is the AppHost project for a .NET Aspire-based application.

The heart of a .NET Aspire project is the AppHost project. This is a .NET project that defines all of the components of a distributed application and how each is related to the others. For example, by using the **.NET Aspire Starter App** project template in Visual Studio, and enabling Redis for caching, you create an AppHost with the following code:

```
var builder = DistributedApplication.CreateBuilder(args);

var cache = builder.AddRedis("cache");

var apiService = builder.AddProject<Projects.FirstApp_ApiService>("apiservice");

builder.AddProject<Projects.FirstApp_Web>("webfrontend")
    .WithExternalHttpEndpoints()
    .WithReference(cache)
    .WaitFor(cache)
    .WithReference(apiService)
    .WaitFor(apiService);

builder.Build().Run();
```

This code uses the Redis integration to create a .NET Aspire resource that represents the Redis container. It then adds a frontend .NET project as a resource and connects it with the Redis resource. A second Web API .NET project is defined and added as a reference to the frontend project.

The AppHost project is the startup project in the IDE. When the AppHost is launched for debugging, the Redis container and .NET projects will all be started. .NET Aspire provides the service discovery for the frontend project to locate the Redis container and Web API project.

## Provisioning Resources

[Aspire.Hosting.AWS](https://www.nuget.org/packages/Aspire.Hosting.AWS) gives developers the ability to provision your AWS resources as part of the inner dev loop of building applications. This uses [AWS CloudFormation](https://aws.amazon.com/cloudformation/) to provision application resources as part of the F5 dev inner loop. AWS resources can be defined using either a CloudFormation template or the [Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/).

The following AppHost code shows how to define AWS resources in the `app-resources.template` file. The .NET project has a reference to the CloudFormation resource.

```
var builder = DistributedApplication.CreateBuilder(args);

// Set up a configuration for the AWS SDK for .NET.
var awsConfig = builder.AddAWSSDKConfig()
                        .WithProfile("dev")
                        .WithRegion(RegionEndpoint.USWest2);

// Provision application-level resources like SQS queues and SNS topics
// defined in the CloudFormation template file called app-resources.template.
var awsResources = builder.AddAWSCloudFormationTemplate("AWSResources", "app-resources.template")
                          .WithReference(awsConfig);

builder.AddProject<Projects.Frontend>("Frontend")
         .WithExternalHttpEndpoints()
         .WithReference(awsResources);
```

When the AppHost is launched, the AWS integration checks to see if there were any changes made to the `app-resources.template` file since the last debug session. If there are changes or if the CloudFormation stack doesn’t exist, the template is applied.

A CloudFormation template defines a collection of output parameters. These output parameters are often the identifiers of the resources created by CloudFormation. By using the `WithReference` method for adding a reference of the CloudFormation resource to the .NET project, the output parameters are assigned to the .NET project. The output parameters can be accessed via the `IConfiguration` interface. For example, the following CloudFormation template defines a topic and queue with output parameters to hold the identifiers for the topic and queue.

[![](https://d2908q01vomqb2.cloudfront.net/0716d9708d321ffb6a00818614779e779925365c/2025/02/11/00-cloudformation.png)](https://d2908q01vomqb2.cloudfront.net/0716d9708d321ffb6a00818614779e779925365c/2025/02/11/00-cloudformation.png)

The output parameter `ChatTopicArn`, which is the identifier for the topic, can be retrieved from `IConfiguration` in the .NET project. By default, the integration puts the output parameters under the `AWS:Resources` config section. This can be changed by passing in a config section name as a parameter on the `WithReference` method call. The code below demonstrates how to get the topic identifier for use with our [AWS Messaging](https://github.com/awslabs/aws-dotnet-messaging) library.

```
builder.Services.AddAWSMessageBus(messageBuilder =>
{
    var chatTopicArn = builder.Configuration["AWS:Resources:ChatTopicArn"];
    if (chatTopicArn != null)
    {
        messageBuilder.AddSNSPublisher<Frontend.Models.ChatMessage>(chatTopicArn);
    }
});
```

The following screenshot shows the .NET Aspire dashboard for this AppHost with both the CloudFormation resource and the .NET project.

[![](https://d2908q01vomqb2.cloudfront.net/0716d9708d321ffb6a00818614779e779925365c/2025/02/11/01-aspire-dashboard.png)](https://d2908q01vomqb2.cloudfront.net/0716d9708d321ffb6a00818614779e779925365c/2025/02/11/01-aspire-dashboard.png)

In this scenario, the CloudFormation stack didn’t yet exist. The console logs for the CloudFormation resource will show the provisioning.

[![](https://d2908q01vomqb2.cloudfront.net/0716d9708d321ffb6a00818614779e779925365c/2025/02/11/02-aspire-console.png)](https://d2908q01vomqb2.cloudfront.net/0716d9708d321ffb6a00818614779e779925365c/2025/02/11/02-aspire-console.png)

If there were no changes to the CloudFormation template, the logs would express that no changes were found, and instead obtain the output parameters from the existing stack for inclusion in the reference projects. This means that there will only be a dev inner loop pause when changes need to be made to the CloudFormation stack.

As part of [.NET Conf 2024](https://www.youtube.com/watch?v=yVgr6cRYOPk), AWS presented the following talk that demonstrated AWS resource provisioning. Check out the video for a deeper dive into the integration along with using the CDK for defining the application resources.

[![](https://d2908q01vomqb2.cloudfront.net/0716d9708d321ffb6a00818614779e779925365c/2025/02/11/netconfscreenshot.png)](https://www.youtube.com/watch?v=yVgr6cRYOPk)

## Integrating Amazon DynamoDB Local

Amazon DynamoDB provides a [local version of DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html) for development and testing that is distributed as a container. With version 9.1.0 of the Aspire.Hosting.AWS package, you can easily integrate the DynamoDB local container with your .NET Aspire project. This enables seamless transition between DynamoDB Local for development and the production DynamoDB service in AWS, without requiring any code changes in your application.

To get started in the .NET Aspire AppHost, call the `AddAWSDynamoDBLocal` method to add DynamoDB local as a resource to the .NET Aspire application.

```
var builder = DistributedApplication.CreateBuilder(args);

// Add a DynamoDB Local instance
var localDynamoDB = builder.AddAWSDynamoDBLocal("DynamoDBLocal");
```

For each .NET project in the .NET Aspire application using DynamoDB, add a reference to the DynamoDB local resource.

```
// Reference DynamoDB local in project
builder.AddProject<Projects.Frontend>("Frontend")
   .WithReference(localDynamoDB);
```

In the .NET projects that use DynamoDB, you need to construct the DynamoDB service client from the SDK without explicitly setting the AWS Region or service endpoint. This means constructing the `AmazonDynamoDBClient` object without passing in the Region or an `AmazonDynamoDBConfig` with the `RegionEndpoint` property set. By not explicitly setting the Region, the SDK searches the environment for configuration that informs the SDK where to send the requests. The Region is set locally by the `AWS_REGION` environment variable or in your credentials profile by setting the region property. Once deployed to AWS, the compute environments set environment configuration such as the `AWS_REGION` environment variable so that the SDK knows what Region to use for the service client.

The AWS SDKs have a feature called [Service-specific endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-ss-endpoints.html) that allow setting an endpoint for a service via an environment variable. The `WithReference` call made on the .NET project sets the `AWS_ENDPOINT_URL_DYNAMODB` environment variable. It will be set to the DynamoDB local container that was started as part of the `AddAWSDynamoDBLocal` method.

[![](https://d2908q01vomqb2.cloudfront.net/0716d9708d321ffb6a00818614779e779925365c/2025/02/11/03-aspire-environment-variable.png)](https://d2908q01vomqb2.cloudfront.net/0716d9708d321ffb6a00818614779e779925365c/2025/02/11/03-aspire-environment-variable.png)

The `AWS_ENDPOINT_URL_DYNAMODB` environment variable overrides other config settings like the `AWS_REGION` environment variable, ensuring your projects running locally use DynamoDB local. After the `AmazonDynamoDBClient` has been created pointing to DynamoDB local, all other service calls work the same as if you are going to the real DynamoDB service. No code changes are required.

### Options for DynamoDB Local

When the `AddAWSDynamoDBLocal` method is called, any data and table definitions are stored in memory by default. This means that every time the .NET Aspire application is started, DynamoDB local is initiated with a fresh instance with no tables or data. The `AddAWSDynamoDBLocal` method takes in an optional `DynamoDBLocalOptions` object that exposes the [options](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.UsageNotes.html) that are available for DynamoDB local.

If you want the tables and data to persist between .NET Aspire debug sessions, set the `LocalStorageDirectory` property on the `DynamoDBLocalOptions` object to a local folder where the data will be persisted. The `AddAWSDynamoDBLocal` method will take care of mounting the local directory to the container and configuring the DynamoDB local process to use the mount point.

## What’s next?

Our work for .NET Aspire is being done in our new [aws/integrations-on-dotnet-aspire-for-aws](https://github.com/aws/integrations-on-dotnet-aspire-for-aws) GitHub repository. We would love to hear from the community on what you think of .NET Aspire and what you would like to see for AWS integrations.

The next big effort we are working on is to create a local development environment for building and debugging .NET Lambda functions. You can track our progress with Lambda by subscribing to the following GitHub issue: <https://github.com/aws/integrations-on-dotnet-aspire-for-aws/issues/17>. We have released an early preview and your feedback is important to make sure we have built the right developer experience.

## Conclusion

Try out using .NET Aspire for your local development environment. You can take advantage of the provisioning for application resources right from .NET Aspire. Team’s can setup their repositories with .NET Aspire so that when members need to start developing on the application they can clone the repository, open the solution in their IDE of choice, and start debugging. The resources required for the new team member will be provisioned as they start their debugging experience. This means that no other tooling is required to get the application running locally. Take advantage of DynamoDB local with .NET Aspire, which makes it easy to acquire and connect without having to take you out of your dev environment. Reach out to us with any issues or feedback on our [aws/integrations-on-dotnet-aspire-for-aws](https://github.com/aws/integrations-on-dotnet-aspire-for-aws) GitHub repository.

TAGS: [.NET](https://aws.amazon.com/blogs/developer/tag/net/), [Amazon DynamoDB](https://aws.amazon.com/blogs/developer/tag/amazon-dynamodb/), [CloudFormation](https://aws.amazon.com/blogs/developer/tag/cloudformation/)

![Norm Johanson](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2019/09/20/square-head.jpg)

### Norm Johanson

Norm Johanson has been a software developer for more than 25 years developing all types of applications. Since 2010 he has been working for AWS focusing on the .NET developer experience at AWS. You can find him on Twitter @socketnorm and GitHub @normj.

### Resources

[Developer Resources & Community](https://aws.amazon.com/developer?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=developer-resources)  [Open Source Repos](https://aws.github.io/)  [Twitch Live Coding](https://aws.amazon.com/twitch?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=developer-resources)  [Labs on Github](https://github.com/awslabs)

---

### Follow

[Instagram](https://www.instagram.com/awsdevelopers)  [Reddit](https://www.reddit.com/user/AmazonWebServices)  [Twitter](https://twitter.com/awscloud)  [Facebook](https://www.facebook.com/amazonwebservices)  [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)  [Twitch](https://www.twitch.tv/aws)  [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=developer-social)

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