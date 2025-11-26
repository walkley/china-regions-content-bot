---
title: 在 Amazon Bedrock AgentCore Runtime 上安全启动和扩展您的代理和工具
publish_date: 2025-08-13
original_url: https://aws.amazon.com/blogs/machine-learning/securely-launch-and-scale-your-agents-and-tools-on-amazon-bedrock-agentcore-runtime/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 4
unavailable_services: 1
---

# 在 Amazon Bedrock AgentCore Runtime 上安全启动和扩展您的代理和工具

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/securely-launch-and-scale-your-agents-and-tools-on-amazon-bedrock-agentcore-runtime/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务在中国区不可用，无法实施

本文完全依赖 Amazon Bedrock 及其 AgentCore 系列服务（AgentCore Runtime、AgentCore Memory、AgentCore Identity、AgentCore Gateway、AgentCore Browser），这些服务在AWS中国区域均不可用，导致文章中的所有技术方案、代码示例和最佳实践都无法在中国区域实施。

## 服务分析

### 可用服务 (4个)

- Amazon Cognito
- Amazon Simple Storage Service (Amazon S3)
- AWS Identity and Access Management (IAM)
- Amazon SageMaker

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务，文章的全部内容都基于此服务及其子服务

### 评估说明

Amazon Bedrock 是本文的核心依赖服务，文章介绍的所有功能都构建在 Bedrock AgentCore Runtime 之上：

1. **核心服务缺失**：Amazon Bedrock AgentCore Runtime 是文章的核心主题，用于托管和运行AI代理
2. **配套服务不可用**：AgentCore Memory（状态持久化）、AgentCore Identity（身份认证）、AgentCore Gateway（网关服务）、AgentCore Browser（浏览器工具）等所有配套服务均不可用
3. **无替代方案**：这些是专门为AI代理工作负载设计的托管服务，在中国区域没有直接的替代服务
4. **GitHub项目无法运行**：文章配套的所有GitHub示例代码都依赖 Bedrock AgentCore 服务，无法在中国区域执行

虽然文章提到的 Amazon Cognito、Amazon S3、IAM 和 SageMaker 在中国区域可用，但它们只是辅助服务，无法弥补核心服务的缺失。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段发现核心服务 Amazon Bedrock 及其所有 AgentCore 子服务在中国区域不可用，文章内容完全依赖这些服务，无实施可能性，因此跳过深入验证阶段。

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此方案**

本文介绍的 Amazon Bedrock AgentCore Runtime 是AWS专门为AI代理工作负载设计的托管服务，提供以下特性：
- 无服务器托管环境
- 会话隔离和安全执行
- 嵌入式身份管理
- 支持大型负载（最高100MB）
- 异步多小时代理执行
- 按使用量付费的定价模型

由于该服务在中国区域完全不可用，且没有功能对等的替代服务，建议考虑以下替代方向：

### 替代方案

1. **自建容器化AI代理平台**
   - 实施方式：使用 Amazon ECS/EKS 构建自己的代理托管平台，结合 Application Load Balancer、Amazon ElastiCache（会话管理）、Amazon RDS（状态持久化）
   - 复杂度：高
   - 适用场景：有充足开发资源和时间，需要完全控制代理执行环境
   - 注意事项：需要自行实现会话隔离、身份管理、资源调度等 AgentCore Runtime 提供的功能

2. **使用 AWS Lambda + Step Functions**
   - 实施方式：使用 Lambda 函数托管代理逻辑，Step Functions 编排多步骤工作流，DynamoDB 存储状态
   - 复杂度：中
   - 适用场景：代理执行时间较短（<15分钟）、工作流相对简单的场景
   - 注意事项：Lambda 有15分钟执行时间限制和6MB负载限制，无法支持文章中提到的8小时执行和100MB负载

3. **使用第三方AI代理平台**
   - 实施方式：考虑使用支持中国区域的第三方AI代理托管平台或开源框架（如 LangGraph、CrewAI）自行部署
   - 复杂度：中到高
   - 适用场景：需要快速启动，但可以接受供应商锁定或自行运维
   - 注意事项：需要评估第三方平台的安全性、合规性和在中国的可用性

### 风险提示

- **核心功能缺失**：无法使用 Amazon Bedrock 的基础模型和 AgentCore 的托管能力
- **开发成本高**：自建替代方案需要大量开发和运维工作
- **功能差距**：替代方案难以完全复制 AgentCore Runtime 的会话隔离、嵌入式身份、大负载支持等特性
- **维护负担**：自建方案需要持续维护和优化，包括安全更新、性能调优、成本控制等

### 配套资源

- **GitHub仓库**: 
  - https://github.com/awslabs/amazon-bedrock-agentcore-samples
  - https://github.com/aws/bedrock-agentcore-starter-toolkit
- **兼容性**: 不兼容中国区域
- **修改建议**: 这些示例代码完全依赖 Amazon Bedrock AgentCore 服务，无法通过简单修改在中国区域运行。如需参考，建议学习其架构设计思路，用于指导自建方案的开发。
