# Amazon EKS Blueprints for CDK: Now supporting Amazon EKS Auto Mode

by Zachary Jacobson and Mikhail Shapirov on 26 NOV 2025 in Amazon Elastic Kubernetes Service, AWS Cloud Development Kit, Technical How-to Permalink  Share

[Amazon EKS Blueprints for CDK](https://aws-quickstart.github.io/cdk-eks-blueprints/) has recently added support for [EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html), a significant enhancement that streamlines Kubernetes management by automatically provisioning infrastructure, choosing optimal compute instances, dynamically scaling resources, continuously optimizing costs, managing core add-ons, patching operating systems, and integrating with Amazon Web Services (AWS) security services.

## What is EKS Blueprints for CDK?

EKS Blueprints for CDK is an open source framework that helps AWS customers bootstrap and configure production-ready [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS) clusters with the [AWS Cloud Development Kit](https://aws.amazon.com/cdk/) (AWS CDK). Customers can describe the desired state of their Amazon EKS environment with worker nodes, auto scaling, networking, and Kubernetes add-ons as an infrastructure as code (IaC) blueprint. These blueprints can be used in pipelines to set up consistent environments across AWS accounts and [AWS Regions.](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) EKS Blueprints is part of the broader initiative by AWS launched in 2022: [Bootstrapping clusters with EKS Blueprints | Amazon Web Services](https://aws.amazon.com/blogs/containers/bootstrapping-clusters-with-eks-blueprints/).

EKS Blueprints can bootstrap your clusters with Amazon EKS add-ons, and many popular open source add-ons, such as ArgoCD, Nginx, Keda, Fluent Bit, FluxCD, and [more](https://awslabs.github.io/cdk-eks-blueprints/addons/). The framework automatically chooses compatible versions for core Amazon EKS add-ons based on your Kubernetes version, eliminating the guesswork of which add-on versions work together. When you upgrade your cluster, the add-on versions automatically update to maintain compatibility, preventing version mismatch errors. EKS Blueprints comes with built-in compatibility handling for your add-ons, so that each add-on you deploy is compatible with your cluster’s configuration. Feedback and support for this framework is available through [GitHub issues](https://github.com/awslabs/cdk-eks-blueprints).

EKS Blueprints provides specialized cluster builders that come pre-configured with the right add-ons and best practices for specific workloads. Whether you’re building observability stacks with Prometheus and Grafana, GPU clusters for machine learning (ML), Windows environments for .NET applications, cost-optimized [AWS Graviton](https://aws.amazon.com/ec2/graviton/) deployments, or AI workloads integrated with [Amazon Bedrock](https://aws.amazon.com/bedrock/), there’s a purpose-built builder ready to go. The latest addition is support for Amazon EKS Auto Mode, which fully automates Kubernetes cluster management for compute, storage, and networking. You can use it to focus on building applications while AWS handles the infrastructure complexity.

## What is EKS Auto Mode?

EKS Auto Mode fully automates Kubernetes cluster management for compute, storage, and networking. You can do the following with EKS Auto Mode:

- AWS automatically provisions and manages your cluster infrastructure with proven best practices.
- Compute instances are chosen and scaled optimally based on workload requirements.
- Essential cluster capabilities are automatically installed, updated, and maintained, including Karpenter, VPC CNI, CoreDNS, and [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/).
- Operating systems are patched and updated automatically with the latest security fixes.
- Infrastructure is hardened according to CIS Level 1 benchmarks with no remote access and immutable root file systems.
- Cluster operations become fully hands-off, removing infrastructure management overhead.
- You can focus on application development instead of cluster administration.
- It remains fully Kubernetes conformant, working with all your existing Kubernetes tools.

EKS Auto Mode instances have a default 14–day maximum lifetime (configurable up to 21 days) and are automatically updated in-place when possible to minimize disruption. AWS manages the full lifecycle while maintaining security through restricted access and automated patching.

You pay for EKS Auto Mode based on the duration and type of [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) instances launched and managed by EKS Auto Mode. EKS Auto Mode charges are billed per-second, with a 1 minute minimum.

## Prerequisites

To use the `eks-blueprints` module, you must have [Node.js](https://nodejs.org/en/) and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed. Here are the [instructions to install these for your platform](https://nodejs.org/en/download).

Create a directory that represents your project (for example `my-blueprints`) and create a new `typescript` CDK project in that directory.

```
npm install -g aws-cdk@2.1029.2 # may require sudo (Ubuntu) depending on configuration
cdk --version # must produce 2.1029.2
mkdir my-blueprints
cd my-blueprints
cdk init app --language typescript
```

[Bootstrap](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html) your environment. This step needs [AWS CloudFormation](https://aws.amazon.com/cloudformation/), [Amazon Elastic Container Registry (Amazon ECR),](https://aws.amazon.com/ecr/) [AWS Systems Manager](https://aws.amazon.com/systems-manager/), [Amazon Simple Storage Service (Amazon S3),](https://aws.amazon.com/s3/) and [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) Admin Permissions. A template can be found in the AWS [CDK Bootstrapping documentation](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping-env.html#bootstrapping-env-permissions).

```
npx cdk bootstrap aws://<AWS_ACCOUNT_ID>/<AWS_REGION>
```

Install the `eks-blueprints` NPM package:

```
npm i @aws-quickstart/eks-blueprints
```

## Implementing EKS Auto Mode with EKS Blueprints for CDK

In this section we go through a few patterns to learn how to create an EKS Auto Mode cluster from scratch. The integration combines EKS Auto Mode benefits with the EKS Blueprints declarative IaC approach. To deploy each of these patterns, copy them to the file `bin/blueprint.ts` in your blueprint directory and run the following command:

```
npx cdk deploy
```

Customers targeting production deployments with these patterns and EKS Blueprints are expected to follow a standard software development life cycle with proper preproduction testing.

### Pattern 1: Basic EKS Auto Mode cluster

```
// Example of deploying a cluster with EKS Auto Mode using EKS Blueprints

import * as cdk from 'aws-cdk-lib';
import * as eks from 'aws-cdk-lib/aws-eks';
import * as blueprints from '@aws-quickstart/eks-blueprints';

const app = new cdk.App();

const account = process.env.CDK_DEFAULT_ACCOUNT;
const region = process.env.CDK_DEFAULT_REGION;

const options: Partial<blueprints.AutomodeClusterProviderProps> = {
version: eks.KubernetesVersion.of("1.33"),
nodePools: ["system", "general-purpose"],
};

blueprints.AutomodeBuilder.builder(options)
.account(account)
.region(region)
.addOns(new blueprints.addons.ArgoCDAddOn())
.addALBIngressClass()
.addEBSStorageClass()
.build(app, 'eks-auto-mode-blueprint');
```

This pattern creates a production-ready EKS Auto Mode cluster with ArgoCD for GitOps, and a preconfigured AWS Load Balancer Controller ingress class and [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/) CSI storage class. That’s everything you need to start deploying applications immediately.

### Pattern 2: EKS Auto Mode cluster with custom ARM NodePool for workloads

```
// Example of deploying a cluster with EKS Auto Mode using EKS Blueprints

import * as cdk from 'aws-cdk-lib';
import * as eks from 'aws-cdk-lib/aws-eks';
import * as blueprints from '@aws-quickstart/eks-blueprints';

const app = new cdk.App();

const account = process.env.CDK_DEFAULT_ACCOUNT;
const region = process.env.CDK_DEFAULT_REGION;

const armNodePool: blueprints.NodePoolV1Spec = {
labels: { type: "arm-blueprint" },
requirements: [
{ key: "eks.amazonaws.com/instance-category", operator: "In", values: ["c", "m", "r"] },
{ key: "eks.amazonaws.com/instance-cpu", operator: "In", values: ["2", "4", "8", "16"] },
{ key: "kubernetes.io/arch", operator: "In", values: ["arm64"] },
{ key: "karpenter.sh/capacity-type", operator: "In", values: ["on-demand"] },
],
expireAfter: "24h",
disruption: { consolidationPolicy: "WhenEmpty", consolidateAfter: "1m" }
};

const options: Partial<blueprints.AutomodeClusterProviderProps> = {
version: eks.KubernetesVersion.of("1.33"),
nodePools: ["system"],
extraNodePools: {
["arm-pool"]: armNodePool
}
};

blueprints.AutomodeBuilder.builder(options)
.account(account)
.region(region)
.addOns(new blueprints.addons.ArgoCDAddOn())
.addALBIngressClass()
.addEBSStorageClass()
.build(app, 'eks-auto-mode-blueprint');
```

This pattern creates an EKS Auto Mode cluster with an added ARM-based Graviton NodePool, delivering up to 40% better price-performance compared to x86 instances while automatically handling ARM-compatible configurations.

### Pattern 3: EKS Auto Mode cluster with custom AI Accelerator NodePool for AI/ML workloads

```
import * as cdk from 'aws-cdk-lib';
import * as eks from 'aws-cdk-lib/aws-eks';
import * as blueprints from '@aws-quickstart/eks-blueprints';

const app = new cdk.App();

const account = process.env.CDK_DEFAULT_ACCOUNT;
const region = process.env.CDK_DEFAULT_REGION;

const inf1NodePoolSpec: blueprints.NodePoolV1Spec = {
taints: [
{
key: "aws.amazon.com/neuron",
value: "Exists",
effect: "NoSchedule"
},
],
startupTaints: [
{
key: "node.kubernetes.io/not-ready",
effect: "NoSchedule"
}
],
requirements: [
{ key: "karpenter.sh/capacity-type", operator: "In", values: ["on-demand"] },
{
key: "node.kubernetes.io/instance-type", operator: "In", values: [
"inf1.xlarge",    // 1 Inferentia Chip, 4 vCPUs, 8 GB
"inf1.2xlarge",   // 1 Inferentia Chip, 8 vCPUs, 16 GB
],
}
],
expireAfter: "24h",
disruption: {
consolidationPolicy: "WhenEmpty",
consolidateAfter: "30s"
},
limits: {
cpu: 320,
memory: "1280Gi",
"aws.amazon.com/neuron": 8
},
weight: 100
};

const options: Partial<blueprints.AutomodeClusterProviderProps> = {
version: eks.KubernetesVersion.of("1.33"),
extraNodePools: {
['inferentia']: inf1NodePoolSpec
}
};

const addons = [
new blueprints.ArgoCDAddOn()
];

blueprints.AutomodeBuilder.builder(options)
.account(account)
.region(region)
.addOns(...addons)
.addALBIngressClass()
.addEBSStorageClass()
.build(app, 'eks-auto-mode-blueprint');
```

This pattern creates an EKS Auto Mode cluster with an added [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/) NodePool. This leads to immediate deployment of AI/ML workloads without manual driver configuration.

We have more configurable [EKS Blueprint patterns](https://github.com/aws-samples/cdk-eks-blueprints-patterns), including multi-cluster pipelines and multi-Region constructs, and configurable [Observability EKS Blueprint patterns](https://github.com/aws-observability/cdk-aws-observability-accelerator). Feel free to fork these repositories, create new patterns, and contribute back to the EKS Blueprints community.

## Cleaning up

To destroy your cluster, run the following command from your blueprint directory:

```
npx cdk destroy
```

## Benefits of using EKS Auto Mode with EKS Blueprints

When implementing EKS Auto Mode through EKS Blueprints, you gain several advantages:

1. **Streamlined IaC**: Define EKS Auto Mode clusters with the same declarative approach that you use for existing, non-EKS Auto Mode clusters.
2. **Consistent management**: Apply the same add-ons, team structures, and configurations to EKS Auto Mode clusters.
3. **Maximum automation**: Combine the EKS Blueprints automated add-on management with the EKS Auto Mode fully managed infrastructure.
4. **Operational consistency**: Use the same deployment pipelines and processes for all of your clusters.
5. **Focus on applications**: AWS can handle both cluster infrastructure (EKS Auto Mode) and add-on compatibility (EKS Blueprints).

## Conclusion

Amazon EKS Blueprints now supports EKS Auto Mode, so that developers can deploy fully managed clusters with minimal configuration. This integration maintains the framework’s structured approach while removing the operational overhead of node group management, networking setup, and cluster scaling decisions. Teams can now focus on application development rather than infrastructure management, while still benefiting from the EKS Blueprints proven patterns and add-on environment.

We encourage you to explore EKS Auto Mode with EKS Blueprints for CDK and experience the benefits of hands-off cluster operations and streamlined application development in your Kubernetes environments.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/zjacobso.jpg) **Zachary Jacobson** is a Partner Solutions Architect with AWS. He focuses on Containers, Agentic AI, and Platform Engineering for partners at scale. He is also a software engineer and OSS contributor.

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/shapirov.jpg)**Mikhail Shapirov** is a Pr. Partner Solutions Architect with AWS. He’s leading solutions architecture initiatives for our strategic partners focusing on Containers, App Modernization, Generative AI and other domains. He is also a software engineer and OSS contributor.