---
title: 使用AWS Backup中对Amazon EKS的新支持保护EKS集群
publish_date: 2025-11-10
original_url: https://aws.amazon.com/blogs/aws/secure-eks-clusters-with-the-new-support-for-amazon-eks-in-aws-backup/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 7
unavailable_services: 0
---

# 使用AWS Backup中对Amazon EKS的新支持保护EKS集群

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/secure-eks-clusters-with-the-new-support-for-amazon-eks-in-aws-backup/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心功能在中国区域不可用，无法实施

博客介绍的核心功能"AWS Backup对Amazon EKS的支持"明确不支持中国区域。原文明确说明："Support for Amazon EKS in AWS Backup is available today in all AWS commercial Regions (except China)"。经API验证，AWS Backup在cn-northwest-1区域不支持EKS资源类型。

## 服务分析

### 可用服务 (7个)

- Amazon EKS (Amazon Elastic Kubernetes Service)
- AWS Backup
- Amazon EBS (Amazon Elastic Block Store)
- Amazon EFS (Amazon Elastic File System)
- Amazon S3 (Amazon Simple Storage Service)
- AWS KMS (AWS Key Management Service)
- IAM (Identity and Access Management)

### 不可用服务 (0个)

无

### 评估说明

虽然博客中提到的所有AWS服务在中国区域都可用，但博客介绍的核心功能——AWS Backup对Amazon EKS的原生支持——在中国区域不可用。这是一个区域功能限制，而非服务可用性问题。

通过AWS CLI验证，AWS Backup在cn-northwest-1区域支持的资源类型包括：DynamoDB、EBS、RDS、Storage Gateway、EFS、Aurora、Redshift、DocumentDB、Neptune、EC2、FSx、S3、CloudFormation、Redshift Serverless，但不包括EKS。

这意味着无法使用博客中介绍的方法在中国区域通过AWS Backup统一管理和自动化EKS集群的备份与恢复。

## 验证结果

### 验证类型

- ⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心功能在中国区域不可用，可行性评估为LOW，无需进行深入验证

### 关键发现

1. **区域功能限制**
   - AWS Backup在中国区域不支持EKS资源类型
   - 博客明确说明该功能不支持中国区域
   - 通过API验证确认了这一限制

2. **服务可用性与功能可用性的区别**
   - 所有相关AWS服务（EKS、Backup、EBS、EFS、S3等）在中国区域都可用
   - 但服务之间的集成功能（AWS Backup对EKS的支持）不可用

## 实施建议

### 推荐方案

不建议在中国区域实施博客中介绍的方案，因为核心功能不可用。

### 替代方案

如需在中国区域备份EKS集群，可考虑以下替代方案：

1. **Velero开源工具**
   - 实施方式：使用Velero（CNCF项目）进行EKS集群备份和恢复
   - 复杂度：中
   - 适用场景：需要跨云平台的Kubernetes备份解决方案，支持备份到S3
   - 优势：成熟的开源方案，社区支持良好，可备份到Amazon S3
   - 劣势：需要自行管理和维护，无法与AWS Backup统一管理

2. **自定义脚本方案**
   - 实施方式：使用kubectl、AWS CLI和自定义脚本备份EKS资源和持久卷
   - 复杂度：高
   - 适用场景：有定制化需求，团队有Kubernetes和AWS运维经验
   - 优势：完全可控，可根据需求定制
   - 劣势：开发和维护成本高，缺乏统一管理界面

3. **分离备份策略**
   - 实施方式：
     - 使用AWS Backup备份EBS、EFS等持久存储资源
     - 使用Kubernetes原生工具或第三方工具备份集群配置和应用定义
   - 复杂度：中
   - 适用场景：可接受分离管理备份的场景
   - 优势：充分利用AWS Backup的现有能力
   - 劣势：无法统一管理，恢复流程较复杂

### 风险提示

- **功能不可用风险**: 博客介绍的核心功能在中国区域完全不可用，无法通过配置调整解决
- **替代方案复杂度**: 所有替代方案都需要额外的开发、部署和维护工作
- **管理分散风险**: 替代方案无法与AWS Backup统一管理，增加运维复杂度
- **功能差异风险**: 替代方案可能无法完全实现AWS Backup的所有功能特性（如不可变备份、跨区域复制等）

### 配套资源

- **GitHub仓库**: 无
- **官方文档**: [AWS Backup文档](https://docs.aws.amazon.com/aws-backup/)
- **Velero项目**: [https://velero.io/](https://velero.io/)
- **区域可用性**: [AWS Backup区域支持列表](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#supported-services-by-region)
