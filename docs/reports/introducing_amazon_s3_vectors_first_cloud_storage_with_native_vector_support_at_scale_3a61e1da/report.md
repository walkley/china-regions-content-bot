---
title: 介绍 Amazon S3 Vectors：首个支持大规模原生向量的云存储（预览版）
publish_date: 2025-07-15
original_url: https://aws.amazon.com/blogs/aws/introducing-amazon-s3-vectors-first-cloud-storage-with-native-vector-support-at-scale/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 5
unavailable_services: 2
---

# 介绍 Amazon S3 Vectors：首个支持大规模原生向量的云存储（预览版）

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/introducing-amazon-s3-vectors-first-cloud-storage-with-native-vector-support-at-scale/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

Amazon S3 Vectors 是一个全新的预览功能（2025年7月15日发布），且严重依赖 Amazon Bedrock 生成向量嵌入。由于 Bedrock 在中国区域不可用，文章中的核心功能和代码示例无法直接实施。

## 服务分析

### 可用服务 (5个)

- Amazon S3
- Amazon OpenSearch Service
- AWS Key Management Service (AWS KMS)
- AWS CLI
- AWS SDKs

### 不可用服务 (2个)

- **Amazon Bedrock** - 核心服务，用于生成向量嵌入
- **Amazon SageMaker Unified Studio** - 相关服务，用于统一开发环境

### 评估说明

1. **核心服务不可用**：Amazon Bedrock 是文章中生成向量嵌入的核心依赖，所有代码示例都使用 Bedrock 的 Titan 嵌入模型。没有 Bedrock，无法按照文章描述的方式生成向量数据。

2. **S3 Vectors 功能可用性未知**：S3 Vectors 是 2025年7月15日刚发布的预览功能，目前仅在以下区域可用：
   - US East (N. Virginia)
   - US East (Ohio)
   - US West (Oregon)
   - Europe (Frankfurt)
   - Asia Pacific (Sydney)
   
   中国区域（cn-northwest-1、cn-north-1）未在支持列表中。

3. **集成功能受限**：文章介绍的三个主要集成场景都依赖不可用服务：
   - Amazon Bedrock Knowledge Bases 集成
   - Amazon SageMaker Unified Studio 集成
   - Amazon OpenSearch Service 集成（此服务可用，但数据源依赖 S3 Vectors）

## 验证结果

### 验证类型

⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 初步可行性评估为 LOW，核心服务 Amazon Bedrock 在中国区域不可用，且 S3 Vectors 功能未在中国区域发布。根据验证流程，不执行深入验证。

## 实施建议

### 推荐方案

**不建议直接实施**

由于以下关键限制，不建议在中国区域实施此方案：

1. **S3 Vectors 功能不可用**：该功能目前仅在5个海外区域预览，中国区域未包含在内
2. **Amazon Bedrock 不可用**：无法使用文章中的向量嵌入生成方法
3. **核心集成场景无法实现**：Bedrock Knowledge Bases 和 SageMaker Unified Studio 集成均不可用

### 替代方案

如果需要在中国区域实现类似的向量存储和检索功能，可以考虑以下替代方案：

1. **使用 Amazon OpenSearch Service 向量引擎**
   - 实施方式：直接使用 OpenSearch 的 k-NN 插件存储和查询向量数据
   - 复杂度：中
   - 适用场景：需要实时、低延迟向量搜索的应用
   - 限制：成本较高，不适合大规模长期存储

2. **自建向量数据库方案**
   - 实施方式：
     - 使用开源向量数据库（如 Milvus、Qdrant、Weaviate）部署在 Amazon EC2 或 Amazon EKS 上
     - 使用 Amazon S3 标准存储桶存储原始数据和向量备份
     - 使用开源或第三方嵌入模型（如 Sentence Transformers、OpenAI API）生成向量
   - 复杂度：高
   - 适用场景：需要完全控制和定制化的企业应用
   - 优势：灵活性高，可以选择适合的嵌入模型和向量数据库

3. **混合云架构**
   - 实施方式：
     - 在海外区域（如 us-west-2）使用 S3 Vectors 和 Bedrock
     - 通过 AWS Direct Connect 或 VPN 连接中国区域应用
     - 考虑数据合规和延迟问题
   - 复杂度：高
   - 适用场景：对数据出境有合规许可的场景
   - 限制：需要处理跨境数据传输的合规性和网络延迟

### 风险提示

- **功能可用性风险**：S3 Vectors 目前处于预览阶段，即使未来在中国区域发布，功能特性和定价可能与海外区域有差异
- **服务依赖风险**：Amazon Bedrock 在中国区域的发布时间未知，短期内无法使用文章中的完整方案
- **成本风险**：替代方案（如自建向量数据库）的运维成本和复杂度显著高于托管服务
- **合规风险**：如采用混合云架构，需要确保符合中国数据安全和隐私保护相关法律法规

### 配套资源

- **GitHub仓库**: https://github.com/awslabs/s3vectors-embed-cli
- **兼容性**: 不可在中国区使用（依赖 S3 Vectors 和 Bedrock）
- **修改建议**: 需要完全重写以使用替代的嵌入模型和存储方案，不建议尝试修改
