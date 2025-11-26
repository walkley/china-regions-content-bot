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

## [AWS Security Blog](https://aws.amazon.com/blogs/security/)

# AI lifecycle risk management: ISO/IEC 42001:2023 for AI governance

by Abdul Javid and Amber Welch on 13 MAY 2025 in [Artificial Intelligence](https://aws.amazon.com/blogs/security/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Best Practices](https://aws.amazon.com/blogs/security/category/post-types/best-practices/ "View all posts in Best Practices"), [Generative AI](https://aws.amazon.com/blogs/security/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Intermediate (200)](https://aws.amazon.com/blogs/security/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/security/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance") [Permalink](https://aws.amazon.com/blogs/security/ai-lifecycle-risk-management-iso-iec-420012023-for-ai-governance/)  [Comments](https://aws.amazon.com/blogs/security/ai-lifecycle-risk-management-iso-iec-420012023-for-ai-governance/#Comments)  Share

As AI becomes central to business operations, so does the need for responsible AI governance. But how can you make sure that your AI systems are ethical, resilient, and aligned with compliance standards?

ISO/IEC 42001, the international management system standard for AI, offers a framework to help organizations implement AI governance across the lifecycle. In this post, we walk through how ISO/IEC 42001 enables effective AI governance, review the risk management requirements, and explore how you can use threat modeling as a practical technique to meet those expectations.

## AI governance

AI governance refers to the organizational structures, policies, and controls that enable AI systems to be used responsibly, ethically, and safely. Governance spans the entire AI lifecycle and includes the following activities:

* Setting the intended purpose and stakeholder alignment
* Managing data, models, and deployment risks
* Designing in explainability, bias mitigation, and traceability
* Establishing accountability, monitoring, and decommissioning practices

These activities are the foundation of a formal framework that you can use to establish governance processes, identify and manage risk, and implement processes for continuous improvement

## AI lifecycle

While ISO 42001 provides a framework for AI governance, ISO/IEC 22989:2022 describes what an AI system is and how it evolves. Governance should be implemented at every stage of the AI lifecycle to manage AI risks effectively. According to the ISO/IEC 22989:2022 standard, an organization’s AI life cycle might include these stages:

1. **Inception**: Identifying needs, goals, and feasibility
2. **Design and development**: Defining system architecture, data flows, and training models
3. **Verification and validation**: Testing and confirming that the system meets requirements and performs as intended
4. **Deployment**: Releasing the system into its operational environment
5. **Operation and monitoring**: Running the system, logging activity, and monitoring performance and outcomes
6. **Re-evaluation**: Assessing whether the system continues to meet objectives under changing conditions
7. **Retirement**: Decommissioning the system and addressing long-term data and access risks

Understanding the AI lifecycle, shown in Figure 1 that follows, is critical for identifying and mitigating AI risks. While these seven stages are provided directly in ISO 22989:2022, your organization might define its AI lifecycle stages differently to suit its business context. We refer to these stages as we explore the components of an AI management system, from initial AI system scoping, through threat monitoring and risk assessment, to monitoring the established governance program.

![Figure 1: Example of AI system lifecycle model stages and high-level processes based on ISO/IEC 22989:2022](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/12/AI-lifecycle-risk-management-1.png)

Figure 1: Example of AI system lifecycle model stages and high-level processes based on ISO/IEC 22989:2022

## Risk management in ISO/IEC 42001:2023

After an organization has identified and assessed AI risks (Clause 6.1 of ISO/IEC 42001:2023), operational controls to mitigate those risks must be implemented (Clause 8.2), and those controls and the AI system itself should be continuously monitored, documented, and improved (Clauses 9 and 10). AI impact assessments (AIIAs) are critical in high-risk use cases, complementing baseline risk assessments by focusing on societal, ethical, and legal impacts. AIIAs are like data protection impact assessments (DPIAs) for high-risk personal data processing under many privacy regulations. DPIAs are specifically designed to assess risks to individuals’ privacy and data protection rights under laws such as the GDPR. While AIIAs help organizations maintain responsible AI governance, DPIAs can be used in parallel to help verify that AI systems comply with data protection laws, together providing a holistic view of risks and safeguards across both ethical and legal dimensions.

You are free to select the AIIA tools or methodologies that best fit your use case. Two widely accepted frameworks are:

* ISO 31000: A general-purpose enterprise risk management standard that helps identify, evaluate, and treat risks in a structured and repeatable way. It aligns well with organizations seeking to embed AI risk into their broader enterprise risk management (ERM) programs.

* NIST AI Risk Management Framework (AI RMF): A NIST framework specifically designed for AI systems. It introduces tailored concepts such as explainability, robustness, fairness, and accountability, with actionable guidance organized into four core functions: Map, measure, manage, and govern.

ISO 42001 provides structured methods to conduct risk and impact assessments. Threat modeling tools such as:

* STRIDE (spoofing, tampering, repudiation, information disclosure, denial of service, and elevation of privilege). STRIDE aims to make sure that a system meets security requirements for confidentiality, integrity and availability.
* DREAD (damage potential, reproducibility, exploitability, affected users, and discoverability) is a framework that can assess severity of individual threats.
* OWASP (Open Worldwide Application Security Project) for machine learning (ML) enables analysis of AI system vulnerabilities, adversarial risks, and privacy threats.

Trustworthy AI is the result of strategic governance, structured methodologies, and technical analysis.

Figure 2 that follows shows the tiered structure of AI risk governance, moving from high-level governance to detailed technical assessments. On the left side, there’s a downward flow representing the increasing depth of controls, while the right side shows an upward scale indicating escalating AI risks.

* At the top layer, ISO/IEC 42001:2023 defines formal requirements for AI governance, including risk assessment mandates, control implementation, and lifecycle oversight.
* The middle layer features widely adopted risk assessment methodologies and frameworks, such as ISO 31000 and the NIST AI Risk Management Framework (RMF), which provide structured methods to identify, evaluate, and mitigate AI risks.
* At the base, are detailed threat modeling tools—including STRIDE, DREAD, PASTA, LINDDUN, and OWASP for ML—that support deep analysis of AI systems for vulnerabilities related to security, privacy, data protection, and adversarial threats.

Together, these layers form a comprehensive approach to AI risk governance, aligning strategic oversight with operational and technical defenses.

![Figure 2: A layered approach to AI risk management aligned with ISO/IEC 42001. ISO/IEC 42001 defines AI governance for responsible AI ](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/13/AI-lifecycle-risk-management-fig2.png)

Figure 2: A layered approach to AI risk management aligned with ISO/IEC 42001. ISO/IEC 42001 defines AI governance for responsible AI

## Threat modeling for AI risk identification

Threat modeling identifies AI lifecycle technical risks such as exploit surfaces, adversarial threats, and misuse scenarios that complement organizational risk analysis and impact assessments. This post takes a broader AI lifecycle view, showing you how threat modeling complements other risk strategies within the context of ISO/IEC 42001:2023. Additionally, AWS has published AI threat modeling guidance, such as:

* [Threat modeling your generative AI workload to evaluate security risk](https://aws.amazon.com/blogs/security/threat-modeling-your-generative-ai-workload-to-evaluate-security-risk)
* [How to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/)
* [How to assess the risk of AI systems](https://aws.amazon.com/blogs/machine-learning/learn-how-to-assess-risk-of-ai-systems/)

The following table is an example STRIDE threat model for a generative AI resource using AWS services by AI lifecycle stage and risk type. This illustrates technical threat remediation through AWS cloud native governance features.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **STRIDE category** | **Example threat** | **Lifecycle stage** | **Risk type** | **AWS feature for governance** |
| Spoofing | A fake identity uses the AI system to generate phishing emails or misinformation | Inception | Security | [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center) and [Amazon Cognito](https://aws.amazon.com/cognito) for multi-factor authentication (MFA), [Amazon GuardDuty](https://aws.amazon.com/guardduty) for threat detection |
| Tampering | A malicious prompt injection or API injection alters the model behavior or bypasses filters | Design development | Integrity | [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails), [Amazon API Gateway](https://aws.amazon.com/api-gateway) and [AWS WAF](https://aws.amazon.com/waf) rules, [AWS CloudTrail](https://aws.amazon.com/cloudtrail) for input auditing |
| Repudiation | Users deny prompt activity or content creation, and there’s no logging | Verification and validation | Accountability | CloudTrail, [Amazon Bedrock](https://aws.amazon.com/bedrock) invocation logs, [Amazon SageMaker ML Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html) for traceability |
| Information disclosure | Sensitive internal data—such as code or personally identifiable information (PII)—accidentally learned and reproduced by the large language model (LLM) | Operation and monitoring | Privacy, Security | [SageMaker Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html), [AWS VPC PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html), [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms) encryption, Amazon Bedrock data handling commitments |
| Denial of service | Bad actors overload the AI endpoint with prompt spam, degrading service | Deployment | Availability | [AWS Shield](https://aws.amazon.com/shield), API rate limiting using API Gateway, auto scaling with SageMaker endpoints |
| Elevation of privilege | An internal user modifies system prompts or updates to override content filters | Reevaluation | Ethics and access control | [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam) roles, Amazon Bedrock Guardrails, AWS Config, service control policies (SCPs) |

While [STRIDE](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) is used here for illustrative clarity, it’s just one of several threat modeling approaches that can be applied depending on the system context. Other widely recognized methods include:

* [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/): A threat-focused list targeting large language models
* [MITRE ATLAS](https://atlas.mitre.org/): A framework for adversarial threat modeling in AI/ML systems
* [NIST AI Risk Management Framework (AI RMF)](https://www.nist.gov/itl/ai-risk-management-framework): A United States standards-based approach focusing on trustworthy and responsible AI development
* [PASTA (Process for Attack Simulation and Threat Analysis)](https://threat-modeling.com/pasta-threat-modeling/): A risk-centric threat modeling methodology
* [LINDDUN](https://linddun.org/): A privacy threat modeling framework addressing data protection risks

By integrating these threat modeling practices into ISO/IEC 42001’s risk-based approach, organizations are not just “checking compliance boxes” they’re operationalizing trustworthy, secure, and accountable AI governance throughout the full system lifecycle.

## Threat modeling touchpoints across the AI lifecycle

ISO 42001:2023 uses the STRIDE threat modeling framework to align specific security threats to each stage. Each lifecycle stage is associated with particular threat types, relevant Annex references from the ISO standard, and examples of what to monitor.

* **Inception** (Annex A.8.1): Focuses on spoofing and fake identity input risks.
* **Design and Development** (Annex A.9.1): Linked to tampering threats.
* **Verification and Validation** (Annex A.7.1): Concerns around repudiation, such as lack of model decision logs.
* **Deployment** (Annex A.5.1): Addresses information disclosure vulnerabilities.
* **Operation and Monitoring** (Annex A.10.3): Maps to denial-of-service attacks.
* **Re-evaluation** (Annex A.8.6): Highlights risks of privilege escalation.

AI threat modeling isn’t a one-time task but must be applied continuously across each lifecycle stage, supported by ISO 42001’s annexes and STRIDE categories.

![Figure 3: An illustration of how organizations can use ISO/IEC 42001:2023 as a structured framework for AI risk management, using threat modeling as a key technique across the AI lifecycle](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/12/AI-lifecycle-risk-management-3.png)

Figure 3: An illustration of how organizations can use ISO/IEC 42001:2023 as a structured framework for AI risk management, using threat modeling as a key technique across the AI lifecycle

## AWS tools for AI governance and risk management

AWS governance service capabilities support the controls required in the Statement of Applicability (SoA) under ISO/IEC 42001. These services and features help organizations operationalize responsible AI practices at scale and align with ISO/IEC 42001’s emphasis on structured, accountable AI lifecycle management.

* [Amazon SageMaker Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html): Provides standardized documentation for ML models including purpose, performance, and limitations. In the governance context, model cards help maintain transparency, accountability, and auditability of model behavior and use.
* [Amazon SageMaker Clarify](https://aws.amazon.com/sagemaker-ai/clarify/): Detects bias in datasets and models and supports explainability of predictions. This directly supports governance controls related to fairness, non-discrimination, and explainability.
* [Amazon SageMaker Ground Truth](https://aws.amazon.com/sagemaker-ai/groundtruth/): Provides high-quality, human-in-the-loop data labeling workflows. It supports data governance by making sure labeled datasets are accurate, consistent, and traceable.
* [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/): Can be used to define safety filters for generative AI, such as avoiding toxic content or harmful outputs. This facilitates alignment with ethical and content governance policies.
* [AWS CloudTrail](https://aws.amazon.com/blogs/mt/auditing-generative-ai-workloads-with-aws-cloudtrail/) and [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/query-assistant.html): Enable audit logging and continuous monitoring of system changes. These are essential for accountability, traceability, and compliance reporting within AI governance frameworks.
* [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/), [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/), and [AWS PrivateLink](https://aws.amazon.com/privatelink/): IAM controls access, AWS KMS provides encryption and key management, and PrivateLink enables private connectivity. These features are critical for enforcing access governance, securing data, and maintaining privacy standards.
* [AWS Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html): A part of the AWS Well-Architected Framework tool. It provides structured guidance for evaluating and improving the design of generative AI systems. It helps organizations implement responsible AI practices, manage risks

## Conducting AI impact assessments for high risk use cases

While general risk assessments (Clause 6.1 of ISO/IEC 42001) are required for AI systems, ISO/IEC 42001 also calls for AIIAs in situations where the AI system poses high potential impact to individuals, groups, or society. AIIAs should result in a documented report of identified risks associated with the target AI activity, in addition to the severity of potential negative outcomes. These risks should be integrated into the AI management system (AIM) and monitored over time. Several stakeholders and specialists might need to provide input in the assessment process, such as legal, risk, compliance, data management, and security teams. Identified risks should be mitigated where possible, and a determination made about whether the residual risk is acceptable.

**AIIAs help answer questions such as:**

* Is the AI use justifiable, ethical, and proportionate?
* Could the system cause discrimination, exclusion, or loss of rights?
* What safeguards should be built to protect affected people?

**AIIA is required:**

* If the system makes or informs decisions that materially affect people
* If the system is deployed in sensitive domains (such as healthcare, finance, or public services)
* If risks to fundamental rights, fairness, or trust are flagged during initial risk assessments

**AIAA should cover:**

* Purpose and scope of the AI system
* Stakeholder and impact mapping
* Legal, ethical, and social risk evaluation
* Transparency and recourse mechanisms
* Recommendations for mitigation

### AIIA process workflow

Figure 4 that follows illustrates a generic AIIA workflow that includes initiating, scoping, assessing impact, planning mitigation, and documenting the outcome to evaluate how an AI system can affect individuals, groups, and society. Organizations can tailor this process to the AI system context, business objectives, and compliance requirements for their use case.

![Figure 4: Sample prescriptive process with key phases on conducting an AIIA](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/13/AI-lifecycle-risk-management-fig4.png)

Figure 4: Sample prescriptive process with key phases on conducting an AIIA

**AIIA outcome**

AIIA reports should capture the core purpose of the exercise: to evaluate how an AI system might affect individuals, communities, and society at large and to make sure that potential risks are addressed through appropriate mitigation strategies. While formats might vary across industries, an AIIA outcome typically includes key sections such as summary of system purpose, a mapping of affected stakeholders, a contextual analysis of legal and social factors, an evaluation of likely impacts (including fairness, bias, and autonomy risks) and a plan for a mitigation, oversight, and monitoring. Governance details such as sign off responsibility and reassessment triggers should also be included.

Whether you’re starting from scratch or adapting an existing template, these foundational elements will help make sure that your documentation supports transparency, accountability, and ethical AI deployment.

**Templates:**

* [AI Impact assessment template – Arxiv](https://arxiv.org/html/2407.17374v1#Sx4)
* [AI Algorithmic assessment tool – Government of Canada](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/algorithmic-impact-assessment.html)
* [Algorithmic impact assessment – Ada Lovelace Institute](https://www.adalovelaceinstitute.org/resource/aia-template/)

## Mapping AI lifecycle risks to ISO/IEC 42001 controls

After you have identified risks through techniques such as threat modeling and impact assessments, the next step is to make sure that they’re mitigated through the appropriate ISO/IEC 42001 controls. Using the lifecycle stages defined in ISO/IEC 22989:2022, you can map AI risks identified during the threat hunting process to the corresponding ISO/IEC 42001:2023 clauses and Annex A controls. This mapping helps you align your AI development and governance efforts with a standards-based risk framework.

| **AI lifecycle stage** | **Identified risk** | **Relevant ISO/IEC 42001 clauses** | **Risk mitigation – Annex A controls** |
| --- | --- | --- | --- |
| Inception | Spoofing: Impersonation | Clause 4, Clause 5 | A.6.1 (Governance roles), A.5.1 |
| Design and development | Tampering: Unauthorized changes | Clause 6.1, Clause 8.2 | A.8.2, A.9.1 |
| Verification and validation | Repudiation: No traceability | Clause 8.2 | A.8.5, A.7.1 |
| Deployment | Elevation of privilege: Unauthorized model tweaks | Clause 8.2, Clause 9.1 | A.10.2, A.6.1 |
| Operation and monitoring | Denial of service: System overload | Clause 9.1, Clause 10.1 | A.8.3, A.10.3 |
| Re-evaluation | Drift and new threat vectors | Clause 9.3, Clause 10.2 | A.10.2, A.6.4 |
| Retirement | Information disclosure: Residual risks | Clause 8.3, Clause 10.2 | A.9.4, A.5.2 |

## Maintaining AI governance

Like most technology risk and governance programs, AI management must be continuously monitored and maintained. ISO 42001 requires an organization to have leadership support and sufficient resources to operate effectively over time. This means that AI governance should be built into every process in the AI development and maintenance journey. AIIAs and threat modeling should be conducted at least annually on existing systems, and prior to the deployment of any new AI function. Policies should be reviewed at least annually and after major change to the AI system. Internal audits should review and monitor compliance with controls continuously, and organizations seeking ISO certification will require annual external audits. Progress toward governance goals and metrics on the status of known AI risks should be reported to the highest level of leadership in a live dashboard, and incidents of negative outcomes related to AI use should be tracked and analyzed to improve the AI system.

## Conclusion

Managing AI risk effectively means aligning technical, organizational, and ethical considerations throughout the AI system lifecycle. ISO/IEC 42001 provides structure and accountability. Threat modeling techniques such as STRIDE, MITRE ATLAS, and OWASP for LLM surface deep technical risks. AWS services and features such as SageMaker Model Cards, SageMaker Clarify, and Amazon Bedrock Guardrails help embed governance into layers of AI development.

By combining technical tools, structured assessments, and standards-driven controls, you can build AI systems that are trustworthy, resilient, and aligned with societal expectations.

For additional guidance on achieving, maintaining, and automating compliance in the cloud, contact [AWS Security Assurance Services](https://aws.amazon.com/professional-services/security-assurance-services/) (AWS SAS) or their account team. AWS SAS is a [PCI QSAC](https://listings.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors) and [HITRUST Assessor Firm](https://hitrustalliance.net/assessor/external-assessors/) that can help by tying together applicable audit standards to AWS service specific features and functionality. They help you build on frameworks such as ISO 42001, PCI DSS, HITRUST CSF, NIST-CSF and Privacy Framework, SOC 2, HIPAA, ISO 27001 and 27701, and more. In addition, [AWS Professional Services](https://aws.amazon.com/professional-services/) can also help you plan and map your compliance journey.

***Disclaimer:** The risk strategies and threat modeling guidance shared in this blog are intended to provide general direction and practical insight into implementing AI risk management under ISO/IEC 42001:2023. However, organizations are responsible for conducting their own context-specific risk assessments, as mandated by the standard. This blog should not be interpreted as an exhaustive approach to or guarantee of compliance with ISO/IEC 42001.*

If you have feedback about this post, submit comments in the **Comments** section below.

![Abdul Javid](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2024/11/14/abdul-javid.png)

### Abdul Javid

Abdul is a Senior Security Assurance Consultant and a PECB ISO 42001 Lead Auditor and IAPP Certified AI Governance Professional. He draws on his extensive experience to guide AWS customers on compliance matters. He holds an M.S. in Computer Science from IIT Chicago and numerous certifications from IAPP, AWS, ISO, HITRUST, ISACA, PMI, PCI DSS, and ISC2.

![Amber Welch](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/12/image6.jpeg)

### Amber Welch

Amber is an AWS Security Assurance Services Senior Privacy Consultant, advising AWS customers on their AI and privacy risk management and compliance. She has an M.A. in English and ISO 42001 Lead Auditor, IAPP CIPM, and IAPP CIPP/E certifications. Amber has spoken and written extensively on AI and privacy topics, and is an [AWS Privacy Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/introduction.html) primary author.

TAGS: [AI](https://aws.amazon.com/blogs/security/tag/ai/), [Application security](https://aws.amazon.com/blogs/security/tag/application-security/), [artificial intelligence](https://aws.amazon.com/blogs/security/tag/artificial-intelligence/), [Security](https://aws.amazon.com/blogs/security/tag/security/), [Security Blog](https://aws.amazon.com/blogs/security/tag/security-blog/)

Loading comments…

### Resources

* [AWS Cloud Security](https://aws.amazon.com/security?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-resources)
* [AWS Compliance](https://aws.amazon.com/compliance?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-resources)
* [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html?secd_ip5)
* [Best Practices](https://aws.amazon.com/architecture/security-identity-compliance)
* [Data Protection at AWS](https://aws.amazon.com/compliance/data-protection/)
* [Zero Trust on AWS](https://aws.amazon.com/security/zero-trust/)
* [Cryptographic Computing](https://aws.amazon.com/security/cryptographic-computing/)

---

### Follow

* [Twitter](https://twitter.com/AWSsecurityinfo)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-social)

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