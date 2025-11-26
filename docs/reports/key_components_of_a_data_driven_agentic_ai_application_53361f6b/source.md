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

# Key components of a data-driven agentic AI application

by Marc Brooker, David Castro, and Vlad Vlasceanu on 03 OCT 2025 in [Artificial Intelligence](https://aws.amazon.com/blogs/database/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Database](https://aws.amazon.com/blogs/database/category/database/ "View all posts in Database"), [Generative AI](https://aws.amazon.com/blogs/database/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Thought Leadership](https://aws.amazon.com/blogs/database/category/post-types/thought-leadership/ "View all posts in Thought Leadership") [Permalink](https://aws.amazon.com/blogs/database/key-components-of-a-data-driven-agentic-ai-application/)  [Comments](https://aws.amazon.com/blogs/database/key-components-of-a-data-driven-agentic-ai-application/#Comments)  Share

Agentic AI promises to enhance productivity and efficiency, taking on problems that can’t be solved with traditional software, simplifying integration, and finding answers in data that were previously invisible. Agentic AI systems autonomously decide how to accomplish a task and take the necessary actions to accomplish the task, adapting their plan as they learn more information. There’s still a human in the mix, only now the human gets to give the system a broad instruction in natural language and exercises supervisory control. Humans focus on the goal, while agents figure out the details of achieving the goal. While the human interface changes, agentic AI systems still rely on the same backend functions to accomplish tasks. Let’s look at a basic side-by side comparison example of an ecommerce product purchasing experience. As shown in the following figure, the agent takes over most of the online purchasing steps that would otherwise have to be taken by the customer.

[![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/10/02/DBBLOG-5187-1.png)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/10/02/DBBLOG-5187-1.png)

In this example, the agentic AI system still needs to trigger the processing of a financial transaction, inventory tracker updates, and fulfillment and order confirmation workflows. You still need the same backend services and databases that implement these workflows. However, this example raises a question: “*Couldn’t the agentic AI system directly interact with the databases to subtract from the stock inventory or call the card network APIs to charge a payment card?*”

In this post, we look at the costs, benefits, and drawbacks of replacing services for agentic AI with direct database access. Including those that work well and are proven in production, and new services yet to be built. Let’s take a closer look at the anatomy of an agentic AI application and what would factor into such decisions.

## Anatomy of an agentic AI application

At the center of an agentic AI application is a *loop*. When the user instructs the system to complete a task, the workflow enters an event loop where it iterates until it considers the task completed or the question answered. The system might come back to the user for clarifications or prompts for additional information.

This design pattern, shown in the following figure, is called the [Reason+Act](https://agent-patterns.readthedocs.io/en/stable/patterns/re_act.html) (or ReAct) loop, and is the most popular design pattern for agentic AI systems.

[![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/10/02/DBBLOG-5187-2.png)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/10/02/DBBLOG-5187-2.png)

Loops like this are used by various agents, from those interacting with customers (such as chatbots), to autonomous agents optimizing business processes, and research agents. The event loop is implemented across agent development frameworks, such as [Strands Agents](https://strandsagents.com/latest/) or [LangGraph](https://www.langchain.com/langgraph), managed services such as [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html), or user agent applications such as [Amazon Q Business](https://aws.amazon.com/q/business/), [Q Developer](https://aws.amazon.com/q/developer/), or [Claude Desktop](https://claude.ai/). You can generally expect the following components and workflows to be present:

* A **context management** component that retrieves, aggregates, and filters the data required to provide as context for each iteration of the ReAct event loop. This component oversees retrieving data from diverse sources including the conversation state, previously created memories (for example, user preferences and conversation history), and the result of tool executions. After data is retrieved, this component helps select the most relevant data to be used in the next large language model (LLM) invocation.
* A **reasoning and planning** component, which infers the user intent, includes the relevant context and creates or revises a plan of actions to complete the requested user task. This component might decide it has enough information based on context and data available in the context management component (memory) to respond back to the user. Or it might decide to take one or more actions and record the results in memory, incrementally working towards completing the user task.
* A **tool or action execution** component that uses a set of [tools](https://huggingface.co/learn/agents-course/en/unit1/tools) available to take actions towards completing the task. This workflow is typically comprised of invoking the tool using the inputs received from the reasoning and planning component and capturing the response into the context management component for the next iteration of the event loop.

This basic architecture allows an agentic AI application to accomplish tasks within the scope it was designed for, over the course of multiple event loop iterations. The more event loop iterations it takes to accomplish a task, the slower and less efficient the agentic AI application is. Along the way, an unpredictable number of LLM invocations can occur, consuming a non-deterministic amount of input and output [tokens](https://blogs.nvidia.com/blog/ai-tokens-explained/), with impact both on cost and performance. Dropping out of the event loop to ask the user for additional data or clarifications also impacts both cost and performance. Diving deeper into the components of the event loop, let’s discover mechanisms to optimize the loop and user experience by extension.

## The context management component of an agentic AI application

While AI agents gain sophisticated reasoning capabilities from LLMs, they face two key limitations inherent to these models. First, LLMs are stateless and unable to remember past interactions or maintain context, and second, their finite [context window](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-a-context-window) restricts the volume of data that can be processed at each step.

The context management component helps developers manage the context window for each iteration of the agent’s event loop. [Context engineering](https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider) is the art and science of carefully selecting the right information to include in the context window at each step of the agent’s execution. The right information for the context window might include user instructions (system and user prompts and tool descriptions), previous memories (conversation history and user preferences), external knowledge (enterprise knowledge bases and authoritative sources), the results of tool executions (API call results), and other data sources.

As an agent executes its loop, it might accumulate large amounts of data from these sources. This can result in a context that exceeds the LLM’s context window so aggregating the data from previous interactions is not an effective solution. Even for LLM models that support a large number of tokens in the context window, the effectiveness of inferences decays as the amount of context increases, making agents more prone to hallucination, overlooking valuable information, or failing to execute their tasks. For this reason, it’s important to carefully filter and select the most valuable data to include in the context window for each LLM inference.

Let’s look at some of the sources of data needed for an agent to operate effectively:

### Instructions

Instructions for an LLM interaction include information such as the system prompt, the user prompt, the tool selection information, and result examples. The system prompt gives the agent instructions such as its role, capabilities, personality, and constraints. The user prompt is the direct user request. The tool selection information is contextual data needed by the agent to select the right tool to execute a task. We discuss tools later in this post.

### Short-term memory

Short-term memory includes the session and state. The session stores the chronological flow of interactions within conversations and task executions. Like web application sessions, the session data requires fast access to recent interaction history and operates as ephemeral storage with time-based expiration. The state acts like the agent’s dedicated scratchpad for each specific interaction. The state memory is where the agent stores and updates dynamic details needed during the task execution such as the to-do list and its progress executing that list. When thinking about the right infrastructure to store this type of data, some common requirements include high-frequency updates, configurable retention policies, session-end memory clearing, and fine-grained session-scoped control. Local agents such as Q Developer, [Claude Code](https://www.anthropic.com/claude-code), and [Cline](https://cline.bot/) use the file system to store session and state. Online agents can use a specialized short-term memory service, like Bedrock AgentCore short-term memory or caches like [Amazon ElastiCache for Valkey](https://aws.amazon.com/elasticache/what-is-valkey/).

### Long-term memory

Long-term memory includes the facts, relationships, and learned behaviors that agents accumulate over time. This means that they don’t need to start from the beginning with each customer or problem on every interaction. Memories allow agents to use prior success patterns, context they’ve learned, and what they know about customers to solve problems more quickly with less customer interaction. After the agent has gathered significant information (often at the end of a session), it can execute a parallel memory extraction process. This process involves asking an LLM to identify relevant information by passing session and state data. The newly extracted memory may be stored in a vector database if it later needs to be searched using similarity search, or in a relational database if it needs to be retrieved through more deterministic queries.

Technical requirements for the database for long-term memories include [vector search](https://aws.amazon.com/blogs/database/the-role-of-vector-datastores-in-generative-ai-applications/) and pre-filtering capabilities to narrow search scope and improve lookup latencies. The memory primitive of Bedrock AgentCore provides these capabilities, along with custom chunking and summarization strategies. Developers also choose databases such as [Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) and [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) to keep vectors with their application data.

To improve memory retrieval, developers can combine vector search with knowledge graphs (GraphRAG). Developers can organize memories in a knowledge graph as interconnected entities and relationships, enabling agents to understand complex dependencies and make inferences based on the connected information. [Amazon Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html) provides the graph definition, retrieval, and dynamic relationship creation support required to store and retrieve memories from a knowledge graph.

### External knowledge bases

Knowledge bases are centralized repositories of structured and unstructured information that serve as grounding data for AI applications. They include documents, FAQs, product specifications, procedures, best practices, and domain-specific expertise. Databases, such as Aurora PostgreSQL, store text as high-dimensional vectors (embeddings), enabling vector searches that understand context and meaning rather than just keyword matching. These capabilities are essential for agents to retrieve the most relevant information using vector search to identify semantic similarity. Developers can also create a knowledge base by using specialized RAG services like [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/), which provide an end-to-end RAG management workflow.

### Data retrieved through tool executions

Tools act as bridges between the AI agents and external systems, enabling dynamic data access. Agents can retrieve a diverse range of data types through tools, such as real-time information (weather, stock prices, news), computational results (calculations, data analysis), and external API data (CRM records, inventory levels). We cover data retrieval tools more in the tool execution component section later in this post. With appropriate context, the reasoning and planning component can determine the most effective path to completing the user task.

## The reasoning and planning component of an agentic AI application

The reasoning and planning component collects the end user question and all context from previous event loop iterations and submits that as input to an LLM for inference. The context sent to the LLM includes the filtered list of the most critical data obtained by the context management module, including instructions, memories, data from knowledge bases and database tools. The response received from the LLM can be one of three options:

* **Respond to the user:** The LLM inference output can contain a response to the user indicating that the task has been completed (or in rare cases, that the agent gave up because of errors or other reasons).
* **Ask user for more information:** Similar to responding to the user, this option will expect a response back from the user. With the additional data from the user in the context, the system can start a new event loop iteration.
* **Select a tool to invoke:** The LLM inference output can contain instruction specifying which tool to invoke (the options were provided part of the system prompt) and the input parameters to use.

Agentic AI systems are often more complex than what we described here because they need to minimize the number of event loop iterations needed to accomplish a task and be more discerning with LLM calls for optimal price performance. Advanced reasoning and planning components might use rules or an LLM to break down the user question into a set of actions (steps) needed to complete the task. Certain planned actions might be executed in parallel (if they don’t depend on each other), thus reducing latency (Strands, for example, allows LLMs to call tools in parallel using a batch interface). For other actions, the initial LLM response that determined the action plan might have already provided the needed input parameters, thus avoiding another LLM call before tool invocation. If a separate LLM call is needed to derive tool input parameters, it might be possible to use smaller specialized LLMs or [small language models](https://www.redhat.com/en/topics/ai/llm-vs-slm) (SLMs). These optimizations improve latency and lower inference cost.

A new emerging design pattern shifts some of the secondary LLM calls to the tool itself. For example, a tool designed to execute queries on a relational database might accept natural language, then make a call by itself to an LLM to generate the corresponding SQL query before connecting to the database and executing the query. The tool can use a model optimized for generating SQL queries as opposed to a larger, general-purpose model. Such a tool is effectively an agent unto itself with its own event loop, iteratively trying out generated queries until it gets the correct one. In this [agents as tools](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/multi-agent/agents-as-tools/) pattern, the memory of the main agent isn’t polluted with context from failed query attempts in the tool. Previously, we [wrote about the convergence of tools and agents in MCP](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp/).

## The tool invocation component

While it might be tempting to think the LLM in the reasoning and planning component directly invokes the correct tool, this is not the case. The LLM has no direct ability to take actions or execute code; instead, it returns a set of instructions specifying what tool to run and what parameters to use. The agentic AI system implementing the event loop then parses the response and invokes the requested tools with the parsed parameters, returning either a natural language or [structured response](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/agents/structured-output/), depending on how the tool was intended to work.

What counts as a tool? Any business logic that takes in a set of input parameters and returns a response back counts as a tool. Frameworks, such as Strands Agents, commonly offer a built-in reference tool that returns the current date and time. This is a basic tool that can be useful where point in time matters for context. At the other end of the spectrum, you can expose entire agents as tools to other agents, as mentioned previously. With such diversity of tools, you need a standardized way to access them.

[Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP) provides that standardized way of declaring and using tools in an agentic AI system. The protocol has a [server](https://modelcontextprotocol.io/docs/learn/server-concepts) and a [client](https://modelcontextprotocol.io/docs/learn/client-concepts) component. The MCP server exposes a set of tools that can be accessed over the MCP protocol. For example, the [Amazon Aurora DSQL MCP server](https://awslabs.github.io/mcp/servers/aurora-dsql-mcp-server/) makes three tools available: table schema discovery, read only query, and a transaction that mutates data. Using these three tools, an agentic AI system can retrieve the schema of the database, compose SQL queries, execute them, and return the results.

The MCP client is effectively an interface construct in your agentic AI system. Because of the standardization offered by MCP, an MCP client can communicate with any MCP server. By implementing an MCP client in your agentic AI system, you can register any tool provided by an MCP server, and have your agent start using it. The following figure shows an example AI agent using five tools. One tool is built-in, three tools are accessible via MCP, and the last is a separate agent exposed as a tool.

[![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/10/02/DBBLOG-5187-3.png)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/10/02/DBBLOG-5187-3.png)

All tools operate in some form or another on data. To better highlight the role of data in agentic AI systems, we separate tools into two categories: *data retrieval* tools and *data manipulation* tools.

Data retrieval tools are used to fetch relevant context needed for the agent to accomplish a task. This data is retrieved directly from databases, data lakes, and analytic systems. Alternatively, data is retrieved from other services and applications such as an enterprise resource planning (ERP) system. Apart from [semantic data retrieval from vector databases](https://aws.amazon.com/blogs/database/the-role-of-vector-datastores-in-generative-ai-applications/), agentic AI doesn’t require or even prefer the use of one database technology over another. The database technology should largely be selected based on the nature of the data stored and access patterns. Agentic AI is more likely to democratize access to a diverse set of data services than depend on specific ones. AWS offers [MCP servers](https://awslabs.github.io/mcp/servers/) for most of our managed database and analytics services, including [Amazon Aurora](https://awslabs.github.io/mcp/servers/postgres-mcp-server), [Amazon DynamoDB](https://awslabs.github.io/mcp/servers/dynamodb-mcp-server), [Amazon ElastiCache](https://awslabs.github.io/mcp/servers/valkey-mcp-server), [Amazon Redshift](https://awslabs.github.io/mcp/servers/redshift-mcp-server), and [Amazon S3 Tables](https://awslabs.github.io/mcp/servers/s3-tables-mcp-server). These simplify the way you interact with data stored in these systems from both existing agentic AI applications or new ones you build yourself.

Data manipulation tools are used to make changes to data, either directly in a database or indirectly through other services and APIs. Using an agentic AI system to purchase a toy fire truck, as the earlier example described, involves invoking tools that decrement inventory, process financial transactions, and add orders to your order history. These actions involve making changes to data in a variety of data stores, even if they are abstracted away using APIs.

The preceding examples lead to another important distinction between tools: *general purpose* or *specialized*. This is better illustrated using an example. One of the authors, Vlad, is a big fan of LEGO toys and likes to have an inventory of the bricks present in any of the sets he owns (too many). This helps him identify missing bricks, or how many bricks of a specific kind he might have. He stores this data in [Aurora DSQL](https://aws.amazon.com/rds/aurora/dsql/) because it’s a highly resilient relational database that requires minimal operational overhead for the use case.

Vlad can use the Aurora DSQL MCP server and plug it into an agentic AI system like Amazon Q or Claude. Now, these applications can answer questions about his LEGO collection, because they have appropriate tools to do so. This is quick and efficient to set up, and he can ask a wide variety of questions on an as-needed basis. What happens within the system? The agent goes through multiple event loop iterations to get to an answer: first it must discover the schema of the database, and then it must assemble the right SQL query to answer Vlad’s question.

Anecdotally, it usually takes an additional two to three event loop iterations to generate a valid SQL query that fetches the data he needs. That used approximately four LLM API calls to get an answer. Even though it takes a long time to get an answer, it is acceptable relative to the level of effort Vlad made setting this general purpose MCP server up, if he asks these questions infrequently.

But what if Vlad frequently asks his agent about the inventory level of specific bricks owned? At scale, it will be more efficient for him to build a specialized tool that can deterministically retrieve the inventory level of his bricks. He can effectively eliminate the LLM calls that perform text to SQL conversion, reducing his LLM API call usage down potentially to one: the reasoning and planning component determining that it needs to invoke his specialized tool with the brick type and color as input parameters. This is often called the *canned query* MCP pattern. General purpose and specialist tools are often complementary. In this use case, he can use the specialized tool for frequent queries, and the general purpose tool for one-time queries.

You can see how reducing the number of event loop iterations needed to complete a task will be key to both performance and cost optimization for your agentic AI application, and the use of data is one way to accomplish this goal.

While general purpose tools and specialized tools are complementary, they lend themselves to different roles. For transactional systems, wrapping database interactions into services and exposing those services as tools leads to more deterministic results and better overall performance. In contrast, general purpose tools interacting with a database (text2SQL or similar) will be more useful in analytical systems and data discovery use cases.

For completeness, let’s close the event loop. After tools are invoked, results are fed back into the memory of the agentic AI system so context management can be applied to them. The next iteration of the event loop will have these results in the context for the next decision.

Other components can be added to the event loop when considering more advanced implementations, such as [guardrail](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-are-ai-guardrails) components to keep agent responses correct, focused, and ethical; or a learning and adaptation component to learn from past experiences using a feedback loop.

## Conclusion

The modular nature of agentic AI systems means you can add more capabilities over time, whether you’re building agentic AI applications or consuming existing agentic AI applications, such as Amazon Q or Claude. You can expand the abilities of those systems using MCP servers. Using this mechanism to tap into your data, whether operating on it or just retrieving context, presents an opportunity to make these applications more efficient for your particular use cases. Understanding when and how data interacts with your application (memory and tools) puts you in a better position to select the right data architecture, factoring in both the nature of your data and how you access it.

---

### About the authors

![Marc Brooker](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/10/02/marc-brooker.png)

### Marc Brooker

[Marc](https://www.linkedin.com/in/marc-brooker-b431772b/) is a VP and Distinguished Engineer at AWS. During his 16 years at AWS, Marc has worked on EC2, EBS, Lambda, and most recently lead the team that launched Aurora DSQL. He is currently focused on infrastructure for agentic AI, and the availability and security of our large-scale systems. Before AWS, Marc completed his PhD at the University of Cape Town.

![David Castro](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/10/02/headshot-Copy.jpg)

### David Castro

[David](https://www.linkedin.com/in/josuetas/) is a Principal Product Manager at Amazon Web Services (AWS), spearheading the development of AWS database capabilities for agentic memory and next-generation caching solutions. With over seven years at Amazon since 2017, he has consistently driven the vision, strategy, and execution of highly scalable data products across Alexa and AWS. Currently, David leads product teams developing Amazon ElastiCache Serverless.

![Vlad Vlasceanu](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2023/07/25/vlad.jpg)

### Vlad Vlasceanu

[Vlad](https://www.linkedin.com/in/vladvlasceanu/) is the Worldwide Tech Leader for Databases at AWS. He focuses on accelerating customer adoption of purpose-built databases, and developing prescriptive guidance mechanisms to help customers select the right databases for their workloads. He is also the leader of the database expert community within AWS, where he helps develop Solutions Architects’ database skills and enables them to deliver the best database solutions for their customers.

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