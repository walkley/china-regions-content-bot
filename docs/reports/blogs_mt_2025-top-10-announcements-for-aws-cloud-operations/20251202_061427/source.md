# 2025 Top 10 Announcements for AWS Cloud Operations

by Nereida Woo, Calvin Weng, and Raviteja Sunkavalli on 26 NOV 2025 in Announcements, Innovation and Reinvention, Management Tools Permalink  Share

![](https://d2908q01vomqb2.cloudfront.net/972a67c48192728a34979d9a35164c1295401b71/2025/11/26/2025-11-26_10-38-58.png)

At AWS re:Invent 2025, we’re excited to share latest innovations designed to empower organizations to thrive in the transformative AI era. This year’s top Cloud Operations announcements address the most pressing challenges our customers face today—from gaining comprehensive visibility into generative AI workloads to significantly accelerating incident resolution and efficiently managing the exponential growth of operational data in modern cloud environments.

### 1. [Generative AI observability in Amazon CloudWatch and AgentCore Observability](https://aws.amazon.com/about-aws/whats-new/2025/10/generative-ai-observability-amazon-cloudwatch/)

Amazon CloudWatch offers comprehensive observability for generative AI applications and agents, providing built-in insights into latency, token usage, and errors across your AI stack. This new capability works seamlessly with Amazon Bedrock AgentCore and is compatible with open-source agentic frameworks like LangChain, LangGraph, and CrewAI. You can monitor model invocations, trace agent workflows end-to-end, and quickly identify performance bottlenecks—all without writing custom instrumentation code.  To learn more, visit [Generative AI observability in Amazon CloudWatch](https://aws.amazon.com/about-aws/whats-new/2025/10/generative-ai-observability-amazon-cloudwatch/).

![[Figure 1] Amazon CloudWatch Generative AI dashboard](https://d2908q01vomqb2.cloudfront.net/972a67c48192728a34979d9a35164c1295401b71/2025/11/26/Figure-1-CloudWatch-Generative-AI-dashboard.png)

[Figure 1] Amazon CloudWatch Generative AI dashboard

![[Figure 2] Agent Management View ](https://d2908q01vomqb2.cloudfront.net/972a67c48192728a34979d9a35164c1295401b71/2025/11/26/Figure-2-Agent-Management-View-.png)

[Figure 2] Agent Management View

### 2. [Amazon CloudWatch application map now supports un-instrumented services discovery](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-cloudwatch-application-map-un-instrumented-discovery/)

Amazon CloudWatch Application Signals application map now automatically discovers and visualizes your application topology without requiring instrumentation, giving you instant visibility into service dependencies and relationships. This enhancement builds on the [application map general availability launch](https://aws.amazon.com/about-aws/whats-new/2025/10/application-map-generally-available-amazon-cloudwatch/) earlier in September, adding intelligent automatic grouping that organizes services based on their relationships and provides contextual operational insights directly in the map view.

![[Figure 3] CloudWatch Application Map](https://d2908q01vomqb2.cloudfront.net/972a67c48192728a34979d9a35164c1295401b71/2025/11/26/Figure-3-CloudWatch-Application-Map.png)

[Figure 3] CloudWatch Application Map

### 3. [Amazon CloudWatch investigations now with incident report generation and 5 “whys” analysis](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-cloudwatch-incident-report/)

AI-powered operations (AIOps) capabilities help you resolve incidents faster, reduce manual toil, and empower operators of all experience levels to troubleshoot complex distributed systems.  [CloudWatch investigations](https://aws.amazon.com/about-aws/whats-new/2025/06/ga-accelerate-troubleshooting-amazon-cloudwatch-investigations/), which reached general availability in June, represents a significant leap forward in operational intelligence. This capability harnesses generative AI to automate complex root cause analysis and provide guided troubleshooting experiences for DevOps teams facing critical incidents. Building on this foundation, our October release introduced interactive incident report generation capabilities, fundamentally transforming how organizations approach operational challenges—enabling teams to shift from reactive emergency response to systematic, knowledge-driven problem resolution and continuous improvement.

We’ve also introduced an integrated AI-powered ‘5 Whys’ analysis workflow that implements the exact systematic methodology AWS teams use internally to drive to root causes. Drawing on two decades of AWS operational discipline through our Correction of Errors (COE) methodology—the same framework we’ve refined internally to document incidents, identify systemic issues, and prevent recurrence—CloudWatch’s incident reporting capability now encapsulates this institutional knowledge in an accessible service. A single click activates comprehensive data collection across telemetry metrics, deployment events, configuration changes, and investigation activities to generate detailed, contextual incident documentation. Unlike generic templates, each report is dynamically constructed from your specific operational data, change history, and architectural context—delivering stakeholders precisely the actionable insights needed to strengthen resilience within your unique environment.

![[Figure 4] Amazon CloudWatch Investigations Incident Report](https://d2908q01vomqb2.cloudfront.net/972a67c48192728a34979d9a35164c1295401b71/2025/11/26/Figure-4-Amazon-CloudWatch-Investigations-Incident-Report.png)

[Figure 4] Amazon CloudWatch Investigations Incident Report

![[Figure 5] 5 Whys Analysis in the CloudWatch investigations Incident Report](https://d2908q01vomqb2.cloudfront.net/972a67c48192728a34979d9a35164c1295401b71/2025/11/26/Figure-4-5-Whys-Analysis-in-the-CloudWatch-investigations-Incident-Report.png)

[Figure 5] 5 Whys Analysis in the CloudWatch investigations Incident Report

###

### 4. [Amazon CloudWatch and Application Signals MCP Servers](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-cloudwatch-application-signals-mcp-servers-for-ai-assisted-troubleshooting/)

Model Context Protocol (MCP) servers for Amazon CloudWatch and CloudWatch Application Signals help bridge AI assistants and agents to interact naturally with your observability data. These MCP servers provide standardized access to metrics, logs, alarms, traces, and service health data, allowing you to build autonomous operational workflows and integrate CloudWatch with AI-powered development tools. Learn more about [how to enhance your AIOps](https://aws.amazon.com/blogs/mt/enhance-your-aiops-introducing-amazon-cloudwatch-and-application-signals-mcp-servers/).

### 5. [Amazon CloudWatch Application Signals adds GitHub Action and MCP server improvements](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-cloudwatch-application-signals-adds-github-action-mcp-server-improvements/)

CloudWatch Application Signals now integrates directly into developer workflows with a new GitHub Action that provide observability insights during pull requests and CI/CD pipelines. Combined with enhanced MCP server capabilities, developers can identify performance regressions, monitor service health, and troubleshoot issues without leaving their development environment.

![[Figure 6] Automated Root Cause Analysis in the GitHub issues](https://d2908q01vomqb2.cloudfront.net/972a67c48192728a34979d9a35164c1295401b71/2025/11/26/Figure-5-Automated-Root-Cause-Analysis-in-the-GitHub-issues.png)

[Figure 6] Automated Root Cause Analysis in the GitHub issues

![[Figure 7] Automated GitHub Pull Request to Fix the Issue](https://d2908q01vomqb2.cloudfront.net/972a67c48192728a34979d9a35164c1295401b71/2025/11/26/Figure-6-Automated-GitHub-Pull-Request-to-Fix-the-Issue.png)

[Figure 7] Automated GitHub Pull Request to Fix the Issue

We introduced a comprehensive suite of capabilities specifically designed to address these challenges head-on. By reimagining how operational data is collected, centralized, analyzed, and visualized, these innovations deliver intelligent aggregation that dramatically reduces complexity, powerful analytics that surface actionable insights, and centralized visibility that eliminates fragmented monitoring silos.

### 6. [Amazon OpenSearch Service enhances log analytics with new PPL experience](https://aws.amazon.com/about-aws/whats-new/2025/11/opensearch-service-log-analytics-ppl/)

Amazon OpenSearch Service introduces significant enhancements to Piped Processing Language (PPL), making log analytics faster and more intuitive. These improvements include advanced query capabilities, better performance for complex analytical queries, and seamless integration with CloudWatch Logs for unified log analysis across your AWS environment.

### 7. [Amazon CloudWatch real user monitoring (RUM) adds support for iOS and Android applications](https://aws.amazon.com/about-aws/whats-new/2025/11/real-user-monitoring-mobile-apps-cloudwatch/)

Amazon CloudWatch now extends Real User Monitoring (RUM) to mobile applications, providing visibility into actual user experiences on iOS and Android devices. Monitor performance metrics, track user journeys, identify client-side errors, and understand how your mobile apps perform across different devices, networks, and geographies—all from the CloudWatch console.

### 8. [AWS CloudTrail adds data event aggregation to simplify security monitoring](https://aws.amazon.com/about-aws/whats-new/2025/11/cloudtrail-data-event-aggregation-security-monitoring/)

AWS CloudTrail now offers event aggregation and insights for data events, consolidating high-volume API activity into 5-minute summaries while automatically detecting unusual patterns. This dual capability reduces data volume and costs while enhancing security monitoring—helping you identify anomalies like unexpected S3 access patterns or DynamoDB throttling without manual analysis. To learn more, visit  [AWS CloudTrail Event Aggregation and Insights for data events](https://aws.amazon.com/blogs/mt/announcing-aws-cloudtrail-event-aggregation-and-insights-for-data-events/).

### 9. [Amazon CloudWatch launches Cross-Account and Cross-Region Log Centralization](https://aws.amazon.com/about-aws/whats-new/2025/09/amazon-cloudwatch-cross-account-cross-region-log-centralization/)

CloudWatch Logs Centralization consolidates log data from multiple AWS accounts and regions into a single destination account—eliminating custom aggregation pipelines and providing a unified view of all operational data. Integrated with AWS Organizations, you can scope and scale centralization rules across your entire organization, specific organizational units, or selected accounts. Log events are automatically enriched with @aws.account and @aws.region fields to maintain source context and data lineage.

With minimal setup time, teams gain improved operational efficiency, enhanced security posture, and faster incident resolution. The first copy of centralized logs incurs no additional ingestion charges, making this a cost-efficient approach to multi-account log management. Read more about [simplifying log management.](https://aws.amazon.com/blogs/mt/simplifying-log-management-using-amazon-cloudwatch-logs-centralization/)

### 10. [Amazon CloudWatch Database Insights adds cross-account cross-region monitoring](https://aws.amazon.com/about-aws/whats-new/2025/11/cloudwatch-database-insights-cross-account-region-monitoring/)

CloudWatch Database Insights now supports cross-account and cross-region monitoring, enabling centralized visibility into database performance across your entire AWS organization. Monitor Amazon RDS, Amazon Aurora, and Amazon DynamoDB metrics from a single monitoring account, correlate database performance with application health, and troubleshoot issues faster with unified observability.

### Conclusion

These announcements represent a **significant leap forward** in cloud operations capabilities. We’ve built transformative solutions that directly address the unique challenges of operating in the AI age. From comprehensive **generative AI observability** that provides unprecedented visibility into AI applications, to **AI-powered incident resolution** that dramatically accelerates troubleshooting, to **intelligent data management** that cuts through complexity—AWS innovations help you operate faster, smarter, and more efficiently.

Don’t miss this opportunity to experience these game-changing capabilities firsthand. Attend our [Innovation Talk](https://registration.awsevents.com/flow/awsevents/reinvent2025/eventcatalog/page/eventcatalog?trk=direct&search.type=1707427142681001EHKS&search=INV206) and sessions at **re:Invent** for live demonstrations and visit the **Cloud Operations booth** to explore how these innovations can transform your operations. The future of cloud operations is here—more powerful, intelligent, and efficient than ever before.