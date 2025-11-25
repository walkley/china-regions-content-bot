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

## [Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/)

# Build AWS architecture diagrams using Amazon Q CLI and MCP

by Joel Asante, Varun Jasti, and Dunieski Otano on 30 JUN 2025 in [Amazon Q Developer](https://aws.amazon.com/blogs/machine-learning/category/amazon-q/amazon-q-developer/ "View all posts in Amazon Q Developer"), [Best Practices](https://aws.amazon.com/blogs/machine-learning/category/post-types/best-practices/ "View all posts in Best Practices"), [Generative AI](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Technical How-to](https://aws.amazon.com/blogs/machine-learning/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/machine-learning/build-aws-architecture-diagrams-using-amazon-q-cli-and-mcp/)  [Comments](https://aws.amazon.com/blogs/machine-learning/build-aws-architecture-diagrams-using-amazon-q-cli-and-mcp/#Comments)  Share

Creating professional AWS architecture diagrams is a fundamental task for solutions architects, developers, and technical teams. These diagrams serve as essential communication tools for stakeholders, documentation of compliance requirements, and blueprints for implementation teams. However, traditional diagramming approaches present several challenges:

* **Time-consuming process** – Creating detailed architecture diagrams manually can take hours or even days
* **Steep learning curve** – Learning specialized diagramming tools requires significant investment
* **Inconsistent styling** – Maintaining visual consistency across multiple diagrams is difficult
* **Outdated AWS icons** – Keeping up with the latest AWS service icons and best practices challenging.
* **Difficult maintenance** – Updating diagrams as architectures evolve can become increasingly burdensome

[Amazon Q Developer CLI](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line.html) with the [Model Context Protocol (MCP)](https://www.anthropic.com/news/model-context-protocol) offers a streamlined approach to creating AWS architecture diagrams. By using generative AI through natural language prompts, architects can now generate professional diagrams in minutes rather than hours, while adhering to AWS best practices.

In this post, we explore how to use Amazon Q Developer CLI with the [AWS Diagram MCP](https://awslabs.github.io/mcp/servers/aws-diagram-mcp-server/) and the [AWS Documentation MCP](https://awslabs.github.io/mcp/servers/aws-documentation-mcp-server/) servers to create sophisticated architecture diagrams that follow AWS best practices. We discuss techniques for basic diagrams and real-world diagrams, with detailed examples and step-by-step instructions.

## **Solution overview**

Amazon Q Developer CLI is a command line interface that brings the generative AI capabilities of [Amazon Q](https://aws.amazon.com/q/) directly to your terminal. Developers can interact with Amazon Q through natural language prompts, making it an invaluable tool for various development tasks.

Developed by Anthropic as an open protocol, the [Model Context Protocol (MCP)](https://www.anthropic.com/news/model-context-protocol) provides a standardized way to connect AI models to virtually any data source or tool. Using a [client-server architecture](https://modelcontextprotocol.io/introduction#general-architecture) (as illustrated in the following diagram), the MCP helps developers expose their data through lightweight MCP servers while building AI applications as MCP clients that connect to these servers.

The MCP uses a client-server architecture containing the following components:

* **Host** – A program or AI tool that requires access to data through the MCP protocol, such as Anthropic’s Claude Desktop, an integrated development environment (IDE), AWS MCP CLI, or other AI applications
* **Client** – Protocol clients that maintain one-to-one connections with server
* **Server** – Lightweight programs that expose capabilities through standardized MCP or act as tools
* **Data sources** – Local data sources such as databases and file systems, or external systems available over the internet through APIs (web APIs) that MCP servers can connect with

![mcp-architectinfo](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/18/mcpinfo-1024x694.png)

[As announced in April 2025](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-q-developer-cli-model-context-protocol/), MCP enables [Amazon Q Developer](https://aws.amazon.com/q/developer/) to connect with specialized servers that extend its capabilities beyond what’s possible with the base model alone. MCP servers act as plugins for Amazon Q, providing domain-specific knowledge and functionality. The AWS Diagram MCP server specifically enables Amazon Q to generate architecture diagrams using the Python diagrams package, with access to the complete AWS icon set and architectural best practices.

## **Prerequisites**

To implement this solution, you must have an AWS account with appropriate permissions and follow the steps below.

## **Set up your environment**

Before you can start creating diagrams, you need to set up your environment with Amazon Q CLI, the AWS Diagram MCP server, and AWS Documentation MCP server. This section provides detailed instructions for installation and configuration.

### **Install Amazon Q Developer CLI**

Amazon Q Developer CLI is available as a standalone installation. Complete the following steps to install it:

1. Download and install Amazon Q Developer CLI. For instructions, see Using Amazon Q Developer on the command line.
2. Verify the installation by running the following command: `q --version`

   *You should see output similar to the following: Amazon Q Developer CLI version 1.x.x*
3. Configure Amazon Q CLI with your AWS credentials: `q login`
4. Choose the login method suitable for you:
   * [Use for free with AWS Builder ID](https://docs.aws.amazon.com/signin/latest/userguide/sign-in-aws_builder_id.html)
   * [Use with Pro license](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-pro-tier.html)

### **Set up MCP servers**

Complete the following steps to set up your MCP servers:

1. Install uv using the following command: `pip install uv`
2. Install Python 3.10 or newer: `uv python install 3.10`
3. Install [GraphViz](https://www.graphviz.org/download/) for your operating system.
4. Add the servers to your `~/.aws/amazonq/mcp.json` file:

```
{
  "mcpServers": {
    "awslabs.aws-diagram-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-diagram-mcp-server"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "autoApprove": [],
      "disabled": false
    },
    "awslabs.aws-documentation-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-documentation-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "autoApprove": [],
      "disabled": false
    }
  }
}
```

Now, Amazon Q CLI automatically discovers MCP servers in the `~/.aws/amazonq/mcp.json` file.

## **Understanding MCP server tools**

The AWS Diagram MCP server provides several powerful tools:

* **list\_icons** – Lists available icons from the diagrams package, organized by provider and service category
* **get\_diagram\_examples** – Provides example code for different types of diagrams (AWS, sequence, flow, class, and others)
* **generate\_diagram** – Creates a diagram from Python code using the diagrams package

The AWS Documentation MCP server provides the following useful tools:

* **search\_documentation** – Searches AWS documentation using the official AWS Documentation Search API
* **read\_documentation** – Fetches and converts AWS documentation pages to markdown format
* **recommend** – Gets content recommendations for AWS documentation pages

These tools work together to help you create accurate architecture diagrams that follow AWS best practices.

## **Test your setup**

Let’s verify that everything is working correctly by generating a simple diagram:

1. Start the Amazon Q CLI chat interface and verify the output shows the MCP servers being loaded and initialized: `q chat`

   ![q chat](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/18/q-chat.png)
2. In the chat interface, enter the following prompt:

   `Please create a diagram showing an EC2 instance in a VPC connecting to an external S3 bucket. Include essential networking components (VPC, subnets, Internet Gateway, Route Table), security elements (Security Groups, NACLs), and clearly mark the connection between EC2 and S3. Label everything appropriately concisely and indicate that all resources are in the us-east-1 region. Check for AWS documentation to ensure it adheres to AWS best practices before you create the diagram.`
3. Amazon Q CLI will ask you to trust the tool that is being used; enter `t` to trust it.Amazon Q CLI will generate and display a simple diagram showing the requested architecture. Your diagram should look similar to the following screenshot, though there might be variations in layout, styling, or specific details because it’s created using generative AI. The core architectural components and relationships will be represented, but the exact visual presentation might differ slightly with each generation.

   ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/19/ec2-to-s3-architecture-1024x487-1.png)

   If you see the diagram, your environment is set up correctly. If you encounter issues, verify that Amazon Q CLI can access the MCP servers by making sure you installed the necessary tools and the servers are in the `~/.aws/amazonq/mcp.json` file.

### **Configuration options**

The AWS Diagram MCP server supports several configuration options to customize your diagramming experience:

* **Output directory** – By default, diagrams are saved in a generated-diagrams directory in your current working directory. You can specify a different location in your prompts.
* **Diagram format** – The default output format is PNG, but you can request other formats like SVG in your prompts.
* **Styling options** – You can specify colors, shapes, and other styling elements in your prompts.

Now that our environment is set up, let’s create more diagrams.

## **Create AWS architecture diagrams**

In this section, we walk through the process of multiple AWS architecture diagrams using Amazon Q CLI with the AWS Diagram MCP server and AWS Documentation MCP server to make sure our requirements follow best practices.

When you provide a prompt to Amazon Q CLI, the AWS Diagram and Documentation MCP servers complete the following steps:

1. Interpret your requirements.
2. Check for best practices on the AWS documentation.
3. Generate Python code using the diagrams package.
4. Execute the code to create the diagram.
5. Return the diagram as an image.

*This process happens seamlessly, so you can focus on describing what you want rather than how to create it.*

**AWS architecture diagrams typically include the following components:**

* **Nodes** – AWS services and resources
* **Edges** – Connections between nodes showing relationships or data flow
* **Clusters** – Logical groupings of nodes, such as virtual private clouds (VPCs), subnets, and Availability Zones
* **Labels** – Text descriptions for nodes and connections

## **Example 1: Create a web application architecture**

Let’s create a diagram for a simple web application hosted on AWS. Enter the following prompt:

`Create a diagram for a simple web application with an Application Load Balancer, two EC2 instances, and an RDS database. Check for AWS documentation to ensure it adheres to AWS best practices before you create the diagram`

After you enter your prompt, Amazon Q CLI will search AWS documentation for best practices using the `search_documentation` tool from `awslabsaws_documentation_mcp_server`.

![search documentaion-img](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/18/search-documentaion-1024x587.png)

Following the search of the relevant AWS documentation, it will read the documentation using the `read_documentation` tool from the MCP server `awslabsaws_documentation_mcp_server`.

![read_document-img](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/18/read_document.png)

Amazon Q CLI will then list the needed AWS service icons using the `list_icons` tool, and will use `generate_diagram` with `awslabsaws_diagram_mcp_server`.

![list and generate on cli](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/18/list-and-generate-1024x620.png)

You should receive an output with a description of the diagram created based on the prompt along with the location of where the diagram was saved.

![final-output-1stexample](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/18/final-output-1stexample-1024x677.png)

**Amazon Q CLI will generate and display the diagram.**

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/19/simple_web_app_architecture_horizontal-1-1024x415.png)

The generated diagram shows the following key components:

* An [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) as the entry point
* Two [Amazon Elastic Compute Cloud](http://aws.amazon.com/ec2) (Amazon EC2) instances for the application tier
* An [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) instance for the database tier
* Connections showing the flow of traffic

## **Example 2: Create a multi-tier architecture**

Multi-tier architectures separate applications into functional layers (presentation, application, and data) to improve scalability and security. We use the following prompt to create our diagram:

`Create a diagram for a three-tier web application with a presentation tier (ALB and CloudFront), application tier (ECS with Fargate), and data tier (Aurora PostgreSQL). Include VPC with public and private subnets across multiple AZs. Check for AWS documentation to ensure it adheres to AWS best practices before you create the diagram.`

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/19/three_tier_web_application-1024x732-1.png)

The diagram shows the following key components:

* A presentation tier in public subnets
* An application tier in private subnets
* A data tier in isolated private subnets
* Proper security group configurations
* Traffic flow between tiers

## **Example 3: Create a serverless architecture**

We use the following prompt to create a diagram for a serverless architecture:

`Create a diagram for a serverless web application using API Gateway, Lambda, DynamoDB, and S3 for static website hosting. Include Cognito for user authentication and CloudFront for content delivery. Check for AWS documentation to ensure it adheres to AWS best practices before you create the diagram.`

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/19/serverless_web_application-1-1024x850.png)

The diagram includes the following key components:

* [Amazon Simple Storage Service](http://aws.amazon.com/s3) (Amazon S3) hosting static website content
* [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distributing content globally
* [Amazon API Gateway](https://aws.amazon.com/api-gateway) handling API requests
* [AWS Lambda](http://aws.amazon.com/lambda) functions implementing business logic
* [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) storing application data
* [Amazon Cognito](https://aws.amazon.com/cognito/) managing user authentication

## **Example 4: Create a data processing diagram**

We use the following prompt to create a diagram for a data processing pipeline:

`Create a diagram for a data processing pipeline with components organized in clusters for data ingestion, processing, storage, and analytics. Include Kinesis, Lambda, S3, Glue, and QuickSight. Check for AWS documentation to ensure it adheres to AWS best practices before you create the diagram.`

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/19/data-processing-pipeline-1-1024x690.png)

The diagram organizes components into distinct clusters:

* **Data ingestion** – [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams), [Amazon Data Firehose](https://aws.amazon.com/firehose/), [Amazon Simple Queue Service](https://aws.amazon.com/sqs/)
* **Data processing** – Lambda functions, [AWS Glue](https://aws.amazon.com/glue) jobs
* **Data storage** – [S3](https://aws.amazon.com/s3) buckets, [DynamoDB](https://aws.amazon.com/dynamodb) tables
* **Data analytics** – [AWS Glue](https://aws.amazon.com/glue), [Amazon Athena,](https://aws.amazon.com/athena) [Amazon QuickSight](https://aws.amazon.com/quicksight)

## **Real-world examples**

Let’s explore some real-world architecture patterns and how to create diagrams for them using Amazon Q CLI with the AWS Diagram MCP server.

### Ecommerce platform

Ecommerce platforms require scalable, resilient architectures to handle variable traffic and maintain high availability. We use the following prompt to create an example diagram:

`Create a diagram for an e-commerce platform with microservices architecture. Include components for product catalog, shopping cart, checkout, payment processing, order management, and user authentication. Ensure the architecture follows AWS best practices for scalability and security. Check for AWS documentation to ensure it adheres to AWS best practices before you create the diagram.`

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/19/ecommerce_microservices_architecture-1-1024x942.png)

The diagram includes the following key components:

* [API Gateway](http://aws.amazon.com/api-gateway) as the entry point for client applications
* Microservices implemented as containers in [Amazon Elastic Container Service](http://aws.amazon.com/ecs) (Amazon ECS) with [AWS Fargate](http://aws.amazon.com/fargate)
* [RDS](http://aws.amazon.com/rds) databases for product catalog, shopping cart, and order data
* [Amazon ElastiCache](http://aws.amazon.com/elasticache) for product data caching and session management
* [Amazon Cognito](http://aws.amazon.com/cognito) for authentication
* [Amazon Simple Queue Service](http://aws.amazon.com/sqs) (Amazon SQS) and [Amazon Simple Notification Service](http://aws.amazon.com/sns) (Amazon SNS) for asynchronous communication between services
* [CloudFront](http://aws.amazon.com/cloudfront) for content delivery and static assets from [Amazon S3](http://aws.amazon.com/s3)
* [Amazon Route 53](http://aws.amazon.com/route53) for DNS management
* [AWS WAF](http://aws.amazon.com/waf) for web application security
* [AWS Lambda](http://aws.amazon.com/lambda) functions for serverless microservice implementation
* [AWS Secrets Manager](http://aws.amazon.com/secrets-manager) for secure credential storage
* [Amazon CloudWatch](http://aws.amazon.com/cloudwatch) for monitoring and observability

### Intelligent document processing solution

We use the following prompt to create a diagram for an intelligent document processing (IDP) architecture:

`Create a diagram for an intelligent document processing (IDP) application on AWS. Include components for document ingestion, OCR and text extraction, intelligent data extraction (using NLP and/or computer vision), human review and validation, and data output/integration. Ensure the architecture follows AWS best practices for scalability and security, leveraging services like S3, Lambda, Textract, Comprehend, SageMaker (for custom models, if applicable), and potentially Augmented AI (A2I). Check for AWS documentation related to intelligent document processing best practices to ensure it adheres to AWS best practices before you create the diagram.`

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/19/idp-1-1024x593.png)

The diagram includes the following key components:

* [Amazon API Gateway](https://aws.amazon.com/api-gateway) as the entry point for client applications, providing a secure and scalable interface
* Microservices implemented as containers in [ECS with Fargate](https://aws.amazon.com/fargate), enabling flexible and scalable processing
* [Amazon RDS](https://aws.amazon.com/rds) databases for product catalog, shopping cart, and order data, providing reliable structured data storage
* [Amazon ElastiCache](https://aws.amazon.com/elasticache) for product data caching and session management, improving performance and user experience
* [Amazon Cognito](https://aws.amazon.com/cognito) for authentication, ensuring secure access control
* [Amazon Simple Queue Service](https://aws.amazon.com/sqs) and [Amazon Simple Notification Service](https://aws.amazon.com/sqs) for asynchronous communication between services, enabling decoupled and resilient architecture
* [Amazon CloudFront](https://aws.amazon.com/cloudfront) for content delivery and static assets from S3, optimizing global performance
* [Amazon Route53](https://aws.amazon.com/route53) for DNS management, providing reliable routing
* [AWS WAF](https://aws.amazon.com/waf) for web application security, protecting against common web exploits
* [AWS Lambda](https://aws.amazon.com/lambda) functions for serverless microservice implementation, offering cost-effective scaling
* [AWS Secrets Manager](https://aws.amazon.com/secrets-manager) for secure credential storage, enhancing security posture
* [Amazon CloudWatch](https://aws.amazon.com/cloudwatch) for monitoring and observability, providing insights into system performance and health.

## **Clean up**

If you no longer need to use the AWS Cost Analysis MCP server with Amazon Q CLI, you can remove it from your configuration:

1. Open your `~/.aws/amazonq/mcp.json` file.
2. Remove or comment out the MCP server entries.
3. Save the file.

This will prevent the server from being loaded when you start Amazon Q CLI in the future.

## **Conclusion**

In this post, we explored how to use Amazon Q CLI with the AWS Documentation MCP and AWS Diagram MCP servers to create professional AWS architecture diagrams that adhere to AWS best practices referenced from official AWS documentation. This approach offers significant advantages over traditional diagramming methods:

* **Time savings** – Generate complex diagrams in minutes instead of hours
* **Consistency** – Make sure diagrams follow the same style and conventions
* **Best practices** – Automatically incorporate AWS architectural guidelines
* **Iterative refinement** – Quickly modify diagrams through simple prompts
* **Validation** – Check architectures against official AWS documentation and recommendations

As you continue your journey with AWS architecture diagrams, we encourage you to deepen your knowledge by learning more about the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) to understand how it enhances the capabilities of Amazon Q. When seeking inspiration for your own designs, the [AWS Architecture Center](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all&awsf.tech-category=*all&awsf.industries=*all&awsf.business-category=*all) offers a wealth of reference architectures that follow best practices. For creating visually consistent diagrams, be sure to visit the [AWS Icons page](https://aws.amazon.com/architecture/icons/), where you can find the complete official icon set. And to stay at the cutting edge of these tools, keep an eye on updates to the [official AWS MCP Servers](https://github.com/awslabs/mcp/tree/main)—they’re constantly evolving with new features to make your diagramming experience even better.

---

### About the Authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/19/CroppedPic-100x150.jpg)**Joel Asante**, an Austin-based Solutions Architect at Amazon Web Services (AWS), works with GovTech (Government Technology) customers. With a strong background in data science and application development, he brings deep technical expertise to creating secure and scalable cloud architectures for his customers. Joel is passionate about data analytics, machine learning, and robotics, leveraging his development experience to design innovative solutions that meet complex government requirements. He holds 13 AWS certifications and enjoys family time, fitness, and cheering for the Kansas City Chiefs and Los Angeles Lakers in his spare time.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/19/4f4204276a914373a00896cd538c74a6-CROPPED_DOWNLOADABLE-100x150.jpeg)**Dunieski Otano** is a Solutions Architect at Amazon Web Services based out of Miami, Florida. He works with World Wide Public Sector MNO (Multi-International Organizations) customers. His passion is Security, Machine Learning and Artificial Intelligence, and Serverless. He works with his customers to help them build and deploy high available, scalable, and secure solutions. Dunieski holds 14 AWS certifications and is an AWS Golden Jacket recipient. In his free time, you will find him spending time with his family and dog, watching a great movie, coding, or flying his drone.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/06/19/awsjasti-1.jpeg)**Varun Jasti** is a Solutions Architect at Amazon Web Services, working with AWS Partners to design and scale artificial intelligence solutions for public sector use cases to meet compliance standards. With a background in Computer Science, his work covers broad range of ML use cases primarily focusing on LLM training/inferencing and computer vision. In his spare time, he loves playing tennis and swimming.

TAGS: [AI/ML](https://aws.amazon.com/blogs/machine-learning/tag/ai-ml/), [Generative AI](https://aws.amazon.com/blogs/machine-learning/tag/generative-ai/)

Loading comments…

### Resources

* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=machine-learning-resources)
* [What's New](https://aws.amazon.com/new?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=machine-learning-resources)

---

### Blog Topics

* [Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/)
* [Amazon Comprehend](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-comprehend/)
* [Amazon Kendra](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-kendra/)
* [Amazon Lex](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-lex/)
* [Amazon Polly](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-polly/)
* [Amazon Q](https://aws.amazon.com/blogs/machine-learning/category/amazon-q/)
* [Amazon Rekognition](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-rekognition/)
* [Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/sagemaker/)
* [Amazon Textract](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-textract/)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=maching-learning-social)

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