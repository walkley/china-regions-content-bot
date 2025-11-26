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

## [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/)

# Introducing MCP Server for Apache Spark History Server for AI-powered debugging and optimization

by Manabu McCloskey, Andrew Kim, Mohit Saxena, Kartik Panjabi, Shubham Mehta, and Vara Bonthu on 23 JUL 2025 in [Amazon SageMaker Data & AI Governance](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-sagemaker-data-ai-governance/ "View all posts in Amazon SageMaker Data & AI Governance"), [Analytics](https://aws.amazon.com/blogs/big-data/category/analytics/ "View all posts in Analytics"), [Announcements](https://aws.amazon.com/blogs/big-data/category/post-types/announcements/ "View all posts in Announcements") [Permalink](https://aws.amazon.com/blogs/big-data/introducing-mcp-server-for-apache-spark-history-server-for-ai-powered-debugging-and-optimization/)  [Comments](https://aws.amazon.com/blogs/big-data/introducing-mcp-server-for-apache-spark-history-server-for-ai-powered-debugging-and-optimization/#Comments)  Share

Organizations running [Apache Spark](https://spark.apache.org/) workloads, whether on [Amazon EMR](https://aws.amazon.com/emr/), [AWS Glue](https://aws.amazon.com/glue/), [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS), or self-managed clusters, invest countless engineering hours in performance troubleshooting and optimization. When a critical extract, transform, and load (ETL) pipeline fails or runs slower than expected, engineers end up spending hours navigating through multiple interfaces such as logs or Spark UI, correlating metrics across different systems and manually analyzing execution patterns to identify root causes. Although [Spark History Server](https://spark.apache.org/docs/latest/monitoring.html) provides detailed telemetry data, including job execution timelines, stage-level metrics, and resource consumption patterns, accessing and interpreting this wealth of information requires deep expertise in Spark internals and navigating through multiple interconnected web interface tabs.

Today, we’re announcing the open source release of [Spark History Server MCP](https://github.com/DeepDiagnostix-AI/mcp-apache-spark-history-server), a specialized [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) server that transforms this workflow by enabling AI assistants to access and analyze your existing Spark History Server data through natural language interactions. This project, developed collaboratively by AWS open source and [Amazon SageMaker Data Processing](https://aws.amazon.com/sagemaker/data-processing/), turns complex debugging sessions into conversational interactions that deliver faster, more accurate insights without requiring changes to your current Spark infrastructure. You can use this MCP server with your self-managed or AWS managed Spark History Servers to analyze Spark applications running in the cloud or on-premises deployments.

### Understanding Spark observability challenge

[Apache Spark](https://spark.apache.org/docs/latest/index.html) has become the standard for large-scale data processing, powering critical ETL pipelines, real-time analytics, and [machine learning](https://aws.amazon.com/ai/machine-learning/) (ML) workloads across thousands of organizations. Building and maintaining Spark applications is, however, still an iterative process, where developers spend significant time testing, optimizing, and troubleshooting their code. Spark application developers focused on data engineering and data integration use cases often encounter significant operational challenges due to a few different reasons:

* **Complex connectivity and configuration options** **to a variety of resources with Spark** – Although this makes it a popular data processing platform, it often makes it challenging to find the root cause of inefficiencies or failures when Spark configurations aren’t optimally or correctly configured.
* **Spark’s in-memory processing model and distributed partitioning of datasets** **across its workers** – Although good for parallelism, this often makes it difficult for users to identify inefficiencies. This results in slow application execution or root cause of failures caused by resource exhaustion issues such as out of memory and disk exceptions.
* **Lazy evaluation of Spark transformations** – Although lazy evaluation optimizes performance, it makes it challenging to accurately and quickly identify the application code and logic that caused the failure from the distributed logs and metrics emitted from different executors.

### Spark History Server

Spark History Server provides a centralized web interface for monitoring completed Spark applications, serving comprehensive telemetry data including job execution timelines, stage-level metrics, task distribution, executor resource consumption, and SQL query execution plans. Although Spark History Server assists developers for performance debugging, code optimization, and capacity planning, it still has challenges:

* **Time-intensive manual workflows** – Engineers spend hours navigating through the Spark History Server UI, switching between multiple tabs to correlate metrics across jobs, stages, and executors. Engineers must constantly switch between the Spark UI, cluster monitoring tools, code repositories, and documentation to piece together a complete picture of application performance, which often takes days.
* **Expertise bottlenecks** – Effective Spark debugging requires deep understanding of execution plans, memory management, and shuffle operations. This specialized knowledge creates dependencies on senior engineers and limits team productivity.
* **Reactive problem-solving** – Teams typically discover performance issues only after they impact production systems. Manual monitoring approaches don’t scale to proactively identify degradation patterns across hundreds of daily Spark jobs.

### How MCP transforms Spark observability

The Model Context Protocol provides a standardized interface for AI agents to access domain-specific data sources. Unlike general-purpose AI assistants operating with limited context, MCP-enabled agents can access technical information about specific systems and provide insights based on actual operational data rather than generic recommendations.With the help of Spark History Server accessible through MCP, instead of manually gathering performance metrics from multiple sources and correlating them to understand application behavior, engineers can engage with AI agents that have direct access to all Spark execution data. These agents can analyze execution patterns, identify performance bottlenecks, and provide optimization recommendations based on actual job characteristics rather than general best practices.

## Introduction to Spark History Server MCP

The [Spark History Server MCP](https://github.com/DeepDiagnostix-AI/mcp-apache-spark-history-server) is a specialized bridge between AI agents and your existing Spark History Server infrastructure. It connects to one or more Spark History Server instances and exposes their data through standardized tools that AI agents can use to retrieve application metrics, job execution details, and performance data.

Importantly, the MCP server functions purely as a data access layer, enabling AI agents such as [Amazon Q Developer CLI](https://github.com/aws/amazon-q-developer-cli), [Claude desktop](https://claude.ai/download), [Strands Agents](https://strandsagents.com/latest/), [LlamaIndex](https://docs.llamaindex.ai/en/stable/), and [LangGraph](https://www.langchain.com/langgraph) to access and reason about your Spark data. The following diagram shows this flow.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/07/23/BDB-5378-1.png)

The Spark History Server MCP directly addresses these operational challenges by enabling AI agents to access Spark performance data programmatically. This transforms the debugging experience from manual UI navigation to conversational analysis. Instead of hours in the UI, ask, “Why did job spark-abcd fail?” and receive root cause analysis of the failure. This allows users to use AI agents for expert-level performance analysis and optimization recommendations, without requiring deep Spark expertise.

The MCP server provides comprehensive access to Spark telemetry across multiple granularity levels. Application-level tools retrieve execution summaries, resource utilization patterns, and success rates across job runs. Job and stage analysis tools provide execution timelines, stage dependencies, and task distribution patterns for identifying critical path bottlenecks. Task-level tools expose executor resource consumption patterns and individual operation timings for detailed optimization analysis. SQL-specific tools provide query execution plans, join strategies, and shuffle operation details for analytical workload optimization. You can review the complete set of tools available in the MCP server in the [project README](https://github.com/DeepDiagnostix-AI/mcp-apache-spark-history-server?tab=readme-ov-file#%EF%B8%8F-available-tools).

## How to use the MCP server

The MCP is an open standard that enables secure connections between AI applications and data sources. This MCP server implementation supports both `Streamable HTTP` and `STDIO` protocols for maximum flexibility.

The MCP server runs as a local service within your infrastructure either on [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) or Amazon EKS, connecting directly to your Spark History Server instances. You maintain complete control over data access, authentication, security, and scalability.

All the tools are available with streamable HTTP and STDIO protocol:

* **Streamable HTTP** – Full advanced tools for LlamaIndex, LangGraph, and programmatic integrations
* **STDIO mode** – Core functionality of [Amazon Q CLI](https://github.com/DeepDiagnostix-AI/mcp-apache-spark-history-server/tree/main/examples/integrations/amazon-q-cli) and [Claude Desktop](https://github.com/DeepDiagnostix-AI/mcp-apache-spark-history-server/tree/main/examples/integrations/claude-desktop)

For deployment, it supports multiple Spark History Server instances and provides deployments with AWS Glue, Amazon EMR, and Kubernetes.

### Quick local setup

To set up Spark History MCP server locally, execute the following commands in your terminal:

```
git clone
cd spark-history-server-mcp

# Install Task (if not already installed)
brew install go-task # macOS, see  for others

# Setup and start testing
task install            # Install dependencies
task start-spark-bg     # Start Spark History Server with sample data
task start-mcp-bg       # Start MCP Server
task start-inspector-bg # Start MCP Inspector

# Opens  for interactive testing
# When done, run task stop-all
```

For comprehensive configuration examples and integration guides, refer to the [project README](https://github.com/DeepDiagnostix-AI/mcp-apache-spark-history-server).

## Integration with AWS managed services

The Spark History Server MCP integrates seamlessly with AWS managed services, offering enhanced debugging capabilities for Amazon EMR and AWS Glue workloads. This integration adapts to various Spark History Server deployments available across these AWS managed services while providing a consistent, conversational debugging experience:

* **AWS Glue** – Users can use the Spark History Server MCP integration with [self-managed Spark History Server](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-history.html) on an EC2 instance or launch locally using Docker container. Setting up the integration is straightforward. Follow the step-by-step instructions in the [README](https://github.com/DeepDiagnostix-AI/mcp-apache-spark-history-server/tree/main/examples/aws/glue) to configure the MCP server with your preferred Spark History Server deployment. Using this integration, AWS Glue users can analyze AWS Glue ETL job performance regardless of their Spark History Server deployment approach.
* **Amazon EMR** – Integration with Amazon EMR uses the service-managed [Persistent UI](https://docs.aws.amazon.com/emr/latest/ManagementGuide/app-history-spark-UI.html) feature for EMR on Amazon EC2. The MCP server requires only an EMR cluster [Amazon Resource Name](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) (ARN) to discover the available Persistent UI on the EMR cluster or automatically configure a new one for cases its missing with token-based authentication. This eliminates the need for manually configuring Spark History Server setup while providing secure access to detailed execution data from EMR Spark applications. Using this integration, data engineers can ask questions about their Spark workloads, such as “Can you get job bottle neck for spark-<emr-applicationId>? ” The MCP responds with detailed analysis of execution patterns, resource utilization differences, and targeted optimization recommendations, so teams can fine-tune their Spark applications for optimal performance across AWS services.

For comprehensive configuration examples and integration details, refer to the [AWS Integration Guides](https://github.com/DeepDiagnostix-AI/mcp-apache-spark-history-server/tree/main?tab=readme-ov-file#-aws-integration-guides).

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/BDB-5378/shs_mcp_glue_and_emr_ec2_demo2.mP4?_=1)

## Looking ahead: The future of AI-assisted Spark optimization

This open-source release establishes the foundation for enhanced AI-powered Spark capabilities. This project establishes the foundation for deeper integration with AWS Glue and Amazon EMR to simplify the debugging and optimization experience for customers using these Spark environments. The Spark History Server MCP is open source under the Apache 2.0 license. We welcome contributions including new tool extensions, integrations, documentation improvements, and deployment experiences.

## Get started today

Transform your Spark monitoring and optimization workflow today by providing AI agents with intelligent access to your performance data.

* Explore the [GitHub repository](https://github.com/DeepDiagnostix-AI/mcp-apache-spark-history-server)
* Review the comprehensive [README](https://github.com/DeepDiagnostix-AI/mcp-apache-spark-history-server/blob/main/README.md) for setup and integration instructions
* Join discussions and submit issues for enhancements
* Contribute new features and deployment patterns

*Acknowledgment: A special thanks to everyone who contributed to the development and open-sourcing of the Apache Spark history server MCP: Vaibhav Naik, Akira Ajisaka, Rich Bowen, Savio Dsouza.*

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/07/23/BDB-5378-2-100x150.jpeg)Manabu McCloskey** is a Solutions Architect at Amazon Web Services. He focuses on contributing to open source application delivery tooling and works with AWS strategic customers to design and implement enterprise solutions using AWS resources and open source technologies. His interests include Kubernetes, GitOps, Serverless, and Souls Series.

**![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/07/23/BDB-5378-3-100x109.jpeg)Vara Bonthu** is a Principal Open Source Specialist SA leading Data on EKS and AI on EKS at AWS, driving open source initiatives and helping AWS customers to diverse organizations. He specializes in open source technologies, data analytics, AI/ML, and Kubernetes, with extensive experience in development, DevOps, and architecture. Vara focuses on building highly scalable data and AI/ML solutions on Kubernetes, enabling customers to maximize cutting-edge technology for their data-driven initiatives

**![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/07/23/BDB-5378-4-100x133.jpeg)Andrew Kim** is a Software Development Engineer at AWS Glue, with a deep passion for distributed systems architecture and AI-driven solutions, specializing in intelligent data integration workflows and cutting-edge feature development on Apache Spark. Andrew focuses on re-inventing and simplifying solutions to complex technical problems, and he enjoys creating web apps and producing music in his free time.

**![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/07/23/BDB-5378-5.jpeg)Shubham Mehta** is a Senior Product Manager at AWS Analytics. He leads generative AI feature development across services such as AWS Glue, Amazon EMR, and Amazon MWAA, using AI/ML to simplify and enhance the experience of data practitioners building data applications on AWS.

**![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/07/23/BDB-5378-6.jpeg)Kartik Panjabi** is a Software Development Manager on the AWS Glue team. His team builds generative AI features for the Data Integration and distributed system for data integration.

**![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/07/23/BDB-5378-7.png)Mohit Saxena** is a Senior Software Development Manager on the AWS Data Processing Team (AWS Glue and Amazon EMR). His team focuses on building distributed systems to enable customers with new AI/ML-driven capabilities to efficiently transform petabytes of data across data lakes on Amazon S3, databases and data warehouses on the cloud.

Loading comments…

### Resources

* [Amazon Athena](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-athena?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon EMR](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-emr?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon Kinesis](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-kinesis?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon MSK](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-managed-streaming-for-apache-kafka/)
* [Amazon QuickSight](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-quicksight?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon Redshift](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-redshift-analytics?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [AWS Glue](https://aws.amazon.com/blogs/big-data/category/analytics/aws-glue?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-social)

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