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

## [AWS Partner Network (APN) Blog](https://aws.amazon.com/blogs/apn/)

# Transforming the Software Development Lifecycle (SDLC) with Generative AI

by Diego Colombatto and Jose Manuel Pose Rivadulla on 16 JAN 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/apn/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Elastic Kubernetes Service](https://aws.amazon.com/blogs/apn/category/compute/amazon-kubernetes-service/ "View all posts in Amazon Elastic Kubernetes Service"), [Artificial Intelligence](https://aws.amazon.com/blogs/apn/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Featured](https://aws.amazon.com/blogs/apn/category/featured/ "View all posts in Featured"), [Partner solutions](https://aws.amazon.com/blogs/apn/category/post-types/partner-solutions/ "View all posts in Partner solutions"), [Thought Leadership](https://aws.amazon.com/blogs/apn/category/post-types/thought-leadership/ "View all posts in Thought Leadership") [Permalink](https://aws.amazon.com/blogs/apn/transforming-the-software-development-lifecycle-sdlc-with-generative-ai/)  [Comments](https://aws.amazon.com/blogs/apn/transforming-the-software-development-lifecycle-sdlc-with-generative-ai/#Comments)  Share

*By Diego Colombatto, Principal Partner Solutions Architect – AWS*

*By José Manuel Pose Rivadulla – CTO, IBM Consulting Spain, Portugal, Greece, and Israel – IBM*

|  |
| --- |
| [![IBM-AWS-Partners-5](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2022/05/09/IBM-AWS-Partners-5-300x150.png)](https://partners.amazonaws.com/partners/001E000001IlLnmIAF/IBM) |
| Partner Name |
| [![](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2024/10/14/IBM-APN-Blog-CTA-Button-2024-300x107.png)](https://partnercentral.awspartner.com/PartnerConnect?id=001E000001IlLnmIAF&source=Blog&campaign=) |

The potential of [Generative Artificial Intelligence (Generative AI)](https://aws.amazon.com/what-is/generative-ai/) continues to evaluated by organizations seeking to innovate. Some areas where Generative AI is creating significant impact include: enhancing customer experiences (chatbots, virtual assistants, and conversational analytics), improving employee productivity (content creation, summarization, and code generation), and business processes optimization (document processing, process optimization, and data augmentation).

Considering code generation, or application development more broadly, generative AI is not only changing the way applications are built, but the way they are envisioned, designed, tested, documented, and deployed.

This blog will explore how Generative AI is revolutionizing the Software Development Life-Cycle (SDLC) and how IBM and AWS infused [Amazon Bedrock](https://aws.amazon.com/bedrock/) generative AI capabilities into IBM’s SDLC solution to drive increased efficiency, speed, quality, and value in every application lifecycle consistently and at scale.

### The Evolution of the Software Development Lifecycle Landscape

The software development lifecycle has undergone several silent revolutions in recent decades. Back in the day, the dawn of software application delivery started with large back-end programs running on specialized servers. The advent of PCs introduced the desktop into application development lifecycle. Later, the rise of the web and social media paved the way for increased speed and scale in the number of applications and their interconnections. Then mobile apps and cloud enabled new levels of automation and agility into development lifecycle. More recently, generative AI is bringing another transformational change in how applications are designed and delivered.

[![](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2024/09/23/6235B80C-E7BB-4CF7-A801-2F1C7583DA7C.png)](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2024/09/23/6235B80C-E7BB-4CF7-A801-2F1C7583DA7C.png)

*Figure 1. Application development across decades*

### The Rise of Generative AI in the SDLC

Adoption of generative AI in the end-to-end SDLC brings numerous benefits, such as accelerating development time, improving code quality, and reducing costs. By leveraging generative AI, we can reduce the time-to-market for our clients. Moreover, it improves the effectiveness and consistency across tasks and participants by reducing the number of handovers, automating or removing low-value mundane tasks, and facilitating access to knowledge and on-boarding.

Generative AI drives these benefits across the entire end-to-end application lifecycle, from ideation to deployment. It provides different benefits at each stage of the SDLC and each stage has different participants, procedures and tasks.

[![https://aws.amazon.com/marketplace](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2024/09/23/Picture5-4.png)](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2024/09/23/Picture5-4.png)

*Figure 2. Typical participants through stages and phases of SDLC*

We list the key SDLC areas containing the tasks that generative AI can help with below:

* **Business and product owners** can use generative AI during ideation and concept generation, requirements identification, prioritization and planning, as well as other activities such as understanding feedback from end users or clients.
* **Analysts and designers** can use generative AI to accelerate the creation of prototypes along with detailed functional designs and solution blueprints.
* **Developers and testers** can use generative AI to define (and reuse) solution architectures, create and reuse technical designs, create code and logic, build (and run) highly automated tests, and perform quality and validation procedures.
* **Engineers** can use generative AI to activate the application underlying technical environment, on cloud or on premises, as well as perform the promotion and deployment of the application across the different environments and governance gates.
* **IT support, administrators and operators** can use generative AI across the multiple activities they perform regularly, including monitoring, operation and remediation, incident management including triage and resolution, and service request fulfillment.

When everything is put together, our approach not only accelerates individual tasks, but also enables us to perform activities earlier than is possible today, such as validation with business and users.

### The new Generative AI powered SDLC Solution

Together, IBM and AWS have launched the joint [Generative AI based SDLC solution](https://aws.amazon.com/marketplace/pp/prodview-dj4ewgartvgxo), which is now available on [AWS Marketplace](https://aws.amazon.com/marketplace). The solution automates the use of company architecture standards, assets, security, available APIs, quality standards, and documentation models ensuring that all artifacts comply with approved and defined policies within the organization’s SLDC.

To achieve the benefits mentioned above at scale in a sustainable manner, we apply a thoughtful and deliberate approach for integrating generative AI into every SDLC. Such an approach involves adapting our solution to the reality of each organization’s needs and SDLC, which is essential for achieving optimal results.

An interesting observation and challenge of the capabilities provided by generative AI is that it often produces different results when given the same input. Just like when two different developers are asked to solve the same problem, generative AI produces similar, but not identical, results. Hence, there’s a need for a new set of frictionless guidelines, guardrails, and controls to achieve quality and consistency with different generative AI results, at scale.

These redesigned standardized procedures are key to deliver high-quality standards throughout, whilst facilitating handovers between teams, as all team members can understand and work with the results generated by generative AI. Furthermore, the technology can drive increased visibility into which stage of the development process is at, improving project management and tracking.

### Solution Standardization and Consistency

It is important to note that standardization and consistency in the SDLC are not achieved solely through generative AI. Our achievement is due to the extensive work done at IBM Consulting, carefully designing generative AI-based procedures applied across the end-to-end SDLC, adapting, and refining our solution for each SDLC stage and task, which allows generative AI to produce consistent and high-quality results. This experience has enabled us to create guided, friction-less procedures adapted to the specific needs of each client, to properly address the reality of their SDLC and software landscape.

### Solution Benefits

Based on data collected from customers already using this solution, customers can expect to achieve significant benefits and outcomes, including the following:

* **Accelerated development time**: Up to 30% reduction in development time, enabling customers to bring their products and services to market faster.
* **Test generation time**: Up to 25% of time improvement in unit test generation and test plan scenarios.
* **Improved code quality**: Up to 25% improvement in code quality, resulting in fewer errors, reduced rework, and lower maintenance costs.
* **Reduction of analysis phase time**: Up to 60% reduction in analysis phase including functional and technical requirements, reverse engineering, and documentation enrichment.
* **Enhanced collaboration**: Improved collaboration and handovers between teams, enabling customers to work more efficiently and effectively.

[![Integration between IBM GenAI SDLC Solution and customer platforms](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2024/09/23/Picture6-2.png)](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2024/09/23/Picture6-2.png)

*Figure 3. Gen AI SDLC Solution and existing client’s platform*

IBM’s generative AI-powered solution offers several key advantages for developers and companies looking to improve their SDLC:

* First, the solution adapts to clients needs including, for example, using custom components or using their own reusable front-end components or back-end libraries.
* Second, it is compatible with existing DevOps solutions, like CI/CD tools to launch compilation after code generation or kanban boards for obtaining user stories to create a detailed design of the software to allow clients to quickly integrate it into their current processes.
* Third, the solution offers greater speed and efficiency in software development, which can reduce costs and improve the quality of the final product. By leveraging our solution, developers can improve the effectiveness of their SDLC, reducing the time and effort required to develop high-quality applications.

Additionally, users have the flexibility to accept solution suggestions as-is, ask for an automated suggestion rephrase, or make manual modifications to adapt suggestions to their specific needs. For example, during coding phase, we provide requirements, test cases for Test Driven Development (TDD) and other information to [Anthropic Claude](https://aws.amazon.com/bedrock/claude/) Sonnet, and the model will generate the needed code. At this point, the developer can modify the code, refactoring it to have the desired code structure. After all, users are experts in their domain, and the IBM solution provides them with the opportunity to refine and perfect the suggested results according to their specific needs.

### Technical Architecture

The generative AI powered SDLC solution uses Amazon Bedrock to consume large language models (LLMs), such as Anthropic’s Claude family of models, and [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) stores our refined and tailored procedures and prompt templates.

A complete user interface and integration layers are built as containers that run on [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS). We use AWS services to fulfill specific needs such as [AWS Web Application Firewall](https://aws.amazon.com/waf/) to secure application endpoints, [AWS Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/) to manage application traffic and [Amazon API Gateway](https://aws.amazon.com/api-gateway/) to enable connections with external services like CI/CD.

Security and compliance are key concerns for any business. [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) is used to manage keys and the encryption of customer data, enabling customers to adhere to their standards of privacy, security, and compliance. External keys can be used depending on where the customer prefers to keep cryptographic material. Integration with [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) or a third party HSM is also possible.

[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) is used to enable detailed audit trails of user and system actions, critical for supporting regulatory audits and helping to demonstrate compliance. [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) is used to implement granular control over access to data and resources with support for multi-factor authentication. [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) provides secure management of X.509 certificates for SSL/TLS connections, securing data in transit. [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) centralizes and secures secrets, such as API keys and data repository credentials.

[![IBM GenAI SDLC solution architecture](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2024/09/23/architecture-3.png)](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2024/09/23/architecture-3.png)

*Figure 4. IBM Generative AI SDLC solution architecture*

The architecture above offers a robust and secure solution intended to be deployed and integrated at scale by your organization’s unique landscape of technologies and vendors, including integration with existing DevOps solutions, allowing you to quickly integrate it into your own current processes.

### Conclusion

IBM generative AI-infused SDLC solution [is available on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-dj4ewgartvgxo) and in this blog we’ve seen how it’s revolutionizing the software development lifecycle by providing a faster, more efficient, consistent, and secure way to develop software. It combines the power of [AWS Generative AI](https://aws.amazon.com/ai/generative-ai/) technologies with the flexibility and scalability of the AWS Cloud, enabling developers and companies to create high-quality applications in a shorter time-frame and at a lower cost. Moreover, it offers greater freedom and flexibility to users, allowing them to work more efficiently and effectively.

IBM is an AWS Premier Tier Partner bringing specialized industry and domain expertise to help organizations move beyond pilots and achieve tangible business outcomes with generative AI. With the new AWS Generative AI Competency, IBM Consulting has now 20 AWS competencies and 17 service delivery designations (SDDs). This demonstrates IBM commitment to helping clients unlock the full potential of cloud-based generative AI solutions.

We are thrilled to see the impact IBM Generative AI SDLC solution can have in transforming the software development landscape, and we’re dedicated to ongoing innovation and improvement to make sure our technology meets the evolving needs of organizations.

[Read more about AWS Consulting Services offered by IBM](https://www.ibm.com/consulting/aws)

.

[![IBM-AWS-Partners-5](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2024/10/14/IBM-APN-Blog-Connect-2.png)](https://partnercentral.awspartner.com/PartnerConnect?id=001E000001IlLnmIAF&source=Blog&campaign=)

.

---

## IBM – AWS Partner Spotlight

**IBM** **is an AWS Premier Tier Services Partner and MSP** that offers comprehensive service capabilities addressing both business and technology challenges that clients face today.

[Contact IBM](https://partnercentral.awspartner.com/PartnerConnect?id=001E000001IlLnmIAF&source=Blog&campaign=) | [Partner Overview](https://partners.amazonaws.com/partners/001E000001IlLnmIAF/IBM) | [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=345ea612-6e57-4b07-b5a9-f5747652c4ee)

TAGS: [IBM](https://aws.amazon.com/blogs/apn/tag/ibm/)

Loading comments…

### Resources

* [AWS Partner and Customer Case Studies](https://aws.amazon.com/partners/success/)
* [AWS Partner Network Case Studies](https://aws.amazon.com/partners/partner-success/)
* [Why Work with AWS Partners](https://aws.amazon.com/partners/work-with-partners/)
* [Join the AWS Partner Network](https://aws.amazon.com/partners/)
* [Partner Central Login](https://aws.amazon.com/partners/apn-portal)
* [AWS Training for Partners](https://aws.amazon.com/partners/training)
* [AWS Sponsorship Opportunities](https://aws.amazon.com/partners/marketing/sponsorships)

---

### Follow

* [AWS Partners LinkedIn](https://www.linkedin.com/showcase/aws-partners/)
* [AWS Partners Twitter](https://twitter.com/aws_partners)
* [AWS Partners YouTube](https://www.youtube.com/c/AWSPartnerNetwork)
* [AWS Email Updates](https://partners.awscloud.com/communication-preferences.html)
* [APN Blog RSS Feed](https://aws.amazon.com/blogs/apn/feed)

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