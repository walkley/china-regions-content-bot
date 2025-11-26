---
title: 介绍AWS SimuLearn：生成式AI从业者课程
publish_date: 2025-05-20
original_url: https://aws.amazon.com/blogs/training-and-certification/introducing-aws-simulearn-generative-ai-practitioner/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 1
unavailable_services: 4
---

# 介绍AWS SimuLearn：生成式AI从业者课程

[📖 查看原始博客](https://aws.amazon.com/blogs/training-and-certification/introducing-aws-simulearn-generative-ai-practitioner/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

该学习计划的核心服务Amazon Bedrock及其相关模型（Amazon Titan、Amazon Nova）在AWS中国区域均不可用，Amazon Q服务也不可用。由于这是一个专门针对这些服务的培训课程，无法在中国区域实施。

## 服务分析

### 可用服务 (1个)

- Amazon SageMaker

### 不可用服务 (4个)

- **Amazon Bedrock** - 核心服务
- **Amazon Q** - 核心服务
- **Amazon Titan** - 核心服务（Bedrock模型）
- **Amazon Nova** - 核心服务（Bedrock模型）

### 评估说明

本文介绍的AWS SimuLearn生成式AI从业者学习计划是一个培训课程，其核心内容围绕Amazon Bedrock、Amazon Q、Amazon Titan和Amazon Nova等生成式AI服务展开。这些服务在AWS中国区域均不可用，导致：

1. **核心服务完全不可用**：Amazon Bedrock是课程的核心技术平台，在中国区不可用
2. **学习内容无法实践**：课程中涉及的Amazon Titan、Amazon Nova模型都依赖于Bedrock
3. **辅助工具缺失**：Amazon Q作为AI助手工具也不可用
4. **可用率极低**：仅20%的服务可用，且唯一可用的Amazon SageMaker并非课程的主要内容

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段评估为LOW可行性，核心服务Amazon Bedrock及相关模型在中国区域不可用，且本文为培训课程介绍而非技术实施指南，不具备实际部署验证的条件。

## 实施建议

### 推荐方案

不建议在AWS中国区域实施此学习计划。该课程专门针对Amazon Bedrock、Amazon Q等生成式AI服务设计，这些服务在中国区域均不可用，课程内容无法在中国区域环境中实践和学习。

### 替代方案

1. **使用Amazon SageMaker的生成式AI功能**
   - 实施方式：利用Amazon SageMaker部署开源大语言模型（如Llama、Mistral等）
   - 复杂度：高
   - 适用场景：需要自行管理模型部署、推理和优化，适合有较强技术能力的团队

2. **关注AWS中国区域的生成式AI服务更新**
   - 实施方式：等待Amazon Bedrock等服务在中国区域上线
   - 复杂度：低
   - 适用场景：不急于立即实施，可以等待服务正式支持

3. **参考全球区域的学习资源**
   - 实施方式：在全球区域（如us-east-1）注册AWS账号进行学习
   - 复杂度：低
   - 适用场景：仅用于学习和培训目的，不涉及生产环境部署

### 风险提示

- **服务不可用风险**：核心服务Amazon Bedrock在中国区域不可用，无法完成课程的实践环节
- **学习效果受限**：无法在实际环境中验证所学知识，影响学习效果
- **投入产出比低**：即使学习了相关知识，也无法在中国区域的生产环境中应用

### 配套资源

- **课程链接**: https://explore.skillbuilder.aws/learn/learning-plans/2451/plan
- **兼容性**: 不兼容AWS中国区域
- **说明**: 该学习计划需要在支持Amazon Bedrock的AWS区域（如美国、欧洲等全球区域）进行学习和实践
