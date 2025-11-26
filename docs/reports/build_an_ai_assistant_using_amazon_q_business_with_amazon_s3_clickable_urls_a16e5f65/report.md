---
title: 使用Amazon Q Business和Amazon S3可点击URL构建AI助手
publish_date: 2025-08-05
original_url: https://aws.amazon.com/blogs/machine-learning/build-an-ai-assistant-using-amazon-q-business-with-amazon-s3-clickable-urls/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 5
unavailable_services: 1
---

# 使用Amazon Q Business和Amazon S3可点击URL构建AI助手

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/build-an-ai-assistant-using-amazon-q-business-with-amazon-s3-clickable-urls/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

本文的核心服务Amazon Q Business在AWS中国区域不可用，整个解决方案完全依赖该服务，无法在中国区域实施。

## 服务分析

### 可用服务 (5个)

- Amazon S3
- AWS IAM Identity Center
- AWS IAM
- AWS CLI
- AWS CloudShell

### 不可用服务 (1个)

- **Amazon Q Business** - 核心服务

### 评估说明

虽然本文涉及的6个AWS服务中有5个（83.3%）在中国区域可用，但唯一不可用的服务Amazon Q Business是整个解决方案的核心和基础。该服务提供了：

1. **生成式AI对话能力** - 整个AI助手的核心功能
2. **文档索引和检索** - 从企业文档中提取信息的能力
3. **用户认证和授权** - 细粒度的访问控制
4. **Web体验界面** - 用户交互的主要方式

没有Amazon Q Business，即使其他所有服务都可用，也无法构建本文描述的AI助手解决方案。目前在AWS中国区域没有直接的替代服务可以提供相同的功能集。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Q Business在AWS中国区域不可用，无法进行实际部署验证。即使进行深入验证，也无法成功部署该解决方案。

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此方案**

由于Amazon Q Business服务在中国区域完全不可用，本文描述的解决方案无法在AWS中国区域实施。

### 替代方案

如果需要在AWS中国区域构建类似的企业AI助手，可以考虑以下替代方案：

1. **Amazon Bedrock + 自建RAG架构**
   - 实施方式：使用Amazon Bedrock提供的基础模型，结合Amazon OpenSearch Service或其他向量数据库，自行构建检索增强生成(RAG)架构
   - 复杂度：高
   - 适用场景：需要完全自定义的AI助手解决方案，有足够的开发资源和时间
   - 注意：需要验证Amazon Bedrock在中国区域的可用性

2. **第三方AI服务集成**
   - 实施方式：使用中国本地的AI服务提供商（如阿里云、腾讯云等）的对话AI服务，结合AWS S3存储企业文档
   - 复杂度：中
   - 适用场景：希望快速部署，可以接受使用第三方AI服务
   - 注意：需要考虑数据跨境和合规性问题

3. **开源LLM自托管方案**
   - 实施方式：在Amazon EC2上部署开源大语言模型（如Llama、ChatGLM等），结合向量数据库构建RAG系统
   - 复杂度：高
   - 适用场景：对数据隐私有严格要求，希望完全控制AI模型
   - 注意：需要较大的计算资源和专业的AI/ML团队

### 风险提示

- **服务不可用风险**: Amazon Q Business在可预见的未来可能仍不会在AWS中国区域推出，依赖该服务的方案无法实施
- **功能差距风险**: 替代方案可能无法完全复制Amazon Q Business的所有功能，特别是在用户认证、细粒度授权和开箱即用的Web体验方面
- **开发成本风险**: 自建替代方案需要大量的开发工作和持续维护，成本远高于使用托管服务
- **合规性风险**: 使用第三方AI服务或跨境数据传输可能涉及数据合规和隐私保护问题

### 配套资源

- **示例数据**: [SampleData.zip](https://aws-blogs-artifacts-public.s3.us-east-1.amazonaws.com/artifacts/ML-19045/SampleData.zip)
- **兼容性**: 示例数据可以下载使用，但由于核心服务不可用，无法按照原文步骤进行部署
- **修改建议**: 不适用，因为核心服务缺失导致整个方案无法实施
