---
title: Amazon SageMaker Catalog新业务元数据功能以提升组织内的可发现性
original_url: https://aws.amazon.com/blogs/aws/new-business-metadata-features-in-amazon-sagemaker-catalog-to-improve-discoverability-across-organizations/
validation_date: 2025-11-24
target_region: cn-northwest-1
feasibility: LOW
available_services: 4
unavailable_services: 1
---

# Amazon SageMaker Catalog新业务元数据功能以提升组织内的可发现性

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/new-business-metadata-features-in-amazon-sagemaker-catalog-to-improve-discoverability-across-organizations/) | 验证日期: 2025-11-24

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon DataZone在中国区不可用，方案无法实施

文章介绍的Amazon SageMaker Catalog功能完全依赖于Amazon DataZone服务。经过实际验证，DataZone服务目前在AWS中国区域（cn-northwest-1和cn-north-1）均不可用，导致整个方案无法在中国区实施。

## 服务分析

### 可用服务 (4个)

- AWS Glue (包括 AWS Glue Data Catalog)
- Amazon Redshift
- Amazon S3 (包括 S3 Tables)
- Amazon QuickSight

### 不可用服务 (1个)

- **Amazon DataZone** - 核心服务（SageMaker Catalog基于DataZone构建）

### 评估说明

虽然文章表面上介绍的是"Amazon SageMaker Catalog"功能，但该服务实际上是基于Amazon DataZone构建的数据目录和治理平台。经过技术验证：

1. **核心依赖不可用**：Amazon DataZone是SageMaker Catalog的底层服务，在中国区域完全不可用。尝试访问cn-northwest-1和cn-north-1的DataZone endpoint均返回连接错误。

2. **功能完全依赖DataZone**：文章中介绍的所有功能（列级元数据表单、富文本描述、术语表关联规则等）都是DataZone的原生功能，无法通过其他服务替代。

3. **其他服务可用但无法弥补**：虽然Glue、Redshift、S3、QuickSight在中国区都可用，但它们只是数据源，无法提供DataZone的数据目录、治理和协作功能。

## 验证结果

### 验证类型

- ⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon DataZone在AWS中国区域不可用，无法进行实际部署验证。在基础验证阶段已确认方案不可行。

### 关键发现

1. **DataZone服务区域限制**
   - 在cn-northwest-1和cn-north-1区域测试DataZone API均返回endpoint连接错误
   - 错误信息：`Could not connect to the endpoint URL: "https://datazone.cn-northwest-1.api.amazonwebservices.com.cn/v2/domains"`
   - 确认DataZone服务未在AWS中国区域部署

2. **服务命名混淆**
   - 文章标题使用"Amazon SageMaker Catalog"，但实际是DataZone服务的一部分
   - SageMaker Unified Studio是DataZone的用户界面，不是独立服务
   - 这种命名可能导致用户误以为是SageMaker的功能而在中国区可用

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此方案**

由于核心服务Amazon DataZone在中国区不可用，文章介绍的所有功能都无法使用。建议等待AWS官方在中国区域发布DataZone服务后再考虑实施。

### 替代方案

如果需要在AWS中国区域实现类似的数据目录和治理功能，可以考虑以下替代方案：

1. **AWS Glue Data Catalog + 自定义元数据管理**
   - 实施方式：使用AWS Glue Data Catalog作为基础数据目录，通过DynamoDB或RDS存储自定义业务元数据，开发自定义UI进行元数据管理
   - 复杂度：高
   - 适用场景：需要完全自主控制元数据管理流程的场景
   - 限制：需要大量开发工作，无法获得DataZone的协作和治理功能

2. **第三方数据目录工具**
   - 实施方式：使用开源或商业数据目录工具（如Apache Atlas、Amundsen、Collibra等）与AWS服务集成
   - 复杂度：中到高
   - 适用场景：已有数据治理工具或愿意引入第三方解决方案
   - 限制：需要额外的基础设施和维护成本，与AWS服务集成度较低

3. **等待服务上线**
   - 实施方式：关注AWS中国区域服务发布公告，等待DataZone服务正式上线
   - 复杂度：低
   - 适用场景：对时间要求不紧迫，希望使用原生AWS解决方案
   - 建议：定期检查AWS中国区域服务列表更新

### 风险提示

- **服务可用性风险**：Amazon DataZone在AWS中国区域的上线时间未知，可能需要较长等待期
- **功能差异风险**：即使DataZone未来在中国区上线，功能可能与全球区域存在差异或延迟
- **替代方案成本**：自建或使用第三方数据目录解决方案需要显著的开发和维护投入
- **数据治理合规**：在中国区域实施数据治理方案需要考虑本地数据保护法规要求

### 配套资源

- **GitHub仓库**: 无
- **官方文档**: [Amazon SageMaker Unified Studio User Guide - Data Catalog](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/working-with-business-catalog.html)
- **注意事项**: 官方文档中的功能仅适用于DataZone服务可用的区域

---

## 验证总结

本次验证通过静态分析和实际API测试确认，文章介绍的Amazon SageMaker Catalog功能完全依赖于Amazon DataZone服务，而该服务目前在AWS中国区域不可用。建议关注AWS中国区域服务更新，或考虑使用替代方案实现类似的数据目录和治理需求。
