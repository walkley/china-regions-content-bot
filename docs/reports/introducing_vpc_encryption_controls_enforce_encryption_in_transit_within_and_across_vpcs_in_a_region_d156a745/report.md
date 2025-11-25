---
title: 介绍VPC加密控制：在区域内和跨VPC强制执行传输中加密
publish_date: 2025-11-21
original_url: https://aws.amazon.com/blogs/aws/introducing-vpc-encryption-controls-enforce-encryption-in-transit-within-and-across-vpcs-in-a-region/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 22
unavailable_services: 0
---

# 介绍VPC加密控制：在区域内和跨VPC强制执行传输中加密

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/introducing-vpc-encryption-controls-enforce-encryption-in-transit-within-and-across-vpcs-in-a-region/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心功能VPC加密控制在中国区域不可用，无法实施

博客介绍的VPC加密控制（VPC Encryption Controls）是Amazon VPC的新功能特性，用于审计和强制执行VPC内及跨VPC的传输加密。虽然博客中提到的所有AWS服务在中国区域都可用，但该核心功能本身在中国区域（cn-north-1和cn-northwest-1）尚未发布，导致无法实施博客中描述的任何操作。

## 服务分析

### 可用服务 (22个)

- Amazon VPC (Virtual Private Cloud)
- Amazon EC2 (Elastic Compute Cloud)
- AWS Nitro System
- Network Load Balancer
- Application Load Balancer
- AWS Fargate
- Amazon EKS (Elastic Kubernetes Service)
- Amazon ECS (Elastic Container Service)
- Amazon RDS (Relational Database Service)
- Amazon DocumentDB
- Amazon ElastiCache
- Amazon Redshift
- Amazon MSK (Managed Streaming for Apache Kafka)
- Amazon OpenSearch Service
- Amazon EMR (Elastic MapReduce)
- AWS Transit Gateway
- AWS PrivateLink
- AWS CloudFormation
- AWS IAM (Identity and Access Management)
- AWS CLI (Command Line Interface)
- VPC Flow Logs
- Auto Scaling

### 不可用服务 (0个)

无

### 评估说明

虽然博客中提到的所有AWS基础服务在中国区域都可用，但博客的核心主题——VPC加密控制功能——在中国区域尚未发布。

根据博客中的区域可用性说明，VPC加密控制功能目前在以下区域可用：
- 美国东部（俄亥俄、弗吉尼亚北部）
- 美国西部（加利福尼亚北部、俄勒冈）
- 非洲（开普敦）
- 亚太地区（香港、海得拉巴、雅加达、墨尔本、孟买、大阪、新加坡、悉尼、东京）
- 加拿大（中部、卡尔加里）
- 欧洲（法兰克福、爱尔兰、伦敦、米兰、巴黎、斯德哥尔摩、苏黎世）
- 中东（巴林、阿联酋）
- 南美洲（圣保罗）

**中国区域（cn-north-1、cn-northwest-1）未在支持列表中。**

实际验证中，尝试调用以下API均返回"UnsupportedOperation"错误：
- `create-vpc-encryption-control`
- `describe-vpc-encryption-controls`

错误信息明确指出："The functionality you requested is not supported in this region."

## 验证结果

### 验证类型

- ✅ 教程步骤验证

### 执行状态

**状态**: ❌ 失败

**原因**: VPC加密控制功能在cn-northwest-1区域不可用，无法执行博客中的任何操作步骤

### 关键发现

1. **核心功能区域限制**
   - VPC加密控制是一个新发布的功能特性，目前仅在全球部分区域可用
   - 中国区域（cn-north-1和cn-northwest-1）不在首批支持区域列表中
   - AWS CLI已包含相关命令（create-vpc-encryption-control、describe-vpc-encryption-controls等），但在中国区域调用时返回"UnsupportedOperation"错误

2. **功能依赖性**
   - VPC加密控制的两个核心模式（监控模式和强制模式）都无法在中国区域启用
   - VPC Flow Logs的加密状态字段（encryption-status）依赖于VPC加密控制功能，在中国区域无法使用
   - Transit Gateway的加密支持配置也依赖于该功能

3. **底层加密能力仍然可用**
   - 虽然VPC加密控制功能不可用，但AWS Nitro System的硬件层加密能力在中国区域的Nitro实例上仍然有效
   - 应用层TLS加密不受影响，可以继续使用
   - 这意味着加密本身是可行的，只是缺少集中化的审计和强制执行机制

## 实施建议

### 推荐方案

**不建议直接实施**

由于VPC加密控制功能在中国区域不可用，无法按照博客内容实施。建议采取以下替代策略：

1. **等待功能发布**
   - 关注AWS中国区域的功能发布公告
   - VPC加密控制是2025年11月21日发布的新功能，中国区域通常会在全球发布后的几个月内跟进

2. **使用现有加密能力**
   - 选择基于AWS Nitro System的实例类型（如M6g、M7g、C6g、C7g等），自动获得硬件层加密
   - 在应用层实施TLS加密，确保数据传输安全
   - 使用AWS PrivateLink和VPC Endpoint，这些服务强制使用TLS加密

### 替代方案

1. **手动审计和管理加密合规性**
   - 实施方式：
     - 制定实例类型白名单，仅允许使用支持Nitro System的实例类型
     - 使用AWS Config规则监控实例类型合规性
     - 通过IAM策略限制创建非Nitro实例的权限
     - 在应用层强制使用TLS/SSL证书
   - 复杂度：中
   - 适用场景：需要确保加密合规但VPC加密控制功能不可用的情况

2. **使用第三方网络加密解决方案**
   - 实施方式：
     - 部署IPsec VPN或WireGuard等网络层加密方案
     - 使用服务网格（如Istio）实现应用间mTLS加密
     - 配置网络策略确保所有流量经过加密通道
   - 复杂度：高
   - 适用场景：有严格合规要求且需要端到端加密证明的场景

3. **AWS Config + Lambda自动化合规检查**
   - 实施方式：
     - 使用AWS Config持续监控资源配置
     - 创建自定义Config规则检查实例类型是否支持加密
     - 使用Lambda函数自动标记或通知不合规资源
     - 生成合规报告用于审计
   - 复杂度：中
   - 适用场景：需要自动化合规监控和报告的场景

### 风险提示

- **合规性风险**: 如果组织有严格的加密合规要求（如HIPAA、PCI DSS、FedRAMP），缺少VPC加密控制功能可能导致难以证明端到端加密合规性
- **运维复杂度**: 替代方案需要手动管理和审计，增加运维负担和人为错误风险
- **功能差距**: 替代方案无法提供VPC加密控制的强制模式，无法在网络层自动阻止未加密流量
- **迁移成本**: 当VPC加密控制功能在中国区域发布后，从替代方案迁移到原生功能可能需要额外的工作量

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 不适用
