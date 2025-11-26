---
title: 从创新到影响：AWS与NVIDIA如何助力真实世界的生成式AI成功
publish_date: 2025-03-19
original_url: https://aws.amazon.com/blogs/machine-learning/from-innovation-to-impact-how-aws-and-nvidia-enable-real-world-generative-ai-success/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: MODERATE
available_services: 8
unavailable_services: 1
---

# 从创新到影响：AWS与NVIDIA如何助力真实世界的生成式AI成功

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/from-innovation-to-impact-how-aws-and-nvidia-enable-real-world-generative-ai-success/) | 验证日期: 2025-11-25

## 可行性评估

!!! warning "MODERATE - 谨慎实施"
    大部分服务可用，需要适当调整

核心基础设施服务（EC2 GPU实例、SageMaker、EKS、存储、网络）在中国区全部可用，但Amazon Bedrock托管模型服务不可用，需要使用自托管模型方案。

## 服务分析

### 可用服务 (8个)

- Amazon EC2 (包括P5en、P5、P4de、G5等GPU实例)
- Amazon FSx for Lustre
- Amazon EKS (Elastic Kubernetes Service)
- Elastic Fabric Adapter (EFA)
- Amazon SageMaker HyperPod
- Amazon SageMaker AI
- Amazon S3
- Amazon FSx

### 不可用服务 (1个)

- **Amazon Bedrock** - 托管基础模型服务

### 评估说明

本文是一篇关于AWS与NVIDIA合作的案例分享文章，介绍了多个客户（Adobe、Perplexity、ServiceNow、Cisco、Hippocratic AI）如何使用AWS和NVIDIA技术构建生成式AI解决方案。

**核心服务可用性：**
- 所有核心基础设施服务（GPU计算、存储、网络、容器编排）在中国区完全可用
- 文章中提到的主要技术架构模式（自托管模型训练和推理）可以在中国区实施

**不可用服务影响：**
- Amazon Bedrock在文中主要作为可选的托管服务方案提及（如Perplexity和Cisco的案例）
- 不影响文章介绍的核心技术架构和最佳实践
- 可以使用SageMaker AI自托管模型作为替代方案

**服务可用性比例：** 88.9% (8/9)

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 本文是案例分享和技术洞察文章，不包含配套的GitHub项目或具体的操作步骤，无需进行实际部署验证。

## 实施建议

### 推荐方案

本文适合作为技术参考和架构设计灵感，文中介绍的技术模式和最佳实践可以在中国区域应用：

**可直接应用的技术模式：**
- 使用EC2 GPU实例（P5、P4de、G5等）进行模型训练和推理
- 使用SageMaker HyperPod进行分布式训练
- 使用FSx for Lustre提供高性能存储
- 使用EFA网络加速GPU间通信
- 使用EKS进行容器化部署和编排
- 使用NVIDIA软件栈（TensorRT、Triton Inference Server等）优化推理性能

**需要调整的部分：**
- 将Amazon Bedrock替换为SageMaker AI自托管模型方案
- 如需使用托管模型服务，考虑使用第三方模型API或自建模型服务

**预计工作量：** 低 - 主要是概念和架构参考，实际实施需根据具体业务场景设计

### 替代方案

针对Amazon Bedrock不可用的情况：

1. **SageMaker AI自托管方案**
   - 实施方式：使用SageMaker Endpoints部署开源或自训练模型，配合NVIDIA Triton Inference Server
   - 复杂度：中
   - 适用场景：需要完全控制模型和推理环境，对性能和成本有精细化要求

2. **第三方模型API服务**
   - 实施方式：集成国内可用的大模型API服务（如阿里云通义千问、百度文心一言等）
   - 复杂度：低
   - 适用场景：快速原型开发，不需要自建模型基础设施

3. **混合架构**
   - 实施方式：核心业务使用自托管模型，辅助功能使用第三方API
   - 复杂度：中
   - 适用场景：平衡性能、成本和开发效率

### 风险提示

- **成本考虑**: GPU实例成本较高，需要合理规划训练和推理资源的使用
- **技术复杂度**: 自托管模型方案需要更多的运维和优化工作，相比托管服务需要更强的技术能力
- **模型选择**: 需要自行选择和评估开源模型，确保满足业务需求和合规要求
- **网络访问**: 部分NVIDIA软件和模型可能需要从海外下载，建议提前准备镜像或使用国内镜像源

### 配套资源

本文无配套GitHub项目，主要价值在于：
- 提供真实客户案例和技术架构参考
- 展示AWS与NVIDIA技术栈的集成最佳实践
- 分享生成式AI从试点到生产的经验教训

**学习建议：**
- 重点关注文中提到的架构模式（如Adobe的"AI superhighway"、Hippocratic AI的"constellation architecture"）
- 参考各客户的技术选型逻辑和优化策略
- 结合自身业务场景，选择合适的技术组合
