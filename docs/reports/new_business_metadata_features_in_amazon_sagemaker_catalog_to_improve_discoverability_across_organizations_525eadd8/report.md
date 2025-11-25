---
title: Amazon SageMaker Catalog 中的新业务元数据功能，提升组织内的可发现性
publish_date: 2025-11-19
original_url: https://aws.amazon.com/blogs/aws/new-business-metadata-features-in-amazon-sagemaker-catalog-to-improve-discoverability-across-organizations/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 6
unavailable_services: 1
---

# Amazon SageMaker Catalog 中的新业务元数据功能，提升组织内的可发现性

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/new-business-metadata-features-in-amazon-sagemaker-catalog-to-improve-discoverability-across-organizations/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon SageMaker Unified Studio（基于Amazon DataZone）在中国区域尚未推出，无法使用文章介绍的新功能

文章介绍的是Amazon SageMaker Catalog的新元数据功能，该服务现已内置于Amazon SageMaker Unified Studio中。虽然传统的SageMaker服务在中国区域可用，但SageMaker Unified Studio依赖的底层服务Amazon DataZone在中国区域无法连接，导致文章中介绍的新功能无法在中国区域使用。

## 服务分析

### 可用服务 (6个)

- Amazon SageMaker (传统功能)
- AWS Glue
- AWS Glue Data Catalog
- Amazon Redshift
- Amazon QuickSight
- Amazon S3

### 不可用服务 (1个)

- **Amazon DataZone** - 核心服务，SageMaker Unified Studio的底层服务

### 评估说明

1. **核心服务不可用**：文章介绍的功能基于Amazon SageMaker Catalog，该服务现已集成到Amazon SageMaker Unified Studio中。SageMaker Unified Studio是基于Amazon DataZone构建的统一数据管理平台。

2. **DataZone在中国区域状态**：虽然AWS CLI中包含DataZone命令，但在cn-northwest-1区域无法连接到服务endpoint（`https://datazone.cn-northwest-1.amazonaws.com.cn`），表明该服务在中国区域尚未正式推出。

3. **功能依赖关系**：文章中介绍的两个新功能：
   - 列级元数据表单和富文本描述
   - 术语表关联的元数据强制规则
   
   这些功能都需要通过SageMaker Unified Studio的界面进行配置和管理，而该界面依赖DataZone服务。

4. **传统SageMaker功能可用**：虽然传统的Amazon SageMaker服务（如训练、推理、笔记本等）在中国区域完全可用，但文章特指的SageMaker Catalog新功能无法使用。

## 验证结果

### 验证类型

- ✅ 教程步骤验证

### 执行状态

**状态**: ❌ 失败

**原因**: 核心依赖服务Amazon DataZone在中国区域无法连接，无法访问SageMaker Unified Studio界面和相关功能

### 关键发现

1. **DataZone服务不可用**
   - 测试endpoint: `https://datazone.cn-northwest-1.amazonaws.com.cn`
   - 错误信息: "Could not connect to the endpoint URL"
   - 影响：无法创建DataZone domain，无法使用SageMaker Unified Studio

2. **SageMaker Resource Catalogs可用但功能受限**
   - 在中国区域可以列出SageMaker Resource Catalogs
   - 发现默认的Feature Group Catalog存在
   - 但无法通过Unified Studio界面进行文章中描述的元数据管理操作

3. **相关服务验证结果**
   - AWS Glue: ✅ 完全可用
   - Amazon Redshift: ✅ 完全可用
   - Amazon QuickSight: ✅ 服务可用（需订阅）
   - Amazon S3: ✅ 完全可用

## 实施建议

### 推荐方案

**不建议直接实施**

由于Amazon SageMaker Unified Studio（基于DataZone）在中国区域尚未推出，文章介绍的新元数据功能无法在中国区域使用。建议等待AWS官方在中国区域正式推出该服务。

### 替代方案

1. **使用AWS Glue Data Catalog进行元数据管理**
   - 实施方式：利用AWS Glue Data Catalog的原生功能管理数据资产元数据
   - 复杂度：中
   - 适用场景：需要基础的数据目录和元数据管理功能
   - 限制：缺少文章中介绍的列级自定义元数据表单、富文本描述、术语表强制规则等高级功能

2. **使用标签和描述字段进行基础元数据管理**
   - 实施方式：在Glue Data Catalog中使用表和列的描述字段，配合AWS标签进行分类
   - 复杂度：低
   - 适用场景：简单的元数据标注和分类需求
   - 限制：功能较为基础，缺少业务术语表、元数据强制规则等治理功能

3. **自建元数据管理系统**
   - 实施方式：基于开源工具（如Apache Atlas、Amundsen）构建元数据管理平台
   - 复杂度：高
   - 适用场景：有专业团队和复杂元数据治理需求的组织
   - 限制：需要额外的开发和维护成本

### 风险提示

- **服务可用性风险**: Amazon DataZone和SageMaker Unified Studio在中国区域的推出时间未知，可能需要较长等待期
- **功能差异风险**: 即使未来服务推出，中国区域版本可能与全球区域存在功能差异
- **迁移成本风险**: 如果采用替代方案，未来迁移到SageMaker Unified Studio可能需要额外的数据迁移和配置工作
- **学习成本风险**: 替代方案可能需要学习不同的工具和工作流程

### 配套资源

- **GitHub仓库**: 无
- **官方文档**: [Amazon SageMaker Unified Studio User Guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/working-with-business-catalog.html)
- **注意事项**: 官方文档中的功能在中国区域暂不可用
