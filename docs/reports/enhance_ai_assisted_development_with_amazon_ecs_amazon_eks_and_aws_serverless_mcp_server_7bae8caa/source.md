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

# Enhance AI-assisted development with Amazon ECS, Amazon EKS and AWS Serverless MCP server

by Elizabeth Fuentes on 29 MAY 2025 in [Amazon Elastic Container Service](https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-service/ "View all posts in Amazon Elastic Container Service"), [Amazon Elastic Kubernetes Service](https://aws.amazon.com/blogs/aws/category/compute/amazon-kubernetes-service/ "View all posts in Amazon Elastic Kubernetes Service"), [Amazon Q](https://aws.amazon.com/blogs/aws/category/amazon-q/ "View all posts in Amazon Q"), [Amazon Q Developer](https://aws.amazon.com/blogs/aws/category/amazon-q/amazon-q-developer/ "View all posts in Amazon Q Developer"), [AWS Lambda](https://aws.amazon.com/blogs/aws/category/compute/aws-lambda/ "View all posts in AWS Lambda"), [Compute](https://aws.amazon.com/blogs/aws/category/compute/ "View all posts in Compute"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Serverless](https://aws.amazon.com/blogs/aws/category/serverless/ "View all posts in Serverless") [Permalink](https://aws.amazon.com/blogs/aws/enhance-ai-assisted-development-with-amazon-ecs-amazon-eks-and-aws-serverless-mcp-server/)  [Comments](https://aws.amazon.com/blogs/aws/enhance-ai-assisted-development-with-amazon-ecs-amazon-eks-and-aws-serverless-mcp-server/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re introducing specialized [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) servers for [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/), [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/), and [AWS Serverless](https://aws.amazon.com/serverless/), now available in the [AWS Labs GitHub repository](https://github.com/awslabs/mcp). These open source solutions extend AI development assistants capabilities with real-time, contextual responses that go beyond their pre-trained knowledge. While [Large Language Models (LLM)](https://aws.amazon.com/what-is/large-language-model/) within AI assistants rely on public documentation, MCP servers deliver current context and service-specific guidance to help you prevent common deployment errors and provide more accurate service interactions.

You can use these open source solutions to develop applications faster, using up-to-date knowledge of [Amazon Web Services (AWS)](https://aws.amazon.com/) capabilities and configurations during the build and deployment process. Whether you’re writing code in your [integrated development environment (IDE)](https://console.aws.amazon.com/), or debugging production issues, these MCP servers support AI code assistants with deep understanding of Amazon ECS, Amazon EKS, and AWS Serverless capabilities, accelerating the journey from code to production. They work with popular AI-enabled IDEs, including [Amazon Q Developer on the command line (CLI)](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line.html), to help you build and deploy applications using natural language commands.

* The [Amazon ECS MCP Server](https://awslabs.github.io/mcp/servers/ecs-mcp-server/) containerizes and deploys applications to Amazon ECS within minutes by configuring all relevant AWS resources, including load balancers, networking, auto-scaling, monitoring, Amazon ECS task definitions, and services. Using natural language instructions, you can manage cluster operations, implement auto-scaling strategies, and use real-time troubleshooting capabilities to identify and resolve deployment issues quickly.
* For Kubernetes environments, the [Amazon EKS MCP Server](https://awslabs.github.io/mcp/servers/eks-mcp-server/) provides AI assistants with up-to-date, contextual information about your specific EKS environment. It offers access to the latest EKS features, knowledge base, and cluster state information. This gives AI code assistants more accurate, tailored guidance throughout the application lifecycle, from initial setup to production deployment.
* The [AWS Serverless MCP Server](https://awslabs.github.io/mcp/servers/aws-serverless-mcp-server/) enhances the serverless development experience by providing AI coding assistants with comprehensive knowledge of serverless patterns, best practices, and AWS services. Using [AWS Serverless Application Model Command Line Interface (AWS SAM CLI)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli.html) integration, you can handle events and deploy infrastructure while implementing proven architectural patterns. This integration streamlines function lifecycles, service integrations, and operational requirements throughout your application development process. The server also provides contextual guidance for infrastructure as code decisions, [AWS Lambda](https://aws.amazon.com/lambda/) specific best practices, and event schemas for AWS Lambda event source mappings.

**Let’s see it in action**

If this is your first time using AWS MCP servers, visit the [Installation and Setup guide in the AWS Labs GitHub repository](https://github.com/awslabs/mcp?tab=readme-ov-file#installation-and-setup) to installation instructions. Once installed, add the following MCP server configuration to your local setup:

Install [Amazon Q for command line](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html) and add the conﬁguration to `~/.aws/amazonq/mcp.json`. If you’re already an Amazon Q CLI user, add only the configuration.

```
{
  "mcpServers": {
    "awslabs.aws-serverless-mcp":  {
      "command": "uvx",
      "args": ["awslabs.aws-serverless_mcp_server@latest"]
    },
    "awslabs.ecs-mcp-server": {
      "disabled": false,
      "command": "uvx",
      "args": ["awslabs.ecs-mcp-server@latest"]
    },
    "awslabs.eks-mcp-server": {
      "disabled": false,
      "command": "uv",
      "args": ["awslabs.eks-mcp-server@latest"]
    }
  }
}
```

For this demo I’m going to use the Amazon Q CLI to create an application that understands video using `[02_using_converse_api.ipynb](https://github.com/aws-samples/amazon-nova-samples/blob/main/multimodal-understanding/getting-started/02_using_converse_api.ipynb)` from [Amazon Nova model cookbook repository](https://github.com/aws-samples/amazon-nova-samples) as sample code. To do this, I send the following prompt:

`I want to create a backend application that automatically extracts metadata and understands the content of images and videos uploaded to an S3 bucket and stores that information in a database. I'd like to use a serverless system for processing. Could you generate everything I need, including the code and commands or steps to set up the necessary infrastructure, for it to work from start to finish? - Use 02_using_converse_api.ipynb as example code for the image and video understanding.`

Amazon Q CLI identifies the necessary tools, including the MCP server`awslabs.aws-serverless-mcp-server`. Through a single interaction, the AWS Serverless MCP server determines all requirements and best practices for building a robust architecture.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/28/new_serveless.jpg)

I ask to Amazon Q CLI that build and test the application, but encountered an error. Amazon Q CLI quickly resolved the issue using available tools. I verified success by checking the record created in the [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) table and testing the application with the [dog2.jpeg file](https://github.com/aws-samples/amazon-nova-samples/blob/main/multimodal-understanding/getting-started/media/dog2.jpeg?raw=true).

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/26/analysis_dog.jpg)

To enhance video processing capabilities, I decided to migrate my media analysis application to a containerized architecture. I used this prompt:

`I'd like you to create a simple application like the media analysis one, but instead of being serverless, it should be containerized. Please help me build it in a new CDK stack.`

Amazon Q Developer begins building the application. I took advantage of this time to grab a coffee. When I returned to my desk, coffee in hand, I was pleasantly surprised to find the application ready. To ensure everything was up to current standards, I simply asked:

`please review the code and all app using the awslabsecs_mcp_server tools`

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/26/ecs_review.jpeg)

Amazon Q Developer CLI gives me a summary with all the improvements and a conclusion.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/26/ecs_conclusion-1024x197.jpeg)

I ask it to make all the necessary changes, once ready I ask Amazon Q developer CLI to deploy it in my account, all using natural language.

After a few minutes, I review that I have a complete containerized application from the S3 bucket to all the necessary networking.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/26/Screenshot-2025-05-26-at-7.57.14 PM.png)

I ask Amazon Q developer CLI to test the app send it [the-sea.mp4 video file](https://github.com/aws-samples/amazon-nova-samples/blob/main/multimodal-understanding/getting-started/media/the-sea.mp4) and received a timed out error, so Amazon Q CLI decides to use the `fetch_task_logs` from `awslabsecs_mcp_server` tool to review the logs, identify the error and then fix it.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/27/error_eks.jpeg)

After a new deployment, I try it again, and the application successfully processed the video file

I can see the records in my Amazon DynamoDB table.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/26/videotest.jpeg)

To test the Amazon EKS MCP server, I have code for a web app in the auction-website-main folder and I want to build a web robust app, for that I asked Amazon Q CLI to help me with this prompt:

`Create a web application using the existing code in the auction-website-main folder. This application will grow, so I would like to create it in a new EKS cluster`

Once the Docker file is created, Amazon Q CLI identifies `generate_app_manifests` from `awslabseks_mcp_server` as a reliable tool to create a Kubernetes manifests for the application.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/27/docker_1.jpeg)

Then create a new EKS cluster using the `manage_eks_staks` tool.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/27/docker_2.jpeg)

Once the app is ready, the Amazon Q CLI deploys it and gives me a summary of what it created.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/27/docker_3.jpeg)

