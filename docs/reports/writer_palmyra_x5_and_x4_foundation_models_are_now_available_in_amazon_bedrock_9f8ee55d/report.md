---
title: Writer Palmyra X5 和 X4 基础模型现已在 Amazon Bedrock 中可用
publish_date: 2025-04-28
original_url: https://aws.amazon.com/blogs/aws/writer-palmyra-x5-and-x4-foundation-models-are-now-available-in-amazon-bedrock/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 1
unavailable_services: 2
---

# Writer Palmyra X5 和 X4 基础模型现已在 Amazon Bedrock 中可用

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/writer-palmyra-x5-and-x4-foundation-models-are-now-available-in-amazon-bedrock/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，无法在中国区域实施

Amazon Bedrock 是本博客的核心服务，目前在AWS中国区域不可用。博客的全部内容都围绕在 Amazon Bedrock 中使用 Writer Palmyra X5 和 X4 模型，因此无法在中国区域实施任何相关功能。

## 服务分析

### 可用服务 (1个)

- AWS SDK for Python (Boto3)

### 不可用服务 (2个)

- **Amazon Bedrock** - 核心服务
- **Amazon SageMaker HyperPod** - 高级训练功能

### 评估说明

1. **核心服务不可用**：Amazon Bedrock 是博客介绍的唯一核心服务，在AWS中国区域完全不可用
2. **无替代方案**：Writer Palmyra 模型专门通过 Amazon Bedrock 提供，没有其他访问途径
3. **功能完全依赖**：博客中的所有示例代码、API调用和功能演示都完全依赖 Amazon Bedrock 服务

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务 Amazon Bedrock 在AWS中国区域不可用，无法进行任何实际验证或部署测试。

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此方案**

由于 Amazon Bedrock 服务在中国区域不可用，无法使用 Writer Palmyra X5 和 X4 模型。博客中介绍的所有功能，包括：
- 大规模上下文窗口处理（Palmyra X5 的 100万 token，X4 的 128K token）
- 企业级推理能力
- 多步骤工具调用
- 文档比较和分析

这些功能都无法在中国区域实现。

### 替代方案

如果需要在AWS中国区域使用大语言模型服务，可以考虑以下替代方案：

1. **自托管开源模型**
   - 实施方式：在 Amazon EC2 或 Amazon ECS 上部署开源大语言模型（如 Llama、Qwen 等）
   - 复杂度：高
   - 适用场景：需要完全控制模型部署和数据隐私的企业场景
   - 注意事项：需要自行管理基础设施、模型优化和扩展

2. **使用第三方API服务**
   - 实施方式：集成在中国可用的第三方大语言模型API服务
   - 复杂度：中
   - 适用场景：快速原型开发和中小规模应用
   - 注意事项：需要评估数据合规性和服务稳定性

3. **混合云架构**
   - 实施方式：在AWS全球区域使用 Amazon Bedrock，通过专线或VPN连接中国区域应用
   - 复杂度：高
   - 适用场景：对延迟不敏感且有跨境数据传输合规要求的场景
   - 注意事项：需要处理跨境数据传输的法律法规要求和网络延迟问题

### 风险提示

- **服务不可用**：Amazon Bedrock 在中国区域完全不可用，短期内无官方支持计划
- **无直接迁移路径**：如果在全球区域使用了 Amazon Bedrock，迁移到中国区域需要完全重新设计架构
- **功能差异**：替代方案可能无法提供与 Writer Palmyra 模型相同的性能和功能特性
- **合规考虑**：使用第三方服务或跨境方案时需要特别注意数据合规和隐私保护要求

### 配套资源

- **GitHub仓库**: 无
- **示例代码**: 博客中包含 Python 示例代码，但依赖 Amazon Bedrock 服务，无法在中国区域运行
