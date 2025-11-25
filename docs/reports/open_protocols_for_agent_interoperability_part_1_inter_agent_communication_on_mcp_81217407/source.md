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

## [AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/)

# Open Protocols for Agent Interoperability Part 1: Inter-Agent Communication on MCP

by Nick Aldridge, Marc Brooker, and Swami Sivasubramanian on 19 MAY 2025 in [Artificial Intelligence](https://aws.amazon.com/blogs/opensource/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Generative AI](https://aws.amazon.com/blogs/opensource/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Open Source](https://aws.amazon.com/blogs/opensource/category/open-source/ "View all posts in Open Source"), [Thought Leadership](https://aws.amazon.com/blogs/opensource/category/post-types/thought-leadership/ "View all posts in Thought Leadership") [Permalink](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp/)  [Comments](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp/#Comments)  Share

At AWS, open standards run deep in our DNA, driving all that we do. That’s why we decided to build Amazon Elastic Cloud Compute (EC2) as a protocol-agnostic cloud computing service and Amazon SageMaker as a framework-agnostic deep learning service. Our commitment to openness continues as we enter the agentic AI era, extending to inter-agent communication. Multiple protocols have emerged that enable this capability, including the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol), open sourced by Anthropic in 2024, and the [Agent2Agent protocol (A2A)](https://github.com/google/A2A), introduced by Google this year. We believe that both MCP and A2A have a lot to offer. Demonstrating our commitment to these open standards, AWS is joining the steering committee for MCP. By supporting multiple protocols, we ensure developers can build breakthrough agentic applications without being tied to one standard.

Open source protocols have been key in enabling innovation. From internet protocols like REST and GraphQL to deep learning frameworks such as TensorFlow and PyTorch, these standards have enabled widespread development and adoption. Now, as developers leverage agent collaboration to automate workflows and create intelligent experiences, new standards like MCP and A2A are emerging for connecting LLM-powered agents to tools and other agents.

AWS is helping developers build interconnected generative AI applications through new services, open source contributions, and best practices. We recently launched [Strands Agents](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/), an open source SDK for building and running AI agents in just a few lines of code. Strands supports various models through integrations with Amazon Bedrock, Anthropic API, Llama API, Ollama, and others via LiteLLM. It works with MCP and will soon support A2A and [OpenTelemetry (OTEL)](https://github.com/open-telemetry) for observability. We believe agentic AI’s full potential depends on open and inter-operable standards.

This blog post is the first in a series diving into the technical details of these advances. We explore how MCP can be used to enable agent-to-agent communication, and highlight AWS’s efforts to simplify this pattern. While this post focuses on evolving MCP, we believe more work is needed in the broader agentic AI space with code-first SDKs, inter-agent communication and open observability standards. Stay tuned as we continue exploring the evolving agentic AI landscape.

## The Evolution of MCP

Developers have embraced MCP as a standard for connecting generative AI agents with external systems. While the initial focus was on tool integration, MCP’s architecture also enables agents to interact with other agents because it already offers fundamental capabilities needed for these interactions. Not surprisingly, we are seeing the MCP community organically contribute to evolve the protocol to provide additional inter-agent capabilities and abstractions.

To help make inter-agent communication on MCP even better, AWS is contributing to MCP and collaborating with leading open source agent frameworks, including LangGraph, CrewAI, and LlamaIndex, to shape the future of inter-agent communication on the protocol. We are also working with innovative companies like Autodesk, Confluent, Dynatrace, Elastic, IBM, Workday, and Writer, who are pushing the boundaries of what can be built on MCP and collectively moving the community forward.

## Building on a Strong Technical Foundation

At its heart, MCP was designed with flexibility and extensibility in mind, creating a foundation that extends from tool integration to agent collaboration. MCP already provides the core infrastructure needed for agents to communicate with each other including support for multiple communication regimes, authentication / authorization, capability negotiation, and context sharing.

### Streamable HTTP for Flexible Communication

Multi-agent communication can take on a variety of different patterns depending on the complexity and design of the interacting agents. MCP’s Streamable HTTP implementation gives developers a rich palette of interaction patterns without having to reinvent the wheel. You can implement stateless request/response flows for simple, one-off interactions between agents. For more complex dialogues, the stateful session management with persistent IDs preserves context across multiple exchanges.

The Streamable HTTP transport also enables response streaming using Server-Sent Events (SSE) for real-time data exchange. Over SSE, MCP supports progress notifications, request cancellation, and response buffering during client disconnects. These features are perfect for building longer-running agents that need to share continuous updates with each other.

### MCP Capability Discovery and Negotiation

For agents to collaborate effectively, each needs to understand what the other can do. MCP addresses this need through its capability discovery feature. When agents connect, they can negotiate which protocol features will be available during their session. This determination happens at the server level but extends down to individual tools or skills that agents expose to each other.

Each agent can declare detailed descriptions of their capabilities (modeled as tools) along with the parameters they accept. The tool notification system allows agents to be notified when new capabilities become available or existing capabilities change. This notification creates a dynamic ecosystem where agents can discover and leverage each other’s evolving skillsets, forming networks that adapt and grow more capable over time.

### MCP Security

Trust and security form the foundation of effective agent collaboration. MCP implements OAuth 2.0/2.1-based authentication and authorization at the transport layer, ensuring that agents can verify each other’s identities and maintain appropriate access controls.

### Context Sharing

Like humans, agents need reliable mechanisms to share context (files, application state, agent memory) with one another. MCP enables agents to share a wide variety of data using its resource capability. With MCP resources, agents can share information about the context they have available, and allow other agents to retrieve that context. MCP also allows agents to subscribe for notifications on resource changes so that developers can implement sophisticated inter-agent workflows with dependencies between agents.

Agents can also share prompts with one another and they can even share LLMs. This capability is called sampling. Sampling enables agentic workflows, such as providing interactive assistance, and works in the following way:

1. Server sends a sampling request to the client

2. Client reviews the request and can modify it

3. Client samples from an LLM

4. Client reviews the completion

5. Client returns the result to the server

## Implementing Agent-To-Agent Communication on MCP

Before diving in, let’s break down how to implement agent-to-agent communication with MCP today and the architectural components involved.

[![MCP agent-to-agent interaction](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/05/20/mcp-mermaid-1024x105.png)](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/05/20/mcp-mermaid.png)

Image 1: Visualization of an example agent-to-agent interaction using MCP.

**Agent:** An agent uses AI to autonomously complete a task. Agents often rely on external data and services or other Agents to help them complete their task. MCP provides a communication layer that enables agents to interact with external data and services and can also be used to enable agents to interact with other agents.

**Tool / Agent Skill:** Tools often perform operations against APIs or databases, but tools can also implement an agent skill or a specific capability of an agent. These agentic tools internally invoke an agent to handle the incoming request.

**MCP Server:** MCP servers handle incoming requests and route them to the appropriate tool / resource methods, then return the results back to the caller.

**MCP Client:** MCP clients provide a way to communicate with an MCP server. An agent may use MCP client(s) to connect to MCP servers to help complete the agent’s task. For example, the agent can invoke an MCP client, such as initiating a CallToolRequest to trigger a tool. The MCP Client will then initiate a CallToolRequest against the MCP server it is connected to.

Let’s consider a simplified example where a human resources (HR) employee asks a question about employee skills to an HR Agent. The HR Agent relies on another agent, the Employee Info Agent, to answer the user’s question.

[![MCP sequence diagram](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/05/19/MCP-sample-architecture-1024x595.png)](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/05/19/MCP-sample-architecture.png)

Image 2: Sequence diagram depicting the HR Agent (Agent 1) interacting with the Employee Data Management Agent (Agent 2).

Let’s see how we would build this architecture in Java using Spring AI. First, let’s say there is an MCP server that exposes data for an employee database. I can now build an agent (the Employee Info Agent) that uses the tools from the employee database MCP server:

```
@Bean
ChatClient chatClient(
    List<McpSyncClient> mcpSyncClients,
    ChatClient.Builder builder
) {
    return builder
            .defaultToolCallbacks(
                new SyncMcpToolCallbackProvider(mcpSyncClients)
            )
            .build();
}

...
// agent that does the MCP tool calling and adds a system prompt into the flow
String employeeInfoAgent(String query) {
    return chatClient
            .prompt()
            .system("abbreviate first names with first letter and a period")
            .user(query)
            .call()
            .content();
}
```

In this example the ChatClient provides the interface to the LLM, handles the tool calling (with MCP), and does the necessary multi-turn conversation with the LLM.

To expose the Employee Info Agent to other agents, we only need to wrap it in an MCP server tool:

```
@Tool(description = "answers questions related to our employees")
String employeeQueries(
	@ToolParam(description = "the query about the employees",
		required = true) String query) {
    return employeeInfoAgent(query);
}
```

Now that we have the Employee Info Agent exposed as an MCP Server, let’s see how we can integrate it with another agent, the HR agent. Suppose the HR agent is exposed as a REST endpoint. We can configure the HR agent to use the Employee Info Agent using MCP, the code is simply:

```
/* Configure the MCP Servers, e.g. in application.properties:
   spring.ai.mcp.client.sse.connections.employee_root.url=${mcp-
   service.url:http://localhost:8081}
*/

// LLM chat client which is configured to use the employee info agent via MCP
@Configuration
class ConversationalConfiguration {
    @Bean
    ChatClient chatClient(List<McpSyncClient> mcpSyncClients, ChatClient.Builder builder) {
        return builder
                .defaultToolCallbacks(new SyncMcpToolCallbackProvider(mcpSyncClients))
                .build();
    }
}

record Prompt(String question) { }

@RestController
class ConversationalController {

    private final ChatClient chatClient;

    ConversationalController(ChatClient chatClient) {
        this.chatClient = chatClient;
    }

    @PostMapping("/inquire")
    String inquire(@RequestBody Prompt prompt) {
        return chatClient
                .prompt()
                .user(prompt.question())
                .call()
                .content();
    }
}
```

And that is all that is needed to do inter-agent communication with Spring AI and MCP. Of course, you can use other languages and agent frameworks, or even mix and match technologies.

Agents exposed as MCP servers provide a micro-service-like architecture that decouples agents from each other, leveraging MCP as the common protocol for communication. You can get the complete working example [here](https://github.com/aws-samples/Sample-Model-Context-Protocol-Demos/tree/main/modules/spring-ai-mcp-inter-agent-ecs).

## Enhancing MCP for Inter-Agent Collaboration

We believe that by evolving MCP on top of this existing foundation, we can make the experience of building inter-agent interactions on MCP even better. AWS, and the rest of the MCP community, are engaged in active discussions to define the right investments for enhanced inter-agent interactions. Here are just a few: [[Discussion](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/111)] [[Discussion](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/330)] [[Discussion](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/503)]. Suggested enhancements (including AWS-led proposals) include:

* **Human In the Loop Interactions**. Updates to the MCP specification and Python SDK to introduce “elicitation” to enable MCP servers to request more information from an end user. [[Specification PR](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/382)] [[Implementation PR](https://github.com/modelcontextprotocol/python-sdk/pull/625)]
* **Streaming Partial Results**. An update to the MCP specification and Python SDK to enable providing partial results as a server is processing a long-running request. Note: intermediate results are already supported via SSE. [[Specification PR](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/383)] [[Implementation PR](https://github.com/modelcontextprotocol/python-sdk/pull/669)]
* **Enhanced Capability Discovery**. Updates to the MCP specification and Python SDK to enable tools/agent skills to declare their output schema and incorporate additional capability metadata for tools/agent skills. [[Specification PR](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/371)] [[Implementation PR](https://github.com/modelcontextprotocol/python-sdk/pull/654)] [[Specification PR](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/489)]
* **Asynchronous Communication**. Updates to the MCP specification to support simpler abstractions for asynchronous communication, shared state, and client-poller-driven status checks. [[Specification PR](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/500)]

We are committed to the goal of seamless inter-agent collaboration and we welcome feedback from those actively working in this space to help shape the future of inter-agent collaboration on MCP. You’ll also be seeing more from AWS in this space. We’re just getting started.

## MCP Is Generating Excitement and Opportunities

The excitement about MCP from developers across companies and the tech community is palpable. Many of our partners who are driving innovation in generative AI see MCP as the protocol of choice for inter-agent communication. We are excited about getting to collaborate and learn from each other as we work together to improve MCP in the open.

“*With Confluent’s real-time data streaming platform serving as the connective tissue between tools and agents, MCP unlocks unprecedented interoperability. Together with AWS and the MCP community we’re proud to advance a unified standard that brings the full power of real-time context to autonomous agents at scale, enabling seamless agent-to-agent interactions and data sharing.*” – Pascal Vantrepote, Sr. Director, Partner Innovation Engineering, Confluent

“*At CrewAI, we’ve long championed open standards as the foundation for scalable, secure agent ecosystems. We’re seeing multiple patterns emerge around agent interoperability, and it’s still early days—but it’s clear that MCP is gaining real traction and we expect it to meaningfully shape whatever the final version of this layer looks like. A unified MCP is an important step toward agent interoperability and we’re glad to see AWS helping push that forward in the MCP community. As agentic systems mature, collaboration across vendors and systems will be key. We’re committed to contributing to that future, with flexibility and openness at the core of everything we build.*” – João Moura, Founder & CEO, CrewAI.

“*With Bedrock and Dynatrace, customers can build smart, agentic systems for auto-remediation, protection, and automation. Customers have the flexibility to choose from a variety of commercial MCP integrations as well as open-source community contributions to build these use cases, all enabled by agent interoperability.*” – Alois Reitbauer, Chief Technical Strategist, Dynatrace

“*Elastic is committed to advancing open standards for organizations to innovate. A unified MCP standard for tools, resources, and agent-to-agent interoperability accelerates customer success by simplifying integration and enabling smarter automation across AI-driven applications. We are happy to be partnering with AWS and the broader MCP community to help shape a future with accessible and scalable AI.*” – Steve Kearns, GVP and GM of Search, Elastic

“*MCP provides an opportunity to break open the agentic landscape and IBM is both using MCP as an agent interoperability layer in its software while building MCP capability into our AI-focused products such as Watsonx Orchestrate. We look forward to collaborating with AWS and the broader MCP community.*” – Anant Jhingran, IBM Fellow & CTO, Software, IBM

“*LangGraph, adopted by LinkedIn, Uber, Klarna, and more, is one of the most popular ways for developers to build agents because of its controllability and stateful memory layer. Being open and interoperable is one of the core tenets of LangGraph, and we are committed to having first class support for MCP — enabling agent and tool interoperability.*” – Harrison Chase, CEO of LangChain

“*For agents to automate meaningful pieces of knowledge work, they need to have high-quality tools to ingest, synthesize, and take actions over enterprise data. We believe that MCP is very important to this vision of agentic knowledge management and interoperability in the enterprise, so we’re delighted to see AWS collaborate with the community to develop an open, interoperable standard that will benefit the entire AI ecosystem.*” – Jerry Liu, CEO of LlamaIndex

“*Writer is excited to build on our growing collaboration with AWS and play a meaningful role in the development of MCP for use in the enterprise. As a leader in enterprise generative AI, we’ve developed a deep understanding of the high standards needed to deliver enterprise-grade agents to the Fortune 500. With increased focus on security and reliability, we believe open source protocols like MCP can become vital for facilitating agent interoperability for our customers.*” – Waseem AlShikh, CTO and Co-founder, Writer

“*Broadcom’s Tanzu Division is dedicated to providing Java developers with powerful, easy-to-use tools for building intelligent applications. Our Spring AI team recognized the promise of the Model Context Protocol (MCP) immediately, shipping support just 16 days after the initial release and donating our implementation as the official Java SDK. We believe MCP has the potential to become foundational for intelligent, collaborative multi-agent systems—applications where autonomous agents communicate and coordinate to solve user problems. We’re excited to collaborate with AWS, Anthropic, and the broader community as MCP evolves to meet the diverse needs of Java and Spring developers.*” -Ryan Morgan, Senior Director, Tanzu Division, Broadcom

## Getting Started with Inter-Agent Communication on MCP

If you’re new to MCP, start by exploring the [official MCP documentation](https://modelcontextprotocol.io/introduction) to understand the core concepts and capabilities. You can also join the [community discussion on GitHub](https://github.com/orgs/modelcontextprotocol/discussions) where developers share implementation patterns, ask questions, and collaborate on protocol enhancements. The community is active and supportive, with both newcomers and experts contributing to ongoing development. To start building inter-agent applications using MCP, follow the getting started guides for setting up MCP [clients](https://modelcontextprotocol.io/quickstart/client) and [servers](https://modelcontextprotocol.io/quickstart/server). You can also follow the [AWS MCP getting started guide](https://community.aws/content/2v8AETAkyvPp9RVKC4YChncaEbs/running-mcp-based-agents-clients-servers-on-aws) and [server deployment guide](https://aws.amazon.com/solutions/guidance/deploying-model-context-protocol-servers-on-aws/) to see how to quickly setup your MCP applications on AWS. [Here](https://github.com/aws-samples/Sample-Model-Context-Protocol-Demos/tree/main/modules/spring-ai-mcp-inter-agent-ecs) is a link to the MCP inter-agent code sample from this blog.

*Editor’s Note: Broadcom added a quote to this post after publication.*

![Nick Aldridge](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/05/19/nick-profile-2.jpg)

### Nick Aldridge

Nick Aldridge is a Principal Engineer at AWS. Over the last 6 years, Nick has worked on multiple AI/ML initiatives including Amazon Lex and Amazon Bedrock. Most recently, he led the team that launched Amazon Bedrock Knowledge Bases. Today he works on generative AI and AI infrastructure with a focus on inter-agent collaboration and function calling. Prior to AWS, Nick earned his MS at the University of Chicago.

![Marc Brooker](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2019/09/19/marc-brooker.png)

### Marc Brooker

Marc Brooker is a VP and Distinguished Engineer at AWS. During his 16 years at AWS, Marc has worked on EC2, EBS, Lambda, and most recently lead the team that launched Aurora DSQL. He is currently focused on infrastructure for agentic AI, and the availability and security of our large-scale systems. Before AWS, Marc completed his PhD at the University of Cape Town.

![Swami Sivasubramanian](https://d2908q01vomqb2.cloudfront.net/cb4e5208b4cd87268b208e49452ed6e89a68e0b8/2024/06/13/Screenshot-2024-06-13-at-12.17.14 PM.png)

### Swami Sivasubramanian

Swami Sivasubramanian is Vice President for Agentic AI at Amazon Web Services (AWS). At AWS, Swami has led the development and growth of leading AI services like Amazon DynamoDB, Amazon SageMaker, Amazon Bedrock, and Amazon Q. His team’s mission is to provide the scale, flexibility, and value that customers and partners require to innovate using agentic AI with confidence and build agents that are not only powerful and efficient, but also trustworthy and responsible. Swami also served from May 2022 through May 2025 as a member of the National Artificial Intelligence Advisory Committee, which was tasked with advising the President of the United States and the National AI Initiative Office on topics related to the National AI Initiative.

Loading comments…

### Resources

* [Open Source at AWS](https://aws.amazon.com/opensource?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=opensource-resources)
* [Projects on GitHub](https://aws.github.io/)

---

### Follow

* [AWS Open Source Twitter](https://twitter.com/awsopen)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Open Source RSS Feed](https://aws.amazon.com/blogs/opensource/feed?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=opensource-follow)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=opensource-social)

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