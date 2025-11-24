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

# Build production-ready applications without infrastructure complexity using Amazon ECS Express Mode

by [Donnie Prakoso](https://aws.amazon.com/blogs/aws/author/donnie/ "Posts by Donnie Prakoso") on 21 NOV 2025 in [Amazon Elastic Container Registry](https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-registry/ "View all posts in Amazon Elastic Container Registry"), [Amazon Elastic Container Service](https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-service/ "View all posts in Amazon Elastic Container Service"), [Compute](https://aws.amazon.com/blogs/aws/category/compute/ "View all posts in Compute"), [Containers](https://aws.amazon.com/blogs/aws/category/containers/ "View all posts in Containers"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/build-production-ready-applications-without-infrastructure-complexity-using-amazon-ecs-express-mode/)  [Comments](https://aws.amazon.com/blogs/aws/build-production-ready-applications-without-infrastructure-complexity-using-amazon-ecs-express-mode/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Deploying containerized applications to production requires navigating hundreds of configuration parameters across load balancers, auto scaling policies, networking, and security groups. This overhead delays time to market and diverts focus from core application development.

Today, I’m excited to announce Amazon ECS Express Mode, a new capability from [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) that helps you launch highly available, scalable containerized applications with a single command. ECS Express Mode automates infrastructure setup including domains, networking, load balancing, and auto scaling through simplified APIs. This means you can focus on building applications while deploying with confidence using [Amazon Web Services (AWS)](https://aws.amazon.com/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) best practices. Furthermore, when your applications evolve and require advanced features, you can seamlessly configure and access the full capabilities of the resources, including Amazon ECS.

You can get started with Amazon ECS Express Mode by navigating to the [Amazon ECS console](https://console.aws.amazon.com/ecs/).

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/08/news-2025-11-ecs-express-01.png)

Amazon ECS Express Mode provides a simplified interface to the Amazon ECS service resource with new integrations for creating commonly used resources across AWS. ECS Express Mode automatically provisions and configures ECS clusters, task definitions, Application Load Balancers, auto scaling policies, and Amazon Route 53 domains from a single entry point.

**Getting started with ECS Express Mode** Let me walk you through how to use Amazon ECS Express Mode. I’ll focus on the console experience, which provides the quickest way to deploy your containerized application.

For this example, I’m using a simple container image application running on Python with the Flask framework. Here’s the `Dockerfile` of my demo, which I have pushed to an [Amazon Elastic Container Registry (Amazon ECR)](https://aws.amazon.com/ecr/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) repository:

```
# Build stage
FROM python:3.6-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt gunicorn

# Runtime stage
FROM python:3.6-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY app.py .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 80
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
```

On the Express Mode page, I choose **Create**. The interface is streamlined — I specify my container image URI from Amazon ECR, then select my task execution role and infrastructure role. If you don’t already have these roles, choose **Create new role** in the drop down to have one created for you from the [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) managed policy.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/08/news-2025-11-ecs-express-02.png)

If I want to customize the deployment, I can expand the **Additional configurations** section to define my cluster, container port, health check path, or environment variables.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/08/news-2025-11-ecs-express-03.png)

In this section, I can also adjust CPU, memory, or scaling policies.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/08/news-2025-11-ecs-express-04.png)

Setting up logs in [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) is something I always configure so I can troubleshoot my applications if needed. When I’m happy with the configurations, I choose **Create**.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/08/news-2025-11-ecs-express-04-1.png)

After I choose **Create**, Express Mode automatically provisions a complete application stack, including an Amazon ECS service with [AWS Fargate](https://aws.amazon.com/fargate/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) tasks, Application Load Balancer with health checks, auto scaling policies based on CPU utilization, security groups and networking configuration, and a custom domain with an AWS provided URL. I can also follow the progress in **Timeline view** on the **Resources** tab.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/08/news-2025-11-ecs-express-05.png)

If I need to do a programmatic deployment, the same result can be achieved with a single [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) command:

```
aws ecs create-express-gateway-service \
--image [ACCOUNT_ID].ecr.us-west-2.amazonaws.com/myapp:latest \
--execution-role-arn arn:aws:iam::[ACCOUNT_ID]:role/[IAM_ROLE] \
--infrastructure-role-arn arn:aws:iam::[ACCOUNT_ID]:role/[IAM_ROLE]
```

After it’s complete, I can see my application URL in the console and access my running application immediately.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/08/news-2025-11-ecs-express-07.png)

After the application is created, I can see the details by visiting the specified cluster, or the default cluster if I didn’t specify one, in the ECS service to monitor performance, view logs, and manage the deployment.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/08/news-2025-11-ecs-express-09-1.png)

When I need to update my application with a new container version, I can return to the console, select my Express service, and choose **Update**. I can use the interface to specify a new image URI or adjust resource allocations.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/08/news-2025-11-ecs-express-08.png)

Alternatively, I can use the AWS CLI for updates:

```
aws ecs update-express-gateway-service \
  --service-arn arn:aws:ecs:us-west-2:[ACCOUNT_ID]:service/[CLUSTER_NAME]/[APP_NAME] \
  --primary-container '{
    "image": "[IMAGE_URI]"
  }'
```

I find the entire experience reduces setup complexity while still giving me access to all the underlying resources when I need more advanced configurations.

**Additional things to know** Here are additional things about ECS Express Mode:

* **Availability** – ECS Express Mode is available in all [AWS Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region) at launch.
* **[Infrastructure as Code](https://aws.amazon.com/what-is/iac/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) support** – You can use IaC tools such as [AWS CloudFormation](https://aws.amazon.com/cloudformation/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el), [AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el), or Terraform to deploy your applications using Amazon ECS Express Mode.
* **Pricing** – There is no additional charge to use Amazon ECS Express Mode. You pay for AWS resources created to launch and run your application.
* **Application Load Balancer sharing** – The ALB created is automatically shared across up to 25 ECS services using host-header based listener rules. This helps distribute the cost of the ALB significantly.

Get started with Amazon ECS Express Mode through the Amazon ECS console. Learn more on the [Amazon ECS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html) page.

Happy building!

— [Donnie](https://www.linkedin.com/in/donnieprakoso)

![Donnie Prakoso](https://d2908q01vomqb2.cloudfront.net/667be543b02294b7624119adc3a725473df39885/2023/05/30/donnie_profile_400x400.jpeg)

### [Donnie Prakoso](https://aws.amazon.com/blogs/aws/author/donnie/ "Posts by Donnie Prakoso")

Donnie Prakoso is a software engineer, self-proclaimed barista, and Principal Developer Advocate at AWS. With more than 17 years of experience in the technology industry, from telecommunications, banking to startups. He is now focusing on helping the developers to understand varieties of technology to transform their ideas into execution. He loves coffee and any discussion of any topics from microservices to AI / ML.

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