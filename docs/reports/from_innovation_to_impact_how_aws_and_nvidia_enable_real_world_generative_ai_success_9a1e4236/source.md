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

# From innovation to impact: How AWS and NVIDIA enable real-world generative AI success

by Rahul Pathak on 19 MAR 2025 in [Generative AI](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI") [Permalink](https://aws.amazon.com/blogs/machine-learning/from-innovation-to-impact-how-aws-and-nvidia-enable-real-world-generative-ai-success/)  [Comments](https://aws.amazon.com/blogs/machine-learning/from-innovation-to-impact-how-aws-and-nvidia-enable-real-world-generative-ai-success/#Comments)  Share

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/19/AWS_-_NVIDIA_logo_lock_up.jpg)

As we gather for NVIDIA GTC, organizations of all sizes are at a pivotal moment in their AI journey. The question is no longer whether to adopt generative AI, but how to move from promising pilots to production-ready systems that deliver real business value. The organizations that figure this out first will have a significant competitive advantage—and we’re already seeing compelling examples of what’s possible.

Consider Hippocratic AI’s work to develop AI-powered clinical assistants to support healthcare teams as doctors, nurses, and other clinicians face unprecedented levels of burnout. During a recent hurricane in Florida, their system called 100,000 patients in a day to check on medications and provide preventative healthcare guidance–the kind of coordinated outreach that would be nearly impossible to achieve manually. They aren’t just building another chatbot; they are reimagining healthcare delivery at scale.

Production-ready AI like this requires more than just cutting-edge models or powerful GPUs. In my decade working with customers’ data journeys, I’ve seen that an organization’s most valuable asset is its domain-specific data and expertise. And now leading our data and AI go-to-market, I hear customers consistently emphasize what they need to transform their domain advantage into AI success: infrastructure and services they can trust—with performance, cost-efficiency, security, and flexibility—all delivered at scale. When the stakes are high, success requires not just cutting-edge technology, but the ability to operationalize it at scale—a challenge that AWS has consistently solved for customers. As the world’s most comprehensive and broadly adopted cloud, our partnership with NVIDIA’s pioneering accelerated computing platform for generative AI amplifies this capability. It’s inspiring to see how, together, we’re enabling customers across industries to confidently move AI into production.

In this post, I will share some of these customers’ remarkable journeys, offering practical insights for any organization looking to harness the power of generative AI.

## Transforming content creation with generative AI

Content creation represents one of the most visible and immediate applications of generative AI today. Adobe, a pioneer that has shaped creative workflows for over four decades, has moved with remarkable speed to integrate generative AI across its flagship products, helping millions of creators work in entirely new ways.

