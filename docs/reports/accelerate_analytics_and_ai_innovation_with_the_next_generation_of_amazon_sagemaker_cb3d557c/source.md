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

## [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/)

# Accelerate analytics and AI innovation with the next generation of Amazon SageMaker

by G2 Krishnamoorthy and Rahul Pathak on 13 MAR 2025 in [Amazon SageMaker](https://aws.amazon.com/blogs/big-data/category/artificial-intelligence/sagemaker/ "View all posts in Amazon SageMaker"), [Amazon SageMaker Unified Studio](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-sagemaker-unified-studio/ "View all posts in Amazon SageMaker Unified Studio"), [Analytics](https://aws.amazon.com/blogs/big-data/category/analytics/ "View all posts in Analytics"), [Artificial Intelligence](https://aws.amazon.com/blogs/big-data/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Thought Leadership](https://aws.amazon.com/blogs/big-data/category/post-types/thought-leadership/ "View all posts in Thought Leadership") [Permalink](https://aws.amazon.com/blogs/big-data/accelerate-analytics-and-ai-innovation-with-the-next-generation-of-amazon-sagemaker/)  [Comments](https://aws.amazon.com/blogs/big-data/accelerate-analytics-and-ai-innovation-with-the-next-generation-of-amazon-sagemaker/#Comments)  Share

At AWS re:Invent 2024, we [announced](https://aws.amazon.com/blogs/big-data/the-next-generation-of-amazon-sagemaker-the-center-for-all-your-data-analytics-and-ai/) the next generation of [Amazon SageMaker](https://aws.amazon.com/sagemaker), the center for all your data, analytics, and AI. Amazon SageMaker brings together widely adopted AWS machine learning (ML) and analytics capabilities and addresses the challenges of harnessing organizational data for analytics and AI through unified access to tools and data with governance built in. It enables teams to securely find, prepare, and collaborate on data assets and build analytics and AI applications through a single experience, accelerating the path from data to value.

At the core of the next generation of Amazon SageMaker is [Amazon SageMaker Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/), a single data and AI development environment where you can find and access your organization’s data and act on it using the best tool for the job across virtually any use case. **We are excited to announce the general availability of SageMaker Unified Studio.**

In this post, we explore the benefits of SageMaker Unified Studio and how to get started.

## Amazon SageMaker Unified Studio

SageMaker Unified Studio brings together the functionality and tools from existing AWS Analytics and AI/ML services, including [Amazon EMR](https://aws.amazon.com/emr/), [AWS Glue](https://aws.amazon.com/glue/), [Amazon Athena](https://aws.amazon.com/athena/), [Amazon Redshift](https://aws.amazon.com/redshift/), [Amazon Bedrock](https://aws.amazon.com/bedrock/ide/), and [Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/). From within the unified studio, you can discover data and AI assets from across your organization, then work together in projects to securely build and share analytics and AI artifacts, including data, models, and generative AI applications. Governance features including fine-grained access control are built into SageMaker Unified Studio using [Amazon SageMaker Catalog](https://aws.amazon.com/sagemaker/data-ai-governance/) to help you meet enterprise security requirements across your entire data estate.

Unified access to your data is provided by [Amazon SageMaker Lakehouse](https://aws.amazon.com/sagemaker/lakehouse/), a unified, open, and secure data lakehouse built on Apache Iceberg open standards. Whether your data is stored in [Amazon Simple Storage Service](http://aws.amazon.com/s3) (Amazon S3) data lakes, Redshift data warehouses, or third-party and federated data sources, you can access it from one place and use it with Iceberg-compatible engines and tools. In addition, SageMaker Lakehouse now integrates with [Amazon S3 Tables](https://aws.amazon.com/s3/features/tables/), the first cloud object store with native Apache Iceberg support, so you can use SageMaker Lakehouse to create, query, and process S3 Tables efficiently using various analytics engines in SageMaker Unified Studio as well as Iceberg-compatible engines like Apache Spark and PyIceberg.

Capabilities from Amazon Bedrock are now generally available in SageMaker Unified Studio, allowing you to rapidly prototype, customize, and share generative AI applications in a governed environment. Users have an intuitive interface to access high-performing foundation models (FMs) in Amazon Bedrock, including the [Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/?gclid=Cj0KCQjwhMq-BhCFARIsAGvo0KdoufWbhEF8G_zG3baFV_q-JC_8NCoMo6lZeYPiPKo_H5JSQPiMBW0aAtFXEALw_wcB&trk=36201f68-a9b0-45cc-849b-8ab260660e1c&sc_channel=ps&ef_id=Cj0KCQjwhMq-BhCFARIsAGvo0KdoufWbhEF8G_zG3baFV_q-JC_8NCoMo6lZeYPiPKo_H5JSQPiMBW0aAtFXEALw_wcB:G:s&s_kwcid=AL!4422!3!692006004844!e!!g!!amazon%20nova!21048268689!159639953895) model series, and the ability to create Agents, Flows, Knowledge Bases, and Guardrails with a few clicks.

[Amazon Q Developer](https://aws.amazon.com/q/developer/), the most capable generative AI assistant for software development, can be used within SageMaker Unified Studio to streamline tasks across the data and AI development lifecycle, including code authoring, SQL generation, data discovery, and troubleshooting.

## A new integrated way of working

The general availability of SageMaker Unified Studio represents another meaningful step in our journey to offer our customers a streamlined way to work with their data, whether for analytics or AI. Many of our customers have told us that you are building data-driven applications to guide business decisions, improve agility, and drive innovation, but that these applications are complex to build because they require collaboration across teams and the integration of data and tools. Not only is it time consuming for users to learn multiple development experiences, but because data, code, and other development artifacts are stored separately, it is challenging for users to understand how they interact with each other and to use them cohesively. Configuring and governing access is also a cumbersome manual process. To overcome these hurdles, many organizations are building bespoke integrations between services, tools, and homegrown access management systems. However, what you need is the flexibility to adopt the best services for your use case while empowering your data teams with a unified development experience.

> *“At Carrier, the next generation of Amazon SageMaker is transforming our enterprise data strategy by streamlining how we build and scale data products. SageMaker Unified Studio’s approach to data discovery, processing, and model development has significantly accelerated our lakehouse implementation. Most impressively, its seamless integration with our existing data catalog and built-in governance controls enables us to democratize data access while maintaining security standards, helping our teams rapidly deliver advanced analytics and AI solutions across the enterprise.”*
>
> – Justin McDowell, Director Data Platform & Data Engineering, Carrier

Millions of organizations trust AWS and utilize our comprehensive set of purpose-built analytics, AI/ML, and generative AI capabilities to power data-driven applications without compromising on performance, scale, or cost. Our goal for the next generation of Amazon SageMaker, including SageMaker Unified Studio, is to make data and AI workers more productive by providing access to all your data and tools in a single development environment.

## Building from a single data and AI development environment

Let’s explore a common business challenge: increasing revenue through better lead generation. Consider an organization implementing an intelligent digital assistant on their website to engage with customers—a process that traditionally requires multiple tools and data sources. With SageMaker Unified Studio, this entire process can now be carried out within a single data and AI development environment.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/03/13/bdb-4933-img2.png)

First, the data team uses the generative AI playground within SageMaker Unified Studio to quickly evaluate and select the best model for their customer interactions. They then create a project to house the tools and resources necessary for their use case and use Amazon Bedrock within the project to build and deploy a sophisticated virtual assistant that quickly begins qualifying leads through their website.

To identify the most promising opportunities, the team develops a segmentation strategy. The data engineer asks Amazon Q Developer to identify datasets that contain lead data and uses zero-ETL integrations to bring the data into SageMaker Lakehouse. The data analyst then discovers it and creates a comprehensive view of their market. They use the SQL query editor to build out marketing segments, which they then write back to SageMaker Lakehouse, where they are available to other team members.

Finally, the data scientist accesses the same dataset, which they use to train and deploy an automated lead scoring model using tools available from SageMaker AI. During the model development phase, they use Amazon Q Developer’s inline code authoring and troubleshooting capabilities to efficiently write error free-code in their JupyterLab notebook. The final model provides sales teams with the highest-value opportunities, which they can visualize in a business intelligence dashboard and take action on immediately.

## Reducing time-to-value in a unified environment

What is remarkable about this example is that entire process happens in one integrated environment. Without SageMaker Unified Studio, the team would have had to work with multiple data sources, tools, and services, spending time learning multiple development environments, creating resources shares, and manually configuring access controls. The data engineer and data analyst would have worked in various data warehouses, data lakes, and analytics tools, the data scientist would have worked in an ML studio and notebook environment, and the application builder in a generative AI tool. Now, they’re able to build and collaborate with their data and tools available in one experience, dramatically reducing time-to-value.

That’s why we’re so excited about the next generation of Amazon SageMaker and the general availability of SageMaker Unified Studio. We believe that by putting everything you need for analytics and AI in one place, you can solve complex end-to-end problems more efficiently and get to innovative outcomes faster than ever before.

## Getting started with SageMaker Unified Studio

To learn more, check out the following resources:

* [Amazon SageMaker](https://aws.amazon.com/sagemaker/)
* [Amazon SageMaker Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/)
* [Amazon SageMaker Lakehouse](https://aws.amazon.com/sagemaker/lakehouse/)

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2023/07/25/g2.jpg)G2 Krishnamoorthy** is VP of Analytics, leading AWS data lake services, data integration, Amazon OpenSearch Service, and Amazon QuickSight. Prior to his current role, G2 built and ran the Analytics and ML Platform at Facebook/Meta, and built various parts of the SQL Server database, Azure Analytics, and Azure ML at Microsoft.

**![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2023/07/25/rahul-pathak.jpg) Rahul Pathak** is VP of Relational Database Engines, leading Amazon Aurora, Amazon Redshift, and Amazon QLDB. Prior to his current role, he was VP of Analytics at AWS, where he worked across the entire AWS database portfolio. He has co-founded two companies, one focused on digital media analytics and the other on IP-geolocation.

Loading comments…

### Resources

* [Amazon Athena](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-athena?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon EMR](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-emr?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon Kinesis](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-kinesis?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon MSK](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-managed-streaming-for-apache-kafka/)
* [Amazon QuickSight](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-quicksight?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon Redshift](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-redshift-analytics?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [AWS Glue](https://aws.amazon.com/blogs/big-data/category/analytics/aws-glue?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-social)

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