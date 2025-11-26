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

## [Networking & Content Delivery](https://aws.amazon.com/blogs/networking-and-content-delivery/)

# Introducing URL and host header rewrite with AWS Application Load Balancers

by Mohamad Naji and Mahmoud Elhusseiny on 15 OCT 2025 in [Amazon VPC](https://aws.amazon.com/blogs/networking-and-content-delivery/category/compute/amazon-vpc/ "View all posts in Amazon VPC"), [Announcements](https://aws.amazon.com/blogs/networking-and-content-delivery/category/post-types/announcements/ "View all posts in Announcements"), [Elastic Load Balancing](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/elastic-load-balancing/ "View all posts in Elastic Load Balancing"), [Networking & Content Delivery](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/ "View all posts in Networking & Content Delivery") [Permalink](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-url-and-host-header-rewrite-with-aws-application-load-balancers/) Share

Today we’re announcing the general availability of rewriting URLs and host headers natively on Amazon Web Services (AWS) [Application Load Balancers (ALB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html). You can use this new feature to implement regex matches based on request parameters and rewrite both host headers and URLs before routing to your targets.

Operating at Layer 7 (application layer) of the [OSI model](https://en.wikipedia.org/wiki/OSI_model), ALBs distribute incoming traffic across multiple targets—such as Amazon Elastic Compute Cloud (Amazon [EC2](https://aws.amazon.com/ec2/)) [instances](https://aws.amazon.com/ec2/), [containers](https://aws.amazon.com/containers/), [AWS Lambda](https://aws.amazon.com/pm/lambda/) functions, and IP addresses—across your AWS [Availability Zones (AZs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html). The service continuously monitors target health to make sure that traffic flows only to operational resources while automatically scaling to accommodate changing traffic patterns. Until now, implementing URL or host header modifications has necessitated either custom application logic or deploying and maintaining third-party proxy solutions.

Today’s announcement eliminates that complexity by integrating more routing capabilities directly into the ALB service. Organizations can now implement advanced request routing scenarios through their existing AWS managed infrastructure without more components. You can consolidate these functions into the ALB itself to benefit from the streamlined architecture, reduced maintenance overhead, lower costs, and decreased latency, while creating a more direct request path for your applications.

## **How it Works**

Regex matching on conditions and URL path and host header rewrites natively on ALBs can be configured on [new](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html) and [existing](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-load-balancer-attributes.html) ALBs through the [AWS Management Console](https://aws.amazon.com/console/), [AWS SDK](https://builder.aws.com/build/tools), or [AWS API](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/Welcome.html). As shown in Figure 1, third-party proxies can now be fully replaced by the new native functionality of ALBs, which supports both rewriting and removing path segments from incoming requests before routing them to the appropriate target group.

![URL rewrite on ALB with target groups](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/10/06/Picture1-2.png)

*Figure 1: URL rewrite on ALB with target groups*

Similarly, Kubernetes users, particularly those using the ALB Ingress Controller, needed path rewriting to properly route traffic to containerized services. They had to implement proxies, such as NGINX Ingress Controller, which added unnecessary complexity to [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/) deployments. The new ALB feature (as shown in Figure 2) now enables users to fully use ALBs while streamlining their microservices architectures.

![URL rewrite on ALB with EKS target groups](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/10/06/Picture2.png)

*Figure 2: URL rewrite on ALB with EKS target groups*

To demonstrate this with an example, we consider the following scenario: An international company maintains an application supporting multiple languages. The architecture is currently split into:

* + French and English backends: already migrated and deployed on Amazon EKS and running with the latest API version 2 (V2).
  + All other language backends: Currently operating on EC2 instances using the legacy API version 1 (V1).

The company is progressively migrating all languages traffic to run on Amazon EKS. It supports the latest API version (V2) and needs to handle URL versioning transparently without modifying any frontend application code.

### **1. Rules streamlining: setting up conditions with regex matching**

Starting today, the Conditions rules have expanded to include two match pattern types:

|  |  |  |
| --- | --- | --- |
| Pattern type | Description | Best for |
| Value matching (existing) | Uses global syntax for basic pattern matching | Routing rules with exact or wildcard matches |
| Regex matching (new) | Enables more sophisticated pattern recognition with regex | Complex routing patterns and conditional logic |

For the use case mentioned previously, before regex support, routing language-specific traffic necessitate creating separate conditions for each language variant. For example, in our use case:

* + One rule was needed for English (en).
  + One rule was needed for French (fr).
  + A third rule was needed for all other language routes.

With regex support, given that both French and English domains are routed to the same EKS cluster running the latest API version (V2), a single rule can handle both domains. This dramatically reduces configuration complexity and provides routing clarity.

To create (or modify the rule for existing ALBs) through the console (as shown in Figure 3), follow these steps:

* + Navigate to your ALB listener rules.
  + Choose the rule you want to modify or create a new one.
  + For host header conditions, choose Regex matching. Regex matching can also be used for path conditions and HTTP header conditions.
  + Enter your regex pattern in the value field. For our use case: ^(en|fr)\.example\.com

![Regex configuration example at the conditions level](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/10/06/pic3-blog.gif)

*Figure 3: Regex configuration example at the conditions level*

A test can be performed using the Regex tester to verify the correct syntax (as shown in Figure 4):

![Regex syntax tester to confirm validity of Regex expressions on conditions](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/10/06/pic4-blog.gif)

*Figure 4: Regex syntax tester to confirm validity of Regex expressions on conditions*

Although routing is powerful, our migration scenario necessitates more than just directing traffic. We need to implement URL transformation to avoid modifying the application code.

### **2. URL transformation: introducing transforms**

Transforms enable you to modify incoming requests before they reach your backend targets. This functionality is positioned between your conditions and actions in the request processing flow.

A common use case is the manipulation of path prefixes, which includes stripping, modifying, or adding them. In our version migration scenario, when we migrate other languages (such as Spanish) to Amazon EKS and need to modify the path to the new API (version 2), we can use the path transforms capability. To modify the path through the console (as shown in Figure 5) follow these steps:

* + Add a Transform URL path under the Transforms section in your rule.
  + Use regex to identify the pattern to transform (for example (^(en|fr|sp)\.example\.com\/v)1).
  + Define the replacement value (for example apply the regex syntax “$12” to replace number 1 with number 2).

![Configuring transforms with URL path](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/10/06/fig5-blog.gif)

*Figure 5: Configuring transforms with URL path*

Similar to testing with Regex in conditions, the console includes a convenient testing tool that helps you validate your transforms (as shown in Figure 6).

![Testing transforms where we see number 1 replaced by 2 in the path](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/10/06/fig6-blog.gif)

*Figure 6: Testing transforms where we see number 1 replaced by 2 in the path*

We have demonstrated how regex matching can be applied to path routing conditions and how the transforms capability enables path manipulation without necessitating code changes. Regex matching can be used with conditions independently of transforms, and transforms can be applied to standard value matching conditions.

This combination enables gradual migration strategies without forcing immediate, costly code changes throughout the entire application stack.

## **Conclusion**

In this post, we explored how to use this new feature, demonstrating its practical implementation and showcasing several real-world scenarios where it can significantly improve your application architecture.

This combination of regex matching and request transforms provides control over traffic flows through your ALB to your backend services, all without needing more infrastructure or code changes.

This feature is now available in [AWS commercial Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), [AWS GovCloud (US) Regions](https://aws.amazon.com/govcloud-us/) and [AWS China Regions](https://www.amazonaws.cn/en/about-aws/china/). To learn more about ALB capabilities, consult the [Application Load Balancer documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/). If you have questions about this post, then you can start a new thread on [AWS re:Post](https://repost.aws/) or contact [AWS Support](https://aws.amazon.com/contact-us/).

##

## About the authors

![Mohamad Naji picture](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2024/04/04/mgnaji-photo-2.jpg)

### Mohamad Naji

Mohamad Naji is a Senior Solutions Architect at Amazon Web Services. Based in Montreal, he has over 15 years of experience in the IT industry and primarily works with Financial Services customers. He focuses on helping customers build and develop architectures for highly scalable and resilient AWS environments. Outside work, he loves all kind of sports and a keen traveler.

![Mahmoud ElHousseiny picture](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/10/14/mahelh7.jpg)

### Mahmoud Elhusseiny

Mahmoud Elhusseiny is a Senior Solutions Architect in AWS, working with customers in the Middle East, North Africa, and Turkey. His extensive experience extends across various technology and industry verticals, rendering him a trusted advisor for numerous enterprises, digital-centered businesses, and independent software vendors, facilitating their seamless navigation and acceleration of their cloud journey and helping them innovate new solutions that enhances their end user experience and increase their business efficiency.

### Resources

* [Networking Products](https://aws.amazon.com/products/networking?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=networking-resources)
* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=networking-resources)
* [Amazon CloudFront](https://aws.amazon.com/cloudfront?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=networking-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
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