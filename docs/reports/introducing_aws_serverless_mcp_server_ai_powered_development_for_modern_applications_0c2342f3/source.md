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

# Introducing AWS Serverless MCP Server: AI-powered development for modern applications

by Shridhar Pandey and Ben Freiberg on 29 MAY 2025 in [Announcements](https://aws.amazon.com/blogs/compute/category/post-types/announcements/ "View all posts in Announcements"), [Intermediate (200)](https://aws.amazon.com/blogs/compute/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [Serverless](https://aws.amazon.com/blogs/compute/category/serverless/ "View all posts in Serverless") [Permalink](https://aws.amazon.com/blogs/compute/introducing-aws-serverless-mcp-server-ai-powered-development-for-modern-applications/) Share

Modern application development demands faster, more efficient ways to build and deploy software. Over the past decade, serverless computing has emerged as a transformative approach to software development, enabling developers to focus on building applications without having to manage the underlying infrastructure. As developers build their applications using [AWS Serverless Compute](https://aws.amazon.com/serverless/), they seek guidance on selecting appropriate services, understanding best practices, and implementation patterns to make the most of this paradigm.

Today, AWS announces the open-source AWS Serverless [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) Server, a tool that combines the power of AI assistance with serverless expertise to enhance how developers build modern applications. The Serverless MCP Server provides contextual guidance specific to serverless development, helping developers make informed decisions about architecture, implementation, and deployment.

This post describes how the [Serverless MCP Server](https://awslabs.github.io/mcp/servers/aws-serverless-mcp-server/) works with AI coding assistants to streamline serverless development. Learn how to use this solution to accelerate your serverless development workflow and build robust, high-performing applications more efficiently.

## Overview

Serverless computing enables development teams to significantly reduce time-to-market while improving operational efficiency. Developers can focus on creating business value, while AWS services automatically handle scaling, availability, and infrastructure maintenance. [AWS Lambda](https://aws.amazon.com/lambda/) provides a seamless compute service where code runs in response to events, scaling instantly from a few requests per day to thousands per second. Through integration with over 200 AWS services, Lambda enables developers to build sophisticated applications using triggers from [Amazon API Gateway](https://aws.amazon.com/api-gateway/), [Amazon S3](https://aws.amazon.com/s3/), [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), and many others. Whether you’re building data processing pipelines, real-time stream processing, or web applications, Lambda’s support for popular programming languages and development frameworks helps development teams leverage their existing skills while embracing the serverless paradigm.

### MCP Server

MCP is an open protocol for AI agents to interact with external tools and data sources. It defines how AI assistants can discover, understand, and use various capabilities provided by external systems. This protocol allows AI models to extend their functionality beyond their own training data by accessing real-time information and executing specific tasks through standardized interfaces.

MCP servers implement this protocol by providing tools, resources, and contextual information that AI assistants can use via MCP clients. They serve as a knowledge bridge that gives AI assistants, such as [Amazon Q Developer](https://aws.amazon.com/q/developer/), [Cline](https://cline.bot/), and [Cursor](https://www.cursor.com/en), the additional context needed to make informed decisions about cloud architecture and implementation. This is particularly valuable for serverless applications, where developers navigate multiple services, event patterns, and integration points to build scalable, performant applications.

AWS currently offers the [AWS Lambda Tool MCP Server](https://awslabs.github.io/mcp/servers/lambda-tool-mcp-server/), which allows AI models to directly interact with existing Lambda functions as MCP tools without any code changes. This MCP server acts as a bridge between MCP clients and Lambda functions, allowing AI assistants to access and invoke Lambda functions.

## Serverless MCP Server

The open-source AWS Serverless MCP launched today enhances the serverless development experience by providing AI coding assistants with comprehensive knowledge of serverless patterns, best practices, and AWS services. This MCP server acts as an intelligent companion, guiding developers through the entire application development lifecycle, from initial design to deployment, offering contextual assistance at each stage.

The new Serverless MCP server provides tools that cover many areas of serverless development. During the initial planning and setup phase, the MCP server helps developers initialize new projects using [AWS Serverless Application Model (AWS SAM)](https://aws.amazon.com/serverless/sam/) templates, select appropriate Lambda runtimes, and set up project dependencies. This enables developers to quickly bootstrap new serverless applications with the right configuration and structure.

As development progresses, the MCP server assists with building and deploying serverless applications. It provides tools for local testing, building deployment artifacts, and managing deployments. For web applications, the MCP server offers specialized support for deploying backend, frontend, or full-stack applications, and setting up custom domains.

The MCP server also emphasizes operational excellence through comprehensive observability tools, helping developers to effectively monitor application performance and troubleshoot issues. Throughout the development process, the server provides contextual guidance for infrastructure as code (IaC) decisions, Lambda-specific best practices, and event schemas for [Lambda event source mappings (ESMs)](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html).

## Serverless MCP Server in action

To demonstrate the capabilities of the Serverless MCP Server, this example walks you through a scenario of creating, deploying, and troubleshooting a serverless application.

### Prerequisites and installation

To get started, download the AWS Serverless MCP Server from [GitHub](https://github.com/awslabs/mcp/blob/main/src/aws-serverless-mcp-server/README.md) or [Python Package Index (PyPi)](https://pypi.org/project/awslabs.aws-serverless-mcp-server/) and follow the installation instructions. You can use this MCP server with any AI coding assistant of your choice, such as Q Developer, Cursor, Cline, etc. The walkthrough example in this post uses Cline.

Add the following code to your MCP client configuration. The Serverless MCP Server uses the `default` AWS profile by default. Specify a value in AWS\_PROFILE if you want to use a different profile. Similarly, adjust the [AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) and log level values as needed.

```
{
  "mcpServers": {
    "awslabs.aws-serverless-mcp": {
      "command": "uvx",
      "args": [
        "awslabs.aws-serverless-mcp-server@latest"
      ],
      "env": {
        "AWS_PROFILE": "your-aws-profile",
        "AWS_REGION": "us-east-1",
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

The Serverless MCP Server incorporates built-in guardrails to ensure secure and controlled development. By default, the MCP server operates in a read-only mode, allowing only non-mutating actions. This safety-first approach allows you to explore serverless capabilities and architectural patterns while preventing unintended changes to your applications or infrastructure. The server also restricts access to [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) by default, protecting sensitive operational data from exposure to AI assistants.

As your development needs evolve, you can selectively override these security defaults. The `--allow-write` flag enables mutating operations for tasks such as deployments and updates, while `--allow-sensitive-data-access` provides access to CloudWatch Logs for debugging and troubleshooting. Consider enabling these permissions only when necessary and in appropriate development contexts.

### Creating and deploying a serverless application

Imagine that you want to build a to-do list web application. Start by prompting your AI assistant.

> *I want to build a new to-do list web application in a new workspace. I want to add, list, and delete to-dos. Would AWS Lambda be a good choice for this?*

[![](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/05/28/image-1-12.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/05/28/image-1-12.png)

The agent uses the `get_lambda_guidance_tool` to receive tailored guidance based on the use case and the inferred event source, API Gateway in this case. Then, you want to better understand how to deploy the application to AWS.

> *I later want to deploy the application to AWS. Which Infrastructure as Code tool would be best for this?*

There are several ways to deploy your functions to AWS such as AWS SAM or the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html). The model opts to get more information before making a recommendation. It selects the `get_iac_guidance_tool` from the Serverless MCP Server.

[![](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/05/28/image-2-11.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/05/28/image-2-11.png)

The Serverless MCP Server can also assist you with interacting with the [AWS Serverless Application Model Command Line Interface (AWS SAM CLI)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) as well as deploying application-based blueprints such as backend, frontend, or full-stack applications.

Before the deployment, test the function locally to verify that it works correctly.

> *I want to test my Lambda function locally before deploying it. Can you invoke the “TodoFunction” from my SAM project with a GET request?*

[![](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/05/28/image-3-10.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/05/28/image-3-10.png)

Now that you are confident that the application works, you want to deploy the backend logic to AWS. So, you prompt the agent to deploy your app. It selects the *deploy\_webapp* tool and provides the tool with arguments to deploy the app, including backend deploymentType. This tool uses the [AWS Lambda Web Adapter](https://github.com/awslabs/aws-lambda-web-adapter) framework, allowing you to easily deploy applications written in standard web frameworks like Express or Next.js, without any additional web adapters.

[![](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/05/28/image-4-2.jpeg)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/05/28/image-4-2.jpeg)

The agent can also check on the status of a deployment to make sure that it completes successfully.

[![](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/05/28/image-5-2.jpeg)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/05/28/image-5-2.jpeg)

Your application is now deployed to AWS and ready to serve traffic.

### Troubleshooting the serverless application

The Serverless MCP Server also supports you in testing and troubleshooting your Lambda functions. It provides valuable context to AI assistants in identifying and remediating issues. For example, you can use your agent to check for any issues with your application.

> *Check the logs and metrics of the todo app for any issues*

[![](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/05/28/image-7-3.jpeg)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/05/28/image-7-3.jpeg)

The model can analyze the logs and metrics and offer recommendations such as adjusting memory allocation.

The Serverless MCP Server tools provide the assistant with the additional context it needs to identify issues and generate recommendations.

In this example, the analysis and recommendations are:

|  |
| --- |
| **Log Analysis**  I’ve checked the logs for all three Lambda functions of your todo app, looking specifically for errors:  • **ListTodosFunction**: No errors detected   • **AddTodoFunction**: No errors detected   • **DeleteTodoFunction**: No errors detected  All functions are operating normally with successful executions and no error logs.  **Performance Metrics**  **Lambda Function Performance**   • Memory usage is reasonable at 100–106 MB out of 512 MB allocated (about 20% utilization)   • Fast execution durations for warm starts: 85–195 ms range   • No throttling or out-of-memory errors detected   • No function errors or exceptions in the logs  **API Gateway Metrics**   • Total Requests: 11 requests recorded   • Average Latency: 797 ms   • P95 Latency: 3364 ms (high)   • 4XX Errors: 0 (no client errors)   • 5XX Errors: 1 (one server error detected)  **Issues Identified**  The log analysis is clean with no errors, but the metrics reveal one potential issue:   1. **One 5XX Error in API Gateway**: There was a single server-side error recorded in the API Gateway logs. Since there are no corresponding errors in the Lambda function logs, this might be related to:         • A timeout (API Gateway taking too long to respond)         • An integration issue between API Gateway and Lambda         • A temporary network issue 2. **Relatively High P95 Latency**: The 95th percentile latency of 3364 ms is quite high compared to the average. This suggests some outlier requests are taking significantly longer to complete.   **Recommendations**   1. Monitor the 5XX error rate as it resurfaces. 2. Consider implementing more detailed logging at the edge of the error path. 3. Investigate the cause of the high P95 latency. Check for cold starts, payload size, or network latency as likely culprits. 4. Consider enabling API Gateway and Lambda performance dashboards for more granular, historical latency and error metrics. 5. Continue to monitor memory and duration metrics to ensure performance remains healthy as traffic increases. |

## Features supported by the Serverless MCP Server

The Serverless MCP Server provides several MCP tools, which can be classified into four categories.

1. **Serverless application lifecycle**
   * `sam_init_tool`: Initializes a new AWS SAM project with the chosen runtime and dependencies.
   * `sam_build_tool`: Builds a serverless application using the AWS SAM CLI and prepares deployment artifacts.
   * `sam_deploy_tool`: Deploys a serverless application to AWS, managing artifact upload and stack creation.
   * `sam_local_invoke_tool`: Locally invokes a Lambda function for testing with custom events and environments.
2. **Web application deployment and management**
   * `deploy_webapp_tool`: Deploys backend, frontend, or fullstack web applications to Lambda using the Lambda Web Adapter.
   * `update_frontend_tool`: Updates the frontend assets and optionally invalidates the [Amazon CloudFront](https://aws.amazon.com/cloudfront/) cache.
   * `configure_domain_tool`: Configures a custom domain, includes certificate and DNS setup.
3. **Observability**
   * `sam_logs_tool`: Retrieves logs, and supports filtering and time range selection.
   * `get_metrics_tool`: Fetches specified metrics.
4. **Guidance, IaC templates, and deployment help**
   * `get_iac_guidance_tool`: Provides guidance for selecting IaC tools.
   * `get_lambda_guidance_tool`: Offers advice on when to use Lambda for specific runtimes and use cases.
   * `get_lambda_event_schemas_tool`: Returns event schemas for Lambda integrations.
   * `get_serverless_templates_tool`: Supplies example AWS SAM templates for different serverless application types.
   * `deployment_help_tool`: Provides help and status information about deployments.
   * `deploy_serverless_app_help_tool`: Offers instructions for deploying serverless applications to Lambda.

Visit the Serverless MCP Server [documentation](https://github.com/awslabs/mcp/blob/main/src/aws-serverless-mcp-server/README.md#available-tools) for the full list of tools and resources.

## Best practices and considerations

When building serverless applications with the AWS Serverless MCP Server, start by using its AI-assisted guidance for architectural decisions. Throughout development, use its guidance tools to make informed decisions about service selection, event patterns, and infrastructure design. Before deploying to AWS, use the Serverless MCP Server’s local testing capabilities to validate your application’s behavior. This approach helps ensure your application aligns with AWS best practices.

Robust monitoring and observability are critical to reliably operate your applications running in production. Use the Serverless MCP Server tools for deployment monitoring and setting up logging and metrics. This helps track application performance and quickly identify potential issues.

## Conclusion

The open-source AWS Serverless MCP Server streamlines serverless application development by providing AI-assisted guidance throughout the development lifecycle. By combining AI assistance with serverless expertise, it enables developers to build and deploy applications more efficiently. The Serverless MCP Server’s toolset supports the complete development process, from initialization to observability, while helping developers implement AWS best practices.

As organizations continue to adopt serverless computing, tools that streamline development and accelerate delivery become increasingly valuable. AWS will continue to expand the collection of MCP servers for developers building serverless applications and refine existing tools based on customer feedback and emerging serverless development patterns.

To get started, visit the [GitHub repository](https://github.com/awslabs/mcp/tree/main/src/aws-serverless-mcp-server) and explore the [documentation](https://github.com/awslabs/mcp/blob/main/src/aws-serverless-mcp-server/README.md). Share your experiences and suggestions through the GitHub repository to improve the MCP server’s capabilities and help shape the future of AI-assisted serverless development.

For more serverless learning resources, visit [Serverless Land](https://serverlessland.com/).

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