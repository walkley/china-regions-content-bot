---
title: Amazon SageMaker HyperPod 的托管分层 KV 缓存和智能路由
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/machine-learning/managed-tiered-kv-cache-and-intelligent-routing-for-amazon-sagemaker-hyperpod/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 3
unavailable_services: 2
---

# Amazon SageMaker HyperPod 的托管分层 KV 缓存和智能路由

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/managed-tiered-kv-cache-and-intelligent-routing-for-amazon-sagemaker-hyperpod/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务 Amazon SageMaker HyperPod 在中国区域不可用，无法实施本文介绍的功能

本文介绍的是 Amazon SageMaker HyperPod 的新功能（托管分层 KV 缓存和智能路由），该服务是实施的核心依赖，但在 AWS 中国区域（cn-northwest-1 和 cn-north-1）均不可用，因此无法按照原文实施。

## 服务分析

### 可用服务 (3个)

- Amazon EKS (Elastic Kubernetes Service)
- Amazon S3
- Amazon ECR (Elastic Container Registry)

### 不可用服务 (2个)

- **Amazon SageMaker HyperPod** - 核心服务
- **Amazon Managed Grafana** - 用于可观测性监控

### 评估说明

本文的核心内容是介绍 Amazon SageMaker HyperPod 的两个新功能：
1. **托管分层 KV 缓存（Managed Tiered KV Cache）**：通过 L1（CPU 内存）和 L2（分布式缓存）两层架构优化 LLM 推理性能
2. **智能路由（Intelligent Routing）**：通过前缀感知、KV 感知和轮询等策略最大化缓存命中率

这些功能完全依赖于 SageMaker HyperPod 服务及其推理操作器（Inference Operator）。经过验证，SageMaker HyperPod 在中国区域不可用（API 调用返回 UnknownOperationException），这意味着：

- 无法创建 HyperPod 集群
- 无法使用 HyperPod Inference Operator
- 无法部署文章中介绍的 InferenceEndpointConfig 自定义资源
- 无法使用托管分层 KV 缓存和智能路由功能

此外，用于监控的 Amazon Managed Grafana 在中国区域也不可用，虽然这不是核心功能，但会影响生产环境的可观测性。

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务 Amazon SageMaker HyperPod 在中国区域不可用，可行性评估为 LOW，无法进行实际部署验证。

### 技术验证详情

通过 AWS CLI 验证了以下服务的可用性：

1. **SageMaker HyperPod 验证**
   ```bash
   aws sagemaker list-clusters --region cn-northwest-1
   # 返回: UnknownOperationException - 操作在该区域不支持
   ```

2. **Amazon Managed Grafana 验证**
   ```bash
   aws grafana list-workspaces --region cn-northwest-1
   # 返回: 无法连接到端点
   ```

3. **EKS、S3、ECR 验证**
   - 均可正常访问和使用

## 实施建议

### 推荐方案

**不建议在 AWS 中国区域实施本文方案**

由于核心服务不可用，建议考虑以下选项：

1. **等待服务上线**：关注 AWS 中国区域的服务发布公告，等待 SageMaker HyperPod 在中国区域上线

2. **使用全球区域**：如果业务允许，可以在 AWS 全球区域（如 us-west-2、us-east-1）使用本文介绍的功能

3. **考虑替代方案**：在中国区域使用其他方式实现类似的 LLM 推理优化

### 替代方案

虽然无法使用 SageMaker HyperPod 的托管功能，但可以考虑在 EKS 上自建类似的架构：

1. **基于 EKS + vLLM 的自建方案**
   - 实施方式：
     - 在 Amazon EKS 上部署 vLLM 推理服务
     - 手动配置 vLLM 的 KV 缓存参数（`--max-model-len`、`--gpu-memory-utilization` 等）
     - 使用 Redis 或其他缓存解决方案实现 L2 缓存
     - 通过 Kubernetes Service 和 Ingress 实现负载均衡和路由
   - 复杂度：高
   - 适用场景：有 Kubernetes 和 LLM 推理经验的团队，需要完全控制基础设施
   - 局限性：
     - 需要手动管理缓存基础设施
     - 缺少 HyperPod 的托管分层存储优化
     - 智能路由需要自行实现
     - 运维复杂度显著增加

2. **使用 Amazon SageMaker Inference（标准版）**
   - 实施方式：
     - 使用 SageMaker Real-time Inference 或 Asynchronous Inference
     - 部署支持 KV 缓存的推理容器（如 vLLM、TGI）
     - 通过 SageMaker Endpoint 配置实现基本的负载均衡
   - 复杂度：中
   - 适用场景：需要托管服务但不需要 HyperPod 高级功能的场景
   - 局限性：
     - 缺少跨实例的分布式 KV 缓存（L2 缓存）
     - 没有智能路由功能
     - 性能优化效果不如 HyperPod 方案

3. **使用 Amazon ECS/EKS + Application Load Balancer**
   - 实施方式：
     - 在 ECS 或 EKS 上部署 LLM 推理容器
     - 使用 ALB 进行负载均衡
     - 配置容器级别的 KV 缓存
   - 复杂度：中
   - 适用场景：已有 ECS/EKS 基础设施的团队
   - 局限性：
     - 仅支持本地 L1 缓存
     - 缺少智能路由和跨实例缓存共享
     - 需要自行优化性能

### 性能对比说明

根据原文的基准测试数据，SageMaker HyperPod 的托管分层 KV 缓存和智能路由可以实现：
- TTFT（首 token 时间）P90 降低 35-40%
- TTFT P50 降低 72-94%
- 吞吐量提升 24-38%
- 成本降低 21-28%

**替代方案无法达到相同的性能水平**，主要原因：
- 缺少 AWS 优化的分层存储架构
- 没有跨实例的智能缓存共享
- 缺少前缀感知和 KV 感知的智能路由

### 风险提示

- **服务不可用风险**：核心服务在中国区域不可用，无法实施原文方案
- **性能差距风险**：替代方案的性能优化效果远不如原文方案
- **运维复杂度风险**：自建方案需要大量的运维工作和专业知识
- **成本风险**：自建方案可能无法实现原文提到的成本优化效果
- **技术债务风险**：自建方案可能在 HyperPod 上线后需要重构迁移

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/sagemaker-genai-hosting-examples
- **兼容性**: 代码示例依赖 SageMaker HyperPod，在中国区域无法直接使用
- **修改建议**: 如果采用替代方案，需要完全重写部署配置，将 HyperPod 特定的 CRD（InferenceEndpointConfig）替换为标准的 Kubernetes 资源定义

## 总结

本文介绍的 Amazon SageMaker HyperPod 托管分层 KV 缓存和智能路由功能在 AWS 中国区域不可用。这些功能可以显著优化 LLM 推理性能和成本，但完全依赖于 SageMaker HyperPod 服务。

**建议**：
- 如果必须在中国区域部署，考虑使用基于 EKS + vLLM 的自建方案，但需要接受更高的运维复杂度和较低的性能优化效果
- 如果业务允许，建议在 AWS 全球区域使用本文介绍的功能
- 持续关注 AWS 中国区域的服务发布，等待 SageMaker HyperPod 上线

**适用场景**：本文方案特别适合以下场景（在全球区域）：
- 处理长文档的应用（如法律合同分析）
- 多轮对话系统（如医疗聊天机器人）
- 高吞吐量推理应用（如客户服务系统）
- 需要优化 LLM 推理成本的企业级部署
