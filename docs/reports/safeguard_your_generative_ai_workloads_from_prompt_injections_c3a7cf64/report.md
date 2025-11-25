---
title: 保护生成式AI工作负载免受提示注入攻击
publish_date: 2025-01-21
original_url: https://aws.amazon.com/blogs/security/safeguard-your-generative-ai-workloads-from-prompt-injections/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 11
unavailable_services: 2
---

# 保护生成式AI工作负载免受提示注入攻击

[📖 查看原始博客](https://aws.amazon.com/blogs/security/safeguard-your-generative-ai-workloads-from-prompt-injections/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Bedrock在中国区域不可用，方案无法直接实施

该博客的核心内容完全基于Amazon Bedrock及其Guardrails功能，而Amazon Bedrock服务在AWS中国区域不可用，导致整个解决方案无法在中国区域实施。

## 服务分析

### 可用服务 (11个)

- Amazon SageMaker
- Amazon CloudFront
- Amazon S3
- Amazon Cognito
- Amazon API Gateway
- AWS Lambda
- AWS IAM
- Amazon CloudWatch
- AWS CloudFormation
- AWS WAF
- AWS CloudTrail

### 不可用服务 (2个)

- **Amazon Bedrock** - 核心服务
- **AWS Amplify**

### 评估说明

虽然可用服务占比达到84.6%，但Amazon Bedrock是该方案的核心服务，文章的所有关键功能都依赖于：

1. **Amazon Bedrock基础模型**：提供生成式AI能力
2. **Amazon Bedrock Guardrails**：实现内容审核、提示攻击过滤、PII识别等核心安全功能
3. **Amazon Bedrock API**：包括CreateGuardrail、ApplyGuardrail、Converse等关键API

没有Amazon Bedrock，整个提示注入防护方案无法实现。AWS Amplify的缺失影响相对较小，可以使用其他前端框架替代。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Bedrock在AWS中国区域不可用，无法进行实际部署验证。即使部署其他组件，也无法实现文章描述的核心功能。

## 实施建议

### 推荐方案

不建议在AWS中国区域直接实施该方案。核心服务的缺失使得原方案的主要价值无法实现。

### 替代方案

如果需要在AWS中国区域实现类似的生成式AI安全防护功能，可以考虑以下替代方案：

1. **使用Amazon SageMaker部署自托管模型**
   - 实施方式：在SageMaker上部署开源大语言模型（如Llama、ChatGLM等），自行实现输入输出过滤逻辑
   - 复杂度：高
   - 适用场景：有较强技术团队，能够自行开发和维护安全防护机制
   - 局限性：需要自行实现Guardrails的所有功能，包括内容审核、提示攻击检测、PII识别等

2. **集成第三方AI安全服务**
   - 实施方式：使用第三方AI安全平台（如国内的AI安全服务提供商）结合SageMaker部署的模型
   - 复杂度：中
   - 适用场景：希望快速获得AI安全能力，但不想完全自研
   - 局限性：依赖第三方服务，可能存在数据隐私和合规考虑

3. **自建提示注入防护系统**
   - 实施方式：基于AWS Lambda、API Gateway等服务，自行开发输入验证、内容过滤、访问控制等安全机制
   - 复杂度：高
   - 适用场景：对安全要求极高，需要完全自主可控的解决方案
   - 局限性：开发和维护成本高，需要持续更新防护规则

### 风险提示

- **功能缺失风险**：任何替代方案都无法完全复制Amazon Bedrock Guardrails的功能和易用性
- **开发成本风险**：自建方案需要投入大量开发和维护资源
- **安全效果风险**：自研的安全防护机制可能不如AWS托管服务成熟和全面
- **合规风险**：使用第三方服务需要评估数据处理的合规性

### 配套资源

- **AWS Workshop**: [Building Secure and Responsible Generative AI Applications with Amazon Bedrock Guardrails](https://catalog.us-east-1.prod.workshops.aws/workshops/53c38a96-45e0-4019-967a-c73dcbe7a839/en-US)
- **兼容性**: 该workshop完全基于Amazon Bedrock，无法在中国区域使用
- **修改建议**: 不适用，核心服务不可用
