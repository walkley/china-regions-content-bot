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

# Monitor network performance and traffic across your EKS clusters with Container Network Observability

by [Donnie Prakoso](https://aws.amazon.com/blogs/aws/author/donnie/ "Posts by Donnie Prakoso") on 19 NOV 2025 in [Amazon CloudWatch](https://aws.amazon.com/blogs/aws/category/management-tools/amazon-cloudwatch/ "View all posts in Amazon CloudWatch"), [Amazon Elastic Kubernetes Service](https://aws.amazon.com/blogs/aws/category/compute/amazon-kubernetes-service/ "View all posts in Amazon Elastic Kubernetes Service"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Compute](https://aws.amazon.com/blogs/aws/category/compute/ "View all posts in Compute"), [DevOps](https://aws.amazon.com/blogs/aws/category/devops/ "View all posts in DevOps"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [Management & Governance](https://aws.amazon.com/blogs/aws/category/management-and-governance/ "View all posts in Management & Governance"), [Management Tools](https://aws.amazon.com/blogs/aws/category/management-tools/ "View all posts in Management Tools"), [Monitoring and observability](https://aws.amazon.com/blogs/aws/category/management-and-governance/monitoring-and-observability/ "View all posts in Monitoring and observability"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/monitor-network-performance-and-traffic-across-your-eks-clusters-with-container-network-observability/)  [Comments](https://aws.amazon.com/blogs/aws/monitor-network-performance-and-traffic-across-your-eks-clusters-with-container-network-observability/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Organizations are increasingly expanding their Kubernetes footprint by deploying microservices to incrementally innovate and deliver business value faster. This growth places increased reliance on the network, giving platform teams exponentially complex challenges in monitoring network performance and traffic patterns in EKS. As a result, organizations struggle to maintain operational efficiency as their container environments scale, often delaying application delivery and increasing operational costs.

Today, I’m excited to announce **Container Network Observability in [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el)**, a comprehensive set of network observability features in Amazon EKS that you can use to better measure your network performance in your system and dynamically visualize the landscape and behavior of network traffic in EKS.

Here’s a quick look at Container Network Observability in Amazon EKS:

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/18/2025-news-eks-container-network-observability-rev-6.png)

Container Network Observability in EKS addresses observability challenges by providing enhanced visibility of workload traffic. It offers performance insights into network flows within the cluster and those with cluster-external destinations. This makes your EKS cluster network environment more observable while providing built-in capabilities for more precise troubleshooting and investigative efforts.

**Getting started with Container Network Observability in EKS**

I can enable this new feature for a new or existing EKS cluster. For a new EKS cluster, during the **Configure observability** setup, I navigate to the **Configure network observability** section. Here, I select **Edit container network observability**. I can see there are three included features: **Service map**, **Flow table**, and **Performance metric endpoint**, which are enabled by [Amazon CloudWatch Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor.html).

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/19/image-8-4.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/19/image-8-4.png)

On the next page, I need to install the **AWS Network Flow Monitor Agent**.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/13/2025-news-eks-container-network-observability-2.png)

After it’s enabled, I can navigate to my EKS cluster and select **Monitor cluster**.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/13/2025-news-eks-container-network-observability-3.png)

This will bring me to my cluster observability dashboard. Then, I select the **Network** tab.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/13/2025-news-eks-container-network-observability-4.png)

**Comprehensive observability features** Container Network Observability in EKS provides several key features, including performance metrics, service map, and flow table with three views: AWS service view, cluster view, and external view.

With **Performance metrics**, you can now scrape network-related system metrics for pods and worker nodes directly from the Network Flow Monitor agent and send them to your preferred monitoring destination. Available metrics include ingress/egress flow counts, packet counts, bytes transferred, and various allowance exceeded counters for bandwidth, packets per second, and connection tracking limits. The following screenshot shows an example of how you can use [Amazon Managed Grafana](https://aws.amazon.com/grafana/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) to visualize the performance metrics scraped using Prometheus.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/13/2025-news-eks-container-network-observability-8.png)

With the **Service map** feature, you can dynamically visualize intercommunication between workloads in your cluster, making it straightforward to understand your application topology with a quick look. The service map helps you quickly identify performance issues by highlighting key metrics such as retransmissions, retransmission timeouts, and data transferred for network flows between communicating pods.

Let me show you how this works with a sample e-commerce application. The service map provides both high-level and detailed views of your microservices architecture. In this e-commerce example, we can see three core microservices working together: the **GraphQL service** acts as an API gateway, orchestrating requests between the frontend and backend services.

When a customer browses products or places an order, the GraphQL service coordinates communication with both the **products service** (for catalog data, pricing, and inventory) and the **orders service** (for order processing and management). This architecture allows each service to scale independently while maintaining clear separation of concerns.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/17/2025-news-eks-container-network-observability-rev-1.png)

For deeper troubleshooting, you can expand the view to see individual pod instances and their communication patterns. The detailed view reveals the complexity of microservices communication. Here, you can see multiple pod instances for each service and the network of connections between them.

This granular visibility is crucial for identifying issues like uneven load distribution, pod-to-pod communication bottlenecks, or when specific pod instances are experiencing higher latency. For example, if one GraphQL pod is making disproportionately more calls to a particular products pod, you can quickly spot this pattern and investigate potential causes.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/17/2025-news-eks-container-network-observability-rev-2.png)

Use the **Flow table** to monitor the top talkers across Kubernetes workloads in your cluster from three different perspectives, each providing unique insights into your network traffic patterns.

**Flow table** – Monitor the top talkers across Kubernetes workloads in your cluster from three different perspectives, each providing unique insights into your network traffic patterns:

* **AWS service view** shows which workloads generate the most traffic to Amazon Web Services (AWS) services such as [Amazon DynamoDB](https://aws.amazon.com/dynamodb/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) and [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el), so you can optimize data access patterns and identify potential cost optimization opportunities.
* **The Cluster view** reveals the heaviest communicators within your cluster (east-west traffic), which means you can spot chatty microservices that might benefit from optimization or colocation strategies
* **External view**identifies workloads with the highest traffic to destinations outside AWS (internet or on premises), which is useful for security monitoring and bandwidth management.

The flow table provides detailed metrics and filtering capabilities to analyze network traffic patterns. In this example, we can see the flow table displaying cluster view traffic between our e-commerce services. The table shows that the `orders` pod is communicating with multiple `products` pods, transferring amounts of data. This pattern suggests the orders service is making frequent product lookups during order processing.

The filtering capabilities are useful for troubleshooting, for example, to focus on traffic from a specific orders pod. This granular filtering helps you quickly isolate communication patterns when investigating performance issues. For instance, if customers are experiencing slow checkout times, you can filter to see if the orders service is making too many calls to the products service, or if there are network bottlenecks between specific pod instances.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/17/2025-news-eks-container-network-observability-rev-5.png)

**Additional things to know** Here are key points to note about Container Network Observability in EKS:

* **Pricing** – For network monitoring, you pay standard Amazon CloudWatch Network Flow Monitor pricing.
* **Availability** – Container Network Observability in EKS is available in all commercial AWS regions where Amazon CloudWatch Network Flow Monitor is available.
* **Export metrics to your preferred monitoring solution** – Metrics are available in OpenMetrics format, compatible with Prometheus and Grafana. For configuration details, refer to [Network Flow Monitor documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor.html).

Get started with [Container Network Observability in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/network-observability.html) today to improve network observability in your cluster.

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