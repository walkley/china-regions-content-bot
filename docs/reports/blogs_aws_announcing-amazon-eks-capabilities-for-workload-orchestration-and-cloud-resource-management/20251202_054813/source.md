# Announcing Amazon EKS Capabilities for workload orchestration and cloud resource management

by Channy Yun (윤석찬) on 30 NOV 2025 in Amazon Elastic Kubernetes Service, AWS re:Invent, Compute, Launch, News, Open Source Permalink  Comments   Share

|  |
| --- |
| [Voiced by Polly](https://aws.amazon.com/polly/) |

Today, we’re announcing [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) Capabilities, an extensible set of Kubernetes-native solutions that streamline workload orchestration, [Amazon Web Services (AWS)](https://aws.amazon.com/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) cloud resource management, and Kubernetes resource composition and orchestration. These fully managed, integrated platform capabilities include open source Kubernetes solutions that many customers are using today, such as [Argo CD](https://argoproj.github.io/cd/), [AWS Controllers for Kubernetes](https://github.com/aws-controllers-k8s/community), and [Kube Resource Orchestrator](https://kro.run/).

With EKS Capabilities, you can build and scale Kubernetes applications without managing complex solution infrastructure. Unlike typical in-cluster installations, these capabilities actually run in EKS service-owned accounts that are fully abstracted from customers.

With AWS managing infrastructure scaling, patching, and updates of these cluster capabilities, you can use the enterprise reliability and security without needing to maintain and manage the underlying components.

Here are the capabilities available at launch:

- **Argo CD** – This is a declarative GitOps tool for Kubernetes that provides continuous continuous deployment (CD) capabilities for Kubernetes. It’s broadly adopted, with more than 45% of Kubernetes end-users reporting production or planned production use in the [2024 Cloud Native Computing Foundation (CNCF) Survey](https://www.cncf.io/reports/cncf-annual-survey-2024/).
- **AWS Controllers for Kubernetes (ACK)** – ACK is highly popular with enterprise platform teams in production environments. ACK provides custom resources for Kubernetes that enable the management of AWS Cloud resources directly from within your clusters.
- **Kube Resource Orchestrator (KRO)** – KRO provides a streamlined way to create and manage custom resources in Kubernetes. With KRO, platform teams can create reusable resource bundles that abstract away complexity while remaining natively to the Kubernetes ecosystem.

With these features, you can accelerate and scale your Kubernetes use with fully managed capabilities, using its opinionated but flexible features to build for scale right from the start. It is designed to offer a set of foundational cluster capabilities that layer seamlessly with each other, providing integrated features for continuous deployment, resource orchestration, and composition. You can focus on managing and shipping software without needing to spend time and resources building and managing these foundational platform components.

**How it works**

Platform engineers and cluster administrators can set up EKS Capabilities to offload building and managing custom solutions to provide common foundational services, meaning they can focus on more differentiated features that matter to your business.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/05/2025-eks-capabilities-1.png)

Your application developers primarily work with EKS Capabilities as they do other Kubernetes features. They do this by applying declarative configuration to create Kubernetes resources using familiar tools, such as `kubectl` or through automation from `git commit` to running code.

**Get started with EKS Capabilities**

To enable EKS Capabilities, you can use the [EKS console](https://us-west-2.console.aws.amazon.com/eks/clusters?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [eksctl](https://docs.aws.amazon.com/eks/latest/eksctl/what-is-eksctl.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), or other preferred tools. In the EKS console, choose **Create capabilities** in the **Capabilities** tab on your existing EKS cluster. EKS Capabilities are AWS resources, and they can be tagged, managed, and deleted.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/14/2025-eks-capabilities-2.png)

You can select one or more capabilities to work together. I checked all three capabilities: ArgoCD, ACK, and KRO. However, these capabilities are completely independent and you can pick and choose which capabilities you want enabled on your clusters.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/10/2025-eks-capabilities-3.jpg)

Now you can configure selected capabilities. You should create [AWS Identity and Access Management (AWS IAM)](https://aws.amazon.com/iam/) roles to enable EKS to operate these capabilities within your cluster. Please note you cannot modify the capability name, namespace, authentication region, or [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) instance after creating the capability. Choose **Next** and review the settings and enable capabilities.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/25/2025-eks-capabilities-4.jpg)

Now you can see and manage created capabilities. Select **ArgoCD** to update configuration of the capability.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/10/2025-eks-capabilities-6-1.png)

You can see details of ArgoCD capability. Choose **Edit** to change configuration settings or **Monitor ArgoCD** to show the health status of the capability for the current EKS cluster.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/10/2025-eks-capabilities-7.png)

Choose **Go to Argo UI** to visualize and monitor deployment status and application health.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/10/2025-eks-capabilities-9.png)

To learn more about how to set up and use each capability in detail, visit [Getting started with EKS Capabilities](https://docs.aws.amazon.com/eks/latest/userguide/capabilities.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the Amazon EKS User Guide.

**Things to know**

Here are key considerations to know about this feature:

- **Permissions** – EKS Capabilities are cluster-scoped administrator resources, and resource permissions are configured through AWS IAM. For some capabilities, there is additional configuration for single sign-on. For example, Argo CD single sign-on configuration is enabled directly in EKS with a direct integration with IAM Identity Center.
- **Upgrades** – EKS automatically updates cluster capabilities you enable and their related dependencies. It automatically analyzes for breaking changes, patches and updates components as needed, and informs you of conflicts or issues through the EKS cluster insights.
- **Adoptions** – ACK provides resource adoption features that enable migration of existing AWS resources into ACK management. ACK also provides read-only resources which can help facilitate a step-wise migration from provisioned resources with Terraform, [AWS CloudFormation](https://aws.amazon.com/cloudformation/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) into EKS Capabilities.

**Now available**

Amazon EKS Capabilities are now available in commercial AWS Regions. For Regional availability and future roadmap, visit the [AWS Capabilities by Region](https://builder.aws.com/capabilities/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). There are no upfront commitments or minimum fees, and you only pay for the EKS Capabilities and resources that you use. To learn more, visit the [EKS pricing page](https://aws.amazon.com/eks/pricing/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

Give it a try in the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/cluster-create?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and send feedback to [AWS re:Post for EKS](https://repost.aws/tags/TA4IvCeWI1TE66q4jEj4Z9zg/amazon-elastic-kubernetes-service?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) or through your usual AWS Support contacts.

— [Channy](https://linkedin.com/in/channy)