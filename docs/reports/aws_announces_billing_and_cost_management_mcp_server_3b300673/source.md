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

## [AWS Cloud Financial Management](https://aws.amazon.com/blogs/aws-cloud-financial-management/)

# AWS Announces Billing and Cost Management MCP Server

by Adam Richter and Aneesh Varghese on 22 AUG 2025 in [Announcements](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/post-types/announcements/ "View all posts in Announcements"), [AWS Cloud Financial Management](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/aws-cloud-financial-management/ "View all posts in AWS Cloud Financial Management"), [AWS Compute Optimizer](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/management-tools/aws-compute-optimizer/ "View all posts in AWS Compute Optimizer"), [Cloud Cost Optimization](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/business-intelligence/cloud-cost-optimization/ "View all posts in Cloud Cost Optimization") [Permalink](https://aws.amazon.com/blogs/aws-cloud-financial-management/aws-announces-billing-and-cost-management-mcp-server/) Share

## Introduction

Unlocking FinOps capabilities for modern cloud teams just got simpler with the introduction of the [AWS Billing and Cost Management Model Context Protocol (MCP) server](https://awslabs.github.io/mcp/servers/billing-cost-management-mcp-server/), which makes advanced cost analysis and optimization features directly available to your favorite AI assistant or chatbot. By integrating natural language queries, secure local credentials, and real-time access to your AWS account’s cost and usage data, the MCP server empower you to interactively analyze costs, identify savings opportunities, and perform detailed FinOps audits without navigating complex consoles or writing custom scripts. Whether asking about last month’s top spending services or discovering actionable recommendations for resource optimization, these capabilities streamline cost transparency and operational efficiency, making cloud financial management faster and easier.

## How the Billing and Cost Management MCP Server Works

The Billing and Cost Management MCP Server (billing-cost-management-mcp-server) provides a standardized way for AI agents to connect to real-time data sources. It works by creating a bridge between your AI Assistants and [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/), [AWS Cost Optimization Hub](https://aws.amazon.com/aws-cost-management/cost-optimization-hub/), [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/), [AWS Savings Plans](https://aws.amazon.com/savingsplans/), [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/), [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-lens/), and [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/). The MCP server will translate your natural language questions, parse your requirements, query the relevant services, process the multi-service output, and provide a consolidated response that is easy-to-understand.

## Why Use It?

If you are managing cloud costs and aiming to make smarter financial decisions with less effort, the Billing and Cost Management MCP server is the tool you need to accelerate your productivity. With this tool, you can directly access AWS cost analysis and optimization capabilities through your preferred AI assistant or chatbots. This means you can run complex cost queries simply by asking in natural language, without touching a console or writing custom scripts. Whether you are a cloud financial analyst, a cloud architect, a DevOps engineer, or part of a FinOps team, you will find it easier to monitor spending, identify savings opportunities, and keep your cloud resources running efficiently. You benefit from real-time access to your AWS financial data, improved transparency into where your budget is going, and actionable insights you can put into practice immediately. By streamlining workflows and making deep cost analysis faster and more accessible, the Billing and Cost Management MCP server puts you in control of your cloud financial management.

## How to Get Started

Different MCP hosts, such as Amazon Q Developer CLI, Claude Desktop, Kiro, and other MCP compatible tools integrate with [billing-cost-management-mcp-server](https://github.com/awslabs/mcp/tree/main/src/billing-cost-management-mcp-server). In this post we focus on Amazon Q Developer CLI example.

### Prerequisites

* AWS account with [Cost Explorer Enabled](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html)
* Install [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [verify access](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-configure.html) to AWS account via AWS CLI
* Verify [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) user has permissions for services mentioned in the post
* Apply [least-privilege principle](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) for IAM permissions
* (optional) Install [Amazon Q for command line](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html). Refer to [supported command line environments](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-supported-envs.html) before installation
* Install `uv` from [Astral](https://docs.astral.sh/uv/getting-started/installation/) or the [GitHub README](https://github.com/astral-sh/uv#installation)
* Install Python using `uv python install 3.12`
* Configure AWS credentials with access to required services
* Add the server to your MCP client configuration

#### Storage Lens

For MCP tools calls that use storage lens data, the prerequisites below will also be required.

Storage Lens Dashboard with Export Enabled:

* You must have a Storage Lens dashboard configured with metrics export enabled
* The export must be configured to write to an S3 bucket in CSV or Parquet format

AWS Permissions:

* S3 permissions to read the manifest and data files
* Athena permissions to create databases, tables, and run queries
* Glue permissions for the Athena catalog

Configure the MCP server in your MCP client configuration. For Amazon Q Developer CLI add the servers to your `~/.aws/amazonq/mcp.json` file

**For Linux/MacOS Users:**

```
{
  "mcpServers": {
    "awslabs.billing-cost-management-mcp-server": {
      "command": "uvx",
      "args": [
         "awslabs.billing-cost-management-mcp-server@latest"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR",
        "AWS_PROFILE": "your-aws-profile",
        "AWS_REGION": "us-east-1"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

**For Windows Users:**

```
{
  "mcpServers": {
    "awslabs.billing-cost-management-mcp-server": {
      "command": "uvx",
      "args": [
         "--from",
         "awslabs.billing-cost-management-mcp-server@latest",
         "awslabs.billing-cost-management-mcp-server.exe"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR",
        "AWS_PROFILE": "your-aws-profile",
        "AWS_REGION": "us-east-1"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

For other Docker Deployment and IDE for Teams, Please refer to [AWS MCP Servers GitHub repository Installation guide](https://awslabs.github.io/mcp/installation)

### Cost Considerations

AWS service APIs incurs charges on a per-request basis. Each API call made by this MCP server will result in charges to your AWS account. For current pricing information review the respective services API pricing.

## Examples

### What is my current AWS service cost utilization?

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/20/example1-1024x513.png)

Figure 1: MCP response showing current AWS service cost utilization.

### Get cost optimization recommendations and show details for the highest savings recommendation.

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/20/example2-1024x539.png)

Figure 2: MCP response showing optimization recommendations with the highest savings

### Compare spend across all AWS regions

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/20/example3-1-1024x481.png)

Figure 3: MCP response showing spend across AWS regions

### Perform a cost comparison analysis between June and July 2025 to identify and quantify any significant changes or variations in my AWS spending

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/20/example4-2-1024x538.png)

Figure 4: MCP response comparing costs between June and July 2025

### Evaluate the potential cost savings of migrating my existing AWS workloads to Graviton-based instances

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/20/example5-1-1024x350.png)

Figure 5: MCP response about Graviton costs

### Conduct a thorough analysis to determine the reasons behind the increase in costs during July 2025 and identify the underlying root causes.

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/22/example_analysis-1024x662.png)

Figure 6: MCP response showing cost drivers

### Provide the cost per GB-month for S3 storage over the past six months

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/22/example_cost_per_gb_s3-1024x298.png)

Figure 7: MCP response showing S3 Cost per GB

### I would like you to generate a comprehensive cost analysis for my largest S3 bucket with detailed breakdown of the associated costs

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/22/example_s3_comp1-1024x501.png)

Figure 8: MCP response showing S3 Comprehensive Response

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/22/example_s3_comp2-1024x544.png)

Figure 9: MCP response showing S3 Comprehensive Response

The following examples demonstrate detailed tool utilization within the MCP, showcasing how various integrations generate comprehensive responses. Additionally, the MCP can be leveraged through Claude Desktop to enhance output visualization and provide richer interactive experiences for developers working with AWS services.

### Analyze my cost data over the last few months and compile a narrative, 2-paragraph report ready for senior IT and finance leadership. The report should discuss cost trends, drivers of any major changes, cost anomalies, how we’re tracking against budgets, and what opportunities we have to optimize and lower costs.

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/22/q1-1024x455.png)

Figure 10: MCP prompt and response for a narrative showing the detailed tool calls

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/22/q2-1024x590.png)

