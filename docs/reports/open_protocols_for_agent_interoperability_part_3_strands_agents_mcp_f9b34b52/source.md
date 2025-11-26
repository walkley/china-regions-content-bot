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

# Open Protocols for Agent Interoperability Part 3: Strands Agents & MCP

by Nick Aldridge, James Ward, and Clare Liguori on 10 JUL 2025 in [Artificial Intelligence](https://aws.amazon.com/blogs/opensource/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Customer Solutions](https://aws.amazon.com/blogs/opensource/category/post-types/customer-solutions/ "View all posts in Customer Solutions"), [Open Source](https://aws.amazon.com/blogs/opensource/category/open-source/ "View all posts in Open Source") [Permalink](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-3-strands-agents-mcp/)  [Comments](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-3-strands-agents-mcp/#Comments)  Share

Developers are architecting and building systems of AI agents that work together to autonomously accomplish users’ tasks. In [Part 1](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp/) of our blog series on Open Protocols for Agent Interoperability we covered how Model Context Protocol (MCP) can be used to facilitate inter-agent communication and the MCP specification enhancements AWS is working on to enable that. The examples in Part 1 used Spring AI and Java for building the agents and connecting them with MCP. In [Part 2](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-2-authentication-on-mcp/) we discussed Authentication on MCP. This is a critical aspect of connecting agents so they can work together in a larger system, all with knowledge of who the user is. In Part 3 we will show how you can build inter-agent systems with the new [Strands Agents SDK](https://strandsagents.com/) and MCP.

Strands Agents is an open source SDK that takes a model-driven approach to building and running AI agents in just a few lines of Python code. You can read more about Strands Agents in [the documentation](https://strandsagents.com/). Since Strands Agents supports MCP we can quickly build a system consisting of multiple inter-connected agents and then deploy the agents on AWS.

Our example is an HR agent which can answer questions about employees. To do this you could imagine the HR agent communicating with a number of other agents like an employee data agent, an Enterprise Resource Planning (ERP) agent, a performance agent, goal agent, etc. For this example let’s start with a basic architecture where a REST API exposes access to an HR agent which connects to an employee info agent:

[![HR agent example architecture](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/07/10/HR-agent-architecture.png)](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/07/10/HR-agent-architecture.png)

> Note: The complete, runnable version of the following example is available in our [Agentic AI samples repo](https://github.com/aws-samples/sample-agentic-ai-demos/tree/main/modules/strands-mcp-inter-agent).

## Create a System of Agents with Strands Agents and MCP

Let’s start with the MCP server that will expose the employee data for use in the employee info agent. This is a basic MCP server:

```
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("employee-server", stateless_http=True, host="0.0.0.0", port=8002)

@mcp.tool()
def get_skills() -> set[str]:
    """all of the skills that employees may have - use this list to figure out related skills"""
    return SKILLS

@mcp.tool()
def get_employees_with_skill(skill: str) -> list[dict]:
    """employees that have a specified skill - output includes fullname (First Last) and their skills"""
    skill_lower = skill.lower()
    return [employee for employee in EMPLOYEES if any(s.lower() == skill_lower for s in employee["skills"])]

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

This MCP server exposes the ability to get a list of employee skills and get a list of employees that have a specific skill. For this example we are using fictitious data and in a future blog we will share how to secure this service.

Now that we have a way for an agent to get this employee information, let’s create the employee agent using Strands Agents. Our agent connects to the MCP server for employee information and uses Bedrock for inference. We also add a system prompt to provide some additional behavior to this agent:

```
EMPLOYEE_INFO_URL = os.environ.get("EMPLOYEE_INFO_URL", "http://localhost:8002/mcp/")
employee_mcp_client = MCPClient(lambda: streamablehttp_client(EMPLOYEE_INFO_URL))

bedrock_model = BedrockModel(
    model_id="amazon.nova-micro-v1:0",
    region_name="us-east-1",
)

def employee_agent(question: str):
    with employee_mcp_client:
        tools = employee_mcp_client.list_tools_sync()

        agent = Agent(model=bedrock_model, tools=tools, system_prompt="you must abbreviate employee first names and list all their skills", callback_handler=None)

        return agent(question)
```

This example uses Amazon Bedrock and the Nova Micro model with the employee data tool for multi-turn inference. Multi-turn inference is when an AI agent makes multiple calls to an AI model in a loop, usually involving calling tools to get or update data, completing when the initial task is done or an error happens. In this example the multi-turn inference enables a flow like:

1. User asks “list employees who have skills related to AI”
2. The LLM sees that it has access to a list of employee skills and instructs the agent to call that tool
3. The agent calls the employee `get_skills` tool and returns the skills to the LLM
4. The LLM then determines which skills are related to AI and sees that it can then get employees with each skill using the `get_employees_with_skill` tool
5. The agent gets the employees for each skill and returns them to the LLM
6. The LLM then assembles the complete list of employees with skills related to AI and returns it

This multi-turn interaction across multiple LLM calls and multiple tool calls encapsulated into a single `agent(question)` call, shows the power of Strands Agents performing an agentic loop to achieve a provided task. This example also shows how the employee agent can add additional instructions on top of the underlying tools, in this case with a system prompt.

## Expose an Agent as an MCP Server

We can interact with this agent in a number of ways. For example, we could expose it as a REST service. In our case we want to expose it in a way that will enable other agents to interact with it. We can use MCP to facilitate that inter-agent communication by exposing this agent as an MCP server. Then another agent (for example HR agent) will be able to use the employee agent as a tool.

To expose the employee agent as an MCP server we just wrap our `employee_agent` function in an `@mcp.tool`, transform the response data into a list of strings, and start the server:

```
mcp = FastMCP("employee-agent", stateless_http=True, host="0.0.0.0", port=8001)

@mcp.tool()
def inquire(question: str) -> list[str]:
    """answers questions related to our employees"""

    return [
        content["text"]
        for content in employee_agent(question).message["content"]
        if "text" in content
    ]

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

Since we’ve wrapped the employee agent in an MCP server we can now use it in other agents. The HR agent is exposed as a REST API so that we could call it from a web application or other services.

```
EMPLOYEE_AGENT_URL = os.environ.get("EMPLOYEE_AGENT_URL", "http://localhost:8001/mcp/")
hr_mcp_client = MCPClient(lambda: streamablehttp_client(EMPLOYEE_AGENT_URL))

bedrock_model = BedrockModel(
    model_id="amazon.nova-micro-v1:0",
    region_name="us-east-1",
    temperature=0.9,
)

app = FastAPI(title="HR Agent API")

class QuestionRequest(BaseModel):
    question: str

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/inquire")
async def ask_agent(request: QuestionRequest):
    async def generate():
        with hr_mcp_client:
            tools = hr_mcp_client.list_tools_sync()
            agent = Agent(model=bedrock_model, tools=tools, callback_handler=None)
            async for event in agent.stream_async(request.question):
                if "data" in event:
                    yield event["data"]

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Run MCP and Strands Agents on AWS

Of course we can run all of this on AWS using a variety of different options. Since the MCP servers use the new MCP Streamable HTTP transport, this could be run on serverless runtimes like AWS Lambda or AWS Fargate. For this example we will containerize the employee info MCP server, the employee agent, and the HR agent, run them on ECS, and expose the HR agent through a load balancer:

[![load balancer diagram](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/07/10/mermaid-diagram-2025-06-12-093700-965x1024.png)](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/07/10/mermaid-diagram-2025-06-12-093700.png)

For this example we’ve used AWS CloudFormation to define the infrastructure ([source](https://github.com/aws-samples/Sample-Model-Context-Protocol-Demos/blob/main/modules/strands-mcp-inter-agent/infra.cfn)). Now with everything running on AWS we can make a request to the HR agent:

```
curl -X POST --location "http://something.us-east-1.elb.amazonaws.com/inquire" \
-H "Content-Type: application/json" \
-d '{"question": "list employees that have skills related to AI programming"}'
```

And we get back:

```
Here are the employees with skills related to AI programming:

1. W. Rodriguez - Machine Learning, REST API
2. M. Rodriguez - DevOps, Machine Learning, Python
3. R. Rodriguez - Machine Learning, JavaScript
4. J. Rodriguez - REST API, Kubernetes, Machine Learning, Node.js
5. W. Garcia - AWS, Kubernetes, GraphQL, Machine Learning
6. W. Davis - MongoDB, Angular, Kotlin, Machine Learning, REST API
7. J. Miller - React, Machine Learning, SQL, Kotlin
8. J. Rodriguez - SQL, Machine Learning, Docker, DevOps, Git

If you need more detailed information about any of these employees or require further assistance, please let me know!
```

Get [the complete source](https://github.com/aws-samples/Sample-Model-Context-Protocol-Demos/tree/main/modules/strands-mcp-inter-agent) for this example.

## MCP Contributions from AWS

This example shows just the beginning of what we can do with Strands Agents and MCP for inter-agent communication. We’ve been working with the MCP specification and implementations to help evolve MCP to support additional capabilities that some inter-agent use cases may need.

The MCP specification has just had a [new 2025-06-18 release](https://modelcontextprotocol.io/specification/2025-06-18) which includes two contributions from AWS to better support inter-agent communication. We’ve also contributed support for these new features in various MCP implementations.

1. [Elicitation](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation): When MCP servers need additional input they can signal that to the agent (via the MCP client). Instead of a tool call providing a data response it can elicit additional information. For example, if an Employee Info Agent using an MCP tool to get employee data determines that a tool request like “get employees that have AI skills” may return more results than the user may want, it can elicit that the user provide a team name to filter on. This approach is different from a tool parameter because runtime characteristics may determine that the team name is necessary. In a future blog post in this series we will dive deeper into how to use this feature. We’ve contributed the implementations of this specification change to the Java and Python MCP SDKs, with both having merged the changes. ([Java SDK chang](https://github.com/modelcontextprotocol/java-sdk/commit/8a5a591d39256ba3947003ec4477e1722363eb35)e; [Python SDK change](https://github.com/modelcontextprotocol/python-sdk/pull/625))
2. [Structured Output Schemas](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#structured-content): MCP tools generally return data to the agent (via the MCP client) but in contrast with input schemas (which have always been required), we’ve contributed a way for tools to optionally specify an output schema. This enables agents to perform more type-safe conversions of tool outputs to typed data, enabling safer and easier transformations of that data within the agent. We will also cover this feature more in future blog posts in this series. Implementations of this feature have been contributed to MCP’s Java, Python, and TypeScript SDKs with the TypeScript implementation having already been merged. ([Java SDK pull request](https://github.com/modelcontextprotocol/java-sdk/pull/302); [Python SDK pull request](https://github.com/modelcontextprotocol/python-sdk/pull/654); [TypeScript SDK pull request](https://github.com/modelcontextprotocol/typescript-sdk/pull/454))

## Conclusion

It’s exciting to see the progress with MCP for inter-agent communication and in future parts of this series we will dive deeper into how these enhancements can be used to enable richer interactions between agents.

In this blog we’ve seen how we can use Strands Agents and MCP to create a system of agents that all work together and run on AWS. Strands Agents made it easy to build an agent connected to MCP tools, and then also expose the agent as an MCP server so that other agents can communicate with it. To get started learning about Strands Agents, check out the [documentation](https://strandsagents.com/) and [GitHub repo](https://github.com/strands-agents/sdk-python). Stay tuned for more parts of this series on Agent Interoperability!

![Nick Aldridge](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/05/19/nick-profile-2.jpg)

### Nick Aldridge

Nick Aldridge is a Principal Engineer at AWS. Over the last 6 years, Nick has worked on multiple AI/ML initiatives including Amazon Lex and Amazon Bedrock. Most recently, he led the team that launched Amazon Bedrock Knowledge Bases. Today he works on generative AI and AI infrastructure with a focus on inter-agent collaboration and function calling. Prior to AWS, Nick earned his MS at the University of Chicago.

![James Ward](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/07/10/James-Ward.png)

### James Ward

James Ward is a Principal Developer Advocate at AWS. James travels the world helping enterprise developers learn how to build reliable systems. His current focus is on helping developers build systems of AI agents using Spring AI, Embabel, Strands Agents, Amazon Bedrock, MCP, and A2A.

![Clare Liguori](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2022/05/23/JTqRDDF__200x200.jpg)

### Clare Liguori

Clare Liguori is a Senior Principal Software Engineer for AWS Agentic AI. She focuses on re-imagining how applications are built and how productive developers can be when their tools are powered by generative AI and AI agents, as part of Amazon Q Developer.

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