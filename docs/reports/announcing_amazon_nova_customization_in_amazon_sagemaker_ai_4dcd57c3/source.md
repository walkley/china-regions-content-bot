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

## [AWS News Blog](https://aws.amazon.com/blogs/aws/)

# Announcing Amazon Nova customization in Amazon SageMaker AI

by Betty Zheng (郑予彬) on 16 JUL 2025 in [Amazon Nova](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-nova/ "View all posts in Amazon Nova"), [Amazon SageMaker](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/sagemaker/ "View all posts in Amazon SageMaker"), [Amazon SageMaker AI](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/sagemaker/amazon-sagemaker-ai/ "View all posts in Amazon SageMaker AI"), [Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/sagemaker/amazon-sagemaker-hyperpod/ "View all posts in Amazon SageMaker HyperPod"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS Summit New York](https://aws.amazon.com/blogs/aws/category/events/aws-summit-new-york/ "View all posts in AWS Summit New York"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Generative AI](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/announcing-amazon-nova-customization-in-amazon-sagemaker-ai/)  [Comments](https://aws.amazon.com/blogs/aws/announcing-amazon-nova-customization-in-amazon-sagemaker-ai/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing a suite of [customization capabilities for Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/customization) in [Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/). Customers can now customize Nova Micro, Nova Lite, and Nova Pro across the model training lifecycle, including pre-training, supervised fine-tuning, and alignment. These techniques are available as ready-to-use Amazon SageMaker recipes with seamless deployment to [Amazon Bedrock](https://aws.amazon.com/bedrock/?nc2=h_prod_ai_br), supporting both on-demand and provisioned throughput inference.

[Amazon Nova foundation models](https://aws.amazon.com/ai/generative-ai/nova/?trk=24a8f13a-f5db-4127-bcb7-8b2876aa4265&sc_channel=ps&ef_id=Cj0KCQjwss3DBhC3ARIsALdgYxOMi3hzAIPtezk6e1xLdsi6Z3LjeLtVdvjyVOHQdScISGz6HYntVasaAknPEALw_wcB:G:s&s_kwcid=AL!4422!3!692062155755!e!!g!!amazon%20nova!21058131112!157173586257&gad_campaignid=21058131112&gclid=Cj0KCQjwss3DBhC3ARIsALdgYxOMi3hzAIPtezk6e1xLdsi6Z3LjeLtVdvjyVOHQdScISGz6HYntVasaAknPEALw_wcB) power diverse generative AI use cases across industries. As customers scale deployments, they need models that reflect proprietary knowledge, workflows, and brand requirements. Prompt optimization and [retrieval-augmented generation (RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/) work well for integrating general-purpose foundation models into applications, however business-critical workflows require model customization to meet specific accuracy, cost, and latency requirements.

**Choosing the right customization technique**

Amazon Nova models support a range of customization techniques including: 1) supervised fine-tuning, 2) alignment, 3) continued pre-training, and 4) knowledge distillation. The optimal choice depends on goals, use case complexity, and the availability of data and compute resources. You can also combine multiple techniques to achieve your desired outcomes with the preferred mix of performance, cost, and flexibility.

**Supervised fine-tuning (SFT)** customizes model parameters using a training dataset of input-output pairs specific to your target tasks and domains. Choose from the following two implementation approaches based on data volume and cost considerations:

* **Parameter-efficient fine-tuning (PEFT)** — updates only a subset of model parameters through lightweight adapter layers such as LoRA (Low-Rank Adaptation). It offers faster training and lower compute costs compared to full fine-tuning. PEFT-adapted Nova models are imported to Amazon Bedrock and invoked using on-demand inference.
* **Full fine-tuning (FFT)** — updates all the parameters of the model and is ideal for scenarios when you have extensive training datasets (tens of thousands of records). Nova models customized through FFT can also be imported to Amazon Bedrock and invoked for inference with provisioned throughput.

**Alignment** steers the model output towards desired preferences for product-specific needs and behavior, such as company brand and customer experience requirements. These preferences may be encoded in multiple ways, including empirical examples and policies. Nova models support two preference alignment techniques:

* **Direct preference optimization (DPO)** — offers a straightforward way to tune model outputs using preferred/not preferred response pairs. DPO learns from comparative preferences to optimize outputs for subjective requirements such as tone and style. DPO offers both a parameter-efficient version and a full-model update version. The parameter-efficient version supports on-demand inference.
* **Proximal policy optimization (PPO)** — uses reinforcement learning to enhance model behavior by optimizing for desired rewards such as helpfulness, safety, or engagement. A reward model guides optimization by scoring outputs, helping the model learn effective behaviors while maintaining previously learned capabilities.

**Continued pre-training (CPT)** expands foundational model knowledge through self-supervised learning on large quantities of unlabeled proprietary data, including internal documents, transcripts, and business-specific content. CPT followed by SFT and alignment through DPO or PPO provides a comprehensive way to customize Nova models for your applications.

**Knowledge distillation** transfers knowledge from a larger “teacher” model to a smaller, faster, and more cost-efficient “student” model. Distillation is useful in scenarios where customers do not have adequate reference input-output samples and can leverage a more powerful model to augment the training data. This process creates a customized model of teacher-level accuracy for specific use cases and student-level cost-effectiveness and speed.

Here is a table summarizing the available customization techniques across different modalities and deployment options. Each technique offers specific training and inference capabilities depending on your implementation requirements.

