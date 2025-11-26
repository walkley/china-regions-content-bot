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

## [AWS Database Blog](https://aws.amazon.com/blogs/database/)

# Supercharging AWS database development with AWS MCP servers

by Aditya Samant, Rohan Bhatia, Michael Shao, and Utkarsh Shah on 27 JUN 2025 in [Amazon Aurora](https://aws.amazon.com/blogs/database/category/database/amazon-aurora/ "View all posts in Amazon Aurora"), [Amazon DynamoDB](https://aws.amazon.com/blogs/database/category/database/amazon-dynamodb/ "View all posts in Amazon DynamoDB"), [Amazon ElastiCache](https://aws.amazon.com/blogs/database/category/database/amazon-elasticache/ "View all posts in Amazon ElastiCache"), [Announcements](https://aws.amazon.com/blogs/database/category/post-types/announcements/ "View all posts in Announcements"), [Intermediate (200)](https://aws.amazon.com/blogs/database/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [Technical How-to](https://aws.amazon.com/blogs/database/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/database/supercharging-aws-database-development-with-aws-mcp-servers/)  [Comments](https://aws.amazon.com/blogs/database/supercharging-aws-database-development-with-aws-mcp-servers/#Comments)  Share

[Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) is transforming how AI systems interact with data and tools, enabling them to easily work with databases, APIs, file systems, and specialized business applications. You’re probably wondering why everyone is talking about MCP servers and how do they relate to your databases. In fact, even our customers are asking us how they can integrate their existing systems with AI models to supplement everyday tasks with AI-assisted tools that understand context and suggest improvements.

At [Amazon Web Services](https://aws.amazon.com/) (AWS), we constantly seek ways to help developers build more quickly, intuitively, and productively in the cloud. [Amazon Aurora](https://aws.amazon.com/aurora/), [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), and [Amazon ElastiCache](https://aws.amazon.com/elasticache/) are popular choices for developers powering critical workloads, including global commerce platforms, financial systems, and real-time analytics applications. With the advent of AI, how developers interact with these services is evolving. To enhance productivity, developers are supplementing everyday tasks with AI-assisted tools that understand context, suggest improvements, and help reason through system configurations. MCP is at the helm of this revolution, rapidly transforming how developers integrate AI assistants into their development pipelines. In this post, we explore the core concepts behind MCP and demonstrate how new AWS MCP servers can accelerate your database development through natural language prompts.

## Traditional development challenges

In a typical development environment, developers can spend hours writing boilerplate queries and switching between development tools and database interfaces (such as psql or mysql client) to inspect schemas and data. Such frequent context switching forces developers to repeatedly reacquaint themselves with different schemas, syntaxes, paradigms, and best practices, slowing development and increasing the risk of errors.

These challenges magnify when applications rely on a combination of relational, nonrelational, and cache database technologies. Within the relational world alone, developers must navigate subtle but breaking differences between SQL dialects. For example, a valid PostgreSQL query can fail in MySQL and the opposite can also happen. Developers must maintain multiple mental models simultaneously, constantly translating between dialects. The cognitive burden amplifies further when switching between relational and nonrelational databases. Each transition demands not just different syntax, but fundamentally different approaches to data modeling, query optimization, and application architecture. Traditional development tools weren’t designed for this reality of constant context-switching across diverse database ecosystems.

## Introducing MCP servers for AWS databases

The approach AWS is taking focuses on secure, protocol-based access to structured metadata, designed to work in your local development environments and collaborative settings. To support this, we’ve made available open source MCP servers for several database services. This post focuses on the following database services:

* **Amazon Aurora** – [MCP server for Aurora PostgreSQL](https://awslabs.github.io/mcp/servers/postgres-mcp-server/), [MCP server for Aurora MySQL](https://awslabs.github.io/mcp/servers/mysql-mcp-server/), and [MCP server for Aurora DSQL](https://awslabs.github.io/mcp/servers/aurora-dsql-mcp-server/)
* **DynamoDB** – [MCP server for DynamoDB](https://awslabs.github.io/mcp/servers/dynamodb-mcp-server/)
* **ElastiCache** – [Valkey](https://awslabs.github.io/mcp/servers/valkey-mcp-server/) and [Memcached](https://awslabs.github.io/mcp/servers/memcached-mcp-server/)

Additionally, we’ve created the following open source MCP servers:

* [**Amazon Neptune**](https://aws.amazon.com/neptune/) – [Neptune MCP server](https://awslabs.github.io/mcp/servers/amazon-neptune-mcp-server/)
* [**Amazon DocumentDB**](https://aws.amazon.com/documentdb/) – [DocumentDB MCP server](https://awslabs.github.io/mcp/servers/documentdb-mcp-server/)
* [**Amazon Timestream**](https://aws.amazon.com/timestream/) – [Timestream for InfluxDB MCP server](https://github.com/awslabs/mcp/tree/main/src/timestream-for-influxdb-mcp-server)
* [**Amazon Keyspaces (for Apache Cassandra)**](https://aws.amazon.com/keyspaces/) – [Keyspaces MCP server](https://github.com/awslabs/mcp/tree/main/src/amazon-keyspaces-mcp-server)
* [**Amazon MemoryDB**](https://aws.amazon.com/memorydb/) – [MemoryDB Valkey MCP server](https://awslabs.github.io/mcp/servers/valkey-mcp-server/)

## What is MCP?

MCP is an open protocol that standardizes connecting AI assistants to the external world, including content repositories, data sources, business tools, and development environments. At its core, MCP follows a client-server architecture where a host application can connect to multiple servers. An MCP architecture has the following components:

* **MCP hosts and clients** – AI-powered applications such as [Amazon Q command line interface (CLI)](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line.html), [Cursor](https://www.cursor.com/), or [Claude Desktop](https://claude.ai/download) that need access to external data or tools.
* **MCP servers** – Lightweight servers that expose specific functionalities through tools, connecting to local or remote data sources.
* **Data sources** – Databases, files, or services that contain the information your AI assistants need.

The following diagram explains how MCP enables [large language model](https://aws.amazon.com/what-is/large-language-model/) (LLM) agents to access and perform tasks on the structured data stored in databases.

![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/06/26/image-1-29.png)

Each AWS database MCP server implements the same protocol while handling database specific connections through appropriate mechanisms. This eliminates the need for developers to build custom integrations for each database when connecting AI tools. By standardizing how AI assistant tools access metadata across database services, MCP enables intelligent suggestions, context-aware query assistance, and real-time understanding of database structure.

Next, we explore some common MCP use cases.

## Accelerating database development with MCP servers

Development often begins with fundamental questions: What am I building, and what tools should I use? Database MCP servers address these questions by bringing database context directly into development environments. These servers expose a curated set of tools that agents can discover and use to accomplish specific tasks. For example, the Aurora DSQL MCP server provides three essential tools: `get_schema`, `readonly_query`, and `transact`. During development, the AI agent invokes the LLM to select the appropriate tool. A typical workflow might begin with get\_schema to discover available tables, continue with readonly\_query to examine table structures, and conclude with transact to insert rows into the relevant tables.

Enabling the AI assistant with such contextual awareness helps developers answer important questions that traditionally slow down development:

* How are tables related?
* Which keys drive specific access patterns?
* What data is available for implementing a particular feature or building analytic dashboards?

By exposing structured metadata from AWS databases, database MCP servers support workflows that enhance development speed, safety, and visibility. They empower AI agents to reason about schemas, access patterns, and recent changes in real time. Next, we explore the common patterns that emerge when using MCP in database development workflows.

### Schema-driven feature development

After determining the appropriate application design and data model, developers can use integrated development environment (IDE) integrations with MCP servers to access real-time schema details and relationships. They can then continue confidently evolving the data model through natural language interactions with the AI Assistant. For example, developers can add a table to Aurora and clearly understand how it connects to existing foreign keys. They can update a DynamoDB attribute structure based on new requirements while comprehending its impact on query patterns. Additionally, they can explore how cached data is stored and used in ElastiCache.

The following video demonstration showcases how developers can use Amazon Q CLI with Cursor to find tables, understand the database schema, and generate create, read, update, and delete (CRUD) APIs in an [Amazon Aurora PostgreSQL-Compatible Edition](https://aws.amazon.com/rds/aurora/features/) database in minutes using natural language prompts. This video is focused on Aurora, but the same concepts apply to other databases, including Amazon Aurora MySQL-Compatible Edition.

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/DBBLOG-4938/APG+MCP+CRUD1.mp4?_=1)

### Exploring data to power business insight

Modern applications do more than store data. They reason about it. Using MCP server capabilities, you can build robust dashboards in minutes. MCP automatically handles data contextualization, relationship mapping, and visualization recommendations. The following demo uses Aurora DSQL MCP server to build a dashboard for an ecommerce database on Aurora DSQL.

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/DBBLOG-4938/Claude+Desktop.mp4?_=2)

### Automated test code generation aligned with your database schemas

Test coverage is only as useful as its accuracy. Using agents with MCP servers, developers can generate tests based on live metadata and query patterns, streamlining various testing activities. For example, using the AI assistant, developers can inspect the current Aurora schema and create specific tests to validate constraints and relationships. For DynamoDB, they can generate tests based on a table’s access patterns and indexes. Similarly, with ElastiCache, they can build tests to simulate specific Time To Live (TTL) configurations and fallback scenarios.With the context of each database available to the AI assistant, these tests are precise and purpose-built to validate your database’s live metadata and query patterns. By following this approach, developers can spend less time writing and maintaining tests, speeding up delivery without compromising confidence in application behavior.The following video demonstration walks through how MCP servers support AI-assisted test generation, ensuring that test logic stays aligned with the current structure of the system.

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/DBBLOG-4938/DDB-MCP-RecurringPayments-TestGeneration.mp4?_=3)

## Monitor and troubleshoot issues

For operations engineers working with complex database systems in production, MCP offers a powerful tool for systemic troubleshooting. When faced with database performance issues or anomalies, an operations engineer can use an AI-assisted workflow directly from their preferred tools to obtain real-time insights. This aids in troubleshooting issues such as high memory usage, slow queries, and other potential problems before they become critical.

A companion demo illustrates how operations teams can use an AI-assisted workflow to interact with an Amazon ElastiCache Valkey cache. This workflow retrieves information such as used memory, peak memory, number of clients connected, status of replications, and more. Although this information can be lengthy and difficult for humans to parse quickly, an AI agent can efficiently summarize the data and highlight the most relevant results that may be causing performance issues.

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/DBBLOG-4938/ValkeyMcpOperationsDemo.mp4?_=4)

## Getting started

The MCP servers for Aurora, DynamoDB, and ElastiCache are available as an open source project maintained by AWS Labs. You’ll run these servers in a Docker container locally on the client running the AI assistant. You’ll need to follow the steps in the prerequisites section before you can start using MCP servers.

### Prerequisites

Before using MCP servers, follow these prerequisite steps:

1. Ensure Docker is installed on your development environment. For instructions to install Docker, visit [Docker Desktop download](https://www.docker.com/products/docker-desktop/)
2. Invoke the following commands in your shell based on the database service(s) you use:

   ```
   # Clone the repository
   git clone https://github.com/awslabs/mcp.git
   # Navigate to folder of the database service (example shown for Aurora PostgreSQL)
   cd mcp/src/postgres-mcp-server/
   # Build the Docker image
   docker build -t awslabs/postgres-mcp-server:latest .
   ```

   | **Database service** | **Directory** |
   | --- | --- |
   | Aurora DSQL | `aurora-dsql-mcp-server` |
   | Aurora MySQL | `mysql-mcp-server` |
   | Aurora PostgreSQL | `postgres-mcp-server` |
   | DynamoDB | `dynamodb-mcp-server` |
   | ElastiCache (Valkey) | `valkey-mcp-server` |
   | ElastiCache (memcached) | `memcached-mcp-server` |
   | Amazon Neptune | `amazon-neptune-mcp-server` |
   | Amazon Timestream | `timestream-for-influxdb-mcp-server` |
   | Amazon DocumentDB | `aws-documentdb-mcp-server` |
   | Amazon Keyspaces | `amazon-keyspaces-mcp-server` |
3. Add the MCP server to your client application’s configuration file. The configuration depends upon the database service and specific client applications, as demonstrated in the following sections.

After you fulfill the prerequisites, you’re ready to use your preferred IDE and [generative AI](https://aws.amazon.com/generative-ai/) tools. We explore a few common IDE and tools in the next sections.

### Amazon Q CLI with Cursor

To use Amazon Q CLI with Cursor, follow these steps:

1. Ensure Cursor is installed on your machine. For instructions, visit [Installation](https://docs.cursor.com/get-started/installation).
2. Ensure Amazon Q CLI and the [Amazon Q Developer](https://aws.amazon.com/q/developer/) extension are installed for Cursor. For more information on how to install these tools, refer to [Installing the Amazon Q Developer extension or plugin in your IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html) and [Installing Amazon Q for command line](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html).
3. We use the following example workspace configuration to demonstrate MCP servers in containers for Amazon Q CLI based on the database service. You can also use the global configuration as specified in the [MCP configuration](https://docs.aws.amazon.com/en_us/amazonq/latest/qdeveloper-ug/command-line-mcp-configuration.html) section in our documentation.
4. Here are sample configurations for `mcp.json` file that you can use depending on the MCP server you choose.

   For Aurora MySQL and Aurora PostgreSQL:

   ```
   {
     "mcpServers": {
       "awslabs.postgres-mcp-server": {
         "command": "docker",
         "args": [
           "run",
           "-i",
           "--rm",
           "-e", "AWS_ACCESS_KEY_ID=YOUR_KEY_HERE",
           "-e", "AWS_SECRET_ACCESS_KEY=YOUR_SECRET_HERE",
           "-e", "AWS_REGION=YOUR_REGION_HERE",
           "awslabs/postgres-mcp-server:latest",
           "--resource_arn", "YOUR_CLUSTER_ARN",
           "--secret_arn", "YOUR_DB_SECRET_ARN",
           "--database", "YOUR_DB_NAME",
           "--region", "YOUR_REGION_NAME",
           "--readonly",
           "True"
         ]
       }
     },
     "awslabs.mysql-mcp-server": {
       "command": "docker",
       "args": [
         "run",
         "-i",
         "--rm",
         "-e", "AWS_ACCESS_KEY_ID=YOUR_KEY_HERE",
         "-e", "AWS_SECRET_ACCESS_KEY=YOUR_SECRET_HERE",
         "-e", "AWS_REGION=YOUR_REGION_HERE",
         "awslabs/mysql-mcp-server:latest",
         "--resource_arn", "YOUR_CLUSTER_ARN",
         "--secret_arn", "YOUR_DB_SECRET_ARN",
         "--database", "YOUR_DB_NAME",
         "--region", "YOUR_REGION_NAME",
         "--readonly",
         "True"
       ]
     }
   }
   ```

   For Aurora DSQL:

   ```
   {
     "mcpServers": {
       "awslabs.aurora-dsql-mcp-server": {
         "command": "docker",
         "args": [
           "run",
           "-i",
           "--rm",
           "-e", "AWS_ACCESS_KEY_ID=YOUR_KEY_HERE",
           "-e", "AWS_SECRET_ACCESS_KEY=YOUR_SECRET_HERE",
           "-e", "AWS_REGION=YOUR_REGION_HERE",
           "awslabs/aurora-dsql-mcp-server:latest",
           "--cluster_endpoint", "DSQL cluster endpoint",
           "--database_user", "admin",
           "--region", "us-east-1"
         ]
       }
     }
   }
   ```

   For DynamoDB:

   ```
   {
       "mcpServers": {
         "awslabs.dynamodb-mcp-server": {
           "command": "docker",
           "args": [
             "run",
             "--rm",
             "--interactive",
             "--env",
             "FASTMCP_LOG_LEVEL=ERROR",
             "awslabs/dynamodb-mcp-server:latest"
           ],
           "env": {},
           "disabled": false,
           "autoApprove": []
         }
       }
     }
   ```

   For ElastiCache:

   ```
   {
     "mcpServers": {
       "awslabs.valkey-mcp-server": {
         "command": "docker",
         "args": [
           "run",
           "--rm",
           "--interactive",
           "--env",
           "FASTMCP_LOG_LEVEL=ERROR",
           "--env",
           "VALKEY_HOST=hostname",
           "--env",
           "VALKEY_PORT=6379",
           "awslabs/valkey-mcp-server:latest"
         ],
         "env": {},
         "disabled": false,
         "autoApprove": []
       }
     }
   }
   ```

### Amazon Q CLI with Visual Studio Code (VS Code)

To use MCP servers with Amazon Q CLI with VS Code, follow these steps:

1. Ensure VS Code is installed on your machine. Refer to [Setting up Visual Studio Code](https://code.visualstudio.com/docs/setup/setup-overview) to learn more.
2. Ensure Amazon Q CLI and Amazon Q Developer extension are installed for VS Code. To learn more, refer to [Installing the Amazon Q Developer extension or plugin in your IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html) and [Installing Amazon Q for the command line](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html).
3. Use the example workspace configuration for Amazon Q CLI based on the database service as explained in the **Amazon Q CLI with Cursor** section, or you can use the global configuration as specified in the [MCP configuration](https://docs.aws.amazon.com/en_us/amazonq/latest/qdeveloper-ug/command-line-mcp-configuration.html) section in our documentation.
4. The rest of the configuration is identical to Amazon Q CLI with Cursor as discussed previously.

### Claude Desktop

To use MCP servers with Claude Desktop, follow these steps:

1. Ensure Claude Desktop is installed and running on your machine. Refer to [Installing Claude for Desktop](https://support.anthropic.com/en/articles/10065433-installing-claude-for-desktop) to learn more.
2. Open Claude Desktop and choose **Settings** then choose **Edit Config**.

   ![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/06/26/image-2-24.png)
3. Select **claude\_desktop\_config.json**. The content of `claude_desktop_config.json` is identical to `mcp.json` file as described in the **Amazon Q CLI with Cursor** section.

### Where we’re headed

The availability of MCP servers reflects a broader shift in how we support builders. The goal is to bring AWS databases into the tools where development starts. That includes local environments, collaborative editors, and AI-assisted workflows.

MCP servers are open source and ready to use. You can find the code, documentation, and setup instructions in the [AWS Labs GitHub](https://github.com/awslabs/mcp) repository. Start integrating them into your workflows and bring the full context of AWS databases into your development environment.

## Conclusion

In this post, we explored how to configure and use the newly released MCP servers for AWS database services, namely Aurora PostgreSQL and Aurora MySQL, Aurora DSQ, DynamoDB, DocumentDB, Keyspaces, Elasticache (Valkey, Memcached), and Neptune. We also looked at a few common patterns where MCP servers can be used to accelerate your development cycle.

Start using MCP servers today to integrate your AI applications and agents with your data sources and services. All these MCP servers are open source, and we welcome both your contributions and feedback about this newly unlocked functionality. We look forward to incorporating your feedback and further enhancing the capabilities of these MCP servers to introduce new ways for both humans and AI models to interact with your business data.

---

### About the authors

![Aditya Samant](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/06/26/DBBLOG-4938a1.jpeg)

### Aditya Samant

[Aditya](https://www.linkedin.com/in/aditya-samant-2283258/) has over two decades of experience working with commercial and open source databases. He currently works at AWS as a Principal Database Specialist Solutions Architect. In his role, he works with customers designing scalable, secure, and robust cloud-native architectures. Aditya works closely with the service teams and collaborates on designing and delivery of new features for Amazon managed databases.

![Michael Shao](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/06/26/DBBLOG-4938a2.jpeg)

### Michael Shao

[Michael](author%20LinkedIn) is a Senior Developer Advocate on the Amazon DynamoDB team. Michael has spent over 8 years as a software engineer at Amazon Retail, with a background in designing and building scalable, resilient, and highly performing software systems. His expertise in exploratory, iterative development helps drive his passion for helping AWS customers understand complex technical topics.

![Rohan Bhatia](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/06/26/DBBLOG-4938a3.png)

### Rohan Bhatia

[Rohan](https://www.linkedin.com/in/rohanbhatia1/) is a Principal Product Manager for the Amazon Aurora service working on the next generation of developer experiences.

![Utkarsh Shah](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/06/26/DBBLOG-4938a4.png)

### Utkarsh Shah

[Utkarsh](https://www.linkedin.com/in/utkarshshah/) is a Software Engineer at AWS who has made significant contributions to AWS non-relational Database products. Including Amazon ElastiCache. Over the past 9 years, he has led the design and delivery of complex projects that have had a lasting impact on the ElastiCache product, technology, and architecture. Utkarsh is also actively involved in the broader engineering community, sharing his expertise through trainings and publications.

TAGS: [Valkey](https://aws.amazon.com/blogs/database/tag/valkey/)

Loading comments…

### Resources

* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=database-resources)
* [What's New](https://aws.amazon.com/new?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=database-resources)

---

### Blog Topics

* [Amazon Aurora](https://aws.amazon.com/blogs/database/category/database/amazon-aurora/)
* [Amazon DocumentDB](https://aws.amazon.com/blogs/database/category/database/amazon-document-db/)
* [Amazon DynamoDB](https://aws.amazon.com/blogs/database/category/database/amazon-dynamodb/)
* [Amazon ElastiCache](https://aws.amazon.com/blogs/database/category/database/amazon-elasticache/)
* [Amazon Keyspaces (for Apache Cassandra)](https://aws.amazon.com/blogs/database/category/database/amazon-managed-apache-cassandra-service/)
* [Amazon Managed Blockchain](https://aws.amazon.com/blogs/database/category/blockchain/amazon-managed-blockchain/)
* [Amazon MemoryDB for Redis](https://aws.amazon.com/blogs/database/category/database/amazon-memorydb-for-redis/)
* [Amazon Neptune](https://aws.amazon.com/blogs/database/category/database/amazon-neptune/)
* [Amazon Quantum Ledger Database (Amazon QLDB)](https://aws.amazon.com/blogs/database/category/database/amazon-quantum-ledger-database/)
* [Amazon RDS](https://aws.amazon.com/blogs/database/category/database/amazon-rds/)
* [Amazon Timestream](https://aws.amazon.com/blogs/database/category/database/amazon-timestream/)
* [AWS Database Migration Service](https://aws.amazon.com/blogs/database/category/database/aws-database-migration-service/)
* [AWS Schema Conversion Tool](https://aws.amazon.com/blogs/database/category/database/aws-schema-conversion-tool/)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=database-social)

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