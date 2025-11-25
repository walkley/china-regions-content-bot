---
title: 为Amazon S3通用存储桶引入基于属性的访问控制
publish_date: 2025-11-20
original_url: https://aws.amazon.com/blogs/aws/introducing-attribute-based-access-control-for-amazon-s3-general-purpose-buckets/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 11
unavailable_services: 0
---

# 为Amazon S3通用存储桶引入基于属性的访问控制

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/introducing-attribute-based-access-control-for-amazon-s3-general-purpose-buckets/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文介绍的Amazon S3基于属性的访问控制（ABAC）功能所依赖的所有AWS服务在中国区域均完全可用，包括核心的S3、IAM、CloudFormation等服务。该功能已在cn-northwest-1区域成功验证，可以直接按照原文步骤实施。

## 服务分析

### 可用服务 (11个)

- Amazon S3
- AWS IAM
- AWS CLI
- AWS CloudFormation
- AWS SDKs
- AWS Config
- AWS CloudTrail
- AWS Billing Console
- AWS Cost Explorer
- AWS Cost and Usage Reports
- AWS Management Console

### 不可用服务 (0个)

无

### 评估说明

所有涉及的AWS服务在中国区域均可用。Amazon S3的ABAC功能是S3服务的原生功能，通过新的API（PutBucketAbac、GetBucketAbac）实现，在中国区域已完全支持。IAM策略中的条件键（aws:ResourceTag、aws:TagKeys、aws:RequestTag）也在中国区域正常工作。

## 验证结果

### 验证类型

✅ 教程步骤验证

### 执行状态

**状态**: ✅ 成功

### 关键发现

1. **ABAC API完全可用**
   - PutBucketAbac和GetBucketAbac API在cn-northwest-1区域正常工作
   - 成功启用存储桶的ABAC功能并验证状态

2. **标签条件策略正常工作**
   - 创建的IAM策略使用aws:ResourceTag/environment条件键
   - 策略成功附加到IAM角色
   - 标签匹配逻辑在中国区域正常运行

3. **S3操作验证成功**
   - 成功对启用ABAC的存储桶执行PutObject操作
   - 成功对启用ABAC的存储桶执行GetObject操作
   - 成功对启用ABAC的存储桶执行ListBucket操作

4. **资源清理完整**
   - 所有测试资源（存储桶、IAM策略、IAM角色）已完全清理
   - 未发现本次验证产生的残留资源

## 实施建议

### 推荐方案

可直接按照原文实施，注意以下事项：

- **区域端点**：使用中国区域的服务端点（如s3.cn-northwest-1.amazonaws.com.cn）
- **ARN格式**：使用aws-cn前缀（如arn:aws-cn:iam::账户ID:role/角色名）
- **API调用**：确保AWS CLI或SDK配置正确的区域和凭证
- **标签管理**：启用ABAC后，建议使用TagResource API而非PutBucketTagging API进行标签管理

### 替代方案

无需替代方案，原方案完全适用。

### 风险提示

- **标签一致性**：启用ABAC前应审查现有存储桶标签，确保标签策略与访问控制需求一致
- **API迁移**：启用ABAC后，PutBucketTagging API将被阻止，需要更新应用程序使用TagResource API
- **权限测试**：在生产环境启用前，建议在测试环境充分验证标签匹配逻辑和权限策略
- **成本分配**：可以将ABAC标签同时用作成本分配标签，需在账单控制台激活

### 配套资源

- **GitHub仓库**: 无
- **AWS文档**: [Amazon S3用户指南 - 启用ABAC](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html)
- **相关功能**: 该功能也适用于S3目录存储桶、S3访问点和S3表存储桶
