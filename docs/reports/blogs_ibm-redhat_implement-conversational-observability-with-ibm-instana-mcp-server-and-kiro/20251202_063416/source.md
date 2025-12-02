# Implement Conversational Observability with IBM Instana MCP Server and Kiro

by Maximilian Schellhorn, Jyotirmay Sharma, Phani Pawan Padmanabharao, Riya Kumari, Sunjit Tara, and Thanos Matzanas on 26 NOV 2025 in IBM & Red Hat on AWS Permalink  Comments   Share

Modern observability tools generate substantial data about application performance, infrastructure health, and system behavior. However, accessing this data typically requires navigating dashboards, constructing API queries, or switching between multiple tools. [IBM Instana Observability](https://www.ibm.com/products/instana) (Instana) MCP server provides conversational AI interactions that transform observability workflows into natural language conversations.

The [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP) is an open-source standard that enables connecting AI agents with external tools and data sources via standardized interfaces. By integrating the [Instana MCP server](https://www.ibm.com/docs/en/instana-observability/1.0.309?topic=apis-mcp-server-instana) with [Kiro CLI](https://kiro.dev/cli/) and [Kiro IDE](https://kiro.dev/), development teams can query observability data, troubleshoot issues, and manage alerts directly from their terminal using natural language.

In this blog, you’ll learn how to get started and configure the Instana MCP server to work with Kiro CLI and IDE by subscribing to [Instana’s free MCP Server listing on AWS Marketplace.](https://aws.amazon.com/marketplace/pp/prodview-q2hjdyja2mg5o) You will also learn about the architecture and implementation steps required to establish AI-powered observability for your applications and infrastructure.

## Instana MCP Server

The Instana MCP server is built as a unified layer that exposes Instana’s full REST API capabilities through MCP. It translates conversational queries into precise API calls and formats responses for AI assistants. This approach makes enterprise-grade observability accessible through questions, reducing the need to memorize API endpoints or construct requests.

As an [open-source project on GitHub](https://github.com/instana/mcp-instana), the Instana MCP server encourages community contributions and customizations. Teams can extend functionality, add custom tools, and adapt the server to their organizational needs.

The Instana MCP Server offers specialized tools that provide access to Instana’s API endpoints for metrics retrieval, resource discovery, alert management, infrastructure analysis, and event monitoring. These tools are organized into logical categories and can be selectively enabled, combined, or filtered based on your use case:

- **Application Performance Monitoring:** Access real-time and historical performance data for applications, endpoints, services, and traces
- **Infrastructure Monitoring:** Monitor hosts, analyze snapshots, manage software inventory, and explore infrastructure topology
- **Alert Configuration**: Manage the complete lifecycle of Application smart alert configurations, including creation, updates, and baseline management
- **Infrastructure Catalog**: Explore available metrics, plugins, and monitoring capabilities across your stack

The MCP interface supports query options including time ranges, tags, entity identifiers, metric thresholds, and environment scopes, allowing AI assistants and developer tools to retrieve the data they need from Instana in real time.

## Instana MCP Server Architecture Overview

The following diagram (Figure 1) shows how the Instana MCP server integrates with Kiro and Instana, illustrating the data flow from client interfaces through the MCP server to the Instana backend.

![Architecture diagram showing data flow from Kiro CLI and Kiro IDE through Instana MCP Server via HTTP or stdio transport to Instana Backend on AWS.](https://d2908q01vomqb2.cloudfront.net/c097638f92de80ba8d6c696b26e6e601a5f61eb7/2025/11/26/Figure1-ReferenceArchitectureInstanaMCPServerKiroInstanaBackend-1024x369.png)

Figure 1. Reference architecture showing Instana MCP server integration with Kiro CLI, Kiro IDE, and Instana Backend.

The architecture consists of these main components:

- **Kiro CLI / Kiro IDE:** Serve as conversational interfaces where users issue natural-language queries, with both clients communicate through the MCP standard to request data from Instana
- **Instana MCP Server**: Acts as the translation layer that converts conversational queries from Kiro into Instana REST API calls and formats responses for AI consumption, receiving requests via MCP protocol and retrieving observability data from the Instana Backend
- **Transport Layer**: Supports both stdio (standard input/output) and HTTP transport modes for compatibility in different deployment scenarios
- **Instana Backend**: Serves as the central storage and analytics system for your observability data, available as a [fully managed SaaS](https://aws.amazon.com/marketplace/pp/prodview-tbam5h35sumqg?sr=0-3&ref_=beagle&applicationId=AWSMPContessa) on AWS or [Self-Hosted](https://aws.amazon.com/marketplace/pp/prodview-mbw42d6cjzi7e) deployment in your own AWS account

## Using Instana MCP Server with Kiro

With the Instana MCP server and Kiro, you can:

- Query application performance metrics using natural language instead of constructing REST API calls.
- Investigate infrastructure issues directly from your terminal without switching contexts.
- Access distributed traces, logs, and metrics through conversational interactions.
- Manage alert configurations and analyze system behavior through queries.
- Accelerate troubleshooting by asking questions about alerts and events.
- Interact via Kiro CLI in the terminal or Kiro IDE, both using the same Instana MCP Server backend.

## Implementation walkthrough

This section walks you through subscribing to the Instana MCP Server on AWS Marketplace, installing and configuring the server locally using Docker, and integrating it with Kiro CLI and Kiro IDE for conversational observability interactions.

### Prerequisites

Before you begin, ensure you have the following:

- An [AWS account](https://aws.amazon.com/resources/create-account/) with credentials configured
- An active subscription to IBM Instana Observability. You can start with an [Instana free trial](https://aws.amazon.com/marketplace/pp/prodview-tbam5h35sumqg?sr=0-3&ref_=beagle&applicationId=AWSMPContessa) from AWS Marketplace
- [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) permissions for [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) (Amazon ECR) operations
- An [Instana API token](https://www.ibm.com/docs/en/instana-observability/1.0.309?topic=working-user-interface), generated from your Instana tenant dashboard after signing in
- Access to your [Instana tenant URL](https://www.ibm.com/docs/en/instana-observability/1.0.304?topic=working-user-interface) (for example, *https://your-instance.instana.io*)
- Basic familiarity with [Instana’s REST APIs](https://www.ibm.com/docs/en/instana-observability/1.0.309?topic=apis-instana-rest-api)

The following tools installed and configured on your workstation:

- [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) (AWS CLI) version 2
- [Kiro CLI](https://kiro.dev/cli/) and [Kiro IDE](https://kiro.dev/downloads/) installed and configured on your workstation
- Python 3.10 or later and [Docker](https://docs.docker.com/engine/install/)

### Cost Considerations

The IBM Instana Observability MCP Server container image has no contract cost. You will incur costs for your Instana Observability SaaS subscription, based on the plan you select on AWS Marketplace after the free trial period ends.

If you deploy the MCP Server to AWS compute services such as [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2), [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS) or [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS), standard AWS service charges apply. Kiro pricing depends on usage. For current pricing information, see [Kiro Pricing](https://kiro.dev/pricing/).

This walkthrough demonstrates local deployment using Docker on your workstation, which does not incur AWS compute costs.

### Deployment options

This walkthrough demonstrates local deployment of the Instana MCP Server using Docker on your workstation. This approach is designed for development and individual use. You can also deploy the MCP Server container on Amazon ECS, Amazon EKS, or Amazon EC2 for team use or production scenarios.

When deploying on AWS, consider these security practices. Use [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) or [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) to store and retrieve Instana API tokens instead of environment variables. Enable encryption at rest using [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) customer managed keys for secrets stored in Secrets Manager or Parameter Store. Rotate API tokens regularly according to your organization’s security policies. Configure [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) to restrict network access to the MCP Server endpoint based on source IP addresses or security group IDs.

Use [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) roles for task execution to grant the container only the permissions it needs to access AWS services. Enable encryption in transit by configuring TLS/SSL certificates for the MCP Server HTTP endpoint. Use [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) to capture and analyze MCP Server access logs and application logs for security monitoring and troubleshooting.

### Subscribe to Instana Observability MCP Server on AWS Marketplace

Before you can use the Instana MCP Server, you must subscribe to it on AWS Marketplace.

1. Navigate to the [Instana Observability MCP Server listing on the AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-q2hjdyja2mg5o) and choose **View Purchase Options**.
2. On the *Subscribe to* **IBM Instana Observability MCP Server** page, review the pricing information and product terms, and choose **Subscribe**.
3. After your subscription request completes, choose **Launch your software** to access the deployment instructions. The following image shows the commands to authenticate to Amazon ECR, pull the Instana MCP Server image, and run the container (Figure 2).

![AWS Marketplace page showing ECR authentication command, docker pull command, and docker run command for Instana MCP Server](https://d2908q01vomqb2.cloudfront.net/c097638f92de80ba8d6c696b26e6e601a5f61eb7/2025/11/26/Figure2-InstanaMCPDeploymentInstructionsAWSMarketplace-1024x378.png)

Figure 2. Instana MCP deployment instructions from AWS Marketplace.

Note the Amazon ECR repository URL and image tag from these instructions. You will use them in the next step to deploy the Instana MCP Server.

### Install Instana MCP Server

After subscribing, install the MCP Server locally using Docker.

4. Run the following commands from your workstation to download and launch the Instana MCP server using the details obtained in step 3:

```
$ aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <<aws-marketplace-repo>>.dkr.ecr.us-east-1.amazonaws.com

$ docker pull <<aws-marketplace-repo>>.dkr.ecr.us-east-1.amazonaws.com/ibm-software/mcp-instana-server:v0.3.1

$ docker run -d -p 8080:8080 --name mcp-instana <<aws-marketplace-repo>>.dkr.ecr.us-east-1.amazonaws.com/ibm-software/mcp-instana-server:v0.3.1
```

5. To verify the server is running, run:

```
$ docker ps
```

The output displays the container ID, image name, creation time, status, and port mappings for the running Instana MCP server container (Figure 3):

![Terminal output showing docker ps command results with Instana MCP server container running on port 8080.](https://d2908q01vomqb2.cloudfront.net/c097638f92de80ba8d6c696b26e6e601a5f61eb7/2025/11/26/Figure3-DockerContainerStatusOutputInstanaMCPServer-1024x78.png)

Figure 3. Docker container status output for Instana MCP Server.

This walkthrough uses *streamable HTTP mode* for connecting to the Instana MCP server which:

- Uses HTTP headers for authentication (no environment variables needed)
- Supports different credentials per request
- Better suited for shared environments
- Default port: 8080
- Endpoint: http://0.0.0.0:8080/mcp/

The Instana MCP Server also supports stdio mode, which enables direct communication over standard input/output. In stdio mode uses environment variables for authentication and is designed for MCP clients that require stdin/stdout transport. For stdio configuration steps, see the [Instana MCP Server GitHub repository](https://github.com/instana/mcp-instana?tab=readme-ov-file#starting-in-stdio-mode)

### Using Instana MCP server with Kiro IDE

After deploying the Instana MCP server, configure it in Kiro IDE.

6. Launch the Kiro IDE application. If this is your first time using Kiro, you will be prompted to sign in and complete the initial setup.
7. From the Getting started page, choose **Open a project** to select your project directory. This will be the workspace where you’ll use Instana via MCP.
8. Choose the **Kiro icon** in the activity sidebar to open the Kiro settings panel.
9. In the MCP SERVERS section, choose **Enable MCP** (if this is your first time configuring MCP) or choose the pencil icon to open the MCP configuration. The following image shows the Kiro settings panel with the MCP SERVERS section (Figure 4).

![Kiro IDE settings interface with MCP SERVERS section and Enable MCP button highlighted.](https://d2908q01vomqb2.cloudfront.net/c097638f92de80ba8d6c696b26e6e601a5f61eb7/2025/11/26/Figure4-KiroSettingsPanelShowingMCPServerConfigurationOptions-1024x552.png)

Figure 4. Kiro settings panel showing MCP server configuration options.

10. Define your Instana MCP server by adding and saving the following entry in the mcp.json configuration file:

```
{
"mcpServers": {
"instana-mcp-server": {
"url": "http://<replace-with-your-instana-mcp-host>:8080/mcp",
"headers": {
"INSTANA-BASE-URL":"https://<replace-with-your-instana-tenant>.instana.io",
"INSTANA-API-TOKEN":"<replace-with-your-instana-api-token>"
},
"disabled": false
}
}
}
```

11. After saving the configuration, the MCP server and its available tools appear under **MCP SERVERS** with a **Connected** status. The following image shows the successfully connected Instana MCP server in Kiro (Figure 5).

![Kiro IDE interface showing connected Instana MCP server with list of available tools in the MCP SERVERS panel.](https://d2908q01vomqb2.cloudfront.net/c097638f92de80ba8d6c696b26e6e601a5f61eb7/2025/11/26/Figure5-ConnectedInstanaMCPServerDisplayedKiroIDE-1-1024x550.png)

Figure 5. Connected Instana MCP server displayed in Kiro IDE.

12. From the Kiro chat panel, you can ask questions such as: *Get the list of Instana applications from the Instana MCP server*. Kiro uses the available MCP tools to retrieve information about the applications monitored in your environment. The following image shows the response in the Kiro chat panel (Figure 6).

![Kiro chat interface showing AI response with list of Instana applications retrieved via MCP tool.](https://d2908q01vomqb2.cloudfront.net/c097638f92de80ba8d6c696b26e6e601a5f61eb7/2025/11/26/Figure6-KiroChatPanelDisplayingRetrievedInstanaApplicationList-1-1024x550.png)

Figure 6. Kiro chat panel displaying retrieved Instana application list.

### Configuring Kiro CLI Integration

After deploying the Instana MCP server, configure it in Kiro CLI.

13. Refer to the [Kiro documentation](https://kiro.dev/docs/cli/custom-agents/creating/) and run the following command to create a custom agent:

```
$ kiro-cli agent create --name instana
```

14. The command creates the *~/.kiro/agents/instana.json* file and prompts you to configure your agent. Use the following JSON example below to configure the instana agent:

```
{
"name": "instana",
"description": "Instana MCP Server for monitoring and observability via Kiro CLI",
"prompt": "You are an assistant that interacts with the Instana MCP server to fetch monitoring and observability data.",
"mcpServers": {
"instana-mcp": {
"type": "http",
"url": "http://<replace-with-your-mcp-host>:8080/mcp",
"timeout": 120000,
"disabled": false,
"headers":{
"INSTANA-BASE-URL":"https://<replace-with-your-instana-tenant>.instana.io",
"INSTANA-API-TOKEN":"<replace-with-your-api-token>"
}
}
},
"tools": ["*"]
}
```

15. After saving the configuration, start a new chat session with your custom Instana agent:

```
$ kiro-cli --agent instana
```

16. Ask questions such as: *List 3 applications in Instana*. Kiro CLI uses the Instana MCP server to retrieve the information. The following image shows the Kiro CLI response with application data (Figure 7):

![Terminal output showing Kiro CLI custom agent response with list of three Instana applications and their details.](https://d2908q01vomqb2.cloudfront.net/c097638f92de80ba8d6c696b26e6e601a5f61eb7/2025/11/26/Figure7-KiroCLIDisplayingInstanaApplicationsRetrievedMCPServer-1-1024x819.png)

Figure 7. Kiro CLI displaying Instana applications retrieved via MCP server.

### Monitoring AWS services with the Instana MCP server

With the Instana MCP server configured, you can monitor AWS services such as Amazon EC2, and Amazon EKS by asking questions in natural language.

17. Prompt your Instana custom agent with the instruction: List of available tool categories. This retrieves the list of available tool categories for monitoring and observability data. The following image shows the Kiro CLI output with the available Instana tool categories (Figure 8):

![Kiro CLI terminal showing categorized list of Instana MCP tools for monitoring and observability.](https://d2908q01vomqb2.cloudfront.net/c097638f92de80ba8d6c696b26e6e601a5f61eb7/2025/11/26/Figure8-AvailableInstanaToolCategoriesDisplayedKiroCLI-1024x827.png)

Figure 8. Available Instana tool categories displayed in Kiro CLI.

18. Next, prompt the agent with the instruction: *Show me 3 applications with health status*. Kiro uses the *get\_applications* MCP tool to retrieve a snapshot of application health directly from Instana. The following image shows the application health data in Kiro CLI (Figure 9):

![Kiro CLI output showing three Instana applications with health metrics including call rates and latency data.](https://d2908q01vomqb2.cloudfront.net/c097638f92de80ba8d6c696b26e6e601a5f61eb7/2025/11/26/Figure9-ApplicationHealthStatusRetrievedInstanaDisplayed-KiroCLI-2-1024x262.png)

Figure 9. Application health status retrieved from Instana displayed in Kiro CLI.

The output shows the health status of three Instana applications, highlighting inactive services with no recent traffic or metrics. Instana determines application health based on call volume and latency data.

19. Use the following prompt to correlate applications with Amazon EC2 instances: *Give me all applications that have at least one Amazon EC2 instance associated with them*. Kiro queries Instana APIs to map EC2-tagged resources to applications and returns a filtered list to help you identify Amazon EC2 dependent workloads. The following image shows the results in Kiro CLI (Figure 10):

![Kiro CLI displaying filtered list of Instana applications running on Amazon EC2 instances.](https://d2908q01vomqb2.cloudfront.net/c097638f92de80ba8d6c696b26e6e601a5f61eb7/2025/11/26/Figure10-InstanaApplicationsCorrelatedAmazonEC2InstancesKiroCLI-1-1024x606.png)

Figure 10. Instana applications correlated with Amazon EC2 instances in Kiro CLI.

20. You can also review recent Kubernetes events with the prompt: *Get Kubernetes events for the last 3 hours*. This calls the *get\_kubernetes\_info\_events* tool to summarize events such as failed container starts, resource constraints, and policy violations. The following image shows the Kubernetes event summary in Kiro CLI (Figure 11):

![Kiro CLI showing summarized Kubernetes events including pod failures and resource warnings.](https://d2908q01vomqb2.cloudfront.net/c097638f92de80ba8d6c696b26e6e601a5f61eb7/2025/11/26/Figure11-KubernetesEventsLastThreeHoursDisplayedKiroCLI-1024x709.png)

Figure 11. Kubernetes events from the last three hours displayed in Kiro CLI.

## Additional query examples

The following examples demonstrate additional queries you can use with Kiro to retrieve insights from Instana using the MCP server:

**Application Performance Analysis:**

- Show me the top 5 slowest endpoints in the last hour
- What applications have error rates above 5%?
- Get metrics for the checkout service in production
- Show services with the highest error rate in the last 30 minutes.

**Infrastructure Monitoring:**

- Show me all hosts in the production environment
- What Amazon EKS pods are consuming the most memory?
- List all infrastructure snapshots from the last 24 hours

**Alert Management:**

- Show me all active alerts for the payment service
- List all active alerts in the production environment.
- What alert configurations do we have for high CPU usage?
- Create a new alert for response time exceeding 500ms

**System Investigation:**

- What changes were made to our Amazon EKS cluster today?
- Show me recent deployment events that might explain the latency spike
- What infrastructure plugins are available for monitoring databases?

## Cleanup Instructions

After you complete your testing and validation, you can stop or remove the Instana MCP Server container to free up resources.

1. Stop and remove the Instana MCP server container:

```
$ docker stop mcp-instana
$ docker rm mcp-instana
```

2. Open Kiro IDE and choose the Kiro icon in the activity sidebar to open the Kiro settings panel.
3. In the **MCP SERVERS** section, locate the Instana MCP entry. Open the context (right-click) menu for the entry and choose **Disable** to disconnect Kiro from the Instana MCP server endpoint.
4. Choose the **pencil icon** to open the MCP configuration and delete the Instana MCP server configuration you added in step 10 of the **Implementation Walkthrough**
5. Remove the Kiro CLI custom Instana agent configuration file:

```
$ rm ~/.kiro/agents/instana.json
```

6. Revoke or rotate any temporary Instana API tokens used during setup to prevent unintended access to your Instana environment.

## Summary

In this blog, you learned how the IBM Instana Observability MCP Server enables users to interact with observability data using AI-driven conversational workflows from Kiro CLI and Kiro IDE.

By combining Instana’s observability capabilities with Kiro, developers can query metrics, traces, and alerts conversationally without dashboards or manual API calls. They can automate performance investigations directly from the command line or IDE and correlate application health with AWS services such as Amazon EC2, Amazon EKS, and [AWS Fargate](https://aws.amazon.com/fargate/) in real time.

This integration eliminates context switching, simplifies troubleshooting, and makes observability a first-class part of the developer experience on AWS. It accelerates root cause analysis using intelligent, context-aware responses from the Instana MCP Server.

To get started, visit Instana Observability on AWS Marketplace and subscribe to a [14-day free trial](https://aws.amazon.com/marketplace/pp/prodview-tbam5h35sumqg) of IBM Instana Observability SaaS on AWS.

### Additional Content:

- [Observe AI Agents on Amazon Bedrock AgentCore with IBM Instana](https://aws.amazon.com/blogs/ibm-redhat/observe-ai-agents-on-amazon-bedrock-agentcore-with-ibm-instana/)
- [Stream Amazon CloudWatch metrics to IBM Instana with Amazon Data Firehose](https://aws.amazon.com/blogs/ibm-redhat/stream-amazon-cloudwatch-metrics-to-ibm-instana-with-amazon-data-firehose/)
- [Reducing Network Costs and Enhancing Observability Security with IBM Instana and AWS PrivateLink](https://aws.amazon.com/blogs/ibm-redhat/reduce-network-costs-and-secure-observability-with-ibm-instana-and-aws-privatelink/)
- [Implement observability for Amazon EKS workloads using the Instana Amazon EKS Add-on](https://aws.amazon.com/blogs/ibm-redhat/implement-observability-for-amazon-eks-workloads-using-the-instana-amazon-eks-add-on/)
- [Monitor and Optimize Amazon EKS Costs with Instana and Kubecost](https://aws.amazon.com/blogs/ibm-redhat/monitor-and-optimize-amazon-eks-costs-with-ibm-instana-and-kubecost/)
- [Monitoring Amazon Bedrock Large Language Models with Instana](https://aws.amazon.com/blogs/ibm-redhat/monitoring-amazon-bedrock-large-language-models-with-ibm-instana/)
- [Automate Observability for AWS with Instana self-hosted](https://aws.amazon.com/blogs/ibm-redhat/automate-observability-for-aws-with-ibm-instana-self-hosted/)
- [Realtime monitoring of microservices and cloud-native applications with Instana SaaS on AWS](https://aws.amazon.com/blogs/architecture/realtime-monitoring-of-microservices-and-cloud-native-applications-with-ibm-instana-saas-on-aws/)

### Visit AWS Marketplace for IBM Instana solutions available on AWS:

- [IBM Instana Observability MCP Server](https://aws.amazon.com/marketplace/pp/prodview-q2hjdyja2mg5o)
- [IBM Instana Observability PayPerUse](https://aws.amazon.com/marketplace/pp/prodview-tbam5h35sumqg?trk=cf6e7ff3-7f21-4339-8254-6e13f0d635d7&sc_channel=el&source=ibm)
- [IBM Instana Observability (contract)](https://aws.amazon.com/marketplace/pp/prodview-xw7vca3ei33ea)
- [IBM Instana Observability Self-Hosted](https://aws.amazon.com/marketplace/pp/prodview-mbw42d6cjzi7e)
- [IBM Instana Observability Operator](https://aws.amazon.com/marketplace/pp/prodview-gsjlmrnf3tck2)