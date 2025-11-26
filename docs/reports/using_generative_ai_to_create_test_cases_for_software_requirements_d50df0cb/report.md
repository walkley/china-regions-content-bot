---
title: 使用生成式AI为软件需求创建测试用例
publish_date: 2025-01-13
original_url: https://aws.amazon.com/blogs/industries/using-generative-ai-to-create-test-cases-for-software-requirements/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 3
unavailable_services: 1
---

# 使用生成式AI为软件需求创建测试用例

[📖 查看原始博客](https://aws.amazon.com/blogs/industries/using-generative-ai-to-create-test-cases-for-software-requirements/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

该方案的核心服务Amazon Bedrock在AWS中国区域不可用，导致整个生成式AI测试用例自动生成功能无法实现。虽然其他基础设施服务（API Gateway、Lambda、DynamoDB）均可用，但缺少Bedrock使得方案失去核心价值。

## 服务分析

### 可用服务 (3个)

- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务

### 评估说明

本方案旨在通过生成式AI自动化汽车软件测试用例的创建过程，核心依赖Amazon Bedrock提供的大语言模型能力（文章中使用了Anthropic Claude模型）。

**核心服务可用性分析**：
- Amazon Bedrock是整个解决方案的AI引擎，负责需求分类和测试用例生成
- 没有Bedrock，方案的主要功能（AI驱动的测试用例自动生成）完全无法实现
- 虽然75%的服务可用，但这些服务仅提供基础设施支持，无法替代AI核心能力

**不可用服务的影响**：
- 无法使用大语言模型进行需求分类
- 无法自动生成测试用例描述
- 无法实现文章中提到的"减少80%测试用例创建时间"的效果
- 整个AI辅助工作流程无法建立

**替代方案可行性**：
- 中国区域暂无直接等效的AWS托管生成式AI服务
- 需要完全重新设计架构，使用第三方AI服务或自建模型

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段识别出核心服务Amazon Bedrock在中国区域不可用，初步可行性评估为LOW。根据验证流程，仅当评估结果为MODERATE或HIGH时才执行深入验证。由于核心AI功能无法实现，跳过深入验证阶段。

## 实施建议

### 推荐方案

**不建议在AWS中国区域直接实施此方案**

该方案的核心价值在于利用Amazon Bedrock的生成式AI能力自动化测试用例创建。由于Bedrock在中国区域不可用，方案的主要功能无法实现，失去了实施意义。

### 替代方案

如果确实需要在中国区域实现类似的AI辅助测试用例生成功能，可以考虑以下替代方案：

1. **使用第三方AI服务**
   - 实施方式：集成国内可用的大语言模型服务（如阿里云通义千问、百度文心一言等）替代Amazon Bedrock
   - 复杂度：高
   - 适用场景：对AI辅助测试用例生成有强需求，且愿意投入资源进行架构重新设计
   - 注意事项：需要重新设计API集成、提示工程、数据流程，并评估第三方服务的合规性和数据安全性

2. **自建模型部署方案**
   - 实施方式：在AWS中国区域使用Amazon SageMaker部署开源大语言模型（如Llama、ChatGLM等）
   - 复杂度：高
   - 适用场景：有较强的技术团队和预算，对数据隐私有严格要求
   - 注意事项：需要考虑模型训练/微调成本、推理性能优化、运维复杂度等因素

3. **混合云架构**
   - 实施方式：在AWS全球区域使用Bedrock处理AI请求，其他基础设施部署在中国区域
   - 复杂度：中
   - 适用场景：数据可以跨境传输，且对延迟不敏感
   - 注意事项：需要评估数据跨境合规性、网络延迟影响、以及跨区域数据传输成本

### 风险提示

- **核心功能缺失**: 无法使用Amazon Bedrock意味着方案的核心AI能力完全缺失
- **架构重构成本**: 任何替代方案都需要大量的架构重新设计和开发工作
- **合规性风险**: 使用第三方AI服务或跨境数据传输需要仔细评估数据合规性要求
- **成本不确定性**: 自建模型或使用第三方服务的成本结构与Bedrock差异较大，需要重新评估
- **技术复杂度**: 替代方案的实施和运维复杂度显著高于原方案

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 由于核心服务不可用，建议等待Amazon Bedrock在中国区域上线，或采用上述替代方案进行完全重新设计
