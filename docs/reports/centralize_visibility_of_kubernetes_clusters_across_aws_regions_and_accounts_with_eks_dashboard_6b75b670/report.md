---
title: 使用EKS Dashboard集中查看跨AWS区域和账户的Kubernetes集群
publish_date: 2025-05-21
original_url: https://aws.amazon.com/blogs/aws/centralize-visibility-of-kubernetes-clusters-across-aws-regions-and-accounts-with-eks-dashboard/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 3
unavailable_services: 0
---

# 使用EKS Dashboard集中查看跨AWS区域和账户的Kubernetes集群

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/centralize-visibility-of-kubernetes-clusters-across-aws-regions-and-accounts-with-eks-dashboard/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    虽然所有底层服务在中国区可用，但EKS Dashboard功能本身不支持中国区域

EKS Dashboard是一个控制台级别的功能，博客明确说明该功能仅在US East (N. Virginia)区域可用，且仅聚合商业AWS区域（commercial AWS Regions）的数据。AWS中国区域作为独立分区（由光环新网和西云数据运营），不属于商业AWS区域范畴，因此无法使用此Dashboard功能。

## 服务分析

### 可用服务 (3个)

- Amazon EKS (Amazon Elastic Kubernetes Service)
- AWS Console
- AWS Organizations

### 不可用服务 (0个)

无 - 所有提到的AWS服务在中国区域都可用

### 评估说明

这是一个特殊情况：虽然博客中提到的所有AWS服务（EKS、Console、Organizations）在中国区域都完全可用，但**EKS Dashboard本身是一个区域限定的控制台功能**，而非独立的AWS服务。

根据博客原文：
> "Amazon EKS Dashboard is available today in the US East (N. Virginia) Region and is able to aggregate data from all commercial AWS Regions."

关键限制：
1. **区域限制**：Dashboard功能仅在us-east-1区域提供
2. **分区隔离**：AWS中国区域（aws-cn分区）与全球商业区域（aws分区）是完全独立的分区，无法跨分区聚合数据
3. **功能不可用**：中国区域的EKS控制台不包含Dashboard功能

## 验证结果

### 验证类型

- ✅ 教程步骤验证

### 执行状态

**状态**: ❌ 失败

**原因**: EKS Dashboard功能在中国区域不可用

### 关键发现

1. **底层服务完全可用**
   - Amazon EKS在cn-northwest-1和cn-north-1区域完全可用
   - AWS Organizations在中国区域正常工作
   - 可以正常创建和管理EKS集群

2. **Dashboard功能缺失**
   - EKS控制台中没有Dashboard功能入口
   - AWS CLI中没有dashboard相关的API命令
   - 这是一个仅在全球商业区域提供的控制台功能

3. **分区隔离限制**
   - AWS中国区域（aws-cn）与全球区域（aws）是独立分区
   - 即使Dashboard功能可用，也无法跨分区聚合数据
   - 中国区域需要独立的可见性解决方案

## 实施建议

### 推荐方案

**不建议直接实施** - EKS Dashboard功能在中国区域不可用，无法按照博客内容实施。

### 替代方案

对于需要在AWS中国区域实现EKS集群集中可见性的客户，可以考虑以下替代方案：

1. **使用AWS Systems Manager - Explorer**
   - 实施方式：通过Systems Manager Explorer聚合多账户、多区域的资源视图
   - 复杂度：中
   - 适用场景：需要跨账户资源可见性，但不限于EKS集群
   - 限制：需要配置Resource Data Sync和Organizations集成

2. **使用AWS Config聚合器**
   - 实施方式：配置AWS Config多账户多区域聚合器，创建自定义查询和仪表板
   - 复杂度：中
   - 适用场景：需要合规性跟踪和资源清单管理
   - 优势：可以跟踪配置变更历史

3. **自建监控方案**
   - 实施方式：使用AWS CLI/SDK定期收集EKS集群信息，存储到中央数据库，使用Grafana/QuickSight可视化
   - 复杂度：高
   - 适用场景：需要高度定制化的可见性和监控需求
   - 示例工具链：
     - 数据收集：Lambda + EventBridge定时任务
     - 数据存储：DynamoDB或RDS
     - 可视化：Amazon QuickSight或自托管Grafana

4. **第三方Kubernetes管理平台**
   - 实施方式：使用Rancher、Lens等第三方工具管理多集群
   - 复杂度：中到高
   - 适用场景：已有第三方工具使用经验，需要跨云管理能力
   - 注意：需要考虑许可成本和维护开销

### 风险提示

- **功能差异**：AWS中国区域的某些控制台功能可能晚于全球区域发布或不提供
- **分区隔离**：中国区域与全球区域完全隔离，无法使用全球区域的管理工具
- **替代方案成本**：自建或第三方方案可能产生额外的开发、维护和许可成本
- **数据主权**：使用第三方工具时需确保符合中国数据合规要求

### 配套资源

- **GitHub仓库**: 无
- **官方文档**: [Amazon EKS Dashboard文档](https://docs.aws.amazon.com/eks/latest/userguide/cluster-dashboard.html)（仅适用于全球区域）
- **中国区域EKS文档**: [Amazon EKS用户指南](https://docs.amazonaws.cn/eks/latest/userguide/)
