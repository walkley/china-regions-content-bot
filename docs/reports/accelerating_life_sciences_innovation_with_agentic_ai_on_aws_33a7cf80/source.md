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

## [AWS for Industries](https://aws.amazon.com/blogs/industries/)

# Accelerating Life Sciences Innovation with Agentic AI on AWS

by Brian Loyal, Hasan Poonawala, Nadeem Bulsara, and Shamika Ariyawansa on 19 MAY 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/industries/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Bedrock Agents](https://aws.amazon.com/blogs/industries/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-bedrock-agents/ "View all posts in Amazon Bedrock Agents"), [Amazon SageMaker](https://aws.amazon.com/blogs/industries/category/artificial-intelligence/sagemaker/ "View all posts in Amazon SageMaker"), [Industries](https://aws.amazon.com/blogs/industries/category/industries/ "View all posts in Industries") [Permalink](https://aws.amazon.com/blogs/industries/accelerating-life-sciences-innovation-with-agentic-ai-on-aws/)  [Comments](https://aws.amazon.com/blogs/industries/accelerating-life-sciences-innovation-with-agentic-ai-on-aws/#Comments)  Share

In the rapidly evolving field of life sciences, organizations are increasingly turning to agentic AI to streamline complex workflows, enhance collaboration, and accelerate research outcomes. With recent advancements in foundation models, enterprise-grade infrastructure, and developer tools, building intelligent agents is now more accessible, scalable, and impactful than ever. With a track record of helping the [Life Sciences industry harness generative AI](https://aws.amazon.com/health/gen-ai/) to drive business value, Amazon Web Services (AWS) is now working with leading organizations like [Genentech](https://aws.amazon.com/solutions/case-studies/genentech-generativeai-case-study/) to deploy agents for use cases across research, clinical development, and commercialization.

### What have we learned?

In our experience helping customers build and launch agents for life sciences, we’ve observed the following challenges:

1. Building and testing agents, in particular multi-agent workflows that are tailored to specialized life sciences use cases, is time consuming for technical teams.
2. A knowledge gap exists between technical teams and functional leaders, due to technology evolving quickly, about how to best design agentic solutions with the most business impact. Cross-functional teams need the ability to co-develop and rapidly iterate to design a solution that delivers production-level quality and scale for user needs.
3. AI agents must adhere to strict data governance and operational security standards. IT teams are faced with ensuring data privacy and auditability—restricting agent actions to within authorized boundaries. They must also integrate with enterprise identity and access management (IAM) policies and existing business workflow constraints.

To address these challenges, and to encourage the democratization of agentic development across the healthcare and life sciences industry, AWS has introduced an [open-source toolkit](https://aws-samples.github.io/amazon-bedrock-agents-healthcare-lifesciences/) with key learnings for the benefit of the developer community.

### Streamlining Development with Starter Agents

The toolkit, built on [Amazon Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/), hosts a growing catalog of starter agents purpose-built for healthcare and life sciences use cases, and encompasses supervisor agents that can complete multi-agent workflows. It also includes a developer-facing UI component that can be used to securely assemble, test, and demonstrate multi-agent workflows within the organization’s VPC, helping to bridge the vision gap between IT and functional leads when designing agentic solutions.

The toolkit currently offers starter agents for common life sciences use cases including:

* **Research Agents –** For target identification, biomarker discovery, literature search, and experimental design
* **Clinical Agents –** To support clinical trial analysis, protocol optimization, and patient stratification
* **Commercial Agents –** For competitive intelligence and market insights generation

The toolkit also offers agents designed in collaboration with industry leaders. For example [Wiley](https://newsroom.wiley.com/press-releases/press-release-details/2025/Wiley-Announces-Collaboration-With-Amazon-Web-Services-AWS-to-Integrate-Scientific-Content-Into-Life-Sciences-AI-Agents/default.aspx), one of the world’s largest publishers and a trusted leader in research, released a new agent able to search full-text articles published under the creative commons license, such as *Cancer Medicine*. This delivers reliable and cited insights in minutes, rather than the current hours- to days-long manual process of discovering and perusing dozens of articles for relevant information.

These pre-built agents serve as a foundation, saving developers and subject matter experts valuable time by eliminating the need to build agents from scratch. Individual agents can be dynamically attached to a multi-agent supervisor by using the [multi-agent collaboration capability on Amazon Bedrock](https://aws.amazon.com/blogs/aws/introducing-multi-agent-collaboration-capability-for-amazon-bedrock/). This enables developers to orchestrate across agents to build new agentic workflows

By breaking down complex tasks into manageable steps while providing transparent reasoning processes and execution paths, these agents help build trust with stakeholders, such as research leaders.

### Customization and Scalability

A compelling feature of agents is the ability to access and integrate dynamic resources, both internal and external, to gain a comprehensive perspective. Recognizing that each organization will have unique requirements for data integration and persona-driven workloads, the toolkit’s starter agents are designed for streamlined customization and orchestration. Organizations can tailor these agents to fit specific workflows and evolve them over time to meet changing requirements. Whether dealing with structured, unstructured, or graph data, the agents can integrate seamlessly with AWS services like [Amazon SageMaker](https://aws.amazon.com/sagemaker/?gclid=Cj0KCQjwrPHABhCIARIsAFW2XBMJvMGHAlloNCZBO-pijtvfxZnVc0GQr2sdemQShghSANnWmVrHU20aAgSNEALw_wcB&trk=b6c2fafb-22b1-4a97-a2f7-7e4ab2c7aa28&sc_channel=ps&ef_id=Cj0KCQjwrPHABhCIARIsAFW2XBMJvMGHAlloNCZBO-pijtvfxZnVc0GQr2sdemQShghSANnWmVrHU20aAgSNEALw_wcB:G:s&s_kwcid=AL!4422!3!651751060692!e!!g!!amazon%20sagemaker!19852662230!145019225977&gad_campaignid=19852662230), APIs, and specialized foundation models deployed on AWS.

Built on Amazon Bedrock, these agents leverage [best practices for robust agentic AI applications](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/), confirming a future-ready foundation that can adapt to emerging challenges and opportunities. All of this can be done while achieving [responsible development of AI](https://aws.amazon.com/ai/responsible-ai/) agents.

### Advanced Technical Capabilities

From a technical standpoint, the toolkit offers several advanced features:

* **Multi-agent Orchestration:** Coordinate multiple agents, build custom supervisors, and select and combine agents at runtime to handle complex tasks efficiently.
* **Evaluation and Observability:** Monitor agent performance with tailored metrics, assess complete goal accuracy, and facilitate continuous improvement.
* **Seamless Deployment:** Utilize one-click templates or Jupyter notebooks to deploy solutions directly into your AWS account within minutes.
* **Model Context Protocol (MCP) Support:** Standardize interactions with external systems using tools built with AWS Lambda [MCP Server](https://awslabs.github.io/mcp/servers/lambda-mcp-server/).

These capabilities enable organizations to develop sophisticated AI applications that can address a wide range of challenges in life sciences research and operations.

### Getting Started with Healthcare and Life Sciences Agents on AWS

It’s quick for developers to get started:

![Demonstration of Agents Catalog](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/05/15/agents_toolkit_overview_revised.gif)

Once the application has been deployed in your VPC, you’re ready to take the following steps to start building agents for your organization:

1. **Browse the catalog:** Users can explore a [catalog](https://github.com/aws-samples/amazon-bedrock-agents-healthcare-lifesciences/tree/main/agents_catalog) of starter agents, including Individual agents for research, clinical development, and commercial use cases. There are also pre-built supervisor agents that orchestrate multiple agents in collaborative workflows.
2. **Configure multi-agent collaboration:** Users can select a custom combination of agents and define instructions for a supervisor agent—enabling dynamic orchestration at runtime.
3. **Invoke supervisor agents for task execution:** Whether using a pre-built or user-configured setup, supervisor agents can route and manage tasks using the multi-agent collaboration capabilities of Amazon Bedrock.
4. **Evaluate:** Evaluation tools enable users to assess the agents’ behavior based on task-specific metrics, such as goal completion, and large language model [(LLM)-as-a-judge](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html) based judging for subjective evaluation of outputs.

The following illustrates how you can quickly get started with the agents in the toolkit.

*[![High-level architecture of sample agents illustrating key capabilities](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/05/14/Figure-1-–-High-level-architecture.png)](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/05/14/Figure-1-%E2%80%93-High-level-architecture.png)Figure 1 – High-level architecture*

### Use Cases: Agents Across the Life Sciences Value Chain

The toolkit offers a diverse set of specialized starter and supervisor agents tailored to accelerate innovation in key areas of the life sciences value chain. Following, we have outlined real-world use cases and the types of agents available to support each domain.

**1. Research: Accelerating Target Identification and Biomarker Discovery**

Research scientists often face complex, manual processes when testing hypotheses, analyzing biomarkers, and synthesizing insights across heterogeneous data sources—from biomedical literature (such as, [PubMed](https://pubmed.ncbi.nlm.nih.gov/)) and scientific databases (for example, [Reactome](https://reactome.org/)) to proprietary research data.

To address these challenges, we’ve extended our work on [cancer biomarker discovery](https://aws.amazon.com/blogs/machine-learning/accelerate-analysis-and-discovery-of-cancer-biomarkers-with-amazon-bedrock-agents/) to build a discovery pipeline orchestrated by the *Biomarker Discovery Supervisor Agent*. It decomposes complex analysis tasks and coordinates a team of specialized agents across four key capability areas.

**Multi-Modal Data Integration:** Process and correlate various patient data modalities to provide a comprehensive biomedical perspective.

* *Biomarker Database Analyst Agent:* Analyzes structured clinical and RNA-seq data
* *Variant Interpreter Agent:* Interprets genetic variant annotations
* *Medical Imaging Agent:* Processes CT scans using asynchronous workflows
* *Pathology Agent:* Analyzes Whole Slide Images (WSIs) for pathology interpretation
* *Radiology Report Agent:* Validates Chest X-ray findings based on ACR guidelines

**Data Enrichment:** Link data entities to external biological knowledge bases.

* *Biological Pathways Agent:* Explores molecular interactions and signaling processes through the Reactome graph
* *Omics Signature Agent:* Enriches entities using databases like OMIM, ENSEMBL, and UniProt

**Evidence Research:** Retrieve and summarize insights from scientific literature.

* *Clinical Evidence Researcher Agent:* Searches PubMed and internal knowledge bases
* *Wiley Online Library Agent:* Performs full-text search through the Wiley API

**Statistical Analysis:** Analytic and visualization support for research insights.

* *Statistician Agent:* Performs survival regression and creates Kaplan-Meier and descriptive plots using python lifelines library

Translational scientists can also orchestrate these capabilities into a complete analysis pipeline using a supervisor agent.

**2. Clinical Development: Protocol Design and Trial Planning**

Developing clinical protocols is a complex, multi-disciplinary effort involving stakeholders such as researchers, CROs, and regulatory specialists. Many steps rely on reusing prior clinical trial designs, referencing best practices, and aligning across systems. To streamline this process, the Clinical Trial Protocol Assistant leverages a team of specialized subagents to:

* Analyze historical trials
* Recommend clinical trial design strategies
* Support collaborative protocol drafting

**Key Agents:**

* *Clinical Study Search Agent:* Retrieves data from [ClinicalTrials.gov](https://clinicaltrials.gov/), helping users explore prior study designs by condition, intervention, or sponsor. It highlights eligibility criteria, endpoints, and outcome measures from past trials.
* *Clinical Trial Protocol Generator Agent:* Builds new study protocols using best practices and the Common Data Model (CDM). It assists in drafting and refining sections, such as inclusion/exclusion criteria, endpoints, and statistical plans.

Development teams can iteratively co-create protocols, integrating feedback and evolving the design in real-time with AI-assisted guidance.

**3. Commercial: Real-Time Competitive Intelligence**

Life Sciences companies must stay ahead of rapid market developments—from clinical breakthroughs to mergers and acquisitions (M&A) activity. Historically, this required manual effort from analysts or consultants, which is time-consuming and expensive. The *Competitive Intelligence Agent* on Amazon Bedrock helps automate this process by orchestrating specialized subagents that monitor and analyze public data sources.

**Key Agents:**

* *Web Search Agent:* Uses the Tavily API to retrieve relevant, filtered news and web content with built-in content guardrails
* *USPTO Search Agent:* Queries patent filings by topic or assignee using the USPTO Open Data API
* *SEC 10-K Agent:* Extracts financial insights and trends from company filings

The resulting analyses provide actionable intelligence across the organization. Sales teams can prepare for provider discussions by understanding recent activity and executives can make data-driven strategic decisions on partnerships, investments, or competitive threats.

### Conclusion: From Idea to Impact

We introduced the open-source Healthcare and Life Sciences Agentic AI toolkit, which includes starter agents built on Amazon Bedrock. These agents demonstrate real-world capabilities like biomarker discovery, clinical protocol development, and competitive intelligence analysis. Each example is designed to inspire builders, streamline early experimentation, and shorten the time it takes to deliver business value with agentic AI.

The era of agentic AI is here—and AWS is your partner in transforming how life sciences organizations operate, innovate, and scale. With the right tools, infrastructure, and support, you can turn breakthrough ideas into business value faster than ever. Together, we can advance the responsible development of AI agents that solve meaningful challenges in healthcare and life sciences, and improve outcomes for patients, researchers, and clinicians alike.

Contact an [AWS Representative](https://pages.awscloud.com/BiotechandPharmaContactSales.html?languages=english) to know how we can help accelerate your business.

### Learn more

* [Evaluate Amazon Bedrock Agents with Ragas and LLM-as-a-judge](https://aws.amazon.com/blogs/machine-learning/evaluate-amazon-bedrock-agents-with-ragas-and-llm-as-a-judge/)
* [150 Models and Counting: Your Guide to Generative AI Models for Healthcare and Life Sciences](https://aws.amazon.com/blogs/industries/150-models-and-counting-your-guide-to-generative-ai-models-for-healthcare-and-life-sciences/)
* [Harness the power of MCP servers with Amazon Bedrock Agents](https://aws.amazon.com/blogs/machine-learning/harness-the-power-of-mcp-servers-with-amazon-bedrock-agents/)

![Brian Loyal](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2022/02/22/bike.jpg)

### Brian Loyal

Brian Loyal is a Senior AI/ML Solutions Architect in the Global Healthcare and Life Sciences team at Amazon Web Services. He has more than 16 years experience in biotechnology and machine learning and is passionate about helping customers solve genomic and proteomic challenges. In his spare time, he enjoys cooking and eating with his friends and family.

![Hasan Poonawala](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/01/06/Hasan-Poonawala.png)

### Hasan Poonawala

Hasan Poonawala is a Senior AI/ML Specialist Solutions Architect at AWS, working with Healthcare and Life Sciences customers. Hasan helps design, deploy and scale generative AI and machine learning applications on AWS. He has 15+ years of combined work experience in machine learning, software development and data science on the cloud. In his spare time, Hasan loves to explore nature and spend time with friends and family.

![Nadeem Bulsara](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2023/10/10/nadeem_photo_rev.png)

### Nadeem Bulsara

Nadeem Bulsara is a Principal Solutions Architect at AWS specializing in Genomics and Life Sciences. He brings his 13+ years of Bioinformatics, Software Engineering, and Cloud Development skills as well as experience in research and clinical genomics and multi-omics to help Healthcare and Life Sciences organizations globally. He is motivated by the industry’s mission to enable people to have a long and healthy life.

![Shamika Ariyawansa](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/05/14/Shamika-Ariyawansa.jpg)

### Shamika Ariyawansa

Shamika Ariyawansa, serving as a Senior AI/ML Solutions Architect in the Global Healthcare and Life Sciences division at Amazon Web Services (AWS), specializes in Generative AI. He assists customers in integrating Generative AI into their projects, emphasizing the adoption of Large Language Models (LLMs) for healthcare and life sciences domains with a focus on distributed training. Beyond his professional commitments, Shamika passionately pursues skiing and off-roading adventures.

Loading comments…

### Resources

* [AWS for Industry](https://aws.amazon.com/industries?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)
* [AWS Events](https://aws.amazon.com/events?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)
* [AWS Training & Certification](https://aws.amazon.com/training/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)
* [AWS Whitepapers](https://aws.amazon.com/whitepapers/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)
* [AWS Compliance Reports](https://aws.amazon.com/artifact/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-social)

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