---
title: Introducing VPC encryption controls: Enforce encryption in transit within and across VPCs in a Region
original_url: https://aws.amazon.com/blogs/aws/introducing-vpc-encryption-controls-enforce-encryption-in-transit-within-and-across-vpcs-in-a-region/
validation_date: 2025-11-24
target_region: cn-northwest-1, cn-north-1
feasibility: LOW
available_services: 24
unavailable_services: 0
---

# Introducing VPC encryption controls: Enforce encryption in transit within and across VPCs in a Region

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/introducing-vpc-encryption-controls-enforce-encryption-in-transit-within-and-across-vpcs-in-a-region/) | 验证日期: 2025-11-24

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心功能VPC加密控制在AWS中国区域不可用，无法实施

文章介绍的VPC加密控制（VPC Encryption Controls）是一个全新的VPC功能特性，虽然所有相关的AWS服务（VPC、EC2、Nitro等）在中国区域都可用，但该核心功能本身在AWS中国区域（cn-north-1和cn-northwest-1）尚未发布，导致文章中的所有操作步骤都无法执行。

## 服务分析

### 可用服务 (24个)

- Amazon VPC
- AWS Nitro System
- Amazon EC2
- Network Load Balancer
- Application Load Balancer
- AWS Fargate
- Amazon EKS
- Amazon ECS
- AWS PrivateLink
- AWS Transit Gateway
- Amazon RDS
- Amazon DocumentDB
- Amazon ElastiCache
- Amazon Redshift
- Amazon MSK
- Amazon OpenSearch Service
- Amazon EMR
- AWS CloudFormation
- AWS IAM
- VPC Flow Logs
- Amazon S3
- Internet Gateway
- NAT Gateway
- Auto Scaling

### 不可用服务 (0个)

无

### 评估说明

虽然文章中提到的所有AWS服务在中国区域都可用，但文章的核心主题——**VPC加密控制功能**本身在AWS中国区域不可用。这是一个区域功能可用性的问题，而非服务可用性问题。

该功能在全球区域的发布时间为2025年11月21日，支持的区域包括美国、欧洲、亚太（不含中国）、中东和南美洲的多个区域，但明确不包括AWS中国区域（cn-north-1和cn-northwest-1）。

这意味着：
1. 无法创建VPC加密控制配置
2. 无法启用监控模式或强制模式
3. 无法使用VPC Flow Logs中的encryption-status字段
4. 无法使用相关的CLI命令和API
5. 文章中的所有操作步骤都无法在中国区域执行

## 验证结果

### 验证类型

✅ 教程步骤验证

### 执行状态

**状态**: ❌ 失败

**原因**: 核心功能VPC加密控制在AWS中国区域不支持

### 关键发现

1. **VPC加密控制功能区域不可用**
   - 在cn-northwest-1和cn-north-1区域执行`create-vpc-encryption-control`命令时，返回错误：`UnsupportedOperation: The functionality you requested is not supported in this region`
   - 该功能是2025年11月21日新发布的功能，目前仅在部分全球区域可用
   - AWS中国区域未在支持区域列表中

2. **CLI命令存在但无法执行**
   - AWS CLI中存在`create-vpc-encryption-control`、`modify-vpc-encryption-control`等命令
   - 命令帮助文档可以正常显示
   - 但实际执行时会返回区域不支持的错误

3. **相关服务均可用但功能缺失**
   - VPC、EC2、Nitro System等所有相关服务在中国区域都可用
   - 但VPC加密控制作为VPC的新增功能特性，在中国区域尚未发布
   - 这是典型的功能发布时间差问题

4. **验证过程**
   - 成功在cn-northwest-1和cn-north-1创建测试VPC
   - 尝试创建VPC加密控制时均失败
   - 所有测试资源已完全清理

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此方案**

该功能是VPC的新增特性，目前在AWS中国区域完全不可用。由于这是核心功能而非可替代的服务，因此无法通过任何方式在中国区域实现文章中描述的功能。

### 替代方案

虽然无法使用VPC加密控制功能，但可以考虑以下替代方案来实现传输加密：

1. **应用层TLS加密**
   - 实施方式：在应用程序层面配置TLS/SSL加密
   - 复杂度：中
   - 适用场景：适用于所有需要加密通信的应用，但需要逐个应用配置
   - 局限性：需要管理证书、配置每个服务，无法自动强制执行

2. **使用Nitro实例的硬件加密**
   - 实施方式：确保所有EC2实例使用支持Nitro System的现代实例类型
   - 复杂度：低
   - 适用场景：EC2实例之间的通信自动加密
   - 局限性：无法审计和强制执行，无法通过VPC Flow Logs查看加密状态

3. **AWS PrivateLink + TLS**
   - 实施方式：使用AWS PrivateLink连接服务，并在应用层配置TLS
   - 复杂度：中
   - 适用场景：跨VPC的服务访问
   - 局限性：需要为每个服务单独配置，无法统一管理

4. **VPN连接**
   - 实施方式：在VPC之间建立VPN连接实现加密通信
   - 复杂度：高
   - 适用场景：跨VPC或跨区域的加密通信
   - 局限性：增加网络复杂度，可能影响性能

### 风险提示

- **合规性风险**: 如果组织需要证明VPC内所有流量都已加密（如HIPAA、PCI DSS、FedRAMP要求），在中国区域将无法使用VPC加密控制功能来实现集中审计和强制执行
- **功能缺失**: 无法使用监控模式审计加密状态，无法使用强制模式阻止未加密流量
- **可见性不足**: VPC Flow Logs中不会包含encryption-status字段，无法通过日志分析加密状态
- **未来可用性不确定**: 该功能何时在AWS中国区域发布尚无明确时间表
- **架构差异**: 如果在全球区域和中国区域都有部署，需要维护不同的安全架构和合规验证方法

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 不适用

---

**验证结论**: 该功能在AWS中国区域完全不可用，建议等待AWS官方在中国区域发布该功能后再考虑实施。如有传输加密需求，请采用上述替代方案。
