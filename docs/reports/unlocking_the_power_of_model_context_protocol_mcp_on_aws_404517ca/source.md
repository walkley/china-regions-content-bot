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

# Unlocking the power of Model Context Protocol (MCP) on AWS

by Aditya Addepalli, Elie Schoppik, Jawhny Cooke, Kenton Blacutt, Mani Khanuja, and Nicolai van der Smagt on 03 JUN 2025 in [Foundation models](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/generative-ai/foundation-models/ "View all posts in Foundation models"), [Generative AI](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Intermediate (200)](https://aws.amazon.com/blogs/machine-learning/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [Technical How-to](https://aws.amazon.com/blogs/machine-learning/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/machine-learning/unlocking-the-power-of-model-context-protocol-mcp-on-aws/)  [Comments](https://aws.amazon.com/blogs/machine-learning/unlocking-the-power-of-model-context-protocol-mcp-on-aws/#Comments)  Share

We’ve witnessed remarkable advances in model capabilities as [generative AI](https://aws.amazon.com/generative-ai/) companies have invested in developing their offerings. Language models such as [Anthropic’s Claude Opus 4 & Sonnet 4](https://aws.amazon.com/bedrock/claude/) and [Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/) on [Amazon Bedrock](https://aws.amazon.com/bedrock/) can reason, write, and generate responses with increasing sophistication. But even as these models grow more powerful, they can only work with the information available to them.

No matter how impressive a model might be, it’s confined to the data it was trained on or what’s manually provided in its context window. It’s like having the world’s best analyst locked in a room with incomplete files—brilliant, but isolated from your organization’s most current and relevant information.

This isolation creates three critical challenges for enterprises using [generative AI](https://aws.amazon.com/generative-ai/):

1. **Information silos** trap valuable data behind custom APIs and proprietary interfaces
2. **Integration complexity** requires building and maintaining bespoke connectors and glue code for every data source or tool provided to the language model for every data source
3. **Scalability bottlenecks** appear as organizations attempt to connect more models to more systems and tools

Sound familiar? If you’re an AI-focused developer, technical decision-maker, or solution architect working with [Amazon Web Services](https://aws.amazon.com/) (AWS) and language models, you’ve likely encountered these obstacles firsthand. Let’s explore how the [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) offers a path forward.

## What is the MCP?

The MCP is an open standard that creates a universal language for AI systems to communicate with external data sources, tools, and services. Conceptually, MCP functions as a universal translator, enabling seamless dialogue between language models and the diverse systems where your valuable information resides.

Developed by Anthropic and released as an open source project, MCP addresses a fundamental challenge: how to provide AI models with consistent, secure access to the information they need, when they need it, regardless of where that information lives.

[![MCP deployment diagram showing client interaction with local and internet-based MCP servers](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-mcp-architecture.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-mcp-architecture.png)

At its core, MCP implements a client-server architecture:

* **MCP clients** are AI applications like Anthropic’s Claude Desktop or custom solutions built on Amazon Bedrock that need access to external data
* **MCP servers** provide standardized access to specific data sources, whether that’s a GitHub repository, Slack workspace, or AWS service
* **Communication flow** between clients and servers follows a well-defined protocol that can run locally or remotely

This architecture supports three essential primitives that form the foundation of MCP:

1. **Tools** – Functions that models can call to retrieve information or perform actions
2. **Resources** – Data that can be included in the model’s context such as database records, images, or file contents
3. **Prompts** – Templates that guide how models interact with specific tools or resources

What makes MCP especially powerful is its ability to work across both local and remote implementations. You can run MCP servers directly on your development machine for testing or deploy them as distributed services across your AWS infrastructure for enterprise-scale applications.

## Solving the M×N integration problem

Before diving deeper into the AWS specific implementation details, it’s worth understanding the fundamental integration challenge MCP solves.

Imagine you’re building AI applications that need to access multiple data sources in your organization. Without a standardized protocol, you face what we call the “M×N problem”: for M different AI applications connecting to N different data sources, you need to build and maintain M×N custom integrations.

This creates an integration matrix that quickly becomes unmanageable as your organization adds more AI applications and data sources. Each new system requires multiple custom integrations, with development teams duplicating efforts across projects. MCP transforms this M×N problem into a simpler M+N equation: with MCP, you build M clients and N servers, requiring only M+N implementations. These solutions to the MCP problem are shown in the following diagram.

[![Visualization showing how MCP reduces integration complexity from 9 to 6 implementations](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-m-x-n.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-m-x-n.png)

This approach draws inspiration from other successful protocols that solved similar challenges:

* **APIs** standardized how web applications interact with the backend
* **Language Server Protocol (LSP)** standardizes how [integrated development environments](https://aws.amazon.com/what-is/ide/) (IDEs) interact with language-specific tools for coding

In the same way that these protocols revolutionized their domains, MCP is poised to transform how AI applications interact with the diverse landscape of data sources in modern enterprises.

## Why MCP matters for AWS users

For AWS customers, MCP represents a particularly compelling opportunity. AWS offers hundreds of services, each with its own APIs and data formats. By adopting MCP as a standardized protocol for AI interactions, you can:

1. **Streamline integration** between Amazon Bedrock language models and AWS data services
2. **Use existing AWS security mechanisms** such as [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) for consistent access control
3. **Build composable, scalable AI solutions** that align with AWS architectural best practices

## MCP and the AWS service landscape

What makes MCP particularly powerful in the AWS context is how it can interface with the broader AWS service landscape. Imagine AI applications that can seamlessly access information from:

* **[Amazon Simple Storage](https://aws.amazon.com/s3/) (Amazon S3) buckets** containing documents, images, and unstructured data
* **[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) tables** storing structured business information
* **[Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) databases** with historical transaction records
* **[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) logs** for operational intelligence
* **[Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/)** for semantic search capabilities

MCP servers act as consistent interfaces to these diverse data sources, providing language models with a unified access pattern regardless of the underlying AWS service architecture. This alleviates the need for custom integration code for each service and enables AI systems to work with your AWS resources in a way that respects your existing security boundaries and access controls.

In the remaining sections of this post, we explore how MCP works with AWS services, examine specific implementation examples, and provide guidance for technical decision-makers considering adopt MCP in their organizations.

## How MCP works with AWS services, particularly Amazon Bedrock

Now that we’ve shown the fundamental value proposition of MCP, we dive into how it integrates with AWS services, with a special focus on Amazon Bedrock. This integration creates a powerful foundation for building context-aware AI applications that can securely access your organization’s data and tools.

### Amazon Bedrock and language models

Amazon Bedrock represents the strategic commitment by AWS to make [foundation models](https://aws.amazon.com/what-is/foundation-models/) (FMs) accessible, secure, and enterprise-ready. It’s a fully managed service that provides a unified API across multiple leading language models, including:

* Anthropic’s Claude
* Meta’s Llama
* Amazon Titan and Amazon Nova

What makes Amazon Bedrock particularly compelling for enterprise deployments is its integration with the broader AWS landscape. You can run FMs with the same security, compliance, and operational tools you already use for your AWS workloads. This includes IAM for access control and CloudWatch for monitoring.

At the heart of the versatility of Amazon Bedrock is the [Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html)—the interface that enables multiturn conversations with language models. The Converse API includes built-in support for what AWS calls “tool use,” allowing models to:

1. Recognize when they need information outside their training data
2. Request that information from external systems using well-defined function calls
3. Incorporate the returned data into their responses

This tool use capability in the Amazon Bedrock Converse API dovetails perfectly with MCP’s design, creating a natural integration point.

### MCP and Amazon Bedrock integration architecture

Integrating MCP with Amazon Bedrock involves creating a bridge between the model’s ability to request information (through the Converse API) and MCP’s standardized protocol for accessing external systems.

### Integration flow walkthrough

To help you understand how MCP and Amazon Bedrock work together in practice, we walk through a typical interaction flow, step-by-step:

1. The user initiates a query through your application interface:

`"What were our Q1 sales figures for the Northwest region?"`

2. Your application forwards the query to Amazon Bedrock through the Converse API:

```
   # Initialize the Bedrock runtime client with your AWS credentials
   bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

   # Define the query from the user
   user_query = "What were our Q1 sales figures for the Northwest region?"

   # available_tools contains tool definitions that match MCP server capabilities
   # These will be exposed to the model through the Converse API

   # Call the Converse API with the user's query and available tools
   response = bedrock.converse(
       modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",  # Specify which language model to use
       messages=[{"role": "user", "content": [{"text": user_query}]}],  # Format the user's message
       toolConfig={"tools": available_tools}  # Pass the tool definitions to the model
   )
```

3. Amazon Bedrock processes the query and determines that it needs financial data that isn’t in its training data
4. Amazon Bedrock returns a `toolUse` message, requesting access to a specific tool:

```
   {
     "role": "assistant",  // Indicates this message is from the model
     "content": [{
       "toolUse": {  // The model is requesting to use a tool
         "toolUseId": "tu_01234567",  // Unique identifier for this tool use request
         "name": "query_sales_data",  // Name of the tool the model wants to use
         "input": {  // Parameters for the tool call
           "quarter": "Q1",  // The model extracted this parameter from the user query
           "region": "Northwest"  // Another parameter extracted from the user query
         }
       }
     }]
   }
```

5. Your MCP client application receives this `toolUse` message and translates it into an MCP protocol

   tool call
6. The MCP client routes the request to the appropriate MCP server (in this case, a server connected to your

   financial database)
7. The MCP server executes the tool, retrieving the requested data from your systems:

```
   # Call the tool through the MCP protocol
   # session is the MCP client session established earlier
   result = await session.call_tool(
       "query_sales_data",  # The tool name from the toolUse message
       {
           "quarter": "Q1",  # Pass through the parameters from the toolUse message
           "region": "Northwest"
       }
   )
   # The MCP server handles authentication, data access, and result formatting
   # This abstracts away the complexity of accessing different data sources
```

8. The tool results are returned through the MCP protocol to your client application
9. Your application sends the results back to Amazon Bedrock as a `toolResult` message:

```
   {
     "role": "user",  // This is sent as if from the user, but contains tool results
     "content": [{
       "toolResult": {  // Indicates this is a result from a tool
         "toolUseId": "tu_01234567",  // Must match the ID from the original toolUse
         "content": [{
           "json": {  // Results are formatted as JSON
             "total_sales": 12450000,  // Numerical data accessible to the model
             "growth": 0.12,  // Percentage growth for analysis
             "top_products": ["Product A", "Product B", "Product C"]  // List data
           }
         }]
       }
     }]
   }
```

10. Amazon Bedrock generates a final response incorporating the tool results:

```
“Based on the data I've retrieved, our Q1 sales figures for the Northwest region were $12.45 million,
representing a 12% growth compared to the previous quarter.
The top-performing products were Product A, Product B, and Product C.”
```

11. Your application returns the final response to the user

This entire process, illustrated in the following diagram, happens in seconds, giving users the impression of a seamless conversation with an AI that has direct access to their organization’s data. Behind the scenes, MCP is handling the complex work of securely routing requests to the right tools and data sources.

[![Streamlined sequence diagram showing core MCP message flow from user query to final response](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-simplified-flow-diagram.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-simplified-flow-diagram.png)

In the next section, we explore a practical implementation example that shows how to connect an MCP server to Amazon Bedrock Knowledge Bases, providing a blueprint for your own implementations.

## Practical implementation example: Amazon Bedrock Knowledge Bases integration

As you might recall from our earlier discussion of strategic use cases, enterprise knowledge bases represent one of the most valuable applications of MCP on AWS. Now, we explore a concrete implementation of MCP that connects language models to Amazon Bedrock Knowledge Bases. The code for the MCP server can be found in the [AWS Labs MCP code repository](https://github.com/awslabs/mcp/blob/main/src/bedrock-kb-retrieval-mcp-server/awslabs/bedrock_kb_retrieval_mcp_server/server.py) and for the client in the same [AWS Labs MCP samples directory](https://github.com/awslabs/mcp/tree/main/samples/mcp-integration-with-kb) on GitHub. This example brings to life the “universal translator” concept we introduced earlier, demonstrating how MCP can transform the way AI systems interact with enterprise knowledge repositories.

### Understanding the challenge

Enterprise knowledge bases contain vast repositories of information—from documentation and policies to technical guides and product specifications. Traditional search approaches are often inadequate when users ask natural language questions, failing to understand context or identify the most relevant content.

Amazon Bedrock Knowledge Bases provide vector search capabilities that improve upon traditional keyword search, but even this approach has limitations:

1. **Manual filter configuration** requires predefined knowledge of metadata structures
2. **Query-result mismatch** occurs when users don’t use the exact terminology in the knowledge base
3. **Relevance challenges** arise when similar documents compete for attention
4. **Context switching** between searching and reasoning disrupts user experience

The MCP server we explore addresses these challenges by creating an intelligent layer between language models and knowledge bases.

### Architecture overview

At a high level, our MCP server for Amazon Bedrock Knowledge Bases follows a clean, well-organized architecture that builds upon the client-server pattern we outlined previously. The server exposes two key interfaces to language models:

1. A knowledge bases resource that provides discovery capabilities for available knowledge bases
2. A query tool that enables dynamic searching across these knowledge bases

[![Detailed MCP Bedrock architecture with intelligent query processing workflow and AWS service connections](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-bedrock-kb-architecture.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-bedrock-kb-architecture.png)

Remember the M×N integration problem we discussed earlier? This implementation provides a tangible example of how MCP solves it – creating a standardized interface between a large language model and your Amazon Bedrock Knowledge Base repositories.

#### Knowledge base discovery resource

The server begins with a resource that enables language models to discover available knowledge bases:

```
@mcp.resource(uri='resource://knowledgebases', name='KnowledgeBases', mime_type='application/json')
async def knowledgebases_resource() -> str:
    """List all available Amazon Bedrock Knowledge Bases and their data sources.

    This resource returns a mapping of knowledge base IDs to their details, including:
    - name: The human-readable name of the knowledge base
    - data_sources: A list of data sources within the knowledge base, each with:
      - id: The unique identifier of the data source
      - name: The human-readable name of the data source

    ## Example response structure:
    ```json
    {
        "kb-12345": {
            "name": "Customer Support KB",
            "data_sources": [
                {"id": "ds-abc123", "name": "Technical Documentation"},
                {"id": "ds-def456", "name": "FAQs"}
            ]
        },
        "kb-67890": {
            "name": "Product Information KB",
            "data_sources": [
                {"id": "ds-ghi789", "name": "Product Specifications"}
            ]
        }
    }
    ```

    ## How to use this information:
    1. Extract the knowledge base IDs (like "kb-12345") for use with the QueryKnowledgeBases tool
    2. Note the data source IDs if you want to filter queries to specific data sources
    3. Use the names to determine which knowledge base and data source(s) are most relevant to the user's query
    """
    return json.dumps(await discover_knowledge_bases(kb_agent_mgmt_client, kb_inclusion_tag_key))
```

This resource serves as both documentation and a discovery mechanism that language models can use to identify available knowledge bases before querying them.

#### Querying knowledge bases with the MCP tool

The core functionality of this MCP server resides in its `QueryKnowledgeBases` tool:

```
@mcp.tool(name='QueryKnowledgeBases')
async def query_knowledge_bases_tool(
    query: str = Field(
        ..., description='A natural language query to search the knowledge base with'
    ),
    knowledge_base_id: str = Field(
        ...,
        description='The knowledge base ID to query. It must be a valid ID from the resource://knowledgebases MCP resource',
    ),
    number_of_results: int = Field(
        10,
        description='The number of results to return. Use smaller values for focused results and larger values for broader coverage.',
    ),
    reranking: bool = Field(
        kb_reranking_enabled,
        description='Whether to rerank the results. Useful for improving relevance and sorting. Can be globally configured with BEDROCK_KB_RERANKING_ENABLED environment variable.',
    ),
    reranking_model_name: Literal['COHERE', 'AMAZON'] = Field(
        'AMAZON',
        description="The name of the reranking model to use. Options: 'COHERE', 'AMAZON'",
    ),
    data_source_ids: Optional[List[str]] = Field(
        None,
        description='The data source IDs to filter the knowledge base by. It must be a list of valid data source IDs from the resource://knowledgebases MCP resource',
    ),
) -> str:
    """Query an Amazon Bedrock Knowledge Base using natural language.

    ## Usage Requirements
    - You MUST first use the `resource://knowledgebases` resource to get valid knowledge base IDs
    - You can query different knowledge bases or make multiple queries to the same knowledge base

    ## Query Tips
    - Use clear, specific natural language queries for best results
    - You can use this tool MULTIPLE TIMES with different queries to gather comprehensive information
    - Break complex questions into multiple focused queries
    - Consider querying for factual information and explanations separately
     """
## Additional Implementation details …
```

What makes this tool powerful is its flexibility in querying knowledge bases with natural language. It supports several key features:

1. **Configurable result sizes** – Adjust the number of results based on whether you need focused or comprehensive information
2. **Optional reranking** – Improve relevance using language models (such as reranking models from Amazon or Cohere)
3. **Data source filtering** – Target specific sections of the knowledge base when needed

Reranking is disabled by default in this implementation but can be quickly enabled through environment variables or direct parameter configuration.

### Enhanced relevance with reranking

A notable feature of this implementation is the ability to rerank search results using language models available through Amazon Bedrock. This capability allows the system to rescore search results based on deeper semantic understanding:

```
# Parse reranking enabled environment variable
kb_reranking_enabled_raw = os.getenv('BEDROCK_KB_RERANKING_ENABLED')
kb_reranking_enabled = False  # Default value is now False (off)
if kb_reranking_enabled_raw is not None:
    kb_reranking_enabled_raw = kb_reranking_enabled_raw.strip().lower()
    if kb_reranking_enabled_raw in ('true', '1', 'yes', 'on'):
        kb_reranking_enabled = True
```

Reranking is particularly valuable for queries where semantic similarity might not be enough to determine the

most relevant content. For example, when answering a specific question, the most relevant document isn’t necessarily

the one with the most keyword matches, but the one that directly addresses the question being asked.

### Full interaction flow

This section walks through a complete interaction flow to show how all these components work

together:

1. The user asks a question to a language model such as Anthropic’s Claude through an application:

```
   "What's our quarterly IT security audit procedure?"
```

2. The language model recognizes it needs to access the knowledge base and calls the MCP tool:

```
{
  "toolUse": {
    "name": "QueryKnowledgeBases",
    "input": {
      "query": "What's our quarterly IT security audit procedure?",
      "knowledge_base_id": "kb-12345abcde",
      "reranking": true
    }
  }
}
```

3. The MCP server processes the request by querying the knowledge base with the specified parameters
4. The MCP server returns formatted results to the language model, including content, location, and relevance scores:

```
Applied metadata filters: department=IT, document_type=Procedure, category=Security Audit, frequency=Quarterly

   Results have been reranked to improve relevance.

   Result 1 [Score: 0.92]:
   Source: S3 - s3://company-docs/procedures/it/security/quarterly-audit-procedure-v2.pdf
   Content: The IT Security Quarterly Audit Procedure outlines the steps for conducting systematic evaluations of the organization's information security controls. This document provides guidance on scope, methodology, reporting requirements, and remediation tracking...
   Metadata:
     • department: IT
     • document_type: Procedure
     • category: Security Audit
     • frequency: Quarterly
     • last_updated: 2024-11-15
```

5. The language model incorporates these results into its response to the user:

```
   Based on our IT Security Quarterly Audit Procedure, the process involves four main phases:

   1. Planning: Define scope, objectives, and schedule for the audit
   2. Execution: Conduct the technical assessments and control evaluations
   3. Reporting: Document findings, risks, and recommendations
   4. Remediation: Track and verify resolution of identified issues

   The procedure was last updated on November 15, 2024, and specifies that the Cybersecurity team leads the effort with support from IT Operations.
```

This interaction, illustrated in the following diagram, demonstrates the seamless fusion of language model capabilities with enterprise knowledge, enabled by the MCP protocol. The user doesn’t need to specify complex search parameters or know the structure of the knowledge base—the integration layer handles these details automatically.

[![End-to-end sequence diagram of IT security audit query processing through Bedrock Claude and MCP Server with metadata analysis](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-bedrock-kb-flow-chart.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-bedrock-kb-flow-chart.png)

## Looking ahead: The MCP journey continues

As we’ve explored throughout this post, the Model Context Protocol provides a powerful framework for connecting language models to your enterprise data and tools on AWS. But this is just the beginning of the journey.

The MCP landscape is rapidly evolving, with new capabilities and implementations emerging regularly. In future posts in this series, we’ll dive deeper into advanced MCP architectures and use cases, with a particular focus on remote MCP implementation.

The introduction of the new [Streamable HTTP transport layer](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) represents a significant advancement for MCP, enabling truly enterprise-scale deployments with features such as:

* Stateless server options for simplified scaling
* Session ID management for request routing
* Robust authentication and authorization mechanisms for secure access control
* Horizontal scaling across server nodes
* Enhanced resilience and fault tolerance

These capabilities will be essential as organizations move from proof-of-concept implementations to production-grade MCP deployments that serve multiple teams and use cases.

We invite you to follow this blog post series as we continue to explore how MCP and AWS services can work together to create more powerful, context-aware AI applications for your organization.

## Conclusion

As language models continue to transform how we interact with technology, the ability to connect these models to enterprise data and systems becomes increasingly critical. The Model Context Protocol (MCP) offers a standardized, secure, and scalable approach to integration.

Through MCP, AWS customers can:

* Establish a standardized protocol for AI-data connections
* Reduce development overhead and maintenance costs
* Enforce consistent security and governance policies
* Create more powerful, context-aware AI experiences

The Amazon Bedrock Knowledge Bases implementation we explored demonstrates how MCP can transform simple retrieval into intelligent discovery, adding value far beyond what either component could deliver independently.

## Getting started

Ready to begin your MCP journey on AWS? Here are some resources to help you get started:

**Learning resources:**

* [AWS Labs MCP client and server code repository](https://github.com/awslabs/mcp/tree/main)
* [Model Context Protocol documentation](https://modelcontextprotocol.io/)
* [Amazon Bedrock Developer Guide](https://docs.aws.amazon.com/bedrock/)
* [MCP servers repository](https://github.com/modelcontextprotocol/servers)

**Implementation steps:**

1. Identify a high-value use case where AI needs access to enterprise data
2. Select the appropriate MCP servers for your data sources
3. Set up a development environment with local MCP implementations
4. Integrate with Amazon Bedrock using the patterns described in this post
5. Deploy to production with appropriate security and scaling considerations

Remember that MCP offers a “start small, scale incrementally” approach. You can begin with a single server connecting to one data source, then expand your implementation as you validate the value and establish patterns for your organization.

We encourage you to try the MCP with AWS services today. Start with a simple implementation, perhaps connecting a language model to your documentation or code repositories, and experience firsthand the power of context-aware AI.

Share your experiences, challenges, and successes with the community. The open source nature of MCP means that your contributions—whether code, use cases, or feedback—can help shape the future of this important protocol.

In a world where AI capabilities are advancing rapidly, the difference between good and great implementations often comes down to context. With MCP and AWS, you have the tools to make sure your AI systems have the right context at the right time, unlocking their full potential for your organization.

*This blog post is part of a series exploring the Model Context Protocol (MCP) on AWS. In our next installment, we’ll explore the world of agentic AI, demonstrating how to build autonomous agents using the open-source [Strands Agents](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/) SDK with MCP to create intelligent systems that can reason, plan, and execute complex multi-step workflows. We’ll also explore advanced implementation patterns, remote MCP architectures, and discover additional use cases for MCP.*

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-adiadd-1.jpeg)**Aditya Addepalli** is a Delivery Consultant at AWS, where he works to lead, architect, and build applications directly with customers. With a strong passion for Applied AI, he builds bespoke solutions and contributes to the ecosystem while consistently keeping himself at the edge of technology. Outside of work, you can find him meeting new people, working out, playing video games and basketball, or feeding his curiosity through personal projects.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/elie-anthropic.jpg)**Elie Schoppik** leads live education at Anthropic as their Head of Technical Training. He has spent over a decade in technical education, working with multiple coding schools and starting one of his own. With a background in consulting, education, and software engineering, Elie brings a practical approach to teaching Software Engineering and AI. He’s shared his insights at a variety of technical conferences as well as universities including MIT, Columbia, Wharton, and UC Berkeley.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-jawcooke-1.jpeg)**Jawhny Cooke** is a Senior Anthropic Specialist Solutions Architect for Generative AI at AWS. He specializes in integrating and deploying Anthropic models on AWS infrastructure. He partners with customers and AI providers to implement production-grade generative AI solutions through Amazon Bedrock, offering expert guidance on architecture design and system implementation to maximize the potential of these advanced models.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-kblacutt-1.jpeg)**Kenton Blacutt** is an AI Consultant within the GenAI Innovation Center. He works hands-on with customers helping them solve real-world business problems with cutting edge AWS technologies, especially Amazon Q and Bedrock. In his free time, he likes to travel, experiment with new AI techniques, and run an occasional marathon.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/27/mankhanu.jpg)**Mani Khanuja** is a Principal Generative AI Specialist Solutions Architect, author of the book Applied Machine Learning and High-Performance Computing on AWS, and a member of the Board of Directors for Women in Manufacturing Education Foundation Board. She leads machine learning projects in various domains such as computer vision, natural language processing, and generative AI. She speaks at internal and external conferences such AWS re:Invent, Women in Manufacturing West, YouTube webinars, and GHC 23. In her free time, she likes to go for long runs along the beach.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/05/23/ML-18605-nsmagt-1.jpeg)**Nicolai van der Smagt** is a Senior Specialist Solutions Architect for Generative AI at AWS, focusing on third-party model integration and deployment. He collaborates with AWS’ biggest AI partners to bring their models to Amazon Bedrock, while helping customers architect and implement production-ready generative AI solutions with these models.

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