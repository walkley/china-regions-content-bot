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

# Extend the Amazon Q Developer CLI with Model Context Protocol (MCP) for Richer Context

by Brian Beach on 29 APR 2025 in [Amazon Aurora](https://aws.amazon.com/blogs/devops/category/database/amazon-aurora/ "View all posts in Amazon Aurora"), [Amazon Q Developer](https://aws.amazon.com/blogs/devops/category/amazon-q/amazon-q-developer/ "View all posts in Amazon Q Developer"), [Announcements](https://aws.amazon.com/blogs/devops/category/post-types/announcements/ "View all posts in Announcements"), [PostgreSQL compatible](https://aws.amazon.com/blogs/devops/category/database/amazon-aurora/postgresql-compatible/ "View all posts in PostgreSQL compatible"), [RDS for PostgreSQL](https://aws.amazon.com/blogs/devops/category/database/amazon-rds/rds-for-postgresql/ "View all posts in RDS for PostgreSQL") [Permalink](https://aws.amazon.com/blogs/devops/extend-the-amazon-q-developer-cli-with-mcp/) Share

Earlier today, [Amazon Q Developer](https://aws.amazon.com/q/developer/) announced [Model Context Protocol (MCP) support](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-q-developer-cli-model-context-protocol/) in the command line interface (CLI). Developers can connect external data sources to Amazon Q Developer CLI with MCP support for more context-aware responses. By integrating MCP tools and prompts into Q Developer CLI, you get access to an expansive list of pre-built integrations or any MCP Servers that support `stdio`. This extra context helps Q Developer write more accurate code, understand your data structures, generate appropriate unit tests, create database documentation, and execute precise queries, all without needing to develop custom integration code. By extending Q Developer with MCP tools and prompts, developers can execute development tasks faster, streamlining the developer experience. At AWS, we’re committed to supporting popular open source protocols for agents like Model Context Protocol (MCP) proposed by Anthropic. We’ll continue to support this effort by extending this functionality within the Amazon Q Developer IDE plugins in the coming weeks.

## Introduction

I’m always on the lookout for tools and technologies that can streamline my workflow and unlock new capabilities. That’s why I was excited about the recent addition of Model Context Protocol (MCP) support in the Amazon Q Developer command line interface (CLI). MCP is an open protocol that standardizes how applications can seamlessly integrate with LLMs, providing a common way to share context, access data sources, and enable powerful AI-driven functionality. You can read more about MCP in [this introduction](https://modelcontextprotocol.io/introduction).

Q Developer has had the ability to use tools for a while. I previously discussed [the ability to run CLI commands and describe AWS resources](https://aws.amazon.com/blogs/devops/introducing-the-enhanced-command-line-interface-in-amazon-q-developer/). With the Q Developer CLI’s support for MCP tools and prompts, I now have the ability to add additional tools. For example, while I have had the ability to describe my AWS resources, I also need to describe database schemas, message formats, etc. to build an application. Let’s see how I can configure MCP to provide this additional context.

In this post, I will configure an MCP server to provide Q Developer with my database schema for a simple Learning Management System (LMS) that I am working on. While Q Developer is great at writing SQL, it does not know the schema of my database. The table structure and relationships are stored in the database and are not part of the source code of my project. Therefore, I am going to use an MCP server that can query the database schema. Specifically, I am using the [official PostgreSQL reference implementation](https://modelcontextprotocol.io/examples) to connect to my [Amazon Relational Database Service (RDS)](https://aws.amazon.com/rds/). Let’s get started.

## Before Model Context Protocol

Prior to the introduction of MCP support, the Q Developer CLI provided a set of native tools, including the ability to execute bash commands, interact with files and the file system, and even make calls to AWS services. However, when it came to querying a database, the CLI was limited in its capabilities.

For example, prior to configuring the MCP server, I asked Q Developer to “Write a query that lists the students and the number of credits each student is taking.” In the following image you can see that Q Developer could only provide a generic SQL query, as it lacked the specific knowledge of the database schema for my LMS.

![Screenshot of Amazon Q Developer CLI showing a response to a query request. The response includes explanatory text acknowledging the lack of schema information, followed by a generic SQL query written in green text. The query joins students, student_courses, and courses tables to calculate total credit hours per student, demonstrating Q's limited ability without MCP configuration.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/28/mcp001.png)

While this is a great start, I know that Q developer could do so much more if it knew the database schema.

## Configuring Model Context Protocol

The introduction of MCP support in the Q Developer CLI allows me to easily configure MCP servers. I configure one or more MCP servers in a file called `mcp.json`. I can store the configuration in my home directory (e.g. `~/.aws/amazonq/mcp.json)` and it is applied to all projects on my machine. Alternatively, I can store the configuration in the workspace root (e.g. `.amazonq/mcp.json)` so it is shared among project members. Here is an example of the configuration for the PostgreSQL MCP server.

```
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://USERNAME:PASSWORD@HOST:5432/DBNAME"
      ]
    }
  }
}
```

With the MCP server configured, let’s see how Amazon Q Developer enhances my experience.

## After Model Context Protocol

First, I start a new Q Developer session and immediately see the benefits. In addition to the existing tools, Q Developer now has access to PostgreSQL as shown in the following image. This means I can easily explore the schema of my database, understand the structure of the tables, and even execute complex SQL queries, all without having to write any additional integration code.

![Screenshot of Amazon Q Developer CLI displaying a list of available tools. The tools are categorized into file system tools, bash execution, AWS tools, PostgreSQL database tools, and issue reporting. The PostgreSQL category is highlighted, showing the integration of MCP for database access.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/28/mcp002.png)

Let’s test the MCP server by asking Q Developer to “List the database tables.” As you can see in the following example, Q Developer now understands that I am asking about the PostgreSQL database, and uses the MCP server to list my three tables: students, courses, and enrollment.

![Screenshot of Amazon Q Developer CLI showing a database table listing request and response. The response shows a tool request using list_objects command with JSON parameters, followed by execution status and a list of three tables in the public schema: courses, enrollment, and students.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/28/mcp003.png)

Let’s go back to the example from earlier in this post. Now, when I ask Q Developer to “Write a query that lists the students and the number of credits each student is taking,” it no longer responds with a generic query. Instead, Q Developer first describes the relevant tables in my database, generates the appropriate SQL query, and then executes it, providing me with the desired results.

![Screenshot of Amazon Q Developer CLI showing a complete SQL query workflow. The image displays a precise SQL query in green syntax highlighting, followed by a results table showing student credit information, and an explanation of how the query works through five numbered steps. This demonstrates Q's ability to generate, execute, and explain database queries with schema knowledge.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/28/mcp004.png)

Of course, Q Developer can do a lot more than just write queries. Q Developer can use the MCP server to write Java code that accesses the database, create unit tests for the data layer, document the database, and much more. For example, I asked Q Developer to “Create an entity-relationship (ER) diagram using Mermaid syntax.” Q Developer was able to generate a visual representation of the database schema, helping me better understand the relationships between the various entities.

![Entity-Relationship (ER) diagram generated by Amazon Q Developer. The diagram shows three tables: STUDENTS, COURSES, and ENROLLMENT. Each table is represented by a box containing column names and data types. The ENROLLMENT table links STUDENTS and COURSES with 'enrolls in' and 'has enrolled' relationships. Primary and foreign keys are indicated. This visualizes the database schema structure for the Learning Management System.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/28/mcp005.png)

The integration of MCP into the Q Developer CLI has significantly streamlined my workflow by allowing me to add additional tools as needed.

## Conclusion

The addition of MCP support in the Amazon Q Developer CLI provides a standardized way to share context and access data sources. In this post, I’ve demonstrated how I can use the Q Developer CLI’s MCP integration to quickly set up a connection to a PostgreSQL database, explore the schema, and generate complex SQL queries without having to write any additional integration code. Moving forward, I’m excited to see how you can leverage MCP to further enhance your development workflow. I encourage you to [explore the MCP capabilities](https://docs.aws.amazon.com/en_us/amazonq/latest/qdeveloper-ug/command-line-mcp.html) and the [AWS MCP Servers](https://github.com/awslabs/mcp) repository on GitHub.

TAGS: [Developer Tools](https://aws.amazon.com/blogs/devops/tag/developer-tools/), [Development](https://aws.amazon.com/blogs/devops/tag/development/)

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