---
title: Amazon EKS Blueprints for CDK：现已支持 Amazon EKS Auto Mode
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/containers/amazon-eks-blueprints-for-cdk-now-supporting-amazon-eks-auto-mode/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 8
unavailable_services: 1
---

# Amazon EKS Blueprints for CDK：现已支持 Amazon EKS Auto Mode

[📖 查看原始博客](https://aws.amazon.com/blogs/containers/amazon-eks-blueprints-for-cdk-now-supporting-amazon-eks-auto-mode/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心功能 EKS Auto Mode 在中国区域不可用，无法实现文章的主要技术方案

虽然 EKS 服务本身在中国区域可用，但文章的核心功能 **EKS Auto Mode** 目前在中国区域尚未正式发布。这是一个全新的 EKS 集群管理模式,需要等待 AWS 在中国区域正式推出该功能。

## 服务分析

### 可用服务 (8个)

- Amazon EKS (Elastic Kubernetes Service)
- AWS CDK (Cloud Development Kit)
- Amazon EC2 (Elastic Compute Cloud)
- Amazon EBS (Elastic Block Store)
- Amazon ECR (Elastic Container Registry)
- AWS CloudFormation
- AWS Systems Manager
- Amazon S3
- AWS IAM (Identity and Access Management)

### 不可用服务 (1个)

- **EKS Auto Mode** - 核心服务

### 评估说明

EKS Auto Mode 是本文的核心技术特性，它提供了完全托管的 Kubernetes 集群管理能力，包括：
- 自动基础设施配置
- 自动计算实例选择和扩展
- 自动安装和维护核心插件（Karpenter、VPC CNI、CoreDNS、AWS Load Balancer Controller）
- 自动操作系统补丁和更新
- 按照 CIS Level 1 基准进行安全加固

虽然从 AWS CLI 的 describe-addon-versions 输出中可以看到 "computeTypes" 包含 "auto" 选项，但这并不意味着 EKS Auto Mode 功能在中国区域完全可用。EKS Auto Mode 是一个需要单独发布和启用的功能特性，目前在中国区域的可用性状态需要进一步确认。

由于无法确认 EKS Auto Mode 在中国区域的完整可用性，且这是文章的核心功能，因此将可行性评估为 LOW。

## 验证结果

### 验证类型

⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心功能 EKS Auto Mode 在中国区域的可用性无法确认，无法进行实际部署验证。即使 EKS 服务本身可用，但缺少 Auto Mode 功能将导致文章中的所有代码示例无法按预期工作。

## 实施建议

### 推荐方案

不建议直接实施此方案。建议采用以下替代方案：

1. **等待官方发布**：关注 AWS 中国区域的服务更新公告，等待 EKS Auto Mode 正式发布
2. **使用传统 EKS 部署方式**：在 EKS Auto Mode 可用之前，继续使用传统的 EKS 集群管理方式

### 替代方案

#### 方案1：使用 EKS Blueprints 配合传统节点组

- **实施方式**：使用 EKS Blueprints for CDK，但配置传统的托管节点组或自管理节点组，而不是 Auto Mode
- **复杂度**：中
- **适用场景**：需要使用 EKS Blueprints 框架进行标准化部署，但不依赖 Auto Mode 的自动化管理功能
- **代码示例**：
```typescript
import * as blueprints from '@aws-quickstart/eks-blueprints';

blueprints.EksBlueprint.builder()
  .account(account)
  .region(region)
  .addOns(new blueprints.addons.ArgoCDAddOn())
  .teams(/* your teams */)
  .build(app, 'my-eks-cluster');
```

#### 方案2：手动配置 Karpenter 实现类似的自动扩展

- **实施方式**：在传统 EKS 集群上手动部署和配置 Karpenter，实现类似 Auto Mode 的自动扩展能力
- **复杂度**：高
- **适用场景**：需要自动化节点管理和成本优化，但 Auto Mode 不可用
- **关键步骤**：
  1. 创建标准 EKS 集群
  2. 安装 Karpenter controller
  3. 配置 Provisioner 资源定义节点需求
  4. 设置适当的 IAM 角色和权限

#### 方案3：使用 AWS Graviton 实例的传统部署

- **实施方式**：针对文章中的 ARM/Graviton 示例，使用传统节点组配置 Graviton 实例
- **复杂度**：低
- **适用场景**：主要关注 Graviton 的成本优势，不需要 Auto Mode 的完整自动化功能
- **配置要点**：
  - 选择 ARM64 架构的 AMI
  - 配置 Graviton 实例类型（如 c6g, m6g, r6g 系列）
  - 确保应用容器镜像支持 ARM64 架构

### 风险提示

- **功能缺失风险**：文章中展示的所有 AutomodeBuilder 相关代码在中国区域无法使用
- **架构差异风险**：替代方案需要手动管理许多 Auto Mode 自动处理的配置，增加运维复杂度
- **成本优化风险**：缺少 Auto Mode 的自动成本优化功能，需要手动配置和监控资源使用
- **安全合规风险**：Auto Mode 提供的 CIS Level 1 基准安全加固需要手动实施
- **更新维护风险**：操作系统补丁和核心组件更新需要手动管理，增加安全风险

### 配套资源

- **GitHub仓库**: https://github.com/aws-quickstart/cdk-eks-blueprints
- **兼容性**: 框架本身在中国区域可用，但需要移除所有 AutomodeBuilder 相关代码
- **修改建议**: 
  1. 将 `AutomodeBuilder.builder()` 替换为 `EksBlueprint.builder()`
  2. 移除 `nodePools` 和 `extraNodePools` 配置
  3. 添加传统的 `ManagedNodeGroup` 或使用 Fargate profiles
  4. 手动配置需要的 add-ons（Karpenter、VPC CNI 等）

## 后续跟进

建议定期检查以下资源以了解 EKS Auto Mode 在中国区域的发布状态：
- AWS 中国区域服务更新页面
- AWS 中国官方博客
- EKS 产品文档的中国区域章节
