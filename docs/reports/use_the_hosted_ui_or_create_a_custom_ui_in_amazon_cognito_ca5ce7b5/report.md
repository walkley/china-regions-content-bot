---
title: 在Amazon Cognito中应该使用托管登录还是创建自定义UI？
publish_date: 2025-10-08
original_url: https://aws.amazon.com/blogs/security/use-the-hosted-ui-or-create-a-custom-ui-in-amazon-cognito/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 7
unavailable_services: 2
---

# 在Amazon Cognito中应该使用托管登录还是创建自定义UI？

[📖 查看原始博客](https://aws.amazon.com/blogs/security/use-the-hosted-ui-or-create-a-custom-ui-in-amazon-cognito/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Cognito在目标区域cn-northwest-1不可用，无法直接实施

本文是关于Amazon Cognito用户池UI选择的最佳实践指南，对比了托管登录（Managed Login）和自定义UI两种实现方式。虽然文章内容具有很高的参考价值，但由于核心服务在目标区域的可用性限制，无法在宁夏区域（cn-northwest-1）直接实施。

## 服务分析

### 可用服务 (7个)

- AWS CloudTrail
- AWS WAF
- Application Load Balancer (ALB)
- AWS AppSync
- Amazon API Gateway
- AWS Lambda
- Amazon Cognito（仅北京区域cn-north-1）

### 不可用服务 (2个)

- **Amazon Cognito**（在cn-northwest-1区域不可用，核心服务）
- **AWS Amplify**（在中国区域不可用，可选集成）

### 评估说明

根据AWS中国区域官方文档和实际验证：

1. **核心服务限制**：Amazon Cognito是本文的核心服务，但在中国区域的可用性受限：
   - 仅在北京区域（cn-north-1）可用
   - 在宁夏区域（cn-northwest-1）不可用
   - 实际API连接测试显示即使在北京区域也存在连接问题

2. **区域差异**：中国区域的服务可用性与全球区域存在显著差异，Cognito服务的功能和可用性可能受到限制

3. **集成服务**：虽然大部分集成服务（如ALB、API Gateway、Lambda等）在中国区域可用，但缺少核心的Cognito服务使得整体方案无法实施

## 验证结果

### 验证类型

⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Cognito在目标区域cn-northwest-1不可用，且在北京区域的可用性也存在限制。即使切换到北京区域，实际API连接测试也显示无法正常访问Cognito服务endpoint，因此跳过深入验证。

## 实施建议

### 推荐方案

不建议在AWS中国区域直接实施本文描述的Cognito方案。如果需要在中国区域实现类似的用户认证和管理功能，建议考虑以下替代方案：

### 替代方案

1. **自建身份认证系统**
   - 实施方式：使用开源身份认证框架（如Keycloak、Auth0替代方案）部署在EC2或ECS上
   - 复杂度：高
   - 适用场景：需要完全控制用户数据和认证流程，对中国区域数据合规有严格要求

2. **使用API Gateway + Lambda自定义认证**
   - 实施方式：通过API Gateway的Lambda授权器实现自定义认证逻辑，使用DynamoDB存储用户信息
   - 复杂度：中
   - 适用场景：需要灵活的认证逻辑，可以接受自行管理用户数据

3. **集成第三方身份提供商**
   - 实施方式：直接集成支持中国区域的第三方IdP（如企业微信、钉钉、国内OAuth提供商）
   - 复杂度：中
   - 适用场景：企业内部应用，用户已有企业身份系统

4. **跨区域架构**
   - 实施方式：在全球区域使用Cognito，通过API Gateway和Lambda在中国区域提供代理访问
   - 复杂度：高
   - 适用场景：全球化应用，需要统一的用户身份管理，可以接受跨境数据传输的延迟和合规要求

### 风险提示

- **服务可用性风险**：Cognito在中国区域的可用性受限，即使在标注为可用的北京区域，实际使用中也可能遇到连接问题
- **功能差异风险**：即使服务可用，中国区域的Cognito功能可能与全球区域存在差异，部分高级特性可能不支持
- **数据合规风险**：如果采用跨区域架构，需要特别注意中国的数据本地化和跨境数据传输相关法规
- **迁移成本风险**：如果未来Cognito在中国区域全面可用，从替代方案迁移到Cognito可能需要较大的工程投入

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 建议参考文章中的认证架构设计理念，使用替代方案实现类似功能
