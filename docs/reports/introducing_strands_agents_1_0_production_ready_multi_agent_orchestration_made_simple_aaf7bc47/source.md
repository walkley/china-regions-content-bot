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

# Introducing Strands Agents 1.0: Production-Ready Multi-Agent Orchestration Made Simple

by Ryan Coleman and Belle Guttman on 15 JUL 2025 in [Amazon Machine Learning](https://aws.amazon.com/blogs/opensource/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Announcements](https://aws.amazon.com/blogs/opensource/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/opensource/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Open Source](https://aws.amazon.com/blogs/opensource/category/open-source/ "View all posts in Open Source") [Permalink](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-1-0-production-ready-multi-agent-orchestration-made-simple/)  [Comments](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-1-0-production-ready-multi-agent-orchestration-made-simple/#Comments)  Share

Today we are excited to announce version 1.0 of the [Strands Agents SDK](https://github.com/strands-agents/sdk-python), marking a significant milestone in our journey to make building AI agents simple, reliable, and production-ready. Strands Agents is an open source SDK that takes a model-driven approach to building and running AI agents in just a few lines of code. Strands scales from simple to complex agent use cases, and from local development to deployment in production.

Since launching as a preview in May 2025, we’ve seen over 2,000 stars on GitHub and over 150K downloads on PyPI. Strands 1.0 brings the same level of simplicity to multi-agent applications that Strands has provided for single agents, with the addition of four new primitives and support for the Agent to Agent (A2A) protocol. To take multi-agent architectures into production, 1.0 also includes a new session manager for retrieving agent state from a remote datastore, and improved async support throughout the SDK. For flexibility to build your agents with any model, support for five additional model provider APIs were contributed by partners like [Anthropic](https://www.anthropic.com/), [Meta](https://www.llama.com/), [OpenAI](https://openai.com/), [Cohere](https://cohere.com/), [Mistral](https://mistral.ai/), [Stability](https://stability.ai/), [Writer](https://writer.com/), and [Baseten](https://www.baseten.co/) (see the [pull request](https://github.com/strands-agents/sdk-python/pull/389)). Let’s get into these updates in detail. Complete code samples are available on [strandsagents.com](https://strandsagents.com/).

## Simplifying multi-agent patterns

Multi-agent patterns enable specialized AI agents to work together—delegating tasks, sharing knowledge, and coordinating actions—to solve complex problems that single agents cannot handle alone. Strands 1.0 introduces four intuitive primitives that make orchestrating multiple agents a simple extension of the model/tool/prompt combination that you use to create single agents.

1. ****Agents-as-Tools: Hierarchical Delegation Made Simple**** The agents-as-tools pattern transforms specialized agents into intelligent tools that other agents can call, enabling hierarchical delegation where agents acting as the orchestrator dynamically consult domain experts without giving up control of the request. This mirrors how human teams work—a project manager doesn’t need to know everything, they just need to know which specialist to consult for each task.

```
from strands import Agent, tool
from strands_tools import calculator, file_write, python_repl, journal

@tool
def web_search(query: str) -> str:
    return "Dummy web search results here!"

# Create specialized agents
research_analyst_agent = Agent(
    system_prompt="You are a research specialist who gathers and analyzes information about local startup markets",
    tools=[web_search, calculator, file_write, python_repl]
)

travel_advisor_agent = Agent(
    system_prompt="You are a travel expert who helps with trip planning and destination advice",
    tools=[web_search, journal]
)

# Convert the agents into tools
@tool
def research_analyst(query: str) -> str:
    response = research_analyst_agent(query)
    return str(response)

@tool
def travel_advisor(query: str) -> str:
    response = travel_advisor_agent(query)
    return str(response)

# Orchestrator naturally delegates to specialists
executive_assistant = Agent(
    tools=[research_analyst, travel_advisor]
)

result = executive_assistant("I have a business meeting in Portland next week. Suggest a nice place to stay near the local startup scene, and suggest a few startups to visit")
```

In this abridged example, we define travel and research agents who have specialized prompts and tools for their areas of focus, which the executive assistant agent can call upon for input on the user’s request. The executive assistant agent is responsible for synthesizing input from other agents into the response back to the user. Learn more about [Agents-as-Tools](https://strandsagents.com/latest/user-guide/concepts/multi-agent/agents-as-tools/) in the Strands documentation.

2. ****Handoffs: Explicit transfer of control**** Handoffs enable agents to explicitly pass responsibility to humans when they encounter tasks outside their expertise, preserving full conversation context during the transfer. Strands provides a built-in `handoff_to_user` tool that agents can use to seamlessly transfer control while maintaining conversation history and context—like a customer service representative asking the customer for more information about their case.

```
from strands import Agent
from strands_tools import handoff_to_user

SYSTEM_PROMPT="""
Answer the user's support query. Ask them questions with the handoff_to_user tool when you need more information
"""

# Include the handoff_to_user tool in our agent's tool list
agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    tools=[handoff_to_user]
)

# The agent calls the handoff_to_user tool which includes the question for the customer
agent("I have a question about my order.")
```

Agents can also ask questions directly to humans when prompted to do so.

```
from strands import Agent

SYSTEM_PROMPT="""
Answer the user's support query. Ask them questions when you need more information
"""

agent = Agent(
    system_prompt=SYSTEM_PROMPT,
)

# The agent asks questions by streaming them back as text
agent("I have a question about my order.")
```

3. ****Swarms: Self-Organizing Collaborative Teams**** A Swarm creates autonomous agent teams that dynamically coordinate through shared memory, allowing multiple specialists to collaborate on complex tasks. Think of it as a brainstorming session where experts build on each other’s ideas, with the team self-organizing to deliver the best collective result.

```
import logging
from strands import Agent
from strands.multiagent import Swarm
from strands_tools import memory, calculator, file_write

# Enables Strands debug logs level, and prints to stderr
logging.getLogger("strands.multiagent").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

researcher = Agent(
    name="researcher",
    system_prompt="You research topics thoroughly using your memory and built-in knowledge",
    tools=[memory]
)

analyst = Agent(
    name="analyst",
    system_prompt="You analyze data and create insights",
    tools=[calculator, memory]
)

writer = Agent(
    name="writer",
    system_prompt="You write comprehensive reports based on research and analysis",
    tools=[file_write, memory]
)

# Swarm automatically coordinates agents
market_research_team = Swarm([researcher, analyst, writer])

result = market_research_team(
    "What is the history of AI since 1950? Create a comprehensive report"
)
```

Learn more about [Swarms](https://strandsagents.com/latest/user-guide/concepts/multi-agent/swarm/) in the Strands documentation.

4. ****Graphs: Deterministic Workflow Control**** Graphs let you define explicit agent workflows with conditional routing and decision points, helpful for processes that require specific steps, approvals, or quality gates. Like a well-designed assembly line or approval chain, graphs ensure agents work through predefined business rules in the correct order every time.

```
from strands import Agent
from strands.multiagent import GraphBuilder

analyzer_agent = Agent(
    name="analyzer",
    system_prompt="Analyze customer requests and categorize them",
    tools=[text_classifier, sentiment_analyzer]
)

normal_processor = Agent(
    name="normal_processor",
    system_prompt="Handle routine requests automatically",
    tools=[knowledge_base, auto_responder]
)

critical_processor = Agent(
    name="critical_processor",
    system_prompt="Handle critical requests quickly",
    tools=[knowledge_base, escalate_to_support_agent]
)

# Build deterministic workflow
builder = GraphBuilder()
builder.add_node(analyzer_agent, "analyze")
builder.add_node(normal_processor, "normal_processor")
builder.add_node(critical_processor, "critical_processor")

# Define conditional routing
def is_approved(state):
    return True

def is_critical(state):
    return False

builder.add_edge("analyze", "normal_processor", condition=is_approved)
builder.add_edge("analyze", "critical_processor", condition=is_critical)
builder.set_entry_point("analyze")
customer_support_graph = builder.build()

# Execute the graph with user input
results = customer_support_graph("I need help with my order!")
```

Learn more about [Graphs](https://strandsagents.com/latest/user-guide/concepts/multi-agent/graph/) in the Strands documentation.

These multi-agent patterns are designed to be gradually adopted and freely combined—start with single agents, add specialists as tools, evolve to swarms, and orchestrate with graphs as your needs grow. Mix and match patterns to create sophisticated systems: swarms can contain graphs, graphs can orchestrate swarms, and any pattern can use agents equipped with other agents as tools.

```
from strands import Agent, tool
from strands.multiagent import GraphBuilder, Swarm
from strands_tools import memory, calculator, python_repl, file_write

# Start simple with a single agent
agent = Agent(tools=[memory])

# Create specialist agents that a lead orchestrator agent can consult
data_analyst = Agent(name="analyst", tools=[calculator, python_repl])

@tool
def data_analyst_tool(query: str) -> str:
    return str(data_analyst(query))

analyst_orchestrator = Agent(tools=[memory, data_analyst_tool]) # Agents-as-tools

# Compose patterns together - a graph that uses a swarm
researcher = Agent(name="researcher", tools=[memory])
writer = Agent(name="writer", tools=[file_write])
research_swarm = Swarm([researcher, analyst_orchestrator, writer])
review_agent = Agent(system_prompt="Review the research quality and suggest improvements")
builder = GraphBuilder()
builder.add_node(research_swarm, "research") # Swarm as graph node
builder.add_node(review_agent, "review")
builder.add_edge("research", "review")
graph = builder.build()

# The patterns nest naturally - swarms in graphs, agents as tools everywhere
result = graph("How has green energy evolved over the last few years?")
```

## Multi-Agent Systems with A2A

Strands 1.0 includes support for the [Agent-to-Agent (A2A) protocol](https://a2aproject.github.io/A2A/latest/), an open standard that enables agents from different platforms to communicate seamlessly. Any Strands agent can be wrapped with A2A capabilities to become network accessible and adhere to the A2A protocol. A2A agents from external organizations can also be used directly within all Strands multi-agent patterns.

```
from strands import Agent
from strands.multiagent.a2a import A2AServer
from strands_tools.a2a_client import A2AClientToolProvider

# Serve your agent via A2A protocol
local_agent = Agent(name="analyzer", tools=[web_search, data_analysis])
a2a_agent = A2AServer(agent=local_agent, port=9000)
a2a_agent.serve() # AgentCard available at http://localhost:9000/.well-known/agent.json

# Use remote A2A agents
partner_agent_url = "https://partner.com"
cloud_agent_url = "https://cloud.ai"

# Connect to remote A2A enabled agents
a2a_tool_provider = A2AClientToolProvider(known_agent_urls=[partner_agent_url, cloud_agent_url])

# Orchestrate remote agents
orchestrator = Agent(tools=[a2a_tool_provider.tools])
```

Because A2A provides features like the agent card, a standardized description of agent capabilities, A2A-enabled multi-agent systems can easily discover and connect to agents created by other teams or other organizations. Strands auto-generates the agent card based on the tools you’ve given the agent. To see complete working examples and get started with the A2A integration, check out our [samples repository](https://github.com/strands-agents/samples/tree/main/03-integrations/Native-A2A-Support) and the [Strands A2A documentation](https://strandsagents.com/latest/user-guide/concepts/multi-agent/agent-to-agent/).

## Production-Ready

While Strands has been used in production by Amazon teams like Amazon Q Developer and AWS Glue long before its public release, we’ve been working backwards with hundreds of customers worldwide to extend Strands to support your production needs. These updates include a session management abstraction to support persisting data to and recovering from external data stores, structured output, improved async support, and much more ([releases changelog](https://github.com/strands-agents/sdk-python/releases)).

**Durable Session Management**: We’ve added `SessionManager`, a session management abstraction that enables automatic persistence and restoration of agent conversations and state. This allows agents to save their complete history to a storage backend like Amazon Simple Storage Service (Amazon S3) and seamlessly resume conversations even after compute restarts. Here’s an example using basic file-based persistence.

```
from strands import Agent
from strands.session.file_session_manager import FileSessionManager

# Create a session manager with file-based storage
Session_manager = FileSessionManager(session_id=”customer_support”, base_dir="./agent_sessions")

# Agent automatically persists all conversations
agent = Agent(
    id="support_bot_1",
    session_manager=session_manager,
    tools=[knowledge_base, ticket_system]
)

# Messages are automatically saved as the conversation progresses
agent("Help me reset my password")
agent("I can't access my email")

# Later, even after a restart, restore the full conversation
restored_session_manager = FileSessionManager(session_id=”customer_support”, base_dir="./agent_sessions")

restored_agent = Agent(
    id="support_bot_1",
    session_manager=restored_session_manager,
    tools=[knowledge_base, ticket_system]
)

# Agent remembers entire conversation history and can continue seamlessly
```

You can extend this abstraction with your own storage backend implementation through a Data Access Object (DAO) pattern, and Strands includes local filesystem and Amazon S3 backends by default. Each agent gets a unique ID for tracking, and the system handles concurrent agents within the same session for multi-agent scenarios, ensuring your agents maintain context across deployments, scaling events, and system restarts. Learn more about [Session Management](https://strandsagents.com/latest/user-guide/concepts/agents/session-management/) in the Strands documentation.

**Native Async Support and Improved Performance**: Production workloads demand reliability and responsive performance. For 1.0, we’ve improved the Strands event loop architecture to support async operations throughout the entire stack. Tools and model providers can now run asynchronously without blocking, enabling true concurrent execution. The new `stream_async` method streams all agent events—text, tool usage, reasoning steps—in real-time, with built-in cancellation support for when users navigate away.

```
import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from strands import Agent
from strands_tools import calculator

app = FastAPI()
@app.post("/chat")

async def chat_endpoint(message: str):
    async def stream_response():
        agent = Agent(tools=[web_search, calculator])
        # Stream agent responses in real-time
        async for event in agent.stream_async(message):
            if "data" in event:
                yield f"data: {event['data']}\n\n"
            elif "current_tool_use" in event:
                yield f"event: tool\ndata: Using {event['current_tool_use']['name']}\n\n"
    return StreamingResponse(stream_response(), media_type="text/event-stream")

# Concurrent agent evaluation
async def evaluate_models_concurrently(prompt: str):
    async def stream(agent: Agent):
        print(f"STARTING: {agent.name}")
        async for event in agent.stream_async(prompt):
            # handle events
        print(f"ENDING: {agent.name}")
        return event[“result”]  # last event is the agent result

    agents = [
        Agent(name="claude", model="us.anthropic.claude-3-7-sonnet-20250219-v1:0”),
        Agent(name="deepseek”, model="us.deepseek.r1-v1:0”),
        Agent(name="nova", model="us.amazon.nova-pro-v1:0")
    ]

    # Execute all agents concurrently
    responses = await asyncio.gather(*[stream(agent) for agent in agents])

    return responses
```

Learn more about [Native Async Support](https://strandsagents.com/latest/user-guide/concepts/streaming/async-iterators/) in the Strands documentation. **Expanded Model Provider Support**: Customers told us they needed flexibility to use different models for different tasks. To deliver this, Strands Agents has received strong support from the model provider community. Model providers like [Anthropic](https://www.anthropic.com/), [Meta](https://www.llama.com/), [OpenAI](https://openai.com/), [Cohere](https://cohere.com/), [Mistral](https://mistral.ai/), [Stability](https://stability.ai/), and [Writer](https://writer.com/) have made contributions which enable their own model API to be used by a Strands Agent with code. Accessing Strands Agents through a provider’s API infrastructure allows developers to focus on building AI-powered solutions, without managing infrastructure. These additions complement preview launch support for any model on Amazon Bedrock, OpenAI, and any OpenAI-compatible endpoint through LiteLLM. Strands lets you use different models for each agent, or switch models and model providers without modifying your tools or logic.

```
from strands import Agent
from strands.models import BedrockModel
from strands.models.openai import OpenAIModel
from strands.models.anthropic import AnthropicModel

# Configure different model providers
bedrock_model = BedrockModel(
    model_id="us.amazon.nova-pro-v1:0",
    temperature=0.3,
    top_p=0.8,
    region_name="us-west-2"
)

openai_model = OpenAIModel(
    client_args={
        "api_key": "your-api-key",
    },
    model_id="gpt-4o",
    params={
        "max_tokens": 1000,
        "temperature": 0.7,
    }
)

anthropic_model = AnthropicModel(
    client_args={
        "api_key": "your-api-key",
    },
    max_tokens=1028,
    model_id="claude-3-7-sonnet-20250219",
    params={
        "temperature": 0.5,
    }
)

# Swap models or use different models for different agents in the same system
researcher = Agent(
    name="researcher",
    model=anthropic_model,
    tools=[web_search]
)

writer = Agent(
    name="writer",
    model=openai_model,
    tools=[document_formatter]
)

analyzer = Agent(
    name="analyzer",
    model=bedrock_model,
    tools=[data_processor]
)
```

The Strands community has been a critical voice in shaping all of these updates, through usage, feedback and direct code contributions. Of the over 150 PRs merged into Strands between 0.1.0 and 1.0, 22% were contributed by community members who fixed bugs, added model providers, wrote docs, added features, and refactored classes to improve performance. We’re deeply grateful to [each of you](https://github.com/strands-agents/sdk-python/graphs/contributors) for helping make Strands the simplest way to take an agent from prototype to production.

The future of AI is multi-agent, and with Strands 1.0, that future is ready for production. Start building today at [strandsagents.com](https://strandsagents.com/).

![Ryan Coleman](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/06/13/Ryan-Coleman.jpg)

### Ryan Coleman

Ryan Coleman is a product manager at Amazon Web Services focused on AI developer tools and agentic frameworks. With a background in DevOps and open source, he helps builders harness the power of large language models to create intelligent, scalable software systems.

![Belle Guttman](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/07/14/Belle-Guttman.png)

### Belle Guttman

Belle Guttman leads the Agentic AI Engineering teams at AWS responsible for the Strands SDK and agentic chat in Q Developer products. With a background in software engineering, she has spent her career solving complex technical problems with simple solutions for her customers.

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