---
title: 掌握Amazon Q Developer规则功能
publish_date: 2025-08-28
original_url: https://aws.amazon.com/blogs/devops/mastering-amazon-q-developer-with-rules/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 0
unavailable_services: 1
---

# 掌握Amazon Q Developer规则功能

[📖 查看原始博客](https://aws.amazon.com/blogs/devops/mastering-amazon-q-developer-with-rules/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，无法在中国区域实施

本文完全围绕Amazon Q Developer的自定义规则功能展开，而该服务在AWS中国区域不可用，因此无法实施文章中介绍的任何功能。

## 服务分析

### 可用服务 (0个)

无

### 不可用服务 (1个)

- **Amazon Q Developer** - 核心服务

### 评估说明

Amazon Q Developer是本文唯一涉及的AWS服务，也是文章的核心主题。该服务目前在AWS中国区域（北京和宁夏）均不可用。

文章详细介绍了如何使用Amazon Q Developer的自定义规则功能来：
- 定义团队编码标准和最佳实践
- 创建可重用的AI助手上下文
- 提高开发团队的一致性和效率
- 通过规则文件（.amazonq/rules目录）自动化AI交互

由于核心服务完全不可用，文章中的所有功能、示例和最佳实践都无法在中国区域实施。

## 验证结果

### 验证类型

⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Q Developer在AWS中国区域不可用，无法进行实际验证

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此方案**

Amazon Q Developer是本文的唯一核心服务，该服务在中国区域完全不可用。文章介绍的所有功能（自定义规则、IDE集成、CLI支持等）都依赖于Amazon Q Developer服务。

### 替代方案

目前没有AWS原生的直接替代方案。如果需要类似的AI辅助开发功能，可以考虑：

1. **第三方AI编码助手**
   - 实施方式：使用GitHub Copilot、Cursor等第三方AI开发工具
   - 复杂度：低
   - 适用场景：需要AI辅助编码但不强制要求AWS原生集成的团队

2. **自建提示词管理系统**
   - 实施方式：创建团队共享的提示词库和编码标准文档，配合通用AI工具使用
   - 复杂度：中
   - 适用场景：希望标准化AI交互但可以接受手动管理的团队

3. **等待服务上线**
   - 实施方式：关注AWS中国区域服务更新公告
   - 复杂度：无
   - 适用场景：可以等待AWS官方在中国区域推出该服务的团队

### 风险提示

- **服务不可用**: Amazon Q Developer在中国区域完全不可用，无上线时间表
- **无直接替代**: AWS在中国区域没有提供功能相似的原生AI开发助手服务
- **第三方依赖**: 使用第三方AI工具可能涉及数据隐私和合规性考虑
- **功能差异**: 第三方工具无法提供与AWS服务的深度集成

### 配套资源

本文没有配套的GitHub项目，主要是概念和最佳实践的介绍。
