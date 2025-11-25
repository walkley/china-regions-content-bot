---
title: 使用新一代Amazon SageMaker加速分析和AI创新
publish_date: 2025-03-13
original_url: https://aws.amazon.com/blogs/big-data/accelerate-analytics-and-ai-innovation-with-the-next-generation-of-amazon-sagemaker/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 16
unavailable_services: 4
---

# 使用新一代Amazon SageMaker加速分析和AI创新

[📖 查看原始博客](https://aws.amazon.com/blogs/big-data/accelerate-analytics-and-ai-innovation-with-the-next-generation-of-amazon-sagemaker/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

虽然80%的服务在中国区可用，但文章重点介绍的核心功能Amazon Bedrock和Amazon Q Developer在中国区不可用，这两项服务是SageMaker Unified Studio的核心价值主张，缺失这些功能将严重影响整体方案的实用性。

## 服务分析

### 可用服务 (16个)

- Amazon SageMaker
- Amazon SageMaker Unified Studio
- Amazon SageMaker Lakehouse
- Amazon SageMaker Catalog
- Amazon SageMaker AI
- Amazon EMR
- AWS Glue
- Amazon Athena
- Amazon Redshift
- Amazon S3
- Amazon S3 Tables
- Amazon Aurora
- Amazon QLDB
- Amazon QuickSight
- Amazon Kinesis
- Amazon MSK
- Amazon OpenSearch Service

### 不可用服务 (4个)

- **Amazon Bedrock** - 核心服务
- **Amazon Q Developer** - 核心服务
- **Amazon Nova** - Bedrock模型系列
- Amazon Q Business

### 评估说明

本文介绍的是Amazon SageMaker的新一代产品，核心亮点是通过SageMaker Unified Studio统一数据和AI开发环境。文章重点强调了以下核心能力：

1. **Amazon Bedrock集成**：文章明确指出"Capabilities from Amazon Bedrock are now generally available in SageMaker Unified Studio"，这是统一工作室的重要功能之一，用于快速原型设计、定制和共享生成式AI应用。

2. **Amazon Q Developer集成**：作为"最强大的软件开发生成式AI助手"，Q Developer在SageMaker Unified Studio中用于代码编写、SQL生成、数据发现和故障排除等关键任务。

3. **业务场景依赖**：文章中的示例场景（智能数字助手、潜在客户评分）严重依赖这两项服务。数据团队使用Bedrock构建虚拟助手，数据科学家使用Q Developer进行代码编写和故障排除。

由于这两项核心服务在中国区不可用，即使其他分析和机器学习服务可用，也无法实现文章描述的统一开发体验和完整功能。

## 验证结果

### 验证类型

- ⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 初步可行性评估为LOW，且文章为产品发布公告，无配套GitHub项目或具体操作步骤可供验证。核心服务Amazon Bedrock和Amazon Q Developer在中国区不可用，无法进行有意义的实际部署验证。

### 关键发现

由于跳过深入验证，此部分不适用。

## 实施建议

### 推荐方案

**不建议直接实施**

本文介绍的新一代Amazon SageMaker的核心价值在于：
- 统一的数据和AI开发环境
- 集成Amazon Bedrock的生成式AI能力
- 集成Amazon Q Developer的智能辅助开发能力

由于Amazon Bedrock和Amazon Q Developer在中国区不可用，无法实现文章描述的完整功能和统一体验。虽然可以使用其他可用的SageMaker组件（如SageMaker AI、SageMaker Lakehouse等），但这将失去"统一工作室"的核心优势。

### 替代方案

1. **使用传统SageMaker服务**
   - 实施方式：继续使用Amazon SageMaker AI进行机器学习模型开发，使用AWS Glue、Amazon Athena、Amazon Redshift等服务进行数据分析
   - 复杂度：中
   - 适用场景：需要机器学习和数据分析能力，但不需要统一开发环境和生成式AI功能的场景

2. **自建生成式AI能力**
   - 实施方式：在Amazon SageMaker上部署开源大语言模型（如Llama、Qwen等），自行构建类似Bedrock的生成式AI能力
   - 复杂度：高
   - 适用场景：有较强技术团队，需要生成式AI能力且愿意投入资源进行自建的组织

3. **分离式工作流**
   - 实施方式：使用可用的AWS服务分别构建数据分析管道（EMR、Glue、Athena、Redshift）和机器学习工作流（SageMaker AI），通过S3和数据目录进行集成
   - 复杂度：中
   - 适用场景：传统的数据分析和机器学习项目，不强调统一开发体验

### 风险提示

- **功能缺失风险**：无法使用Amazon Bedrock的基础模型、Agents、Flows、Knowledge Bases和Guardrails功能，严重限制生成式AI应用开发能力
- **开发效率风险**：缺少Amazon Q Developer的智能辅助，代码编写、SQL生成、故障排除等任务需要更多人工投入
- **体验一致性风险**：无法实现文章描述的"单一数据和AI开发环境"，团队需要在多个工具和控制台之间切换
- **未来兼容性风险**：随着SageMaker Unified Studio的持续演进，中国区与全球区的功能差距可能进一步扩大

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 不适用
