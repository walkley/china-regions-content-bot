# Amazon EKS introduces Provisioned Control Plane

by Shyam Jeedigunta, George John, and Apoorva Kulkarni on 27 NOV 2025 in Amazon Elastic Kubernetes Service, Announcements, Compute, Technical How-to Permalink  Share

[Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS) powers tens of millions of clusters annually, with an architecture refined by years of real-world insights from thousands of customers running diverse workloads. EKS automatically scales your cluster’s control plane to meet your workload demands. This dynamic, intelligent scaling powers most use cases, handling everything from startup applications to enterprise platforms to mission critical workloads. Building on this proven architecture, we’re introducing capabilities designed for next-generation workloads with specialized requirements.

When you’re running AI training or inference workloads at ultra scale, running multi-tenant SaaS platforms, or running mission-critical web applications where every second matters, you need absolute predictability – the ability to guarantee control plane responsiveness before peak demand arrives. To meet these advanced requirements, we’re introducing EKS Provisioned Control Plane, an enhanced option that complements the Standard Control Plane capabilities.

## Delivering predictable and high performance at scale

Amazon EKS Provisioned Control Plane gives you the ability to pre-allocate control plane capacity from a set of new scaling tiers, ensuring predictable and high performance for your most demanding workloads. By provisioning capacity ahead of time, your cluster handles instantaneous traffic bursts without the need for control plane scaling, which is crucial for serving traffic during high-demand events or sudden workload spikes. These new scaling tiers unlock significantly higher control plane performance and scalability required for emerging workload patterns like ultra scale AI training/inference, high performance computing, or large-scale data processing.

Provisioned Control Plane allows you to choose from multiple control plane scaling tiers (XL, 2XL, 4XL) with each tier offering well defined performance on these Kubernetes attributes:

- API request concurrency – the volume of requests processed by the Kubernetes API servers concurrently
- Pod scheduling rate – the throughput at which the Kubernetes default scheduler assigns pods to nodes
- Cluster database size – the storage space allocated to etcd, the database that holds the cluster state/metadata

