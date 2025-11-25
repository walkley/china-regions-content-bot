---
title: 在 Amazon SageMaker AI 中宣布 Amazon Nova 定制化功能
publish_date: 2025-07-16
original_url: https://aws.amazon.com/blogs/aws/announcing-amazon-nova-customization-in-amazon-sagemaker-ai/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 1
unavailable_services: 2
---

# 在 Amazon SageMaker AI 中宣布 Amazon Nova 定制化功能

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/announcing-amazon-nova-customization-in-amazon-sagemaker-ai/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

核心服务 Amazon Bedrock 和 Amazon Nova 在中国区域不可用，虽然可以使用 SageMaker 进行模型训练，但无法实现完整的工作流程（训练后部署到 Bedrock 进行推理）。

## 服务分析

### 可用服务 (1个)

- Amazon SageMaker AI（包括 SageMaker Studio、SageMaker HyperPod、SageMaker Training Jobs）

### 不可用服务 (2个)

- **Amazon Bedrock** - 核心服务
- **Amazon Nova** - 核心服务

### 评估说明

本文介绍了在 Amazon SageMaker AI 中定制 Amazon Nova 模型的功能，支持多种定制技术（监督微调、对齐、持续预训练、知识蒸馏）。然而，该方案的核心价值在于完整的工作流程：

1. **训练阶段**：在 SageMaker 中使用各种定制技术训练 Nova 模型
2. **部署阶段**：将定制化的模型无缝部署到 Amazon Bedrock
3. **推理阶段**：通过 Bedrock 的按需或预置吞吐量进行推理

在中国区域：
- ✅ 可以使用 SageMaker 进行模型训练（如果有 Nova 模型的访问权限）
- ❌ 无法部署到 Amazon Bedrock（服务不可用）
- ❌ 无法使用 Amazon Nova 基础模型（服务不可用）

由于 Amazon Bedrock 和 Amazon Nova 是该方案的核心依赖，缺失这些服务将导致整个工作流程无法完成。服务可用率仅为 33.3%，远低于可实施的阈值。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 初步可行性评估为 LOW，核心服务 Amazon Bedrock 和 Amazon Nova 在中国区域不可用，无法实现文章描述的完整功能，因此跳过深入验证阶段。

## 实施建议

### 推荐方案

**不建议直接实施**

该博客介绍的 Amazon Nova 定制化功能依赖于 Amazon Bedrock 和 Amazon Nova 服务，这两个核心服务在中国区域均不可用。虽然理论上可以在 SageMaker 中进行模型训练，但由于：

1. 无法获取 Amazon Nova 基础模型作为训练起点
2. 训练完成后无法部署到 Amazon Bedrock 进行推理
3. 缺少完整的端到端工作流程支持

因此，该方案在中国区域无法实施。

### 替代方案

如果您需要在中国区域实现类似的模型定制化功能，可以考虑以下替代方案：

1. **使用开源基础模型 + SageMaker**
   - 实施方式：选择开源的大语言模型（如 Llama、Qwen 等），在 SageMaker 中进行微调和定制
   - 复杂度：中
   - 适用场景：需要完全控制模型训练和部署流程，对特定开源模型有偏好

2. **使用其他可用的托管模型服务**
   - 实施方式：探索中国区域可用的其他 AI 模型服务，结合 SageMaker 进行定制化训练
   - 复杂度：中到高
   - 适用场景：需要托管服务的便利性，但可以接受不同的模型选择

3. **完全自建模型训练和推理管道**
   - 实施方式：使用 SageMaker Training、SageMaker HyperPod 进行训练，使用 SageMaker Endpoints 或 EKS 进行推理部署
   - 复杂度：高
   - 适用场景：有充足的技术资源和时间，需要完全自主可控的解决方案

### 风险提示

- **服务依赖性**：Amazon Bedrock 和 Amazon Nova 在中国区域的可用性未知，短期内可能不会推出
- **功能差异**：替代方案无法完全复制 Amazon Nova 的特性和性能
- **成本考虑**：自建方案可能需要更多的开发和运维成本
- **技术复杂度**：替代方案通常需要更深入的技术知识和更长的实施周期

### 配套资源

- **GitHub仓库**: https://github.com/aws/sagemaker-hyperpod-recipes
- **兼容性**: 该仓库中的 SageMaker HyperPod 训练配方（recipes）理论上可以在中国区域使用，但由于缺少 Amazon Nova 模型访问权限，无法直接应用于 Nova 模型的定制化
- **修改建议**: 如果要在中国区域使用该仓库，需要将其中的 Nova 模型替换为其他可用的开源模型，并移除所有与 Amazon Bedrock 部署相关的代码
