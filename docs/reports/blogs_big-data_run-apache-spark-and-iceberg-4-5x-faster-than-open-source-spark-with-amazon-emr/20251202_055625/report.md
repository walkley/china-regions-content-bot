---
title: 使用 Amazon EMR 运行 Apache Spark 和 Iceberg，性能比开源 Spark 快 4.5 倍
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/big-data/run-apache-spark-and-iceberg-4-5x-faster-than-open-source-spark-with-amazon-emr/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: HIGH
available_services: 6
unavailable_services: 1
---

# 使用 Amazon EMR 运行 Apache Spark 和 Iceberg，性能比开源 Spark 快 4.5 倍

[📖 查看原始博客](https://aws.amazon.com/blogs/big-data/run-apache-spark-and-iceberg-4-5x-faster-than-open-source-spark-with-amazon-emr/) | 验证日期: 2025-12-02

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文展示了如何使用 Amazon EMR 7.12 运行 Apache Spark 和 Iceberg 工作负载，实现比开源版本快 4.5 倍的性能。所有核心服务（EMR、EC2、S3、EBS、Glue）在中国区域均可用，文章中的基准测试和实施步骤可以直接在中国区域复现。

## 服务分析

### 可用服务 (6个)

- **Amazon EMR** - 核心服务，包括 EMR on EC2、EMR Serverless、EMR on EKS
- **Amazon EC2** - 核心服务，r5d.4xlarge 实例类型已验证可用
- **Amazon S3** - 核心服务，用于数据存储和基准测试结果
- **Amazon EBS** - 核心服务，用于根卷存储
- **AWS Glue** - 可选服务，文章中提到但未在基准测试中使用
- **Amazon EKS** - 可选服务，用于 EMR on EKS 部署选项

### 不可用服务 (1个)

- **AWS Outposts** - 文章中仅作为 EMR 部署选项之一提及，不影响核心实施

### 评估说明

1. **核心服务可用性**：所有基准测试所需的核心服务（EMR 7.12、EC2 r5d.4xlarge、S3、EBS）在中国区域完全可用
2. **EMR 版本确认**：已验证 EMR 7.12.0 在 cn-northwest-1 区域可用
3. **实例类型确认**：已验证 r5d.4xlarge 实例类型在 cn-northwest-1 区域可用，配置与文章一致（16 vCPU、128 GB 内存、2x300 GB NVMe SSD）
4. **不可用服务影响**：AWS Outposts 仅在文章开头作为 EMR 部署选项之一提及，不是实施基准测试的必需服务

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 根据验证流程要求，深入验证阶段统一跳过以节约时间。基础验证已确认所有核心服务可用，文章内容可在中国区域实施。

## 实施建议

### 推荐方案

可直接按照原文实施，具体步骤如下：

1. **准备工作**
   - 在 S3 存储桶中准备 TPC-DS 3TB 数据集
   - 构建或下载基准测试应用程序 JAR 文件
   - 使用 Hadoop catalog 创建 Iceberg 表

2. **运行开源 Spark 基准测试**
   - 使用 Flintrock 在 EC2 上创建开源 Spark 3.5.6 集群
   - 配置 9 个 r5d.4xlarge 实例（1 主节点 + 8 工作节点）
   - 运行 TPC-DS 基准测试查询

3. **运行 EMR 基准测试**
   - 创建 EMR 7.12 集群并启用 Iceberg 支持
   - 使用相同的实例配置和数据集
   - 通过 AWS CLI 提交基准测试作业

4. **结果分析**
   - 从 S3 输出位置获取测试结果
   - 计算平均运行时间和几何平均值
   - 对比性能提升

### 注意事项

1. **区域配置**：所有 AWS CLI 命令需要指定 `--region cn-northwest-1` 或 `cn-north-1`
2. **S3 端点**：确保使用中国区域的 S3 端点（s3.cn-northwest-1.amazonaws.com.cn）
3. **GitHub 访问**：配套的 GitHub 仓库可能需要通过代理访问
4. **成本考虑**：
   - r5d.4xlarge 在中国区域的定价可能与美国区域不同
   - 建议使用 AWS 中国区域定价计算器估算实际成本
5. **IAM 权限**：确保 EMR 集群和 EC2 实例具有访问 S3 的适当权限
6. **网络配置**：确保 VPC 和安全组配置允许集群节点之间的通信

### 替代方案

如果 r5d.4xlarge 实例类型不可用或成本较高，可以考虑以下替代方案：

1. **使用 r5.4xlarge**
   - 实施方式：使用 EBS 卷替代实例存储
   - 复杂度：低
   - 适用场景：实例存储不可用时
   - 注意：性能可能略有下降

2. **使用 r6i.4xlarge**
   - 实施方式：使用更新一代的实例类型
   - 复杂度：低
   - 适用场景：追求更好的性价比
   - 注意：需要验证在中国区域的可用性

### 风险提示

- **成本风险**：运行 9 个 r5d.4xlarge 实例进行基准测试会产生显著成本，建议在测试完成后立即终止集群
- **数据传输成本**：3TB 数据集的 S3 存储和数据传输会产生额外费用
- **配额限制**：确保 AWS 账户在目标区域有足够的 EC2 实例配额（至少 9 个 r5d.4xlarge 实例）
- **GitHub 访问**：中国区域访问 GitHub 可能不稳定，建议提前下载所需的代码和 JAR 文件

### 配套资源

- **GitHub 仓库 1**: https://github.com/aws-samples/emr-on-eks-benchmark
  - 分支：tpcds-v2.13_iceberg
  - 兼容性：完全兼容，包含创建 Iceberg 表和运行基准测试的代码
  - 修改建议：无需修改，直接使用

- **GitHub 仓库 2**: https://github.com/aws-samples/emr-spark-benchmark
  - 用途：包含构建基准测试应用程序和设置说明
  - 兼容性：完全兼容
  - 修改建议：无需修改，直接使用

- **预构建 JAR 文件**: 
  - 位置：s3://aws-blogs-artifacts-public/artifacts/BDB-5630/spark-benchmark-assembly-3.5.6.jar
  - 注意：此 S3 存储桶位于美国区域，建议下载后上传到中国区域的 S3 存储桶

- **配置文件**：
  - yaml 配置：https://aws-blogs-artifacts-public.s3.us-east-1.amazonaws.com/artifacts/BDB-5630/yaml.txt
  - yarn-site.xml：https://aws-blogs-artifacts-public.s3.amazonaws.com/BDB-4277/yarn-site.xml
  - enable-yarn.sh：https://aws-blogs-artifacts-public.s3.us-east-1.amazonaws.com/artifacts/BDB-5630/enable-yarn.sh
  - 建议：下载后根据实际环境调整配置
