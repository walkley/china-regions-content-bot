---
title: 代理互操作性开放协议第一部分：MCP上的代理间通信
publish_date: 2025-05-19
original_url: https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: MODERATE
available_services: 3
unavailable_services: 2
---

# 代理互操作性开放协议第一部分：MCP上的代理间通信

[📖 查看原始博客](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp/) | 验证日期: 2025-11-25

## 可行性评估

!!! warning "MODERATE - 谨慎实施"
    核心概念可实施，但需要替换LLM服务提供商

文章介绍的Model Context Protocol (MCP)是一个开源协议，本身与AWS服务无关。虽然示例代码使用Amazon Bedrock，但Spring AI框架支持多种LLM提供商，可以使用替代方案实现相同功能。

## 服务分析

### 可用服务 (3个)

- Amazon EC2
- Amazon SageMaker
- Aurora DSQL

### 不可用服务 (2个)

- **Amazon Bedrock** - 核心服务（示例代码的LLM提供商）
- **Amazon Lex** - 非核心服务（仅在背景介绍中提及）

### 评估说明

1. **核心概念独立性**：MCP协议是开源标准，不依赖特定AWS服务，可在任何环境中使用
2. **示例代码依赖**：配套的GitHub项目硬编码使用Amazon Bedrock Nova Pro模型
3. **替代方案可行**：Spring AI支持多种LLM提供商（Anthropic API、Llama API、Ollama、LiteLLM等），可替换Bedrock
4. **基础设施兼容**：项目使用的ECS Fargate、VPC、ALB等服务在中国区域均可用

## 验证结果

### 验证类型

- ✅ GitHub项目部署验证

### 执行状态

**状态**: ❌ 失败

**原因**: 配套GitHub项目硬编码依赖Amazon Bedrock Nova Pro模型，该服务在中国区域不可用。根据验证策略，替换核心服务超出允许的修正范围（仅允许endpoint URL调整、区域配置、网络配置优化），因此未进行实际部署。

### 关键发现

1. **硬编码Bedrock依赖**
   - 项目配置文件中明确指定：`spring.ai.bedrock.converse.chat.options.model=amazon.nova-pro-v1:0`
   - IAM策略授予Bedrock InvokeModel权限
   - 影响：无法直接在中国区域部署

2. **区域硬编码**
   - CloudFormation模板中Bedrock ARN硬编码为us-east-1
   - 影响：需要修改配置以适配中国区域

3. **基础设施服务兼容**
   - 使用ECS Fargate、VPC、ECR、CloudWatch Logs、ALB等服务
   - 这些服务在中国区域均可用
   - 影响：基础设施层面无障碍

## 实施建议

### 推荐方案

**概念学习与理解**：
- 文章的核心价值在于介绍MCP协议及其在代理间通信中的应用
- MCP协议本身是开源的，可以在任何环境中学习和使用
- 建议重点关注：MCP的架构设计、能力发现机制、安全认证、上下文共享等概念

**实践实施路径**：
- 不建议直接部署配套的GitHub项目，需要进行重大修改
- 可以学习项目的架构设计和MCP集成模式
- 使用替代LLM服务重新实现类似功能

### 替代方案

1. **使用国内LLM服务**
   - 实施方式：将Spring AI配置修改为使用国内可用的LLM API（如通义千问、文心一言等）
   - 复杂度：中
   - 适用场景：需要在中国区域实际部署MCP代理系统
   - 修改要点：
     - 替换`application.properties`中的Bedrock配置
     - 修改IAM策略，移除Bedrock权限
     - 配置对应LLM服务的API密钥和endpoint

2. **使用自托管开源模型**
   - 实施方式：在EC2或ECS上部署开源LLM（如Llama、Mistral），通过Ollama或vLLM提供API
   - 复杂度：高
   - 适用场景：对数据隐私有严格要求，或需要完全自主控制的场景
   - 修改要点：
     - 部署模型推理服务
     - 配置Spring AI使用Ollama或OpenAI兼容的API
     - 调整ECS任务定义，增加模型服务容器

3. **使用LiteLLM代理层**
   - 实施方式：部署LiteLLM作为统一代理层，支持多种LLM提供商
   - 复杂度：中
   - 适用场景：需要灵活切换不同LLM提供商，或使用多个LLM服务
   - 修改要点：
     - 部署LiteLLM服务
     - 配置Spring AI连接到LiteLLM endpoint
     - 在LiteLLM中配置可用的LLM提供商

### 风险提示

- **API兼容性**：不同LLM提供商的API格式和能力可能有差异，需要测试验证
- **性能差异**：替代模型的性能和响应质量可能与Bedrock Nova Pro不同
- **成本考虑**：自托管模型需要持续的计算资源成本，商业API按调用计费
- **网络连接**：使用国际LLM服务可能面临网络延迟或连接稳定性问题
- **合规要求**：使用第三方LLM服务需要考虑数据隐私和合规要求

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/Sample-Model-Context-Protocol-Demos/tree/main/modules/spring-ai-mcp-inter-agent-ecs
- **兼容性**: 不可直接在中国区使用
- **修改建议**: 
  - 必须替换Bedrock配置为可用的LLM服务
  - 修改CloudFormation模板中的IAM策略
  - 调整区域相关的硬编码配置
  - 建议工作量：2-3天（包括LLM服务选型、配置调整、测试验证）

### MCP协议资源

- **官方文档**: https://modelcontextprotocol.io/introduction
- **GitHub讨论区**: https://github.com/orgs/modelcontextprotocol/discussions
- **客户端快速开始**: https://modelcontextprotocol.io/quickstart/client
- **服务端快速开始**: https://modelcontextprotocol.io/quickstart/server
- **AWS MCP指南**: https://community.aws/content/2v8AETAkyvPp9RVKC4YChncaEbs/running-mcp-based-agents-clients-servers-on-aws
