---
title: 通过AWS Glue Iceberg REST端点使用PyIceberg访问Amazon S3 Tables中的数据
publish_date: 2025-02-17
original_url: https://aws.amazon.com/blogs/storage/access-data-in-amazon-s3-tables-using-pyiceberg-through-the-aws-glue-iceberg-rest-endpoint/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 7
unavailable_services: 1
---

# 通过AWS Glue Iceberg REST端点使用PyIceberg访问Amazon S3 Tables中的数据

[📖 查看原始博客](https://aws.amazon.com/blogs/storage/access-data-in-amazon-s3-tables-using-pyiceberg-through-the-aws-glue-iceberg-rest-endpoint/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon S3 Tables在中国区域不可用，无法实施

Amazon S3 Tables是本方案的核心存储服务，整个博客围绕如何通过PyIceberg访问S3 Tables中的Iceberg表展开。该服务在中国区域完全不可用，导致方案无法实施。

## 服务分析

### 可用服务 (7个)

- Amazon S3
- AWS Glue
- AWS Lake Formation
- AWS IAM
- Amazon Athena
- Amazon Redshift
- Amazon QuickSight

### 不可用服务 (1个)

- **Amazon S3 Tables** - 核心服务

### 评估说明

经过实际验证，Amazon S3 Tables服务在中国区域（cn-northwest-1）完全不可用。尝试调用S3 Tables API时返回端点连接错误：

```
Could not connect to the endpoint URL: "https://s3tables.cn-northwest-1.amazonaws.com.cn/buckets"
```

虽然其他相关服务（AWS Glue、Lake Formation、Athena等）在中国区域都可用，但S3 Tables是整个方案的基础和核心：

1. **核心依赖**：博客的主要目标是演示如何访问S3 Tables中存储的Iceberg表
2. **无法替代**：S3 Tables提供的自动表维护、优化性能和简化安全特性是其独特价值
3. **架构核心**：整个数据流程从S3 Tables开始，没有该服务则方案无法启动

## 验证结果

### 验证类型

- ⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon S3 Tables在中国区域不可用，可行性评估为LOW，无需进行深入验证

### 关键发现

通过API调用验证确认：

1. **S3 Tables不可用**
   - 服务端点在中国区域不存在
   - API调用返回连接错误
   - 无法创建table buckets或访问S3 Tables功能

2. **支持服务可用**
   - AWS Glue Data Catalog正常运行
   - Lake Formation服务可用
   - 其他分析服务（Athena、Redshift、QuickSight）均可用

## 实施建议

### 推荐方案

**不建议在中国区域实施此方案**

由于Amazon S3 Tables是整个架构的核心组件，其在中国区域的不可用性使得该方案无法按原文实施。

### 替代方案

如果需要在中国区域实现类似的Iceberg表管理和查询功能，可以考虑以下替代方案：

1. **使用标准S3 + AWS Glue Data Catalog**
   - 实施方式：在标准S3存储桶中存储Iceberg表，使用AWS Glue Data Catalog管理元数据
   - 复杂度：中
   - 适用场景：需要Iceberg表格式但不依赖S3 Tables特定功能的场景
   - 缺点：缺少S3 Tables的自动优化、维护和性能增强特性

2. **使用Amazon EMR + Iceberg**
   - 实施方式：通过EMR集群管理Iceberg表，数据存储在标准S3中
   - 复杂度：高
   - 适用场景：需要完整的大数据处理能力和Iceberg支持
   - 缺点：需要管理EMR集群，运维复杂度较高

3. **使用AWS Glue ETL + Iceberg格式**
   - 实施方式：使用AWS Glue ETL作业处理Iceberg格式数据，存储在标准S3中
   - 复杂度：中
   - 适用场景：ETL工作负载为主的数据湖场景
   - 缺点：需要自行管理Iceberg表的维护和优化

### 风险提示

- **功能缺失**：替代方案无法提供S3 Tables的自动表维护、压缩和优化功能
- **性能差异**：标准S3存储的Iceberg表性能可能不如S3 Tables优化后的性能
- **管理复杂度**：需要手动管理表的生命周期、快照清理和元数据维护
- **成本考虑**：替代方案可能需要额外的计算资源（如EMR集群），增加运营成本

### 配套资源

- **Python脚本**: 博客提供了完整的PyIceberg示例代码
- **兼容性**: 代码依赖S3 Tables服务，无法在中国区域直接使用
- **修改建议**: 如采用替代方案，需要修改catalog配置，将warehouse指向标准S3存储桶而非S3 Tables catalog
