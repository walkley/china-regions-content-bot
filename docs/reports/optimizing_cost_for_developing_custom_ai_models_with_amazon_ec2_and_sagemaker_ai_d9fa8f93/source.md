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

# Optimizing cost for building AI models with Amazon EC2 and SageMaker AI

by Adam Richter and [Bowen Wang](https://aws.amazon.com/blogs/aws-cloud-financial-management/author/bowewang/ "Posts by Bowen Wang") on 28 MAR 2025 in [Amazon EC2](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/compute/amazon-ec2/ "View all posts in Amazon EC2"), [Amazon SageMaker](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/artificial-intelligence/sagemaker/ "View all posts in Amazon SageMaker"), [Amazon SageMaker AI](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/artificial-intelligence/sagemaker/amazon-sagemaker-ai/ "View all posts in Amazon SageMaker AI"), [Artificial Intelligence](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [AWS Cloud Financial Management](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/aws-cloud-financial-management/ "View all posts in AWS Cloud Financial Management"), [Best Practices](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/post-types/best-practices/ "View all posts in Best Practices"), [Compute](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/compute/ "View all posts in Compute"), [Generative AI](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI") [Permalink](https://aws.amazon.com/blogs/aws-cloud-financial-management/optimizing-cost-for-developing-custom-ai-models-with-amazon-ec2-and-sagemaker-ai/) Share

*This post was made better through reviews from Shane Robbins, Shruti Koparkar, and Natalia Cummings*

Welcome to the second blog of the series on optimizing costs for generative AI workloads on AWS. In our [first blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/optimizing-cost-for-generative-ai-with-aws/), we provided an overview of different implementation approaches and Cloud Financial Management principles for generative AI adoption. Today, we’ll dive deep into cost optimization strategies for building and deploying custom AI models using Amazon Elastic Compute Cloud ([Amazon EC2](https://aws.amazon.com/ec2/)) and [Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/). Whether you’re training large language models, fine-tuning existing models, or deploying inference endpoints, we’ll explore key cost levers such as instance type selection, capacity management, and commitment planning for Amazon EC2, as well as model optimization, training efficiency, and deployment strategies for Amazon SageMaker AI. These practices will help you balance performance requirements with cost efficiency while maintaining the flexibility and control that comes with managing your own AI infrastructure.

Amazon EC2 and SageMaker AI are two of the foundational AWS services for Generative AI. Amazon EC2 provides the scalable computing power needed for training and inference, while SageMaker AI offers built-in tools for model development, deployment, and optimization. Cost optimization is crucial since Generative AI workloads require high-performance accelerators (GPU, [Trainium](https://aws.amazon.com/ai/machine-learning/trainium/), or [Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/)) and extensive processing, which can become expensive without efficient resource management. By leveraging the below cost optimization strategies, you can reduce costs while maintaining performance and scalability.

![Cost optimization strategy graph for Amazon EC2 and SageMaker AI](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/03/27/GenAI-cost-optimization-series-EC2-and-SageMaker-AI-cost-optimization-tactics-graph.jpg)

Image 1 “Amazon EC2 and SageMaker AI cost optimization strategy: cost savings vs effort.” This graph is for illustrative purposes only. Actual effort required and cost savings achieved may vary based on implementation scale, infrastructure, and team expertise.

## Amazon EC2

### 1. Selecting the optimal instance type

Amazon EC2 instances are the primary component in a self-managed deployment and it is important to choose the right instance type. With CPU based instance types, like those powered by [AWS Graviton](https://aws.amazon.com/ec2/graviton/),  you can use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to easily analyze and rightsize your instances. Generative AI solutions typically need accelerated instances that are powered by NVIDIA GPUs or AWS AI chips like Tranium and Inferentia. AWS Trainium and Inferentia based instances offer up to 30-50% better price performance for training and inference and can be a cost-effective option for your workloads. To rightsize GPU based instances, you can [enable NVIDIA GPU utilization with the CloudWatch agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/ec2-metrics-analyzed.html#nvidia-cw-agent). This allows AWS Compute Optimizer to collect NVIDIA GPU utilization and provide rightsizing recommendations.

Contextual testing should be used for more comprehensive analysis of your instance performance against your data sets, workloads, and models. Tools like [FM Bench](https://aws-samples.github.io/foundation-model-benchmarking-tool/) can help streamline this testing by analyzing performance across different instance types and serving stacks. It will help you identify the most cost-effective configuration through markdown reports that show inference latency, transactions per-minute, error rates, and cost per transaction. The reports contain explanatory text, tables, and figures that give you the information you need to rightsize your instances and to ensure that you are only paying for what you need.

### 2. Smart capacity management

Once you understand the type of instance to use, the next step is to understand your capacity management strategy. Some common questions to think about are:

* How many instances are needed?
* How often do they need to run?
* How long will they be needed?

#### On-Demand Capacity Reservations (ODCRs)

[ODCRs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservation-overview.html) allow you to reserve compute capacity for Amazon EC2 instances in a specific Availability Zone (AZ). For machine learning (ML) model training and fine-tuning, ODCRs allow you to get uninterrupted access to the accelerated (GPU, Trainium, or Inferentia) instances that you reserve. You should consider using ODCRs if you have strict capacity requirements or your solution requires capacity assurance.

ODCRs require no long term commitment and you can modify or cancel them at any time. Capacity Reservations are charged at the equivalent On-Demand rate whether you run instances in reserved capacity or not. Billing starts as soon as the ODCR is provisioned in your account, and it continues while the Capacity Reservation remains provisioned in your account.

To ensure that you are using ODCRs efficiently, it is important to [monitor the utilization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservation-cw-metrics.html). The first way to accomplish this is to utilize Amazon CloudWatch. With CloudWatch you can setup alarms to monitor metrics like ‘AvailableInstanceCount’. This metric will help you determine how many instances in the ODCR are going unused. Another option to monitor ODCRs is to utilize [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer) or the [Cost and Usage Reports (CUR)](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/). Using these tools, you can filter for usage types containing ‘UnusedBox’ or ‘UnusedDed’. This will show you the amount of ODCRs that are not being used. Lastly, the [AWS Health Dashboard](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-eventbridge.html#monitor-cr-utilization) will send an email when capacity utilization for ODCRs in your account drops below 20 percent.

#### Instance scheduling

If the workloads in your environment do not need to run 24/7, you should consider using [AWS instance scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/). AWS Instance Scheduler is a solution designed to automate the starting and stopping of Amazon Elastic Compute Cloud (EC2) and [Amazon Relational Database Service (RDS)](https://aws.amazon.com/rds/) instances. This automation is beneficial to help reduce operational costs by ensuring that resources are only running when needed. Instance Scheduler can be configured to work across multiple AWS accounts, enhancing its utility for larger organizations. The scheduler is installed with [AWS CloudFormation](https://aws.amazon.com/cloudformation/) templates and can be customized with various parameters such as schedule, service (Amazon EC2 or Amazon RDS), and timezone settings. This flexibility allows you to tailor the scheduler to your specific needs, ensuring efficient resource management and cost optimization.

If you cannot shut down or release instances for capacity purposes, consider using instance scheduler with ODCRs so the spare capacity can be temporarily shifted to other accounts, teams, or workloads in your environment. While this method may not result in cost savings, it will allow you to get more value out of the instances you are utilizing.

### 3. Strategic commitment planning

When developing your AWS commitment strategy, the following factors will help maximize your savings: workload longevity (1 or 3 years), instance family requirements, and regional flexibility. The [Savings Plan Purchase Analyzer](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-analyzer.html) tool can help examine your historical usage patterns and recommend optimal commitment levels based on these factors. For those requiring specific instance families in particular regions, [Instance Savings Plans (ISPs)](https://aws.amazon.com/savingsplans/compute-pricing/) offer the deepest discounts. Alternatively, Compute Savings Plans (CSPs) provide greater flexibility across instance generations and regions at a lower discount rate. CSPs allow you to move workloads between regions or upgrade to newer instance families without losing your committed discount benefits. Depending on which you choose, you can save up to 72% vs. On-Demand pricing, which makes AWS Savings Plans an impactful cost optimization tool for your AWS infrastructure.

### 4. Maximizing resource efficiency

Tracking accelerator (GPU, Trainium, or Inferentia) utilization will give you a better understanding of how efficiently resources are being utilized. GPU utilization metrics help to validate instance requirements, maximize efficiency, and identify opportunities for resource sharing across teams and projects. While CPU utilization monitoring is relatively straightforward, GPU monitoring presents unique challenges. As mentioned above, when selecting the optimal instance type, GPU utilization requires more detailed metrics. Two metrics that can be used to estimate GPU utilization are temperature and power draw. These metrics are available from the [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-NVIDIA-GPU.html) and this approach allows GPU saturation levels to be estimated which provides valuable insights into resource utilization patterns. With this estimation, you can achieve greater utility from existing infrastructure which translates to a reduction in the Total Cost of Ownership.

![QuotebyBrentSegner](https://d2908q01vomqb2.cloudfront.net/2e01e17467891f7c933dbaa00e1459d23db3fe4f/2025/03/27/QuotebyBrentSegner.jpg)

## Amazon SageMaker AI

As you accelerate AI/ML initiatives, you’re confronted with a strategic decision: should you invest resources in building and maintaining ML infrastructure, or channel you effort toward driving business outcomes? [Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/) is the ideal solution to this dilemma, offering a fully managed service that removes undifferentiated heavy lifting while maintaining the flexibility you need. [SageMaker JumpStart](https://aws.amazon.com/sagemaker-ai/jumpstart/) helps you get started quickly by providing pre-built solutions, ready-to-deploy models, and example notebooks. Whether you’re just starting your SageMaker AI journey, or looking to optimize your existing implementation, these strategies will help you build a more efficient and cost-effective AI and ML solution.

### 1. Rightsizing for success

Optimizing your SageMaker AI instance type and size can impact both performance and cost-efficiency in your solutions. Through careful analysis of our your usage patterns, you can reduce your ML infrastructure costs through strategic rightsizing of your SageMaker AI instances. To select the right instance type and size for your workload, it is critical to test. FM Bench, mentioned above, is a valuable tool in making this process easier.

### 2. Balancing model capability and cost

Selecting the right model for your machine learning workloads is one of the most critical decisions in building effective SageMaker AI projects. Thoughtful model selection can improve both performance and cost-efficiency by up to 45%. We recommend a systematic approach that evaluates three key dimensions: 1)  your specific use case requirements, 2) available computational resources, and 3) your budget. For example, while large language models (LLMs) offer impressive capabilities, they may not always be the most cost-effective solution for straightforward tasks where simpler models could suffice. You can achieve optimal results by starting with models from SageMaker Jumpstart which is a hub with foundation models, built-in algorithms, and prebuilt ML solutions. You can then evaluate whether the incremental benefits of more sophisticated (and often more expensive) models justify the additional computational and financial costs. This iterative approach to model selection often leads to solutions that are both technically superior and more sustainable.

### 3. Leverage SageMaker AI Savings Plans

Optimizing costs while maintaining operational flexibility is crucial for running machine learning solutions at scale. [Machine Learning Savings Plans](https://aws.amazon.com/savingsplans/ml-pricing/) (MLSPs) are a commitment available to you that can save up to 64% on SageMaker AI through a usage-based pricing model. These plans require a commitment to a consistent amount of usage (measured in dollars per hour) over either a one or three-year term. What makes MLSPs particularly powerful is their flexibility – the savings automatically apply to the usage of eligible SageMaker ML instances in SageMaker Studio Notebooks, SageMaker On-Demand Notebooks, SageMaker Processing, SageMaker Data Wrangler, SageMaker Training, SageMaker Real-Time Inference, and SageMaker Batch Transform. This means you can freely innovate and adjust your machine learning infrastructure without worrying about losing your committed savings. MLSPs provide a low effort path to significant cost optimization, especially for sustained machine learning operations. The simplicity and effectiveness of MLSPs make them an essential consideration when you are looking to scale your machine learning initiatives while maintaining cost efficiency.

### 4. Optimize training costs with Spot Instances

[Managed Spot Training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html) offers a cost optimization strategy for machine learning workloads. By leveraging Spot Instance pricing, you can reduce training costs by up to 90% compared to On-Demand instances, making it a valuable option for projects with restricted budgets. This cost-effective approach is particularly well-suited for non-time-sensitive training jobs that can tolerate occasional interruptions. When combined with AWS Graviton processors, you can achieve even greater price-performance benefits. To make the process easy to use, SageMaker AI can automatically manage the Spot Instance lifecycle. This is accomplished through [checkpointing model artifacts](https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints.html) to ensuring training progress is preserved even if instances are reclaimed. This makes it an ideal solution for development, testing, and other environments where training time flexibility exists.

### 5. Choose the right inference strategy

Amazon SageMaker AI provides several options for inference deployment, which are designed for various use cases and cost structures, see [Inference cost optimization best practices](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-cost-optimization.html) for more information. Real-time inference provides low-latency but incurs continuous costs as the instance run constantly. Real-time is ideal for applications requiring immediate responses. [Serverless Inference,](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) introduced to reduce costs for intermittent workloads, automatically scales to zero when not in use and charges only for the compute time used during invocations. For batch processing, SageMaker AI [Batch transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html) offers the most cost-effective solution by processing large datasets in bulk without maintaining persistent endpoints. Lastly, [Asynchronous inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) processes requests asynchronously, making it ideal for large payloads, long processing times, and near real-time latency needs. It reduces costs by automatically scaling instances to zero when idle, so you only pay when requests are being processed.

By implementing these optimization strategies, you can significantly reduce your infrastructure costs while maintaining high performance and scalability. The key to success is aligning these choices with your specific use case and business requirements, ensuring that you’re not just cutting costs, but optimizing for long-term success in your machine learning operations.

## Conclusion:

In this post, we’ve explored cost optimization strategies for custom AI model development using Amazon EC2 and SageMaker AI. In our next blog, we’ll dive into cost optimization techniques for Amazon Bedrock, including smart model selection, knowledge base optimization, and caching strategies. Stay tuned to learn how to maximize the value of foundation models while keeping costs under control.

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