| Recipe | Modality | Training | | Inference | |
| --- | --- | --- | --- | --- | --- |
| **Amazon Bedrock** | **Amazon SageMaker** | **Amazon Bedrock On-demand** | **Amazon Bedrock Provisioned Throughput** |
| Supervised fine tuning | Text, image, video |  |  |  |  |
| Parameter-efficient fine-tuning (PEFT) |  | ✅ | ✅ | ✅ | ✅ |
| Full fine-tuning |  |  | ✅ |  | ✅ |
| **Direct preference optimization (DPO)** | Text, image |  |  |  |  |
| Parameter-efficient DPO |  |  | ✅ | ✅ | ✅ |
| Full model DPO |  |  | ✅ |  | ✅ |
| **Proximal policy optimization (PPO)** | Text-only |  | ✅ |  | ✅ |
| **Continuous pre-training** | Text-only |  | ✅ |  | ✅ |
| **Distillation** | Text-only | ✅ | ✅ | ✅ | ✅ |

Early access customers, including Cosine AI, Massachusetts Institute of Technology (MIT) Computer Science and Artificial Intelligence Laboratory (CSAIL), Volkswagen, Amazon Customer Service, and Amazon Catalog Systems Service, are already successfully using Amazon Nova customization capabilities.

**Customizing Nova models in action**

The following walks you through an example of customizing the Nova Micro model using direct preference optimization on an existing preference dataset. To do this, you can use [Amazon SageMaker Studio](https://aws.amazon.com/sagemaker-ai/studio/).

Launch your SageMaker Studio in the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/home#/studio) and choose **JumpStart**, a machine learning (ML) hub with foundation models, built-in algorithms, and pre-built ML solutions that you can deploy with a few clicks.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/14/Screenshot-2025-07-15-at-01.07.18.png)

Then, choose **Nova Micro**, a text-only model that delivers the lowest latency responses at the lowest cost per inference among the Nova model family, and then choose **Train**.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/14/nova-customization-in-sagemaker-step-2.png)

Next, you can choose a **fine-tuning** recipe to train the model with labeled data to enhance performance on specific tasks and align with desired behaviors. Choosing the **Direct Preference Optimization** offers a straightforward way to tune model outputs with your preferences.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/14/2025-nova-customization-in-sagemaker-step-3-1.png)

When you choose **Open sample notebook**, you have two environment options to run the recipe: either on the SageMaker training jobs or SageMaker Hyperpod:

Choose **Run recipe on** **SageMaker training jobs** when you don’t need to create a cluster and train the model with the sample notebook by selecting your JupyterLab space.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/16/nova-customization-in-sagemaker-step-4-1.png)

Alternately, if you want to have a persistent cluster environment optimized for iterative training processes, choose **Run recipe on SageMaker HyperPod**. You can choose a HyperPod EKS cluster with at least one restricted instance group (RIG) to provide a specialized isolated environment, which is required for such Nova model training. Then, choose your JupyterLabSpace and **Open sample notebook**.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/15/nova-customization-in-sagemaker-step-5-1.png)

This notebook provides an end-to-end walkthrough for creating a SageMaker HyperPod job using a SageMaker Nova model with a recipe and deploying it for inference. With the help of a SageMaker HyperPod recipe, you can streamline complex configurations and seamlessly integrate datasets for optimized training jobs.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/14/nova-customization-in-sagemaker-step-6.jpg)

In SageMaker Studio, you can see that your SageMaker HyperPod job has been successfully created and you can monitor it for further progress.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/14/2025-nova-customization-in-sagemaker-step-7-1.png)

After your job completes, you can use a benchmark recipe to evaluate if the customized model performs better on agentic tasks.

For comprehensive documentation and additional example implementations, visit the [SageMaker HyperPod recipes repository on GitHub.](https://github.com/aws/sagemaker-hyperpod-recipes) We continue to expand the recipes based on customer feedback and emerging ML trends, ensuring you have the tools needed for successful AI model customization.

**Availability and getting started**

Recipes for Amazon Nova on Amazon SageMaker AI are available in US East (N. Virginia). Learn more about this feature by visiting the [Amazon Nova customization webpage](https://aws.amazon.com/ai/generative-ai/nova/customization/) and [Amazon Nova user guide](https://docs.aws.amazon.com/nova/latest/userguide/customization.html) and get started in the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/home#/studio).

–[Betty](https://www.linkedin.com/in/zhengyubin714/)

*Updated on July 16, 2025 – Revised the table data and console screenshot.*

![Betty Zheng (郑予彬)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2024/06/12/形象照-betty-0181-scaled-e1718178653724.jpg)

### Betty Zheng (郑予彬)

Betty Zheng is a Senior Developer Advocate at AWS, focusing on developer-centric content across Cloud Native, Cloud Security, and Generative AI technologies. With over 20 years of experience in the ICT industry and 18 years as an application architect and cloud infrastructure expert, she actively engages with the Chinese developer community, helping developers understand AWS technologies and transform their ideas into execution.

Loading comments…

### Resources

* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [What's New](https://aws.amazon.com/new?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [Top Posts](https://aws.amazon.com/blogs?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [Official AWS Podcast](https://aws.amazon.com/podcasts/aws-podcast?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [Case Studies](https://aws.amazon.com/solutions/case-studies?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [AWS re:Post](https://repost.aws/ "https://repost.aws/")

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [RSS Feed](https://aws.amazon.com/blogs/aws/feed/)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-social)

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