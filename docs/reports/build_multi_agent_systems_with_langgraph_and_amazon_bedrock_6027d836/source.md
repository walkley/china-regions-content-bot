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

# Build multi-agent systems with LangGraph and Amazon Bedrock

by Jagdeep Singh Soni, Ajeet Tewari, and Rupinder Grewal on 14 APR 2025 in [Advanced (300)](https://aws.amazon.com/blogs/machine-learning/category/learning-levels/advanced-300/ "View all posts in Advanced (300)"), [Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Generative AI](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Technical How-to](https://aws.amazon.com/blogs/machine-learning/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/machine-learning/build-multi-agent-systems-with-langgraph-and-amazon-bedrock/)  [Comments](https://aws.amazon.com/blogs/machine-learning/build-multi-agent-systems-with-langgraph-and-amazon-bedrock/#Comments)  Share

Large language models (LLMs) have raised the bar for human-computer interaction where the expectation from users is that they can communicate with their applications through natural language. Beyond simple language understanding, real-world applications require managing complex workflows, connecting to external data, and coordinating multiple AI capabilities. Imagine scheduling a doctor’s appointment where an AI agent checks your calendar, accesses your provider’s system, verifies insurance, and confirms everything in one go—no more app-switching or hold times. In these real-world scenarios, agents can be a game changer, delivering more customized generative AI applications.

LLM agents serve as decision-making systems for application control flow. However, these systems face several operational challenges during scaling and development. The primary issues include tool selection inefficiency, where agents with access to numerous tools struggle with optimal tool selection and sequencing, context management limitations that prevent single agents from effectively managing increasingly complex contextual information, and specialization requirements as complex applications demand diverse expertise areas such as planning, research, and analysis. The solution lies in implementing a multi-agent architecture, which involves decomposing the main system into smaller, specialized agents that operate independently. Implementation options range from basic prompt-LLM combinations to sophisticated [ReAct](https://arxiv.org/abs/2210.03629) (Reasoning and Acting) agents, allowing for more efficient task distribution and specialized handling of different application components. This modular approach enhances system manageability and allows for better scaling of LLM-based applications while maintaining functional efficiency through specialized components.

This post demonstrates how to integrate open-source multi-agent framework, [LangGraph](https://www.langchain.com/langgraph), with [Amazon Bedrock](https://aws.amazon.com/bedrock/). It explains how to use LangGraph and Amazon Bedrock to build powerful, interactive multi-agent applications that use graph-based orchestration.

AWS has introduced a [multi-agent collaboration](https://aws.amazon.com/blogs/aws/introducing-multi-agent-collaboration-capability-for-amazon-bedrock/) capability for [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/), enabling developers to build, deploy, and manage multiple AI agents working together on complex tasks. This feature allows for the creation of specialized agents that handle different aspects of a process, coordinated by a supervisor agent that breaks down requests, delegates tasks, and consolidates outputs. This approach improves task success rates, accuracy, and productivity, especially for complex, multi-step tasks.

## Challenges with multi-agent systems

In a single-agent system, planning involves the LLM agent breaking down tasks into a sequence of small tasks, whereas a multi-agent system must have workflow management involving task distribution across multiple agents. Unlike single-agent environments, multi-agent systems require a coordination mechanism where each agent must maintain alignment with others while contributing to the overall objective. This introduces unique challenges in managing inter-agent dependencies, resource allocation, and synchronization, necessitating robust frameworks that maintain system-wide consistency while optimizing performance.

Memory management in AI systems differs between single-agent and multi-agent architectures. Single-agent systems use a three-tier structure: short-term conversational memory, long-term historical storage, and external data sources like Retrieval Augmented Generation (RAG). Multi-agent systems require more advanced frameworks to manage contextual data, track interactions, and synchronize historical records across agents. These systems must handle real-time interactions, context synchronization, and efficient data retrieval, necessitating careful design of memory hierarchies, access patterns, and inter-agent sharing.

Agent frameworks are essential for multi-agent systems because they provide the infrastructure for coordinating autonomous agents, managing communication and resources, and orchestrating workflows. Agent frameworks alleviate the need to build these complex components from scratch.

[LangGraph](https://www.langchain.com/langgraph), part of [LangChain](https://www.langchain.com/), orchestrates agentic workflows through a graph-based architecture that handles complex processes and maintains context across agent interactions. It uses supervisory control patterns and memory systems for coordination.

[LangGraph Studio](https://studio.langchain.com/) enhances development with graph visualization, execution monitoring, and runtime debugging capabilities. The integration of LangGraph with Amazon Bedrock empowers you to take advantage of the strengths of multiple agents seamlessly, fostering a collaborative environment that enhances the efficiency and effectiveness of LLM-based systems.

## Understanding LangGraph and LangGraph Studio

LangGraph implements state machines and directed graphs for multi-agent orchestration. The framework provides fine-grained control over both the flow and state of your agent applications. LangGraph models agent workflows as graphs. You define the behavior of your agents using three key components:

* **State** – A shared data structure that represents the current snapshot of your application.
* **Nodes** – Python functions that encode the logic of your agents.
* **Edges** – Python functions that determine which Node to execute next based on the current state. They can be conditional branches or fixed transitions.

LangGraph implements a central persistence layer, enabling features that are common to most agent architectures, including:

* **Memory** – LangGraph persists arbitrary aspects of your application’s state, supporting memory of conversations and other updates within and across user interactions.
* **Human-in-the-loop** – Because state is checkpointed, execution can be interrupted and resumed, allowing for decisions, validation, and corrections at key stages through human input.

LangGraph Studio is an integrated development environment (IDE) specifically designed for AI agent development. It provides developers with powerful tools for visualization, real-time interaction, and debugging capabilities. The key features of LangGraph Studio are:

* **Visual agent graphs** – The IDE’s visualization tools allow developers to represent agent flows as intuitive graphic wheels, making it straightforward to understand and modify complex system architectures.
* **Real-time debugging** – The ability to interact with agents in real time and modify responses mid-execution creates a more dynamic development experience.
* **Stateful architecture** – Support for stateful and adaptive agents within a graph-based architecture enables more sophisticated behaviors and interactions.

The following screenshot shows the nodes, edges, and state of a typical LangGraph agent workflow as viewed in LangGraph Studio.

[![LangGraph agent workflow as viewed in LangGraph Studio](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/02/blog-18269-Pic1.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/02/blog-18269-Pic1.png)

*Figure 1: LangGraph Studio UI*

In the preceding example, the state begins with `__start__` and ends with `__end__`. The nodes for invoking the model and tools are defined by you and the edges tell you which paths can be followed by the workflow.

LangGraph Studio is available as a [desktop application](https://studio.langchain.com/) for MacOS users. Alternatively, you can [run a local in-memory development server](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/) that can be used to connect a local LangGraph application with a web version of the studio.

## Solution overview

This example demonstrates the supervisor agentic pattern, where a supervisor agent coordinates multiple specialized agents. Each agent maintains its own scratchpad while the supervisor orchestrates communication and delegates tasks based on agent capabilities. This distributed approach improves efficiency by allowing agents to focus on specific tasks while enabling parallel processing and system scalability.

Let’s walk through an example with the following user query: “Suggest a travel destination and search flight and hotel for me. I want to travel on 15-March-2025 for 5 days.” The workflow consists of the following steps:

1. The Supervisor Agent receives the initial query and breaks it down into sequential tasks:
   1. Destination recommendation required.
   2. Flight search needed for March 15, 2025.
   3. Hotel booking required for 5 days.
2. The Destination Agent begins its work by accessing the user’s stored profile. It searches its historical database, analyzing patterns from similar user profiles to recommend the destination. Then it passes the destination back to the Supervisor Agent.
3. The Supervisor Agent forwards the chosen destination to the Flight Agent, which searches available flights for the given date.
4. The Supervisor Agent activates the Hotel Agent, which searches for hotels in the destination city.
5. The Supervisor Agent compiles the recommendations into a comprehensive travel plan, presenting the user with a complete itinerary including destination rationale, flight options, and hotel suggestions.

The following figure shows a multi-agent workflow of how these agents connect to each other and which tools are involved with each agent.

[![multi-agent workflow ](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/02/blog-18269-Pic2.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/02/blog-18269-Pic2.png)*Figure 2: Multi-agent workflow*

## Prerequisites

You will need the following prerequisites before you can proceed with this solution. For this post, we use the `us-west-2` AWS Region. For details on available Regions, see [Amazon Bedrock endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html).

* A valid AWS account.
* An [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) role in the account that has sufficient permissions to create the necessary resources.
* Access to Anthropic’s Claude 3 Sonnet and Claude 3.5 Sonnet in Amazon Bedrock. For instructions, see [Access Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).
* A LangGraph application up and running locally. For instructions, see [Quickstart: Launch Local LangGraph Server](https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/#quickstart-launch-local-langgraph-server).

## Core components

Each agent is structured with two primary components:

* [graph.py](https://github.com/aws-samples/aim323_build_agents_with_bedrock_oss/blob/main/bedrock-multi-agent-langgraph-studio/src/flight_agent/graph.py) – This script defines the agent’s workflow and decision-making logic. It implements the LangGraph state machine for managing agent behavior and configures the communication flow between different components. For example:
  + The Flight Agent’s graph manages the flow between chat and tool operations.
  + The Hotel Agent’s graph handles conditional routing between search, booking, and modification operations.
  + The Supervisor Agent’s graph orchestrates the overall multi-agent workflow.
* [tools.py](https://github.com/aws-samples/aim323_build_agents_with_bedrock_oss/blob/main/bedrock-multi-agent-langgraph-studio/src/hotel_agent/tools.py) – This script contains the concrete implementations of agent capabilities. It implements the business logic for each operation and handles data access and manipulation. It provides specific functionalities like:
  + Flight tools: `search_flights`, `book_flights`, `change_flight_booking`, `cancel_flight_booking`.
  + Hotel tools: `suggest_hotels`, `book_hotels`, `change_hotel_booking`, `cancel_hotel_booking`.

This separation between graph (workflow) and tools (implementation) allows for a clean architecture where the decision-making process is separate from the actual execution of tasks. The agents communicate through a state-based graph system implemented using LangGraph, where the Supervisor Agent directs the flow of information and tasks between the specialized agents.

To set up Amazon Bedrock with LangGraph, refer to the following [GitHub repo](https://github.com/aws-samples/aim323_build_agents_with_bedrock_oss/blob/main/bedrock-multi-agent-langgraph-studio/README.md). The high-level steps are as follows:

1. Install the required packages:

```
pip install boto3 langchain-aws
```

These packages are essential for AWS Bedrock integration:

* `boto`: AWS SDK for Python, handles AWS service communication
* `langchain-aws`: Provides LangChain integrations for AWS services

2. Import the modules:

```
from langchain_aws import ChatBedrockConverse
from langchain_aws import ChatBedrock
```

3. Create an LLM object:

```
bedrock_client = boto3.client("bedrock-runtime", region_name="<region_name>")
llm = ChatBedrockConverse(
        model="anthropic.claude-3-haiku-20240307-v1:0",
        temperature=0,
        max_tokens=None,
        client=bedrock_client,
        # other params...
    )
```

## LangGraph Studio configuration

This project uses a [langgraph.json](https://github.com/aws-samples/aim323_build_agents_with_bedrock_oss/blob/main/bedrock-multi-agent-langgraph-studio/langgraph.json) configuration file to define the application structure and dependencies. This file is essential for LangGraph Studio to understand how to run and visualize your agent graphs.

```
{
"dependencies": [
"boto3>=1.35.87",
"langchain-aws>=0.2.10",
"."
],
"graphs": {
"supervisor": "./src/supervisor_agent/graph.py:graph",
"flight": "./src/flight_agent/graph.py:graph",
"hotel": "./src/hotel_agent/graph.py:graph"
},
"env": "./.env"
}
```

LangGraph Studio uses this file to build and visualize the agent workflows, allowing you to monitor and debug the multi-agent interactions in real time.

## Testing and debugging

You’re now ready to test the multi-agent travel assistant. You can start the graph using the `langgraph dev` command. It will start the LangGraph API server in development mode with hot reloading and debugging capabilities. As shown in the following screenshot, the interface provides a straightforward way to select which graph you want to test through the dropdown menu at the top left. The **Manage Configuration** button at the bottom lets you set up specific testing parameters before you begin. This development environment provides everything you need to thoroughly test and debug your multi-agent system with real-time feedback and monitoring capabilities.

[![Testing multi-agent travel assistant](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/02/blog-18269-Pic3.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/02/blog-18269-Pic3.png)*Figure 3: LangGraph studio with Destination Agent recommendation*

LangGraph Studio offers flexible configuration management through its intuitive interface. As shown in the following screenshot, you can create and manage multiple configuration versions (v1, v2, v3) for your graph execution. For example, in this scenario, we want to use `user_id` to fetch historic use information. This versioning system makes it simple to track and switch between different test configurations while debugging your multi-agent system.

[![Create and manage multiple configuration versions (v1, v2, v3) for your graph execution](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/02/blog-18269-Pic4.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/02/blog-18269-Pic4.png)*Figure 4: Runnable configuration details*

In the preceding example, we set up the `user_id` that tools can use to retrieve history or other details.

Let’s test the Planner Agent. This agent has the `compare_and_recommend_destination` tool, which can check past travel data and recommend travel destinations based on the user profile. We use `user_id` in the configuration so that can it be used by the tool.

LangGraph has concept of checkpoint memory that is managed using a thread. The following screenshot shows that you can quickly manage threads in LangGraph Studio.

[![Manage threads in LangGraph Studio](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/02/blog-18269-Pic5.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/02/blog-18269-Pic5.png)*Figure 5: View graph state in the thread*

In this example, `destination_agent` is using a tool; you can also check the tool’s output. Similarly, you can test `flight_agent` and `hotel_agent` to verify each agent.

When all the agents are working well, you’re ready to test the full workflow. You can evaluate the state a verify input and output of each agent.

The following screenshot shows the full view of the Supervisor Agent with its sub-agents.

[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/03/ml-18369-image6.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/02/blog-18269-Pic6.png)*Figure 6: Supervisor Agent with complete workflow*

## Considerations

Multi-agent architectures must consider agent coordination, state management, communication, output consolidation, and guardrails, maintaining processing context, error handling, and orchestration. Graph-based architectures offer significant advantages over linear pipelines, enabling complex workflows with nonlinear communication patterns and clearer system visualization. These structures allow for dynamic pathways and adaptive communication, ideal for large-scale deployments with simultaneous agent interactions. They excel in parallel processing and resource allocation but require sophisticated setup and might demand higher computational resources. Implementing these systems necessitates careful planning of system topology, robust monitoring, and well-designed fallback mechanisms for failed interactions.

When implementing multi-agent architectures in your organization, it’s crucial to align with your company’s established generative AI operations and governance frameworks. Prior to deployment, verify alignment with your organization’s AI safety protocols, data handling policies, and model deployment guidelines. Although this architectural pattern offers significant benefits, its implementation should be tailored to fit within your organization’s specific AI governance structure and risk management frameworks.

## Clean up

Delete any IAM roles and policies created specifically for this post. Delete the local copy of this post’s code. If you no longer need access to an Amazon Bedrock FM, you can remove access from it. For instructions, see [Add or remove access to Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.html)

## Conclusion

The integration of LangGraph with Amazon Bedrock significantly advances multi-agent system development by providing a robust framework for sophisticated AI applications. This combination uses LangGraph’s orchestration capabilities and FMs in Amazon Bedrock to create scalable, efficient systems. It addresses challenges in multi-agent architectures through state management, agent coordination, and workflow orchestration, offering features like memory management, error handling, and human-in-the-loop capabilities. LangGraph Studio’s visualization and debugging tools enable efficient design and maintenance of complex agent interactions. This integration offers a powerful foundation for next-generation multi-agent systems, providing effective workflow handling, context maintenance, reliable results, and optimal resource utilization.

For the example code and demonstration discussed in this post, refer to the accompanying [GitHub repository](https://github.com/aws-samples/aim323_build_agents_with_bedrock_oss/tree/main/bedrock-multi-agent-langgraph-studio). You can also refer to the following [GitHub repo for Amazon Bedrock multi-agent collaboration code samples](https://github.com/awslabs/amazon-bedrock-agent-samples).

---

### About the Authors

**[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/09/Jagdeep_profile_pic.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2023/11/21/jagdsoni.jpeg)Jagdeep Singh Soni** is a Senior Partner Solutions Architect at AWS based in the Netherlands. He uses his passion for generative AI to help customers and partners build generative AI applications using AWS services. Jagdeep has 15 years of experience in innovation, experience engineering, digital transformation, cloud architecture, and ML applications.

**[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/05/23/ajeet-100.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/05/23/ajeet-100.jpg)Ajeet Tewari** is a Senior Solutions Architect for Amazon Web Services. He works with enterprise customers to help them navigate their journey to AWS. His specialties include architecting and implementing scalable OLTP systems and leading strategic AWS initiatives.

**[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/03/05/ML-16194-Rupinder-Grewal.jpeg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/03/05/ML-16194-Rupinder-Grewal.jpeg)Rupinder Grewal** is a Senior AI/ML Specialist Solutions Architect with AWS. He currently focuses on serving of models and MLOps on Amazon SageMaker. Prior to this role, he worked as a Machine Learning Engineer building and hosting models. Outside of work, he enjoys playing tennis and biking on mountain trails.

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