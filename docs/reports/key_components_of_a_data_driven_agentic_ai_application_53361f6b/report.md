---
title: 数据驱动的智能体AI应用的关键组件
publish_date: 2025-10-03
original_url: https://aws.amazon.com/blogs/database/key-components-of-a-data-driven-agentic-ai-application/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 9
unavailable_services: 4
---

# 数据驱动的智能体AI应用的关键组件

[📖 查看原始博客](https://aws.amazon.com/blogs/database/key-components-of-a-data-driven-agentic-ai-application/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心AI推理服务在中国区不可用，无法构建完整的agentic AI应用

文章讨论的核心服务Amazon Bedrock、Amazon Q Business和Amazon Q Developer在AWS中国区域均不可用。虽然文章提到的数据库服务（Aurora、DynamoDB、ElastiCache等）大部分可用，但缺少AI推理引擎和agent框架，无法实现文章描述的agentic AI应用架构。

## 服务分析

### 可用服务 (9个)

- Amazon Aurora PostgreSQL
- Amazon Aurora DSQL
- Amazon ElastiCache for Valkey
- Amazon OpenSearch Service
- Amazon Neptune Analytics
- Amazon DynamoDB
- Amazon Redshift
- Amazon S3 Tables
- AWS Lambda

### 不可用服务 (4个)

- **Amazon Bedrock** - 核心服务（AI推理引擎）
- **Amazon Bedrock AgentCore** - 核心服务（agent框架）
- **Amazon Bedrock Knowledge Bases** - 核心服务（RAG管理）
- **Amazon Q Business** - 核心服务（示例应用）
- **Amazon Q Developer** - 核心服务（示例应用）

### 评估说明

本文的核心主题是构建数据驱动的agentic AI应用，详细介绍了agent应用的三大核心组件：上下文管理、推理与规划、工具调用。文章重点讨论了如何使用Amazon Bedrock AgentCore构建agent事件循环，以及如何通过Amazon Q Business和Q Developer等应用展示agent能力。

虽然文章提到的数据存储和检索服务（如Aurora、DynamoDB、ElastiCache、OpenSearch、Neptune等）在中国区大部分可用，但这些只是agent应用的数据层支撑。缺少核心的AI推理服务（Amazon Bedrock）和agent框架（Bedrock AgentCore），就无法实现文章描述的ReAct事件循环、LLM推理、工具选择等核心功能。

服务可用率为69.2%（9/13），低于70%的MODERATE阈值，且所有不可用服务都是实现agentic AI应用的核心依赖。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 初步可行性评估为LOW，核心AI服务不可用，无法进行实际部署验证。文章是架构性和概念性内容，没有配套的完整应用代码仓库或具体操作步骤。

## 实施建议

### 推荐方案

**不建议直接实施**

本文介绍的agentic AI应用架构依赖于Amazon Bedrock作为核心AI推理引擎，以及Bedrock AgentCore作为agent框架。这些服务在AWS中国区域不可用，导致无法按照文章描述的方式构建完整的agentic AI应用。

虽然文章讨论的数据管理最佳实践（如使用向量数据库存储长期记忆、使用缓存存储短期会话、通过MCP协议标准化工具访问等）具有参考价值，但缺少AI推理层，这些数据层的设计无法发挥作用。

### 替代方案

如果希望在AWS中国区域构建类似的agentic AI应用，可以考虑以下替代方案：

1. **使用第三方LLM服务**
   - 实施方式：集成国内可用的大语言模型服务（如通义千问、文心一言等），自行实现agent事件循环和工具调用框架
   - 复杂度：高
   - 适用场景：有较强开发能力的团队，需要完全自主控制agent逻辑

2. **使用Amazon SageMaker部署开源模型**
   - 实施方式：在SageMaker上部署开源LLM（如Llama、Mistral等），使用开源agent框架（如LangGraph、Strands Agents）构建应用
   - 复杂度：高
   - 适用场景：需要数据隐私和模型自主可控的场景，有MLOps能力的团队

3. **混合架构**
   - 实施方式：在AWS中国区域部署数据层（Aurora、DynamoDB、ElastiCache等），通过专线或VPN连接到AWS全球区域使用Bedrock服务
   - 复杂度：中
   - 适用场景：对数据主权有要求但可以接受AI推理在境外的场景，需要评估数据传输的合规性和延迟影响

### 风险提示

- **服务依赖风险**: 文章的核心架构完全依赖Amazon Bedrock和相关AI服务，这些服务在中国区不可用
- **开发复杂度**: 替代方案需要自行实现agent框架、事件循环、工具调用等核心逻辑，开发工作量大
- **模型性能差异**: 使用第三方LLM或开源模型可能在推理能力、响应速度、成本等方面与Bedrock有显著差异
- **合规性考虑**: 如采用混合架构，需要评估跨境数据传输的合规性要求
- **运维成本**: 自建agent框架和模型部署需要持续的运维投入

### 配套资源

- **GitHub仓库**: 文章提到了多个AWS官方MCP服务器（如[Aurora DSQL MCP server](https://awslabs.github.io/mcp/servers/aurora-dsql-mcp-server/)、[DynamoDB MCP server](https://awslabs.github.io/mcp/servers/dynamodb-mcp-server/)等）
- **兼容性**: 这些MCP服务器可以在中国区使用，用于连接中国区的数据库服务
- **修改建议**: MCP服务器本身可用，但需要配合自建的agent框架使用，无法直接与Bedrock AgentCore集成
