---
title: AWS Transform for mainframe 推出重构能力和自动化测试功能
publish_date: 2025-12-01
original_url: https://aws.amazon.com/blogs/aws/aws-transform-for-mainframe-introduces-reimagine-capabilities-and-automated-testing-functionality/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 1
unavailable_services: 1
---

# AWS Transform for mainframe 推出重构能力和自动化测试功能

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/aws-transform-for-mainframe-introduces-reimagine-capabilities-and-automated-testing-functionality/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务 AWS Transform for mainframe 在中国区域不可用，无法实施文章中的任何功能

文章完全围绕 AWS Transform for mainframe 服务展开，介绍其新推出的 Reimagine 重构能力和自动化测试功能。由于该服务在中国区域不可用，文章中描述的所有操作步骤、功能特性和使用场景均无法在中国区域实现。

## 服务分析

### 可用服务 (1个)

- Amazon S3 (Amazon Simple Storage Service)

### 不可用服务 (1个)

- **AWS Transform for mainframe** - 核心服务

### 评估说明

AWS Transform for mainframe 是本文的唯一核心服务，文章详细介绍了该服务的以下功能：

1. **Reimagine 重构模式**：使用 AI 驱动的分析将大型机应用程序完全重构为现代架构模式（如微服务）
2. **自动化测试功能**：
   - 自动生成测试计划
   - 生成测试数据收集脚本
   - 生成测试自动化脚本
3. **数据分析能力**：
   - 数据血缘分析
   - 自动化数据字典生成
4. **支持的大型机技术栈**：COBOL、CICS、DB2、VSAM、JCL 等

经过验证，AWS CLI 在中国区域（cn-northwest-1）不支持 `transform` 服务命令，确认该服务未在中国区域上线。虽然文章中提到使用 Amazon S3 存储代码库和文档，但 S3 仅作为辅助存储，无法替代 AWS Transform 的核心功能。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为 LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务 AWS Transform for mainframe 在中国区域不可用，无法进行任何实际验证。该服务是文章的唯一主题，没有该服务就无法执行文章中描述的任何操作步骤。

## 实施建议

### 推荐方案

**LOW等级**:
- 不建议在中国区域实施此方案
- AWS Transform for mainframe 是一个专门的大型机现代化服务，目前仅在全球区域提供
- 文章中的所有功能（Reimagine 重构、自动化测试、数据分析等）都完全依赖该服务

### 替代方案

对于在中国区域有大型机现代化需求的客户，可以考虑以下替代方案：

1. **使用全球区域的 AWS Transform 服务**
   - 实施方式：在全球区域（如 us-east-1）使用 AWS Transform 进行大型机现代化分析和代码转换，然后将生成的现代化应用部署到中国区域
   - 复杂度：中
   - 适用场景：源代码和业务逻辑可以在全球区域处理，最终应用需要在中国区域运行
   - 注意事项：需要考虑数据合规性和跨境传输要求

2. **传统大型机迁移方法**
   - 实施方式：使用传统的人工分析和代码重写方法，结合 AWS 中国区域的计算、存储和数据库服务
   - 复杂度：高
   - 适用场景：对数据本地化有严格要求，无法使用全球区域服务
   - 可用服务：Amazon EC2、Amazon RDS、Amazon S3、AWS Lambda 等基础服务

3. **第三方迁移工具**
   - 实施方式：使用第三方大型机现代化工具和咨询服务，配合 AWS 中国区域的基础设施
   - 复杂度：高
   - 适用场景：需要完整的本地化解决方案

### 风险提示

- **服务不可用风险**: AWS Transform for mainframe 在中国区域没有上线计划的公开信息，短期内无法使用
- **数据合规风险**: 如果选择使用全球区域的 AWS Transform 服务，需要评估大型机源代码和业务数据的跨境传输合规性
- **成本和时间风险**: 传统迁移方法相比 AI 驱动的 AWS Transform 服务，需要更多的人力投入和更长的项目周期（从数月延长到数年）
- **技术复杂度风险**: 大型机现代化本身就是高度复杂的项目，缺少 AWS Transform 的自动化能力会显著增加技术难度

### 配套资源

- **GitHub仓库**: 文章未提供配套的 GitHub 项目
- **相关文档**: 
  - [AWS Transform 产品页面](https://aws.amazon.com/transform/mainframe/)（全球区域）
  - [AWS Transform 用户指南](https://docs.aws.amazon.com/transform/latest/userguide/)（全球区域）
  - [AWS 区域服务列表](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)
