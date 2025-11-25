---
title: 使用Amazon Bedrock保护RAG应用中的敏感数据
publish_date: 2025-04-23
original_url: https://aws.amazon.com/blogs/machine-learning/protect-sensitive-data-in-rag-applications-with-amazon-bedrock/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 13
unavailable_services: 5
---

# 使用Amazon Bedrock保护RAG应用中的敏感数据

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/protect-sensitive-data-in-rag-applications-with-amazon-bedrock/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务在中国区不可用，方案无法实施

该博客方案依赖Amazon Bedrock作为核心基础服务，包括Amazon Bedrock Knowledge Bases、Amazon Bedrock Guardrails和Foundation Models，这些服务目前在AWS中国区域均不可用。此外，Scenario 1中用于敏感数据二次验证的Amazon Macie服务也不可用。由于核心服务缺失，该方案无法在中国区域实施。

## 服务分析

### 可用服务 (13个)

- Amazon OpenSearch Service
- AWS Lambda
- Amazon S3
- Amazon Comprehend
- Amazon EventBridge
- Amazon DynamoDB
- Amazon Cognito
- Amazon API Gateway
- Amazon Redshift
- AWS IAM
- AWS CloudTrail
- AWS CloudHSM
- AWS KMS
- Application Load Balancer

### 不可用服务 (5个)

- **Amazon Bedrock** - 核心服务（包括Knowledge Bases、Guardrails、Foundation Models）
- **Amazon Macie** - 核心服务（用于敏感数据检测和验证）
- **Amazon Rekognition** - 提及用于图像处理
- **Amazon Textract** - 提及用于文档处理
- **AWS Control Tower** - 提及用于治理和数据驻留控制

### 评估说明

虽然可用服务占比达到72.2%，但不可用的服务中包含了方案的核心依赖：

1. **Amazon Bedrock是整个方案的基础**：博客的两个场景都完全依赖Amazon Bedrock Knowledge Bases进行RAG工作流管理，依赖Amazon Bedrock Guardrails进行PII检测和过滤，依赖Amazon Bedrock Foundation Models进行推理生成。没有这些服务，方案的核心功能无法实现。

2. **Amazon Macie在Scenario 1中不可替代**：Scenario 1采用多层安全防护，Amazon Comprehend进行初次PII删除后，Amazon Macie作为二次验证层确保删除的有效性。虽然可以考虑其他敏感数据检测方案，但会显著改变架构设计。

3. **其他不可用服务影响有限**：Amazon Rekognition、Amazon Textract和AWS Control Tower在博客中仅作为扩展功能提及，不影响核心方案。

## 验证结果

### 验证类型

- ⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段评估可行性为LOW，核心服务Amazon Bedrock在中国区域不可用，方案无法实施，因此跳过深入验证阶段。

## 实施建议

### 推荐方案

不建议在AWS中国区域实施此方案。核心服务Amazon Bedrock（包括Knowledge Bases、Guardrails和Foundation Models）的缺失使得该方案无法按原设计实现。

### 替代方案

如果需要在AWS中国区域实现类似的RAG应用敏感数据保护功能，可以考虑以下替代方案：

1. **自建RAG系统 + 开源LLM**
   - 实施方式：
     - 使用Amazon OpenSearch Service作为向量数据库
     - 使用开源嵌入模型（如sentence-transformers）进行文本向量化
     - 在Amazon SageMaker上部署开源LLM（如Llama、ChatGLM等）
     - 使用Amazon Comprehend进行PII检测和删除
     - 自行实现Guardrails逻辑（基于规则或开源工具）
   - 复杂度：高
   - 适用场景：有较强技术团队，愿意投入开发和维护资源

2. **混合云架构**
   - 实施方式：
     - 敏感数据处理和存储保留在中国区域
     - 使用Amazon Comprehend在中国区域进行PII删除
     - 删除后的数据通过专线或VPN传输到海外区域
     - 在海外区域使用Amazon Bedrock进行RAG处理
     - 结果返回中国区域
   - 复杂度：高
   - 适用场景：对数据跨境传输有合规支持，且能接受延迟增加

3. **等待服务上线**
   - 实施方式：关注AWS中国区域服务更新，等待Amazon Bedrock正式上线
   - 复杂度：低
   - 适用场景：项目时间线灵活，可以等待服务可用

### 风险提示

- **合规风险**：如采用混合云方案，需要确保数据跨境传输符合中国数据安全法律法规要求
- **技术复杂度**：自建方案需要处理模型部署、性能优化、安全防护等多方面技术挑战
- **维护成本**：开源方案需要持续投入资源进行模型更新、安全补丁和性能优化
- **功能差距**：自建方案难以完全复制Amazon Bedrock Guardrails的智能PII检测和过滤能力

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/amazon-bedrock-samples/tree/main/security/securing-rag-apps
- **兼容性**: 代码依赖Amazon Bedrock服务，无法直接在中国区域使用
- **修改建议**: 需要完全重构方案架构，替换Amazon Bedrock相关组件，工作量巨大且不建议进行
