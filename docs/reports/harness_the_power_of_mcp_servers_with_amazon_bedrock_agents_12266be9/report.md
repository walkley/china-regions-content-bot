---
title: 利用Amazon Bedrock Agents发挥MCP服务器的强大能力
publish_date: 2025-04-01
original_url: https://aws.amazon.com/blogs/machine-learning/harness-the-power-of-mcp-servers-with-amazon-bedrock-agents/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 11
unavailable_services: 3
---

# 利用Amazon Bedrock Agents发挥MCP服务器的强大能力

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/harness-the-power-of-mcp-servers-with-amazon-bedrock-agents/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Bedrock在中国区不可用，整个方案无法实施

Amazon Bedrock是本文的核心基础服务，所有架构设计、代码实现和功能演示都完全依赖于Amazon Bedrock Agents。由于该服务在AWS中国区域不可用，整个解决方案无法在中国区实施。

## 服务分析

### 可用服务 (11个)

- AWS Lambda
- AWS Cost Explorer
- Amazon CloudWatch
- AWS IAM
- AWS STS
- AWS CloudTrail
- Amazon SageMaker
- Amazon Neptune
- Amazon OpenSearch Service
- Amazon EC2
- AWS CDK

### 不可用服务 (3个)

- **Amazon Bedrock** - 核心服务，整篇文章的基础
- **Amazon Q** - 在成本分析示例中被提及
- **Amazon Kendra** - 在博客主题标签中提及

### 评估说明

虽然文章中提到的14个AWS服务中有11个（78.6%）在中国区可用，但核心服务Amazon Bedrock的缺失使得整个方案无法实施：

1. **Amazon Bedrock是不可替代的核心**：文章的核心内容是展示如何将Model Context Protocol (MCP)与Amazon Bedrock Agents集成，所有代码示例、API调用和架构设计都基于Bedrock服务。

2. **Bedrock Agents是关键组件**：文章介绍的Inline Agent SDK、Return Control机制、Action Groups配置等功能都是Amazon Bedrock Agents特有的能力。

3. **MCP集成是AWS特定实现**：文章展示的MCP与Bedrock的集成方式是AWS提供的专有功能，无法通过其他服务替代。

4. **配套代码完全依赖Bedrock**：GitHub仓库中的所有示例代码都使用了Bedrock的API和SDK，包括模型调用、agent创建、工具编排等核心功能。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段发现核心服务Amazon Bedrock在AWS中国区域不可用，整个方案的技术基础不存在，无需进行深入验证。

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此方案**

由于Amazon Bedrock服务在中国区不可用，本文介绍的所有功能和实现方式都无法在中国区域使用。这不是一个可以通过简单调整或配置修改解决的问题，而是服务本身在该区域不存在。

### 替代方案

如果您希望在AWS中国区域实现类似的AI Agent功能，可以考虑以下替代方案：

1. **使用Amazon SageMaker部署自定义AI模型**
   - 实施方式：在SageMaker上部署开源大语言模型（如Llama、Mistral等），自行实现Agent编排逻辑
   - 复杂度：高
   - 适用场景：需要完全自主控制模型和推理流程的场景
   - 注意事项：需要自行处理模型部署、推理优化、工具调用编排等复杂问题

2. **集成第三方AI服务**
   - 实施方式：使用AWS Lambda和API Gateway集成国内可用的AI服务（如阿里云通义千问、百度文心一言等）
   - 复杂度：中
   - 适用场景：对模型选择灵活性要求较高的场景
   - 注意事项：需要处理跨服务集成、数据安全和合规性问题

3. **使用AWS全球区域的Bedrock服务**
   - 实施方式：在AWS全球区域（如us-east-1）部署Bedrock应用，通过API方式为中国区用户提供服务
   - 复杂度：中
   - 适用场景：可以接受跨境数据传输延迟和合规要求的场景
   - 注意事项：需要考虑网络延迟、数据跨境传输的法律法规要求、成本增加等因素

### 风险提示

- **服务不可用风险**: Amazon Bedrock在中国区域完全不可用，没有上线时间表
- **架构差异风险**: 替代方案的架构和实现方式与原文差异巨大，需要重新设计整个系统
- **功能缺失风险**: Bedrock Agents的许多高级功能（如Inline Agents、Return Control、内置Code Interpreter等）在替代方案中难以实现
- **开发成本风险**: 使用替代方案需要大量的自定义开发工作，时间和人力成本显著增加
- **维护成本风险**: 自建Agent系统需要持续维护和优化，长期运营成本较高
- **合规风险**: 如使用跨境方案，需要严格遵守数据跨境传输的相关法律法规

### 配套资源

- **GitHub仓库**: https://github.com/awslabs/amazon-bedrock-agent-samples/tree/main/src/InlineAgent
- **兼容性**: ❌ 无法在中国区使用
- **修改建议**: 由于核心依赖服务不可用，无法通过修改代码使其在中国区运行。如需实现类似功能，建议参考其架构思路，使用中国区可用的服务重新设计和实现。
