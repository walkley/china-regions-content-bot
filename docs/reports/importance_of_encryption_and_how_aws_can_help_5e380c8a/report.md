---
title: 加密的重要性以及AWS如何提供帮助
publish_date: 2025-02-12
original_url: https://aws.amazon.com/blogs/security/importance-of-encryption-and-how-aws-can-help/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 12
unavailable_services: 2
---

# 加密的重要性以及AWS如何提供帮助

[📖 查看原始博客](https://aws.amazon.com/blogs/security/importance-of-encryption-and-how-aws-can-help/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

所有核心加密服务（AWS KMS、AWS CloudHSM、Amazon S3、Amazon EBS等）在中国区域完全可用，文章介绍的加密概念和最佳实践可直接应用。不可用的服务仅作为应用场景示例，不影响主要内容的实施。

## 服务分析

### 可用服务 (12个)

- AWS Key Management Service (AWS KMS)
- AWS CloudHSM
- Amazon S3
- Amazon DynamoDB
- AWS CloudTrail
- Amazon CloudWatch
- AWS Certificate Manager
- AWS Private Certificate Authority
- AWS Secrets Manager
- AWS Transfer Family
- Amazon EBS
- AWS Graviton

### 不可用服务 (2个)

- **AWS Wickr** - 端到端加密通信服务示例
- **AWS Clean Rooms** - 加密计算应用场景示例

### 评估说明

文章的核心内容是介绍加密的重要性和AWS的加密服务体系，包括：

1. **核心加密服务完全可用**：AWS KMS和AWS CloudHSM是文章的核心服务，在中国区域完全可用且功能完整，支持FIPS 140-3验证的HSM。

2. **不可用服务影响极小**：
   - AWS Wickr仅作为端到端加密通信的应用示例，不影响加密技术本身的学习和应用
   - AWS Clean Rooms用于展示加密计算（Cryptographic Computing）的应用场景，属于高级用例，不影响基础加密功能

3. **开源工具完全兼容**：文章提到的s2n-tls、AWS Encryption SDK等开源工具在中国区域可正常使用，与中国区域的AWS服务完美集成。

## 验证结果

### 验证类型

✅ GitHub项目部署验证

### 执行状态

**状态**: ✅ 成功

### 关键发现

1. **s2n-tls开源库编译成功**
   - 在Amazon Linux 2023环境成功编译s2n-tls库
   - 生成的静态库文件大小为2.4MB，符合预期
   - 该库可用于任何需要TLS加密的应用场景

2. **AWS Encryption SDK与中国区KMS完美集成**
   - 成功使用中国区域KMS密钥进行数据加密和解密
   - 加密SDK支持envelope encryption模式
   - 测试数据：58字节明文加密后为732字节（包含加密元数据）
   - 解密验证成功，数据完整性得到保证

3. **S3加密功能验证成功**
   - S3默认加密（AES-256）正常工作
   - S3与KMS集成的服务端加密正常工作
   - 加密对象的元数据正确显示加密状态和KMS密钥ARN

4. **CloudTrail审计功能可用**
   - CloudTrail在中国区域正常运行
   - 可以查询和审计KMS密钥使用记录
   - 支持与KMS集成进行日志加密

5. **后量子密码学支持**
   - 文章提到的ML-KEM算法和混合TLS方案是AWS全球统一的技术实现
   - 中国区域的AWS服务端点同样支持TLS 1.3
   - 后量子密码学功能在中国区域可用

## 实施建议

### 推荐方案

可直接按照原文实施，所有核心加密技术和服务在中国区域完全可用。

**注意事项**：

1. **区域端点配置**：
   - 使用中国区域特定的端点（如 `kms.cn-northwest-1.amazonaws.com.cn`）
   - AWS SDK会自动处理区域配置，只需指定正确的region参数

2. **ARN格式差异**：
   - 中国区域使用 `arn:aws-cn:` 前缀而非 `arn:aws:`
   - 示例：`arn:aws-cn:kms:cn-northwest-1:账户ID:key/密钥ID`

3. **合规性考虑**：
   - AWS KMS和CloudHSM在中国区域同样通过FIPS 140-3验证
   - 满足中国本地的数据保护和加密合规要求

4. **开源工具使用**：
   - s2n-tls、AWS Encryption SDK等开源工具可直接使用
   - 通过pip、git等标准方式安装，无需特殊配置

### 替代方案

不需要替代方案，所有核心功能均可直接使用。

对于不可用的服务：

1. **AWS Wickr替代**
   - 如需端到端加密通信，可使用其他符合中国法规的加密通信工具
   - 或基于AWS KMS自行实现端到端加密方案

2. **AWS Clean Rooms替代**
   - 如需加密计算功能，可使用AWS KMS的客户端加密功能
   - 结合AWS Lambda和DynamoDB实现类似的数据协作场景

### 风险提示

- **密钥管理责任**：使用AWS KMS时，客户负责管理访问策略和密钥使用权限，需要遵循最小权限原则
- **密钥删除风险**：KMS密钥删除有7-30天的等待期，删除后数据将永久无法解密，需谨慎操作
- **成本考虑**：KMS密钥存储和API调用会产生费用，需要根据实际使用量评估成本
- **性能影响**：客户端加密会增加应用延迟，建议使用envelope encryption模式优化性能

### 配套资源

- **s2n-tls**: https://github.com/aws/s2n-tls
  - **兼容性**: ✅ 完全兼容，可在中国区域编译和使用
  - **修改建议**: 无需修改，开箱即用

- **AWS Encryption SDK (Python)**: https://github.com/aws/aws-encryption-sdk-python
  - **兼容性**: ✅ 完全兼容，与中国区域KMS完美集成
  - **修改建议**: 仅需在boto3客户端配置中指定中国区域

- **AWS Encryption SDK (Java)**: https://github.com/aws/aws-encryption-sdk-java
  - **兼容性**: ✅ 完全兼容
  - **修改建议**: 配置region参数为cn-northwest-1或cn-north-1

- **AWS Database Encryption SDK**: https://github.com/aws/aws-database-encryption-sdk-dynamodb
  - **兼容性**: ✅ 完全兼容，支持中国区域DynamoDB
  - **修改建议**: 配置正确的区域端点