Once you designate a scaling tier to your cluster, EKS ensures sufficient capacity is always available to the control plane to meet the attribute values for that tier. You also get comprehensive visibility into your tier utilization through granular metrics for each attribute, available through both the EKS Prometheus metrics endpoint and [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics vended to your account. As your workload demands evolve, you can switch between scaling tiers or go back to the standard control plane at any time. Provisioned Control Plane is an opt-in feature with tiered pricing based on your capacity selection. Visit the [Amazon EKS pricing page](https://aws.amazon.com/eks/pricing/) to learn more.

| Scaling Tier | Tier attributes | | | Price ($/hr) |
| --- | --- | --- | --- | --- |
| API Request Concurrency (seats) | Pod Scheduling Rate (pods/sec) | Cluster Database Size (GB) |
| XL | 1700 | 167 | 16 | $1.65/hr |
| 2XL | 3400 | 283 | 16 | $3.40/hr |
| 4XL | 6800 | 400 | 16 | $6.90/hr |

Tier attribute values are specific to the EKS cluster version. The above values apply to EKS version 1.30 and later. You can lookup the values for each version under our [user guide](https://docs.aws.amazon.com/eks/latest/userguide/eks-provisioned-control-plane.html). If you need higher attributes for your cluster beyond the 4XL tier, contact your AWS account team and we’ll be happy to assist.

## How did we unlock this?

Over the years, EKS have been steadily making strides in cluster performance, scale and resiliency. Earlier this year, we announced support for [ultra-scale clusters](https://aws.amazon.com/blogs/containers/amazon-eks-enables-ultra-scale-ai-ml-workloads-with-support-for-100k-nodes-per-cluster/) capable of running up to 100,000 worker nodes purpose-built for computationally demanding workloads such as AI/ML training and inference. We made that possible through [innovations](https://aws.amazon.com/blogs/containers/under-the-hood-amazon-eks-ultra-scale-clusters/) across storage, API, controllers and the cluster data plane. We incorporated these architectural improvements, infrastructure optimizations and additional resiliency mechanisms to enhance the control plane performance and reliability. These are now accessible for all types of workloads.

For customers to run their clusters with enhanced reliability, scalability and high performance with Provisioned Control Plane, EKS handles several operations behind the scenes. First, we ensure sufficient capacity has been provisioned for the control plane and its underlying infrastructure at all times. This minimizes performance variability during traffic spikes by ensuring sufficient API server throughput, controller/scheduler capacity and database size are always available. This architecture delivers consistent performance across core scaling dimensions such as cluster size, API request rate, application churn, and more. Second, by managing a sophisticated set of throttling mechanisms across components within the control plane we allow gracefully handling traffic patterns beyond the provisioned limits, a critical piece in ensuring system reliability. Third, zonal redundancy, automated fail-overs and auto-scaling mechanisms always maintain enough capacity headroom for reliable cluster operation across planned as well as unplanned incidents. Finally, our new generation etcd architecture has enabled larger databases that deliver superior durability and recovery times while maintaining high performance.

## Getting started with Provisioned Control Plane

Amazon EKS Provisioned Control Plane is available for new and existing EKS clusters running Kubernetes version 1.29 and above. You can get started with Provisioned Control Plane using AWS Management Console, AWS CLI, [eksctl](https://github.com/eksctl-io/eksctl/releases/tag/v0.218.0), [AWS CloudFormation](https://aws.amazon.com/cloudformation/), or Hashicorp [Terraform](https://github.com/hashicorp/terraform-provider-aws/releases/tag/v6.23.0). This guide shows you how to create and update clusters using the AWS Management Console. You can configure your cluster’s control plane scaling tier when creating a new cluster or update the cluster configuration at a later time. In this section, we demonstrate how to create a cluster with a specific control plane tier and how to update the tier as your workload requirements change. For more information see our Getting Started guide.

### Creating a cluster with Provisioned Control Plane

When creating a new EKS cluster, you can specify the control plane tier using the control plane scaling tier section in the Custom configuration tab as shown below. If you don’t select a scaling tier, your cluster will use the standard control plane by default.

![Create EKS cluster with provisioned control plane scaling tier](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/image1-7-998x1024.png)

### Updating control plane scaling tier

As your workload requirements change, you can update your cluster’s control plane tier without recreating the cluster. You may also use this method for your existing clusters that need to scale up. For example, if you’re preparing for a high-traffic event or scaling up your batch processing workloads, you can upgrade to a higher tier. Similarly, you can scale down to a lower tier during periods of reduced demand to optimize costs. To change your control plane’s scaling tier, in the cluster details view, go to overview tab, and click “manage” in the Control plane scaling tier section. And then choose the appropriate control plane scaling tier:

![Update EKS control plance scaling tier](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/image2-5-1024x364.png)

### Monitoring control plane scaling tier utilization

Keeping track of your cluster’s control plane performance is straightforward in the AWS Management Console. Simply click the “Monitor cluster” button in the cluster details view.

![Cluster information](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/image4-7-1024x212.png)

Once there, navigate to the “Control plane monitoring” tab, where you’ll find the “Control Plane scaling” section. This dashboard provides valuable insights into your scaling tier’s capacity thresholds and offers a real-time view of how your cluster’s utilization measures up against these limits, helping you make informed scaling decisions.

![Monitoring control plane scaling tier utilization](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/image5-5-1024x785.png)

## Benchmarking with Provisioned Control Plane

To validate the EKS Provisioned Control Plane’s performance characteristics we used [cluster-loader2](https://github.com/kubernetes/perf-tests/tree/master/clusterloader2), a standard open-source Kubernetes stress-testing tool. We created an EKS cluster on a 4XL control plane tier with other supporting cluster configurations for running workloads at scale. We configured the VPC with multiple subnets and CIDR blocks to provide sufficient IP space. For compute, we deployed [Karpenter](https://karpenter.sh/) with static node pools across multiple availability zones. We used [AWS VPC CNI](https://github.com/aws/amazon-vpc-cni-k8s) with Prefix Delegation and warm prefix mode to boost pod launches. Finally, we pulled container images from Amazon ECR ([Amazon Elastic Container Registry](https://aws.amazon.com/ecr/)) with [SOCI-optimized containerd](https://aws.amazon.com/blogs/containers/introducing-seekable-oci-parallel-pull-mode-for-amazon-eks/) on the nodes for high throughput.

The workload simulated a large-scale platform running multiple stateless services, batch processing jobs, and system-level daemonsets. The micro-services represent typical web application workloads with multiple replicas performing lightweight compute tasks, while jobs handle batch processing tasks with a high degree of parallelism. The daemonsets provide essential cluster functionality around monitoring, networking, health and telemetry on each node. Throughout the test, we progressively stressed the cluster with sustained and spiky workloads. This validated the 4XL tier’s advertised capabilities for API concurrency, pod scheduling throughput, and etcd database size. Also, assessing the static stability of the cluster at the tier’s capacity was a key objective.

This benchmark represents a specific test scenario illustrating how a provisioned control plane pushes the envelope much further beyond what’s already possible with our standard control plane today. Think of these as directional indicators rather than absolute limits; your actual mileage will vary based on your workload characteristics.

| Resource type | Standard Control Plane | Provisioned Control Plane – 4XL tier |
| --- | --- | --- |
| Nodes | 5,000 | 40,000 |
| Pods | 80,000 | 640,000 |
| Deployments | 500 | 40,000 |
| Jobs | 500 | 40,000 |

As we steered the cluster through various phases of node scaling, application launches, deployment updates and cleanup, we observed the 4XL tier consistently maintained high performance without degradation even when operating close to the tier’s capacity for an extended period. Below graphs show the tier utilization and performance observed during the test.

![Figure 1 - API request concurrency](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/ARC-Blog-1024x369.png)

API request concurrency

![Figure 2 - Pod scheduling rate](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/PSR-Blog-1024x403.png)

Pod scheduling rate

![Figure 3 - Cluster database size](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/ETCD-Blog-1024x325.png)

Cluster database size

![Figure 4 - Metrics in order from left to right, top to bottom - incoming request volume, request latencies, requests with HTTP 429 response (shows graceful throttling) and HTTP 5XX responses (shows minimal degradation).](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/Screenshot-2025-11-26-at-12.36.30-PM-1024x563.png)

Metrics in order from left to right, top to bottom – incoming request volume, request latencies, requests with HTTP 429 response (shows graceful throttling) and HTTP 5XX responses (shows minimal degradation).

## Conclusion

Amazon EKS Provisioned Control Plane delivers predictable, high-performance Kubernetes control plane at scale, enabling you to run demanding workloads with confidence. Provisioning your desired control plane capacity allows you to preemptively eliminate performance variability and ensure consistent behavior across environments. With transparent pricing and clearly defined capabilities including API request concurrency, pod scheduling rates, and cluster database size, you gain full control over your cluster’s performance characteristics. Whether you’re preparing for anticipated high-demand events or running performance-critical workloads, Provisioned Control Plane gives you the tools to satisfy your workload demands. Learn more about Provisioned Control Plane in the EKS [user guide](https://docs.aws.amazon.com/eks/latest/userguide/eks-provisioned-control-plane.html), including how to select the appropriate control plane scaling tier, tier transition times, tier exit restrictions, and more.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/27/shyam2.jpg)**Shyam Jeedigunta** is a Principal Engineer at AWS and helped evolve Amazon EKS architecture over the years to unlock availability, durability, scalability and efficiency wins. He’s spent close to a decade in the open-source Kubernetes, containers and cloud infrastructure space. He focuses on problems around scaling, scheduling, accelerated workloads and databases.

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/27/george.jpg)**George John** is a Senior Product Manager for Amazon Elastic Kubernetes Service (EKS) at AWS, where he drives product strategy and innovation for one of the industry’s leading managed Kubernetes platforms. In his role, George works closely with customers, partners, and the broader cloud-native community to shape the future of container orchestration on AWS. When he is not building products, he loves to explore the Pacific Northwest with his family.

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/27/apoorva.jpg)**Apoorva Kulkarni** is a Principal Specialist Solutions Architect, Containers, AWS, where he focuses on customers who are building modern AI/ML and data platforms on Amazon EKS. In his role, he supports Go-to-Market for AWS containers services and loves collaborating with Open Source communities. Outside of work, Apoorva loves to spend time outdoors in Southern California with this family.