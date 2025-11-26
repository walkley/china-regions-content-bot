---
title: 使用LangGraph和Mistral在AWS上构建多智能体系统
publish_date: 2025-03-06
original_url: https://aws.amazon.com/blogs/machine-learning/build-a-multi-agent-system-with-langgraph-and-mistral-on-aws/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 4
unavailable_services: 1
---

# 使用LangGraph和Mistral在AWS上构建多智能体系统

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/build-a-multi-agent-system-with-langgraph-and-mistral-on-aws/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

Amazon Bedrock是整个解决方案的核心基础服务，在AWS中国区域不可用。该博客的主要内容是使用Bedrock上的Mistral模型构建多智能体系统，所有的文本生成、工具调用和智能体协作都完全依赖于Amazon Bedrock服务，没有可行的替代方案。

## 服务分析

### 可用服务 (4个)

- Amazon SageMaker
- Amazon Titan Text Embeddings
- Amazon Bedrock Converse API
- Amazon Bedrock Knowledge Bases

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务

### 评估说明

虽然从数量上看，服务可用率达到80%（4/5），但Amazon Bedrock是整个架构的核心基础：

1. **核心依赖**：博客的核心内容是使用Amazon Bedrock上的Mistral模型构建多智能体系统
2. **功能实现**：所有智能体的文本生成功能都通过Bedrock Converse API实现
3. **工具调用**：外部函数调用（tools）功能依赖于Bedrock的能力
4. **无替代方案**：在AWS中国区域没有等效的托管大语言模型服务可以替代Bedrock

列为"可用"的其他服务（如Titan Embeddings、Converse API、Knowledge Bases）实际上都是Amazon Bedrock的组成部分或依赖于Bedrock，因此在Bedrock不可用的情况下，这些服务也无法使用。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 初步可行性评估为LOW，核心服务Amazon Bedrock在AWS中国区域不可用，无法进行实际部署验证。

## 实施建议

### 推荐方案

**不建议直接实施**

该解决方案完全依赖于Amazon Bedrock服务，而Bedrock在AWS中国区域不可用。由于这是架构的核心基础，无法通过简单的配置调整或服务替换来实现相同功能。

### 替代方案

1. **使用Amazon SageMaker部署开源模型**
   - 实施方式：在SageMaker上部署开源的Mistral模型或其他大语言模型（如Llama、ChatGLM等）
   - 复杂度：高
   - 适用场景：需要完全控制模型部署和推理环境，有足够的技术团队支持
   - 注意事项：
     - 需要自行管理模型部署、扩展和优化
     - 需要实现类似Bedrock Converse API的接口层
     - 需要自行实现工具调用（function calling）功能
     - 成本和运维复杂度显著增加

2. **使用第三方API服务**
   - 实施方式：使用国内可访问的大语言模型API服务（如阿里云通义千问、百度文心一言等）
   - 复杂度：中
   - 适用场景：快速原型验证，不需要完全在AWS环境内运行
   - 注意事项：
     - 数据需要传输到第三方服务，需考虑数据安全和合规性
     - API能力和接口可能与Bedrock有差异
     - 需要修改代码以适配不同的API规范

3. **混合架构方案**
   - 实施方式：在AWS全球区域使用Bedrock，通过专线或VPN连接到中国区域的其他服务
   - 复杂度：高
   - 适用场景：对数据出境有明确合规路径，需要使用Bedrock的特定能力
   - 注意事项：
     - 需要处理跨境数据传输的合规问题
     - 网络延迟可能影响用户体验
     - 架构复杂度和成本显著增加

### 风险提示

- **核心功能缺失**：Amazon Bedrock不可用意味着无法使用托管的Mistral模型，需要完全重新设计模型部署方案
- **开发工作量**：任何替代方案都需要大量的开发和测试工作，与原博客内容差异较大
- **功能差异**：替代方案可能无法完全复制Bedrock的所有功能特性（如Converse API、工具调用等）
- **成本增加**：自行部署和管理模型的成本通常高于使用托管服务
- **合规风险**：使用第三方API或跨境方案需要仔细评估数据安全和合规要求

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/mistral-on-aws
- **兼容性**: 不可在AWS中国区直接使用
- **修改建议**: 
  - 需要完全重写模型调用部分，替换为SageMaker端点或第三方API
  - 需要重新实现工具调用（function calling）机制
  - 需要调整向量存储和RAG系统以适配中国区域的服务
  - 建议评估是否值得投入资源进行如此大规模的修改，或考虑在全球区域实施
