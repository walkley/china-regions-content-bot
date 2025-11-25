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

## [Migration & Modernization](https://aws.amazon.com/blogs/migration-and-modernization/)

# AWS Agentic AI Options for migrating VMware based workloads

by Shiva Vaidyanathan and Mike Kuznetsov on 04 JUN 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/migration-and-modernization/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Bedrock Agents](https://aws.amazon.com/blogs/migration-and-modernization/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-bedrock-agents/ "View all posts in Amazon Bedrock Agents"), [AWS Application Migration Service](https://aws.amazon.com/blogs/migration-and-modernization/category/migration/aws-application-migration-service/ "View all posts in AWS Application Migration Service"), [AWS Transform](https://aws.amazon.com/blogs/migration-and-modernization/category/artificial-intelligence/generative-ai/aws-transform/ "View all posts in AWS Transform"), [Generative AI](https://aws.amazon.com/blogs/migration-and-modernization/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Migration](https://aws.amazon.com/blogs/migration-and-modernization/category/enterprise-strategy/migration-enterprise-strategy/ "View all posts in Migration") [Permalink](https://aws.amazon.com/blogs/migration-and-modernization/aws-agentic-ai-options-for-migrating-vmware-based-workloads/) Share

AWS offers several generative AI services that transform VMware workload migrations into a streamlined, automated process. By using agentic AI technology, organizations can now accelerate their cloud journey while maintaining operational excellence and reducing risk.

AI powered migration tools can assess your on-premises servers in VMWare environments to map complex application dependencies, recommend optimized resource allocations, and generate precise cloud migration plans. This automation reduces planning time while improving accuracy. During the mobilize phase, the agents can translate on-premises architectures to AWS native constructs. This helps to identify the more efficient configuration of VPCs, security groups, and network connectivity. Finally, during the migration process, agents can orchestrate complex migration workflows such as replication, testing, and coordinated cutover processes using AWS Application Migration Service (MGN). This advanced automation helps organizations to migrate complex and mission-critical workloads with precision and reliability.

In this blog, we explore different agentic AI solutions from AWS for use during the migration of VMware workloads. Specifically we will explore features from both [AWS Transform for VMware](https://aws.amazon.com/transform/vmware/) and [Amazon Bedrock multi-agent collaboration](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html). Considering VMware based workloads as our primary example, we’ll demonstrate how these tools can accelerate the overall migration process. While our focus is on VMware based workloads, you can also use these services for general-purpose non-VMware workload migrations as well.

## Key Concepts

1. [Bedrock Knowledge Base](https://aws.amazon.com/bedrock/knowledge-bases/) : A collection of relevant information and documentation attached to agents that provides domain-specific expertise for their assigned tasks (like migration templates, best practices, or technical guidelines).
2. [Bedrock Action Groups](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html) : Configuration settings that enable agents to perform specific tasks or operations within their domain of expertise.
3. [Bedrock Supervisor Agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html) : The primary orchestrating agent that analyzes requests, coordinates tasks, and manages communications between specialized sub-agents to deliver comprehensive solutions.
4. [Bedrock Collaborative Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html) : Specialized sub-agents with specific expertise that work together under a supervisor agent’s coordination to handle complex multi-step tasks.
5. [Bedrock Collaborative Modes](https://aws.amazon.com/blogs/aws/introducing-multi-agent-collaboration-capability-for-amazon-bedrock/) : Bedrock offers two types of collaborative modes – a Supervisor mode for complex orchestration across multiple agents, and a Supervisor with routing mode that efficiently handles simple requests by directly routing them to specialized agents while maintaining full supervisory capabilities for complex tasks.
6. [Transformation Job](https://aws.amazon.com/transform/vmware/) : An automated process within AWS Transform that analyzes VMware infrastructure and generates AWS-equivalent configurations and migration plans.
7. [Model Context Protocol (MCP) Servers](https://aws.amazon.com/blogs/machine-learning/harness-the-power-of-mcp-servers-with-amazon-bedrock-agents/) : MCP servers act as standardized intermediaries that enable Large Language Models to securely connect with and utilize external tools and data sources through a unified protocol. A suite of specialized MCP servers that help you get the most out of AWS, wherever you use MCP can be found [here](https://awslabs.github.io/mcp/).

## Agentic AI Migration Options for VMware based workloads

### Option 1 : AWS Transform

Figure 1 shows steps to assess your VMware environment and migrate it to AWS via AWS Transform. AWS Transform streamlines the migration assessment process by analyzing on-premises servers using data from RVTools, AWS Migration Portfolio Assessment ([MPA](https://mpa.accelerate.amazonaws.com/)), or [Migration Evaluator](https://aws.amazon.com/migration-evaluator/) exports. It generates a comprehensive assessment for x86 servers and Windows licensing. The workflow includes an interactive chat feature that explains the assessment output in detail. This detail includes insights into how recommendations were made which helps you to understand specific aspects of the migration plan. The workflow helps you to create full transformation plans without any complex infrastructure setup.

![Diagram illustrating the VMware migration assessment workflow using AWS Transform. The process begins with data collection from on-premises environments using RVTools. AWS Transform Assessment performs the analysis to generate a business case and TCO. It then helps you generate a wave , do network converstion and VM migration and deployment.](https://d2908q01vomqb2.cloudfront.net/1f1362ea41d1bc65be321c0a378a20159f9a26d0/2025/06/01/Screenshot-2025-06-01-at-10.35.14 AM-1024x574.png)

Figure 1: Migrating VMware workloads using AWS Transform

To set up AWS Transform for VMware, you will need an inventory of your on-premises components. This can be done using collectors or file imports to get a comprehensive view of the VMware footprint using aforementioned tooling such as RVTools, MPA files, or Migration Evaluator exports. If you are working with a VMware NSX environment, you must follow the specific steps for exporting network configuration data using Import/Export for NSX. Once this is done, AWS Transform provides an AI-driven web interface where you can interact with autonomous generative AI agents to create transformation plans. The system automates the conversion of VMware networking configurations to AWS constructs (VPCs, subnets, security groups), generates EC2 sizing recommendations, and creates comprehensive migration plans. You can review and edit these plans through the collaborative web interface and then initiate server migration using AWS Application Migration Service (MGN). The platform includes dashboards for monitoring job progress and maintaining detailed work logs of all migration activities. The AWS Transform for VMware [blog](https://aws.amazon.com/blogs/migration-and-modernization/new-capabilities-in-aws-transform-for-vmware/) provides detailed instructions for setup.

### Option 2 : Amazon Bedrock multi-agent collaboration

Figure 2 shows an example architecture with Amazon Bedrock multi-agent collaboration for migrations where specialized agents handle distinct aspects of the migration process. The system consists of a primary supervisor agent that coordinates with specialized sub-agents and Action groups. The sub-agents include portfolio assessment, infrastructure, migration orchestration, and operations. Each sub-agent has action groups associated to them focused on specific migration tasks. As an example, you can associate wave plan and sprint plan action groups with a portfolio agent. You can associate a design document, infrastructure as code templates (IaC), and cost estimate action groups with an infrastructure agent. You can integrate these sub-agents with MCP servers that provide a standardized, secure way for Large Language Models (LLMs) to interact with external tools and data sources. This serves as a bridge between AI models and operational systems. Amazon S3 can be used to store all migration related information (RVTools exports, business decisions, migration process documentation.) An AWS Lambda function can be used to sync the information into Amazon Bedrock Knowledge Bases.

![diagram showing Amazon Bedrock multi-agent collaboration system for migrations, featuring a supervisor agent coordinating specialized sub-agents through action groups and MCP server integrations.](https://d2908q01vomqb2.cloudfront.net/1f1362ea41d1bc65be321c0a378a20159f9a26d0/2025/06/01/Screenshot-2025-06-01-at-10.37.37 AM-1024x743.png)

Figure 2: Migrating VMware workloads using Amazon Bedrock multi agents collaboration

To set up Amazon Bedrock multi-agent collaboration for migrations, start by creating specialized sub-agents through the agent builder workflow. Configure each agent with specific instructions and knowledge bases relevant to their migration expertise. These sub-agents are associated with a supervisor agent that is enabled for multi-agent collaboration. A specific collaborator name is given to each sub-agent with instructions defining their role in the migration process. The architecture includes an integrated trace and debug console for visualizing agent interactions. This framework enables efficient handling of both straightforward migration tasks and complex transformation scenarios that require sophisticated coordination between multiple specialized agents. For help with getting started, review the following blogs: [Portfolio Assessments Using Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/accelerate-migration-portfolio-assessment-using-amazon-bedrock/), [Infrastructure As Code Generation Using Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/using-amazon-bedrock-agents-to-interactively-generate-infrastructure-as-code/), [Account Vending Using Amazon Bedrock](https://aws.amazon.com/blogs/mt/modernizing-account-management-with-amazon-bedrock-and-aws-control-tower/) or [Multi-Agent Collaborative Capability Using Amazon Bedrock](https://aws.amazon.com/blogs/aws/introducing-multi-agent-collaboration-capability-for-amazon-bedrock/).

## Comparison

|  |  |  |
| --- | --- | --- |
|  | **AWS Transform for VMware** | **Amazon Bedrock multi-agent collaboration** |
| Primary Purpose | Automated assessment and migration planning tool specifically for VMware to AWS migrations | AI-powered multi-agent collaboration framework for complex migration and transformation tasks |
| Advantages | * 80x faster network configuration conversion * Automated self-service assessments * Single consolidated platform * Built-in cost optimization * Simplified wave planning * Integrated chat explanations * Historical tracking of decisions * Managed service, simplifies operational tasks | * Flexible agent specialization * Advanced reasoning capabilities * Supervisor/routing modes * Detailed tracing and debugging * Knowledge base integration * MCP Servers for integrating custom tools |
| Limitations | * Limited to VMware workloads * Fixed assessment types and analysis capabilities * Less flexible for custom scenarios * Primarily focused on rehosting | * Higher initial infrastructure setup complexity * Maximum three (3) hierarchical agent layers * Learning curve for agent configuration * Operational overhead in managing the Amazon Bedrock agent infrastructure and knowledge bases |
| Pricing | Core features—including assessment and transformation—at no cost. Check [AWS Transform Pricing](https://aws.amazon.com/transform/pricing/) for details | There is cost associated to Agents, Knowledge Base, Model in use. Check [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)for details |
| Use cases | * Standard VMware to EC2 rehost style migrations * Complex Migration tasks are workflow jobs * License optimizations including Windows licensing analysis * Cost analysis | * Complex migration scenarios * Custom tooling and complex workflows * Advanced dependency analysis * Complex modernization scenarios |

## Considerations

When selecting between AWS Transform for VMware and Bedrock Collaborative Agents, you should first evaluate the migration complexity and organization’s internal capabilities.

AWS Transform is ideally suited for customers undertaking straightforward VMware-to-AWS migrations who need rapid assessment (It takes 1-2 days when compared to 2-3 weeks), standardized planning, and automated infrastructure sizing. This platform can benefit organizations with limited cloud expertise, those requiring quick time-to-value, or teams focusing on rehosting scenarios with standard networking configurations and licensing requirements. Amazon Bedrock Collaborative Agents, conversely, is suited for organizations facing complex migration scenarios that demand specialized expertise across multiple domains. This includes situations requiring custom transformation patterns, intricate application dependencies, or complex modernization requirements. Organizations with mature cloud teams, those undertaking multi-phase transformations, or building reusable migration patterns will find the Amazon Bedrock multi-agent framework well aligned for their needs.

Enterprise customers with diverse workload portfolios may choose to implement both solutions. We recommend AWS Transform for VMware for an initial assessment to rehost VMware workload migrations. Amazon Bedrock multi-agent collaborative agents are recommended for more complex migration and modernization scenarios. These can include replatform or refactor patterns, and non-VMware based migration workloads.

## Conclusion

The introduction of AI-powered migration tools represents a significant advancement in cloud migration capabilities, offering organizations unprecedented efficiency and accuracy in their transformation journeys. [AWS Transform for VMware](https://aws.amazon.com/transform/) provides a solution for standard VMware migrations that includes the ability to translate VMware networking configurations to AWS constructs. This includes constructs such as VPCs, subnets, transit gateways, and internet gateways. Typical translation can be achieved within one hour. This is nearly [80 times](https://aws.amazon.com/about-aws/whats-new/2025/05/aws-transform-vmware-generally-available/) faster compared to the two work weeks taken with traditional, manual approaches. [Amazon Bedrock multi-agent collaboration](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html) extends these capabilities to handle more complex, custom migration scenarios. Organizations can maximize their migration success by strategically employing both solutions: using AWS Transform for VMware in rehost patterns and Bedrock multi-agent collaboration for modernization scenarios that require specialized expertise and custom approaches. This two-pattern approach provides comprehensive coverage of migration and modernization needs. In addition, this can help to create transformation efficiency while reducing risk across your migration portfolio.

![Shiva Vaidyanathan](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2022/03/03/Shiva-Vaidyanathan.jpeg)

### Shiva Vaidyanathan

Shiva Vaidyanathan is a Principal Cloud Architect at AWS. He provides technical guidance, design and leads complex customer migration and modernization intiatives ensuring their success on AWS. He focuses on building agents for migration and modernization use cases leveraging Generative AI making AWS cloud adoption simpler for everyone. Prior to joining AWS, he has worked on several NSF funded research initiatives on how to perform secure computing in public cloud infrastructures. He holds a MS in Computer Science from Rutgers University and a MS in Electrical Engineering from New York University.

![Mike Kuznetsov](https://d2908q01vomqb2.cloudfront.net/972a67c48192728a34979d9a35164c1295401b71/2022/12/13/Mike-suite-square-photo-400pdi.png)

### Mike Kuznetsov

Mike Kuznetsov is a Principal Migration and Modernization Solutions Architect at AWS. He works with large enterprise customers helping them to rehost and modernize applications at scale as they migrate to AWS. He enjoys solving complex technical challenges to unblock customer migrations. In his free time, he loves to spent time with his family and spark curiosity in his kids.

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