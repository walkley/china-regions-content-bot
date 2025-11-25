---
title: Amazon SageMaker Unified Studio 中的一键式入门和内置 AI 代理的笔记本
publish_date: 2025-11-21
original_url: https://aws.amazon.com/blogs/aws/new-one-click-onboarding-and-notebooks-with-ai-agent-in-amazon-sagemaker-unified-studio/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 9
unavailable_services: 2
---

# Amazon SageMaker Unified Studio 中的一键式入门和内置 AI 代理的笔记本

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/new-one-click-onboarding-and-notebooks-with-ai-agent-in-amazon-sagemaker-unified-studio/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务 Amazon SageMaker Unified Studio（基于 Amazon DataZone）在中国区域不可用，无法实施

本博客介绍的 Amazon SageMaker Unified Studio 是一个统一的数据和 AI 工作平台，但其底层核心服务 Amazon DataZone 在 AWS 中国区域（cn-northwest-1 和 cn-north-1）均不可用，导致整个解决方案无法在中国区域实施。

## 服务分析

### 可用服务 (9个)

- Amazon SageMaker
- AWS Identity and Access Management (IAM)
- AWS Glue Data Catalog
- AWS Lake Formation
- Amazon S3
- Amazon Athena
- Amazon Redshift
- AWS Glue Spark
- Amazon Managed Workflows for Apache Airflow (MWAA)

### 不可用服务 (2个)

- **Amazon SageMaker Unified Studio** - 核心服务（基于 Amazon DataZone）
- **Amazon S3 Tables** - 核心功能

### 评估说明

通过深入验证发现：

1. **核心服务不可用**：Amazon SageMaker Unified Studio 依赖于 Amazon DataZone 服务作为底层基础设施。经过实际测试，DataZone 服务在 cn-northwest-1 和 cn-north-1 两个中国区域均无法连接，返回 EndpointConnectionError 错误。

2. **功能完全依赖**：博客中介绍的所有核心功能（一键式入门、统一项目管理、内置 AI 代理的笔记本、Query Editor 等）都是 SageMaker Unified Studio 的专属功能，无法通过其他服务替代。

3. **相关服务可用**：虽然 SageMaker、Glue、Athena、Lake Formation 等底层服务在中国区域可用，但它们无法提供 Unified Studio 的统一体验和集成功能。

4. **S3 Tables 不可用**：博客中提到的 Amazon S3 Tables 功能也在中国区域不可用，进一步限制了数据管理能力。

## 验证结果

### 验证类型

- ✅ 深入验证（服务可用性测试）

### 执行状态

**状态**: ❌ 失败

**原因**: 核心服务 Amazon DataZone（SageMaker Unified Studio 的底层服务）在 AWS 中国区域完全不可用

### 关键发现

1. **Amazon DataZone 服务不可用**
   - 在 cn-northwest-1 和 cn-north-1 区域均无法连接到 DataZone 服务端点
   - 错误信息：`Could not connect to the endpoint URL: "https://datazone.cn-northwest-1.api.amazonwebservices.com.cn/v2/domains"`
   - 影响：无法创建 SageMaker Unified Studio 域和项目

2. **Amazon S3 Tables 服务不可用**
   - S3 Tables 是博客中提到的数据管理功能之一
   - 该服务在中国区域无法使用
   - 影响：无法使用 S3 Tables 的表格式数据管理功能

3. **相关服务验证成功**
   - AWS Glue Data Catalog：✓ 可用
   - Amazon Athena：✓ 可用
   - AWS Lake Formation：✓ 可用
   - Amazon MWAA：✓ 可用
   - Amazon SageMaker（传统功能）：✓ 可用

## 实施建议

### 推荐方案

**不建议在 AWS 中国区域实施此解决方案**

由于 Amazon SageMaker Unified Studio 是一个完整的统一平台，其核心架构依赖于 Amazon DataZone 服务，而该服务在中国区域不可用，因此无法实施博客中介绍的任何功能，包括：

- ❌ 一键式入门（One-click onboarding）
- ❌ 统一的项目和数据管理
- ❌ 内置 AI 代理的笔记本
- ❌ 从 Athena、Redshift、S3 Tables 控制台直接启动
- ❌ Query Editor 集成体验
- ❌ 自动化的权限管理和数据访问控制

### 替代方案

虽然无法使用 SageMaker Unified Studio，但可以通过组合使用中国区域可用的服务来实现部分类似功能：

1. **数据分析和查询**
   - 实施方式：使用 Amazon Athena + AWS Glue Data Catalog 进行数据查询和分析
   - 复杂度：中
   - 适用场景：SQL 查询、数据探索、临时分析
   - 限制：缺少统一的项目管理和协作功能

2. **机器学习开发**
   - 实施方式：使用传统的 Amazon SageMaker Notebook Instances 或 SageMaker Studio（非 Unified Studio）
   - 复杂度：中
   - 适用场景：机器学习模型开发、训练和部署
   - 限制：没有内置 AI 代理辅助编码，需要手动编写代码

3. **数据权限管理**
   - 实施方式：使用 AWS Lake Formation 管理数据湖权限
   - 复杂度：中到高
   - 适用场景：细粒度的数据访问控制
   - 限制：需要手动配置，没有自动化的项目级权限继承

4. **ETL 和数据处理**
   - 实施方式：使用 AWS Glue ETL 作业或 AWS Glue Studio
   - 复杂度：中
   - 适用场景：数据转换、清洗和准备
   - 限制：缺少可视化工作流编排

5. **工作流编排**
   - 实施方式：使用 Amazon MWAA（Apache Airflow）或 AWS Step Functions
   - 复杂度：中到高
   - 适用场景：复杂的数据管道和工作流自动化
   - 限制：需要编写 DAG 代码，学习曲线较陡

### 风险提示

- **功能差距**：替代方案无法提供 SageMaker Unified Studio 的统一体验，需要在多个服务之间切换，增加操作复杂度
- **协作限制**：缺少统一的项目管理和团队协作功能，需要通过 IAM 和其他机制手动管理
- **AI 辅助缺失**：没有内置的 AI 代理来辅助代码生成和数据分析，开发效率较低
- **学习成本**：需要分别学习和配置多个服务，而不是使用一个统一平台
- **维护复杂度**：需要单独管理和维护多个服务的配置和集成

### 配套资源

- **GitHub仓库**: 无
- **官方文档**: [Amazon SageMaker Unified Studio User Guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/)
- **兼容性**: 不适用于 AWS 中国区域
- **建议**: 关注 AWS 中国区域的服务更新公告，等待 Amazon DataZone 和 SageMaker Unified Studio 在中国区域上线