Figure 11: MCP response additional tool calls

### Claude Desktop (using Sonnet 4)

#### What was my EC2 cost per vCPU hour last month?

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/22/claude1-1024x980.png)

Figure 12: MCP response from Claude Desktop showing vCPU hours

#### Can you double check those vCPU counts using the pricing tool?

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/22/claude2-1024x1021.png)

Figure 13: MCP response from Claude Desktop including vCPU pricing

#### Cool. Can you repeat this analysis for the past 6 months please?

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/22/claude3-1024x1021.png)

Figure 14: MCP response from Claude Desktop analyzing a six month time frame

#### wonderful. Can you put this in a line chart for me?

![](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/08/22/claude4-878x1024.png)

Figure 15: MCP response from Claude Desktop showing Cost per vCPU hour chart

## Conclusion

The AWS Billing and Cost Management MCP Server marks a major step forward in cloud financial management. It connects powerful AWS cost analysis and optimization tools with natural language AI assistants. This makes complex cost queries simple and speeds up FinOps workflows. It also improves cost transparency so you can easily access real-time insights and actionable recommendations.

![Adam Richter](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/03/12/adaricht_avatar.jpg)

### Adam Richter

Adam Richter is a Senior Optimization Solutions Architect with AWS OPTICS, where he focuses on AI cost optimization and FinOps best practices. He has helped shape customer-facing features such as Amazon Q Business and Amazon Q Developer, and frequently shares his expertise as a speaker at AWS re:Invent and other industry events. Adam also represents AWS in the FinOps Foundation AI Working Group, contributing to the broader conversation on financial operations in AI.

![Aneesh Varghese](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2024/06/19/vaneesh.jpg)

### Aneesh Varghese

Aneesh Varghese is a Senior Technical Account Manager at AWS with more than 19 years of Information Technology industry experience. Aneesh supports enterprise customers in cost optimization strategies, Cloud operations, MLOps, providing advocacy and strategic technical guidance to help plan and build solutions using AWS best practices. Outside of work, Aneesh likes to spend time with family, play Basketball and Badminton

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