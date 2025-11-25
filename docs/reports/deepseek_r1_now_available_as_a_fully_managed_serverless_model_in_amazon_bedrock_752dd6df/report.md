---
title: DeepSeek-R1 现已作为完全托管的无服务器模型在 Amazon Bedrock 中提供
publish_date: 2025-03-10
original_url: https://aws.amazon.com/blogs/aws/deepseek-r1-now-available-as-a-fully-managed-serverless-model-in-amazon-bedrock/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 2
unavailable_services: 5
---

# DeepSeek-R1 现已作为完全托管的无服务器模型在 Amazon Bedrock 中提供

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/deepseek-r1-now-available-as-a-fully-managed-serverless-model-in-amazon-bedrock/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

Amazon Bedrock 是本文的核心服务，目前在 AWS 中国区域（宁夏和北京）完全不可用，导致文章中介绍的所有功能和特性均无法在中国区域实施。

## 服务分析

### 可用服务 (2个)

- AWS CLI（通用工具）
- AWS SDK（通用工具）

### 不可用服务 (5个)

- **Amazon Bedrock** - 核心服务
- **Amazon Bedrock Guardrails** - 核心功能
- **Amazon Bedrock Marketplace** - 核心功能
- **Amazon Bedrock Custom Model Import** - 核心功能
- **Amazon Bedrock Converse API** - 核心功能

### 评估说明

本文完全围绕 Amazon Bedrock 服务展开，介绍了如何在 Bedrock 中使用 DeepSeek-R1 模型。由于 Amazon Bedrock 在中国区域不可用，文章中的所有内容都无法实施：

1. **核心服务完全不可用**：Amazon Bedrock 是文章的唯一主题，在中国区域没有提供
2. **所有功能依赖 Bedrock**：Guardrails、Marketplace、Custom Model Import、Converse API 等所有功能都是 Bedrock 的组成部分
3. **无替代方案**：中国区域没有等效的托管 AI 模型服务可以替代 Bedrock 的功能
4. **可用率 0%**：除了通用的 CLI 和 SDK 工具外，文章中提到的所有服务和功能在中国区域都不可用

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段确认核心服务 Amazon Bedrock 在中国区域完全不可用，无法进行任何实际部署或功能验证。

## 实施建议

### 推荐方案

**不建议在中国区域实施此方案**

由于 Amazon Bedrock 服务在中国区域不可用，本文介绍的所有功能和操作步骤都无法在中国区域执行。如果需要在中国区域使用大语言模型服务，需要考虑完全不同的技术方案。

### 替代方案

如果您需要在 AWS 中国区域部署大语言模型服务，可以考虑以下替代方案：

1. **自托管模型方案**
   - 实施方式：在 Amazon EC2 或 Amazon EKS 上部署开源大语言模型（如 DeepSeek-R1 开源版本）
   - 复杂度：高
   - 适用场景：需要完全控制模型部署和数据隐私的场景
   - 注意事项：需要自行管理基础设施、模型优化、扩展性和安全性

2. **Amazon SageMaker 部署方案**
   - 实施方式：使用 Amazon SageMaker 部署和托管开源大语言模型
   - 复杂度：中
   - 适用场景：需要托管服务但 Bedrock 不可用的场景
   - 注意事项：需要自行处理模型推理优化、endpoint 管理和成本控制

3. **混合云方案**
   - 实施方式：在全球区域使用 Amazon Bedrock，通过专线或 VPN 从中国区域访问
   - 复杂度：高
   - 适用场景：对数据出境有合规许可的场景
   - 注意事项：需要考虑网络延迟、数据合规性、跨境数据传输成本

### 风险提示

- **服务不可用风险**：Amazon Bedrock 在中国区域没有上线计划的公开信息，短期内无法使用
- **数据合规风险**：如果采用混合云方案访问全球区域的 Bedrock，需要确保符合中国的数据出境相关法律法规
- **成本风险**：自托管方案需要投入大量的基础设施成本和运维成本
- **技术复杂度**：替代方案都需要更高的技术能力和更多的开发工作量
- **功能差异**：自托管方案无法获得 Bedrock 提供的开箱即用的 Guardrails、模型评估等企业级功能

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 不适用

## 总结

本文介绍的 DeepSeek-R1 在 Amazon Bedrock 中的使用方法完全依赖于 Amazon Bedrock 服务，而该服务在 AWS 中国区域（宁夏和北京）不可用。因此，文章内容无法在中国区域直接实施。

如果您的业务需要在中国区域使用大语言模型服务，建议：
1. 评估业务需求是否可以在全球区域实施（考虑数据合规性）
2. 如果必须在中国区域部署，考虑使用 Amazon SageMaker 或 EC2 自托管开源模型
3. 关注 AWS 中国区域的服务更新，等待 Bedrock 或类似服务的上线
