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

# AWS AI infrastructure with NVIDIA Blackwell: Two powerful compute solutions for the next frontier of AI

by David Brown on 09 JUL 2025 in [Amazon EC2](https://aws.amazon.com/blogs/machine-learning/category/compute/amazon-ec2/ "View all posts in Amazon EC2"), [Announcements](https://aws.amazon.com/blogs/machine-learning/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Compute](https://aws.amazon.com/blogs/machine-learning/category/compute/ "View all posts in Compute") [Permalink](https://aws.amazon.com/blogs/machine-learning/aws-ai-infrastructure-with-nvidia-blackwell-two-powerful-compute-solutions-for-the-next-frontier-of-ai/)  [Comments](https://aws.amazon.com/blogs/machine-learning/aws-ai-infrastructure-with-nvidia-blackwell-two-powerful-compute-solutions-for-the-next-frontier-of-ai/#Comments)  Share

Imagine a system that can explore multiple approaches to complex problems, drawing on its understanding of vast amounts of data, from scientific datasets to source code to business documents, and reasoning through the possibilities in real time. This lightning-fast reasoning isn’t waiting on the horizon. It’s happening today in our customers’ AI production environments. The scale of the AI systems that our customers are building today—across drug discovery, enterprise search, software development, and more—is truly remarkable. And there’s much more ahead.

To accelerate innovation across emerging generative AI developments such as reasoning models and agentic AI systems, we’re excited to announce general availability of [P6e-GB200 UltraServers](https://aws.amazon.com/ec2/instance-types/p6/), accelerated by NVIDIA Grace Blackwell Superchips. P6e-GB200 UltraServers are designed for training and deploying the largest, most sophisticated AI models. Earlier this year, we launched [P6-B200 instances](https://aws.amazon.com/ec2/instance-types/p6/), accelerated by NVIDIA Blackwell GPUs, for diverse AI and high-performance computing workloads.

In this post, we share how these powerful compute solutions build on everything we’ve learned about delivering secure, reliable GPU infrastructure at a massive scale, so that customers can confidently push the boundaries of AI.

## Meeting the expanding compute demands of AI workloads

P6e-GB200 UltraServers represent our most powerful GPU offering to date, featuring up to 72 NVIDIA Blackwell GPUs interconnected using fifth-generation NVIDIA NVLink—all functioning as a single compute unit. Each UltraServer delivers a massive 360 petaflops of dense FP8 compute and 13.4 TB of total high bandwidth GPU memory (HBM3e)—which is over 20 times the compute and over 11 times the memory in a single NVLink domain compared to P5en instances. P6e-GB200 UltraServers support up to 28.8 Tbps aggregate bandwidth of fourth-generation Elastic Fabric Adapter (EFAv4) networking.P6-B200 instances are a versatile option for a broad range of AI use cases. Each instance provides 8 NVIDIA Blackwell GPUs interconnected using NVLink with 1.4 TB of high bandwidth GPU memory, up to 3.2 Tbps of EFAv4 networking, and fifth-generation Intel Xeon Scalable processors. P6-B200 instances offer up to 2.25 times the GPU TFLOPs, 1.27 times the GPU memory size, and 1.6 times the GPU memory bandwidth compared to P5en instances.

How do you choose between P6e-GB200 and P6-B200? This choice comes down to your specific workload requirements and architectural needs:

* P6e-GB200 UltraServers are ideal for the most compute and memory intensive AI workloads, such as training and deploying frontier models at the trillion-parameter scale. Their NVIDIA GB200 NVL72 architecture really shines at this scale. Imagine all 72 GPUs working as one, with a unified memory space and coordinated workload distribution. This architecture enables more efficient distributed training by reducing communication overhead between GPU nodes. For inference workloads, the ability to fully contain trillion-parameter models within a single NVLink domain means faster, more consistent response times at scale. When combined with optimization techniques such as disaggregated serving with NVIDIA Dynamo, the large domain size of GB200 NVL72 architecture unlocks significant inference efficiencies for various model architectures such as mixture of experts models. GB200 NVL72 is particularly powerful when you need to handle extra-large context windows or run high-concurrency applications in real time.
* P6-B200 instances support a broad range of AI workloads and are an ideal option for medium to large-scale training and inference workloads. If you want to port your existing GPU workloads, P6-B200 instances offer a familiar 8-GPU configuration that minimizes code changes and simplifies migration from current generation instances. Additionally, although NVIDIA’s AI software stack is optimized for both Arm and x86, if your workloads are specifically built for x86 environments, P6-B200 instances, with their Intel Xeon processors, will be your ideal choice.

## Innovation built on AWS core strengths

Bringing NVIDIA Blackwell to AWS isn’t about a single breakthrough—it’s about continuous innovation across multiple layers of infrastructure. By building on years of learning and innovation across compute, networking, operations, and managed services, we’ve brought NVIDIA Blackwell’s full capabilities with the reliability and performance customers expect from AWS.

### Robust instance security and stability

When customers tell me why they choose to run their GPU workloads on AWS, one crucial point comes up consistently: they highly value our focus on instance security and stability in the cloud. The specialized hardware, software, and firmware of the [AWS Nitro System](https://aws.amazon.com/ec2/nitro/) are designed to enforce restrictions so that nobody, including anyone in AWS, can access your sensitive AI workloads and data. Beyond security, the Nitro System fundamentally changes how we maintain and optimize infrastructure. The Nitro System, which handles networking, storage, and other I/O functions, makes it possible to deploy firmware updates, bug fixes, and optimizations while it remains operational. This ability to update without system downtime, which we call *live update*, is crucial in today’s AI landscape, where any interruption significantly impacts production timelines. P6e-GB200 and P6-B200 both feature the sixth generation of the Nitro System, but these security and stability benefits aren’t new—our innovative Nitro architecture has been protecting and optimizing [Amazon Elastic Compute Cloud](http://aws.amazon.com/ec2) (Amazon EC2) workloads since 2017.

### Reliable performance at massive scale

In AI infrastructure, the challenge isn’t just reaching massive scale—it’s delivering consistent performance and reliability at that scale. We’ve deployed P6e-GB200 UltraServers in third-generation EC2 UltraClusters, which creates a single fabric that can encompass our largest data centers. Third-generation UltraClusters cut power consumption by up to 40% and reduce cabling requirements by more than 80%—not only improving efficiency, but also significantly reducing potential points of failure.

To deliver consistent performance at this massive scale, we use [Elastic Fabric Adapter](https://aws.amazon.com/hpc/efa/) (EFA) with its Scalable Reliable Datagram protocol, which intelligently routes traffic across multiple network paths to maintain smooth operation even during congestion or failures. We’ve continuously improved EFA’s performance across four generations. P6e-GB200 and P6-B200 instances with EFAv4 show up to 18% faster collective communications in distributed training compared to P5en instances that use EFAv3.

### Infrastructure efficiency

Whereas P6-B200 instances use our proven air-cooling infrastructure, P6e-GB200 UltraServers use liquid cooling, which enables higher compute density in large NVLink domain architectures, delivering higher system performance. P6e-GB200 are liquid cooled with novel mechanical cooling solutions providing configurable liquid-to-chip cooling in both new and existing data centers, so we can support both liquid-cooled accelerators and air-cooled network and storage infrastructure in the same facility. With this flexible cooling design, we can deliver maximum performance and efficiency at the lowest cost.

## Getting started with NVIDIA Blackwell on AWS

We’ve made it simple to get started with P6e-GB200 UltraServers and P6-B200 instances through multiple deployment paths, so you can quickly begin using Blackwell GPUs while maintaining the operational model that works best for your organization.

### Amazon SageMaker HyperPod

If you’re accelerating your AI development and want to spend less time managing infrastructure and cluster operations, that’s exactly where [Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker/hyperpod/) excels. It provides managed, resilient infrastructure that automatically handles provisioning and management of large GPU clusters. We keep enhancing SageMaker HyperPod, adding innovations like flexible training plans to help you gain predictable training timelines and run training workloads within your budget requirements.

SageMaker HyperPod will support both P6e-GB200 UltraServers and P6-B200 instances, with optimizations to maximize performance by keeping workloads within the same NVLink domain. We’re also building in a comprehensive, multi-layered recovery system: SageMaker HyperPod will automatically replace faulty instances with preconfigured spares in the same NVLink domain. Built-in dashboards will give you visibility into everything from GPU utilization and memory usage to workload metrics and UltraServer health status.

### Amazon EKS

For large-scale AI workloads, if you prefer to manage your infrastructure using Kubernetes, [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS) is often the control plane of choice. We continue to drive innovations in Amazon EKS with capabilities like [Amazon EKS Hybrid Nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-overview.html), which enable you to manage both on-premises and EC2 GPUs in a single cluster—delivering flexibility for AI workloads.

Amazon EKS will support both P6e-GB200 UltraServers and P6-B200 instances with automated provisioning and lifecycle management through managed node groups. For P6e-GB200 UltraServers, we’re building in topology awareness that understands the GB200 NVL72 architecture, automatically labeling nodes with their UltraServer ID and network topology information to enable optimal workload placement. You will be able to span node groups across multiple UltraServers or dedicate them to individual UltraServers, giving you flexibility in organizing your training infrastructure. Amazon EKS monitors GPU and accelerator errors and relays them to the Kubernetes control plane for optional remediation.

### NVIDIA DGX Cloud on AWS

P6e-GB200 UltraServers will also be available through NVIDIA DGX Cloud. DGX Cloud is a unified AI platform optimized at every layer with multi-node AI training and inference capabilities and NVIDIA’s complete AI software stack. You benefit from NVIDIA’s latest optimizations, benchmarking recipes, and technical expertise to improve efficiency and performance. It offers flexible term lengths along with comprehensive NVIDIA expert support and services to help you accelerate your AI initiatives.

This launch announcement is an important milestone, and it’s just the beginning. As AI capabilities evolve rapidly, you need infrastructure built not just for today’s demands but for all the possibilities that lie ahead. With innovations across compute, networking, operations, and managed services, P6e-GB200 UltraServers and P6-B200 instances are ready to enable these possibilities. We can’t wait to see what you will build with them.

## Resources

* [AWS News Blog: P6e-GB200 UltraServers](https://aws.amazon.com/blogs/aws/new-amazon-ec2-p6e-gb200-ultraservers-powered-by-nvidia-grace-blackwell-gpus-for-the-highest-ai-performance)
* [AWS News Blog: P6-B200 Instances](https://aws.amazon.com/blogs/aws/new-amazon-ec2-p6-b200-instances-powered-by-nvidia-blackwell-gpus-to-accelerate-ai-innovations/)

---

### About the author

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/07/09/dbrown-1.jpg)**David Brown** is the Vice President of AWS Compute and Machine Learning (ML) Services. In this role he is responsible for building all AWS Compute and ML services, including Amazon EC2, Amazon Container Services, AWS Lambda, Amazon Bedrock and Amazon SageMaker. These services are used by all AWS customers but also underpin most of AWS’s internal Amazon applications. He also leads newer solutions, such as AWS Outposts, that bring AWS services into customers’ private data centers.

David joined AWS in 2007 as a Software Development Engineer based in Cape Town, South Africa, where he worked on the early development of Amazon EC2. In 2012, he relocated to Seattle and continued to work in the broader Amazon EC2 organization. Over the last 11 years, he has taken on larger leadership roles as more of the AWS compute and ML products have become part of his organization.

Prior to joining Amazon, David worked as a Software Developer at a financial industry startup. He holds a Computer Science & Economics degree from the Nelson Mandela University in Port Elizabeth, South Africa.

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