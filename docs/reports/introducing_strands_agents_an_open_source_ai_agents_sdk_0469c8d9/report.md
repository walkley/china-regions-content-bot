---
title: 介绍Strands Agents：一个开源AI代理SDK
publish_date: 2025-05-16
original_url: https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 5
unavailable_services: 2
---

# 介绍Strands Agents：一个开源AI代理SDK

[📖 查看原始博客](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Bedrock在中国区不可用，需要使用替代模型提供商

核心服务Amazon Bedrock在AWS中国区域不可用，虽然Strands Agents SDK本身支持多种模型提供商，但博客中的示例代码和默认配置均基于Amazon Bedrock，需要进行重大调整才能在中国区域使用。

## 服务分析

### 可用服务 (5个)

- AWS Lambda
- AWS Fargate
- Amazon EC2
- AWS Glue
- VPC Reachability Analyzer

### 不可用服务 (2个)

- **Amazon Bedrock** - 核心服务
- **Amazon Q Developer** - 提及但非核心

### 评估说明

1. **核心服务可用性**：Amazon Bedrock是该方案的核心依赖，用于提供大语言模型的推理能力。该服务在AWS中国区域不可用，直接影响博客示例代码的可执行性。

2. **不可用服务影响**：
   - Amazon Bedrock：博客中的代码示例默认使用Bedrock作为模型提供商，需要完全替换为其他模型服务
   - Amazon Q Developer：仅作为使用场景提及，不影响Strands Agents SDK的核心功能

3. **替代方案可行性**：Strands Agents SDK设计上支持多种模型提供商，包括Anthropic API、Ollama、LiteLLM等，理论上可以通过配置替代模型提供商来实现相同功能，但需要对代码进行修改。

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段评估为LOW等级，核心服务Amazon Bedrock在中国区域不可用，需要重大架构调整。跳过GitHub项目部署验证，避免不必要的资源消耗。

## 实施建议

### 推荐方案

**不建议直接按照原文实施**

虽然Strands Agents SDK本身是开源的Python库，可以在任何环境中安装使用，但博客中的示例代码和推荐配置严重依赖Amazon Bedrock服务。在AWS中国区域实施该方案需要：

1. **替换模型提供商**：将所有使用Amazon Bedrock的代码修改为使用其他可用的模型提供商
2. **调整示例代码**：修改博客中提供的所有代码示例
3. **重新配置部署架构**：调整生产环境部署方案中涉及Bedrock的部分

**预计工作量**：中到高
- 需要深入理解Strands Agents SDK的模型提供商配置机制
- 需要选择并配置替代的模型服务
- 需要测试验证替代方案的功能完整性

### 替代方案

#### 方案1：使用Anthropic API

- **实施方式**：直接使用Anthropic提供的Claude模型API，Strands已内置支持
- **复杂度**：低
- **适用场景**：
  - 可以访问Anthropic API服务
  - 接受使用第三方API服务
  - 需要高质量的模型推理能力
- **注意事项**：
  - 需要Anthropic API密钥
  - 可能涉及数据出境问题
  - API调用费用由Anthropic收取

#### 方案2：使用Ollama本地部署

- **实施方式**：在本地或私有云环境部署Ollama，运行开源大语言模型（如Llama）
- **复杂度**：中
- **适用场景**：
  - 对数据隐私有严格要求
  - 有足够的计算资源（GPU）
  - 可以接受开源模型的性能表现
- **注意事项**：
  - 需要准备GPU服务器
  - 模型性能可能不如商业API
  - 需要自行管理模型部署和维护

#### 方案3：使用LiteLLM连接其他模型服务

- **实施方式**：通过LiteLLM统一接口连接国内可用的大语言模型服务（如阿里云通义千问、百度文心一言等）
- **复杂度**：中
- **适用场景**：
  - 希望使用国内模型服务
  - 需要符合国内数据合规要求
  - 对模型中文能力有较高要求
- **注意事项**：
  - 需要验证LiteLLM对目标模型服务的支持程度
  - 可能需要额外的适配工作
  - 不同模型服务的能力和API规范可能有差异

### 风险提示

- **模型能力差异**：替代模型提供商的推理能力、工具调用能力可能与Amazon Bedrock中的模型存在差异，影响代理的实际表现
- **API兼容性**：虽然Strands支持多种模型提供商，但不同提供商的API规范和功能特性可能不完全一致，需要额外的适配和测试
- **数据合规性**：使用第三方API服务（如Anthropic API）可能涉及数据出境问题，需要评估合规风险
- **成本考量**：不同模型提供商的定价策略差异较大，需要重新评估使用成本
- **生产环境部署**：博客中提供的AWS Lambda、Fargate、EC2部署方案在中国区域可用，但需要调整模型配置部分

### 配套资源

- **GitHub仓库**: https://github.com/strands-agents
- **兼容性**: SDK本身可在中国区使用，但需要配置替代的模型提供商
- **修改建议**: 
  1. 将所有`Agent()`初始化代码中的模型配置从Bedrock改为其他提供商
  2. 示例代码中的`GITHUB_TOKEN`和AWS凭证配置保持不变
  3. 部署架构中的Lambda、Fargate、EC2部分无需修改，仅需调整模型调用配置
  4. 如使用Amazon Bedrock Knowledge Bases功能，需要寻找替代的向量数据库和检索方案
