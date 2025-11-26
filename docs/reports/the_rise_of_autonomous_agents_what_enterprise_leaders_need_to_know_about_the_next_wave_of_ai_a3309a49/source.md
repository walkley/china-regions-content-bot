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

## [AWS Insights](https://aws.amazon.com/blogs/aws-insights/)

# The rise of autonomous agents: What enterprise leaders need to know about the next wave of AI

by Sri Elaprolu on 13 JUN 2025 in [Amazon Q Developer](https://aws.amazon.com/blogs/aws-insights/category/amazon-q/amazon-q-developer/ "View all posts in Amazon Q Developer"), [Artificial Intelligence](https://aws.amazon.com/blogs/aws-insights/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Best Practices](https://aws.amazon.com/blogs/aws-insights/category/post-types/best-practices/ "View all posts in Best Practices"), [Featured](https://aws.amazon.com/blogs/aws-insights/category/featured/ "View all posts in Featured"), [Generative AI](https://aws.amazon.com/blogs/aws-insights/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Generative AI](https://aws.amazon.com/blogs/aws-insights/category/generative-ai-2/ "View all posts in Generative AI"), [Thought Leadership](https://aws.amazon.com/blogs/aws-insights/category/post-types/thought-leadership/ "View all posts in Thought Leadership") [Permalink](https://aws.amazon.com/blogs/aws-insights/the-rise-of-autonomous-agents-what-enterprise-leaders-need-to-know-about-the-next-wave-of-ai/)  [Comments](https://aws.amazon.com/blogs/aws-insights/the-rise-of-autonomous-agents-what-enterprise-leaders-need-to-know-about-the-next-wave-of-ai/#Comments)  Share

![Autonomous AI](https://d2908q01vomqb2.cloudfront.net/b7103ca278a75cad8f7d065acda0c2e80da0b7dc/2025/06/04/AUTONOMOUS-AI.png)

Autonomous AI agents represent the next significant evolution in artificial intelligence, moving beyond conversational interfaces to systems that leverage AI to reason, plan, and complete tasks in tandem with – or on behalf of humans – like compiling research, paying bills, planning a trip or managing enterprise applications.

Use of autonomous agents is rapidly maturing and reaching a tipping point in enterprise adoption, enabled by cost effective foundational models with advanced reasoning capabilities, secure data infrastructure, and emergence of development tools. Enterprise leaders face tremendous opportunities and significant organizational challenges as these AI agents transition from experimental technology to core business infrastructure.

## Understanding autonomous AI agents: beyond simple automation

Just like autonomous driving has progressed from Level 1 (cruise control) to Level 4 (full autonomy in specific domains), the level of agency of AI agents is growing.

* **Level 1 – Chain**: Rule-based robotic process automation (RPA) where both actions and their sequence are pre-defined. Example: Extracting invoice data from PDFs and entering it into a database.
* **Level 2 – Workflow**: Actions are pre-defined, but the sequence can be dynamically determined using routers or Large Language Models (LLMs). Example: Drafting customer emails or running Retrieval Augmented Generation (RAG) pipelines with branching logic.
* **Level 3 – Partially autonomous**: Given a goal, the agent can plan, execute, and adjust a sequence of actions using a domain-specific toolkit, with minimal human oversight. Example: Resolving customer support tickets across multiple systems.
* **Level 4 – Fully autonomous**: Operates with little to no oversight across domains, proactively sets goals, adapts to outcomes, and may even create or select its own tools. Example: Strategic research agents that discover, summarize, and synthesize information independently.

As of Q1 2025, most agentic AI applications (AI systems that can act autonomously) remain at Level 1 and 2, with a few exploring Level 3 within narrow domains and a limited number of tools (generally under 30). What distinguishes truly autonomous agents is their capacity to reason iteratively, evaluate outcomes, adapt plans, and pursue goals without ongoing human input.

## The economic impact: market projections and business transformation

Based on [McKinsey](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier) estimates, generative AI (gen AI) is projected to contribute between $2.6 and $4.4 trillion annually to global GDP. This is coming to life with the use of autonomous agents, with [Gartner](https://www.gartner.com/en/articles/intelligent-agent-in-ai) projecting that at least 15 percent of work decisions will be made autonomously by agentic AI by 2028, as compared to 0 percent in 2024. The AI agents market itself is expected to [grow to $52.6 billion](https://www.marketsandmarkets.com/Market-Reports/ai-agents-market-15761548.html?gad_source=1&gbraid=0AAAAADxY7SzIPNP1hoRzTlxwgvEWX-gBz&gclid=Cj0KCQjw_JzABhC2ARIsAPe3ynrmv6gaz5kYEVUU53zfXP8Gc1nWppnfsJ93QCjcAmQbNW3BZHb-9qAaAklmEALw_wcB) by 2030, reflecting a compound annual growth rate of around 45 percent.

All these estimates reflect not just enthusiasm, but a growing enterprise conviction in agentic AI’s tangible capabilities. Organizations are showing significant interest in agentic AI, with [over 50 percent](https://www2.deloitte.com/content/dam/Deloitte/us/Documents/consulting/us-state-of-gen-ai-q4.pdf) identifying it as a priority area within gen AI development. While there might be skepticism about whether this represents a temporary trend, evidence suggests this growth is sustainable. Companies are progressing beyond experimental phases and implementing these solutions in real-world operations, achieving tangible benefits in three key areas: improved productivity, reduced costs, and faster innovation cycles. For example:

* **Innovation and research agents**: [Genentech](https://aws.amazon.com/solutions/case-studies/genentech-generativeai-case-study/), a U.S.-based biotechnology company, built an agentic solution on AWS that automates time-consuming manual search process, enabling their scientists to focus on high-impact research and accelerate drug discovery innovation. The system uses autonomous agents that can break down complicated research tasks into dynamic, multi-step workflows. Unlike traditional automation systems that follow predetermined paths, these agents adapt their approach based on information gathered at each step, access and analyze multiple knowledge bases using RAG, and execute complex queries by interfacing with Genentech internal APIs and databases. This agentic solution will help Genentech automate much of the manual effort required for biomarker validation across therapeutic areas, reducing the time-to-target identification, and accelerating innovation.
* **Workplace productivity agents**: Amazon accelerated developer productivity for legacy application modernization by deploying agents using [Amazon Q Developer](https://aws.amazon.com/q/developer/). One of the most powerful capabilities of Amazon Q Developer is automating Java version upgrades to transform Java applications. In 2024, Amazon integrated the Java transformation capability into Amazon’s internal systems and migrated tens of thousands of production applications from older versions of Java 8 or 11 to Java 17. This effort allowed developers to complete these upgrades in a fraction of the time, and resulted in both performance improvements and costs savings across Amazon.
* **Business workflow agents**: U.S.-based [Rocket Mortgage](https://aws.amazon.com/blogs/machine-learning/enabling-complex-generative-ai-applications-with-amazon-bedrock-agents/) needed a more personalized and efficient approach to navigating home ownership. Rocket developed an AI-powered support system using Amazon Bedrock Agents, creating an intelligent platform that aggregated 10 petabytes of financial data and provides tailored mortgage recommendations and real-time personalized financial guidance. The results are faster query resolution, improved personalization accuracy, and enhanced customer experience in navigating complex home financing processes.

## Tools or teammates? The future of human-AI collaboration

Beyond economic projections, autonomous agents represent a deeper transformation in how work is structured and value is created. At the core of this shift is the emergence of the “human-AI partnership” — a reimagining of the “human-in-the-loop” paradigm. While both humans and agents are capable of generating ideas, making decisions, and adapting to new inputs, they do so in fundamentally different ways. Humans bring lived experience, moral reasoning, and intuitive creativity — often grounded in ambiguity and emotion. Agents, by contrast, excel at tireless execution, statistical pattern recognition, and goal-directed autonomy at scale.

The question then emerges: Are autonomous agents merely tools, or are they evolving into teammates? One might argue that agents remain tools, lacking consciousness, intentionality, or moral responsibility. However, functionally, their capacity to act autonomously, maintain persistent goals, and coordinate with other agents introduces a new operational reality, where they do behave like teammates. While agents themselves lack moral agency, the consequences of their actions often exhibit moral behavior — behavior shaped by the human architects who design their objectives, constraints, and ethical guardrails. The critical question we need to ponder: Where do humans still add irreplaceable value for cognitive tasks? The answer will increasingly depend on context. In high-stakes domains such as healthcare, legal interpretation, or policymaking – human judgment, empathy, and ethical reasoning remain irreplaceable. In domains like logistics or IT automation – oversight, exception handling, and system design will still rely heavily on human expertise.

We will have a rebalancing of roles, where humans focus on supervising complex workflows, shaping objectives, and ensuring responsible outcomes. Skill development will become essential as success in the workplace may increasingly depend on agent literacy — the ability to supervise, collaborate with, and strategically direct agent teams, much like working with human teammates today. While this may lead to the emergence of some new roles, especially in AI governance, it will more often involve the evolution of existing roles. For instance, customer support leads might oversee multi-agent service systems, and business analysts could additionally be AI outcome evaluators. The challenge for enterprises is to build systems, policies, and cultures where this new form of collaboration can thrive.

## Ethics in the world of autonomous agents

The successful adoption of autonomous agents requires deliberate attention to governance and ethics. As AI agents take on more decision-making responsibility, organizations must establish clear ethical guidelines—especially in contexts involving customer data, finances, or sensitive operations. What makes this really important is the expectation gap: Users often demand perfection from technology, in this case AI agents, while accepting imperfection in humans. This high bar for AI agents can erode trust even if agents make errors at a far smaller scale than humans. [Explainability](https://royalsocietypublishing.org/doi/10.1098/rsta.2020.0363) and interpretability play a crucial role in bridging this gap. Humans are more likely to accept an AI decision if it comes along with an explanation that mimics human reasoning and moral principles.

Accountability and privacy are two critical aspects here as level of agency rises.

**Accountability** (who is responsible): As agents evolve from tools to teammates, the notion of accountability will likely evolve the most – it will not be eliminated, but redistributed (we will likely never say the AI agent is responsible). Enterprises will need a shared responsibility framework where each stakeholder is accountable for the part of the system they control. As agent autonomy increases, this “accountability stack” becomes even more critical — and must be explicitly defined and documented, such as via a Responsible, Accountable, Consulted, and Informed (RACI) matrix or governance policy. For example:

* ML engineers are responsible for ensuring models are fine tuned on unbiased data
* Developers and MLOps teams are responsible for making sure correct data permissions are set and guardrails are integrated
* Business owners and product teams are responsible for approving solutions for use after rigorous testing

Traceability will be a key enabler to ensure that root cause analysis can be done when agents do not behave as intended.

**Privacy** (who gets to see my data): While autonomous agents inherit traditional privacy controls like IAM based access, their dynamic behavior introduces new risks. Agents can make real-time decisions, synthesize data across contexts, and potentially repurpose information in ways that violate principles like data minimization and purpose limitation under regulations like General Data Protection Regulation (GDPR) in the European Union. Enterprises must go beyond static access controls—embedding context-aware guardrails, runtime minimization, and traceability to ensure agents act within privacy boundaries.

## Leadership imperatives: The CIO’s role as an enabler of agentic innovation

As autonomous AI agents blur the lines between tools and teammates, enterprises will need to fundamentally rethink how they govern and collaborate with these agents. In this shift, the Chief Information Officer (CIO) is uniquely positioned to evolve into the enterprise’s key orchestrator of agentic value.

We’ve often heard the analogy that IT will “[become the HR of AI agents](https://fortune.com/2025/01/09/nvidia-ceo-jensen-huangt-take-over-hr-ai-agents/).” While this may be oversimplified, it does hint at a future where CIOs are responsible not just for deploying technology but for curating, coordinating, and governing fleets of autonomous agents across the organization. The most successful implementations will empower departments — marketing, operations, finance — to tailor agents to their needs while operating within shared guardrails for governance, security, and data integrity.

This is where the CIO’s role becomes critical — not as a gatekeeper, but as an enabler of decentralized agentic innovation. Here are a few key actions that CIOs should consider taking to be the enabler for agentic innovation in their organization:

1. **Develop a business-led strategic roadmap for AI agent implementation,** starting with basic automation and progressively moving toward more autonomous systems – but ensure this roadmap includes clear governance frameworks and accountability structures from the start.
2. **Position yourself as the key orchestrator of human-AI collaboration**, focusing on integrating AI agents as teammates rather than tools, while driving the necessary cultural change and skill development across the organization.
3. **Establish robust security and privacy controls** that go beyond traditional methods, specifically designed for the dynamic nature of autonomous agents.
4. Finally, and perhaps most critically, **balance innovation with control** by enabling decentralized AI adoption across departments while maintaining consistent standards and guardrails.

**Learn more:**

[Contact us](https://aws.amazon.com/contact-us/) to learn more about evaluating if your organization is set up to work with autonomous agents as teammates, or if you’d like to dive deeper into skill development and risk posture for your agentic AI plans.

Learn more about the [GenAI Innovation Center](https://aws.amazon.com/ai/generative-ai/innovation-center/) and how we are accelerating agentic AI adoption across organizations.

*Many thanks to contributors to this post: Shuja Sohrawardy (Sr. Manager, GenAI Strategy, AWS) and Anurag Bhagat (Sr. GenAI Strategist, AWS).*

![Sri Elaprolu](https://d2908q01vomqb2.cloudfront.net/b7103ca278a75cad8f7d065acda0c2e80da0b7dc/2025/06/04/sri.jpg)

### Sri Elaprolu

Sri Elaprolu is a technology leader with over 25 years of experience spanning artificial intelligence, machine learning, and software engineering. As Director of the AWS Generative AI Innovation Center, Sri leads a global team of ML scientists and engineers applying the latest advances in generative AI to solve complex challenges for enterprises and the public sector.

Loading comments…

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