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

## [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)

# Use generative AI on AWS for efficient clinical document analysis

by Alex Boudreau and John O'Donnell on 05 FEB 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/architecture/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Comprehend Medical](https://aws.amazon.com/blogs/architecture/category/artificial-intelligence/amazon-comprehend-medical/ "View all posts in Amazon Comprehend Medical"), [Amazon Machine Learning](https://aws.amazon.com/blogs/architecture/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Amazon SageMaker](https://aws.amazon.com/blogs/architecture/category/artificial-intelligence/sagemaker/ "View all posts in Amazon SageMaker"), [Best Practices](https://aws.amazon.com/blogs/architecture/category/post-types/best-practices/ "View all posts in Best Practices"), [Customer Solutions](https://aws.amazon.com/blogs/architecture/category/post-types/customer-solutions/ "View all posts in Customer Solutions"), [Generative AI](https://aws.amazon.com/blogs/architecture/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI") [Permalink](https://aws.amazon.com/blogs/architecture/use-generative-ai-on-aws-for-efficient-clinical-document-analysis/) Share

Clinical trials involve the ingestion and processing of vast amounts of highly regulated data, including complex protocol documents that describe how the trial will be conducted. Managing this volume of information can be overwhelming, but generative AI offers a solution by helping automate the process and enabling clinical researchers to quickly focus on the most relevant information. Currently, the drug approval process takes on average 10–12 years, with clinical trial study startup time accounting for 1 year of that timeframe. Much of the challenge with study startup lies in the complex and non-standard nature of protocol documents. These often require weeks or months of effort to review and assess. This review time adds to the already long cycle time to bring a new drug to market.

In this post, we show how Clario uses the AWS platform to accelerate clinical document analysis.

## About Clario

