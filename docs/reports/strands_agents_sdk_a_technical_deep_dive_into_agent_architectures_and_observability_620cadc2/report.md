---
title: Strands Agents SDK：代理架构和可观测性的技术深度解析
publish_date: 2025-07-31
original_url: https://aws.amazon.com/blogs/machine-learning/strands-agents-sdk-a-technical-deep-dive-into-agent-architectures-and-observability/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 14
unavailable_services: 5
---

# Strands Agents SDK：代理架构和可观测性的技术深度解析

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/strands-agents-sdk-a-technical-deep-dive-into-agent-architectures-and-observability/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

虽然73.7%的服务在中国区可用，但核心服务Amazon Bedrock及其相关组件（Bedrock Agents、Bedrock AgentCore）在中国区不可用。文章的主要内容围绕使用Bedrock上的基础模型来运行Strands Agents SDK，这使得按原文直接实施存在重大障碍。

## 服务分析

### 可用服务 (14个)

- AWS Glue
- Amazon EC2
- AWS Lambda
- AWS Fargate
- AWS X-Ray
- Amazon CloudWatch
- Amazon DynamoDB
- AWS Step Functions
- AWS KMS
- Amazon ECS
- Amazon EKS
- Amazon API Gateway
- AWS IAM
- Amazon Cognito
- VPC Reachability Analyzer

### 不可用服务 (5个)

- **Amazon Bedrock** - 核心服务
- **Amazon Bedrock Agents** - 核心服务
- **Amazon Bedrock AgentCore** - 核心服务
- **Amazon Q** - 核心服务（文章中的实际应用案例）
- **Amazon Kendra** - 文章中提到的相关服务

### 评估说明

1. **核心服务不可用**：Amazon Bedrock是文章的核心依赖，Strands Agents SDK虽然支持多种模型提供商，但文章重点介绍的是与Bedrock的集成和在AWS环境中的部署。

2. **生产部署受限**：文章推荐的生产级部署方式Amazon Bedrock AgentCore在中国区不可用，这意味着无法使用文章中描述的最佳实践进行部署。

3. **实际案例不适用**：文章中提到的Amazon Q、AWS Glue中的AI代理等实际应用案例都依赖于Bedrock，在中国区无法复现。

4. **基础设施服务可用**：好消息是大部分AWS基础设施服务（Lambda、ECS、CloudWatch等）在中国区可用，这为替代方案提供了基础。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 由于核心服务Amazon Bedrock在中国区不可用，且文章的主要内容围绕Bedrock集成，直接部署验证无实际意义。根据验证流程，LOW等级的内容跳过深入验证阶段。

## 实施建议

### 推荐方案

**不建议直接实施**

由于Amazon Bedrock在中国区不可用，无法按照原文描述的方式使用Strands Agents SDK。但是，Strands SDK本身是开源的，支持多种模型提供商，因此可以考虑以下替代方案。

### 替代方案

1. **使用第三方模型API**
   - 实施方式：配置Strands SDK使用Anthropic API、OpenAI API或其他可访问的商业模型API
   - 复杂度：中
   - 适用场景：对模型性能要求高，可以接受使用国际API服务（需考虑网络连接和合规性）
   - 限制：需要确保网络连接稳定，可能涉及数据出境合规问题

2. **使用开源模型（本地或自托管）**
   - 实施方式：
     - 使用Ollama在本地或EC2实例上运行开源模型（如Llama 3、Qwen等）
     - 在Amazon SageMaker上部署开源模型，通过API调用
     - 配置Strands SDK连接到自托管的模型端点
   - 复杂度：高
   - 适用场景：对数据安全和合规性要求高，需要完全控制模型部署
   - 优势：数据不出境，完全可控
   - 挑战：需要自行管理模型部署、性能优化和扩展

3. **混合架构**
   - 实施方式：
     - 核心推理逻辑使用自托管开源模型
     - AWS基础设施服务（Lambda、ECS、CloudWatch、DynamoDB等）用于部署和监控
     - 使用AWS X-Ray和CloudWatch实现文章中描述的可观测性功能
   - 复杂度：高
   - 适用场景：需要在中国区实现类似架构，同时保持数据合规性
   - 优势：充分利用AWS中国区可用的基础设施服务

4. **等待服务上线**
   - 实施方式：关注Amazon Bedrock在中国区的上线计划
   - 复杂度：低
   - 适用场景：项目时间线允许等待，希望使用原生AWS服务
   - 注意：目前没有Bedrock在中国区上线的明确时间表

### 风险提示

- **模型性能差异**：使用替代模型提供商或开源模型，性能和能力可能与文章中使用的Claude等模型存在差异
- **集成复杂度**：虽然Strands SDK支持多种模型提供商，但文章中的示例和最佳实践都基于Bedrock，需要额外的适配工作
- **可观测性功能**：文章中描述的与AWS X-Ray、CloudWatch的深度集成需要额外配置，可能无法达到相同的开箱即用体验
- **生产部署**：无法使用Amazon Bedrock AgentCore，需要自行设计和实现生产级部署架构
- **合规性考虑**：如果使用国际API服务，需要评估数据出境的合规性要求
- **成本考虑**：自托管模型需要考虑计算资源成本（GPU实例），可能高于托管服务
- **维护负担**：自托管方案需要持续的运维和模型更新工作

### 配套资源

- **Strands Agents SDK官网**: https://strandsagents.com/latest/
- **GitHub示例仓库**: https://github.com/strands-agents/samples
- **兼容性**: SDK本身开源且支持多种模型提供商，可在中国区使用
- **修改建议**: 
  - 将模型提供商从Amazon Bedrock切换到可访问的替代方案（Anthropic API、OpenAI、或自托管开源模型）
  - 保留AWS基础设施服务的使用（Lambda、ECS、CloudWatch等）
  - 根据选择的模型提供商调整认证和端点配置
  - 实现自定义的可观测性集成以替代Bedrock AgentCore的功能
