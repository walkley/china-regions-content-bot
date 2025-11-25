---
title: DeepSeek-R1模型现已在Amazon Bedrock Marketplace和Amazon SageMaker JumpStart上可用
publish_date: 2025-01-30
original_url: https://aws.amazon.com/blogs/machine-learning/deepseek-r1-model-now-available-in-amazon-bedrock-marketplace-and-amazon-sagemaker-jumpstart/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 2
unavailable_services: 2
---

# DeepSeek-R1模型现已在Amazon Bedrock Marketplace和Amazon SageMaker JumpStart上可用

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/deepseek-r1-model-now-available-in-amazon-bedrock-marketplace-and-amazon-sagemaker-jumpstart/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Bedrock在中国区域不可用，仅能通过SageMaker JumpStart实现部分功能

博客介绍了DeepSeek-R1模型在两个平台上的部署方式，但Amazon Bedrock Marketplace在中国区域完全不可用，导致博客约50%的内容无法在中国区域实施。

## 服务分析

### 可用服务 (2个)

- Amazon SageMaker (包括 SageMaker JumpStart)
- AWS Identity and Access Management (IAM)

### 不可用服务 (2个)

- **Amazon Bedrock** - 核心服务
- **Amazon Bedrock Guardrails** - 核心服务

### 评估说明

1. **核心服务不可用**：Amazon Bedrock及其Marketplace是博客的两大核心部署平台之一，在中国区域完全不可用
2. **功能受限严重**：博客详细介绍了Bedrock Marketplace和SageMaker JumpStart两种部署方式，中国区域只能使用后者
3. **Guardrails功能缺失**：Amazon Bedrock Guardrails是博客强调的重要安全功能，用于内容过滤和安全控制，在中国区域无法使用
4. **可用服务比例**：仅50%的服务可用，远低于MODERATE级别的70%阈值

## 验证结果

### 验证类型

- ⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证评估结果为LOW，核心服务Amazon Bedrock在中国区域不可用，不满足深入验证的触发条件（需要MODERATE或HIGH）

## 实施建议

### 推荐方案

**不建议直接实施**

虽然可以通过Amazon SageMaker JumpStart部署DeepSeek-R1模型，但这只能实现博客内容的一半功能。具体限制包括：

1. **无法使用Bedrock Marketplace**：博客中关于Bedrock部署的所有步骤和代码示例均不适用
2. **缺少Guardrails集成**：无法使用Amazon Bedrock Guardrails的ApplyGuardrail API进行内容安全控制
3. **API差异**：Bedrock的InvokeModel API在中国区域不可用，需要使用SageMaker的InvokeEndpoint API

### 替代方案

#### 方案1：仅使用SageMaker JumpStart部署

- **实施方式**：
  - 按照博客中"Deploy DeepSeek-R1 with SageMaker JumpStart"章节的步骤操作
  - 使用ml.p5e.48xlarge实例类型（需要确认配额）
  - 通过SageMaker Python SDK或控制台UI部署模型
  
- **复杂度**：中
- **适用场景**：需要部署DeepSeek-R1模型但不依赖Bedrock生态系统的场景
- **注意事项**：
  - 需要申请ml.p5e.48xlarge实例配额
  - 无法使用Bedrock Guardrails，需要自行实现内容安全控制
  - 配套的GitHub示例代码中涉及Bedrock的部分需要跳过

#### 方案2：自建内容安全控制机制

- **实施方式**：
  - 使用SageMaker JumpStart部署DeepSeek-R1模型
  - 在应用层实现自定义的内容过滤和安全控制逻辑
  - 可以考虑使用开源的内容审核工具或第三方服务
  
- **复杂度**：高
- **适用场景**：对内容安全有严格要求，需要替代Bedrock Guardrails功能的场景
- **注意事项**：
  - 需要额外的开发工作量来实现安全控制
  - 需要持续维护和更新安全规则
  - 可能无法达到Bedrock Guardrails的功能完整性

### 风险提示

- **功能完整性风险**：只能实现博客介绍的部分功能，Bedrock相关的所有特性均不可用
- **成本风险**：ml.p5e.48xlarge是高性能GPU实例，运行成本较高，需要及时清理测试资源
- **配额限制风险**：P5e实例在中国区域可能需要申请配额，审批时间不确定
- **安全控制风险**：缺少Bedrock Guardrails的内置安全功能，需要自行实现内容审核机制
- **维护成本风险**：自建的安全控制机制需要持续维护和更新

### 配套资源

- **GitHub仓库1**: https://github.com/aws-samples/amazon-bedrock-samples
  - **兼容性**: 部分不兼容
  - **修改建议**: 该仓库中关于Bedrock Guardrails的示例代码在中国区域无法使用，仅供参考学习

- **GitHub仓库2**: https://github.com/aws-samples/sagemaker-genai-hosting-examples
  - **兼容性**: 兼容
  - **修改建议**: 可以直接使用Deepseek-R1-Jumpstart.ipynb进行部署，但需要确认实例配额和区域可用性
