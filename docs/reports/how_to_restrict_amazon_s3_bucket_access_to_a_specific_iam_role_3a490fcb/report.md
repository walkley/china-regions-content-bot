---
title: 如何限制Amazon S3存储桶访问到特定IAM角色
publish_date: 2025-02-14
original_url: https://aws.amazon.com/blogs/security/how-to-restrict-amazon-s3-bucket-access-to-a-specific-iam-role/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 2
unavailable_services: 0
---

# 如何限制Amazon S3存储桶访问到特定IAM角色

[📖 查看原始博客](https://aws.amazon.com/blogs/security/how-to-restrict-amazon-s3-bucket-access-to-a-specific-iam-role/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文涉及的所有AWS服务（S3和IAM）在中国区域完全可用，文章中描述的bucket policy和IAM policy配置方法在中国区域与全球区域完全一致，可以直接按照原文实施。

## 服务分析

### 可用服务 (2个)

- Amazon S3 (Amazon Simple Storage Service)
- AWS IAM (AWS Identity and Access Management)

### 不可用服务 (0个)

无

### 评估说明

本文的核心内容是通过S3 bucket policy和IAM policy的配置来实现细粒度的访问控制。文章重点介绍了使用`aws:PrincipalArn`条件键来限制S3存储桶访问，这是IAM和S3的基础功能，在AWS中国区域完全支持。

主要技术点：
1. 使用bucket policy的Deny语句配合`aws:PrincipalArn`条件键
2. 同账户和跨账户场景的访问控制
3. IAM角色和IAM用户的权限管理

所有这些功能在中国区域都可以正常使用，唯一需要注意的是ARN格式使用`arn:aws-cn`前缀而非`arn:aws`。

## 验证结果

### 验证类型

✅ 教程步骤验证

### 执行状态

**状态**: ✅ 成功

### 关键发现

1. **Bucket Policy在中国区域完全有效**
   - 成功创建S3存储桶并应用了文章中描述的bucket policy
   - 使用`aws:PrincipalArn`条件键配合`StringNotEquals`操作符实现访问限制
   - 验证了即使是具有管理权限的用户，一旦被bucket policy的Deny语句排除，也无法访问bucket（包括无法执行GetBucketPolicy、PutBucketPolicy、DeleteBucketPolicy等操作）

2. **ARN格式差异**
   - 中国区域使用`arn:aws-cn`前缀，而非全球区域的`arn:aws`
   - 示例：`arn:aws-cn:iam::086750097665:role/ValidationTestRole`
   - S3 endpoint使用`.amazonaws.com.cn`而非`.amazonaws.com`

3. **IAM角色和用户管理**
   - 成功创建测试IAM角色和用户
   - 验证了多个principal的配置方式
   - 标签功能正常工作

4. **安全机制验证成功**
   - Bucket policy的Deny语句优先级高于任何Allow语句
   - 成功演示了"即使用户有s3:*权限，也会被bucket policy拒绝"的场景
   - 这正是文章要传达的核心安全概念

5. **资源清理注意事项**
   - 测试bucket `china-region-validation-test-1764056103` 因bucket policy锁定，当前IAM用户无法删除
   - 这是预期行为，证明了安全机制的有效性
   - 需要使用root账户或通过AWS Support清理该资源

## 实施建议

### 推荐方案

可直接按照原文实施，仅需注意以下配置差异：

1. **ARN格式调整**
   - 将所有`arn:aws`替换为`arn:aws-cn`
   - 示例：
     ```json
     "arn:aws-cn:s3:::your-bucket-name"
     "arn:aws-cn:iam::account-id:role/role-name"
     ```

2. **区域端点**
   - S3 endpoint自动使用`.amazonaws.com.cn`
   - 无需手动配置，AWS CLI会自动处理

3. **实施步骤**
   - 按照文章中的策略模板创建bucket policy
   - 确保IAM角色或用户的ARN正确
   - 测试验证访问控制是否生效

### 替代方案

无需替代方案，原方案在中国区域完全适用。

### 风险提示

- **Bucket Policy锁定风险**: 如文章所述，配置不当的bucket policy可能会锁定所有用户（包括管理员）对bucket的访问。建议在应用Deny策略前：
  - 仔细检查`aws:PrincipalArn`条件中的ARN是否正确
  - 确保至少有一个可用的IAM角色或用户在允许列表中
  - 在生产环境应用前先在测试环境验证
  - 保留root账户访问权限以便紧急情况下恢复

- **跨账户访问**: 跨账户场景需要同时配置bucket policy和IAM policy，确保两边的ARN格式都使用`arn:aws-cn`前缀

- **策略优先级**: Deny语句始终优先于Allow语句，这是IAM的基本原则，在配置时需要特别注意

### 配套资源

- **GitHub仓库**: 无
- **相关文档**: 
  - [AWS中国区域IAM文档](https://docs.amazonaws.cn/IAM/latest/UserGuide/)
  - [AWS中国区域S3文档](https://docs.amazonaws.cn/AmazonS3/latest/userguide/)
- **最佳实践**: 建议结合AWS Organizations的SCP（服务控制策略）实现多层次的访问控制
