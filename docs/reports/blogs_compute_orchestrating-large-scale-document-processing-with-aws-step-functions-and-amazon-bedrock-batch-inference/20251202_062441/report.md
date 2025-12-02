---
title: 使用AWS Step Functions和Amazon Bedrock批量推理编排大规模文档处理
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/compute/orchestrating-large-scale-document-processing-with-aws-step-functions-and-amazon-bedrock-batch-inference/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 10
unavailable_services: 5
---

# 使用AWS Step Functions和Amazon Bedrock批量推理编排大规模文档处理

[📖 查看原始博客](https://aws.amazon.com/blogs/compute/orchestrating-large-scale-document-processing-with-aws-step-functions-and-amazon-bedrock-batch-inference/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Bedrock及其相关功能在中国区域不可用，无法直接实施此解决方案

该解决方案的核心依赖Amazon Bedrock批量推理、Amazon Bedrock Knowledge Bases和Amazon Nova Pro模型进行文档分析和元数据提取。这些服务目前在AWS中国区域均不可用，导致整个解决方案无法按原设计实施。

## 服务分析

### 可用服务 (10个)

- AWS Step Functions
- Amazon Textract
- Amazon S3
- Amazon EventBridge
- Amazon SNS
- Amazon DynamoDB
- AWS Lambda
- AWS CloudFormation
- AWS CDK
- AWS IAM

### 不可用服务 (5个)

- **Amazon Bedrock** - 核心服务
- **Amazon Bedrock Knowledge Bases** - 核心服务
- **Amazon Bedrock batch inference** - 核心服务
- **Amazon Nova Pro** - 核心服务
- **Amazon OpenSearch Serverless**

### 评估说明

虽然该解决方案中的编排层（Step Functions）、文档处理层（Textract）和基础设施服务（S3、Lambda、DynamoDB等）在中国区域均可用，但核心的AI推理和知识库服务完全不可用：

1. **Amazon Bedrock及其批量推理功能**：这是整个解决方案的核心，用于分析提取的文本并生成结构化元数据。该服务在中国区域不可用。

2. **Amazon Bedrock Knowledge Bases**：用于存储和检索处理后的文档及元数据。该服务在中国区域不可用。

3. **Amazon Nova Pro模型**：解决方案使用的基础模型，在中国区域不可用。

4. **Amazon OpenSearch Serverless**：作为知识库的后端存储，在中国区域不可用。

由于核心AI服务不可用，即使其他基础设施服务可用，也无法实现原方案的主要功能。

## 验证结果

### 验证类型

⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Bedrock在中国区域不可用，无法进行实际部署验证。根据验证流程，可行性评估为LOW时跳过深入验证阶段。

## 实施建议

### 推荐方案

**不建议直接实施**

由于Amazon Bedrock及其相关服务在AWS中国区域不可用，此解决方案无法按原设计实施。核心的AI推理和知识库功能缺失，使得整个文档处理管道无法完成其主要目标。

### 替代方案

如果需要在AWS中国区域实现类似的大规模文档处理和知识库构建功能，可以考虑以下替代方案：

#### 1. **使用Amazon SageMaker替代Bedrock**

- **实施方式**：
  - 保留Step Functions + Textract的文档提取架构
  - 使用Amazon SageMaker部署开源LLM（如Llama、ChatGLM等）替代Amazon Bedrock
  - 使用SageMaker批量转换作业替代Bedrock批量推理
  - 自行实现元数据提取的提示工程和结果解析
  
- **复杂度**：高
  - 需要自行管理模型部署、版本控制和扩展
  - 需要处理模型推理的并发控制和成本优化
  - 需要实现批量推理的调度和监控逻辑
  
- **适用场景**：
  - 有机器学习团队支持
  - 对模型有定制化需求
  - 可以接受较高的初始开发成本

#### 2. **使用Amazon OpenSearch Service + 自建向量搜索**

- **实施方式**：
  - 使用Amazon OpenSearch Service（托管版）替代OpenSearch Serverless
  - 使用开源嵌入模型（如sentence-transformers）生成文档向量
  - 在OpenSearch中配置k-NN插件实现向量搜索
  - 自行实现RAG检索逻辑
  
- **复杂度**：中
  - 需要管理OpenSearch集群
  - 需要实现向量生成和索引管道
  - 相比Bedrock Knowledge Bases需要更多配置工作
  
- **适用场景**：
  - 需要对搜索和索引有更多控制
  - 已有OpenSearch使用经验
  - 文档量和查询量可预测

#### 3. **混合架构：中国区+全球区域**

- **实施方式**：
  - 在中国区域运行Step Functions + Textract进行文档提取
  - 通过跨区域复制将提取的文本传输到支持Bedrock的区域（如us-east-1）
  - 在全球区域使用Bedrock进行推理和知识库构建
  - 根据合规要求决定数据存储位置
  
- **复杂度**：中
  - 需要处理跨区域数据传输
  - 需要考虑数据合规性和延迟
  - 成本包含跨区域数据传输费用
  
- **适用场景**：
  - 数据合规允许跨境传输
  - 对Bedrock功能有强需求
  - 可以接受跨区域延迟

#### 4. **使用第三方AI服务**

- **实施方式**：
  - 保留AWS基础设施（Step Functions、Textract、S3等）
  - 集成中国本地的AI服务提供商（如阿里云通义千问、百度文心一言等）
  - 使用Lambda调用第三方API进行文本分析
  - 使用Amazon OpenSearch Service或其他数据库存储结果
  
- **复杂度**：中
  - 需要集成第三方服务API
  - 需要管理多个服务提供商的认证和配额
  - 可能面临不同的定价模型
  
- **适用场景**：
  - 数据必须保留在中国境内
  - 对中文处理有特殊要求
  - 愿意使用多云架构

### 风险提示

- **服务可用性风险**：Amazon Bedrock在中国区域的上线时间不确定，短期内无法使用原生服务。

- **替代方案复杂度**：所有替代方案都需要显著的额外开发工作，包括模型部署、推理管道构建、向量搜索实现等。

- **成本考虑**：
  - SageMaker方案需要持续运行推理端点或管理批量转换作业，成本可能高于Bedrock批量推理的50%折扣
  - OpenSearch Service需要持续运行集群，相比Serverless版本成本管理更复杂
  - 跨区域方案会产生数据传输费用

- **合规性风险**：跨区域方案需要确保符合数据本地化和跨境传输的法律法规要求。

- **维护负担**：自建方案需要持续维护模型、监控性能、处理扩展问题，运维复杂度显著高于托管服务。

- **功能差异**：替代方案可能无法完全复制Bedrock Knowledge Bases的所有功能，如自动分块、元数据过滤、混合搜索等。

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/sample-step-functions-batch-inference
- **兼容性**: 代码无法在中国区域直接使用，因为依赖Amazon Bedrock服务
- **修改建议**: 
  - 如采用SageMaker替代方案，需要重写所有Bedrock相关的调用逻辑
  - 需要实现自定义的批量推理输入/输出处理
  - 需要替换Knowledge Base相关的数据摄取和查询代码
  - 预计需要重写约40-50%的代码以适配替代服务

## 总结

该解决方案展示了一个优秀的大规模文档处理架构设计，但由于核心依赖的Amazon Bedrock服务在AWS中国区域不可用，无法直接实施。如果必须在中国区域实现类似功能，建议评估上述替代方案，并充分考虑额外的开发成本、运维复杂度和功能差异。对于有跨境数据传输合规性的场景，混合架构可能是最接近原方案的选择。
