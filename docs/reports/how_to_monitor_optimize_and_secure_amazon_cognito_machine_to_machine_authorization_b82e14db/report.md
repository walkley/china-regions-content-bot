---
title: 如何监控、优化和保护Amazon Cognito机器对机器授权
publish_date: 2025-01-13
original_url: https://aws.amazon.com/blogs/security/how-to-monitor-optimize-and-secure-amazon-cognito-machine-to-machine-authorization/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 8
unavailable_services: 1
---

# 如何监控、优化和保护Amazon Cognito机器对机器授权

[📖 查看原始博客](https://aws.amazon.com/blogs/security/how-to-monitor-optimize-and-secure-amazon-cognito-machine-to-machine-authorization/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Cognito在AWS中国区域无法正常使用，方案无法直接实施

本文的核心服务Amazon Cognito虽然在AWS中国官网显示在北京区域（cn-north-1）可用，但实际API调用测试显示无法连接到Cognito服务端点。这使得整个M2M授权方案无法在中国区域实施。

## 服务分析

### 可用服务 (8个)

- Amazon API Gateway
- AWS CloudTrail
- Amazon CloudWatch
- AWS Secrets Manager
- AWS WAF
- AWS Lambda
- Amazon EventBridge
- Amazon Verified Permissions

### 不可用服务 (1个)

- **Amazon Cognito** - 核心服务，无法连接到中国区域端点

### 评估说明

1. **核心服务不可用**：Amazon Cognito是本文的核心服务，用于实现OAuth 2.0客户端凭证授权流程和M2M授权。虽然AWS中国官网显示该服务在北京区域可用，但实际测试表明无法连接到服务端点（`https://cognito-idp.cn-north-1.amazonaws.com.cn/` 和 `https://cognito-idp.cn-northwest-1.amazonaws.com.cn/`）。

2. **辅助服务可用**：文章中提到的其他服务（API Gateway、CloudWatch、WAF等）在中国区域均可用，但这些服务都是围绕Cognito构建的辅助功能。

3. **无直接替代方案**：Amazon Cognito作为托管的身份和访问管理（CIAM）服务，在AWS中国区域没有直接的官方替代服务。

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Cognito在AWS中国区域不可用，无法进行实际部署验证。基础验证阶段已确认方案不可行。

### 关键发现

1. **Cognito服务端点不可达**
   - 测试了cn-northwest-1和cn-north-1两个区域
   - 所有API调用均返回连接错误
   - 官网显示与实际可用性存在差异

2. **架构依赖性强**
   - 整个M2M授权流程完全依赖Cognito
   - 无法通过简单配置调整解决
   - 需要重新设计整体架构

## 实施建议

### 推荐方案

**不建议直接实施**

由于核心服务Amazon Cognito在AWS中国区域不可用，本文描述的方案无法直接在中国区域实施。

### 替代方案

1. **使用开源身份认证解决方案**
   - 实施方式：部署Keycloak、Auth0或其他开源OAuth 2.0服务器
   - 复杂度：高
   - 适用场景：需要完全控制身份认证流程，可以接受自行维护的团队
   - 注意事项：需要自行管理高可用性、扩展性和安全更新

2. **使用API Gateway + Lambda自定义授权**
   - 实施方式：
     - 使用Lambda函数实现OAuth 2.0客户端凭证流程
     - 在DynamoDB中存储客户端凭证和令牌
     - 使用API Gateway Lambda授权器验证令牌
     - 使用Secrets Manager存储密钥
   - 复杂度：中
   - 适用场景：需要轻量级M2M授权，不需要完整的用户管理功能
   - 优势：完全使用中国区域可用服务，可控性强

3. **使用第三方中国本地化身份服务**
   - 实施方式：集成符合中国合规要求的第三方身份认证服务
   - 复杂度：中
   - 适用场景：需要符合中国本地合规要求的企业
   - 注意事项：需要评估第三方服务的可靠性和安全性

### 风险提示

- **服务可用性风险**: Amazon Cognito在中国区域的可用性状态不明确，官网显示与实际测试结果不一致
- **架构重构成本**: 采用替代方案需要重新设计整体架构，开发和测试成本较高
- **功能差异风险**: 替代方案可能无法完全复制Cognito的所有功能特性
- **维护成本**: 自建方案需要持续投入维护资源，包括安全更新、性能优化等
- **合规性风险**: 在中国区域实施身份认证服务需要确保符合当地法律法规要求

### 配套资源

- **GitHub仓库**: 文章未提供配套代码仓库
- **兼容性**: 不适用
- **修改建议**: 建议参考文章中的架构设计思路，使用替代方案重新实现M2M授权流程

## 补充说明

### 监控和成本管理

文章中提到的CUDOS（Cost and Usage Dashboards Operations Solution）仪表板在中国区域可用，可以用于监控其他AWS服务的使用情况和成本。但由于Cognito不可用，相关的M2M令牌请求监控功能无法使用。

### 安全最佳实践

文章中提到的安全最佳实践（如使用Secrets Manager、WAF、Lambda授权器等）在中国区域仍然适用，可以应用于替代方案的实施中。

### 建议行动

1. 如果必须在AWS中国区域实施M2M授权，建议采用"API Gateway + Lambda自定义授权"替代方案
2. 联系AWS中国支持团队确认Amazon Cognito的实际可用性和未来规划
3. 评估业务需求，考虑是否可以使用AWS全球区域的Cognito服务（需要考虑网络延迟和合规性）