I can see the cluster status in the console.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/27/console_eks.jpeg)

After a few minutes and resolving a couple of issues using the `search_eks_troubleshoot_guide` tool the application is ready to use.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/27/eks_done.jpeg)

Now I have a Kitties marketplace web app, deployed on Amazon EKS using only natural language commands through Amazon Q CLI.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/27/kitty_place.jpeg)

**Get started today**

Visit the [AWS Labs GitHub repository](https://github.com/awslabs/mcp?tab=readme-ov-file#installation-and-setup) to start using these AWS MCP servers and enhance your AI-powered developmen there. The repository includes implementation guides, example configurations, and additional specialized servers [to run AWS Lambda function](https://github.com/awslabs/mcp/tree/main?tab=readme-ov-file#aws-lambda-mcp-server), which transforms your existing AWS Lambda functions into AI-accessible tools without code modifications, and [Amazon Bedrock Knowledge Bases Retrieval MCP server](https://github.com/awslabs/mcp/tree/main?tab=readme-ov-file#amazon-bedrock-knowledge-bases-retrieval-mcp-server), which provides seamless access to your Amazon Bedrock knowledge bases. Other [AWS specialized servers](https://github.com/awslabs/mcp?tab=readme-ov-file#installation-and-setup) in the repository include documentation, example configurations, and implementation guides to begin building applications with greater speed and reliability.

To learn more about MCP Servers for AWS Serverless and Containers and how they can transform your AI-assisted application development, visit the [Introducing AWS Serverless MCP Server: AI-powered development for modern applications](https://aws.amazon.com/blogs/compute/introducing-aws-serverless-mcp-server-ai-powered-development-for-modern-applications/), [Automating AI-assisted container deployments with the Amazon ECS MCP Server](https://aws.amazon.com/blogs/containers/automating-ai-assisted-container-deployments-with-amazon-ecs-mcp-server/), and [Accelerating application development with the Amazon EKS MCP server](https://aws.amazon.com/blogs/containers/accelerating-application-development-with-the-amazon-eks-model-context-protocol-server/) deep-dive blogs.

— [Eli](https://www.linkedin.com/in/lizfue/)

![Elizabeth Fuentes](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2024/06/03/Elizabeth-Fuentas.jpeg)

### Elizabeth Fuentes

My mission is to break down complex concepts into easily digestible explanations, inspiring developers to continually expand their skills and knowledge. Through conferences, tutorials, and online resources, I share my expertise with the global developer community, providing them with the tools and confidence to reach their full potential. With a hands-on approach and a commitment to simplifying the complex, I strive to be a catalyst for growth and learning in the world of AWS technology.

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