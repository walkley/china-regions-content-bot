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

# Build agentic AI solutions with DeepSeek-R1, CrewAI, and Amazon SageMaker AI

by Surya Kari, Bobby Lindsey, Karan Singh, and Pranav Murthy on 10 FEB 2025 in [Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/sagemaker/amazon-sagemaker-ai/ "View all posts in Amazon SageMaker AI"), [Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/ "View all posts in Artificial Intelligence") [Permalink](https://aws.amazon.com/blogs/machine-learning/build-agentic-ai-solutions-with-deepseek-r1-crewai-and-amazon-sagemaker-ai/)  [Comments](https://aws.amazon.com/blogs/machine-learning/build-agentic-ai-solutions-with-deepseek-r1-crewai-and-amazon-sagemaker-ai/#Comments)  Share

AI agents are rapidly becoming the next frontier in enterprise transformation, with 82% of organizations planning adoption within the next 3 years. According to a [Capgemini survey](https://www.capgemini.com/wp-content/uploads/2024/11/Generative-AI-in-Organizations-Refresh_25112024.pdf) of 1,100 executives at large enterprises, 10% of organizations already use AI agents, and more than half plan to use them in the next year. The recent release of the DeepSeek-R1 models brings state-of-the-art reasoning capabilities to the open source community. Organizations can build agentic applications using these reasoning models to execute complex tasks with advanced decision-making capabilities, enhancing efficiency and adaptability.

In this post, we dive into how organizations can use [Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/?gclid=CjwKCAiAtYy9BhBcEiwANWQQL-kwoCy7ZdAghF_qTtqKZCdOoS419cBEv70K_pLlN0NeCVYS8bV-JRoCPMQQAvD_BwE&trk=8987dd52-6f33-407a-b89b-a7ba025c913c&sc_channel=ps&ef_id=CjwKCAiAtYy9BhBcEiwANWQQL-kwoCy7ZdAghF_qTtqKZCdOoS419cBEv70K_pLlN0NeCVYS8bV-JRoCPMQQAvD_BwE:G:s&s_kwcid=AL!4422!3!724218586004!e!!g!!amazon%20sagemaker%20ai!11206038603!174643422154), a fully managed service that allows you to build, train, and deploy ML models at scale, and can build AI agents using CrewAI, a popular agentic framework and open source models like DeepSeek-R1.

## Agentic design vs. traditional software design

Agentic systems offer a fundamentally different approach compared to traditional software, particularly in their ability to handle complex, dynamic, and domain-specific challenges. Unlike traditional systems, which rely on rule-based automation and structured data, agentic systems, powered by large language models (LLMs), can operate autonomously, learn from their environment, and make nuanced, context-aware decisions. This is achieved through modular components including reasoning, memory, cognitive skills, and tools, which enable them to perform intricate tasks and adapt to changing scenarios.

Traditional software platforms, though effective for routine tasks and horizontal scaling, often lack the domain-specific intelligence and flexibility that agentic systems provide. For example, in a manufacturing setting, traditional systems might track inventory but lack the ability to anticipate supply chain disruptions or optimize procurement using real-time market insights. In contrast, an agentic system can process live data such as inventory fluctuations, customer preferences, and environmental factors to proactively adjust strategies and reroute supply chains during disruptions.

Enterprises should strategically consider deploying agentic systems in scenarios where adaptability and domain-specific expertise are critical. For instance, consider customer service. Traditional chatbots are limited to preprogrammed responses to expected customer queries, but AI agents can engage with customers using natural language, offer personalized assistance, and resolve queries more efficiently. AI agents can significantly improve productivity by automating repetitive tasks, such as generating reports, emails, and software code. The deployment of agentic systems should focus on well-defined processes with clear success metrics and where there is potential for greater flexibility and less brittleness in process management.

### DeepSeek-R1

In this post, we show you how to deploy [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) on SageMaker, particularly the Llama-70b distilled variant [DeepSeek-R1-Distill-Llama-70B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B) to a SageMaker real-time endpoint. DeepSeek-R1 is an advanced LLM developed by the AI startup DeepSeek. It employs reinforcement learning techniques to enhance its reasoning capabilities, enabling it to perform complex tasks such as mathematical problem-solving and coding. To learn more about [DeepSeek-R1, refer to DeepSeek-R1 model now available in Amazon Bedrock Marketplace](https://aws.amazon.com/blogs/machine-learning/deepseek-r1-model-now-available-in-amazon-bedrock-marketplace-and-amazon-sagemaker-jumpstart/) and Amazon SageMaker JumpStart and deep dive into the thesis behind building DeepSeek-R1.

### Generative AI on SageMaker AI

SageMaker AI, a fully managed service, provides a comprehensive suite of tools designed to deliver high-performance, cost-efficient machine learning (ML) and generative AI solutions for diverse use cases. SageMaker AI empowers you to build, train, deploy, monitor, and govern ML and generative AI models through an extensive range of services, including notebooks, jobs, hosting, experiment tracking, a curated model hub, and MLOps features, all within a unified integrated development environment (IDE).

SageMaker AI simplifies the process for generative AI model builders of all skill levels to work with foundation models (FMs):

* [Amazon SageMaker Canvas](https://aws.amazon.com/sagemaker-ai/canvas/) enables data scientists to seamlessly use their own datasets alongside FMs to create applications and architectural patterns, such as chatbots and Retrieval Augmented Generation (RAG), in a low-code or no-code environment.
* [Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker-ai/jumpstart/) offers a diverse selection of open and proprietary FMs from providers like Hugging Face, Meta, and Stability AI. You can deploy or fine-tune models through an intuitive UI or APIs, providing flexibility for all skill levels.
* SageMaker AI features like [notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl.html), [Amazon SageMaker Training](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html), [inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html), [Amazon SageMaker for MLOps](https://aws.amazon.com/sagemaker-ai/mlops/), and [Partner AI Apps](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-apps.html) enable advanced model builders to adapt FMs using LoRA, full fine-tuning, or training from scratch. These services support single GPU to HyperPods (cluster of GPUs) for training and include built-in FMOps tools for tracking, debugging, and deployment.

With SageMaker AI, you can build generative AI-powered agentic workflows using a framework of your choice. Some of the key benefits of using SageMaker AI for fine-tuning and hosting LLMs or FMs include:

* **Ease of deployment** – SageMaker AI offers access to SageMaker JumpStart, a curated model hub where models with open weights are made available for seamless deployment through a few clicks or API calls. Additionally, for Hugging Face Hub models, SageMaker AI provides pre-optimized containers built on popular open source hosting frameworks such as [vLLM](https://github.com/vllm-project/vllm), [NVIDIA Triton](https://github.com/triton-inference-server/server), and H[ugging Face Text Generation Inference (TGI).](https://huggingface.co/docs/text-generation-inference/en/index) You simply need to specify the model ID, and the model can be deployed quickly.
* **Instance-based deterministic pricing** – SageMaker AI hosted models are billed based on instance-hours rather than token usage. This pricing model enables you to more accurately predict and manage generative AI inference costs while scaling resources to accommodate incoming request loads.
* **Deployments with quantization** – SageMaker AI enables you to optimize models prior to deployment using advanced strategies such as quantized deployments (such as AWQ, GPTQ, float16, int8, or int4). This flexibility allows you to efficiently deploy large models, such as a 32-billion parameter model, onto smaller instance types like ml.g5.2xlarge with 24 GB of GPU memory, significantly reducing resource requirements while maintaining performance.
* **Inference load balancing and optimized routing** – SageMaker endpoints support load balancing and optimized routing with various strategies, providing users with enhanced flexibility and adaptability to accommodate diverse use cases effectively.
* **SageMaker fine-tuning recipes** – SageMaker offers [ready-to-use recipes](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-recipes.html) for quickly training and fine-tuning publicly available FMs such as Meta’s Llama 3, Mistral, and Mixtral. These recipes use [Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker-ai/hyperpod/) (a SageMaker AI service that provides resilient, self-healing clusters optimized for large-scale ML workloads), enabling efficient and resilient training on a GPU cluster for scalable and robust performance.

## Solution overview

CrewAI provides a robust framework for developing multi-agent systems that integrate with AWS services, particularly SageMaker AI. CrewAI’s role-based agent architecture and comprehensive performance monitoring capabilities work in tandem with [Amazon CloudWatch](http://aws.amazon.com/cloudwatch).

The framework excels in workflow orchestration and maintains enterprise-grade security standards aligned with AWS best practices, making it an effective solution for organizations implementing sophisticated agent-based systems within their AWS infrastructure.

In this post, we demonstrate how to use CrewAI to create a multi-agent research workflow. This workflow creates two agents: one that researches on a topic on the internet, and a writer agent takes this research and acts like an editor by formatting it in a readable format. Additionally, we guide you through deploying and integrating one or multiple LLMs into structured workflows, using tools for automated actions, and deploying these workflows on SageMaker AI for a production-ready deployment.

The following diagram illustrates the solution architecture.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/02/06/Picture1.png)

## Prerequisites

To follow along with the code examples in the rest of this post, make sure the following prerequisites are met:

* **Integrated development environment** – This includes the following:
  + **(Optional) Access to Amazon SageMaker Studio and the JupyterLab IDE** – We will use a Python runtime environment to build agentic workflows and deploy LLMs. Having access to a JupyterLab IDE with Python 3.9, 3.10, or 3.11 runtimes is recommended. You can also set up [Amazon SageMaker Studio](https://aws.amazon.com/sagemaker/studio/) for single users. For more details, see [Use quick setup for Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-quick-start.html). Create a new SageMaker JupyterLab Space for a quick JupyterLab notebook for experimentation. To learn more, refer to Boost productivity on Amazon SageMaker Studio: Introducing JupyterLab Spaces and generative AI tools.
  + **Local IDE** – You can also follow along in your local IDE (such as PyCharm or VSCode), provided that Python runtimes have been configured for site to AWS VPC connectivity (to deploy models on SageMaker AI).
* **Permission to deploy models** – Make sure that your user execution role has the necessary permissions to deploy models to a SageMaker real-time endpoint for inference. For more information, refer to [Deploy models for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html).
* **Access to Hugging Face Hub** – You must have access to Hugging Face Hub’s [deepseek-ai/DeepSeek-R1-Distill-Llama-8B model](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B) weights from your environment.
* **Access to code** – The code used in this post is available in the following GitHub repo.

## Simplified LLM hosting on SageMaker AI

Before orchestrating agentic workflows with CrewAI powered by an LLM, the first step is to host and query an LLM using [SageMaker real-time inference endpoints](https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/sagemaker.html). There are two primary methods to host LLMs on SageMaker AI:

* Deploy from SageMaker JumpStart
* Deploy from Hugging Face Hub

## Deploy DeepSeek from SageMaker JumpStart

SageMaker JumpStart offers access to a diverse array of state-of-the-art FMs for a wide range of tasks, including content writing, code generation, question answering, copywriting, summarization, classification, information retrieval, and more. It simplifies the onboarding and maintenance of publicly available FMs, allowing you to access, customize, and seamlessly integrate them into your ML workflows. Additionally, SageMaker JumpStart provides solution templates that configure infrastructure for common use cases, along with executable example notebooks to streamline ML development with SageMaker AI.

The following screenshot shows an example of available models on SageMaker JumpStart.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/02/06/Picture2.png)

To get started, complete the following steps:

1. Install the latest version of the [sagemaker-python-sdk](https://github.com/aws/sagemaker-python-sdk) using [pip](https://pypi.org/project/sagemaker/).
2. Run the following command in a Jupyter cell or the SageMaker Studio terminal:

```
pip install -U sagemaker
```

3. List all available LLMs under the Hugging Face or Meta JumpStart hub. The following code is an example of how to do this programmatically using the SageMaker Python SDK:

```
from sagemaker.jumpstart.filters import (And, Or)
from sagemaker.jumpstart.notebook_utils import list_jumpstart_models

# generate a conditional filter to only select LLMs from HF or Meta
filter_value = Or(
    And("task == llm", "framework == huggingface"),
    "framework == meta", "framework == deekseek"
)

# Retrieve all available JumpStart models
all_models = list_jumpstart_models(filter=filter_value)
```

For example, deploying the `deepseek-llm-r1` model directly from SageMaker JumpStart requires only a few lines of code:

```
from sagemaker.jumpstart.model import JumpStartModel

model_id = " deepseek-llm-r1"
model_version = "*"

# instantiate a new JS meta model
model = JumpStartModel(
    model_id=model_id,
    model_version=model_version
)

# deploy model on a 1 x p5e instance
predictor = model.deploy(
    accept_eula=True,
    initial_instance_count=1,
    # endpoint_name="deepseek-r1-endpoint" # optional endpoint name
)
```

We recommend deploying your SageMaker endpoints within a VPC and a private subnet with no egress, making sure that the models remain accessible only within your VPC for enhanced security.

We also recommend you integrate with [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) for increased safeguards against harmful content. For more details on how to implement Amazon Bedrock Guardrails on a self-hosted LLM, see [Implement model-independent safety measures with Amazon Bedrock Guardrails](https://aws.amazon.com/blogs/machine-learning/implement-model-independent-safety-measures-with-amazon-bedrock-guardrails/).

## Deploy DeepSeek from Hugging Face Hub

Alternatively, you can deploy your preferred model directly from the [Hugging Face Hub](https://huggingface.co/models) or the [Hugging Face Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/) to a SageMaker endpoint. Hugging Face LLMs can be hosted on SageMaker using a variety of supported frameworks, such as NVIDIA Triton, vLLM, and Hugging Face TGI. For a comprehensive list of supported deep learning container images, refer to the available [Amazon SageMaker Deep Learning Containers](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html). In this post, we use a ***DeepSeek-R1-Distill-Llama-70B*** SageMaker endpoint using the TGI container for agentic AI inference. We deploy the model from Hugging Face Hub using [Amazon’s optimized TGI container](https://huggingface.co/blog/sagemaker-huggingface-llm), which provides enhanced performance for LLMs. This container is specifically optimized for text generation tasks and automatically selects the most performant parameters for the given hardware configuration. To deploy from Hugging Face Hub, refer to the **[GitHub repo](https://github.com/aws-samples/amazon-sagemaker-generativeai/tree/main/agents-with-sagemaker/deepseek_crewai_based_agent)** or the following code snippet:

```
import json
import sagemaker
import boto3
from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri
import os
from datetime import datetime

# Model configuration
hub = {'HF_MODEL_ID':'deepseek-ai/DeepSeek-R1-Distill-Llama-70B', #Llama-3.3-70B-Instruct
       'SM_NUM_GPUS': json.dumps(number_of_gpu),
       'HF_TOKEN': HUGGING_FACE_HUB_TOKEN,
       'SAGEMAKER_CONTAINER_LOG_LEVEL': '20',  # Set to INFO level
       'PYTORCH_CUDA_ALLOC_CONF': 'expandable_segments:True'  # configure CUDA memory to use expandable memory segments
}
# Create and deploy model
huggingface_model =   HuggingFaceModel(image_uri=get_huggingface_llm_image_uri("huggingface",
version="2.3.1"),
env=hub,
role=role,sagemaker_session=sagemaker_session)
predictor = huggingface_model.deploy(
               initial_instance_count=1,
               instance_type="ml.p4d.24xlarge"
               endpoint_name=custom_endpoint_name,
               container_startup_health_check_timeout=900)
```

A new ***DeepSeek-R1-Distill-Llama-70B*** endpoint should be `InService` in under 10 minutes. If you want to change the model from DeepSeek to another model from the hub, simply replace the following parameter or refer to the DeepSeek deploy example in the following [GitHub repo](https://github.com/huggingface/text-generation-inference/blob/main/docs/source/reference/launcher.md). To learn more about deployment parameters that can be reconfigured inside TGI containers at runtime, refer to the following [GitHub repo](https://github.com/aws-samples/sagemaker-genai-hosting-examples/blob/main/Deepseek/DeepSeek-R1-Llama8B-LMI-TGI-Deploy.ipynb) on TGI arguments.

```
...
"HF_MODEL_ID": "deepseek-ai/...", # replace with any HF hub models
# "HF_TOKEN": "hf_..." # add your token id for gated models
...
```

For open-weight models deployed directly from hubs, we strongly recommend placing your SageMaker endpoints within a VPC and a private subnet with no egress, making sure that the models remain accessible only within your VPC for a secure deployment.

## Build a simple agent with CrewAI

CrewAI offers the ability to create multi-agent and very complex agentic orchestrations using LLMs from several LLM providers, including SageMaker AI and Amazon Bedrock. In the following steps, we create a simple blocks counting agent to serve as an example.

**Create a blocks counting agent**

The following code sets up a simple blocks counter workflow using CrewAI with two main components:

* **Agent creation (blocks\_counter\_agent)** – The agent is configured with a specific role, goal, and capabilities. This agent is equipped with a tool called ***BlocksCounterTool***.
* **Task definition (count\_task)** – This is a task that we want this agent to execute. The task includes a template for counting how many of each color of blocks are present, where ***{color}*** will be replaced with actual color of the block. The task is assigned to ***blocks\_counter\_agent***.

```
from crewai import Agent, Task
from pydantic import BaseModel, Field

# 1. Configure agent
blocks_counter_agent = Agent(
    role="Blocks Inventory Manager",
    goal="Maintain accurate block counts",
    tools=[BlocksCounterTool],
    verbose=True
)

# 2. Create counting task
count_task = Task(
    description="Count {color} play blocks in storage",
    expected_output="Exact inventory count for specified color",
    agent=blocks_counter_agent
)
```

As you can see in the preceding code, each agent begins with two essential components: an agent definition that establishes the agent’s core characteristics (including its role, goal, backstory, available tools, LLM model endpoint, and so on), and a task definition that specifies what the agent needs to accomplish, including the detailed description of work, expected outputs, and the tools it can use during execution.

This structured approach makes sure that agents have both a clear identity and purpose (through the agent definition) and a well-defined scope of work (through the task definition), enabling them to operate effectively within their designated responsibilities.

## Tools for agentic AI

Tools are special functions that give AI agents the ability to perform specific actions, like searching the internet or analyzing data. Think of them as apps on a smartphone—each tool serves a specific purpose and extends what the agent can do. In our example, ***BlocksCounterTool*** helps the agent count the number of blocks organized by color.

Tools are essential because they let agents do real-world tasks instead of just thinking about them. Without tools, agents would be like smart speakers that can only talk—they could process information but couldn’t take actual actions. By adding tools, we transform agents from simple chat programs into practical assistants that can accomplish real tasks.

**Out-of-the-box tools with CrewAI** Crew AI offers a range of tools out of the box for you to use along with your agents and tasks. The following table lists some of the available tools.

|  |  |  |
| --- | --- | --- |
| **Category** | **Tool** | **Description** |
| **Data Processing Tools** | FileReadTool | For reading various file formats |
| **Web Interaction Tools** | WebsiteSearchTool | For web content extraction |
| **Media Tools** | YoutubeChannelSearchTool | For searching YouTube channels |
| **Document Processing** | PDFSearchTool | For searching PDF documents |
| **Development Tools** | CodeInterpreterTool | For Python code interpretation |
| **AI Services** | DALL-E Tool | For image generation |

**Build custom tools with CrewAI** You can build custom tools in CrewAI in two ways: by subclassing BaseTool or using the @tool decorator. Let’s look at the following BaseTool subclassing option to create the BlocksCounterTool we used earlier:

```
from crewai.tools import BaseTool

class BlocksCounterTool(BaseTool):
    name = "blocks_counter"
    description = "Simple tool to count play blocks"

    def _run(self, color: str) -> str:
        return f"There are 10 {color} play blocks available"
```

## **Build a multi-agent workflow with CrewAI, DeepSeek-R1, and SageMaker AI**

Multi-agent AI systems represent a powerful approach to complex problem-solving, where specialized AI agents work together under coordinated supervision. By combining CrewAI’s workflow orchestration capabilities with SageMaker AI based LLMs, developers can create sophisticated systems where multiple agents collaborate efficiently toward a specific goal. The code used in this post is available in the following [GitHub repo](https://github.com/aws-samples/amazon-sagemaker-generativeai/tree/main/agents-with-sagemaker/deepseek_crewai_based_agent).

Let’s build a research agent and writer agent that work together to create a PDF about a topic. We will use a DeepSeek-R1 Distilled Llama 3.3 70B model as a SageMaker endpoint for the LLM inference.

**Define your own DeepSeek SageMaker LLM (using LLM base class)**

The following code integrates SageMaker hosted LLMs with CrewAI by creating a custom inference tool that formats prompts with system instructions for factual responses, uses Boto3, an AWS core library, to call SageMaker endpoints, and processes responses by separating reasoning (before </think>) from final answers. This enables CrewAI agents to use deployed models while maintaining structured output patterns.

```
# Calls SageMaker endpoint for DeepSeek inference
def deepseek_llama_inference(prompt: dict, endpoint_name: str, region: str = "us-east-2") -> dict:
    try:
        # ... Response parsing Code...

    except Exception as e:
        raise RuntimeError(f"Error while calling SageMaker endpoint: {e}")

# CrewAI-compatible LLM implementation for DeepSeek models on SageMaker.
class DeepSeekSageMakerLLM(LLM):
    def __init__(self, endpoint: str):
        # <... Initialize LLM with SageMaker endpoint ...>

    def call(self, prompt: Union[List[Dict[str, str]], str], **kwargs) -> str:
        # <... Format and return the final response ...>
```

**Name the DeepSeek-R1 Distilled endpoint**

Set the endpoint name as defined earlier when you deployed DeepSeek from the Hugging Face Hub:

```
deepseek_endpoint = "deepseek-r1-dist-v3-llama70b-2025-01-22"
```

**Create a DeepSeek inference tool**

Just like how we created the BlocksCounterTool earlier, let’s create a tool that uses the DeepSeek endpoint for our agents to use. We use the same BaseTool subclass here, but we hide it in the CustomTool class implementation in sage\_tools.py in the tools folder. For more information, refer to the [GitHub repo](https://github.com/aws-samples/amazon-sagemaker-generativeai/tree/main/agents-with-sagemaker/deepseek_crewai_based_agent).

```
from crewai import Crew, Agent, Task, Process

# Create the Tool for LLaMA inference
deepseek_tool = CustomTool(
    name="deepseek_llama_3.3_70B",
    func=lambda inputs: deepseek_llama_inference(
        prompt=inputs,
        endpoint_name=deepseek_endpoint
    ),
    description="A tool to generate text using the DeepSeek LLaMA model deployed on SageMaker."
)
```

**Create a research agent**

Just like the simple blocks agent we defined earlier, we follow the same template here to define the research agent. The difference here is that we give more capabilities to this agent. We attach a SageMaker AI based DeepSeek-R1 model as an endpoint for the LLM.

This helps the research agent think critically about information processing by combining the scalable infrastructure of SageMaker with DeepSeek-R1’s advanced reasoning capabilities.

The agent uses the SageMaker hosted LLM to analyze patterns in research data, evaluate source credibility, and synthesize insights from multiple inputs. By using the deepseek\_tool, the agent can dynamically adjust its research strategy based on intermediate findings, validate hypotheses through iterative questioning, and maintain context awareness across complex information it gathers.

```
# Research Agent

research_agent = Agent(
    role="Research Bot",
    goal="Scan sources, extract relevant information, and compile a research summary.",
    backstory="An AI agent skilled in finding relevant information from a variety of sources.",
    tools=[deepseek_tool],
    allow_delegation=True,
    llm=DeepSeekSageMakerLLM(endpoint=deepseek_endpoint),
    verbose=False
)
```

**Create a writer agent**

The writer agent is configured as a specialized content editor that takes research data and transforms it into polished content. This agent works as part of a workflow where it takes research from a research agent and acts like an editor by formatting the content into a readable format. The agent is used for writing and formatting, and unlike the research agent, it doesn’t delegate tasks to other agents.

```
writer_agent = Agent(
    role="Writer Bot",
    goal="Receive research summaries and transform them into structured content.",
    backstory="A talented writer bot capable of producing high-quality, structured content based on research.",
    tools=[deepseek_tool],
    allow_delegation=False,
    llm=DeepSeekSageMakerLLM(endpoint=deepseek_endpoint),
    verbose=False
)
```

**Define tasks for the agents**

Tasks in CrewAI define specific operations that agents need to perform. In this example, we have two tasks: a research task that processes queries and gathers information, and a writing task that transforms research data into polished content.

Each task includes a clear description of what needs to be done, the expected output format, and specifies which agent will perform the work. This structured approach makes sure that agents have well-defined responsibilities and clear deliverables.

Together, these tasks create a workflow where one agent researches a topic on the internet, and another agent takes this research and formats it into readable content. The tasks are integrated with the DeepSeek tool for advanced language processing capabilities, enabling a production-ready deployment on SageMaker AI.

```
research_task = Task(
    description=(
        "Your task is to conduct research based on the following query: {prompt}.\n"
    ),
    expected_output="A comprehensive research summary based on the provided query.",
    agent=research_agent,
    tools=[deepseek_tool]
)

writing_task = Task(
    description=(
              "Your task is to create structured content based on the research provided.\n""),
    expected_output="A well-structured article based on the research summary.",
    agent=research_agent,
    tools=[deepseek_tool]
)
```

**Define a crew in CrewAI**

A crew in CrewAI represents a collaborative group of agents working together to achieve a set of tasks. Each crew defines the strategy for task execution, agent collaboration, and the overall workflow. In this specific example, the sequential process makes sure tasks are executed one after the other, following a linear progression. There are other more complex orchestrations of agents working together, which we will discuss in future blog posts.

This approach is ideal for projects requiring tasks to be completed in a specific order. The workflow creates two agents: a research agent and a writer agent. The research agent researches a topic on the internet, then the writer agent takes this research and acts like an editor by formatting it into a readable format.

Let’s call the crew scribble\_bots:

```
# Define the Crew for Sequential Workflow #

scribble_bots = Crew( agents=[research_agent, writer_agent],
       tasks=[research_task, writing_task],
       process=Process.sequential # Ensure tasks execute in sequence)
```

**Use the crew to run a task**

We have our endpoint deployed, agents created, and crew defined. Now we’re ready to use the crew to get some work done. Let’s use the following prompt:

```
result = scribble_bots.kickoff(inputs={"prompt": "What is DeepSeek?"})
```

Our result is as follows:

```
**DeepSeek: Pioneering AI Solutions for a Smarter Tomorrow**

In the rapidly evolving landscape of artificial intelligence,
DeepSeek stands out as a beacon of innovation and practical application.
As an AI company, DeepSeek is dedicated to advancing the field through cutting-edge research and real-world applications,
making AI accessible and beneficial across various industries.

**Focus on AI Research and Development**

………………….. ………………….. ………………….. …………………..
```

## Clean up

Complete the following steps to clean up your resources:

1. Delete your GPU DeekSeek-R1 endpoint:

```
import boto3

# Create a low-level SageMaker service client.
sagemaker_client = boto3.client('sagemaker', region_name=<region>)

# Delete endpoint
sagemaker_client.delete_endpoint(EndpointName=endpoint_name)
```

2. If you’re using a SageMaker Studio JupyterLab notebook, shut down the JupyterLab notebook instance.

## Conclusion

In this post, we demonstrated how you can deploy an LLM such as DeepSeek-R1—or another FM of your choice—from popular model hubs like SageMaker JumpStart or Hugging Face Hub to SageMaker AI for [real-time inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-deploy-models.html). We explored inference frameworks like Hugging Face TGI which helps streamline deployment while integrating built-in performance optimizations to minimize latency and maximize throughput. Additionally, we showcased how the SageMaker developer-friendly Python SDK simplifies endpoint orchestration, allowing seamless experimentation and scaling of LLM-powered applications.

Beyond deployment, this post provided an in-depth exploration of agentic AI, guiding you through its conceptual foundations, practical design principles using CrewAI, and the seamless integration of state-of-the-art LLMs like DeepSeek-R1 as the intelligent backbone of an autonomous agentic workflow. We outlined a sequential CrewAI workflow design, illustrating how to equip LLM-powered agents with specialized tools that enable autonomous data retrieval, real-time processing, and interaction with complex external systems.

Now, it’s your turn to experiment! Dive into our publicly available code on [GitHub](https://github.com/aws-samples/amazon-sagemaker-generativeai/tree/main/agents-with-sagemaker/deepseek_crewai_based_agent), and start building your own DeepSeek-R1-powered agentic AI system on SageMaker. Unlock the next frontier of AI-driven automation—seamlessly scalable, intelligent, and production-ready.

Special thanks to Giuseppe Zappia, Poli Rao, and Siamak Nariman for their support with this blog post.

---

### About the Authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2020/12/18/Surya-Kari.jpg)[Surya Kari](https://www.linkedin.com/in/suryakari/)** is a Senior Generative AI Data Scientist at AWS, specializing in developing solutions leveraging state-of-the-art foundation models. He has extensive experience working with advanced language models including DeepSeek-R1, the LLama family, and Qwen, focusing on their fine-tuning and optimization for specific scientific applications. His expertise extends to implementing efficient training pipelines and deployment strategies using AWS SageMaker, enabling the scaling of foundation models from development to production. He collaborates with customers to design and implement generative AI solutions, helping them navigate model selection, fine-tuning approaches, and deployment strategies to achieve optimal performance for their specific use cases.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2021/06/26/Bobby-LIndsey.jpg)**Bobby Lindsey** is a Machine Learning Specialist at Amazon Web Services. He’s been in technology for over a decade, spanning various technologies and multiple roles. He is currently focused on combining his background in software engineering, DevOps, and machine learning to help customers deliver machine learning workflows at scale. In his spare time, he enjoys reading, research, hiking, biking, and trail running.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/11/25/DSC03728_cleanup-PhotoRoom-1.jpeg)**[Karan Singh](https://www.linkedin.com/in/karan-singh-a8aa7518/)** is a Generative AI Specialist for third-party models at AWS, where he works with top-tier third-party foundation model (FM) providers to develop and execute joint Go-To-Market strategies, enabling customers to effectively train, deploy, and scale FMs to solve industry specific challenges. Karan holds a Bachelor of Science in Electrical and Instrumentation Engineering from Manipal University, a master’s in science in Electrical Engineering from Northwestern University and is currently an MBA Candidate at the Haas School of Business at University of California, Berkeley.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/08/29/Pranav-Profile-100.jpeg)**Pranav Murthy** is an AI/ML Specialist Solutions Architect at AWS. He focuses on helping customers build, train, deploy and migrate machine learning (ML) workloads to SageMaker. He previously worked in the semiconductor industry developing large computer vision (CV) and natural language processing (NLP) models to improve semiconductor processes using state of the art ML techniques. In his free time, he enjoys playing chess and traveling. You can find Pranav on [LinkedIn](https://www.linkedin.com/in/pranav-murthy-6bbb5773/).

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