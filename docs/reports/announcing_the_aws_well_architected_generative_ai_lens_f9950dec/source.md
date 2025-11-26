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

# Announcing the AWS Well-Architected Generative AI Lens

by Dan Ferguson, Steven DeVries, Haleh Najafzadeh, and Jeff Ruhnow on 17 APR 2025 in [Announcements](https://aws.amazon.com/blogs/architecture/category/post-types/announcements/ "View all posts in Announcements"), [AWS Well-Architected](https://aws.amazon.com/blogs/architecture/category/aws-well-architected/ "View all posts in AWS Well-Architected"), [Generative AI](https://aws.amazon.com/blogs/architecture/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI") [Permalink](https://aws.amazon.com/blogs/architecture/announcing-the-aws-well-architected-generative-ai-lens/) Share

We are delighted to introduce the new AWS Well-Architected Generative AI Lens. The AWS Well-Architected Framework provides architectural best practices for designing and operating [generative AI](https://aws.amazon.com/generative-ai/) workloads on AWS. The Generative AI Lens uses the Well-Architected Framework to outline the steps for performing a Well-Architected Framework Review for your generative AI workloads.

The Generative AI Lens provides a consistent approach for customers to evaluate architectures that use large language models (LLMs) to achieve their business goals. This lens addresses common considerations relevant to model selection, prompt engineering, model customization, workload integration, and continuous improvement. Specifically excluded from this lens are best practices associated with model training and advanced model customization techniques. We identify best practices that help you architect your cloud-based applications and workloads according to AWS Well-Architected design principles gathered from supporting thousands of customer implementations.

The Generative AI Lens joins a collection of Well-Architected lenses published under [AWS Well-Architected Lenses](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&awsm.page-wa-lens-whitepapers=1&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc).

## What is the Generative AI Lens?

The Well-Architected Generative AI Lens focuses on the six pillars of the Well-Architected Framework across six phases of the generative AI lifecycle, as illustrated in the following figure.

![](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2025/03/07/archblog-1154-Picture1.png)

The six phases are:

1. Scoping the impact of generative AI in solving your problem.
2. Selecting a model that sufficiently addresses the task.
3. Customizing the model with prompts, data sources, or updated weights to improve performance.
4. Integrating the model into your existing applications.
5. Deploying the new generative AI capability into your environment.
6. Iterating and improving on the generative AI capabilities you have released.

Unlike the traditional waterfall approach, an iterative approach is required to achieve a working prototype based on the six phases of the generative AI lifecycle. The lens provides you with a set of established cloud-agnostic best practices in the form of Well-Architected Framework pillars for each generative AI lifecycle phase.

You can also use the Well-Architected Generative AI Lens wherever you are on your cloud journey. You can choose to apply this guidance either during the design of your generative AI workloads or after your workloads have entered production as a part of the continuous improvement process.

## What’s else is discussed in the Generative AI Lens?

The Generative AI Lens also discusses the following key topics:

* **Responsible AI** – Responsible implementation of generative AI workloads is discussed in this paper. We describe some of the common considerations facing customers as they address the responsible implementation and deployment of generative AI.
* **Data architecture for generative AI** – At the core of any AI workload is data. We feature a brief survey on the nuances of data architectures with regards to generative AI workloads.

## Who should use the Generative AI Lens?

The Generative AI Lens is of use to many roles. Business leaders can use this lens to acquire a broader appreciation of the end-to-end implementation and benefits of generative AI. Data scientists and engineers can read this lens to understand how to use, secure, and gain insights from their data at scale. Risk and compliance leaders can understand how generative AI is implemented responsibly by providing compliance with regulatory and governance requirements.

## Generative AI Lens components

The lens includes four focus areas:

* **The Well-Architected Generative AI Lens design principles** – Design principles are the guidelines and value statements that frame the presented best practices.
* **The Generative AI lifecycle and the Well Architected Framework pillars** – This considers all aspects of the generative AI lifecycle and reviews design strategies to align to the pillars of the overall Well-Architected Framework:
  + **Operational excellence** – Ability to support ongoing development, run operational workloads effectively, gain insight into your operations, and continuously improve supporting processes and procedures to deliver business value.
  + **Security** – Ability to protect data, systems, and assets, and to take advantage of cloud technologies to improve your security.
  + **Reliability** – Ability of a workload to perform its intended function correctly and consistently, and to automatically recover from failure situations.
  + **Performance efficiency** – Ability to use computing resources efficiently to meet system requirements, and to maintain that efficiency as system demand changes and technologies evolve.
  + **Cost optimization** – Ability to run systems to deliver business value at the lowest price point.
  + **Sustainability** – Addresses the long-term environmental, economic, and societal impact of your business activities.
* **Cloud-agnostic best practices** – These are best practices for each generative AI lifecycle phase across the Well-Architected Framework pillars irrespective of your technology setting. The best practices are accompanied by:
  + **Implementation guidance** – The AWS implementation plans for each best practice with references to AWS technologies and resources.
  + **Resources** – A set of links to AWS documents, blogs, videos, and code examples as supporting resources to the best practices and their implementation plans.
* **Related generative AI architecture considerations** – This includes discussions on the generative AI application lifecycle, and where the listed best practices in this lens could fit into the lifecycle. Additionally, we discuss elements of data architecture for generative AI workloads, and Well-Architected considerations for responsible AI.

## What are the next steps?

The new [Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html) is available now. Use the lens to make sure that your generative AI workloads are architected with operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability in mind.

If you require support on the implementation or assessment of your generative AI workloads, please contact your AWS Solutions Architect or Account Representative.

Special thanks to everyone across the AWS Solution Architecture, AWS Professional Services, and Machine Learning communities who contributed to the Generative AI Lens. These contributions encompassed diverse perspectives, expertise, backgrounds, and experiences in developing the new AWS Well-Architected Generative AI Lens.

For additional reading, refer to the [AWS Well-Architected Framework and pillar whitepapers](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc), or use the [AWS Well-Architected Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html) and its custom lens accessible from the AWS Well-Architected Tool.

---

### About the authors

![Dan Ferguson](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2025/03/07/frgud.jpg)

### Dan Ferguson

Dan Ferguson is a Solutions Architect at AWS, based in New York, USA. As a machine learning services expert, Dan works to support customers on their journey to integrating ML workflows efficiently, effectively, and sustainably.

![Steven DeVries](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2025/03/07/devris.jpg)

### Steven DeVries

Steven is a Principal Solutions Architect at AWS leading Data and AI initiatives for Automotive and Manufacturing customers. He deploys agentic workflows, builds ML pipelines, and architects generative AI applications that turn emerging technologies into business value.

![Haleh Najafzadeh](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2021/09/23/Haleh-Najafzadeh.jpg)

### Haleh Najafzadeh

is a Principal Solutions Architect at AWS with over 25 years of experience in applying scientific techniques to challenging industrial problems while sharing technology best practices enabling customers with architecting and implementing solutions at scale.

![Jeff Ruhnow](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2025/03/07/ruhnow.jpg)

### Jeff Ruhnow

Jeff is a resident cat herder, and can be frequently found ranting about the irrationality of markets and humans. In his spare time he puts together pretty slides to help bring a little more excitement to the drably decorated business world. Sometimes, these even matter to customers, and help them move faster and more intelligently.

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