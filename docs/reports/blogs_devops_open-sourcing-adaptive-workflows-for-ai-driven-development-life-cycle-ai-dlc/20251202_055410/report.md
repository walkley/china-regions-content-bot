---
title: 开源AI驱动开发生命周期（AI-DLC）的自适应工作流
publish_date: 2025-11-29
original_url: https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 0
unavailable_services: 2
---

# 开源AI驱动开发生命周期（AI-DLC）的自适应工作流

[📖 查看原始博客](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Q Developer在中国区域不可用，无法直接实施

本文介绍的AI-DLC工作流完全依赖Amazon Q Developer和Kiro作为执行引擎，这两个服务目前在AWS中国区域均不可用，因此无法按照原文方式实施。

## 服务分析

### 可用服务 (0个)

无

### 不可用服务 (2个)

- **Amazon Q Developer** - 核心服务
- **Kiro** - 核心服务（Amazon Q Developer的CLI版本）

### 评估说明

本文的核心内容是介绍AI-DLC（AI驱动开发生命周期）方法论，并提供基于Amazon Q Developer Rules和Kiro Steering Files的开源实现。分析如下：

1. **核心服务不可用**：Amazon Q Developer是AWS的生成式AI编码助手服务，依赖于Amazon Bedrock基础设施。经验证，Bedrock服务在中国区域（cn-northwest-1）不可用，因此Amazon Q Developer及其CLI版本Kiro也无法使用。

2. **完全依赖性**：文章介绍的工作流规则（Rules）和引导文件（Steering Files）是专门为Amazon Q Developer设计的，没有这些服务作为执行引擎，开源的工作流定义无法运行。

3. **无直接替代方案**：虽然AI-DLC的方法论思想（自适应工作流、灵活深度、人机协作）具有普遍价值，但其技术实现与Amazon Q Developer深度绑定，在中国区域缺乏等效的AWS服务替代。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Q Developer在中国区域不可用，无法进行实际部署验证。即使下载GitHub项目，也无法在中国区域的AWS环境中运行。

## 实施建议

### 推荐方案

**不建议在AWS中国区域直接实施**

由于Amazon Q Developer服务在中国区域不可用，无法使用本文介绍的开源工作流实现。但AI-DLC的方法论思想仍具有参考价值。

### 替代方案

1. **方案1：使用全球区域的Amazon Q Developer**
   - 实施方式：在AWS全球区域（如us-east-1）使用Amazon Q Developer和AI-DLC工作流
   - 复杂度：低
   - 适用场景：团队可以访问AWS全球区域，且对数据驻留没有严格要求

2. **方案2：借鉴方法论，使用其他AI编码工具**
   - 实施方式：学习AI-DLC的核心原则（自适应工作流、灵活深度、人机协作），在其他AI编码助手（如GitHub Copilot、Claude等）中通过提示工程实现类似理念
   - 复杂度：高
   - 适用场景：需要在中国区域工作，但希望应用AI-DLC的方法论思想

3. **方案3：等待服务在中国区域上线**
   - 实施方式：关注AWS中国区域的服务更新，等待Amazon Q Developer正式支持
   - 复杂度：低
   - 适用场景：对AI编码助手没有紧急需求，可以等待官方支持

### 风险提示

- **服务可用性风险**：Amazon Q Developer在中国区域的上线时间未知，短期内无法使用
- **数据合规风险**：如果选择使用全球区域服务，需要评估代码和数据跨境传输的合规性要求
- **工具依赖风险**：AI-DLC工作流与Amazon Q Developer深度集成，迁移到其他工具需要重新设计实现
- **学习成本**：如果采用替代方案2，需要投入大量时间理解AI-DLC原理并在其他平台重新实现

### 配套资源

- **GitHub仓库**: https://github.com/awslabs/aidlc-workflows
- **兼容性**: 仓库中的Rules和Steering Files专为Amazon Q Developer设计，在中国区域无法直接使用
- **修改建议**: 
  - 可以研究工作流定义的结构和逻辑，作为方法论学习材料
  - 如果未来Amazon Q Developer在中国区域上线，可以直接使用这些配置文件
  - 当前阶段，这些文件更适合作为设计参考，而非可执行代码

### 方法论价值

虽然技术实现无法在中国区域使用，但AI-DLC提出的核心理念仍值得学习：

1. **自适应工作流**：根据项目类型（新功能、缺陷修复、重构等）动态选择开发阶段，避免"一刀切"流程
2. **灵活深度**：根据任务复杂度调整每个阶段的详细程度，避免过度工程或不足
3. **人机协作**：在AI自动化的同时，强调人类在关键决策点的审查和验证作用

这些原则可以应用于任何AI辅助开发实践，不局限于特定工具。
