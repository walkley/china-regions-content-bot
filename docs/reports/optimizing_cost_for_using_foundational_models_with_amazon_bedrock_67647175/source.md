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

## [AWS Cloud Financial Management](https://aws.amazon.com/blogs/aws-cloud-financial-management/)

# Optimizing cost for using foundational models with Amazon Bedrock

by Adam Richter and [Bowen Wang](https://aws.amazon.com/blogs/aws-cloud-financial-management/author/bowewang/ "Posts by Bowen Wang") on 22 APR 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Bedrock Guardrails](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-bedrock-guardrails/ "View all posts in Amazon Bedrock Guardrails"), [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-bedrock-knowledge-bases/ "View all posts in Amazon Bedrock Knowledge Bases"), [Artificial Intelligence](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [AWS Cloud Financial Management](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/aws-cloud-financial-management/ "View all posts in AWS Cloud Financial Management"), [Best Practices](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/post-types/best-practices/ "View all posts in Best Practices"), [Generative AI](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/generative-ai-2/ "View all posts in Generative AI") [Permalink](https://aws.amazon.com/blogs/aws-cloud-financial-management/optimizing-cost-for-using-foundational-models-with-amazon-bedrock/) Share

*This post was made better through reviews from Andrew Shamiya and Zhibin Cao.*

As we continue our five-part series on optimizing costs for generative AI workloads on AWS, our third blog shifts focus to Amazon Bedrock. In our previous posts, we explored general [Cloud Financial Management principles on generative AI adoption](https://aws.amazon.com/blogs/aws-cloud-financial-management/optimizing-cost-for-generative-ai-with-aws/) and strategies for custom model development using [Amazon EC2 and Amazon SageMaker AI](https://aws.amazon.com/blogs/aws-cloud-financial-management/optimizing-cost-for-developing-custom-ai-models-with-amazon-ec2-and-sagemaker-ai/). Today, we’ll guide you through cost optimization techniques for Amazon Bedrock. We’ll explore making informed decisions about pricing options, model selection, knowledge base optimization, prompt caching, and automated reasoning. Whether you’re just starting with foundation models or looking to optimize your existing Amazon Bedrock implementation, these techniques will help you balance capability and cost while leveraging the convenience of managed AI models.

## What is Amazon Bedrock?

Amazon Bedrock is a fully managed service that provides access to leading foundation models (FMs) from multiple AI companies through a unified API. This enables developers to build and scale generative AI applications without managing complex infrastructure. Key benefits include seamless model switching, enterprise-grade security and privacy controls, customization capabilities through model fine-tuning, and direct integration with AWS services. Amazon Bedrock offers several powerful levers to help you balance cost and performance.

## Inference, the New Building Block in Modern Applications

At re:Invent 2024, our CEO Matt Garman introduced a paradigm shift in how we think about application architecture: positioning [inference](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-how.html) as a fundamental building block of modern applications, alongside traditional components like compute, storage, and databases (listen to Matt’s keynote presentation, [AWS re:Invent 2024 – CEO Keynote with Matt Garman](https://www.youtube.com/watch?v=LY7m5LQliAo&t=4348s)). As you increasingly embed generative AI capabilities into your operational workflows, managing and optimizing inference costs will become as crucial as traditional cloud cost management. To support this evolution, AWS introduced [inference-level Cost Allocation Tags](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-bedrock-cost-allocation-tags-inference-profiles), providing granular visibility into inference spend. This enhanced monitoring capability enables you to visualize and analyze cost at the inference level, set and manage budgets specifically for your AI workloads, and make data-driven decisions on model selection and usage. In the following sections, we’ll explore practical cost optimization techniques that can help you lower your inference cost.

## Flexible Pricing Models for Every Use Case

Amazon Bedrock’s flexible [pricing model](https://aws.amazon.com/bedrock/pricing/) encompasses three key options: 1) **On-Demand** for pay-as-you-go flexibility, 2) **Provisioned Throughput** offering savings through one or six month commitments (depending on usage patterns), and 3) **batch processing** which can offer up to a 50% lower price when compared to on-demand. Selecting the optimal pricing option is crucial for your success as it directly impacts financial outcomes and operational efficiency. You can optimize spend while maintaining service quality by choosing the most appropriate option: On-Demand for variable workloads, Provisioned Throughput for consistent usage patterns, or Batch processing for non-time-sensitive operations. This flexibility supports various stages of AI implementation and enables proper resource allocation, prevents over-provisioning, and ensures better budget predictability. Making an informed pricing decision is essential, as the wrong choice could lead to unnecessary expenses that impact both operational efficiency and bottom-line results.

## Strategic Model Selection

![List of currently supported Bedrock models](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/04/21/bedrock_models-1024x299.png)

Figure 1. Amazon Bedrock offers the broadest selection of fully managed models from leading AI companies.

Model selection in Amazon Bedrock is a strategic decision that can impact cost, efficiency, and performance outcomes. Amazon Bedrock provides access to diverse foundation models from industry leaders like Anthropic, Meta, Mistral AI, and Amazon. In addition to the models available from those providers, you can leverage 100+ other models in the Amazon Bedrock Marketplace. Rather than committing to a single model or provider, you can leverage Amazon Bedrock’s flexibility to seamlessly switch between models with minimal code modifications. As newer, more efficient models are released, you can easily switch for cost savings and increased performance. The platform’s batch processing capabilities further enhance this advantage by enabling continuous evaluation of new models as they become available, ensuring solutions remain optimized over time and maintain competitive advantages in rapidly evolving AI landscapes. This strategic approach to model diversity and evaluation helps you maximize your AI investments while maintaining operational agility.

Another consideration, when selecting a model, is response time. Some Amazon Bedrock models support latency optimized configurations, see [Optimize model inference for latency](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html), which deliver faster response times compared to standard performance. These models improve efficiency and make your generative AI applications more responsive. You can currently use latency optimized configurations for Amazon Nova Pro, Anthropic’s Claude 3.5 Haiku, and Meta’s Llama 3.1 405B and 70B, running them faster on AWS than anywhere else.

## Leveraging Knowledge Bases

Amazon Bedrock supports the inclusion of Knowledge Bases that enable you to create highly accurate, low-latency, secure, and custom generative AI applications by incorporating contextual information from your own data sources. Knowledge Bases, also known as RAG (retrieval augmented generation), can lead to more accurate, relevant, and up-to-date responses. Utilizing Knowledge Bases helps you get higher quality answers which will drive cost savings through a reduction in the number of prompts and responses needed to get a relevant answer. The key to optimizing Knowledge Bases is to manage the data and indexing frequency. Indexing fees are the primary cost driver and they are charged per object, or OpenSearch Compute Unit (OCU) hour, depending on the vector database. The three things you can do to minimize these costs are:

1. Include only relevant data in your data source(s) to avoid indexing data that will not contribute to your solution
2. Avoid updating or modifying files that are already indexed. If a file is modified, it will cause that file to be re-indexed which will incur additional charges.
3. Remove data that is no longer needed to simplify your index. This will reduce the total indexing costs and speed up requests against the indexed data.

By following these practices, you can achieve cost reductions and faster indexing for your knowledge base deployments.

![Amazon Bedrock user queries go through an augmentation progress with data from knowledge bases. ](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/04/21/bedrock_kb-1024x282.png)

Figure 2. Amazon Bedrock has native support for Retrieval Augmented Generation (RAG)

## Customization for Enhanced Performance

Recent advances in fine-tuning capabilities have made it easier than ever to optimize model performance. You can now [customize and fine-tune models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html), using your data, and without needing to writing code. This reduces the need for continuous model retraining and results in a more efficient, less costly, solution to operate because of the higher quality output.

## Distillation for More Cost-Efficient Performance

Amazon Bedrock’s [Model Distillation](https://aws.amazon.com/bedrock/model-distillation/) feature represents an opportunity to balance performance with efficiency. Through a sophisticated knowledge transfer process from larger “teacher” models to smaller “student” models, this technology enables you to achieve optimization without significantly compromising accuracy. This process produces distilled models that can operate up to 500% faster and costs up to 75% less than the original counterpart with less than 2% accuracy loss for use cases like RAG. This feature addresses the traditional trade-off between model capability and operational efficiency, making advanced AI applications more accessible and economically viable for budgets of all sizes.

![Amazon Bedrock Model Distillation](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/04/21/bedrock_distill-1024x338.png)

Figure 3. Match the performance of advanced models with cost-efficient models for your use case with Model Distillation

## Prompt Caching for Cost and Latency Reduction

Amazon Bedrock’s [prompt caching](https://aws.amazon.com/bedrock/prompt-caching/) capability delivers exceptional cost and performance benefits. By intelligently caching frequently used prompts across multiple API calls, this feature eliminates the need to re-process identical requests. This results in up to 90% reduction in costs and 85% decrease in latency for supported models. Prompt Caching works by reusing cached prompt prefixes, bypassing the need for reprocessing of matching prefixes, thereby significantly reducing the computational resources required for generating outputs while maintaining the quality of responses. This optimization makes enterprise-scale AI implementations more economically viable and responsive.

## Automated Reasoning to Improve Accuracy

Through the integration of [Automated Reasoning](https://aws.amazon.com/bedrock/guardrails/), Amazon Bedrock presents a chance to improve generative AI accuracy and cost optimization. Automated Reasoning is available through Amazon Bedrock Guardrails and it employs mathematical methods to guarantee accuracy in strategic areas like human resources, finance, and compliance. This mathematical proof process not only increases the response reliability but also improves the operational efficiency. This efficiency is accomplished by decreasing the number of prompts that you have to give in order to get an accurate response. Moreover, by offering a proof of accuracy and a logical explanation for every response, the system enables you to speed up your AI adoption in accuracy critical use cases while not spending the resources that are usually put into manual verification and error correction. When a combination of improved accuracy, low interaction cost, and verification are factored in, the cost savings can be significant.

## Conclusion

By implementing the above optimization strategies, you can significantly reduce costs while maintaining or improving performance. The key is to continuously evaluate and adjust your approach as new capabilities become available. The flexibility and comprehensive feature set of Amazon Bedrock make it an ideal platform when looking to optimize your generative AI implementation.

We’ve covered various approaches to optimize your Amazon Bedrock generative AI application development costs. In our next post, we’ll explore cost optimization strategies for Amazon Q, including pricing tier selection, user management, and content indexing. Join us to learn how to make the most of AWS’s AI-powered assistant while maintaining cost efficiency.

![Adam Richter](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/03/12/adaricht_avatar.jpg)

### Adam Richter

Adam Richter is a Senior Optimization Solutions Architect with AWS OPTICS, where he focuses on AI cost optimization and FinOps best practices. He has helped shape customer-facing features such as Amazon Q Business and Amazon Q Developer, and frequently shares his expertise as a speaker at AWS re:Invent and other industry events. Adam also represents AWS in the FinOps Foundation AI Working Group, contributing to the broader conversation on financial operations in AI.

![Bowen Wang](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2023/10/23/2023ProfileBW-small.jpg)

### [Bowen Wang](https://aws.amazon.com/blogs/aws-cloud-financial-management/author/bowewang/ "Posts by Bowen Wang")

Bowen is a Principal Product Marketing Manager for AWS Billing and Cost Management services. She focuses on enabling finance and business leaders to better understand the value of the cloud and ways to optimize their cloud financial management. In her previous career, she helped a tech start up enter the Chinese market.

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