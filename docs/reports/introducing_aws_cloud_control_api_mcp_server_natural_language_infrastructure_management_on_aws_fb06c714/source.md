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

# Introducing AWS Cloud Control API MCP Server: Natural Language Infrastructure Management on AWS

by Kevon Mayers and Brian Terry on 13 AUG 2025 in [Amazon Q Developer](https://aws.amazon.com/blogs/devops/category/amazon-q/amazon-q-developer/ "View all posts in Amazon Q Developer"), [Announcements](https://aws.amazon.com/blogs/devops/category/post-types/announcements/ "View all posts in Announcements"), [Customer Solutions](https://aws.amazon.com/blogs/devops/category/post-types/customer-solutions/ "View all posts in Customer Solutions"), [DevOps](https://aws.amazon.com/blogs/devops/category/devops/ "View all posts in DevOps"), [Featured](https://aws.amazon.com/blogs/devops/category/featured/ "View all posts in Featured"), [Generative AI](https://aws.amazon.com/blogs/devops/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Launch](https://aws.amazon.com/blogs/devops/category/news/launch/ "View all posts in Launch"), [Provisioning and orchestration](https://aws.amazon.com/blogs/devops/category/management-and-governance/provisioning-and-orchestration/ "View all posts in Provisioning and orchestration"), [Top Posts](https://aws.amazon.com/blogs/devops/category/top-posts/ "View all posts in Top Posts") [Permalink](https://aws.amazon.com/blogs/devops/introducing-aws-cloud-control-api-mcp-server-natural-language-infrastructure-management-on-aws/) Share

Today, we’re officially announcing the [**AWS Cloud Control API (CCAPI) MCP Server**](https://awslabs.github.io/mcp/servers/ccapi-mcp-server). This MCP server transforms AWS infrastructure management by allowing developers to create, read, update, delete, and list resources using natural language. As part of the [awslabs/mcp](https://github.com/awslabs/mcp) project, this new and innovative tool serves as a bridge between natural language commands and AWS infrastructure deployment and management. This MCP server is powered by the [**AWS Cloud Control API**](https://aws.amazon.com/cloudcontrolapi/) – a standardized API that allows CRUDL (Create/Read/Update/Delete/List) operations to be performed against AWS and third party resources using a single endpoint.

### **Key Features:**

* Leverages AWS Cloud Control API for CRUDL operations for more than 1,200 AWS resources
* Enables LLM-powered agents and developers to manage infrastructure with natural language prompts
* Provides the option to output Infrastructure as Code (IaC) templates for infrastructure it will create, allowing to still be used with existing CI/CD pipelines
* Integrates with AWS Pricing API to provide cost estimates for the infrastructure it will create
* Applies security best practices automatically using [Checkov](https://www.checkov.io/)

## Why Use CCAPI MCP Server?

* **Simplified Infrastructure Management**: No more wrestling with complex templates or documentation
* **Increased Developer Productivity**: Focus on what you need, not how to configure it
* **Reduced Learning Curve**: Onboard new team members faster with natural language commands
* **LLM Integration**: Perfect companion for AI-assisted development workflows

The CCAPI MCP Server transforms infrastructure management by enabling natural language interactions for AWS resource operations. Bridging natural language commands with AWS infrastructure deployment and management, this MCP Server allows developers to manage cloud infrastructure through conversational inputs such as:

* `Can you create a new s3 bucket for me?`or
* `Find all of my EC2 instances and tell me which one have an instance type that is not t2.large`

This significantly reduces configuration overhead and accelerates onboarding for new team members, directly translates developer intent into cloud infrastructure.

Let’s see it in action.

## Creating and Managing Cloud Infrastructure

### Prerequisites

* uv package manager installed
* Python 3.x.x installed
* AWS credentials with appropriate permissions. The MCP server supports multiple ways to define these credentials. See the [MCP documentation](https://awslabs.github.io/mcp/#aws-cloudformation-mcp-server) for more information. Using dynamic credentials such as one provided via SSO is recommended. For more information on configuring AWS credentials, see the [AWS CLI documentation](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html).
* An **MCP Host** application installed that supports MCP Clients and MCP Servers (e.g. Amazon Q Developer, Claude Desktop, Cursor, etc.). To follow this blog install [Amazon Q Developer for CLI](https://aws.amazon.com/developer/learning/q-developer-cli/) (CLI) as described in the [installation instructions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html)

### Integration with Developer Tools

To start using the CCAPI MCP server, you will need to set up your server configuration which is typically in a file named `mcp.json`. For this blog we will focus on using the CCAPI MCP server with [Amazon Q Developer](https://aws.amazon.com/q/developer/). Note that for other MCP Host applications the path to the mcp configuration file may differ. You will need to create the file if it does not already exist in the directory.

1. **Global Configuration**: `~/.aws/amazon/mcp.json` – Applies to all workspaces

2. **Workspace Configuration**: `.amazonq/mcp.json` – Specific to the current workspace

More information can be found in the [Amazon Q Developer User Guide](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-mcp-configuration.html).

### Configuration file structure

The MCP configuration file uses a JSON format with the following structure:

`mcp.json`

```
{
  "mcpServers": {
    "server-name": {
      "command": "command-to-run",
      "args": ["arg1", "arg1",],
      "env": {
        "ENV_VAR1": "value1",
        "ENV_VAR2": "value2",
      },
    }
  }
}
```

Here is mcp.json with the CCAPI MCP Server configuration:

```
{
  "mcpServers": {
   "awslabs.ccapi-mcp-server": {
      "command": "uvx",
      "args": [
        "awslabs.ccapi-mcp-server@latest"
      ],
      "env": {
        "AWS_PROFILE": "your named AWS profile",
	"DEFAULT_TAGS": “enabled”,
	"SECURITY_SCANNING": “enabled”,
	"FASTMCP_LOG_LEVEL": “ERROR”
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

### **Important**

Ensure you correctly set your AWS credentials in the MCP server config. It is essential that you properly configure these credentials, as the MCP server uses their associated permissions when invoking the AWS Cloud Control API for CRUDL operations in your AWS account. The server supports multiple methods of consuming these credentials such as AWS profiles, Environment Variables, SSO tokens, etc. You can see some of this in the [aws\_client.py](https://github.com/awslabs/mcp/blob/main/src/ccapi-mcp-server/awslabs/ccapi_mcp_server/aws_client.py) file. See [these docs](https://awslabs.github.io/mcp/servers/ccapi-mcp-server#configuration) on using named profiles for more information.

### **Read Only Mode**

If you would like to prevent the MCP server from performing mutating actions (e.g. Create/Update/Delete Resource), you can specify the `--readonly` flag as demonstrated below:

```
{
  "mcpServers": {
   "awslabs.ccapi-mcp-server": {
      "command": "uvx",
      "args": [
        "awslabs.ccapi-mcp-server@latest",
        “--readonly”"
      ],
      "env": {
        "AWS_PROFILE": "your named AWS profile",
	"DEFAULT_TAGS": “enabled”,
	"SECURITY_SCANNING": “enabled”,
	"FASTMCP_LOG_LEVEL": “ERROR”
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

More information on the configuration and tools the CCAPI MCP server provides can be found in the AWS CloudFormation MCP Server documentation.

### Security Considerations

* Ensure the IAM credentials include permissions for Cloud Control API actions (List, Get, Create, Update, Delete). See the AWS CCAPI API [documentation](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/security.html) for more info
* Follow IAM least privilege [principles](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)
* Enable [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) auditing
* Consider running in read-only mode with `--readonly` flag for safer operations

## Example Use Case: Creating an S3 Bucket with KMS Encryption

***IMPORTANT: Ensure you have satisfied all prerequisites before attempting these commands.***

1. With the `mcp.json` file correctly set, try to run a sample prompt. In your terminal, run q chat to start using Amazon Q in the CLI.

![Terminal screen showing 'q chat' command with AWS Labs CCAPI MCP Server loaded in 1.31 seconds. Shows ASCII art banner and 'Did you know?' tip about resuming conversations with 'q chat --resume'. Bottom shows help commands and indicates chatting with claude-3.7-sonnet.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/1-q-cli-initial-load.png) 2. This will start initializing the MCP servers in the background, allowing you to immediately start using Q Chat even if they are still loading. As a note, if these have not finished loading, your prompts will be handled without using any MCP servers. To check the status of the servers, run `/mcp`

![Terminal screen showing '/mcp' command being entered, with AWS Labs CCAPI MCP Server loaded confirmation and the same ASCII art banner displayed.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/2-q-cli-show-mcp-servers.png)

3. Once that you have validated that the MCP server was loaded successfully, try a sample command. Simply tell Amazon Q : `Create an S3 bucket with versioning and encrypt it using a new KMS key`

Amazon Q will use the server to automatically:

1. Fetch your current environment variables
2. Use those to fetch your current AWS session info
3. Create code that defines what is in your prompt
4. Explain the code that was generated
5. Run security analysis against the code that was generated (if enabled)
6. Explain the results of the security analysis
7. Validate the configuration against AWS Cloud Control API schemas (which use CloudFormation Resource Provider Schemas as their foundation) and IAM policies. This validation ensures compliance with Cloud Control API requirements, which is essential for resource creation
8. Create the resources directly through Cloud Control API

*Note: While CloudFormation schemas are referenced in the validation step, this solution uses Cloud Control API for resource management, not CloudFormation. The schemas are used because they define the standardized resource properties that Cloud Control API expects.*

4. First, Amazon Q will mention that it needs to check the environment variables to find information related to the AWS session information. It will inform you about the specific tool it aims to use and will ask for permission. Select `y` to accept and allow actions.

![Claude's response about helping create an S3 bucket with versioning and KMS encryption. Shows tool usage for 'check_environment_variables' from MCP server with JSON parameters, asking for permission to proceed with [y/n/t] options.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/3-q-cli-check-env-vars-request.png)

5. Next, Amazon Q will ask to use `get_aws_session_info()` to fetch information about the AWS session it should use for subsequent actions. It will use the relevant values from the environment variables defined in the MCP configuration file (e.g. `~/.aws/amazon/mcp.json`)

![Tool execution for 'get_aws_session_info' with environment token parameter, showing JSON structure and asking for permission to allow this action.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/4-q-cli-get-aws-session-info-request.png)

6.Amazon Q will then display the AWS account ID and region it will use to deploy resources. To start, it will use `generate_infrastructure_code()` to generate the resource properties for a KMS key that will be sent to Cloud Control API. These properties mirror the structure defined in AWS CloudFormation Resource Provider Schemas (which Cloud Control API uses as its foundation), allowing for security validation through Checkov before deployment. The key will be configured following security best practices, with a key policy scoped to only allow usage within the AWS account.

![AWS Session Information display showing Standard AWS Profile, masked Account ID, and us-east-1 region. Claude explains it will create KMS key first, then S3 bucket, followed by 'generate_infrastructure_code' tool usage with JSON parameters for KMS key creation including description, key usage, and policy details.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/5-q-cli-show-aws-inf-and-gen-infra-code-request.png)

7. Once that Amazon Q has generated the code for the resource, it will run then use the `explain()` tool to explain the infrastructure code that was generated. Note that default tags `MANAGED_BY`, `MCP_SERVER_SOURCE_CODE`, and `MCP_SERVER_VERSION` are added for all resources managed by the CCAPI MCP server. These tags provide for ease of identification of infrastructure that is being managed by the MCP server. They are configurable and you optionally can disable them, but we highly recommend adding tags to ensure you have visibility into infrastructure that is being managed by the CCAPI MCP server.

![Tool execution for 'explain' function showing generated code token, context for KMS key creation, and operation type as 'create', asking for permission to proceed.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/6-q-cli-explain-tool-request.png)

![Explanation screen showing 'KMS key creation for S3 bucket encryption - Create Operation' with configuration summary of 5 properties including Description, KeyUsage, KeySpec, KeyPolicy, and Tags. Shows default management tags in red box including MANAGED_BY, MCP_SERVER_SOURCE_CODE, and MCP_SERVER_VERSION.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/7-q-cli-explain-tool-response.png)

8. It will then attempt to use the `run_checkov()` tool to inspect the security of the code. This tool is triggered because `SECURITY_SCANNING` was set to enabled in your server configuration file.

![Claude initiating security scanning on the KMS key using 'run_checkov' tool with explained token parameter, asking for permission to proceed.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/8-q-cli-run-checkov-tool-request.png)

9. After Checkov has run, it will then attempt to use the `explain()` tool again to explain the security findings from the Checkov run. If there were no security issues, it will attempt to proceed. If there were security issues, you will be asked how you’d like to proceed, and Amazon Q will recommend necessary fixes. By default, the checks that passed will only give a minimal summary. If you’d like to get more information, just ask for more details.

![Tool execution for 'explain' showing security scan results with scan_status 'FAILED', displaying failed and passed security checks including rotation settings and wildcard principal policies.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/9-q-cli-explain-tool-checkov-request.png) ![Security scan results summary showing 'ISSUES FOUND' with 1 passed check and 1 failed check. Failed check is CKV_AWS_7 for KMS key rotation not enabled. Claude explains the security issue and offers three options: fix, proceed anyway, or cancel.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/10-q-cli-explain-tool-checkov-response.png)

10. The next tool that Amazon Q will use is the `create_resource()` tool. This tool will attempt to create the resource using the AWS Cloud Control API, and then use the `get_resource_request_status()` tool to check the status of the creation. This tool uses the request token to identify the request that was submitted to the Cloud Control API and uses this to fetch its status information.

![User responds 'you can keep going' and Claude proceeds with creating KMS key as-is. Shows 'create_resource' tool execution with resource type, credentials, and security scan tokens.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/11-q-cli-create-tool-kms-request.png) ![KMS key creation in progress message followed by 'get_resource_request_status' tool usage with request token to check the status.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/12-q-cli-get-resource-request-status-kms-request.png)

11. Amazon Q will continue using the CCAPI MCP server tools as needed until it finishes creation of both the S3 Bucket and KMS Key and will output a summary.

![Success message showing both resources created: KMS Key (1d58649e-22af-4ed2-a3ea-ab6e51fd9106) and S3 Bucket (cm1qstfl8fnts3nnptnofscax-6mwspsvaa0wa) with summary of features including versioning enabled, KMS encryption, public access blocked, and bucket key enabled.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/13-q-cli-finish-resource-creation.png)

12. Now, ask Amazon Q to make a change potentially negatively affecting security, for example by allowing the S3 bucket to be publicly accessible. While this configuration is generally advised against, sometimes it is necessary – such as when you want to use the S3 bucket for public website hosting. Amazon Q will respond letting you know that what you are asking for is not the best practice, and explain why. However, since this could be a valid request depending on your use case, it will prompt you to confirm.

![User requests bucket policy for worldwide access. Claude warns about significant security concerns, explaining the contradiction with current secure setup and offering three options: reconsider with specific users/roles, proceed anyway (not recommended), or create alternative restricted policy.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/14-q-cli-ask-for-s3-insecure-config.png)

13. The CCAPI MCP server also has integrations with the AWS Pricing API, so you can even ask for the estimated cost of what it has deployed.

![User requests cost estimate. Claude provides breakdown: KMS Key at $1/month plus usage costs, S3 Bucket storage at ~$0.023 per GB/month with request costs. Minimal monthly cost ~$1 if bucket empty, with usage-dependent scaling. Recommends AWS Pricing Calculator for precise estimates.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/15-q-cli-ask-for-cost-estimate.png)

14. Lastly, ask Amazon Q to create a CloudFormation template of what it has created so far so you can either have a backup, or if you want to redeploy something similar, you will have a template to work off. It will use the create\_template() tool to accomplish this task.

**Note**: The `create_template()` tool comes with predefined settings:

* Outputs YAML format by default (can be JSON)
* Sets DeletionPolicy to `RETAIN`
* Sets UpdateReplacePolicy to `RETAIN`
* Allows optional parameters for template ID, file saving location, and region specification

For more information, review the tool [in the source code](https://github.com/awslabs/mcp/blob/692a1d5be15aacea997d4cbe5dca51fa804611ee/src/ccapi-mcp-server/awslabs/ccapi_mcp_server/server.py#L526-L622).

![User requests CloudFormation template backup. Claude uses 'create_template' tool showing template name 's3-kms-backup-template' with resources array containing KMS Key and S3 Bucket resource types and identifiers.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/16-q-cli-ask-for-backup-cfn-template.png)

15. Try one more dangerous operation, attempting to delete all resources within an AWS account. The security checks block this attempt and suggest other alternatives.

![User requests to 'delete everything in my aws account'. Claude firmly refuses, explaining it would be extremely destructive and could cause permanent data loss, compliance violations, and business disruption. Offers to help delete only the specific resources created today instead.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/17-q-cli-ask-to-delete-everything-in-aws-account.png)

16. Finally, ask Amazon Q to just delete what it has created. This time it will use the `get_resource()` tool to get information about the existing resources it created, the `explain()` tool to explain the changes that will be made, and finally the `delete_resource()` tool to delete the resources.

![User clarifies to delete only what was created. Claude proceeds to delete resources, starting with S3 bucket using 'get_resource' tool with bucket identifier and resource type parameters.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/18-q-cli-ask-to-delte-just-what-it-made.png) ![Tool execution for 'explain' showing S3 bucket deletion context with identifier and resource type AWS::S3::Bucket, asking for permission to proceed.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/19-q-cli-explain-tool-delete-request.png)

![S3 bucket deletion operation summary showing configuration with 2 properties (identifier and resource_type), followed by 'delete_resource' tool execution with confirmed parameter set to true, asking for final permission to proceed.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/20-q-cli-explain-tool-output-and-delete-reqest.png)

After successfully deleting the resources, it will provide a final summary.

![Terminal output showing cleanup completion with green checkmarks. Text reads 'Cleanup Complete!' followed by 'Both resources have been successfully deleted:' with bullet points showing an S3 bucket and KMS key marked as DELETED. The message concludes that the AWS account is back to its original state with no ongoing costs.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/21-q-cli-cleanup-success.png)

### Sample Prompts for Easy Start

| Sample Prompt | What It Does |
| --- | --- |
| “Create a VPC with private and public subnets” | Sets up a complete network environment |
| “List all my EC2 instances” | Shows running instances across your account |
| “Create a serverless API for my application” | Deploys API Gateway with Lambda integration |
| “Set up a load-balanced web application” | Creates ALB with target groups and instances |

## Conclusion

The [AWS Cloud Control API MCP Server](https://awslabs.github.io/mcp/servers/ccapi-mcp-server/) represents a significant advancement in AWS infrastructure management, making operations on cloud resources easy to express and access through natural language. Whether you’re streamlining operations, experimenting with LLM-based development, or onboarding new team members, whether you are using Amazon Q Developer in CLI or any other MCP Host application (such as Claude Desktop or Cursor), the CCAPI MCP servet and its tools offer a truly intuitive way to interact with AWS.

## Authors

![Headshot of Kevon Mayers, Infrastructure as Code Focus Area Lead and Games Solutions Architect, AWS](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/14/Screenshot-2025-08-14-at-3.08.43 PM.png)

### Kevon Mayers

[Kevon Mayers](https://www.linkedin.com/in/kevonmayers)  is a Games Solutions Architect at AWS and is the Infrastructure as Code (IaC) Focus Area Lead for the NextGen Developer Experience Technical Field Community at AWS. Kevon is a Core Contributor for Terraform and has led multiple Terraform initiatives within AWS. Prior to joining AWS, he was working as a DevOps engineer and developer, and before that was working with the GRAMMYs/The Recording Academy as a studio manager, music producer, and audio engineer. He also owns a professional production company, [MM Productions](https://mmproductionsfl.com/).

![Image of Brian Terry, Sr. Data & AI Partner Solutions Architect, AWS](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/08/09/brian-terry.jpg)

### Brian Terry

[Brian Terry](https://www.linkedin.com/in/brian-t-b3276250/), Senior WW Data & AI PSA, is an innovation leader with 20+ years of experience in technology and engineering. Pursuing a Ph.D. in Computer Science at the University of North Dakota. Brian has spearheaded generative AI projects, optimized infrastructure scalability, and driven partner integration strategies. He is passionate about leveraging technology to deliver scalable, resilient solutions that foster business growth and innovation.

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