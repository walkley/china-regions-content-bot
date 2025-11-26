---
title: GitHub中的Amazon Q Developer（预览版）加速代码生成
publish_date: 2025-05-05
original_url: https://aws.amazon.com/blogs/aws/amazon-q-developer-in-github-now-in-preview-with-code-generation-review-and-legacy-transformation-capabilities/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 0
unavailable_services: 2
---

# GitHub中的Amazon Q Developer（预览版）加速代码生成

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/amazon-q-developer-in-github-now-in-preview-with-code-generation-review-and-legacy-transformation-capabilities/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

文章的核心服务Amazon Q Developer在AWS中国区域不可用，无法实现文章描述的功能。

## 服务分析

### 可用服务 (0个)

无

### 不可用服务 (2个)

- **Amazon Q Developer** - 核心服务
- **Amazon Bedrock** - 核心服务

### 评估说明

本文介绍的Amazon Q Developer是一个集成在GitHub中的AI辅助开发工具，用于：
1. 自动生成代码（Feature development）
2. 代码审查（Code review）
3. Java代码迁移（Code transformation）

核心问题：
1. **Amazon Q Developer不可用**：这是文章的核心主题，所有功能都依赖于此服务。该服务在AWS中国区域完全不可用。
2. **Amazon Bedrock不可用**：虽然只在示例应用中使用，但也在不可用列表中。
3. **无替代方案**：Amazon Q Developer是AWS专有的AI开发助手服务，在中国区域没有等效的AWS服务可以替代。

由于核心服务完全不可用，文章描述的所有功能（GitHub集成、自动代码生成、代码审查、Java迁移）都无法在AWS中国区域实现。

## 验证结果

### 验证类型

⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段发现核心服务Amazon Q Developer在AWS中国区域不可用，可行性评估为LOW。根据验证流程，仅当可行性为MODERATE或HIGH时才执行深入验证。

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此方案**

核心原因：
- Amazon Q Developer服务在AWS中国区域完全不可用
- 这是文章的核心主题，所有功能都依赖于此服务
- 无法通过配置调整或参数修改来解决

### 替代方案

由于Amazon Q Developer是AWS专有服务，在中国区域没有直接的AWS替代方案。如果需要类似的AI辅助开发功能，可以考虑：

1. **GitHub Copilot**
   - 实施方式：使用GitHub原生的AI编程助手
   - 复杂度：低
   - 适用场景：需要AI辅助代码生成和补全功能
   - 注意：这不是AWS服务，需要单独订阅GitHub Copilot

2. **本地IDE集成的AI工具**
   - 实施方式：使用JetBrains AI Assistant、VS Code扩展等
   - 复杂度：低
   - 适用场景：在本地开发环境中需要AI辅助
   - 注意：这些是第三方工具，不是AWS服务

3. **自建AI辅助开发方案**
   - 实施方式：使用中国区可用的AI服务（如果有）构建自定义开发助手
   - 复杂度：高
   - 适用场景：有专门的开发团队和预算
   - 注意：需要大量开发工作，且功能可能无法完全对标

### 风险提示

- **服务不可用**：Amazon Q Developer在AWS中国区域完全不可用，这是无法绕过的限制
- **无AWS替代方案**：AWS在中国区域没有提供类似的AI开发助手服务
- **功能缺失**：文章描述的所有功能（GitHub集成、自动代码生成、代码审查、Java迁移）都无法实现

### 配套资源

- **GitHub仓库**: 文章中提到的是作者个人演示项目（storybook-teller-demo），不是AWS官方配套代码仓库
- **兼容性**: 不适用 - 核心服务不可用
- **修改建议**: 不适用 - 无法通过修改实现兼容
