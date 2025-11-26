---
title: AWS Transform for .NET：首个用于大规模现代化.NET应用程序的代理式AI服务
publish_date: 2025-05-15
original_url: https://aws.amazon.com/blogs/aws/aws-transform-for-net-the-first-agentic-ai-service-for-modernizing-net-applications-at-scale/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 0
unavailable_services: 2
---

# AWS Transform for .NET：首个用于大规模现代化.NET应用程序的代理式AI服务

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/aws-transform-for-net-the-first-agentic-ai-service-for-modernizing-net-applications-at-scale/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务在中国区不可用，无法实施

博客介绍的AWS Transform for .NET和Amazon Q Developer均不在中国区域提供服务，这两个服务是实现.NET应用程序现代化转换的核心组件，缺少它们将无法实施博客中描述的任何功能。

## 服务分析

### 可用服务 (0个)

无

### 不可用服务 (2个)

- **AWS Transform for .NET** - 核心服务
- **Amazon Q Developer** - 核心服务

### 评估说明

AWS Transform for .NET是本文的核心主题，它是一个基于代理式AI的服务，用于将.NET Framework应用程序自动迁移到跨平台的.NET版本。该服务提供两种使用方式：

1. **Web体验**：用于大规模转换企业中的数百个应用程序，可以连接到GitHub、GitLab和Bitbucket等源代码仓库
2. **Visual Studio IDE扩展**：用于单个项目和解决方案的迁移

该服务依赖于Amazon Q Developer的AI能力来实现代码分析、兼容性检测、代码转换、单元测试执行等功能。由于这两个核心服务都不在中国区域提供，博客中描述的所有功能都无法在中国区域实现。

博客中提到的主要功能包括：
- 自动检测和转换.NET Framework代码到.NET 8
- 支持私有NuGet包依赖
- 自动迁移MVC Razor视图到ASP.NET Core
- 执行单元测试并生成转换报告
- 跨仓库依赖分析和自动转换

所有这些功能都完全依赖于AWS Transform for .NET服务，没有可行的替代方案。

## 验证结果

### 验证类型

⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务AWS Transform for .NET和Amazon Q Developer在中国区域不可用，可行性评估为LOW，不满足深入验证的触发条件。

## 实施建议

### 推荐方案

**不建议在中国区域实施此方案**

AWS Transform for .NET是一个完全托管的AI服务，其核心功能无法通过其他AWS服务或开源工具替代。该服务的价值在于：

1. **代理式AI能力**：利用大语言模型理解代码语义并进行智能转换
2. **大规模自动化**：可以同时处理数百个仓库的转换工作
3. **深度集成**：与源代码仓库、构建系统、测试框架深度集成

这些能力都依赖于AWS的专有AI服务和基础设施，无法在中国区域复制。

### 替代方案

对于需要在中国区域进行.NET应用程序现代化的场景，可以考虑以下传统方法：

1. **手动迁移配合工具辅助**
   - 实施方式：使用Microsoft提供的.NET Upgrade Assistant、Portability Analyzer等开源工具进行辅助分析，然后手动完成代码迁移
   - 复杂度：高
   - 适用场景：应用程序数量较少（<10个），有经验丰富的.NET开发团队

2. **分阶段迁移策略**
   - 实施方式：先迁移业务逻辑层到.NET Core/8，保留UI层在.NET Framework，逐步完成全栈迁移
   - 复杂度：中
   - 适用场景：大型单体应用，需要降低迁移风险

3. **容器化现有应用**
   - 实施方式：将现有.NET Framework应用容器化运行在Windows容器中，暂不进行代码级别的迁移
   - 复杂度：低
   - 适用场景：短期内需要云化但无法投入大量资源进行代码迁移

### 风险提示

- **人力成本高**：没有AI辅助的自动化转换，需要投入大量开发人员进行手动迁移
- **周期长**：大规模应用组合的迁移可能需要数月甚至数年时间
- **质量风险**：手动迁移容易引入错误，需要充分的测试覆盖
- **技能要求**：需要团队同时熟悉.NET Framework和现代.NET平台

### 配套资源

本文没有提供配套的GitHub项目，主要介绍的是AWS托管服务的使用方法。
