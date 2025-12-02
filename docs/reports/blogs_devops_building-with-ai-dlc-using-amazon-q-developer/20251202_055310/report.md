---
title: 使用 Amazon Q Developer 构建 AI-DLC 应用
publish_date: 2025-11-29
original_url: https://aws.amazon.com/blogs/devops/building-with-ai-dlc-using-amazon-q-developer/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 0
unavailable_services: 1
---

# 使用 Amazon Q Developer 构建 AI-DLC 应用

[📖 查看原始博客](https://aws.amazon.com/blogs/devops/building-with-ai-dlc-using-amazon-q-developer/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务 Amazon Q Developer 在中国区域不可用，无法按照原文实施

文章的核心依赖服务 Amazon Q Developer 目前在 AWS 中国区域（宁夏和北京）均不可用。整个 AI-DLC（AI-Driven Development Life Cycle）工作流程完全基于 Amazon Q Developer 的 Project Rules 功能实现，没有该服务无法完成文章中描述的任何开发流程。

## 服务分析

### 可用服务 (0个)

无

### 不可用服务 (1个)

- **Amazon Q Developer** - 核心服务，文章的全部实现依赖此服务

### 评估说明

Amazon Q Developer 是一个生成式 AI 编码助手，支持整个软件开发生命周期。文章详细介绍了如何使用其 Project Rules 功能来实现 AI-DLC 工作流程。

该服务目前在 AWS 中国区域（cn-north-1 北京区域和 cn-northwest-1 宁夏区域）均不可用。通过 API 调用验证，Bedrock 服务（Amazon Q Developer 的底层服务）在中国区域的端点无法连接。

由于整个教程从环境设置、工作流程触发、需求分析、代码生成到测试部署的每个步骤都完全依赖 Amazon Q Developer，因此在中国区域无法实施本文描述的任何功能。

## 验证结果

### 验证类型

⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务 Amazon Q Developer 在中国区域完全不可用，无法进行实际部署验证。根据验证规则，可行性等级为 LOW 时跳过深入验证。

## 实施建议

### 推荐方案

**不建议在 AWS 中国区域实施此方案**

Amazon Q Developer 是本文的唯一核心服务，目前在中国区域不可用。文章介绍的 AI-DLC 工作流程完全依赖于：

1. Amazon Q Developer IDE 插件或 Kiro CLI
2. Amazon Q Developer 的 Project Rules 功能
3. Amazon Q Developer 的代码生成和分析能力

这些功能在中国区域均无法使用。

### 替代方案

虽然无法直接使用 Amazon Q Developer，但可以考虑以下替代思路：

1. **使用全球区域的 Amazon Q Developer**
   - 实施方式：在 AWS 全球区域（如 us-east-1）使用 Amazon Q Developer 进行开发
   - 复杂度：低
   - 适用场景：开发环境可以访问全球区域，仅生产环境在中国区域部署
   - 限制：需要网络访问全球区域，可能存在延迟和合规性考虑

2. **使用其他 AI 编码助手**
   - 实施方式：使用 GitHub Copilot、Cursor、Codeium 等第三方 AI 编码助手
   - 复杂度：中
   - 适用场景：需要 AI 辅助开发但不强制使用 AWS 服务
   - 限制：无法使用 AI-DLC 工作流程的 Project Rules 功能，需要手动管理开发流程

3. **使用 Amazon Bedrock（全球区域）+ 自定义工作流**
   - 实施方式：在全球区域使用 Amazon Bedrock API，自行实现类似 AI-DLC 的工作流程
   - 复杂度：高
   - 适用场景：需要完全自定义的 AI 辅助开发流程
   - 限制：需要大量开发工作，且 Bedrock 在中国区域也不可用

### 风险提示

- **服务不可用风险**: Amazon Q Developer 在中国区域的上线时间未知，短期内无法使用
- **合规性风险**: 使用全球区域服务需要考虑数据出境和合规性要求
- **网络访问风险**: 访问全球区域服务可能受到网络限制，影响开发体验
- **成本风险**: 跨区域数据传输可能产生额外费用

### 配套资源

- **GitHub仓库**: https://github.com/awslabs/aidlc-workflows
- **兼容性**: 仓库中的 AI-DLC 工作流程规则文件可以下载，但需要 Amazon Q Developer 才能使用
- **修改建议**: 无法通过修改使其在中国区域工作，因为依赖的核心服务不可用

## 总结

本文介绍的 AI-DLC 方法论和工作流程理念很有价值，但由于完全依赖 Amazon Q Developer 服务，目前无法在 AWS 中国区域实施。建议关注 Amazon Q Developer 在中国区域的上线计划，或考虑使用其他 AI 编码助手实现类似的开发流程。
