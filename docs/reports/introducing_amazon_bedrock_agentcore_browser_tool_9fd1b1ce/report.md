---
title: 介绍 Amazon Bedrock AgentCore 浏览器工具
publish_date: 2025-08-01
original_url: https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-browser-tool/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 5
unavailable_services: 2
---

# 介绍 Amazon Bedrock AgentCore 浏览器工具

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-browser-tool/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，无法在中国区域实施

Amazon Bedrock AgentCore Browser Tool 是本文的核心服务，属于 Amazon Bedrock 服务家族。该服务在AWS中国区域完全不可用，导致整个方案无法实施。

## 服务分析

### 可用服务 (5个)

- AWS Identity and Access Management (IAM)
- AWS CloudTrail
- Amazon CloudWatch
- Amazon Elastic Compute Cloud (Amazon EC2)
- Amazon SageMaker

### 不可用服务 (2个)

- **Amazon Bedrock** - 核心服务，文章的主要主题
- **Amazon Q Developer** - 文中提及

### 评估说明

虽然可用服务占比达到71.4%，但核心服务 Amazon Bedrock 及其 AgentCore Browser Tool 功能在中国区域完全不可用。该工具是一个完全托管的云端浏览器自动化解决方案，专门为生成式AI代理设计，用于与网站进行交互。

不可用的核心功能包括：
1. AgentCore Browser Tool 的完整浏览器自动化能力
2. 与 Amazon Nova Act 的集成
3. 托管的浏览器基础设施
4. 企业级安全和隔离环境
5. 与 Amazon Bedrock 的原生集成

由于这是一个专有的AWS托管服务，没有直接的替代方案可以提供相同的功能和集成体验。

## 验证结果

### 验证类型

⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务 Amazon Bedrock AgentCore Browser Tool 在中国区域不可用，无法进行实际部署验证。即使配套的 GitHub 项目（https://github.com/awslabs/amazon-bedrock-agentcore-samples）可以克隆，但由于依赖的 AWS 服务不可用，代码无法在中国区域执行。

## 实施建议

### 推荐方案

**不建议在中国区域实施此方案**

Amazon Bedrock AgentCore Browser Tool 是一个完全托管的AWS服务，在中国区域不可用。该服务的核心价值在于：
- 零管理的浏览器集群
- 与 Amazon Bedrock 的深度集成
- 企业级安全和隔离
- 全球自动扩展能力

这些特性无法通过简单的配置调整或服务替换来实现。

### 替代方案

如果需要在中国区域实现类似的浏览器自动化功能，可以考虑以下自建方案：

1. **开源浏览器自动化框架**
   - 实施方式：使用 Playwright、Puppeteer 或 Selenium 搭建自己的浏览器自动化基础设施
   - 复杂度：高
   - 适用场景：需要完全控制浏览器自动化流程，有足够的技术团队维护基础设施
   - 局限性：需要自行管理浏览器实例、扩展、安全隔离和监控

2. **容器化浏览器服务**
   - 实施方式：在 Amazon ECS 或 EKS 上部署容器化的浏览器服务（如 browserless.io 的开源版本）
   - 复杂度：高
   - 适用场景：需要可扩展的浏览器自动化，愿意投入运维资源
   - 局限性：缺少与AI模型的原生集成，需要自行开发代理逻辑

3. **第三方浏览器自动化服务**
   - 实施方式：使用在中国区域可用的第三方浏览器自动化SaaS服务
   - 复杂度：中
   - 适用场景：快速实现浏览器自动化，不需要深度定制
   - 局限性：数据安全考虑，服务可用性依赖第三方

**重要提示**：以上替代方案都无法提供与 Amazon Bedrock 的原生集成，也无法使用 Amazon Nova Act 等AI代理框架。如果核心需求是AI驱动的浏览器自动化，建议等待 Amazon Bedrock 在中国区域上线，或在全球区域使用该服务。

### 风险提示

- **服务不可用风险**：核心服务在中国区域完全不可用，无法实施
- **架构复杂度**：自建替代方案需要大量的基础设施管理和运维工作
- **成本考虑**：自建方案的总拥有成本可能显著高于托管服务
- **安全合规**：自建浏览器自动化需要额外的安全措施和隔离机制
- **AI集成挑战**：替代方案缺少与生成式AI模型的原生集成能力

### 配套资源

- **GitHub仓库**: https://github.com/awslabs/amazon-bedrock-agentcore-samples
- **兼容性**: 代码仓库可以访问，但由于依赖 Amazon Bedrock AgentCore 服务，无法在中国区域运行
- **修改建议**: 不适用 - 核心服务依赖无法通过代码修改解决
