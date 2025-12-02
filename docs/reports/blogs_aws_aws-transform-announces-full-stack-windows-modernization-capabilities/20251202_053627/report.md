---
title: AWS Transform 宣布推出全栈 Windows 现代化功能
publish_date: 2025-12-01
original_url: https://aws.amazon.com/blogs/aws/aws-transform-announces-full-stack-windows-modernization-capabilities/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 6
unavailable_services: 2
---

# AWS Transform 宣布推出全栈 Windows 现代化功能

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/aws-transform-announces-full-stack-windows-modernization-capabilities/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务 AWS Transform 在中国区域不可用，无法按照原文方案实施

文章介绍的 AWS Transform 全栈 Windows 现代化服务是本方案的核心，该服务目前仅在美国东部（弗吉尼亚北部）区域可用，在中国区域（北京和宁夏）均不可用。虽然文章中提到的其他支持服务（如 Aurora PostgreSQL、EC2、ECS、DMS 等）在中国区域都可用，但缺少核心的 AWS Transform 服务，无法实现文章中描述的自动化现代化流程。

## 服务分析

### 可用服务 (6个)

- Amazon Aurora PostgreSQL-Compatible Edition
- Amazon EC2
- Amazon ECS
- AWS CloudFormation
- Amazon RDS
- AWS Database Migration Service (AWS DMS)

### 不可用服务 (2个)

- **AWS Transform** - 核心服务，文章的主要功能依赖
- **AWS Toolkit for Visual Studio** - 开发工具，可能在中国区使用受限

### 评估说明

AWS Transform 是本文介绍的核心服务，用于自动化完成以下关键功能：

1. **应用程序现代化**：将 .NET Framework 应用迁移到跨平台 .NET
2. **UI 框架升级**：将 ASP.NET Web Forms 转换为 Blazor
3. **数据库迁移**：将 SQL Server 迁移到 Aurora PostgreSQL，包括存储过程转换
4. **依赖关系分析**：自动识别应用和数据库之间的依赖关系
5. **波次编排**：协调多层应用的现代化过程

虽然数据库迁移所需的 AWS DMS、目标数据库 Aurora PostgreSQL、以及部署所需的 EC2 和 ECS 等服务在中国区域都可用，但缺少 AWS Transform 这个核心的 AI 驱动自动化服务，意味着无法使用文章中描述的简化流程和自动化能力。

## 验证结果

### 验证类型

- ⏭️ 已跳过（核心服务不可用）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: AWS Transform 服务在中国区域不可用，无法进行实际部署验证。该服务是实现文章中所有功能的前提条件。

## 实施建议

### 推荐方案

**不建议直接实施**

由于 AWS Transform 服务在中国区域不可用，无法按照文章描述的方式实施全栈 Windows 现代化。企业如需在中国区域进行类似的现代化工作，需要采用传统的手动迁移方法。

### 替代方案

如果确实需要在中国区域进行 Windows 应用现代化，可以考虑以下手动方案：

1. **手动 .NET 应用迁移**
   - 实施方式：使用 .NET Upgrade Assistant 等开源工具手动迁移 .NET Framework 应用到 .NET 6/8/10
   - 复杂度：高
   - 适用场景：有经验的 .NET 开发团队，应用规模较小
   - 局限性：缺少 AI 辅助，需要大量人工工作

2. **手动数据库迁移**
   - 实施方式：
     - 使用 AWS DMS 进行数据迁移（中国区可用）
     - 使用 AWS Schema Conversion Tool (SCT) 进行架构转换
     - 手动重写或调整存储过程以适配 PostgreSQL
   - 复杂度：高
   - 适用场景：数据库结构相对简单，存储过程数量有限
   - 局限性：存储过程转换需要大量手动工作，容易出错

3. **手动 UI 框架升级**
   - 实施方式：手动将 ASP.NET Web Forms 重写为 Blazor 或其他现代框架
   - 复杂度：非常高
   - 适用场景：有充足预算和时间的重构项目
   - 局限性：工作量巨大，可能需要完全重写 UI 层

4. **分阶段迁移策略**
   - 实施方式：
     - 第一阶段：在全球区域使用 AWS Transform 完成转换
     - 第二阶段：将转换后的代码和数据库部署到中国区域
   - 复杂度：中
   - 适用场景：应用需要同时在全球和中国区域运行
   - 注意事项：需要考虑数据合规性和跨境传输限制

### 风险提示

- **服务可用性风险**：AWS Transform 目前仅在美国东部（弗吉尼亚北部）区域可用，短期内在中国区域上线的可能性未知
- **手动迁移风险**：手动进行应用现代化工作量大、周期长、容易出错，需要有经验的技术团队
- **成本风险**：手动迁移需要投入大量人力资源，成本可能远高于使用自动化工具
- **测试复杂度**：缺少 AWS Transform 的自动化部署和测试能力，需要自行搭建完整的测试环境
- **依赖关系管理**：手动识别和管理应用与数据库之间的依赖关系容易遗漏，可能导致迁移后的兼容性问题
- **数据合规性**：如果考虑在全球区域使用 AWS Transform 后再迁移到中国区域，需要确保符合数据本地化和跨境传输的合规要求

### 配套资源

- **GitHub仓库**: 文章未提供配套的 GitHub 项目
- **相关文档**: 
  - [AWS DMS 用户指南](https://docs.aws.amazon.com/dms/)（中国区可用）
  - [.NET Upgrade Assistant](https://dotnet.microsoft.com/platform/upgrade-assistant)（开源工具）
  - [AWS Schema Conversion Tool](https://aws.amazon.com/dms/schema-conversion-tool/)
