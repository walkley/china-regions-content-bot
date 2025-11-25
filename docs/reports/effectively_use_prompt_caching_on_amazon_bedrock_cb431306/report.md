---
title: 在Amazon Bedrock上有效使用提示词缓存
publish_date: 2025-04-07
original_url: https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 2
unavailable_services: 1
---

# 在Amazon Bedrock上有效使用提示词缓存

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

Amazon Bedrock是本文的核心服务，整篇文章围绕Bedrock的prompt caching功能展开。该服务在AWS中国区域不可用，导致文章内容无法在中国区域实施。

## 服务分析

### 可用服务 (2个)

- Amazon CloudWatch
- Amazon S3

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务

### 评估说明

本文详细介绍了Amazon Bedrock的prompt caching功能，包括：
- 如何通过缓存频繁使用的提示词前缀来降低延迟（最高85%）和成本（最高90%）
- 适用场景：文档问答、代码助手、智能体工作流、少样本学习等
- 具体实现方法和代码示例
- 使用CloudWatch进行监控和可观测性

由于Amazon Bedrock在AWS中国区域完全不可用，文章中的所有核心功能、API调用、代码示例均无法在中国区域执行。虽然文章提到的CloudWatch监控服务在中国区域可用，但没有Bedrock服务本身，监控功能也失去了意义。

## 验证结果

### 验证类型

- ⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段评估为LOW等级，核心服务Amazon Bedrock在AWS中国区域不可用，不满足深入验证的触发条件（需要MODERATE或HIGH等级）。

## 实施建议

### 推荐方案

不建议在AWS中国区域实施本文内容。Amazon Bedrock作为核心服务在中国区域不可用，文章中介绍的所有功能特性、API接口、代码实现均依赖于该服务，无法在中国区域运行。

### 替代方案

目前AWS中国区域没有直接等效的托管生成式AI服务可以替代Amazon Bedrock。如需在中国区域实现类似的生成式AI应用，可考虑以下替代方案：

1. **自托管开源大语言模型**
   - 实施方式：在Amazon EC2或Amazon ECS上部署开源LLM（如Llama、ChatGLM等），自行实现prompt caching机制
   - 复杂度：高
   - 适用场景：有充足的技术团队和基础设施管理能力，对数据主权有严格要求

2. **使用Amazon SageMaker部署模型**
   - 实施方式：通过SageMaker部署和托管大语言模型，自行开发缓存层
   - 复杂度：高
   - 适用场景：需要更灵活的模型选择和定制化能力

3. **集成国内AI服务提供商**
   - 实施方式：集成国内云服务商提供的大语言模型API服务
   - 复杂度：中
   - 适用场景：快速实现生成式AI功能，但需要评估数据合规性

### 风险提示

- **服务不可用风险**: Amazon Bedrock在AWS中国区域完全不可用，无法使用文章中介绍的任何功能
- **架构重构风险**: 采用替代方案需要完全重新设计架构，开发工作量大
- **成本风险**: 自托管方案的基础设施成本和运维成本可能显著高于托管服务
- **技术复杂度**: 自行实现prompt caching等优化功能需要深厚的技术积累
- **合规风险**: 使用第三方AI服务需要仔细评估数据安全和合规要求

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/amazon-bedrock-samples/blob/main/introduction-to-bedrock/prompt-caching/getting_started_with_prompt_caching.ipynb
- **兼容性**: 不兼容AWS中国区域，代码依赖Amazon Bedrock服务
- **修改建议**: 无法通过简单修改使其在中国区域运行，需要完全替换底层服务
