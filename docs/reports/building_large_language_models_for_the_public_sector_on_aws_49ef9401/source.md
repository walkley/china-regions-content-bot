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

## [AWS Public Sector Blog](https://aws.amazon.com/blogs/publicsector/)

# Building large language models for the public sector on AWS

by Laura Verghote, Anton Alexander, Eliuth Triana Isaza, Niki Sotiria Kokkalas, and Wenhan Tan on 27 OCT 2025 in [Amazon EC2](https://aws.amazon.com/blogs/publicsector/category/compute/amazon-ec2/ "View all posts in Amazon EC2"), [Amazon Machine Learning](https://aws.amazon.com/blogs/publicsector/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/publicsector/category/artificial-intelligence/sagemaker/amazon-sagemaker-hyperpod/ "View all posts in Amazon SageMaker HyperPod"), [Artificial Intelligence](https://aws.amazon.com/blogs/publicsector/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Public Sector](https://aws.amazon.com/blogs/publicsector/category/public-sector/ "View all posts in Public Sector"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/publicsector/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance"), [Technical How-to](https://aws.amazon.com/blogs/publicsector/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/publicsector/building-large-language-models-for-the-public-sector-on-aws/) Share

[![AWS branded background with text "Building large language models for the public sector on AWS"](https://d2908q01vomqb2.cloudfront.net/9e6a55b6b4563e652a23be9d623ca5055c356940/2025/10/22/AWS-Public-Sector-Blog-Featured-Images-Blog-Header-static-template-Autosaved-17.png)](https://d2908q01vomqb2.cloudfront.net/9e6a55b6b4563e652a23be9d623ca5055c356940/2025/10/22/AWS-Public-Sector-Blog-Featured-Images-Blog-Header-static-template-Autosaved-17.png)

[Large language models (LLMs)](https://aws.amazon.com/what-is/large-language-model/) are transforming how public sector organizations deliver services, engage with citizens, and make data-driven decisions. Through advanced multilingual support and complex task automation, LLMs can unlock faster response times and new capabilities for processing domain-specific information at scale.

Off-the-shelf models are powerful, but they often fall short of the specific regulatory, cultural, and operational requirements that define public sector missions. Many commercial LLMs are trained on broad, internet-scale datasets that might not reflect the linguistic nuances, cultural context, or regulatory frameworks of specific countries or sectors. They can also carry biases from their training data, lack specialized terminology, or operate in environments that cannot meet data sovereignty and privacy requirements. For public sector agencies—where accuracy, compliance, and trust are critical—these limitations can make commercial models insufficient for mission-critical applications. Custom LLM development addresses these challenges. By training a model from scratch, continued pretraining of an existing model, or fine-tuning a pre-trained model, organizations can incorporate language- or domain-specific knowledge, comply with local regulations and address contextual nuances.

Two types of custom LLMs are particularly relevant to public sector missions:

* **National LLMs** are built to reflect a specific country or region’s linguistic nuances, cultural context, and regulatory frameworks. They can help preserve local languages, account for culturally appropriate outputs, and align with national data sovereignty requirements. A notable example is [Greece’s initiative](https://www.ilsp.gr/en/news/krikri/) to develop an open-weight LLM that addresses the underrepresentation of the Greek language in commercial models, while preserving both contemporary and historical linguistic heritage.
* **Domain-specific LLMs** are optimized for highly specialized sectors such as healthcare, education, finance, or legal services—delivering greater accuracy on technical tasks and deeper understanding of subject-specific terminology. These models demonstrate how domain adaptation can enhance core professional tasks while maintaining quality and appropriateness standards.

This blog post provides a comprehensive overview of the custom LLM development lifecycle for public sector use, emphasizing scientific methodology and measurable outcomes. The development process follows six key stages, each critical for ensuring the model serves its intended mission while meeting strict security, compliance, and performance standards.

## Cost analysis framework

Before embarking on custom LLM development, organizations must evaluate costs at two levels: near-term per-token pricing for managed APIs versus total cost of ownership (TCO) for self-hosting.

Managed APIs optimize for speed of adoption, but can become expensive at scale due to per-token charges and egress costs. Self-hosting shifts spending toward upfront capital expenditure (GPU acquisition or reserved capacity, engineering resources) with lower marginal operational expenditure per token over time.

Model size serves as a key cost driver: Larger parameter counts generally improve quality up to a point, but increase serving latency, memory footprint, and training/inference costs. Right-sizing through continued pre-training or targeted fine-tuning can deliver comparable task performance at reduced cost.

To make informed deployment decisions, organizations first need to estimate daily traffic (tokens/day), seasonality, target latency, and availability requirements. By then modeling the breakeven point where cumulative API spending exceeds self-hosting TCO (including hardware amortization, power, and operations), data-driven deployment choices can be made. In many public sector cases, a mid-sized, adapted open-source model hosted within the organization’s own cloud environment offers the optimal balance—meeting residency constraints, achieving latency targets on fewer GPUs, and reducing long-term operational expenses after initial capital investment.

## The customer LLM development process

The stages of developing a custom LLM are:

1. Use case and requirements definition
2. Evaluation framework establishment
3. Model selection and training approach
4. Data collection and preparation
5. Infrastructure provisioning and training approach
6. Production deployment and performance testing

Each stage shapes how effectively the model will serve its intended mission, while meeting public sector’s standards for security, compliance, and performance.

### Stage 1: Use case requirements definition

Custom LLM development begins with rigorous requirements definition, translating high-level organizational goals into concrete, measurable specifications. This stage determines whether a custom approach is necessary or if prompt engineering alone can achieve desired outcomes.

A customized approach typically becomes necessary when prompt engineering consistently fails to deliver acceptable results across multiple attempts, when specific language requirements are not met by existing models, or when use cases require deep domain expertise that cannot be reliably accessed through standard prompting techniques.

The requirements definition process starts by identifying specific use cases where the custom LLM will provide measurable value. Government agencies must consider practical applications—citizen engagement platforms, policy analysis systems, specialized research tools, or administrative automation. Recent examples demonstrate this stage’s criticality: Greece’s national LLM project defined precise requirements for processing both modern and ancient Greek texts while maintaining strong English performance, enabling applications across various public sector verticals.

Organizations must establish clear success metrics, including quantifiable improvements in service delivery times, accuracy rates for specialized tasks, and citizen satisfaction scores. Technical requirements should address response time targets, expected query volumes, and integration needs with existing government systems.

Additionally, organizations must define comprehensive data handling protocols, access controls, and audit requirements. For national LLMs, this often includes specific data sovereignty and local hosting requirements. Domain-specific models may require compliance with specialized regulations in healthcare, finance, or other sensitive sectors.

Documenting these requirements helps communicate business value to stakeholders while providing technical teams with clear development guidelines. This documentation becomes particularly important when coordinating across multiple government departments or agencies, ensuring alignment between technical capabilities and organizational needs.

### Stage 2: Evaluation framework establishment

Establishing a robust evaluation framework before model selection ensures scientific rigor and measurable outcomes throughout the development process. This framework forms the foundation for all subsequent decisions and prevents subjective choices that can undermine project success.

#### Baseline performance and adaptation rate metrics

Two key metrics drive model selection and training decisions:

* **Baseline performance (b)**: Task- and domain-specific evaluation scores of candidate models before any adaptation, using fixed prompts and held-out development/test sets. This provides an objective starting point for comparing different base models.
* **Rate of adaptation (ra)**: The speed and efficiency with which a model improves on evaluations during adaptation, normalized by training progress (steps, tokens, time, or cost). This metric helps predict which models will respond best to continued training within available budgets.

#### Evaluation tools and implementation

The [Language Model Evaluation Harness (LM Harness)](https://github.com/EleutherAI/lm-evaluation-harness) serves as the industry standard for LLM evaluation, providing a unified framework to test models across over 60 academic benchmarks with hundreds of subtasks and variants. LM Harness supports various model backends, including Hugging Face transformers, [vLLM](https://github.com/vllm-project/vllm) for fast inference, and commercial APIs, enabling reproducibility and comparability across different implementations.

For AWS-focused workflows, organizations can complement LM Harness with AWS-native evaluation tools while maintaining industry standard compatibility. The [Hugging Face Open LLM Leaderboard](https://huggingface.co/open-llm-leaderboard), which uses LM Harness as its backend, provides standardized performance comparisons across various tasks and languages, serving as an excellent reference point for national LLM evaluation.

#### Q&A dataset generation and validation process

Developing high-quality evaluation datasets requires a systematic approach combining automated generation with human validation:

1. **Define scope and corpus**: List priority use cases, domains, and languages. Assemble representative, high-quality corpus from documents, policies, FAQs, and knowledge bases, ensuring proper cleaning, deduplication, and personally identifiable information (PII) removal.
2. **Establish baseline generator:** Run quick evaluations across candidate models to select the best generator for target languages and domains, avoiding self-grading bias.
3. **Design prompt templates:** Specify style, difficulty, answer format, and grounding requirements. Create variants for factual Q&A, multi-step reasoning, policy compliance, and multilingual scenarios.
4. **Pilot generation (100-300 items):** Use the baseline model to generate Q&A pairs from the corpus, covering all domains, difficulties, and languages proportionally. Tag each item with provenance metadata.
5. **Human validation loop:** Sample and label items for correctness, grounding, clarity, and safety. Fix issues and document error patterns. Compute acceptance metrics (target ≥ 90 percent correct and grounded).
6. **Quality and safety filters:** Apply automated passes for deduplication, boilerplate removal, perplexity filtering, and PII checks using tools [like NVIDIA’s NeMo Curator](https://github.com/NVIDIA-NeMo/Curator).
7. **Scale generation:** Generate the full Q&A dataset with locked templates and models, maintaining strict metadata and versioning across train/dev/test splits.
8. **Validation hardening:** Conduct human audits on stratified samples, adding adversarial cases and safety scenarios.

#### Performance measurement framework

Evaluation must consider multiple dimensions:

* Language proficiency and cultural accuracy
* Task-specific performance in government use cases
* Compliance with regulatory and ethical guidelines
* Response appropriateness and safety
* Computational efficiency and resource utilization

Organizations should implement iterative evaluation processes with findings feeding back into optimization phases until models meet performance targets and satisfy compliance requirements.

### Stage 3: Model selection and training approach

After establishing evaluation frameworks, organizations must make crucial decisions about model architecture and training strategies. These decisions are influenced by the problem scope, current model performance, security requirements, and required level of customization.

#### Training approach decision matrix

There are three primary options, each with distinct advantages and resource requirements.

* **Fine-tuning** represents the most resource-efficient approach, involving targeted training of a pre-trained model on domain-specific data. This method suits scenarios where target domains share similarities with the pre-training data or when resources are limited. Fine-tuning can be specialized through instruction fine-tuning, which uses examples of how the model should respond to specific instructions, or through techniques like Reinforcement Learning from Human Feedback (RLFH) to better align the model with human preferences.
* **Continued pretraining (CPT)** involves training existing base models on additional data while preserving general capabilities. This approach effectively adapts models to new languages or domains while maintaining fundamental understanding and reasoning abilities. It requires less data than training from scratch but more than fine-tuning, offering better longevity for unseen questions through two-phase training with high-quality data. Specifically, CPT first adapts the model to new domains or languages while maintaining its base knowledge, then focuses on refining specific capabilities—resulting in more robust and generalizable performance.
* **Training from scratch** provides complete control over model architecture and capabilities but demands significantly more computational resources and high-quality data than customizing existing foundation models. This approach becomes necessary when existing models inadequately represent target languages or fail to meet specific compliance requirements.

Organizations should model breakeven points where API spending exceeds self-hosting TCO, factoring in traffic estimates, latency requirements, and hardware costs. The TCO analysis must carefully evaluate both capital expenditure (CAPEX) and operational expenditure (OPEX). OPEX components are primarily driven by model hosting requirements, where larger models with more parameters and GPU compute demands lead to proportionally higher running costs over time, assuming consistent user traffic and bandwidth. The decision framework should prioritize the smallest model achieving key performance indicators after adaptation within serving constraints, as this directly impacts long-term operational sustainability through reduced CAPEX in initial training and lower OPEX through reduced hosting costs and resource requirements.

Choose fine-tuning when a base model achieves approximately 80 percent of target performance through prompting and labeled task data is available. Select continued pre-training (CPT) when domain or language coverage is insufficient, but a large unlabeled in-domain corpus (10-1000B tokens) exists. Consider training from scratch only when no acceptable base model exists and the organization can support trillion-token training infrastructure.

Key factors include cost and time constraints (API vs GPU-hours), serving requirements (latency/memory), residency mandates, and risk tolerance (catastrophic forgetting). Organizations should prefer the smallest base model that meets key performance indicators after CPT or fine-tuning, validating decisions through baseline performance (b) and rate of adaptation (ra) curves.

#### Model architecture considerations

For organizations pursuing fine-tuning or CPT, several open-source models are available as starting points. Model selection depends on technical factors including desired model size and computational requirements, language support needs, and the out of the box performance.

Organizations must also consider the model’s architecture (for example, transformer-based designs or Expert Parallelism), modality requirements (text-only or multimodal), parameter count, and how these choices will impact both training requirements and inference performance in production environment.

### Stage 4: Data collection and preparation

Data collection and preparation represents the most critical phase in custom LLM development, particularly for public sector applications where data quality, relevance, and security are crucial. The approach varies significantly based on the chosen model architecture and training strategy.

#### Comprehensive data pipeline with NeMo Curator

[NVIDIA’s NeMo Curator](https://github.com/NVIDIA-NeMo/Curator) provides an end-to-end data curation toolkit designed for pretraining and fine-tuning corpora at scale. This modular pipeline system supports distributed processing through Spark, Ray, or Dask, handling everything from data download and extraction to cleaning, filtering, deduplication, and classification.

Key NeMo Curator capabilities include:

* **Ingestion:** Web crawling, Common Crawl processing, data lake integration (S3), and document parsing (PDF-to-text with layout heuristics)
* **Normalization:** Unicode/NFKC processing, whitespace and punctuation standardization, boilerplate and template removal
* **Safety and PII processing:** Regex and ML-based detectors with configurable redaction/drop policies and country/sector-specific compliance profiles
* **Advanced deduplication:** Exact hash matching (MinHash/SimHash) and fuzzy near-duplicate detection (LSH) at document and paragraph levels
* **Quality filtering:** Language identification, length/perplexity bounds, n-gram/stopword ratios, toxicity/safety scoring
* **Classification and tagging:** Domain/topic labeling, document structure analysis, jurisdiction/language tagging

#### Critical data processing components

* **Deduplication** operates at multiple levels: exact content hashing (SHA256) on normalized text removes identical documents and segments, while near-duplicate detection uses MinHash/SimHash with LSH clustering at document and paragraph levels. The process maintains provenance by keeping canonical copies and logging hash clusters with retention rationale.
* **PII removal** employs multiple detection methods: regex patterns for emails, phones, and IDs; dictionaries for names and locations; ML NER for person/organization/location entities; and specialized patterns for payment and health information. Organizations can configure policies to redact versus drop content by data class and jurisdiction, with comprehensive audit logging for compliance validation.
* **Synthetic data generation** addresses sparse domains through systematic processes: seed selection, LLM prompting with style and grounding constraints, output schema enforcement (JSON), validation through regex/schema/toxicity/grounding checks, human review sampling, and scaling with appropriate controls including temperature/top-p limits, length bounds, and source span citations.
* **Quality filtering and perplexity scoring** combine multiple signals: language identification gates, length bounds, heuristic measures (stopword ratios, symbol/emoji fractions), toxicity/safety scores, domain fitness classification, and perplexity scoring using reference language models to flag low-information or degenerate text while avoiding bias against rare but valid content.

Organizations should run data processing stages in sequence:

1. Normalization
2. Removing PII
3. Deduplication
4. Quality filters
5. Perplexity trimming
6. Classification/splits, while tracking metrics including retention percentages
7. Duplication ratios
8. PII hit rates
9. Perplexity distributions
10. Per-language/domain coverage.

#### Dataset composition strategies

**For national LLMs**, organizations should include diverse content mixing target language materials, related languages or dialects, and general knowledge. Including English data alongside target languages serves two purposes: preventing catastrophic forgetting of general capabilities and maintaining practical bilingual functionality. Parallel data (paired texts in both languages) helps models understand cross-language relationships for seamless switching. The key lies in balanced composition—excessive English data may dilute target language capabilities, while insufficient English content can compromise general knowledge and reasoning abilities. Organizations may include specialized content like code or mathematical texts if required for specific use cases.

**For domain-specific models**, maintaining balance between domain-specific content and general knowledge proves essential. Heavy focus on domain data can cause models to lose broader reasoning and language skills, while excessive general data dilutes specialized expertise. Parallel datasets offer solutions by pairing technical and simplified text within the same language—for example, matching medical guidelines with patient-friendly explanations to connect expert terminology with accessible descriptions.

#### Technical implementation considerations

The choice of tokenization method critically affects model performance, particularly for languages using different writing systems or alphabets. Standard tokenization methods developed for Latin-script languages might prove ineffective for languages without word spacing or containing characters not represented in basic tokenizer vocabularies. For multilingual models, creating shared vocabularies that adequately represent multiple languages becomes particularly challenging, potentially resulting in inefficient text representation and reduced performance.

### Stage 5: Infrastructure provisioning and training approach

Infrastructure selection significantly impacts training efficiency, cost, and operational complexity. AWS offers multiple options designed for different organizational needs and expertise levels.

#### Compute infrastructure options

[Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) with [Capacity Blocks for ML](https://aws.amazon.com/ec2/capacityblocks/) provides maximum flexibility and control. It’s ideal for organizations that require specific customizations. However, this approach demands deep in-house expertise in managing computational infrastructure. Amazon EC2 offers various ML-optimized instance types with powerful GPUs, providing cost-effective resources tailored to specific project requirements.

[Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker/ai/hyperpod/) with SageMaker Training Plans delivers a managed solution optimized for large-scale deep learning workloads, simplifying distributed training infrastructure setup and management through features like automatic health monitoring and instance replacement. The SageMaker HyperPod cluster agent will automatically detect any fulty node, replace the faulty node and resume the training from the last working checkpoint without any user interruption. This proves particularly valuable for long-running LLM training jobs where reliability is crucial.

#### Network and storage optimization

[Elastic Fabric Adapter (EFA)](https://aws.amazon.com/hpc/efa/) provides high-performance computing networks significantly boosting distributed LLM training efficiency through low-latency, high throughput networking for multi-node GPU training. EFA enables you to run applications requiring high levels of inter-node communications at scale on AWS through its custom-built operating system bypass hardware interface. This allows applications to communicate directly with the network hardware while bypassing the operating system kernel, significantly reducing latency and CPU overhead. This direct hardware access is particularly beneficial for distributed ML workloads where frequent inter-node communication during gradient synchronization can become a bottleneck.

The choice of data storage and access methods is critical for training efficiency. For large-scale training, AWS provides optimal storage solutions combining [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) for long-term storage and [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/)as a high-performance file system, enabling efficient data access across training nodes. Amazon [FSx for Lustre](https://aws.amazon.com/fsx/lustre/) uses [distributed file storage](https://wiki.lustre.org/Introduction_to_Lustre) (stripping) and physically separates file metadata from file content to achieve high-performance read/writes. The connection between Amazon S3 and Amazon FSx for Lustre can be managed through a [data repository association](https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-dra-linked-data-repo.html).

#### Orchestration and job management

Organizations can choose from various orchestration tools depending on infrastructure choice and team expertise.

**SLURM integration** supports both on-premises migration and cloud-native deployment. [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/) uses SLURM as its default job scheduler, providing familiar workflow management for HPC teams. SLURM configuration should include GPU resource management (gres.conf), NCCL/IB optimization, heterogeneous job support, and checkpointing to shared filesystems.

**Amazon EKS integration** offers flexibility for organizations with Kubernetes expertise. EKS setup requires GPU-enabled node groups (p4d/p5, L4/L40S), NVIDIA GPU Operator installation, proper scheduling with node selectors and taints, Karpenter for scale-out, and pod priority/preemption for training versus inference workloads.

**Migration considerations** between SLURM and EKS include network performance validation (enabling comparable interconnect performance), scheduler semantic mapping (Slurm partitions/QoS to K8s namespaces/ResourceQuotas), checkpoint compatibility verification, security control mapping (IAM roles for service accounts), and cost modeling with phased rollout plans.

#### Training process implementation

The training process typically involves frameworks such as PyTorch or TensorFlow, using distributed processing across multiple GPUs or nodes. The process follows a pattern of data scattering, results gathering, and iterative cycles based on training outcomes.

Training is an iterative process of training, testing, and refinement until models meets the defined performance goals. This often involves techniques like hyperparameter tuning, where parameters such as learning rate, batch size, and model architecture are adjusted for optimal performance.

Organizations should evaluate infrastructure options considering training job scale, in-house expertise, specific performance requirements, and the balance between operational complexity and flexibility.

## Stage 6: Production deployment and performance testing

After an LLM meets performance and compliance standards, comprehensive production deployment requires systematic performance testing, infrastructure optimization, and monitoring.

#### Production performance testing framework

Organizations must conduct systematic performance testing to validate the model’s capabilities under various conditions. This includes establishing a benchmark framework using industry-standard tools like [GenAI-Perf](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html) and [vLLM](https://docs.vllm.ai/en/latest/) to consistently measure and compare performance across different configurations. Testing should capture both steady-state and burst behavior through step-load and spike tests using canary datasets for repeatability. Organizations can automate testing through tools like k6, Locust, or custom Python harnesses. For GPU services, running multiple replicas tests autoscaling thresholds effectively. Validation should cover stability across 10-30 minute windows per concurrency level, extending to 1-2 hour endurance runs for production readiness.

#### Model deployment options and data sovereignty

When selecting model hosting for national LLMs, organizations must distinguish between three primary deployment approaches, each with distinct implications for data sovereignty:

1. Closed-source models on third-party cloud service providers: Data flows and logs are controlled by external parties outside your account boundary, potentially creating compliance challenges for jurisdictions with strict data residency requirements.
2. Open-source models via managed services (such as [Amazon Bedrock](https://aws.amazon.com/bedrock/)): These simplify access and governance while running in a managed service environment, offering a balance between control and operational simplicity.
3. Open-source models fully hosted in customer AWS accounts: This provides the strongest control over data paths, telemetry, and audit trails, often necessary for meeting stringent sovereignty requirements.

Data residency and sovereignty requirements—such as GDPR compliance or in-country processing mandates—frequently dictate this choice. Some jurisdictions require both training and inference to remain within national boundaries, ruling out cross-border endpoints. Beyond storage location, compliance extends to where prompts, outputs, and model logs are processed; even transient inference traffic can violate regulations if it crosses required boundaries.

For many public sector builds, self-hosting open-source models in customer accounts provides the clearest path to meeting residency, privacy, and audit obligations, while managed APIs may remain viable for non-sensitive workloads or early evaluation phases.

[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/) provides a managed environment for model deployment, handling much of the underlying infrastructure complexity while offering scalable inference options and seamless integration with other AWS services. For organizations that require greater control or specific configurations, [Amazon EC2](https://aws.amazon.com/ec2/?trk=d8dedb65-2342-4d54-8849-ce8532afc9c7&sc_channel=ps&ef_id=CjwKCAjwxrLHBhA2EiwAu9EdM1fRpzYYYIhq7KwxgvFMgSodH9SQG0jDJDBYWkym3Ojeo_zMD4DbNRoC1IwQAvD_BwE:G:s&s_kwcid=AL!4422!3!646065809923!e!!g!!amazon%20ec2!19610627737!149206344847&gad_campaignid=19610627737&gbraid=0AAAAADjHtp-WaiajWt0mUzAH46avU_cmx&gclid=CjwKCAjwxrLHBhA2EiwAu9EdM1fRpzYYYIhq7KwxgvFMgSodH9SQG0jDJDBYWkym3Ojeo_zMD4DbNRoC1IwQAvD_BwE) enables direct deployment with full customization capabilities. Organizations with existing Kubernetes expertise might prefer [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/) for containerized deployments, providing flexibility and portability across environments.

Successful deployment requires careful attention to cost management, performance monitoring, and security compliance. Organizations must implement appropriate optimization strategies while ensuring the model integrates seamlessly with existing systems and meets public sector security and compliance requirements.

#### Security and Compliance Framework

Public sector LLM deployments demand comprehensive security and compliance measures addressing data sovereignty, privacy, and audit requirements.

Organizations must enforce data residency by pinning training and inference to approved regions and VPCs (Virtual Private Clouds), using customer-managed KMS keys, private subnets, and VPC endpoints. PII detection and removal should be implemented in curation pipelines with audited reject buckets and immutable transformation logs.

Documentation must cover where prompts, outputs, and telemetry are processed, including transient logs. For model hosting, organizations should prefer in-account endpoints (Amazon EC2/Amazon EKS/Amazon SageMaker) when sovereignty mandates require control over data paths and logs, maintaining access controls (IAM/IRSA), encryption in transit and at rest, audit trails (CloudTrail), and periodic compliance reviews.

## Conclusion

Developing and deploying custom LLMs for public sector use requires systematic approaches balancing innovation with security, compliance, and reliability requirements. Through scientific methodology emphasizing measurable outcomes and repeatable processes, organizations can successfully navigate the complexity while achieving mission-critical objectives.

The comprehensive AWS service suite provides tools and infrastructure necessary for each development stage, from initial evaluation frameworks through production deployment and monitoring. Whether preserving cultural heritage through national language models or enhancing public services with specialized domain models, custom LLMs offer significant potential for improving how governments and public institutions serve their communities.

Success requires ongoing commitment beyond initial deployment, including continuous monitoring, refinement, and adaptation to sustain LLM effectiveness in evolving operational environments.

Organizations ready to begin custom LLM development should:

1. **Establish evaluation frameworks** using [LM Harness](https://github.com/EleutherAI/lm-evaluation-harness) and AWS-native tools
2. **Conduct cost analysis** comparing API usage versus self-hosting TCO for projected workloads
3. **Review AWS infrastructure options** including [SageMaker HyperPod](https://aws.amazon.com/sagemaker/ai/hyperpod/), [AWS PCS](https://aws.amazon.com/pcs), and [Amazon EC2](https://aws.amazon.com/ec2/?trk=d8dedb65-2342-4d54-8849-ce8532afc9c7&sc_channel=ps&ef_id=CjwKCAjwxrLHBhA2EiwAu9EdM1fRpzYYYIhq7KwxgvFMgSodH9SQG0jDJDBYWkym3Ojeo_zMD4DbNRoC1IwQAvD_BwE:G:s&s_kwcid=AL!4422!3!646065809923!e!!g!!amazon%20ec2!19610627737!149206344847&gad_campaignid=19610627737&gbraid=0AAAAADjHtp-WaiajWt0mUzAH46avU_cmx&gclid=CjwKCAjwxrLHBhA2EiwAu9EdM1fRpzYYYIhq7KwxgvFMgSodH9SQG0jDJDBYWkym3Ojeo_zMD4DbNRoC1IwQAvD_BwE) Capacity Blocks
4. **Implement data curation pipelines** using tools like [Nemo Curator](https://github.com/NVIDIA/NeMo-Curator) for large-scale processing
5. **Design security and compliance frameworks** meeting specific jurisdictional requirements

For detailed technical guidance, explore our comprehensive resource library:

* [An introduction to preparing your own dataset for LLM training](https://aws.amazon.com/blogs/machine-learning/an-introduction-to-preparing-your-own-dataset-for-llm-training/)
* [AWS Machine Learning documentation](https://docs.aws.amazon.com/machine-learning/)
* [Amazon SageMaker developer guide](https://docs.aws.amazon.com/sagemaker/)
* [Beyond accelerators: Lessons from building foundation models on AWS with Japan’s GENIAC program](https://aws.amazon.com/blogs/machine-learning/beyond-accelerators-lessons-from-building-foundation-models-on-aws-with-japans-geniac-program/)

Contact your AWS account team to discuss specific requirements and develop customized implementation roadmaps for your organization’s national LLM initiatives.

TAGS: [Artificial Intelligence](https://aws.amazon.com/blogs/publicsector/tag/artificial-intelligence/), [AWS Public Sector](https://aws.amazon.com/blogs/publicsector/tag/aws-public-sector/), [technical how-to](https://aws.amazon.com/blogs/publicsector/tag/technical-how-to/)

![Laura Verghote](https://d2908q01vomqb2.cloudfront.net/9e6a55b6b4563e652a23be9d623ca5055c356940/2025/10/22/Picture1-8.png)

### Laura Verghote

Laura is the generative AI lead for PSI Europe at AWS, driving generative AI adoption across public sector organizations. She partners with customers throughout Europe to accelerate their generative AI initiatives through technical expertise and strategic planning, bridging complex requirements with innovative AI solutions.

![Anton Alexander](https://d2908q01vomqb2.cloudfront.net/9e6a55b6b4563e652a23be9d623ca5055c356940/2025/10/22/Picture2-3.jpg)

### Anton Alexander

Anton is a senior specialist in generative AI at AWS, focusing on scaling large training and inference workloads with AWS HyperPod. As a veteran CUDA programmer and Kubernetes expert, he helps enterprises integrate NVIDIA technologies for distributed training, specializing in EKS and Slurm implementations. Anton works closely with MENA Region and government sector clients to optimize generative AI solutions. He holds a patent pending for machine learning edge computing systems. Outside of work, Anton is a Brazilian jiu-jitsu and collegiate boxing champion who enjoys flying planes.

![Eliuth Triana Isaza](https://d2908q01vomqb2.cloudfront.net/9e6a55b6b4563e652a23be9d623ca5055c356940/2025/10/23/eliuth.jpg)

### Eliuth Triana Isaza

Eliuth is a developer relations manager at NVIDIA, empowering Amazon’s AI MLOps, DevOps, scientists, and AWS technical experts to master the NVIDIA computing stack for accelerating and optimizing generative AI foundation models spanning from data curation, GPU training, model inference, and production deployment on AWS GPU instances. In addition, Eliuth is a passionate mountain biker, skier, and tennis and poker player.

![Niki Sotiria Kokkalas](https://d2908q01vomqb2.cloudfront.net/9e6a55b6b4563e652a23be9d623ca5055c356940/2025/10/03/Picture7.jpg)

### Niki Sotiria Kokkalas

Niki Sotiria is an industry solutions architect at AWS specialized in generative AI and data analytics workloads for public sector organizations across EMEA. She mainly partners with education-focused institutions and organizations to design and implement effective data and AI strategies that drive innovation and impact.

![Wenhan Tan](https://d2908q01vomqb2.cloudfront.net/9e6a55b6b4563e652a23be9d623ca5055c356940/2025/10/23/Wenhan-Tan.png)

### Wenhan Tan

Wenhan is a solutions architect at NVIDIA, assisting customers to adopt NVIDIA AI solutions at large-scale. His work focuses on accelerating deep learning applications and addressing inference and training challenges.

### Resources

* [AWS in the Public Sector](https://aws.amazon.com/government-education?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=publicsector-resources)
* [AWS for Government](https://aws.amazon.com/government-education/government/)
* [AWS for Education](https://aws.amazon.com/education/)
* [AWS for Nonprofits](https://aws.amazon.com/government-education/nonprofits/)
* [AWS for Public Sector Health](https://aws.amazon.com/government-education/public-sector-healthcare/)
* [AWS for Aerospace and Satellite Solutions](https://aws.amazon.com/government-education/aerospace-and-satellite/)
* [Case Studies](https://aws.amazon.com/solutions/case-studies?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=publicsector-resources)
* [Fix This Podcast](https://aws.amazon.com/government-education/fix-this/)
* [Additional Resources](https://aws.amazon.com/government-education/resources?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=publicsector-resources)
* [Contact Us](https://aws.amazon.com/government-education/contact/?trkCampaign=ps&trk=ps_blog_resources)

---

### Follow

* [AWS for Government Twitter](https://twitter.com/aws_gov)
* [AWS Education Twitter](https://twitter.com/aws_edu)
* [AWS Nonprofits Twitter](https://twitter.com/AWS_Nonprofits)
* [Newsletter Subscription](https://pages.awscloud.com/WWPSBlogNewsletterOpt-In.html?trk=ta_a134p000006vtakAAA&trkCampaign=AWS_Public_Sector_Blog_Newsletter_Opt-In&sc_channel=ta&sc_campaign=Blog-opt-in-cta-2-side-bar&sc_outcome=WWPS)

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