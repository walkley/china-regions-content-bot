---
title: Medidata在AWS上构建现代湖仓架构的实践之旅
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/big-data/medidatas-journey-to-a-modern-lakehouse-architecture-on-aws/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: HIGH
available_services: 6
unavailable_services: 0
---

# Medidata在AWS上构建现代湖仓架构的实践之旅

[📖 查看原始博客](https://aws.amazon.com/blogs/big-data/medidatas-journey-to-a-modern-lakehouse-architecture-on-aws/) | 验证日期: 2025-12-02

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

文章中涉及的所有AWS服务在中国区域（cn-northwest-1）均可用，架构基于标准AWS服务和开源技术栈，无区域限制性依赖。

## 服务分析

### 可用服务 (6个)

- Amazon EKS (Amazon Elastic Kubernetes Service)
- Amazon MSK (Amazon Managed Streaming for Apache Kafka)
- AWS Glue Data Catalog
- Amazon S3 (Amazon Simple Storage Service)
- AWS IAM (Identity and Access Management)
- Amazon Kinesis

### 不可用服务 (0个)

无

### 评估说明

本文介绍了Medidata如何利用AWS服务构建现代湖仓架构，从传统批处理ETL迁移到实时流处理平台。核心技术栈包括：

1. **计算层**：Amazon EKS托管Apache Flink流处理作业
2. **消息层**：Amazon MSK托管Apache Kafka
3. **存储层**：Amazon S3存储Apache Iceberg表
4. **元数据层**：AWS Glue Data Catalog管理表元数据
5. **安全层**：AWS IAM统一访问控制

所有涉及的AWS托管服务在中国区域均已上线，开源组件（Apache Flink、Apache Kafka、Apache Iceberg）不受区域限制。架构设计遵循AWS最佳实践，适合在中国区域实施。

## 验证结果

### 验证类型

⏭️ 已跳过（按照验证流程要求）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 根据验证流程配置，深入验证阶段统一跳过以节约时间

### 关键发现

基于静态分析的关键发现：

1. **服务完全兼容**
   - 文章中提到的6个AWS服务在cn-northwest-1区域全部可用
   - 无需服务替代或架构调整

2. **开源技术栈无限制**
   - Apache Flink、Apache Kafka、Apache Iceberg均为开源项目
   - 可在任何AWS区域的EKS/MSK上运行

3. **架构模式可复用**
   - 从批处理到流处理的迁移模式具有通用性
   - Iceberg湖仓架构是行业标准方案

## 实施建议

### 推荐方案

可直接按照原文架构在中国区域实施，具体建议：

**实施路径**：
1. 使用Amazon EKS部署Apache Flink流处理集群
2. 配置Amazon MSK作为消息中间件
3. 在Amazon S3上创建Apache Iceberg表，使用AWS Glue Data Catalog管理元数据
4. 通过AWS IAM配置细粒度访问控制
5. 利用AWS Glue的Iceberg优化功能（压缩、快照保留、孤儿文件清理）

**注意事项**：
- **网络配置**：确保VPC配置符合中国区域合规要求
- **数据主权**：数据存储在中国区域，满足数据本地化要求
- **服务配额**：提前检查EKS节点、MSK集群等资源配额
- **Iceberg版本**：使用AWS Glue支持的Apache Iceberg版本（建议1.0+）
- **监控告警**：配置CloudWatch监控Flink作业和MSK集群健康状态

**预计工作量**：中等
- 架构设计：1-2周
- 基础设施搭建：2-3周
- 数据迁移和测试：4-6周

### 替代方案

虽然原方案可直接实施，但根据具体需求可考虑以下变体：

1. **轻量级方案**
   - 实施方式：使用Amazon Kinesis Data Streams替代MSK，减少运维复杂度
   - 复杂度：低
   - 适用场景：数据吞吐量较小（<1MB/s），团队对Kafka不熟悉

2. **Serverless方案**
   - 实施方式：使用AWS Glue Streaming ETL替代自建Flink on EKS
   - 复杂度：低
   - 适用场景：希望减少基础设施管理，接受AWS Glue的功能限制

3. **混合方案**
   - 实施方式：保留MSK和Iceberg，使用Amazon EMR on EKS运行Flink作业
   - 复杂度：中
   - 适用场景：需要更灵活的Spark/Flink混合处理能力

### 风险提示

- **成本管理**：EKS集群和MSK集群为持续运行资源，需做好成本预算和优化
- **技能要求**：团队需具备Kubernetes、Flink、Kafka、Iceberg等技术栈经验
- **数据迁移**：从传统批处理迁移到流处理需要重构ETL逻辑，建议分阶段实施
- **性能调优**：Flink作业和Iceberg表需要根据实际数据量进行性能调优
- **版本兼容**：注意Apache Flink、Kafka、Iceberg版本之间的兼容性

### 配套资源

- **AWS文档**：
  - [AWS Glue中的Apache Iceberg表优化](https://docs.aws.amazon.com/glue/latest/dg/table-optimizers.html)
  - [在AWS上使用Apache Iceberg](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.html)
  - [Amazon MSK最佳实践](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html)
  - [Amazon EKS最佳实践指南](https://aws.github.io/aws-eks-best-practices/)

- **开源项目**：
  - [Apache Iceberg官方文档](https://iceberg.apache.org/)
  - [Apache Flink官方文档](https://flink.apache.org/)

- **GitHub仓库**：文章未提供配套代码仓库

**中国区域特别说明**：
- 所有AWS服务文档在中国区域AWS官网均有中文版本
- 建议参考AWS中国区域的服务限制和配额文档
- 可联系AWS中国团队获取架构审查和技术支持
