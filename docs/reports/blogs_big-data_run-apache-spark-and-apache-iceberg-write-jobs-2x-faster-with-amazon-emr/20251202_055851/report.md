---
title: 使用Amazon EMR将Apache Spark和Apache Iceberg写入作业速度提升2倍
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/big-data/run-apache-spark-and-apache-iceberg-write-jobs-2x-faster-with-amazon-emr/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: HIGH
available_services: 9
unavailable_services: 1
---

# 使用Amazon EMR将Apache Spark和Apache Iceberg写入作业速度提升2倍

[📖 查看原始博客](https://aws.amazon.com/blogs/big-data/run-apache-spark-and-apache-iceberg-write-jobs-2x-faster-with-amazon-emr/) | 验证日期: 2025-12-02

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

文章介绍的Amazon EMR 7.12性能基准测试方案在中国区域完全可行。所有核心服务（Amazon EMR、EC2、S3、EBS）均在中国区域可用，包括所需的r5d.4xlarge实例类型。唯一不可用的Amazon EMR on AWS Outposts仅作为EMR部署选项之一被提及，不影响文章核心内容的实施。

## 服务分析

### 可用服务 (9个)

- **Amazon EMR** - 核心服务
- **Amazon EMR on EC2** - 核心服务
- **Amazon EMR Serverless**
- **Amazon EMR on EKS**
- **AWS Glue**
- **Amazon EC2** (r5d.4xlarge实例已验证可用)
- **Amazon S3** - 核心服务
- **Amazon EBS** - 核心服务
- **AWS CLI**

### 不可用服务 (1个)

- **Amazon EMR on AWS Outposts**

### 评估说明

文章的核心内容是展示Amazon EMR 7.12在Spark和Iceberg写入性能方面的优化，主要使用Amazon EMR on EC2部署模式。所有核心服务在中国区域均可用：

1. **核心服务完全可用**：Amazon EMR、EC2、S3、EBS等核心服务在cn-northwest-1区域均可用
2. **实例类型支持**：文章使用的r5d.4xlarge实例类型在中国区域完全支持，包括2x300GB NVMe SSD本地存储
3. **不可用服务影响极小**：Amazon EMR on AWS Outposts仅在文章开头作为EMR的部署选项之一被提及，不涉及具体实施步骤
4. **GitHub项目可访问**：配套的emr-spark-benchmark项目可以正常访问

## 验证结果

### 验证类型

⏭️ 已跳过（按照验证策略统一跳过深入验证）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 根据验证流程要求，深入验证阶段统一跳过以节约时间

## 实施建议

### 推荐方案

可直接按照原文实施，具体步骤：

1. **创建EMR集群**：在cn-northwest-1区域创建EMR 7.12集群，使用9个r5d.4xlarge实例（1个主节点，8个工作节点）
2. **准备测试数据**：在S3存储桶中设置TPC-DS 3TB测试数据集，使用Iceberg表格式
3. **运行基准测试**：从GitHub克隆emr-spark-benchmark项目，构建并运行基准测试
4. **分析结果**：从S3输出路径获取测试结果CSV文件，计算性能指标

**注意事项**：
- 确保在中国区域使用正确的S3存储桶和EMR配置
- 文章中的定价信息基于全球区域，中国区域定价需单独查询
- 使用AWS CLI时确保配置正确的中国区域endpoint

### 配置差异

- **区域设置**：所有资源需创建在cn-northwest-1或cn-north-1区域
- **定价**：中国区域的EC2、EMR、EBS定价与全球区域不同，需使用AWS中国区域定价计算器
- **文档链接**：部分AWS文档链接可能需要访问中国区域的文档站点

### 预期工作量

- **准备阶段**：1-2小时（创建集群、准备数据）
- **测试执行**：根据文章，单次测试约7-15分钟
- **结果分析**：30分钟-1小时

### 风险提示

- **成本控制**：9个r5d.4xlarge实例的集群成本较高，建议测试完成后立即清理资源
- **配额限制**：确保AWS账户在目标区域有足够的EC2实例配额（至少9个r5d.4xlarge实例）
- **数据传输**：3TB测试数据集的准备和存储会产生S3存储和数据传输费用
- **测试时长**：完整的基准测试需要运行多次迭代，建议合理安排测试时间

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/emr-spark-benchmark
- **兼容性**: 可在中国区使用，需要修改配置文件中的区域和S3存储桶设置
- **修改建议**: 
  - 将AWS区域配置改为cn-northwest-1或cn-north-1
  - 使用中国区域的S3存储桶
  - 确保EMR集群版本选择7.12或更高版本
