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

## [Containers](https://aws.amazon.com/blogs/containers/)

# Amazon EKS enables ultra scale AI/ML workloads with support for 100K nodes per cluster

by Aditya Ramakrishnan and Shyam Jeedigunta on 16 JUL 2025 in [Amazon Elastic Kubernetes Service](https://aws.amazon.com/blogs/containers/category/compute/amazon-kubernetes-service/ "View all posts in Amazon Elastic Kubernetes Service"), [Announcements](https://aws.amazon.com/blogs/containers/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/containers/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [AWS Trainium](https://aws.amazon.com/blogs/containers/category/artificial-intelligence/aws-trainium/ "View all posts in AWS Trainium"), [Generative AI](https://aws.amazon.com/blogs/containers/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Thought Leadership](https://aws.amazon.com/blogs/containers/category/post-types/thought-leadership/ "View all posts in Thought Leadership") [Permalink](https://aws.amazon.com/blogs/containers/amazon-eks-enables-ultra-scale-ai-ml-workloads-with-support-for-100k-nodes-per-cluster/) Share

We’re excited to announce that [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/) now supports up to 100,000 worker nodes in a single cluster, enabling customers to scale up to 1.6 million [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/) accelerators or 800K NVIDIA GPUs to train and run the largest AI/ML models. This capability empowers customers to pursue their most ambitious AI goals, from training trillion-parameter models to advancing artificial general intelligence (AGI). Amazon EKS provides this industry-leading scale with Kubernetes conformance, ensuring that customers can achieve these breakthroughs with their choice of open source tools and frameworks.

Kubernetes has emerged as a key enabler for customers to run large scale AI/ML workloads given its ability to efficiently scale to meet varying computational demands and its rich collection of AI/ML frameworks and tools. However, as AI/ML models continue to evolve in complexity, they require highly advanced capabilities beyond Kubernetes’ traditional boundaries. By leveraging AWS’s leading capabilities in resilience, security, and availability augmented with technical innovations and open source collaboration, Amazon EKS has made transformative enhancements to provide customers with the scale, performance, and reliability required for their most advanced and large-scale AI/ML workloads, all while preserving the familiar Kubernetes experience.

### **Driving highly performant ultra scale AI infrastructure with Amazon EKS**

State-of-the-art (SOTA) models follow empirical scaling laws – as they increase in size with more training data, they display significantly enhanced capabilities in understanding context, reasoning, and autonomously solving complex tasks. Leading builders of these frontier models – Anthropic, with [Claude](https://www.anthropic.com/claude), and Amazon, with [Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/), have adopted Amazon EKS and its ultra scale capabilities to now scale a single cluster up to 100K nodes. With [Amazon EC2’s](https://aws.amazon.com/pm/ec2/) accelerated computing instance types, this translates to harnessing the performance of up to 1.6 million [Trn2 instances](https://aws.amazon.com/ec2/instance-types/trn2/) or 800K NVIDIA H200/Blackwell GPUs with [P5e](https://aws.amazon.com/ec2/instance-types/p5/)/[P6](https://aws.amazon.com/ec2/instance-types/p6/) instances. This level of scale, in a single Amazon EKS cluster, provides customers with unique benefits:

**Accelerating AI/ML innovation:** Ability to run the largest AI/ML training jobs that demand unprecedented scale by efficiently coordinating hundreds of thousands of GPUs and AI accelerators as a single system.

**Reducing costs:** Consolidate diverse workloads, ranging from large scale training to fine-tuning and inference in a unified environment to reduce operational overhead and improve overall resource utilization. This helps optimize investments in expensive AI accelerators.

**Providing choice and flexibility:** Freedom to use preferred AI/ML frameworks, workflows and tools, both proprietary and open source, per specific needs while maintaining full compatibility with standard Kubernetes APIs.

Amazon EKS has implemented architectural changes across the stack, including enhancements to core Kubernetes components, to support AI/ML workloads at this ultra scale. With a reimagined etcd storage layer for efficient state management and an optimized control plane to handle millions of operations, Amazon EKS can now consistently deliver significantly higher performance. These enhancements also enable more efficient resource orchestration by supporting thousands of concurrent pod operations and advanced monitoring and recovery capabilities, delivering high resiliency at this ultra scale.

### **Empowering the next generation of AI models with Anthropic**

Leading AI innovator and AWS partner, Anthropic runs their flagship Claude family of foundation models on Amazon EKS and operates some of the largest EKS clusters in production, consisting of AWS Trainium (trn2) instances and NVIDIA GPUs for AI workloads alongside [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/) for CPU intensive data processing. This consolidated environment enables them to shift workloads between different AI/ML use cases and optimize resource allocation for their research teams.

Achieving reliable operations at very large scales with a multi-cluster architecture presented Anthropic with some unique challenges across networking, control plane operations, and resource management. By leveraging Amazon EKS’ new ultra scale capabilities, including optimizations at the networking layer and in the Kubernetes control plane, Anthropic has realized significant performance improvements, with end user latency KPIs improving from an average of 35% to consistently above 90%.

> *“Working with AWS, we’ve enhanced our AI infrastructure capabilities with Amazon EKS support for clusters of up to 100K nodes. This combination of EKS’ industry-leading scale and AWS accelerated compute options helps strengthen our foundation for safe and scalable AI” – Nova DasSarma, Technical Lead for Anthropic Infrastructure*

![Figure 1: Percentage of write API calls completing within 15ms increased from 35% to 90% with EKS ultra scale capabilities ](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/07/11/Titan-blog-image.png)

Figure 1: Percentage of write API calls completing within 15ms increased from 35% to 90% with EKS ultra scale capabilities

### **Propelling Artificial General Intelligence (AGI) within Amazon**

Amazon’s AGI infrastructure team builds and operates the infrastructure for the Nova family of foundation models. Their use cases range from massive training jobs orchestrating thousands of nodes in parallel, to complex post-training workflows including model evaluation, distillation, and reinforcement learning. These workloads require sophisticated infrastructure orchestration at a massive scale and rapid recovery abilities to maintain high resiliency and performance.

To meet these needs, the team uses a combination of Amazon EKS and [Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker-ai/hyperpod/), which enhances their ability to run extended training jobs with automated health monitoring and failure recovery leading to reduced down times and high performance. The team leverages Amazon EKS’ ultra scale capabilities and integration with key AWS services for security and monitoring, to maintain consistent performance across their compute intensive training and inference workflows.

> *“Amazon EKS and SageMaker HyperPod have been instrumental in helping us push the boundaries of foundational AI model training at unprecedented scale, while delivering the high resiliency our workloads demand. This technological foundation has not only accelerated our innovation timeline but has become the cornerstone of our strategy to build the next generation of AGI capabilities that will transform how the world interacts with AI” – Rohit Prasad, SVP & Head Scientist, AGI*

### **Building for tomorrow**

AI/ML technologies are evolving at an unprecedented pace, but their effectiveness is directly impacted by the computational power they can efficiently harness. With support for ultra scale clusters, Amazon EKS has evolved many foundational capabilities across the compute stack to enable customers to continue advancing their scale of operations while driving higher performance, resilience, security, and efficiency. With these advancements, customers can utilize the power of Kubernetes and leverage AWS’ broadest and deepest set of cloud capabilities to build their most sophisticated and intelligent applications yet.

To fully explore the technical advancements enabling this scale, read the comprehensive [deep dive blog](https://aws.amazon.com/blogs/containers/under-the-hood-amazon-eks-ultra-scale-clusters/) that details the architectural decisions, implementation challenges, and solutions developed. Please reach out to your AWS account team to learn more about this new capability.

TAGS: [Amazon EKS](https://aws.amazon.com/blogs/containers/tag/amazon-eks/), [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/blogs/containers/tag/amazon-elastic-kubernetes-service-amazon-eks/), [artificial intelligence](https://aws.amazon.com/blogs/containers/tag/artificial-intelligence/), [Machine Learning](https://aws.amazon.com/blogs/containers/tag/machine-learning/)

### Resources

* [Amazon Container Services](https://aws.amazon.com/containers?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-resources)
* [AWS Fargate](https://aws.amazon.com/fargate/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-resources)
* [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-resources)
* [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-resources)
* [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-resources)
* [AWS Cloud Map](https://aws.amazon.com/cloud-map?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [RSS Feed](http://feeds.feedburner.com/AmazonWebServicesBlog)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-social)

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