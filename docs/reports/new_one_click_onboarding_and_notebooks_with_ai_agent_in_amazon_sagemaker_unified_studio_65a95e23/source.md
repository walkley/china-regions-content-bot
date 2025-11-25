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

# New one-click onboarding and notebooks with a built-in AI agent in Amazon SageMaker Unified Studio

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 21 NOV 2025 in [Amazon SageMaker Unified Studio](https://aws.amazon.com/blogs/aws/category/analytics/amazon-sagemaker-unified-studio/ "View all posts in Amazon SageMaker Unified Studio"), [Analytics](https://aws.amazon.com/blogs/aws/category/analytics/ "View all posts in Analytics"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/new-one-click-onboarding-and-notebooks-with-ai-agent-in-amazon-sagemaker-unified-studio/)  [Comments](https://aws.amazon.com/blogs/aws/new-one-click-onboarding-and-notebooks-with-ai-agent-in-amazon-sagemaker-unified-studio/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today we’re announcing a faster way to get started with your existing AWS datasets in [Amazon SageMaker Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). You can now start working with any data you have access to in a new serverless notebook with a built-in AI agent, using your existing [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) roles and permissions.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/19/2025-sagemaker-unified-studio-3-new-IDE-1.jpg)

New updates include:

* **One-click onboarding** – Amazon SageMaker can now automatically create a project in Unified Studio with all your existing data permissions from [AWS Glue Data Catalog](https://aws.amazon.com/glue/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [AWS Lake Formation](https://aws.amazon.com/lake-formation/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and [Amazon Simple Storage Services (Amazon S3)](https://aws.amazon.com/s3/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).
* **Direct integration** – You can launch SageMaker Unified Studio directly from [Amazon SageMaker](https://aws.amazon.com/sagemaker/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [Amazon Athena](https://aws.amazon.com/athena/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [Amazon Redshift](https://aws.amazon.com/redshift/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and [Amazon S3 Tables](https://aws.amazon.com/s3/features/tables/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) console pages, giving a fast path to analytics and AI workloads.
* **Notebooks with a built-in AI agent** – You can use a new serverless notebook with a built-in AI agent, which supports SQL, Python, Spark, or natural language and gives data engineers, analysts, and data scientists one place to develop and run both SQL queries and code.

You also have access to other tools such as a [Query Editor](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/getting-started-querying.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for SQL analysis, [JupyterLab](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/jupyterlab.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) integrated developer environment (IDE), [Visual ETL and workflows](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/visual-etl.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and [machine learning (ML) capabilities](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/sagemaker.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

**Try one-click onboarding and connect to Amazon SageMaker Unified Studio**

To get started, go to the [SageMaker console](https://console.aws.amazon.com/datazone/home?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and choose the **Get started** button.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/11/2025-sagemaker-unified-studio-1-get-started.jpg)

You will be prompted either to select an existing [AWS Identity and Access Management (AWS IAM)](https://aws.amazon.com/iam/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) role that has access to your data and compute, or to create a new role.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/21/2025-sagemaker-unified-studio-2-quick-setup.png)

Choose **Set up**. It takes a few minutes to complete your environment. After this role is granted access, you’ll be taken to the SageMaker Unified Studio landing page where you will see the datasets that you have access to in AWS Glue Data Catalog as well as a variety of analytics and AI tools to work with.

This environment automatically creates the following serverless compute: Amazon Athena Spark, Amazon Athena SQL, AWS Glue Spark, and [Amazon Managed Workflows for Apache Airflow (MWAA)](https://aws.amazon.com/managed-workflows-for-apache-airflow/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) serverless. This means you completely skip provisioning and can start working immediately with just-in-time compute resources, and it automatically scales back down when you finish, helping to save on costs.

You can also get started working on specific tables in Amazon Athena, Amazon Redshift, and Amazon S3 Tables. For example, you can select **Query your data in Amazon SageMaker Unified Studio** and then choose **Get started** in Amazon Athena console.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/11/2025-sagemaker-unified-studio-integration-athena.png)

If you start from these consoles, you’ll connect directly to the Query Editor with the data that you were looking at already accessible, and your previous query context preserved. By using this context-aware routing, you can run queries immediately once inside the SageMaker Unified Studio without unnecessary navigation.

**Getting started with notebooks with a built-in AI agent**

Amazon SageMaker is introducing a new notebook experience that provides data and AI teams with a high-performance, serverless programming environment for analytics and ML jobs. The new notebook experience includes Amazon SageMaker Data Agent, a built-in AI agent that accelerates development by generating code and SQL statements from natural language prompts while guiding users through their tasks.

To start a new notebook, choose the **Notebooks** menu in the left navigation pane to run SQL queries, Python code, and natural language, and to discover, transform, analyze, visualize, and share insights on data. You can get started with sample data such as customer analytics and retail sales forecasting.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/19/2025-sagemaker-unified-studio-4-new-notebooks-1.png)

When you choose a sample project for customer usage analysis, you can open sample notebook to explore customer usage patterns and behaviors in a telecom dataset.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/20/2025-sagemaker-unified-studio-5-notebook-data-1.png)

As I noted, the notebook includes a built-in AI agent that helps you interact with your data through natural language prompts. For example, you can start with data discovery using prompts like:

`Show me some insights and visualizations on the customer churn dataset.`

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/20/2025-sagemaker-unified-studio-5-notebook-genai-2.jpg)

After you identify relevant tables, you can request specific analysis to generate Spark SQL. The AI agent creates step-by-step plans with initial code for data transformations and Python code for visualizations. If you see an error message while running the generated code, choose **Fix with AI** to get help resolving it. Here is a sample result:

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/20/2025-sagemaker-unified-studio-5-notebook-genai-visual-1.jpg)

For ML workflows, use specific prompts like:

`Build an XGBoost classification model for churn prediction using the churn table, with purchase frequency, average transaction value, and days since last purchase as features.`

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/20/2025-sagemaker-unified-studio-6-notebook-ml-prompt-3.png)

This prompt receives structured responses including a step-by-step plan, data loading, feature engineering, and model training code using the SageMaker AI capabilities, and evaluation metrics. SageMaker Data Agent works best with specific prompts and is optimized for AWS data processing services including Athena for Apache Spark and SageMaker AI.

To learn more about new notebook experience, visit the [Amazon SageMaker Unified Studio User Guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

**Now available**

One-click onboarding and the new notebook experience in Amazon SageMaker Unified Studio are now available in US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Singapore), and Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Frankfurt), Europe (Ireland) Regions. To learn more, visit the [SageMaker Unified Studio product page](https://aws.amazon.com/sagemaker/unified-studio/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

Give it a try in the [SageMaker console](https://console.aws.amazon.com/datazone/home?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and send feedback to [AWS re:Post for SageMaker Unified Studio](https://repost.aws/tags/TAdXqriMJIT6CL4ervYlUgow/amazon-sagemaker-unified-studio?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) or through your usual AWS Support contacts.

— [Channy](https://linkedin.com/in/channy)

![Channy Yun (윤석찬)](https://d2908q01vomqb2.cloudfront.net/7b52009b64fd0a2a49e6d8a939753077792b0554/2020/06/05/channyun_400x400.jpg)

### [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)")

Channy is a Lead Blogger of AWS News Blog and Principal Developer Advocate for AWS Cloud. As an open web enthusiast and blogger at heart, he loves community-driven learning and sharing of technology.

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