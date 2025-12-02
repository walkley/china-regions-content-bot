---
title: 使用❜embed的AI推荐平台在AWS上构建个性化Web3体验
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/web3/building-personalized-web3-experiences-with-embeds-ai-recommendation-platform-on-aws/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: HIGH
available_services: 15
unavailable_services: 1
---

# 使用❜embed的AI推荐平台在AWS上构建个性化Web3体验

[📖 查看原始博客](https://aws.amazon.com/blogs/web3/building-personalized-web3-experiences-with-embeds-ai-recommendation-platform-on-aws/) | 验证日期: 2025-12-02

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

文章介绍了❜embed如何在AWS上构建可扩展的Web3智能推荐引擎。架构涉及的16个AWS服务中，15个在中国区域完全可用，仅有1个非核心服务不可用且有成熟的替代方案。核心的机器学习、数据处理、存储和计算服务均可在中国区域正常使用。

## 服务分析

### 可用服务 (15个)

- Amazon Kinesis Data Streams - 实时数据流处理
- AWS Lambda - 无服务器计算
- Amazon EC2 - 弹性计算实例
- AWS Glue - ETL数据处理
- Amazon Athena - 无服务器查询服务
- Amazon RDS for PostgreSQL - 关系型数据库
- Amazon DynamoDB - NoSQL数据库
- Amazon ElastiCache - 内存缓存服务
- Amazon Aurora Serverless v2 - 无服务器关系型数据库
- Amazon SageMaker - 机器学习平台
- AWS IAM - 身份和访问管理
- AWS Secrets Manager - 密钥管理
- Amazon S3 - 对象存储
- Amazon CloudWatch - 监控和日志服务
- Amazon API Gateway - API管理服务

### 不可用服务 (1个)

- **Amazon SageMaker Ground Truth** - 用于机器学习数据标注

### 评估说明

该架构的核心服务可用性达到93.75%，所有关键组件均在中国区域可用：

1. **数据摄取层**：Amazon Kinesis Data Streams、AWS Lambda完全可用，可处理高速区块链数据流
2. **数据处理层**：AWS Glue、Amazon Athena、Amazon EC2均可用，支持ETL和图分析
3. **存储层**：Amazon RDS、Amazon DynamoDB、Amazon ElastiCache、Amazon Aurora Serverless v2全部可用
4. **机器学习层**：Amazon SageMaker完全可用，支持模型训练和推理
5. **安全和监控**：AWS IAM、AWS Secrets Manager、Amazon CloudWatch均可用

唯一不可用的Amazon SageMaker Ground Truth仅用于训练数据标注，属于模型开发阶段的辅助工具，不影响生产环境运行。可使用开源标注工具或第三方服务替代。

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 可行性评估为HIGH，所有核心服务可用，文章未提供需要部署验证的GitHub项目。架构方案可直接在中国区域实施。

## 实施建议

### 推荐方案

该方案可直接在AWS中国区域实施，架构设计和服务配置无需重大调整。

**实施路径**：
1. 按照文章描述的三层架构在中国区域部署服务
2. 使用Amazon SageMaker进行模型训练和部署
3. 配置Amazon Kinesis Data Streams处理实时区块链数据
4. 部署混合数据库架构（Aurora Serverless v2 + ElastiCache + Pinecone）
5. 使用AWS Lambda实现无服务器候选检索

**注意事项**：

- **数据标注替代方案**：由于Amazon SageMaker Ground Truth不可用，建议使用以下替代方案：
  - Label Studio（开源）- 功能完整的数据标注平台
  - Amazon SageMaker内置的标注功能（基础功能）
  - 第三方标注服务或人工标注团队
  
- **Pinecone向量数据库**：文章使用Pinecone作为向量数据库，需确认其在中国区域的可用性。如不可用，可考虑：
  - Amazon OpenSearch Service with k-NN插件
  - 自建向量数据库（如Milvus、Weaviate）
  
- **跨境数据传输**：如需访问全球区块链数据，需考虑网络连接和数据合规性
  
- **区域服务端点**：确保所有AWS服务使用中国区域端点（amazonaws.com.cn）

- **P3实例可用性**：确认cn-northwest-1区域P3实例的配额和可用性，用于SageMaker模型训练

### 替代方案

#### 方案1：数据标注替代

- **实施方式**：使用Label Studio开源平台替代SageMaker Ground Truth
- **复杂度**：低
- **适用场景**：需要持续标注训练数据的场景
- **部署建议**：在EC2上部署Label Studio，集成到现有ML pipeline

#### 方案2：向量数据库替代

- **实施方式**：使用Amazon OpenSearch Service with k-NN插件替代Pinecone
- **复杂度**：中
- **适用场景**：Pinecone在中国区域不可用或需要完全托管的AWS服务
- **优势**：完全托管、与AWS服务深度集成、支持向量相似度搜索

#### 方案3：自建向量数据库

- **实施方式**：在EC2上部署Milvus或Weaviate
- **复杂度**：中
- **适用场景**：需要更高的定制化和控制权
- **考虑因素**：需要自行管理运维、扩展和高可用性

### 风险提示

- **第三方服务依赖**：Pinecone为第三方服务，需确认其在中国区域的服务可用性和数据合规性
- **GPU实例配额**：SageMaker P3实例可能需要申请配额提升，建议提前规划
- **跨境数据访问**：访问全球区块链节点可能面临网络延迟和稳定性问题，建议评估使用中国区域的区块链节点服务
- **成本优化**：大规模向量搜索和ML推理成本较高，建议使用Reserved Instances和Savings Plans优化成本
- **数据合规**：处理用户行为数据需遵守中国数据保护法规，确保数据存储和处理符合合规要求

### 配套资源

- **GitHub仓库**：文章未提供配套代码仓库
- **官方文档**：[❜embed文档](https://docs.getembed.ai)
- **案例研究**：[Coinbase Wallet案例](https://getembed.ai/blog/a-personalized-onchain-feed-powered-by-embed-lands-inside-coinbase-wallet)
- **AWS服务文档**：
  - [Amazon SageMaker中国区文档](https://docs.amazonaws.cn/sagemaker/)
  - [Amazon Kinesis中国区文档](https://docs.amazonaws.cn/kinesis/)
  - [AWS Glue中国区文档](https://docs.amazonaws.cn/glue/)
