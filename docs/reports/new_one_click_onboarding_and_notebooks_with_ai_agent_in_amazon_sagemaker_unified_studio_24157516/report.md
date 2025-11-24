---
title: New one-click onboarding and notebooks with a built-in AI agent in Amazon SageMaker Unified Studio
original_url: https://aws.amazon.com/blogs/aws/new-one-click-onboarding-and-notebooks-with-ai-agent-in-amazon-sagemaker-unified-studio/
validation_date: 2025-11-24
target_region: cn-northwest-1
feasibility: LOW
available_services: 10
unavailable_services: 1
---

# New one-click onboarding and notebooks with a built-in AI agent in Amazon SageMaker Unified Studio

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/new-one-click-onboarding-and-notebooks-with-ai-agent-in-amazon-sagemaker-unified-studio/) | 验证日期: 2025-11-24

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon SageMaker Unified Studio在中国区域不可用，无法实施

文章介绍的核心功能Amazon SageMaker Unified Studio（基于AWS DataZone）在cn-northwest-1区域不可用，经实际验证DataZone服务endpoint无法连接。虽然文章提到的其他支撑服务均在中国区可用，但核心功能的缺失导致整个方案无法实施。

## 服务分析

### 可用服务 (10个)

- Amazon SageMaker（基础服务）
- AWS Identity and Access Management (IAM)
- AWS Glue Data Catalog
- AWS Lake Formation
- Amazon S3
- Amazon S3 Tables
- Amazon Athena
- Amazon Redshift
- Amazon Managed Workflows for Apache Airflow (MWAA)
- AWS Glue Spark

### 不可用服务 (1个)

- **Amazon SageMaker Unified Studio** - 核心服务

### 评估说明

1. **核心服务不可用**：Amazon SageMaker Unified Studio是文章的核心主题，该服务在中国区域完全不可用。实际验证显示DataZone服务（Unified Studio的底层服务）在cn-northwest-1区域无法连接。

2. **区域限制明确**：文章明确指出该功能仅在以下区域可用：
   - US East (Ohio, N. Virginia)
   - US West (Oregon)
   - Asia Pacific (Mumbai, Singapore, Sydney, Tokyo)
   - Europe (Frankfurt, Ireland)
   
   中国区域（cn-northwest-1和cn-north-1）均不在支持列表中。

3. **技术验证结果**：
   - DataZone API endpoint连接失败
   - 错误信息：`Could not connect to the endpoint URL: "https://datazone.cn-northwest-1.api.amazonwebservices.com.cn/v2/domains"`

4. **支撑服务可用**：虽然S3、Glue、Athena、Redshift等支撑服务在中国区可用，但没有Unified Studio作为统一平台，无法实现文章描述的一键式入门和集成体验。

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon SageMaker Unified Studio在cn-northwest-1区域不可用，经API验证确认DataZone服务无法连接。由于核心功能缺失，无法进行实际操作验证。

## 实施建议

### 推荐方案

**不建议在中国区域实施此方案**

Amazon SageMaker Unified Studio是文章的核心功能，该服务在中国区域完全不可用。文章介绍的所有特性（一键式入门、内置AI代理的笔记本、跨服务集成）都依赖于Unified Studio平台，无法在中国区域实现。

### 替代方案

虽然无法使用Unified Studio，但可以考虑以下替代方案实现类似的数据分析和机器学习工作流：

1. **使用Amazon SageMaker Studio Classic**
   - 实施方式：使用传统的SageMaker Studio进行机器学习开发
   - 复杂度：中
   - 适用场景：需要完整的ML开发环境，但不需要跨服务统一界面
   - 限制：缺少Unified Studio的一键式入门和跨服务集成体验

2. **组合使用独立服务**
   - 实施方式：分别使用Athena查询编辑器、SageMaker Notebooks、Glue Studio等独立工具
   - 复杂度：高
   - 适用场景：团队熟悉各个独立服务，可以接受在多个控制台间切换
   - 限制：
     - 需要手动配置服务间的集成
     - 缺少统一的数据目录和权限管理
     - 无法使用内置AI代理辅助开发

3. **使用AWS Glue Studio + SageMaker组合**
   - 实施方式：使用Glue Studio进行ETL和数据准备，SageMaker进行模型训练
   - 复杂度：中
   - 适用场景：数据工程和机器学习工作流相对独立
   - 限制：缺少统一的笔记本体验和AI辅助功能

### 风险提示

- **功能缺失**：无法使用文章介绍的任何核心功能，包括一键式入门、内置AI代理、统一笔记本体验
- **区域限制**：Amazon SageMaker Unified Studio短期内不太可能在中国区域推出，需要长期使用替代方案
- **学习成本**：替代方案需要分别学习和配置多个独立服务，增加团队学习成本
- **集成复杂度**：手动集成多个服务需要额外的开发和维护工作
- **权限管理**：缺少Unified Studio的统一权限管理，需要在各个服务中分别配置IAM权限

### 配套资源

- **GitHub仓库**: 无
- **官方文档**: [Amazon SageMaker Unified Studio User Guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/)（仅适用于支持区域）
- **替代方案文档**:
  - [Amazon SageMaker Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html)
  - [AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/ug/what-is-glue-studio.html)
  - [Amazon Athena Query Editor](https://docs.aws.amazon.com/athena/latest/ug/query-editor.html)
