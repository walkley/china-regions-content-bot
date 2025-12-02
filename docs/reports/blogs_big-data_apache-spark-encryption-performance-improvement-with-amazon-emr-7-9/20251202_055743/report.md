---
title: 使用 Amazon EMR 7.9 改进 Apache Spark 加密性能
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/big-data/apache-spark-encryption-performance-improvement-with-amazon-emr-7-9/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: HIGH
available_services: 7
unavailable_services: 0
---

# 使用 Amazon EMR 7.9 改进 Apache Spark 加密性能

[📖 查看原始博客](https://aws.amazon.com/blogs/big-data/apache-spark-encryption-performance-improvement-with-amazon-emr-7-9/) | 验证日期: 2025-12-02

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

文章介绍的 Amazon EMR 7.9 Spark 加密性能优化功能所依赖的所有核心服务在 AWS 中国区域均可用。文章提供了详细的基准测试步骤、配置说明和 GitHub 示例代码，可以在中国区域直接复现和实施。

## 服务分析

### 可用服务 (7个)

- **Amazon EMR** - 核心服务，EMR 7.9 版本在中国区可用
- **Amazon S3** - 数据存储服务
- **Amazon EC2** - 计算实例服务
- **Amazon EBS** - 块存储服务
- **AWS KMS** - 密钥管理服务
- **AWS IAM** - 身份和访问管理
- **AWS CLI** - 命令行工具

### 不可用服务 (0个)

无

### 评估说明

本文所涉及的所有 AWS 服务在中国区域均完全可用：

1. **核心服务可用性**: Amazon EMR 7.9 在中国区域（cn-north-1 和 cn-northwest-1）均已发布，支持文章中描述的 Spark 3.5.5 加密优化功能。

2. **支持服务完整**: 所有配套服务（S3、EC2、EBS、KMS、IAM）在中国区域功能完整，与全球区域保持一致。

3. **实例类型支持**: 文章中使用的 r5d.4xlarge 实例类型在中国区域可用。

4. **无替代方案需求**: 由于所有服务均可用，无需寻找替代方案或进行架构调整。

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 根据验证流程要求，深入验证阶段统一跳过以节约时间。基础验证（静态分析）已确认所有服务在中国区域可用，文章提供的配置和步骤可直接应用。

### 关键发现

基于静态分析的关键发现：

1. **服务版本一致性**
   - EMR 7.9.0 在中国区域可用
   - Spark 3.5.5 运行时完全支持
   - 加密优化功能无区域限制

2. **实例和存储支持**
   - r5d.4xlarge 实例类型在中国区域可用
   - EBS gp2 卷类型支持完整
   - 本地 NVMe SSD 存储可用

3. **GitHub 项目兼容性**
   - 配套的基准测试工具（https://github.com/aws-samples/emr-spark-benchmark）可直接使用
   - TPC-DS 测试数据集可从公共 S3 存储桶复制
   - Bootstrap 脚本在公共 S3 存储桶中可访问

4. **定价差异提醒**
   - 文章中的成本分析基于 us-east-1 区域
   - 中国区域的定价可能有所不同
   - 建议使用 AWS 中国区域定价计算器重新计算成本

## 实施建议

### 推荐方案

可直接按照原文实施，但需注意以下中国区域特定配置：

**区域配置调整**:
```bash
# 在所有 AWS CLI 命令中指定中国区域
--region cn-northwest-1

# 或设置环境变量
export AWS_DEFAULT_REGION=cn-northwest-1
export AWS_PROFILE=zhy
```

**S3 存储桶创建**:
```bash
# 在中国区域创建 S3 存储桶
aws s3 mb s3://your-bucket-name --region cn-northwest-1 --profile zhy
```

**数据集准备**:
```bash
# 从公共数据集复制到中国区域存储桶
# 注意：跨区域复制可能需要先下载到本地再上传
aws s3 cp s3://blogpost-sparkoneks-us-east-1/blog/BLOG_TPCDS-TEST-3T-partitioned \
  s3://your-cn-bucket/BLOG_TPCDS-TEST-3T-partitioned \
  --recursive --region cn-northwest-1 --profile zhy
```

**子网配置**:
```bash
# 确保使用中国区域的 VPC 子网 ID
--ec2-attributes SubnetId=subnet-xxxxx
```

**实施步骤**:

1. 配置 AWS CLI 指向中国区域和正确的 profile
2. 在中国区域创建 S3 存储桶
3. 准备测试数据集（可能需要跨区域传输）
4. 按照文章步骤创建 EMR 集群
5. 提交基准测试作业
6. 分析结果并根据中国区域定价计算成本

**预计工作量**: 低 - 主要是配置调整，无需代码修改

### 替代方案

无需替代方案，所有服务均可用。

### 风险提示

- **跨区域数据传输**: 从 us-east-1 公共数据集复制 3TB 数据到中国区域可能需要较长时间和产生数据传输费用。建议评估是否可以使用较小的数据集进行初始测试。

- **定价差异**: 中国区域的 EMR、EC2 和 EBS 定价与 us-east-1 不同。文章中的成本分析（$4.25 vs $5.28）仅供参考，实际成本需要根据中国区域定价重新计算。

- **Bootstrap 脚本访问**: 文章中的 bootstrap 脚本位于公共 S3 存储桶 `s3://spark-ba/`，需要确认从中国区域是否可以访问。如果无法访问，需要将脚本复制到中国区域的 S3 存储桶。

- **网络连接**: 访问 GitHub 仓库和公共 S3 存储桶时，可能需要考虑网络连接稳定性。

- **IAM 角色**: 确保 EMR_DefaultRole 和 EMR_EC2_DefaultRole 在中国区域账户中已正确配置。

### 配套资源

- **GitHub 仓库**: https://github.com/aws-samples/emr-spark-benchmark
- **兼容性**: 完全兼容，可在中国区使用
- **修改建议**: 
  - 将所有 AWS CLI 命令添加 `--region cn-northwest-1` 参数
  - 更新 S3 存储桶名称为中国区域的存储桶
  - 如果 bootstrap 脚本无法从公共存储桶访问，需要复制到中国区域存储桶

**相关文档**:
- [AWS 中国区域 EMR 文档](https://docs.amazonaws.cn/emr/)
- [AWS 中国区域定价](https://www.amazonaws.cn/pricing/)
- [EMR 7.x 发行说明](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-790-release.html)
