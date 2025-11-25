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

# DeepSeek-R1 models now available on AWS

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 30 JAN 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Machine Learning](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Amazon SageMaker](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/sagemaker/ "View all posts in Amazon SageMaker"), [Amazon SageMaker AI](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/sagemaker/amazon-sagemaker-ai/ "View all posts in Amazon SageMaker AI"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/deepseek-r1-models-now-available-on-aws/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

***Updated on March 10, 2025** — DeepSeek-R1 now available as a [fully managed serverless model](https://aws.amazon.com/blogs/aws/deepseek-r1-now-available-as-a-fully-managed-serverless-model-in-amazon-bedrock/) in Amazon Bedrock*

***Updated on February 5, 2025** — DeepSeek-R1 Distill Llama and Qwen models are now available in Amazon Bedrock Marketplace and Amazon SageMaker JumpStart.*

During this past AWS re:Invent, Amazon CEO Andy Jassy [shared valuable lessons learned](https://youtu.be/LY7m5LQliAo?feature=shared&t=6291) from Amazon’s own experience developing nearly 1,000 [generative AI](https://aws.amazon.com/ai/generative-ai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) applications across the company. Drawing from this extensive scale of AI deployment, Jassy offered three key observations that have shaped Amazon’s approach to enterprise AI implementation.

> First is that as you get to scale in generative AI applications, the cost of compute really matters. People are very hungry for better price performance. The second is actually quite difficult to build a really good generative AI application. The third is the diversity of the models being used when we gave our builders freedom to pick what they want to do. It doesn’t surprise us, because we keep learning the same lesson over and over and over again, which is that there is never going to be one tool to rule the world.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/01/30/2025-deepseek-r1-on-aws-1-andy-keynote.png)

As Andy emphasized, a broad and deep range of models provided by Amazon empowers customers to choose the precise capabilities that best serve their unique needs. By closely monitoring both customer needs and technological advancements, AWS regularly expands our curated selection of models to include promising new models alongside established industry favorites. This ongoing expansion of high-performing and differentiated model offerings helps customers stay at the forefront of AI innovation.

This leads us to Chinese AI startup [DeepSeek](https://www.deepseek.com/). DeepSeek launched [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) on December 2024 and subsequently released [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1), DeepSeek-R1-Zero with 671 billion parameters, and DeepSeek-R1-Distill models ranging from 1.5–70 billion parameters on January 20, 2025. They added their vision-based [Janus-Pro-7B](https://github.com/deepseek-ai/Janus) model on January 27, 2025. The models are publicly available and are [reportedly 90-95% more affordable and cost-effective than comparable models](https://venturebeat.com/ai/open-source-deepseek-r1-uses-pure-reinforcement-learning-to-match-openai-o1-at-95-less-cost/). Per Deepseek, their model stands out for its reasoning capabilities, achieved through innovative training techniques such as reinforcement learning.

**Today, you can now deploy DeepSeek-R1 models in [Amazon Bedrock](https://aws.amazon.com/bedrock/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and [Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)**. Amazon Bedrock is best for teams seeking to quickly integrate pre-trained foundation models through APIs. Amazon SageMaker AI is ideal for organizations that want advanced customization, training, and deployment, with access to the underlying infrastructure. Additionally, you can also use [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) to deploy DeepSeek-R1-Distill models cost-effectively via [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) or Amazon SageMaker AI.

With AWS, you can use DeepSeek-R1 models to build, experiment, and responsibly scale your generative AI ideas by using this powerful, cost-efficient model with minimal infrastructure investment. You can also confidently drive generative AI innovation by building on AWS services that are uniquely designed for security. We highly recommend integrating your deployments of the DeepSeek-R1 models with [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) to add a layer of protection for your generative AI applications, which can be used by both Amazon Bedrock and Amazon SageMaker AI customers.

You can choose how to deploy DeepSeek-R1 models on AWS today in a few ways: **1/ [Amazon Bedrock Marketplace](https://aws.amazon.com/bedrock/marketplace/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for the DeepSeek-R1 model**, **2/ [Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker/jumpstart/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for the DeepSeek-R1 model**, **3/ [Amazon Bedrock Custom Model Import](https://aws.amazon.com/bedrock/custom-model-import/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for the DeepSeek-R1-Distill models**, and **4/ [Amazon EC2 Trn1 instances](https://aws.amazon.com/ec2/instance-types/trn1/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for the DeepSeek-R1-Distill models**.

Let me walk you through the various paths for getting started with DeepSeek-R1 models on AWS. Whether you’re building your first AI application or scaling existing solutions, these methods provide flexible starting points based on your team’s expertise and requirements.

**1. The DeepSeek-R1 model in Amazon Bedrock Marketplace**

[Amazon Bedrock Marketplace](https://aws.amazon.com/bedrock/marketplace/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) offers over 100 popular, emerging, and specialized FMs alongside the current selection of industry-leading models in Amazon Bedrock. You can easily discover models in a single catalog, subscribe to the model, and then deploy the model on managed endpoints.

To access the DeepSeek-R1 model in Amazon Bedrock Marketplace, go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/model-catalog&trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and select **Model catalog** under the **Foundation models** section. You can quickly find DeepSeek by searching or filtering by model providers.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/01/30/2025-deepseek-r1-on-aws-3-bedrock-marketplace.png)

After checking out the model detail page including the model’s capabilities, and implementation guidelines, you can directly deploy the model by providing an endpoint name, choosing the number of instances, and selecting an instance type.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/01/30/2025-deepseek-r1-on-aws-3-bedrock-marketplace-deploy.png)

You can also configure advanced options that let you customize the security and infrastructure settings for the DeepSeek-R1 model including VPC networking, service role permissions, and encryption settings. For production deployments, you should review these settings to align with your organization’s security and compliance requirements.

With Amazon Bedrock Guardrails, you can independently evaluate user inputs and model outputs. You can control the interaction between users and DeepSeek-R1 with your defined set of policies by filtering undesirable and harmful content in generative AI applications. The DeepSeek-R1 model in Amazon Bedrock Marketplace can only be used with Bedrock’s [ApplyGuardrail API](https://aws.amazon.com/blogs/aws/guardrails-for-amazon-bedrock-can-now-detect-hallucinations-and-safeguard-apps-built-using-custom-or-third-party-fms/) to evaluate user inputs and model responses for custom and third-party FMs available outside of Amazon Bedrock. To learn more, read [Implement model-independent safety measures with Amazon Bedrock Guardrails](https://aws.amazon.com/blogs/machine-learning/implement-model-independent-safety-measures-with-amazon-bedrock-guardrails/).

Amazon Bedrock Guardrails can also be integrated with other Bedrock tools including [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) to build safer and more secure generative AI applications aligned with responsible AI policies. To learn more, visit the [AWS Responsible AI](https://aws.amazon.com/ai/responsible-ai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) page.

**Updated on 1st February** – You can use the Bedrock playground for understanding how the model responds to various inputs and letting you fine-tune your prompts for optimal results.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/02/02/bedrock-marketplace-playground-1.png)

When using DeepSeek-R1 model with the Bedrock’s playground or `InvokeModel` API, please use DeepSeek’s chat template for optimal results. For example, `<｜begin_of_sentence｜><｜User｜>content for inference<｜Assistant｜>`.

Refer to this [step-by-step guide](https://aws.amazon.com/blogs/machine-learning/deepseek-r1-model-now-available-in-amazon-bedrock-marketplace-and-amazon-sagemaker-jumpstart/) on how to deploy the DeepSeek-R1 model in Amazon Bedrock Marketplace. To learn more, visit [Deploy models in Amazon Bedrock Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

**2. The DeepSeek-R1 model in Amazon SageMaker JumpStart**

[Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker-ai/jumpstart/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) is a machine learning (ML) hub with FMs, built-in algorithms, and prebuilt ML solutions that you can deploy with just a few clicks. To deploy DeepSeek-R1 in SageMaker JumpStart, you can discover the DeepSeek-R1 model in [SageMaker Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [SageMaker Studio](https://aws.amazon.com/sagemaker-ai/studio/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [SageMaker AI console](https://us-east-1.console.aws.amazon.com/sagemaker/home#/foundation-models&trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), or programmatically through the [SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/overview.html).

In the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), open SageMaker Studio and choose **JumpStart** and search for “`DeepSeek-R1`” in the **All public models** page.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/01/30/2025-deepseek-r1-on-aws-5-sagemaker-jumpstart.png)

You can select the model and choose deploy to create an endpoint with default settings. When the endpoint comes **InService**, you can make inferences by sending requests to its endpoint.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/01/30/2025-deepseek-r1-on-aws-6-sagemaker-jumpstart-deploy.png)

You can derive model performance and ML operations controls with [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) features such as [Amazon SageMaker Pipelines](https://aws.amazon.com/sagemaker/pipelines/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [Amazon SageMaker Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), or container logs. The model is deployed in an AWS secure environment and under your virtual private cloud (VPC) controls, helping to support data security.

As like Bedrock Marketpalce, you can use the `ApplyGuardrail` API in the SageMaker JumpStart to decouple safeguards for your generative AI applications from the DeepSeek-R1 model. You can now use guardrails without invoking FMs, which opens the door to more integration of standardized and thoroughly tested enterprise safeguards to your application flow regardless of the models used.

Refer to this [step-by-step guide](https://aws.amazon.com/blogs/machine-learning/deepseek-r1-model-now-available-in-amazon-bedrock-marketplace-and-amazon-sagemaker-jumpstart/) on how to deploy the DeepSeek-R1 model in Amazon SageMaker JumpStart. To learn more, visit [Discover SageMaker JumpStart models in SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/sagemaker-discover-models.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) or [Deploy SageMaker JumpStart models in SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-studio-updated-deploy.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

**3. DeepSeek-R1-Distill models using Amazon Bedrock Custom Model Import**

[Amazon Bedrock Custom Model Import](https://aws.amazon.com/bedrock/custom-model-import/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) provides the ability to import and use your customized models alongside existing FMs through a single serverless, unified API without the need to manage underlying infrastructure. With Amazon Bedrock Custom Model Import, you can import [DeepSeek-R1-Distill models](https://huggingface.co/collections/deepseek-ai/deepseek-r1-678e1e131c0169c0bc89728d) ranging from 1.5–70 billion parameters. As I highlighted in [my blog post about Amazon Bedrock Model Distillation](https://aws.amazon.com/blogs/aws/build-faster-more-cost-efficient-highly-accurate-models-with-amazon-bedrock-model-distillation-preview/), the distillation process involves training smaller, more efficient models to mimic the behavior and reasoning patterns of the larger DeepSeek-R1 model with 671 billion parameters by using it as a teacher model.

After storing these publicly available models in an [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) bucket or an [Amazon SageMaker Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), go to **Imported models** under **Foundation models** in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/model-catalog&trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and import and deploy them in a fully managed and serverless environment through Amazon Bedrock. This serverless approach eliminates the need for infrastructure management while providing enterprise-grade security and scalability.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/01/30/2025-deepseek-r1-on-aws-4-bedrock-custom-model-import.png)

**Updated on 1st February** – After importing the distilled model, you can use the Bedrock playground for understanding distilled model responses for your inputs.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/02/02/bedrock-customer-model-import-playground-1.jpg)

Watch a [demo video](https://www.youtube.com/watch?v=1aq_ju70qHQ) made by my colleague [Du’An Lightfoot](https://www.linkedin.com/in/duanlightfoot/) for importing the model and inference in the Bedrock playground.

Refer to this [step-by-step guide](https://aws.amazon.com/blogs/machine-learning/deploy-deepseek-r1-distilled-llama-models-with-amazon-bedrock-custom-model-import/) on how to deploy DeepSeek-R1-Distill models using Amazon Bedrock Custom Model Import. To learn more, visit [Import a customized model into Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

**4. DeepSeek-R1-Distill models using AWS Trainium and AWS Inferentia**

[AWS Deep Learning AMIs (DLAMI)](https://docs.aws.amazon.com/dlami/latest/devguide/getting-started.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) provides customized machine images that you can use for deep learning in a variety of Amazon EC2 instances, from a small CPU-only instance to the latest high-powered multi-GPU instances. You can deploy the DeepSeek-R1-Distill models on AWS Trainuim1 or AWS Inferentia2 instances to get the best price-performance.

To get started, go to [Amazon EC2 console](https://console.aws.amazon.com/ec2?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and launch a `trn1.32xlarge` EC2 instance with the [Neuron Multi Framework DLAMI](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/dlami/index.html) called Deep Learning AMI Neuron (Ubuntu 22.04).

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/01/30/2025-deepseek-r1-on-aws-7-ec2-instance.png)

Once you have connected to your launched ec2 instance, install vLLM, an open-source tool to serve [Large Language Models (LLMs)](https://aws.amazon.com/what-is/large-language-model/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and download the DeepSeek-R1-Distill model from Hugging Face. You can deploy the model using vLLM and invoke the model server.

To learn more, refer to this [step-by-step guide](https://repost.aws/articles/ARDaRTyEVQR9iWfVdek2CQwg/get-started-with-deepseek-r1-on-aws-inferentia-and-trainium) on how to deploy DeepSeek-R1-Distill Llama models on AWS Inferentia and Trainium.

You can also visit [DeepSeek-R1-Distill models cards](https://huggingface.co/collections/deepseek-ai/deepseek-r1-678e1e131c0169c0bc89728d) on Hugging Face, such as [DeepSeek-R1-Distill-Llama-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B) or [deepseek-ai/DeepSeek-R1-Distill-Llama-70B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B). Choose **Deploy** and then **Amazon SageMaker**. From the **AWS Inferentia and Trainium** tab, copy the example code for deploy DeepSeek-R1-Distill models.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/01/30/2025-deepseek-r1-on-aws-8-hugging-face.png)

Since the release of DeepSeek-R1, various guides of its deployment for Amazon EC2 and [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) have been posted. Here is some additional material for you to check out:

* [Leveraging DeepSeek-R1 with CPU and GPU options on AWS](https://community.aws/content/2Z6DlAohx12yuNoEAs7qb5YTH0q/leveraging-deepseek-r1-on-aws?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) by [Daniel Wirjo](https://community.aws/%40wirjo)
* [Benefits of installing DeepSeek on an Amazon EC2 instance](https://community.aws/content/2sHGS4Eqeekz32OOzn7am5lnGEX/benefits-of-installing-deepseek-on-an-aws-ec2-instance?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) by [Enrique Aguilar Martinez](https://community.aws/%40kikitos)
* [Deploying DeepSeek Llama models on Amazon EC2 inferentia instance](https://community.aws/content/2sKnCT05v1WiD0Dw8QB5wfAf1Cm/deploying-deepseek-llama-model-on-amazon-ec2-inferentia-instance?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) by [Irshad Chohan](https://community.aws/%40irshadc)
* [How to deploy and fine-tune DeepSeek models on AWS](https://huggingface.co/blog/deepseek-r1-aws) by [Hugging Face](https://huggingface.co/)
* [Hosting DeepSeek-R1 on Amazon EKS Auto Mode](https://community.aws/content/2sJofoAecl6jVdDwVqglbZwKz2E/hosting-deepseek-r1-on-amazon-eks?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) by [Tiago Reichert](https://community.aws/%40tiagoreichert)

**Things to know**

Here are a few important things to know.

* **Pricing** – For publicly available models like DeepSeek-R1, you are charged only the infrastructure price based on inference instance hours you select for Amazon Bedrock Markeplace, Amazon SageMaker JumpStart, and Amazon EC2. For the Bedrock Custom Model Import, you are only charged for model inference, based on the number of copies of your custom model is active, billed in 5-minute windows. To learn more, check out the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [Amazon SageMaker AI Pricing](https://aws.amazon.com/sagemaker-ai/pricing/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) pages.
* **Data security**– You can use enterprise-grade security features in Amazon Bedrock and Amazon SageMaker to help you make your data and applications secure and private. This means your data is not shared with model providers, and is not used to improve the models. This applies to all models—proprietary and publicly available—like DeepSeek-R1 models on Amazon Bedrock and Amazon SageMaker. To learn more, visit [Amazon Bedrock Security and Privacy](https://aws.amazon.com/bedrock/security-compliance/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and [Security in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/security.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

**Now available**

DeepSeek-R1 is generally available today in Amazon Bedrock Marketplace and Amazon SageMaker JumpStart in US East (Ohio) and US West (Oregon) AWS Regions. You can also use DeepSeek-R1-Distill models using Amazon Bedrock Custom Model Import and Amazon EC2 instances with AWS Trainum and Inferentia chips.

Give DeepSeek-R1 models a try today in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and [Amazon EC2 console](https://console.aws.amazon.com/ec2/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and send feedback to [AWS re:Post for Amazon Bedrock](https://repost.aws/tags/TAQeKlaPaNRQ2tWB6P7KrMag/amazon-bedrock) and [AWS re:Post for SageMaker AI](https://repost.aws/tags/TAT80swPyVRPKPcA0rsJYPuA/amazon-sagemaker) or through your usual AWS Support contacts.

— [Channy](https://twitter.com/channyun)

***Updated on 1st February** — Added more screenshots and demo video of Amazon Bedrock Playground.*

***Updated on 3rd February** — Fixed unclear message for DeepSeek-R1 Distill model names and SageMaker Studio interface.*

![Channy Yun (윤석찬)](https://d2908q01vomqb2.cloudfront.net/7b52009b64fd0a2a49e6d8a939753077792b0554/2020/06/05/channyun_400x400.jpg)

### [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)")

Channy is a Lead Blogger of AWS News Blog and Principal Developer Advocate for AWS Cloud. As an open web enthusiast and blogger at heart, he loves community-driven learning and sharing of technology.

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