---
title: 使客户能够大规模交付生产就绪的AI代理
publish_date: 2025-07-16
original_url: https://aws.amazon.com/blogs/machine-learning/enabling-customers-to-deliver-production-ready-ai-agents-at-scale/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 7
unavailable_services: 11
---

# 使客户能够大规模交付生产就绪的AI代理

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/enabling-customers-to-deliver-production-ready-ai-agents-at-scale/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

本文的核心内容围绕 Amazon Bedrock AgentCore 展开，这是一个完整的AI代理部署和运营服务套件。然而，Amazon Bedrock 及其所有子服务在AWS中国区域均不可用，导致文章介绍的整体解决方案无法在中国区实施。

## 服务分析

### 可用服务 (7个)

- Amazon SageMaker AI
- Amazon S3
- Amazon OpenSearch Service
- Amazon Cognito
- AWS Lambda
- AWS Marketplace
- Amazon DynamoDB

### 不可用服务 (11个)

- **Amazon Bedrock** - 核心服务
- **Amazon Bedrock AgentCore** - 核心服务（包括 Runtime, Identity, Observability, Gateway, Memory, Browser, Code Interpreter）
- **Amazon Bedrock Knowledge Bases** - 核心服务
- **Amazon Nova** - 核心服务（模型系列）
- **Amazon Connect** - 核心服务
- **Amazon Q Business** - 提及的相关服务
- **Amazon Q Developer** - 提及的相关服务
- **Amazon Rekognition** - 博客中提及
- **Amazon Textract** - 博客中提及
- **Amazon Translate** - 博客中提及
- **Amazon Lex** - 博客中提及

### 评估说明

1. **核心服务完全不可用**：文章的核心主题是 Amazon Bedrock AgentCore，这是一个专门为部署和运营AI代理而设计的服务套件。该服务及其所有组件（Runtime、Identity、Observability、Gateway、Memory、Browser、Code Interpreter）在中国区均不可用。

2. **模型基础缺失**：Amazon Nova 模型系列是文章介绍的AI代理的基础模型，包括 Nova Act（专门用于浏览器自动化的模型），这些在中国区无法使用。

3. **集成解决方案不可用**：Amazon Connect 作为客户体验解决方案在文章中被重点提及，但在中国区不可用。

4. **服务可用率极低**：仅有 38.9% 的服务可用，且可用的服务（如 S3、Lambda、DynamoDB）只是基础设施层面的支持，无法替代核心的AI代理服务。

## 验证结果

### 验证类型

⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段发现核心服务 Amazon Bedrock AgentCore 在AWS中国区域完全不可用，服务可用率仅为 38.9%，远低于深入验证的触发条件（MODERATE或HIGH）。由于核心架构无法实施，跳过深入验证阶段。

## 实施建议

### 推荐方案

**不建议直接实施**

本文介绍的 Amazon Bedrock AgentCore 解决方案在AWS中国区域无法实施，原因如下：

1. **核心服务缺失**：Amazon Bedrock 及其 AgentCore 套件是整个解决方案的基础，在中国区不可用
2. **模型不可用**：Amazon Nova 模型系列（包括 Nova Act）无法在中国区使用
3. **无直接替代方案**：AgentCore 提供的完整代理运营能力（安全运行时、身份管理、可观测性、网关、内存管理等）需要从零构建

### 替代方案

如果您需要在AWS中国区域构建AI代理系统，可以考虑以下替代路径：

1. **自建代理框架**
   - 实施方式：使用开源框架（如 LangChain、LlamaIndex）结合可用的AWS服务（Lambda、S3、DynamoDB）自行构建代理基础设施
   - 复杂度：高
   - 适用场景：有强大技术团队和充足开发时间的组织
   - 注意事项：需要自行实现安全隔离、会话管理、可观测性、权限控制等企业级功能

2. **使用第三方模型服务**
   - 实施方式：结合中国区可用的AWS基础服务（Lambda、S3、OpenSearch）与第三方大语言模型API（如国内模型提供商）构建代理系统
   - 复杂度：中到高
   - 适用场景：对模型选择灵活、可接受第三方服务的场景
   - 注意事项：需要评估数据隐私、合规性和服务稳定性

3. **Amazon SageMaker 自托管模型**
   - 实施方式：使用 Amazon SageMaker 部署开源大语言模型（如 Llama、Mistral），结合自建代理框架
   - 复杂度：高
   - 适用场景：对数据主权有严格要求、需要完全控制模型的场景
   - 注意事项：需要管理模型训练、部署、推理优化等全生命周期

### 风险提示

- **开发成本高**：缺少 AgentCore 提供的开箱即用能力，需要投入大量开发资源构建基础设施
- **安全性挑战**：自建系统需要自行实现会话隔离、权限管理、数据保护等安全机制
- **运维复杂度**：缺少托管服务的自动扩展、监控、恢复能力，需要建立完整的运维体系
- **技术债务**：自建方案可能难以跟上AI代理技术的快速演进
- **合规考虑**：使用第三方模型服务时需要仔细评估数据出境和隐私保护要求

### 配套资源

- **GitHub仓库**: 
  - AWS API MCP Server: https://github.com/awslabs/mcp/tree/main/src/aws-api-mcp-server
  - Strands Agents SDK: https://strandsagents.com/
  - Nova Act SDK: 处于研究预览阶段，具体链接未提供
- **兼容性**: 这些开源工具本身可以使用，但依赖 Amazon Bedrock 作为模型后端，在中国区需要替换为其他模型服务
- **修改建议**: 如要使用这些工具，需要将模型调用部分替换为中国区可用的模型服务API，这需要对代码进行较大改动
