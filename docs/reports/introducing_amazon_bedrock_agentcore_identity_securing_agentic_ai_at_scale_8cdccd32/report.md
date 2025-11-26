---
title: 介绍Amazon Bedrock AgentCore Identity：大规模保护代理AI安全
publish_date: 2025-08-15
original_url: https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-identity-securing-agentic-ai-at-scale/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 6
unavailable_services: 1
---

# 介绍Amazon Bedrock AgentCore Identity：大规模保护代理AI安全

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-identity-securing-agentic-ai-at-scale/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

Amazon Bedrock AgentCore Identity是本博客介绍的核心产品,目前在AWS中国区域不可用。由于整个解决方案完全依赖于该服务,无法在中国区域实施。

## 服务分析

### 可用服务 (6个)

- AWS IAM (Identity and Access Management)
- AWS KMS (Key Management Service)
- Amazon Cognito
- AWS Secrets Manager
- Amazon CloudWatch
- Amazon SageMaker

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务,包括:
  - Amazon Bedrock AgentCore Identity
  - Amazon Bedrock AgentCore Runtime
  - Amazon Bedrock AgentCore Gateway

### 评估说明

虽然从数量上看,可用服务占比达到85.7%,但Amazon Bedrock AgentCore Identity是整篇博客的核心主题和唯一实现方式。该服务提供了:

1. **Agent Identity Directory** - 代理身份目录管理
2. **Agent Authorizer** - 代理授权验证
3. **Resource Credential Provider** - 资源凭证提供者
4. **Resource Token Vault** - 资源令牌保管库

这些功能是专门为AI代理身份和访问管理设计的,不是可以用其他AWS服务简单替代的通用功能。博客中的所有示例代码、SDK集成、OAuth流程管理都完全依赖于AgentCore Identity服务。

其他可用的服务(如IAM、Cognito、Secrets Manager)虽然可以提供部分身份管理和凭证存储功能,但无法提供AgentCore Identity的核心能力:
- 专门为AI代理设计的身份管理
- 双向认证模型(入站和出站)
- 与AgentCore Runtime和Gateway的深度集成
- 自动化的OAuth令牌管理和注入

## 验证结果

### 验证类型

- ⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Bedrock在AWS中国区域不可用,整个解决方案无法实施,因此跳过GitHub项目部署验证和教程步骤验证。

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此方案**

由于Amazon Bedrock AgentCore Identity服务在中国区域不可用,且该服务是整个解决方案的核心,无法通过简单的服务替换或配置调整来实现相同功能。

### 替代方案

如果需要在AWS中国区域实现类似的AI代理身份和访问管理功能,可以考虑以下自建方案:

1. **基础身份管理方案**
   - 实施方式: 使用Amazon Cognito进行用户身份验证,结合AWS IAM进行服务间认证,使用AWS Secrets Manager存储OAuth令牌和API密钥
   - 复杂度: 高
   - 适用场景: 需要完全自定义的身份管理流程,有专门的开发团队维护
   - 局限性: 
     - 需要自行实现OAuth流程管理
     - 缺少专门为AI代理设计的身份目录
     - 需要手动处理令牌刷新和注入逻辑
     - 无法使用AgentCore SDK的声明式注解

2. **第三方身份管理平台集成**
   - 实施方式: 集成企业级身份管理平台(如Okta、Auth0等)处理OAuth流程,结合自定义代码实现代理身份管理
   - 复杂度: 中到高
   - 适用场景: 已有企业身份管理基础设施,需要与现有系统集成
   - 局限性:
     - 需要额外的第三方服务费用
     - 仍需自行开发代理特定的身份管理逻辑
     - 缺少与AWS服务的原生集成

3. **等待服务在中国区域上线**
   - 实施方式: 关注AWS中国区域服务更新,等待Amazon Bedrock及AgentCore服务正式发布
   - 复杂度: 低(无需开发)
   - 适用场景: 项目时间线灵活,可以等待服务上线
   - 建议: 定期查看AWS中国区域服务公告

### 风险提示

- **功能完整性风险**: 自建方案无法完全复制AgentCore Identity的所有功能,特别是与AgentCore Runtime和Gateway的深度集成
- **开发成本风险**: 自建身份管理系统需要大量开发和维护工作,包括OAuth流程、令牌管理、安全审计等
- **安全合规风险**: 自建方案需要确保符合企业安全标准和合规要求,包括加密、审计日志、访问控制等
- **维护成本风险**: 持续的安全更新、漏洞修复和功能增强需要专门的团队支持
- **技术债务风险**: 如果未来Amazon Bedrock在中国区域上线,需要进行系统迁移

### 配套资源

- **GitHub仓库**: https://github.com/awslabs/amazon-bedrock-agentcore-samples
- **兼容性**: 不可在AWS中国区域使用,因为依赖Amazon Bedrock AgentCore服务
- **修改建议**: 无法通过简单修改使其在中国区域运行,需要完全重新设计身份管理架构
