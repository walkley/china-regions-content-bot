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

## [Containers](https://aws.amazon.com/blogs/containers/)

# Accelerating application development with the Amazon EKS MCP server

by Aditya Ramakrishnan on 29 MAY 2025 in [Amazon Elastic Kubernetes Service](https://aws.amazon.com/blogs/containers/category/compute/amazon-kubernetes-service/ "View all posts in Amazon Elastic Kubernetes Service"), [Amazon Q Developer](https://aws.amazon.com/blogs/containers/category/amazon-q/amazon-q-developer/ "View all posts in Amazon Q Developer"), [Announcements](https://aws.amazon.com/blogs/containers/category/post-types/announcements/ "View all posts in Announcements"), [Open Source](https://aws.amazon.com/blogs/containers/category/open-source/ "View all posts in Open Source") [Permalink](https://aws.amazon.com/blogs/containers/accelerating-application-development-with-the-amazon-eks-model-context-protocol-server/) Share

*This blog post was jointly authored by Niall Thomson, Principal Solutions Architect – Containers, Carlos Santana, Solutions Architect – Containers and George John, Senior Product Manager – Amazon EKS*

## Introduction

Today, we’re excited to announce the launch of the open source [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server for [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/). This new capability enables artificial intelligence (AI) code assistants such as [Amazon Q Developer CLI,](https://github.com/aws/amazon-q-developer-cli) [Cline,](https://cline.bot/) and [Cursor](https://www.cursor.com/) to seamlessly interact with your EKS clusters in a standardized way. The MCP server provides AI assistants with contextual data and enables them to manage EKS and Kubernetes resources. As a result, developers can now receive tailored guidance throughout the entire development lifecycle, streamlining and accelerating their application development process.

Large Language Models (LLMs) have revolutionized the way developers write code, and their capabilities are being further enhanced through innovative solutions like the Model Context Protocol (MCP) server. While LLMs excel at providing general coding assistance based on their training data, the MCP server extends their capabilities by enabling real-time access to external tools and data sources, particularly valuable in complex environments like Kubernetes. As an open standard, MCP creates a standardized interface that empowers LLMs to tap into current, contextual information, making them even more powerful and precise in supporting specific application development use cases. This synergy between LLMs and MCP represents a significant advancement in AI-assisted development.

The EKS MCP server provides AI code assistants with resource management tools and up-to-date, contextual information about your Amazon EKS clusters. This allows code assistants to provide more accurate, tailored guidance throughout the application lifecycle, from initial setup through production optimization and troubleshooting. Integrating the EKS MCP server into your development workflow can provide you with significant enhancements across various phases of application development. During the getting started phase, it offers guided cluster creation with all necessary prerequisites automatically created and best practice applied. In the development phase, it reduces the EKS and Kubernetes learning curve by providing high-level workflows for application deployment and cluster management, as well as generating EKS-aware code and manifests. For debugging and troubleshooting, the EKS MCP server accelerates issue resolution by offering troubleshooting aids and access to a knowledge base. These capabilities are now accessible through natural language interactions within an AI code assistant, transforming how developers interact with EKS and making complex Kubernetes operations more intuitive and efficient.

## Features

The EKS MCP server provides several MCP tools, each of which can be invoked by AI assistants to interact with external systems such as APIs or knowledge bases.

The tools provided by the EKS MCP server can be broken down into three categories:

1) **Kubernetes resource management:** Interact and manage Kubernetes resources in an EKS cluster without relying on Kubernetes commands. These tools include seamless authentication for EKS clusters, allowing efficient operations across multiple clusters without needing to manage a kubeconfig file.

* `list_k8s_resources`– List Kubernetes resources of a specific kind
* `list_api_versions`– List all available Kubernetes API versions
* `manage_k8s_resource`– Create, update, or delete an individual Kubernetes resource
* `apply_yaml`– Apply YAML objects
* `get_k8s_events`– Get events related to a specific Kubernetes resource
* `get_pod_logs`– Get logs for a specific pod

2) **EKS cluster management:** Conveniently create and manage EKS clusters powered by [EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html) through [AWS CloudFormation](https://aws.amazon.com/cloudformation/).

* `manage_eks_stacks`– Generate, deploy, and delete CloudFormation stacks for EKS clusters

3) **Troubleshooting:** Streamlines issue resolution by providing comprehensive telemetry data, such as logs and metrics. It enhances LLM capabilities by combining real-time cluster insights with curated troubleshooting playbooks for common failure scenarios, enabling faster and more accurate problem diagnosis and resolution.

* `search_eks_troubleshoot_guide`– Search the Amazon EKS knowledge base for troubleshooting information
* `get_cloudwatch_logs`– Retrieve logs from [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) for a pod or an EKS cluster control plane
* `get_cloudwatch_metrics`– Retrieve metrics from CloudWatch for a container, pod, node, or cluster

Additional tools are included, check out the [documentation](https://awslabs.github.io/mcp/servers/eks-mcp-server/) for more details.

## Walkthrough

To demonstrate the capabilities of the EKS MCP server, the following sections walk through example scenarios.

### Deploying a workload

In this section we demonstrate how the EKS MCP server can accelerate getting a workload running on Amazon EKS faster. For this you create a new application and package it as a container, ready to be deployed to Amazon EKS. This involves coding, thus you can use [Cline](https://cline.bot/), an autonomous agent for VS Code.

Follow the EKS MCP Server documentation [here](https://awslabs.github.io/mcp/servers/eks-mcp-server/) to install the pre-requisites including IAM permissions. To configure Cline to use the EKS MCP server following the Cline documentation [here](https://docs.cline.bot/mcp/configuring-mcp-servers#editing-mcp-settings-files). Your `cline_mcp_settings.json` file should resemble the following example.

If the installation is successful, then you should see the EKS MCP server in list of MCP servers installed in Cline as shown in the following figure.

![Figure 1: Configuring the EKS MCP server in Cline](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/05/29/EKS-MCP-1-New.png)

Figure 1: Configuring the EKS MCP server in Cline

![Figure 2: MCP successfully installed in Cline](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/05/28/EKS-MCP-2.jpg)

Figure 2: MCP successfully installed in Cline

You need an application to deploy to Amazon EKS, and for that you rely on Cline and the LLM model that it’s been configured to use. You don’t need to rely on the EKS MCP server yet. Enter the following prompt into the a new Cline task:

```
Bootstrap the current directory with a Node.js application which uses Express to provide
an API. The application should provide a single path “/demo” which responds with
the text “Welcome to the Amazon EKS MCP server”. It should also provide a health
endpoint at “/health” which will be used to perform health checks of the
application.

Create a Dockerfile which can be used to package this application as a container.
Use Node.js version 22, which is the current Long-Term Support version. Use
"docker build" to build the container image after the file is created and tag it
with "eks-mcp-demo". Once the container is built run it with "docker run" and test
the endpoints. Make sure the container is built as a multi-architecture image
supporting both x86_64 and ARM64.

Push this image to an Amazon ECR repository called "eks-mcp-demo" in the AWS account
Provide the image URL once this is complete.
```

We can break down this prompt:

1. You’re asking the assistant to build a Node.js application that uses the popular Express framework, with some starter endpoints you can access.
2. You need a Dockerfile, so you ask the assistant to create one.
3. Next you ask the assistant to build the container image, making sure that it’s built for multiple CPU architectures. It also quickly tests the image locally to make sure that its basic functions are correct.
4. Finally you ask the assistant to push the container image to [Amazon Elastic Container Registry (Amazon )](https://aws.amazon.com/ecr/) so that it can be deployed to Amazon EKS.

The application repository produced would look something like the following:

![Figure 3: Generated application file structure](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/05/28/EKS-MCP-3.jpg)

Figure 3: Generated application file structure

The container image has been built and pushed to Amazon ECR, as shown in the following figure:

![Figure 4: Application bootstrap task completion in Cline](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/05/28/EKS-MCP-4-2.jpg)

Figure 4: Application bootstrap task completion in Cline

Now you ask the assistant to deploy the application to Amazon EKS:

```
Deploy this application to Amazon EKS. Create a new cluster for the application. I
want to test the application over the public Internet.
```

Under the hood, the code assistant uses the EKS MCP server’s `manage_eks_stacks` tool to automate the entire cluster provisioning process, as shown in the following figure. It needs zero input from the user, and automates creation of all cluster prerequisites, such as VPC, subnets, and [AWS Identity and Access Management](https://aws.amazon.com/iam/?trk=46f27e04-0cd6-46e2-b3da-7fc43e7d0b9c&sc_channel=ps&ef_id=EAIaIQobChMI0bHxzarFjQMVGtvCBB354iolEAAYASAAEgKddfD_BwE:G:s&s_kwcid=AL!4422!3!747067298857!e!!g!!amazon%20iam!22461653254!177842081963&gad_campaignid=22461653254&gbraid=0AAAAADjHtp9u8_nx6m0SBR8hqS3Zgm-rT&gclid=EAIaIQobChMI0bHxzarFjQMVGtvCBB354iolEAAYASAAEgKddfD_BwE) roles. The EKS MCP server tool not only streamlines infrastructure setup but also applies Amazon EKS recommendations on the cluster automatically, such as enablement of EKS Auto Mode for streamlined cluster management.

![Figure 5: Cline invoking EKS MCP stack management tool](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/05/29/EKS-MCP-5-New-1-e1748485241158.png)

Figure 5: Cline invoking EKS MCP stack management tool

The cluster creation takes several minutes, after which the assistant generates and deploys Kubernetes manifests using EKS MCP server’s `apply_yaml` tool, as shown in the following figure:

![Figure 6: Cline invoking EKS MCP tool to apply YAML manifest](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/05/28/EKS-MCP-6.jpg)

Figure 6: Cline invoking EKS MCP tool to apply YAML manifest

When the manifests are deployed, the assistant can use EKS MCP server tools such as `list_k8s_resources` and `manage_k8s_resources` to check the status of the Pods, as shown in the following figure.

![Figure 7: Cline invoking EKS MCP tool to list Kubernetes resources](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/05/28/EKS-MCP-7.jpg)

Figure 7: Cline invoking EKS MCP tool to list Kubernetes resources

Finally, the assistant retrieves the application URL to confirm that it’s deployed and running, as shown in the following figure.

![Figure 8: Cline successfully deployed the application to Amazon EKS](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/05/28/EKS-MCP-8.jpg)

Figure 8: Cline successfully deployed the application to Amazon EKS

Although we used docker in this walkthrough, we have also developed the [Finch MCP Server](https://awslabs.github.io/mcp/servers/finch-mcp-server/) to support our users’ diverse container management needs. Finch offers a secure, standardized approach to container operations, integrating seamlessly with AWS services while maintaining robust security controls. It reflects our commitment to providing flexible, enterprise-grade solutions that meet varying user requirements.

## Troubleshooting

Another area where the EKS MCP server can provide valuable context to AI assistants is identifying and remediating issues. To demonstrate the portability of MCP servers, switch to using Amazon Q Developer CLI, which supports MCP servers for tools and prompts. After [installing](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html) [Q Developer CLI,](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html) the EKS MCP can be added by [configuring](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-mcp-configuration.html) the `mcp.json` file

```
{
  "mcpServers": {
    "awslabs.eks-mcp-server": {
      "command": "uvx",
      "args": [
        "awslabs.eks-mcp-server",
        "--allow-write",
        "--allow-sensitive-data-access"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "autoApprove": [],
      "disabled": false
    }
  }
}
```

```
When the CLI loads, you can use the /tools command to see which tools have been added:
```

```
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
awslabseks_mcp_server (MCP):
- awslabseks_mcp_server___add_inline_policy                * not trusted
- awslabseks_mcp_server___apply_yaml                       * not trusted
- awslabseks_mcp_server___generate_app_manifest            * not trusted
- awslabseks_mcp_server___get_cloudwatch_logs              * not trusted
- awslabseks_mcp_server___get_cloudwatch_metrics           * not trusted
- awslabseks_mcp_server___get_k8s_events                   * not trusted
- awslabseks_mcp_server___get_pod_logs                     * not trusted
- awslabseks_mcp_server___get_policies_for_role            * not trusted
- awslabseks_mcp_server___list_api_versions                * not trusted
- awslabseks_mcp_server___list_k8s_resources               * not trusted
- awslabseks_mcp_server___manage_eks_stacks                * not trusted
- awslabseks_mcp_server___manage_k8s_resource              * not trusted
- awslabseks_mcp_server___search_eks_troubleshoot_guide    * not trusted
```

Now let’s take a look at two scenarios where the EKS MCP can support the AI assistant.

### Troubleshooting pods

In this situation there are two pods that are failing to start:

```
NAMESPACE      NAME                               READY   STATUS             RESTARTS   AGE
default        nginx-deployment-6ccc9899c-nhbrf   0/1     ImagePullBackOff   0          17s
default        nginx-deployment-6ccc9899c-wq5ls   0/1     ImagePullBackOff   0          17s
```

Ask the AI assistant to troubleshoot and try to directly fix the issue:

```
The Pods in the nginx-deployment Deployment are not starting. Diagnose and remediate
the issue, apply any fixes directly and not via a manifest. Once the deployment is
healthy provide a brief summary of the issues identified and the fixes applied.
```

The assistant can use the EKS MCP server for several parts of this task. For example, it might retrieve logs and events with the EKS MCP server’s `get_pod_logs` and `get_k8s_events` respectively, as shown in the following figure:

![Figure 9: Amazon Q CLI invoking the EKS MCP tool to get Kubernetes events](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/05/28/EKS-MCP-9.jpg)

Figure 9: Amazon Q CLI invoking the EKS MCP tool to get Kubernetes events

It can remediate the issues directly through the EKS MCP server’s `manage_k8s_resources` to update the Deployment resource, as shown in the following figure:

![Figure 10: Amazon Q CLI invoking the EKS MCP tool to update a Kubernetes resource](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/05/28/EKS-MCP-10.jpg)

Figure 10: Amazon Q CLI invoking the EKS MCP tool to update a Kubernetes resource

Finally, you get a summary of the multiple issues that were identified and fixed, as shown in the following figure:

![Figure 11: Amazon Q CLI summarizing the troubleshooting issues and remediations](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/05/28/EKS-MCP-11.jpg)

Figure 11: Amazon Q CLI summarizing the troubleshooting issues and remediations

### Troubleshooting infrastructure

When users troubleshoot Amazon EKS environments, they must consider not only the Kubernetes resources but also the AWS resources that are used to create the clusters, as well as the related resources such as VPC networking and IAM.

In this example we start with a similar situation as the previous scenario, but in this case the pods are in a `Pending` state, indicating they can’t be scheduled to an EKS worker node:

```
NAMESPACE   NAME                                READY   STATUS    RESTARTS   AGE
default     nginx-deployment-5559f849f6-ccg6l   0/1     Pending   0          4m
default     nginx-deployment-5559f849f6-w9bs6   0/1     Pending   0          4m
```

We can ask the AI assistant to help figure out the issue:

```
The Pods in the nginx-deployment Deployment are not starting. Diagnose the issue and
suggest how to fix it.
```

The assistant likely takes similar action to the previous scenario to begin to diagnose the issue, checking the status of the Deployment and Pods, as well as retrieving Kubernetes events. However, in this case it can also use the EKS MCP server’s `search_eks_troubleshoot_guide` knowledge base tool to gain specialized troubleshooting knowledge related to Amazon EKS, as shown in the following figure:

![Figure 12: Amazon Q CLI invoking the EKS MCP tool to search the Amazon EKS knowledge base](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/05/28/EKS-MCP-12.jpg)

Figure 12: Amazon Q CLI invoking the EKS MCP tool to search the Amazon EKS knowledge base

The Amazon EKS troubleshooting tools responds with targeted advice related to the assistant’s query, along with related reference documentation that can be used for further research. For example:

```
{
  "answer": "This can occur if the compute configuration associated with the EKS Auto Mode cluster does not include either a general purpose or system node group, or if required IAM permissions for Auto Mode have been deleted from the associated role, or if the trust policy for the role is incorrect.",
  "symptoms": [
    "Pod remains in 'Pending' state for an extended period",
    "kubectl describe pod shows '0/0 nodes are available' or similar scheduling errors",
    "No nodes are listed in 'kubectl get nodes' output for the EKS Auto Mode cluster",
    "Events indicate scheduling failures due to lack of available nodes"
  ],
  "references": [
    "https://docs.aws.amazon.com/eks/latest/userguide/auto-cluster-iam-role.html"
  ]
}
```

This documentation provides the assistant with the context it needs to identify the issue and a solution. In this case it correctly identified an issue with the IAM role used to provide permissions to the EKS cluster, as shown in the following figure:

![Figure 13: Amazon Q CLI summarizing the issue that was identified and remediation steps ](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/05/28/EKS-MCP-13.jpg)

Figure 13: Amazon Q CLI summarizing the issue that was identified and remediation steps

# Conclusion

The open source MCP server for Amazon EKS provides users with an exciting new way to interact with their Kubernetes environments.

This MCP server allows you to do the following:

* Deploy and manage Kubernetes resources with AI-assisted guidance
* Troubleshoot EKS cluster issues using conversational AI

As organizations continue to adopt containerized architectures, tools that streamline management and reduce cognitive load become increasingly valuable. The EKS MCP server demonstrates our commitment to making Kubernetes more accessible while maintaining the power and flexibility that Amazon EKS users expect.

At AWS, our roadmap is deeply influenced by customer feedback. We encourage you to share your experiences with the EKS MCP server: whether it’s suggesting new features, reporting challenges, or highlighting workflows where AI assistance could be more impactful. Your insights into daily development patterns, pain points, and areas where you need enhanced automation or guidance are invaluable in shaping the future capabilities of this tool. You can provide feedback in the [AWSLabs MCP Servers Github repository](https://github.com/awslabs/mcp) by creating a new issue.

Get started today by visiting the [EKS MCP Server documentation](https://awslabs.github.io/mcp/servers/eks-mcp-server/) and join us in shaping the future of AI-assisted Kubernetes management.

TAGS: [Amazon ECR](https://aws.amazon.com/blogs/containers/tag/amazon-ecr/), [Amazon EKS](https://aws.amazon.com/blogs/containers/tag/amazon-eks/), [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/blogs/containers/tag/amazon-elastic-kubernetes-service-amazon-eks/), [open source](https://aws.amazon.com/blogs/containers/tag/open-source/)

### Resources

* [Amazon Container Services](https://aws.amazon.com/containers?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-resources)
* [AWS Fargate](https://aws.amazon.com/fargate/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-resources)
* [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-resources)
* [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-resources)
* [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-resources)
* [AWS Cloud Map](https://aws.amazon.com/cloud-map?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [RSS Feed](http://feeds.feedburner.com/AmazonWebServicesBlog)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=containers-social)

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