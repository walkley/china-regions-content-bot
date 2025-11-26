---
title: Amazon Bedrock AgentCore Memory：构建上下文感知的智能代理
publish_date: 2025-08-13
original_url: https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 2
unavailable_services: 1
---

# Amazon Bedrock AgentCore Memory：构建上下文感知的智能代理

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

本文介绍的 Amazon Bedrock AgentCore Memory 是 Amazon Bedrock 的核心功能组件，而 Amazon Bedrock 服务在 AWS 中国区域不可用，因此该方案无法在中国区域实施。

## 服务分析

### 可用服务 (2个)

- AWS KMS (Key Management Service)
- AWS IAM (Identity and Access Management)

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务

### 评估说明

Amazon Bedrock AgentCore Memory 是 Amazon Bedrock 服务的一个子功能，专门用于为 AI 代理提供记忆管理能力。该服务包括：

1. **短期记忆（Short-term Memory）**：存储即时对话上下文和原始事件数据
2. **长期记忆（Long-term Memory）**：提取和存储持久化的洞察、偏好和知识
3. **记忆策略（Memory Strategies）**：包括语义策略、摘要策略和用户偏好策略

由于 Amazon Bedrock 是该方案的基础服务且在中国区域完全不可用，因此：

- 无法创建 AgentCore Memory 资源
- 无法使用任何记忆管理 API（CreateMemory、CreateEvent、RetrieveMemoryRecords 等）
- 无法实现文章中描述的任何功能特性（分支、检查点等）

该服务没有直接的替代方案，因为它是 Amazon Bedrock 生态系统的专有功能。

## 验证结果

### 验证类型

⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务 Amazon Bedrock 在 AWS 中国区域不可用，无法进行实际部署验证。

## 实施建议

### 推荐方案

**不建议在 AWS 中国区域实施此方案**

由于 Amazon Bedrock 服务在中国区域不可用，该方案无法直接实施。如果需要在中国区域构建具有记忆能力的 AI 代理，需要考虑完全不同的技术架构。

### 替代方案

如果需要在 AWS 中国区域实现类似的 AI 代理记忆管理功能，可以考虑以下自建方案：

1. **基于开源 LLM + 自建记忆系统**
   - 实施方式：
     - 使用 Amazon SageMaker 部署开源大语言模型（如 Llama、Mistral 等）
     - 使用 Amazon DynamoDB 存储短期对话历史
     - 使用 Amazon OpenSearch Service 或自建向量数据库存储长期记忆
     - 自行实现记忆提取和检索逻辑
   - 复杂度：高
   - 适用场景：有充足开发资源和时间，需要完全控制记忆管理逻辑

2. **使用第三方 AI 服务 + AWS 存储**
   - 实施方式：
     - 集成可在中国访问的第三方 LLM API（需确保合规性）
     - 使用 AWS 中国区域的存储服务（DynamoDB、RDS、S3）管理对话历史
     - 自行实现上下文管理和记忆检索
   - 复杂度：中
   - 适用场景：可以使用第三方 AI 服务，但希望数据存储在 AWS 中国区域

3. **简化的状态管理方案**
   - 实施方式：
     - 使用 Amazon ElastiCache 或 DynamoDB 实现会话状态管理
     - 实现简单的对话历史存储和检索
     - 不包含智能记忆提取功能
   - 复杂度：低
   - 适用场景：只需要基本的对话上下文保持，不需要复杂的长期记忆功能

### 风险提示

- **服务可用性风险**：Amazon Bedrock 及其相关服务在可预见的未来可能仍不会在中国区域提供
- **开发成本风险**：自建替代方案需要大量的开发和维护工作，成本远高于使用托管服务
- **功能差距风险**：自建方案难以完全复制 AgentCore Memory 的智能记忆提取和管理能力
- **合规性风险**：如使用第三方 AI 服务，需要确保符合中国的数据安全和隐私法规

### 配套资源

- **GitHub仓库**: https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory
- **兼容性**: 不兼容 AWS 中国区域
- **修改建议**: 由于依赖 Amazon Bedrock 服务，该示例代码无法通过简单修改在中国区域运行，需要完全重新设计架构
