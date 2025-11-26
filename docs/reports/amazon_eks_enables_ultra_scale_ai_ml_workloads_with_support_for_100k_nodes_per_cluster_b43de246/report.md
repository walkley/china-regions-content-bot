---
title: Amazon EKS 支持超大规模 AI/ML 工作负载，单集群可达 100K 节点
publish_date: 2025-07-16
original_url: https://aws.amazon.com/blogs/containers/amazon-eks-enables-ultra-scale-ai-ml-workloads-with-support-for-100k-nodes-per-cluster/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 5
unavailable_services: 0
---

# Amazon EKS 支持超大规模 AI/ML 工作负载，单集群可达 100K 节点

[📖 查看原始博客](https://aws.amazon.com/blogs/containers/amazon-eks-enables-ultra-scale-ai-ml-workloads-with-support-for-100k-nodes-per-cluster/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文介绍的 Amazon EKS 超大规模集群能力（支持最多 100K 节点）所涉及的所有服务在 AWS 中国区域均可用，客户可以充分利用这一能力来运行大规模 AI/ML 工作负载。

## 服务分析

### 可用服务 (5个)

- Amazon EKS (Amazon Elastic Kubernetes Service)
- Amazon EC2 (包括加速计算实例类型)
- AWS Trainium
- AWS Graviton
- Amazon SageMaker HyperPod

### 不可用服务 (0个)

无

### 评估说明

本文所有提到的核心服务在 AWS 中国区域均完全可用：

1. **Amazon EKS** - 核心服务，在中国区域完全支持，包括超大规模集群能力
2. **Amazon EC2 加速计算实例** - Trainium (Trn2) 和 GPU 实例在中国区域可用
3. **AWS Graviton** - 基于 ARM 架构的处理器，在中国区域 EC2 实例中可用
4. **Amazon SageMaker HyperPod** - 用于大规模机器学习训练的托管服务，在中国区域可用

所有服务均为核心服务，无替代需求。客户可以直接在中国区域利用 EKS 的超大规模能力来运行 AI/ML 工作负载。

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 本文为产品功能公告博客，主要介绍 Amazon EKS 支持 100K 节点集群的新能力以及客户案例分享（Anthropic 和 Amazon AGI 团队），不包含配套的 GitHub 项目或具体的操作教程步骤，因此无需进行部署验证或步骤验证。

## 实施建议

### 推荐方案

可直接按照原文理解和规划实施：

- **核心能力**：Amazon EKS 在中国区域支持超大规模集群（最多 100K 节点），可用于大规模 AI/ML 训练和推理工作负载
- **适用场景**：
  - 大规模 AI/ML 模型训练（需要协调数千个 GPU 或 AI 加速器）
  - 统一环境中整合训练、微调和推理工作负载
  - 需要使用开源 Kubernetes 工具和框架的 AI/ML 项目

- **注意事项**：
  - 确认所需的 EC2 实例类型（如 Trn2、P5e、P6）在目标中国区域的可用性和配额
  - 超大规模集群需要与 AWS 账户团队联系以获取支持和最佳实践指导
  - 考虑网络架构和 VPC 配置以支持大规模节点部署
  - 评估 etcd 存储和控制平面的性能优化需求

### 替代方案

无需替代方案，所有服务均可用。

### 风险提示

- **配额限制**：超大规模集群部署需要提前申请 EC2 实例配额，特别是加速计算实例（GPU/Trainium）
- **成本管理**：大规模 AI/ML 工作负载会产生显著的计算成本，建议使用成本监控和优化工具
- **网络规划**：100K 节点集群对网络架构有较高要求，需要仔细规划 VPC、子网和安全组配置
- **运维复杂度**：超大规模集群的运维管理需要专业的 Kubernetes 和 AWS 经验，建议与 AWS 团队合作

### 配套资源

本文为功能公告，无配套 GitHub 项目。

如需了解技术实现细节，原文提到了一篇深度技术博客（deep dive blog），建议查阅该文档以了解架构决策和实现方案。客户可联系 AWS 账户团队获取更多关于超大规模集群能力的技术支持和最佳实践。
