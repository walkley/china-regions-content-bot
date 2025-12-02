---
title: 宣布推出用于工作负载编排和云资源管理的 Amazon EKS Capabilities
publish_date: 2025-11-30
original_url: https://aws.amazon.com/blogs/aws/announcing-amazon-eks-capabilities-for-workload-orchestration-and-cloud-resource-management/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 3
unavailable_services: 1
---

# 宣布推出用于工作负载编排和云资源管理的 Amazon EKS Capabilities

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/announcing-amazon-eks-capabilities-for-workload-orchestration-and-cloud-resource-management/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心功能 EKS Capabilities 在中国区域不可用，无法按照原文实施

文章介绍的核心功能 Amazon EKS Capabilities 是一个全新的托管服务特性，目前在中国区域尚未推出。虽然底层的 EKS 服务可用，但 Capabilities 功能（包括托管的 Argo CD、ACK、KRO）在中国区域的 EKS API 中不存在。

## 服务分析

### 可用服务 (3个)

- Amazon EKS (基础服务)
- AWS IAM
- AWS CloudFormation

### 不可用服务 (1个)

- **Amazon EKS Capabilities** - 核心服务
  - 包括托管的 Argo CD
  - 包括托管的 AWS Controllers for Kubernetes (ACK)
  - 包括托管的 Kube Resource Orchestrator (KRO)

### 评估说明

通过 AWS CLI 验证发现，中国区域（cn-northwest-1）的 EKS 服务不支持 `list-capabilities` 等 Capabilities 相关的 API 操作。这表明 EKS Capabilities 功能尚未在中国区域发布。

虽然 Amazon EKS 基础服务在中国区域可用，但本文介绍的核心特性——EKS Capabilities（一个扩展的 Kubernetes 原生解决方案集）完全不可用。这意味着：

1. 无法通过 EKS 控制台的 "Capabilities" 标签页创建托管能力
2. 无法使用 AWS 托管的 Argo CD、ACK、KRO
3. 文章中展示的所有控制台操作步骤在中国区域无法执行

## 验证结果

### 验证类型

- ⏭️ 已跳过（核心功能不可用）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 通过 AWS CLI 验证确认 EKS Capabilities 功能在中国区域（cn-northwest-1）不可用，无法进行实际部署验证。

### 关键发现

1. **EKS Capabilities API 不存在**
   - 中国区域的 EKS CLI 不包含 `list-capabilities`、`create-capability` 等命令
   - 这是区域功能差异，而非配置问题

2. **服务发布时间差异**
   - 文章发布于 2025-11-30，宣布在商业区域可用
   - 中国区域通常在全球区域之后获得新功能
   - 需要等待 AWS 中国正式宣布支持

## 实施建议

### 推荐方案

**不建议直接实施**

由于 EKS Capabilities 是一个完全托管的服务特性，在中国区域不可用的情况下，无法通过任何配置或调整来实现文章中描述的功能。

### 替代方案

如果需要在中国区域的 EKS 集群中实现类似功能，可以考虑以下自建方案：

1. **自行部署 Argo CD**
   - 实施方式：在 EKS 集群中手动安装开源 Argo CD
   - 复杂度：中
   - 适用场景：需要 GitOps 持续部署能力
   - 注意事项：需要自行管理升级、补丁和高可用性配置

2. **自行部署 ACK (AWS Controllers for Kubernetes)**
   - 实施方式：在集群中安装 ACK 控制器
   - 复杂度：中到高
   - 适用场景：需要从 Kubernetes 管理 AWS 资源
   - 注意事项：需要配置 IAM 角色和权限，自行维护控制器版本

3. **自行部署 KRO (Kube Resource Orchestrator)**
   - 实施方式：在集群中安装开源 KRO
   - 复杂度：中
   - 适用场景：需要创建自定义资源包和抽象
   - 注意事项：需要自行管理和维护

### 风险提示

- **维护负担**：自建方案需要平台团队负责所有组件的安装、升级、补丁和故障排除，这正是 EKS Capabilities 试图解决的问题
- **安全更新**：需要持续关注各开源项目的安全公告并及时更新
- **集成复杂性**：自建方案之间的集成需要额外配置，不如托管服务的无缝集成
- **功能差异**：EKS Capabilities 运行在 AWS 服务账户中，与自建方案的架构和权限模型不同
- **等待官方支持**：建议关注 AWS 中国的产品发布公告，等待 EKS Capabilities 正式支持

### 配套资源

- **GitHub仓库**: 文章未提供专门的配套代码仓库
- **开源项目**:
  - Argo CD: https://github.com/argoproj/argo-cd
  - ACK: https://github.com/aws-controllers-k8s/community
  - KRO: https://kro.run/
- **兼容性**: 开源版本可在中国区域的 EKS 集群中自行安装使用

## 总结

Amazon EKS Capabilities 是一个创新的托管服务特性，但目前仅在全球商业区域可用。中国区域用户如需类似功能，只能采用传统的自建开源方案，这意味着需要承担额外的运维负担。建议持续关注 AWS 中国的产品路线图，等待该功能的正式发布。
