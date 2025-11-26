---
title: 使用模型上下文协议（MCP）与Amazon Q Developer实现上下文感知的IDE工作流
publish_date: 2025-06-12
original_url: https://aws.amazon.com/blogs/devops/use-model-context-protocol-with-amazon-q-developer-for-context-aware-ide-workflows/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 0
unavailable_services: 1
---

# 使用模型上下文协议（MCP）与Amazon Q Developer实现上下文感知的IDE工作流

[📖 查看原始博客](https://aws.amazon.com/blogs/devops/use-model-context-protocol-with-amazon-q-developer-for-context-aware-ide-workflows/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

文章的核心服务Amazon Q Developer在AWS中国区域不可用，无法实施文章中描述的任何功能。

## 服务分析

### 可用服务 (0个)

无

### 不可用服务 (1个)

- **Amazon Q Developer** - 核心服务

### 评估说明

本文完全围绕Amazon Q Developer的模型上下文协议（MCP）支持功能展开，介绍如何在IDE（Visual Studio Code和JetBrains）中配置和使用MCP服务器，以实现与外部工具（如Jira和Figma）的集成。

**核心问题：**
1. Amazon Q Developer是文章的唯一核心服务，在AWS中国区域完全不可用
2. 文章中演示的所有功能（MCP配置、工具集成、代码生成等）都依赖于Amazon Q Developer
3. 没有等效的替代服务可以提供相同的MCP集成能力

**影响范围：**
- 无法在IDE中使用Amazon Q Developer插件
- 无法配置和使用MCP服务器
- 无法实现文章中描述的任何工作流程
- 配套的演示项目（Q Words game）虽然可以访问，但无法使用Q Developer进行开发

## 验证结果

### 验证类型

- ⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Q Developer在AWS中国区域不可用，可行性评估为LOW，无需进行深入验证。

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此方案**

由于Amazon Q Developer服务在中国区域完全不可用，文章中描述的所有功能和工作流程都无法实现。这不是配置或调整的问题，而是服务本身在该区域不存在。

### 替代方案

目前AWS中国区域没有直接等效的AI辅助开发工具。如果需要类似的AI编码辅助功能，可以考虑：

1. **使用第三方AI编码助手**
   - 实施方式：使用GitHub Copilot、Cursor等第三方工具
   - 复杂度：低
   - 适用场景：需要AI辅助编码但不依赖AWS生态系统的场景
   - 限制：无法与AWS服务深度集成，不支持MCP协议

2. **等待服务上线**
   - 实施方式：关注AWS中国区域服务更新公告
   - 复杂度：无
   - 适用场景：对Amazon Q Developer有强需求且可以等待的场景
   - 限制：服务上线时间不确定

### 风险提示

- **服务不可用**: Amazon Q Developer在AWS中国区域完全不可用，这是根本性限制
- **无替代方案**: AWS中国区域目前没有提供类似的AI开发助手服务
- **生态系统差异**: 第三方工具无法提供与AWS服务的深度集成

### 配套资源

- **Q Words game**: https://catalog.workshops.aws/qwords/en-US
  - 兼容性：游戏代码本身可以访问和运行，但无法使用Amazon Q Developer进行开发
  - 修改建议：不适用，因为核心问题是Q Developer服务不可用

- **AWS MCP Servers repository**: https://github.com/awslabs/mcp
  - 兼容性：代码仓库可以访问，但MCP服务器需要Amazon Q Developer才能使用
  - 修改建议：不适用，因为没有可用的客户端工具
