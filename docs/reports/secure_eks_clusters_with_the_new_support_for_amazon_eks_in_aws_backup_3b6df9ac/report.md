---
title: Secure EKS clusters with the new support for Amazon EKS in AWS Backup
original_url: https://aws.amazon.com/blogs/aws/secure-eks-clusters-with-the-new-support-for-amazon-eks-in-aws-backup/
validation_date: 2025-11-24
target_region: cn-northwest-1
feasibility: LOW
available_services: 7
unavailable_services: 0
---

# Secure EKS clusters with the new support for Amazon EKS in AWS Backup

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/secure-eks-clusters-with-the-new-support-for-amazon-eks-in-aws-backup/) | 验证日期: 2025-11-24

## 可行性评估

!!! danger "LOW - 不建议实施"
    该功能明确不支持中国区域，无法在AWS中国区域实施

博客内容明确指出："Support for Amazon EKS in AWS Backup is available today in all AWS commercial Regions **(except China)**"。这是AWS Backup对EKS支持的区域功能限制，与服务可用性无关。

## 服务分析

### 可用服务 (7个)

- Amazon EKS (Elastic Kubernetes Service)
- AWS Backup
- Amazon EBS (Elastic Block Store)
- Amazon EFS (Elastic File System)
- Amazon S3 (Simple Storage Service)
- AWS KMS (Key Management Service)
- IAM (Identity and Access Management)

### 不可用服务 (0个)

无

### 评估说明

虽然博客中涉及的所有AWS服务在中国区域都可用，但**AWS Backup对Amazon EKS的集成支持功能**在中国区域不可用。这是一个特定功能的区域限制，而非服务本身的可用性问题。

关键限制：
1. AWS Backup无法直接备份和恢复EKS集群（包括集群配置和持久化存储）
2. 无法使用AWS Backup控制台、API或CLI对EKS集群进行统一的备份管理
3. 无法利用AWS Backup的策略驱动、集中化备份能力来保护EKS工作负载

## 验证结果

### 验证类型

⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 博客内容明确说明该功能不支持中国区域，无需进行实际部署验证。这是AWS官方文档确认的区域功能限制。

## 实施建议

### 推荐方案

**不建议直接实施**

由于AWS Backup对EKS的原生集成支持在中国区域不可用，无法按照博客内容实施该解决方案。

### 替代方案

如需在AWS中国区域备份EKS集群，可考虑以下替代方案：

1. **Velero (开源工具)**
   - 实施方式：部署Velero到EKS集群，配置S3作为备份存储后端
   - 复杂度：中
   - 适用场景：需要完整的EKS集群备份和恢复能力，包括Kubernetes资源和持久化卷
   - 优势：成熟的开源解决方案，社区支持良好
   - 劣势：需要自行管理和维护，无法与AWS Backup统一管理

2. **自定义脚本方案**
   - 实施方式：
     - 使用kubectl导出Kubernetes资源配置
     - 使用AWS Backup分别备份EBS、EFS等持久化存储
     - 编写自动化脚本协调备份流程
   - 复杂度：高
   - 适用场景：对备份有特定需求，需要精细控制备份内容
   - 优势：灵活可定制
   - 劣势：开发和维护成本高，缺乏统一管理界面

3. **AWS Backup单独备份存储资源**
   - 实施方式：使用AWS Backup仅备份EBS卷、EFS文件系统等存储资源，Kubernetes配置单独管理
   - 复杂度：中
   - 适用场景：主要关注数据保护，集群配置变更较少
   - 优势：可利用AWS Backup的部分能力
   - 劣势：无法实现集群配置和数据的统一备份恢复

### 风险提示

- **功能缺失风险**: 中国区域无法使用AWS Backup的EKS集成功能，需要额外的工具和流程
- **管理复杂度**: 替代方案无法提供与AWS Backup相同的集中化、策略驱动的管理体验
- **恢复时间**: 使用替代方案可能增加灾难恢复的复杂度和时间
- **合规性考虑**: 如果有不可变备份、加密备份等合规要求，需要在替代方案中单独实现

### 配套资源

- **GitHub仓库**: 无
- **相关文档**: 
  - [Velero官方文档](https://velero.io/docs/)
  - [AWS Backup文档](https://docs.amazonaws.cn/aws-backup/)
  - [Amazon EKS最佳实践指南](https://aws.github.io/aws-eks-best-practices/)
