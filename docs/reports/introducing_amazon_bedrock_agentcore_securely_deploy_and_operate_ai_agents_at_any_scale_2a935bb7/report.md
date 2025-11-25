---
title: 介绍Amazon Bedrock AgentCore：在任何规模下安全部署和运营AI代理（预览版）
publish_date: 2025-07-16
original_url: https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 10
unavailable_services: 4
---

# 介绍Amazon Bedrock AgentCore：在任何规模下安全部署和运营AI代理（预览版）

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Bedrock及其所有相关服务在中国区域不可用，整个方案无法实施

Amazon Bedrock AgentCore是完全基于Amazon Bedrock构建的企业级AI代理服务套件。由于Amazon Bedrock在AWS中国区域不可用，该方案的所有核心功能都无法使用，没有直接的替代方案。

## 服务分析

### 可用服务 (10个)

- AWS Lambda
- AWS IAM
- Amazon ECR
- Amazon S3
- Amazon DynamoDB
- Amazon CloudWatch
- AWS X-Ray
- Amazon Cognito
- AWS PrivateLink
- AWS Marketplace

### 不可用服务 (4个)

- **Amazon Bedrock** - 核心服务
- **Amazon Bedrock Agents** - 核心服务
- **Amazon Bedrock Knowledge Bases** - 核心服务
- **Amazon Bedrock AgentCore** - 核心服务（包含Runtime、Memory、Observability、Identity、Gateway、Browser、Code Interpreter等所有子服务）

### 评估说明

虽然从数量上看，可用服务占比达到71.4%，但这些可用服务都是支撑性服务。文章的核心内容是介绍Amazon Bedrock AgentCore，这是一个完全基于Amazon Bedrock构建的新服务套件，包括：

1. **AgentCore Runtime** - 提供无服务器环境运行AI代理
2. **AgentCore Memory** - 管理会话和长期记忆
3. **AgentCore Observability** - 提供可观测性和调试能力
4. **AgentCore Identity** - 管理身份和访问控制
5. **AgentCore Gateway** - 转换API为代理工具
6. **AgentCore Browser** - 提供托管浏览器实例
7. **AgentCore Code Interpreter** - 提供代码执行环境

由于Amazon Bedrock在中国区域不可用，上述所有AgentCore服务都无法使用。文章中的所有示例代码、部署步骤和功能演示都依赖于这些不可用的服务。

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证结果为LOW，核心服务Amazon Bedrock及其所有相关服务在中国区域不可用，整个方案无法实施，不满足深入验证的触发条件（需要MODERATE或HIGH）。

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此方案**

Amazon Bedrock AgentCore是一个完全依赖于Amazon Bedrock的服务套件，在中国区域无法使用。整个方案的核心价值在于：
- 简化AI代理的生产部署
- 提供企业级的会话管理、身份控制、记忆系统和可观测性
- 支持多种开源AI代理框架（CrewAI、LangGraph、LlamaIndex、Strands Agents等）

由于核心服务不可用，这些价值无法在中国区域实现。

### 替代方案

如果需要在AWS中国区域构建类似的AI代理解决方案，可以考虑以下替代方案：

1. **自建AI代理基础设施**
   - 实施方式：使用开源AI代理框架（如LangChain、LlamaIndex等）结合AWS中国区域可用的服务自行构建
   - 复杂度：高
   - 适用场景：有充足的开发资源和时间，需要完全自主控制的场景
   - 主要组件：
     - 使用AWS Lambda或Amazon ECS运行代理代码
     - 使用Amazon DynamoDB存储会话和记忆数据
     - 使用Amazon CloudWatch和AWS X-Ray实现可观测性
     - 使用AWS IAM和Amazon Cognito管理身份和访问控制
     - 使用第三方或自部署的大语言模型服务（非AWS Bedrock）

2. **使用第三方AI平台**
   - 实施方式：评估在中国区域可用的第三方AI代理平台或大语言模型服务
   - 复杂度：中
   - 适用场景：希望快速实现AI代理功能，可以接受第三方服务的场景
   - 注意事项：需要评估数据合规性、服务稳定性和成本

3. **混合云架构**
   - 实施方式：在AWS全球区域使用Amazon Bedrock AgentCore，通过专线或VPN连接到中国区域的应用系统
   - 复杂度：高
   - 适用场景：对数据出境有明确合规路径，且可以接受跨境网络延迟的场景
   - 注意事项：需要满足中国的数据安全和跨境传输相关法规要求

### 风险提示

- **服务不可用风险**: Amazon Bedrock及其所有相关服务在中国区域不可用，短期内没有上线计划的公开信息
- **开发成本风险**: 自建替代方案需要投入大量开发资源，包括会话管理、记忆系统、可观测性等企业级功能的实现
- **维护成本风险**: 自建方案需要持续维护和优化，包括安全更新、性能优化、功能扩展等
- **合规风险**: 如采用混合云架构，需要确保符合中国的数据安全和跨境传输相关法规
- **技术债务风险**: 自建方案可能在未来Amazon Bedrock进入中国区域时需要重构

### 配套资源

- **GitHub仓库**: 
  - https://github.com/aws/bedrock-agentcore-sdk-python (AgentCore SDK)
  - https://github.com/awslabs/amazon-bedrock-agentcore-samples/ (AgentCore示例)
- **兼容性**: 不兼容AWS中国区域，所有代码和示例都依赖于Amazon Bedrock AgentCore服务
- **修改建议**: 无法通过简单修改使其在中国区域运行，需要完全重新设计和实现
