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

# AWS Weekly Roundup: How to join AWS re:Invent 2025, plus Kiro GA, and lots of launches (Nov 24, 2025)

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 24 NOV 2025 in [Amazon API Gateway](https://aws.amazon.com/blogs/aws/category/application-services/amazon-api-gateway-application-services/ "View all posts in Amazon API Gateway"), [Amazon Aurora](https://aws.amazon.com/blogs/aws/category/database/amazon-aurora/ "View all posts in Amazon Aurora"), [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon CloudWatch](https://aws.amazon.com/blogs/aws/category/management-tools/amazon-cloudwatch/ "View all posts in Amazon CloudWatch"), [Amazon Connect](https://aws.amazon.com/blogs/aws/category/messaging/amazon-connect/ "View all posts in Amazon Connect"), [Amazon EC2](https://aws.amazon.com/blogs/aws/category/compute/amazon-ec2/ "View all posts in Amazon EC2"), [Amazon Elastic Container Registry](https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-registry/ "View all posts in Amazon Elastic Container Registry"), [Amazon Elastic Container Service](https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-service/ "View all posts in Amazon Elastic Container Service"), [Amazon Elastic Kubernetes Service](https://aws.amazon.com/blogs/aws/category/compute/amazon-kubernetes-service/ "View all posts in Amazon Elastic Kubernetes Service"), [Amazon OpenSearch Service](https://aws.amazon.com/blogs/aws/category/analytics/amazon-elasticsearch-service/ "View all posts in Amazon OpenSearch Service"), [Amazon SageMaker](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/sagemaker/ "View all posts in Amazon SageMaker"), [Amazon Simple Storage Service (S3)](https://aws.amazon.com/blogs/aws/category/storage/amazon-simple-storage-services-s3/ "View all posts in Amazon Simple Storage Service (S3)"), [AWS CloudFormation](https://aws.amazon.com/blogs/aws/category/management-tools/aws-cloudformation/ "View all posts in AWS CloudFormation"), [AWS Control Tower](https://aws.amazon.com/blogs/aws/category/management-tools/aws-control-tower/ "View all posts in AWS Control Tower"), [AWS Identity and Access Management (IAM)](https://aws.amazon.com/blogs/aws/category/security-identity-compliance/aws-identity-and-access-management-iam/ "View all posts in AWS Identity and Access Management (IAM)"), [AWS Lambda](https://aws.amazon.com/blogs/aws/category/compute/aws-lambda/ "View all posts in AWS Lambda"), [AWS Step Functions](https://aws.amazon.com/blogs/aws/category/application-services/aws-step-functions/ "View all posts in AWS Step Functions"), [Billing & Account Management](https://aws.amazon.com/blogs/aws/category/aws-cloud-financial-management/billing-and-account-management/ "View all posts in Billing & Account Management"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-how-to-join-aws-reinvent-2025-plus-kiro-ga-and-lots-of-launches-nov-24-2025/)  [Comments](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-how-to-join-aws-reinvent-2025-plus-kiro-ga-and-lots-of-launches-nov-24-2025/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/24/reInvent-2025-logo-300x108.jpg)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/24/reInvent-2025-logo.jpg)Next week, don’t miss **[AWS re:Invent](https://reinvent.awsevents.com/),** Dec. 1-5, 2025, for the latest AWS news, expert insights, and global cloud community connections! Our News Blog team is finalizing posts to introduce the most exciting launches from our service teams. If you’re joining us in person in Las Vegas, review the [agenda](https://reinvent.awsevents.com/agenda/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [session catalog,](https://registration.awsevents.com/flow/awsevents/reinvent2025/eventcatalog/page/eventcatalog??trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and [attendee guides](https://registration.awsevents.com/flow/awsevents/reinvent2025/AttendeeGuides/page/attendeeguidelanding?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) before arriving. Can’t attend in person? [Watch our Keynotes and Innovation Talks via livestream.](https://reinvent.awsevents.com/livestream/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)

**Kiro is now generally available**

Last week, [Kiro](https://kiro.dev/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), the first AI coding tool built around spec-driven development, became [generally available](https://kiro.dev/blog/general-availability/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). This tool, which we pioneered to bring more clarity and structure to agentic workflows, has already been embraced by over 250,000 developers since its preview release. The GA launch introduces four new capabilities: [property-based testing for spec correctness](https://kiro.dev/blog/property-based-testing/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) (which measures whether your code matches what you specified); [a new way to checkpoint your progress on Kiro](https://kiro.dev/blog/introducing-checkpointing/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el); [a new Kiro CLI bringing agents to your terminal](https://kiro.dev/blog/introducing-kiro-cli/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el); and [enterprise team plans](https://kiro.dev/enterprise/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) with centralized management.

**Last week’s launches**

We’ve announced numerous new feature and service launches as we approach re:Invent week. Key launches include:

* [Accelerate large-scale AI applications with the new Amazon EC2 P6-B300 instances](https://aws.amazon.com/blogs/aws/accelerate-large-scale-ai-applications-with-the-new-amazon-ec2-p6-b300-instances/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [Introducing flat-rate pricing plans with no overages for website delivery and security](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-flat-rate-pricing-plans-with-no-overages/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [New Amazon Bedrock service tiers help you match AI workload performance with cost](https://aws.amazon.com/blogs/aws/new-amazon-bedrock-service-tiers-help-you-match-ai-workload-performance-with-cost/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [Monitor network performance and traffic across your EKS clusters with Container Network Observability](https://aws.amazon.com/blogs/aws/monitor-network-performance-and-traffic-across-your-eks-clusters-with-container-network-observability/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [New: AWS Billing Transfer for centrally managing AWS billing and costs across multiple organizations](https://aws.amazon.com/blogs/aws/new-aws-billing-transfer-for-centrally-managing-aws-billing-and-costs-across-multiple-organizations/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [AWS Control Tower introduces a Controls Dedicated experience](https://aws.amazon.com/blogs/aws/aws-control-tower-introduces-a-controls-dedicated-experience/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [New business metadata features in Amazon SageMaker Catalog to improve discoverability across organizations](https://aws.amazon.com/blogs/aws/new-business-metadata-features-in-amazon-sagemaker-catalog-to-improve-discoverability-across-organizations/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [Streamlined multi-tenant application development with tenant isolation mode in AWS Lambda](https://aws.amazon.com/blogs/aws/streamlined-multi-tenant-application-development-with-tenant-isolation-mode-in-aws-lambda/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [Accelerate workflow development with enhanced local testing in AWS Step Functions](https://aws.amazon.com/blogs/aws/accelerate-workflow-development-with-enhanced-local-testing-in-aws-step-functions/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [Simplify access to external services using AWS IAM Outbound Identity Federation](https://aws.amazon.com/blogs/aws/simplify-access-to-external-services-using-aws-iam-outbound-identity-federation/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [Introducing attribute-based access control for Amazon S3 general purpose buckets](https://aws.amazon.com/blogs/aws/introducing-attribute-based-access-control-for-amazon-s3-general-purpose-buckets/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [Introducing VPC encryption controls: Enforce encryption in transit within and across VPCs in a Region](https://aws.amazon.com/blogs/aws/introducing-vpc-encryption-controls-enforce-encryption-in-transit-within-and-across-vpcs-in-a-region/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [Build production-ready applications without infrastructure complexity using Amazon ECS Express Mode](https://aws.amazon.com/blogs/aws/build-production-ready-applications-without-infrastructure-complexity-using-amazon-ecs-express-mode/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [New one-click onboarding and notebooks with a built-in AI agent in Amazon SageMaker Unified Studio](https://aws.amazon.com/blogs/aws/new-one-click-onboarding-and-notebooks-with-ai-agent-in-amazon-sagemaker-unified-studio/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* [Simplified developer access to AWS with ‘aws login’](https://aws.amazon.com/blogs/security/simplified-developer-access-to-aws-with-aws-login/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)

Here are some AWS bundled feature launches:

* **Amazon EKS** announces new [Provisioned Control Plane](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-eks-provisioned-control-plane/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and [fully managed MCP servers](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-eks-ecs-fully-managed-mcp-servers-preview?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) (preview) and [enhanced AI-powered troubleshooting](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-ecs-eks-ai-powered-troubleshooting-console/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the console with **Amazon ECS**.
* **Amazon ECR** introduces [managed container image signing](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-ecr-managed-container-image-signing?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [archive storage class for rarely accessed container images](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-ecr-archive-storage-class-container-images/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and [AWS PrivateLink for FIPS Endpoints](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-ecr-privatelink-fips-endpoints/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).
* **Amazon Aurora DSQL** provides an [integrated query editor](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-aurora-dsql-integrated-query-editor/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the console, s[tatement-level cost estimates](https://aws.amazon.com/about-aws/whats-new/2025/11/aurora-dsql-statement-level-cost-estimates-query-plans/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in query plans, [new Python, Node.js, and JDBC Connectors](https://aws.amazon.com/about-aws/whats-new/2025/11/aurora-dsql-python-node-js-jdbc-connectors-iam?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), up to [256 TiB of storage volume.](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-aurora-dsql-database-clusters-up-to-256-tib?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* **Amazon API Gateway** supports [response streaming for REST APIs](https://aws.amazon.com/about-aws/whats-new/2025/11/api-gateway-response-streaming-rest-apis/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [developer portal capabilities](https://aws.amazon.com/about-aws/whats-new/2025/11/api-gateway-developer-portal-capabilities/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and [additional TLS security policies for REST APIs.](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-api-gateway-tls-security-rest-apis/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
* **Amazon Connect** provides [conversational analytics for voice](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-connect-conversational-analytics/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [persistent agent connections for faster call handling](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-connect-persistent-agent-connections?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and [multi skill agent scheduling](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-connect-multi-skill-agent-scheduling?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).
* **Amazon CloudWatch** introduces [scheduled queries in Logs Insights](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-cloudwatch-scheduled-queries?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and [in-console agent management on EC2](https://aws.amazon.com/about-aws/whats-new/2025/11/cloudwatch-in-console-agent-management-ec2/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).
* **AWS CloudFormation** StackSets offers [deployment ordering for auto-deployment mode](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-cloudformation-stacksets-deployment-ordering/). You can define the sequence in which your stack instances automatically deploy across accounts and Regions.
* **AWS NAT Gateway** supports [Regional availability](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-nat-gateway-regional-availability/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) to create a single NAT Gateway that automatically expands and contracts across availability zones (AZs).
* **Amazon Bedrock** supports [OpenAI GPT OSS models for Custom Model Import](https://aws.amazon.com/about-aws/whats-new/2025/11/bedrock-model-import-openai-gpt-oss-models/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [coding use cases for Guardrails](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-bedrock-guardrails-coding-use-cases?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and [10 additional languages for speech analytics](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-bedrock-data-automation-10-languages/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for Data Automation.
* **Amazon OpenSearch** supports [Cluster Insights for improved operational visibility](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-opensearch-service-cluster-insights/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [backup and restore](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-opensearch-serverless-backup-and-restore-console?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and [audit logs for data plane APIs](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-opensearch-serverless-auditlogs-dataplane-apis?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in Serverless through the console.

See [AWS What’s New](https://aws.amazon.com/new/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for more launch news that I haven’t covered here, and we’ll see you next week at re:Invent!

– [Channy](https://twitter.com/channyun)

TAGS: [Week in Review](https://aws.amazon.com/blogs/aws/tag/week-in-review/)

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