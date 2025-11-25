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

# Using Strands Agents with Claude 4 Interleaved Thinking

by Ryan Coleman, Jawhny Cooke, Mark Roy, and Vadim Omeltchenko on 13 JUN 2025 in [Amazon Machine Learning](https://aws.amazon.com/blogs/opensource/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Artificial Intelligence](https://aws.amazon.com/blogs/opensource/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Open Source](https://aws.amazon.com/blogs/opensource/category/open-source/ "View all posts in Open Source"), [Technical How-to](https://aws.amazon.com/blogs/opensource/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/opensource/using-strands-agents-with-claude-4-interleaved-thinking/)  [Comments](https://aws.amazon.com/blogs/opensource/using-strands-agents-with-claude-4-interleaved-thinking/#Comments)  Share

When we [introduced](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/) the Strands Agents SDK, our goal was to make agentic development simple and flexible by embracing a model-driven approach. Today, we’re excited to highlight how you can use Claude 4’s interleaved thinking beta feature with Strands to further simplify how you write AI agents to solve complex tasks with tools. With a model-driven approach, developers no longer need to define a rigid workflow to call tools and parse model responses at each step to complete a task. With [Strands Agents](https://github.com/strands-agents/sdk-python), you equip a model with tools and a prompt, letting it plan, chain thoughts, call tools, and reflect. Strands manages an event loop around model calls until it considers the task completed, returning a response to the client. Let’s consider how it works with this simple example (assuming you have completed the [quickstart](https://strandsagents.com/latest/user-guide/quickstart/)):

```
from strands import Agent
from strands_tools import http_request, python_repl

agent = Agent(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    tools=[http_request, python_repl]
)

prompt="""
Which of the following cities is closest to the ISS?
Portland, Vancouver, Seattle, or New York?

Include the current altitude of the ISS, and the distance and vector from the closest city to the ISS.
"""

agent(prompt)
```

Strands has everything it needs to provide an answer, equipped with Claude 4 Sonnet, its prompt, and tools to generate Python code and make HTTP requests. Here’s how the event loop works.

First, Strands structures your prompt and any previous conversation history into a format the language model (like Claude) can understand. Then, Strands automatically loads available tools—these can be MCP Server tools or custom Python functions decorated with @tool. Your Python docstrings become tool descriptions, and type hints define the parameter schemas. In this example, we use two built-in tools from the [strands-agents-tools](https://strandsagents.com/latest/user-guide/concepts/tools/tools_overview/#3-example-built-in-tools) package. The SDK manages errors (like rate limiting or context overflows), performs retries when needed, and emits detailed traces and metrics for observability.

With this setup complete, Strands manages an event loop that invokes the model, handles tool calling, and manages the conversation until the model provides a final answer.

1. **Model invocation and reasoning**: The event loop calls the language model with the current conversation state, prompt, and tools. The model streams its responses, including step-by-step reasoning that you can observe as it “thinks out loud.”
2. **Tool use detection and execution**: If the model decides it needs to call a tool (to fetch data, perform a calculation, etc.), the event loop detects this request, validates it, and executes the corresponding Python function or MCP Server tool with the parameters provided by the model.
3. **Context update**: The result of the tool execution is appended to the ongoing conversation, allowing the model to incorporate the new information into its next iteration.

You will see this loop in action when running the ISS example with Python. The model makes a plan to use its tools, including API calls for real-time data about the ISS and using its Python REPL (Read evaluate print loop) to calculate distances and vectors. The agent will respond with an answer to the question, including a statement like “The ISS is currently positioned over the western Pacific Ocean, making the western North American cities (Vancouver, Seattle, Portland) much closer than New York. Vancouver’s slightly more northern latitude gives it the advantage over Seattle and Portland.”

The model makes a plan to use its tools, involving API calls for real-time data about the ISS and using its Python REPL to calculate distances and vectors. It then generates an answer and shows its work. The following is example output from this agent running locally.

```
To answer this question, I need to:
1. Get the current position of the ISS (International Space Station)
2. Get the coordinates of the four cities: Portland, Vancouver, Seattle, and New York
3. Calculate the distance from each city to the ISS
4. Determine which is closest and provide the requested information
First, I need to find an API that provides the current ISS position. There are several free APIs available for this, such as:
- http://api.open-notify.org/iss-now.json (provides current ISS position)
- Others that might provide more detailed information
Let me start by getting the current ISS position.I'll help you find which city is closest to the ISS by getting the current position of the International Space Station and calculating distances. Let me start by fetching the current ISS location.
Tool #1: http_request
Great! I got the current ISS position:
- Latitude: -24.4214°
- Longitude: 14.4347°
- Timestamp: 1749832513
Now I need to get the altitude of the ISS. The basic API doesn't provide altitude, but I know the ISS orbits at approximately 400-420 km altitude. Let me try to find a more detailed API or use a known average.
Actually, let me try another API that might give more details about the ISS:Now let me get more detailed information about the ISS including its altitude:
Tool #2: http_request
Perfect! Now I have more detailed ISS information:
- Name: ISS
- Latitude: -24.844251408166°
- Longitude: 14.692696204258°
- Altitude: 422.41885597014 km
- Velocity: 27570.247286017 km/h
- Timestamp: 1749832520
Now I need to calculate the distances from each city to the ISS. For this, I'll need the coordinates of each city and then calculate 3D distances considering the ISS altitude.
The cities I need coordinates for:
1. Portland (I'll assume Portland, Oregon)
2. Vancouver (I'll assume Vancouver, BC, Canada)
3. Seattle, Washington
4. New York, New York
Let me use Python to calculate these distances. Perfect! Now I have the current ISS data. Let me calculate the distances from each city to the ISS using Python:
Tool #3: python_repl
Current ISS Position:
Latitude: -24.844251408166°
Longitude: 14.692696204258°
Altitude: 422.42 km
Portland:
  Coordinates: 45.5152°, -122.6784°
  3D Distance to ISS: 15588.43 km
  Surface Distance: 15582.71 km
Vancouver:
  Coordinates: 49.2827°, -123.1207°
  3D Distance to ISS: 15484.80 km
  Surface Distance: 15479.03 km
Seattle:
  Coordinates: 47.6062°, -122.3321°
  3D Distance to ISS: 15493.28 km
  Surface Distance: 15487.52 km
New York:
  Coordinates: 40.7128°, -74.006°
  3D Distance to ISS: 11680.55 km
  Surface Distance: 11672.91 km
CLOSEST CITY: New York
Distance: 11680.55 km
Great! Now I have all the distances calculated. New York is the closest city to the ISS. Now I need to calculate the vector from New York to the ISS. A vector would include both the direction and magnitude. I should calculate:
1. The bearing (direction) from New York to the ISS
2. The elevation angle
3. The distance (which I already have)
Let me calculate these additional details.Now let me calculate the vector (direction and elevation) from New York to the ISS:
Tool #4: python_repl
==================================================
FINAL RESULTS
==================================================
International Space Station Current Status:
• Altitude: 422.42 km above Earth
• Position: -24.8443°, 14.6927°
• Location: Over the South Atlantic Ocean
Distance Analysis:
• Portland, OR: 15588.43 km
• Vancouver, BC: 15484.80 km
• Seattle, WA: 15493.28 km
• New York, NY: 11680.55 km
CLOSEST CITY: NEW YORK
• Distance: 11680.55 km
• Bearing: 110.1° (ESE)
• Elevation angle: 2.1° above horizon
Vector from New York to ISS:
• Direction: 110.1° bearing (ESE)
• Elevation: 2.1° above horizontal
• Distance: 11680.55 km
Perfect! I now have all the information requested. Let me summarize the key findings:
1. **Current ISS altitude**: 422.42 km above Earth
2. **Closest city**: New York is closest to the ISS
3. **Distance and vector**:
   - Distance: 11,680.55 km
   - Direction: 110.1° bearing (East-Southeast)
   - Elevation: 2.1° above horizon
The ISS is currently positioned over the South Atlantic Ocean at coordinates -24.8443°, 14.6927°. Among the four cities, New York is significantly closer than the other three cities (which are all on the US/Canadian west coast and much farther from the ISS's current position).## Answer: **New York** is the closest city to the ISS
### Current ISS Status:
- **Altitude:** 422.42 km above Earth
- **Position:** 24.84°S, 14.69°E (over the South Atlantic Ocean)
### Distance Comparison:
- **New York, NY:** 11,680.55 km ✅ **CLOSEST**
- **Vancouver, BC:** 15,484.80 km
- **Seattle, WA:** 15,493.28 km
- **Portland, OR:** 15,588.43 km
### Vector from New York to ISS:
- **Distance:** 11,680.55 km
- **Direction:** 110.1° bearing (East-Southeast)
- **Elevation:** 2.1° above the horizon
The ISS is currently positioned over the South Atlantic Ocean, making New York significantly closer than the three Pacific Northwest cities. New York is about 4,800 km closer to the ISS than the nearest west coast city (Vancouver).
```

## Supercharging the Strands event loop with Claude 4’s interleaved thinking

Claude 4 introduces a beta feature called “interleaved thinking” which fits perfectly with Strands’ model-driven approach. This enables Claude to reflect after a tool call and adjust its plan dynamically without needing to complete the current event loop iteration. Interleaved thinking expands on the model’s ability to self-reflect, correct errors, and orchestrate a workflow of reasoning and tool use.

If you’re using Amazon Bedrock as your Strands model provider, you can turn on interleaved thinking by specifying the additional request fields parameter to Bedrock:

```
from strands import Agent
from strands_tools import http_request, python_repl
from strands.models import BedrockModel

model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-20250514-v1:0",
    additional_request_fields={
        "anthropic_beta": ["interleaved-thinking-2025-05-14"],
        "thinking": {"type": "enabled", "budget_tokens": 8000},
    },
)

agent = Agent(
    model=model,
    tools=[http_request, python_repl]
)
…
```

If you enable [tracing with Strands](https://strandsagents.com/latest/user-guide/observability-evaluation/traces/), you’ll see additional blocks of “reasoningContent” in your trace, like in the following image, including reasoning when Claude 4 decides to interleave thinking after tool calls.

[![Reasoning content example](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/06/13/Model-invoke-1024x216.png)](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/06/13/Model-invoke.png)

For example, in this response there is an erroneous calculation from a tool call, which Claude could identify and fix immediately, before continuing to the next iteration of the event loop.

```
City Rankings (closest to farthest):
1	Vancouver: 12027.19 km
2	Seattle: 12144.49 km
3	Portland: 12195.86 km
4	New York: 15432.29 km
The calculation for longitude difference looks wrong - it's showing 243.6443° which is more than 180°. This happens because we're dealing with the international date line. Let me correct this calculation to show the actual shortest path. Let me correct the longitude calculation to show the actual shortest path:
Tool #6: python_repl
CORRECTED VECTOR CALCULATION:
ニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニニ
ISS Current Altitude: 418.15 km above Earth's surface
Closest City: Vancouver, BC
Distance to ISS: 12027.19 km
Vector from Vancouver to ISS:
- **Distance:** 12027.19 km
- **Direction:** 110.1° bearing (East-Southeast)
- **Elevation:** 2.1° above the horizon
```

Compared to the traditional ReAct method, the interleaved thinking approach is faster and more fluid. You can think of ReAct like a detective taking notes and making deductions step by step, whereas interleaved thinking is more like a domain expert mentally juggling facts while explaining a concept. In other words, thought and action happen in one thinking block, not another complete loop.

Here’s another example where Claude was able to reduce the number of tool calls by noticing it could calculate the answer from the information retrieved in its first API call, which otherwise would have only been determined in a second iteration of the event loop.

```
Let me start by getting the ISS position. I'll help you find which city is closest to the ISS by getting the current ISS position and calculating distances. Let me start by fetching the current ISS location.
Tool #1: http_request
Great! I got the ISS position. Now I need to get the altitude of the ISS. The Open Notify API doesn't provide altitude in the basic position endpoint, but I know the ISS typically orbits at around 400-420 km altitude. Let me check if there's another endpoint that provides more detailed information.
Actually, let me use Python to calculate the distances between the ISS and each city. I'll need to: Define the coordinates of each city, Calculate the distance from each city to the ISS position, Account for the ISS altitude in the calculation
The ISS position shows:
⁃	Latitude: 44.7381°
⁃	Longitude: 169.1833°
This puts the ISS somewhere over the Pacific Ocean, likely between Russia and Alaska.
```

These examples only scratch the surface of what you can build with Strands and Claude 4 using interleaved thinking. We’ve published additional [agent samples](https://github.com/strands-agents/samples/tree/main) tackling more complex problems and equipped with numerous tools, like [this one](https://github.com/strands-agents/samples/blob/main/01-tutorials/02-multi-agent-systems/01-agent-as-tool/agents-as-tools-interleaved.ipynb) demonstrating interleaved thinking. Using these examples, you’ll see more dynamic reasoning from Claude, like learning from a failed tool call and retrying with refined parameters, or coming up with new strategies on the fly instead of looping the same strategy across multiple tool calls.

We built Strands Agents to simplify agent development by embracing models like Claude 4 that do a great job of breaking down problems into tool workflows that achieve results. We can’t wait to see what you build with Strands. Join the discussion at <https://github.com/strands-agents/sdk-python>

*Jawhny Cooke, Vadim Omeltchenko, and Mark Roy contributed to this post.*

![Ryan Coleman](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/06/13/Ryan-Coleman.jpg)

### Ryan Coleman

Ryan Coleman is a product manager at Amazon Web Services focused on AI developer tools and agentic frameworks. With a background in DevOps and open source, he helps builders harness the power of large language models to create intelligent, scalable software systems.

![Jawhny Cooke](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/06/25/jawcooke.png)

### Jawhny Cooke

Jawhny Cooke is a Senior Anthropic Specialist Solutions Architect for Generative AI at AWS. He specializes in integrating and deploying Anthropic models on AWS infrastructure. He partners with customers and AI providers to implement production-grade generative AI solutions through Amazon Bedrock, offering expert guidance on architecture design and system implementation to maximize the potential of these advanced models.

![Mark Roy](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/06/25/roymark.jpg)

### Mark Roy

Mark Roy is a Principal Machine Learning Architect for AWS, helping customers design and build generative AI solutions. His focus since early 2023 has been leading solution architecture efforts for the launch of Amazon Bedrock, the flagship generative AI offering from AWS for builders. Mark’s work covers a wide range of use cases, with a primary interest in generative AI, agents, and scaling ML across the enterprise. He has helped companies in insurance, financial services, media and entertainment, healthcare, utilities, and manufacturing. Prior to joining AWS, Mark was an architect, developer, and technology leader for over 25 years, including 19 years in financial services. Mark holds six AWS Certifications, including the ML Specialty Certification.

![Vadim Omeltchenko](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/06/25/vadimo.png)

### Vadim Omeltchenko

Vadim Omeltchenko is a Sr. AI/ML Solutions Architect who is passionate about helping AWS customers innovate in the cloud. His prior IT experience was predominantly on the ground.

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