Adobe’s approach to generative AI infrastructure exemplifies what their VP of Generative AI, Alexandru Costin, calls an “AI superhighway”—a sophisticated technical foundation that enables rapid iteration of AI models and seamless integration into their creative applications. The success of their Firefly family of generative AI models, integrated across flagship products like Photoshop, demonstrates the power of this approach. For their AI training and inference workloads, Adobe uses NVIDIA GPU-accelerated [Amazon Elastic Compute Cloud](http://aws.amazon.com/ec2) (Amazon EC2) P5en (NVIDIA H200 GPUs), P5 (NVIDIA H100 GPUs), P4de (NVIDIA A100 GPUs), and G5 (NVIDIA A10G GPUs) instances. They also use NVIDIA software such as NVIDIA TensorRT and NVIDIA Triton Inference Server for faster, scalable inference. Adobe needed maximum flexibility to build their AI infrastructure, and AWS provided the complete stack of services needed—from [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/) for high-performance storage, to [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS) for container orchestration, to [Elastic Fabric Adapter](https://aws.amazon.com/hpc/efa/) (EFA) for high-throughput networking—to create a production environment that could reliably serve millions of creative professionals.

### Key takeaway

If you’re building and managing your own AI pipelines, Adobe’s success highlights a critical insight: although GPU-accelerated compute often gets the spotlight in AI infrastructure discussions, what’s equally important is the NVIDIA software stack along with the foundation of orchestration, storage, and networking services that enable production-ready AI. Their results speak for themselves—Adobe achieved a 20-fold scale-up in model training while maintaining the enterprise-grade performance and reliability their customers expect.

## Pioneering new AI applications from the ground up

Throughout my career, I’ve been particularly energized by startups that take on audacious challenges—those that aren’t just building incremental improvements but are fundamentally reimagining how things work. Perplexity exemplifies this spirit. They’ve taken on a technology most of us now take for granted: search. It’s the kind of ambitious mission that excites me, not just because of its bold vision, but because of the incredible technical challenges it presents. When you’re processing 340 million queries monthly and serving over 1,500 organizations, transforming search isn’t just about having great ideas—it’s about building robust, scalable systems that can deliver consistent performance in production.

Perplexity’s innovative approach earned them membership in both [AWS Activate](https://aws.amazon.com/activate/activate-landing/) and NVIDIA Inception—flagship programs designed to accelerate startup innovation and success. These programs provided them with the resources, technical guidance, and support needed to build at scale. They were one of the early adopters of [Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker/hyperpod/), and continue to use its distributed training capabilities to accelerate model training time by up to 40%. They use a highly optimized inference stack built with NVIDIA TensorRT-LLM and NVIDIA Triton Inference Server to serve both their search application and pplx-api, their public API service that gives developers access to their proprietary models. The results speak for themselves—their inference stack achieves up to 3.1 times lower latency compared to other platforms. Both their training and inference workloads run on NVIDIA GPU-accelerated EC2 P5 instances, delivering the performance and reliability needed to operate at scale. To give their users even more flexibility, Perplexity complements their own models with services such as [Amazon Bedrock](https://aws.amazon.com/bedrock/), and provides access to additional state-of-the-art models in their API. Amazon Bedrock offers ease of use and reliability, which are crucial for their team—as they note, it allows them to effectively maintain the reliability and latency their product demands.

What I find particularly compelling about Perplexity’s journey is their commitment to technical excellence, exemplified by their work optimizing GPU memory transfer with EFA networking. The team achieved 97.1% of the theoretical maximum bandwidth of 3200 Gbps and open sourced their innovations, enabling other organizations to benefit from their learnings.

For those interested in the technical details, I encourage you to read their fascinating post [Journey to 3200 Gbps: High-Performance GPU Memory Transfer on AWS Sagemaker Hyperpod.](https://www.perplexity.ai/hub/blog/high-performance-gpu-memory-transfer-on-aws)

### Key takeaway

For organizations with complex AI workloads and specific performance requirements, Perplexity’s approach offers a valuable lesson. Sometimes, the path to production-ready AI isn’t about choosing between self-hosted infrastructure and managed services—it’s about strategically combining both. This hybrid strategy can deliver both exceptional performance (evidenced by Perplexity’s 3.1 times lower latency) and the flexibility to evolve.

## Transforming enterprise workflows with AI

Enterprise workflows represent the backbone of business operations—and they’re a crucial proving ground for AI’s ability to deliver immediate business value. ServiceNow, which terms itself the AI platform for business transformation, is rapidly integrating AI to reimagine core business processes at scale.

ServiceNow’s innovative AI solutions showcase their vision for enterprise-specific AI optimization. As Srinivas Sunkara, ServiceNow’s Vice President, explains, their approach focuses on deep AI integration with technology workflows, core business processes, and CRM systems—areas where traditional large language models (LLMs) often lack domain-specific knowledge. To train generative AI models at enterprise scale, ServiceNow uses NVIDIA DGX Cloud on AWS. Their architecture combines high-performance FSx for Lustre storage with NVIDIA GPU clusters for training, and NVIDIA Triton Inference Server handles production deployment. This robust technology platform allows ServiceNow to focus on domain-specific AI development and customer value rather than infrastructure management.

### Key takeaway

ServiceNow offers an important lesson about enterprise AI adoption: while foundation models (FMs) provide powerful general capabilities, the greatest business value often comes from optimizing models for specific enterprise use cases and workflows. In many cases, it’s precisely this deliberate specialization that transforms AI from an interesting technology into a true business accelerator.

## Scaling AI across enterprise applications

Cisco’s Webex team’s journey with generative AI exemplifies how large organizations can methodically transform their applications while maintaining enterprise standards for reliability and efficiency. With a comprehensive suite of telecommunications applications serving customers globally, they needed an approach that would allow them to incorporate LLMs across their portfolio—from AI assistants to speech recognition—without compromising performance or increasing operational complexity.

The Webex team’s key insight was to separate their models from their applications. Previously, they had embedded AI models into the container images for applications running on Amazon EKS, but as their models grew in sophistication and size, this approach became increasingly inefficient. By migrating their LLMs to [Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/) and using NVIDIA Triton Inference Server, they created a clean architectural break between their relatively lean applications and the underlying models, which require more substantial compute resources. This separation allows applications and models to scale independently, significantly reducing development cycle time and increasing resource utilization. The team deployed dozens of models on SageMaker AI endpoints, using Triton Inference Server’s model concurrency capabilities to scale globally across AWS data centers.

The results validate Cisco’s methodical approach to AI transformation. By separating applications from models, their development teams can now fix bugs, perform tests, and add features to applications much faster, without having to manage large models in their workstation memory. The architecture also enables significant cost optimization—applications remain available during off-peak hours for reliability, and model endpoints can scale down when not needed, all without impacting application performance. Looking ahead, the team is evaluating Amazon Bedrock to further improve their price-performance, demonstrating how thoughtful architecture decisions create a foundation for continuous optimization.

### Key takeaway

For enterprises with large application portfolios looking to integrate AI at scale, Cisco’s methodical approach offers an important lesson: separating LLMs from applications creates a cleaner architectural boundary that improves both development velocity and cost optimization. By treating models and applications as independent components, Cisco significantly improved development cycle time while reducing costs through more efficient resource utilization.

## Building mission-critical AI for healthcare

Earlier, we highlighted how Hippocratic AI reached 100,000 patients during a crisis. Behind this achievement lies a story of rigorous engineering for safety and reliability—essential in healthcare where stakes are extraordinarily high.

Hippocratic AI’s approach to this challenge is both innovative and rigorous. They’ve developed what they call a “constellation architecture”—a sophisticated system of over 20 specialized models working in concert, each focused on specific safety aspects like prescription adherence, lab analysis, and over-the-counter medication guidance. This distributed approach to safety means they have to train multiple models, requiring management of significant computational resources. That’s why they use SageMaker HyperPod for their training infrastructure, using [Amazon FSx](https://aws.amazon.com/fsx/) and [Amazon Simple Storage Service](http://aws.amazon.com/s3) (Amazon S3) for high-speed storage access to NVIDIA GPUs, while Grafana and Prometheus provide the comprehensive monitoring needed to provide optimal GPU utilization. They build upon NVIDIA’s low-latency inference stack, and are enhancing conversational AI capabilities using NVIDIA Riva models for speech recognition and text-to-speech translation, and are also using NVIDIA NIM microservices to deploy these models. Given the sensitive nature of healthcare data and HIPAA compliance requirements, they’ve implemented a sophisticated multi-account, multi-cluster strategy on AWS—running production inference workloads with patient data on completely separate accounts and clusters from their development and training environments. This careful attention to both security and performance allows them to handle thousands of patient interactions while maintaining precise control over clinical safety and accuracy.

The impact of Hippocratic AI’s work extends far beyond technical achievements. Their AI-powered clinical assistants address critical healthcare workforce burnout by handling burdensome administrative tasks—from pre-operative preparation to post-discharge follow-ups. For example, during weather emergencies, their system can rapidly assess heat risks and coordinate transport for vulnerable patients—the kind of comprehensive care that would be too burdensome and resource-intensive to coordinate manually at scale.

### Key takeaway

For organizations building AI solutions for complex, regulated, and high-stakes environments, Hippocratic AI’s constellation architecture reinforces what we’ve consistently emphasized: there’s rarely a one-size-fits-all model for every use case. Just as Amazon Bedrock offers a choice of models to meet diverse needs, Hippocratic AI’s approach of combining over 20 specialized models—each focused on specific safety aspects—demonstrates how a thoughtfully designed ensemble can achieve both precision and scale.

## Conclusion

As the technology partners enabling these and countless other customer innovations, AWS and NVIDIA’s long-standing collaboration continues to evolve to meet the demands of the generative AI era. Our partnership, which began over 14 years ago with the world’s first GPU cloud instance, has grown to offer the industry’s widest range of NVIDIA accelerated computing solutions and software services for optimizing AI deployments. Through initiatives like Project Ceiba—one of the world’s fastest AI supercomputers hosted exclusively on AWS using NVIDIA DGX Cloud for NVIDIA’s own research and development use—we continue to push the boundaries of what’s possible.

As all the examples we’ve covered illustrate, it isn’t just about the technology we build together—it’s how organizations of all sizes are using these capabilities to transform their industries and create new possibilities. These stories ultimately reveal something more fundamental: when we make powerful AI capabilities accessible and reliable, people find remarkable ways to use them to solve meaningful problems. That’s the true promise of our partnership with NVIDIA—enabling innovators to create positive change at scale. I’m excited to continue inventing and partnering with NVIDIA and can’t wait to see what our mutual customers are going to do next.

## Resources

Check out the following resources to learn more about our partnership with NVIDIA and generative AI on AWS:

* Learn about the [AWS and NVIDIA partnership](https://aws.amazon.com/nvidia/)
* [Explore generative AI on AWS](https://aws.amazon.com/generative-ai/)
* Cost-effectively access NVIDIA GPUs across several new AWS Regions with [Amazon EC2 Capacity Blocks for ML](https://aws.amazon.com/ec2/capacityblocks/pricing/)
* Get started with [Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker-ai/hyperpod/) for generative AI model development
* Build and scale generative AI applications with [Amazon Bedrock](https://aws.amazon.com/bedrock/)

---

### About the Author

**![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2023/07/25/rahul-pathak.jpg) Rahul Pathak** is Vice President Data and AI GTM at AWS, where he leads the global go-to-market and specialist teams who are helping customers create differentiated value with AWS’s AI and capabilities such as Amazon Bedrock, Amazon Q, Amazon SageMaker, and Amazon EC2 and Data Services such as Amaqzon S3, AWS Glue and Amazon Redshift. Rahul believes that generative AI will transform virtually every single customer experience and that data is a key differentiator for customers as they build AI applications. Prior to his current role, he was Vice President, Relational Database Engines where he led Amazon Aurora, Redshift, and DSQL . During his 13+ years at AWS, Rahul has been focused on launching, building, and growing managed database and analytics services, all aimed at making it easy for customers to get value from their data. Rahul has over twenty years of experience in technology and has co-founded two companies, one focused on analytics and the other on IP-geolocation. He holds a degree in Computer Science from MIT and an Executive MBA from the University of Washington.

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