[Clario](https://www.clario.com) is a leading provider of endpoint data solutions to the clinical trials industry providing regulatory-grade clinical evidence for pharmaceutical, biotech, and medical device partners. Since Clario’s founding more than 50 years ago, their endpoint data solutions have supported clinical trials more than 26,000 times with over 700 regulatory approvals across more than 100 countries. One of the critical challenges Clario faces is the time-consuming process of generating documentation for clinical trials, which can take weeks or months.

## The business challenge

Clinical trials are essential for the approval of new health innovations, including treatments, procedures, and medical devices. They require the collection of vast quantities of complex data from dispersed clinical trial sites to support assessments of medical benefits and risks, all while maintaining privacy and regulatory compliance. To make matters even more challenging, capturing data in clinical trial occurs not only in healthcare centers but also through remote capture through various aspects of trial participants’ daily activities.

Partners like Clario understand the challenges faced by life sciences companies when it comes to analyzing large volumes of complex clinical documents, such as study protocols. These documents often contain a mix of structured and unstructured data, including tables, images, and diagrams, making it difficult to accurately interpret and extract key information at scale. In this post, we explore how Clario has used the power of [generative AI](https://aws.amazon.com/generative-ai/) on AWS to efficiently analyze clinical documents and drive better outcomes for its clients.

## Harnessing the power of large language models

The rapid progress in large language models (LLMs) has expanded the potential applications of natural language processing beyond simple conversational AI assistants. Clario has experimented with various techniques, such as zero-shot learning, few-shot learning, classification, entity extraction, and summarization, for the effective use of LLMs in specialized use cases. By employing prompt engineering, AI orchestration, and content retrieval, Clario can guide the models to accurately generate insights and extract relevant information from key clinical research documents, including complex clinical trial protocols.

## Four pillars of effective document analysis on AWS

Through its research and development efforts, Clario has identified four core pillars that enable effective document analysis using generative AI on AWS:

* **Parsing** – Clario uses AWS services such as [Amazon Textract](https://aws.amazon.com/textract/) and [Amazon Comprehend](https://aws.amazon.com/comprehend/) to extract text, images, and tables from clinical documents, maintaining both data privacy and security.
* **Retrieval** – By using embedding models and vector databases like [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/), Clario efficiently stores and retrieves relevant information from large document collections based on similarity search. The team has experimented with various chunking and retrieval strategies to optimize accuracy and performance.
* **Prompting** – Using techniques like zero-shot and few-shot learning, Clario has enhanced the accuracy of LLMs for classifying and extracting information . AWS services such as and [Amazon Bedrock](https://aws.amazon.com/bedrock/) simplify experimentation with different prompting strategies and the evaluation of model performance.
* **Generation** – Clario carefully considers factors such as context size, reasoning capabilities, and latency when selecting the appropriate LLMs for generating structured outputs. AWS offers a range of pre-trained models and frameworks that seamlessly integrate into Clario’s pipeline.

## Solution overview

To tackle the unique challenges associated with analyzing clinical documents, Clario has built a custom generative AI platform on AWS. This platform incorporates an orchestration engine that combines multiple LLMs and deep learning models, enabling it to extract key information accurately and at scale. By using AWS services such as [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2), [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS), [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3), SageMaker, and [AWS Lambda](https://aws.amazon.com/lambda/), Clario can efficiently process thousands of documents in a matter of seconds.

The following diagram illustrates the solution architecture.

[![Solution Overview](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2025/01/23/ARCHBLOG-1078-clario3-imaging-and-alexb-alex-edit-v3-Page-3.drawio-Copy.png)](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2025/01/23/ARCHBLOG-1078-clario3-imaging-and-alexb-alex-edit-v3-Page-3.drawio-Copy.png)

The workflow consists of the following steps:

* Documents are collected on premises (1) and uploaded using [AWS Direct Connect](https://aws.amazon.com/directconnect/) (2) with encryption in transit to Amazon S3 (3). All uploaded documents are then automatically and securely stored with server-side object-level encryption.
* After the documents are uploaded and the user has reviewed them, the Clario AI Orchestration Engine (4) determines the best document parsing strategy based on file type, and extracts text using Amazon Textract (5). Once extracted, the text is vectorized and stored in the Amazon OpenSearch Service vector engine (6) for later semantic retrieval.
* After vectorization, the Clario AI Orchestration Engine (4), which runs as a distributed service in Amazon EKS, launches a document classification async task using [Amazon MQ](https://aws.amazon.com/amazon-mq/). Amazon EC2 and Lambda are used for additional processing if needed. This triggers the Document Classification Agent, which uses [Amazon Bedrock](https://aws.amazon.com/bedrock/) LLMs (8), for automatically determining the document type.
* After the documents are classified, the Clario AI Orchestration Engine (4) launches the appropriate document analysis agent for further background processing. In the case of study protocols, the engine launches the Protocol Analysis agent, which uses a predefined analysis graph configuration stored in [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) (7), as well as a combination of retrieval strategies and AI models, including custom deep learning models on SageMaker (9), and pre-trained LLMs on Amazon Bedrock (8). This orchestration powers advanced document analysis, transforming massive amounts of unstructured multi-modal data into structured data and insights.
* Following the analysis, all structured data is then persisted to Amazon RDS (7) for later visualization, review, and querying.

## Recommendations and best practices

Based on their experience developing and deploying generative AI solutions on AWS, Clario learned the following best practices:

* Adopt an incremental and iterative development approach to gradually build and refine your models
* Follow a standard machine learning approach for evaluating and validating model performance using representative test sets
* Optimize the four pillars of document analysis before investing in fine-tuning and continuous pre-training of LLMs
* Tailor your approaches to specific use cases, because not all problems require the same models or techniques

## Conclusion

By using the power of generative AI on AWS, Clario has been able to efficiently analyze complex clinical trial documents and extract valuable insights for its clients in the life sciences industry. Through a combination of careful model selection, iterative development, and adherence to best practices, Clario has built a scalable and accurate document analysis pipeline using AWS. Unlock the full potential of your clinical trial data by applying these best practices with an AWS generative AI solution today.

---

### About the Authors

![Alex Boudreau](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2025/01/23/1624904528953.jpg)

### Alex Boudreau

Alex Boudreau is the Director of AI at Clario. He leads the company's innovative Generative AI department and oversees the development of the company’s advanced multi-modal GenAI Platform, which encompasses cutting-edge cloud engineering, AI engineering, and foundational AI research. With a distinguished career in AI and machine learning, Alex previously pioneered Deep Learning speech analysis systems for automotive applications, led cloud-based enterprise fraud detection solutions, advanced conversational AI technologies, and groundbreaking projects in medical image analysis. His expertise in leading high-impact initiatives positions him uniquely to drive forward the boundaries of AI technology in the business world.

![John O'Donnell](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2025/01/23/1675893031202-1-1.jpg)

### John O'Donnell

John O'Donnell is a Principal Solutions Architect at Amazon Web Services (AWS) where he provides CIO-level engagement and design for complex cloud-based solutions in the healthcare and life sciences (HCLS) industry. With over 20 years of hands-on experience, he has a proven track record of delivering value and innovation to HCLS customers across the globe. As a trusted technical leader, he has partnered with AWS teams to dive deep into customer challenges, propose outcomes, and ensure high-value, predictable, and successful cloud transformations. John is passionate about helping HCLS customers achieve their goals and accelerate their cloud native modernization efforts.

### Resources

* [AWS Architecture Center](https://aws.amazon.com/architecture/)
* [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=architecture-resources)
* [AWS Architecture Monthly](https://aws.amazon.com/architecture/architecture-monthly/)
* [AWS Whitepapers](https://aws.amazon.com/whitepapers?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=architecture-resources)
* [AWS Training and Certification](https://aws.amazon.com/training?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=architecture-resources)
* [This Is My Architecture](https://aws.amazon.com/this-is-my-architecture?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=architecture-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=architecture-social)

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