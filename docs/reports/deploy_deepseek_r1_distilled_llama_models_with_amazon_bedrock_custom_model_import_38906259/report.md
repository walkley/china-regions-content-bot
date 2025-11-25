---
title: 使用 Amazon Bedrock 自定义模型导入部署 DeepSeek-R1 蒸馏版 Llama 模型
publish_date: 2025-01-29
original_url: https://aws.amazon.com/blogs/machine-learning/deploy-deepseek-r1-distilled-llama-models-with-amazon-bedrock-custom-model-import/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 5
unavailable_services: 1
---

# 使用 Amazon Bedrock 自定义模型导入部署 DeepSeek-R1 蒸馏版 Llama 模型

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/deploy-deepseek-r1-distilled-llama-models-with-amazon-bedrock-custom-model-import/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

Amazon Bedrock 是该方案的核心服务，但在AWS中国区域不可用，导致整个部署方案无法直接实施。

## 服务分析

### 可用服务 (5个)

- Amazon S3
- Amazon SageMaker AI
- AWS IAM
- Amazon CloudWatch
- AWS Cost Explorer

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务

### 评估说明

该博客的核心内容是使用 Amazon Bedrock Custom Model Import 功能来部署 DeepSeek-R1 蒸馏版模型。Amazon Bedrock 是整个方案的基础平台，提供了：

1. 自定义模型导入功能
2. 无服务器的模型托管和推理
3. 统一的 API 接口
4. 自动扩缩容能力
5. 与其他 AWS 服务的集成（Knowledge Bases、Guardrails、Agents）

由于 Amazon Bedrock 在中国区域不可用，整个方案的核心功能无法实现。虽然辅助服务如 S3（用于存储模型文件）、IAM（权限管理）、CloudWatch（监控）等都可用，但缺少核心的模型托管和推理平台，使得该方案无法在中国区域实施。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务 Amazon Bedrock 在AWS中国区域不可用，无法进行实际部署验证。

## 实施建议

### 推荐方案

**不建议直接实施**

由于 Amazon Bedrock 在中国区域不可用，该方案无法直接实施。建议考虑以下替代方案。

### 替代方案

1. **使用 Amazon SageMaker 部署模型**
   - 实施方式：在 SageMaker 上创建推理端点，手动部署 DeepSeek-R1 蒸馏版模型
   - 复杂度：中到高
   - 适用场景：需要完全控制模型部署和推理环境，可以接受额外的基础设施管理工作
   - 说明：需要自行处理模型容器化、端点配置、扩缩容策略等，无法使用 Bedrock 的无服务器特性和统一 API

2. **使用 Amazon ECS/EKS 容器化部署**
   - 实施方式：将模型打包为容器镜像，在 ECS 或 EKS 上部署推理服务
   - 复杂度：高
   - 适用场景：需要高度定制化的部署环境，有专业的容器和 Kubernetes 运维团队
   - 说明：提供最大的灵活性，但需要自行管理所有基础设施、负载均衡、监控和扩缩容

3. **使用 Amazon EC2 实例直接部署**
   - 实施方式：在 EC2 GPU 实例上直接部署模型推理服务
   - 复杂度：中
   - 适用场景：小规模部署或测试环境，对自动化要求不高
   - 说明：最简单的方式，但缺乏自动扩缩容和高可用性保障

### 风险提示

- **服务不可用风险**: Amazon Bedrock 在中国区域不可用是根本性限制，无法通过配置调整解决
- **架构差异风险**: 替代方案需要重新设计架构，无法享受 Bedrock 的无服务器、统一 API 等特性
- **运维复杂度风险**: 替代方案需要自行管理基础设施，增加运维成本和复杂度
- **成本模型差异**: Bedrock 的按使用付费模型与 SageMaker/EC2 的实例计费模型有显著差异，需要重新评估成本
- **功能缺失风险**: Bedrock 的 Knowledge Bases、Guardrails、Agents 等集成功能在替代方案中需要自行实现

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/amazon-bedrock-samples/blob/main/custom-models/import_models/llama-3/DeepSeek-R1-Distill-Llama-Noteb.ipynb
- **兼容性**: 不可在中国区使用（依赖 Amazon Bedrock 服务）
- **修改建议**: 需要完全重写部署逻辑，改用 SageMaker 或其他计算服务，无法简单修改
