---
title: 使用 Bedrock AgentCore Gateway 拦截器应用细粒度访问控制
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/machine-learning/apply-fine-grained-access-control-with-bedrock-agentcore-gateway-interceptors/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 3
unavailable_services: 2
---

# 使用 Bedrock AgentCore Gateway 拦截器应用细粒度访问控制

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/apply-fine-grained-access-control-with-bedrock-agentcore-gateway-interceptors/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务 Amazon Bedrock AgentCore Gateway 及其 gateway interceptors 功能在中国区域不可用，无法实施本文介绍的技术方案

本文介绍的 Amazon Bedrock AgentCore Gateway 的 gateway interceptors 功能是2025年11月26日发布的新特性，目前处于预览阶段。该功能是实现细粒度访问控制的核心组件，但在AWS中国区域（北京和宁夏）尚未提供服务。

## 服务分析

### 可用服务 (3个)

- **AWS Lambda** - 用于实现自定义拦截器逻辑
- **Amazon CloudWatch** - 用于监控和日志记录
- **Amazon Cognito** - 用于OAuth 2.0身份验证和JWT令牌管理

### 不可用服务 (2个)

- **Amazon Bedrock AgentCore Gateway** - 核心服务，文章的主要技术实现基础
- **Amazon Bedrock AgentCore Gateway Interceptors** - 核心功能，用于实现请求/响应拦截和细粒度访问控制

### 评估说明

本文的核心技术方案完全依赖于 Amazon Bedrock AgentCore Gateway 及其 gateway interceptors 功能。该服务提供以下关键能力：

1. **Gateway Request Interceptor** - 在请求到达目标工具前进行处理，实现细粒度访问控制、审计跟踪、模式转换等
2. **Gateway Response Interceptor** - 在响应返回调用代理前进行处理，实现工具过滤、模式转换等
3. **MCP (Model Context Protocol) 集成** - 将现有API和Lambda函数转换为代理兼容的工具

由于这两个核心服务在中国区域不可用，文章介绍的所有技术实现方案（包括细粒度访问控制、动态工具过滤、自定义头传播、OAuth授权等）都无法在中国区域实施。虽然 Lambda、CloudWatch 和 Cognito 等支持服务可用，但缺少核心的 AgentCore Gateway 平台，这些服务无法组合实现文章描述的功能。

## 验证结果

### 验证类型

⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务 Amazon Bedrock AgentCore Gateway 在中国区域不可用，无法进行实际部署验证。该服务是实现本文所有技术方案的基础平台，缺少该服务将导致所有功能无法实现。

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施本文方案**

由于核心服务不可用，建议采取以下策略：

1. **等待服务上线** - 关注 Amazon Bedrock AgentCore 服务在中国区域的发布计划
2. **使用全球区域** - 如果业务允许，可以在AWS全球区域（如美国东部、美国西部等）实施本方案
3. **考虑替代架构** - 在中国区域使用其他方式实现类似的访问控制需求

### 替代方案

#### 方案1：API Gateway + Lambda 自定义授权器

- **实施方式**：使用 Amazon API Gateway 的 Lambda 授权器实现细粒度访问控制
  - 在 API Gateway 层面配置 Lambda 授权器验证 JWT 令牌
  - 使用 Lambda 函数实现工具级别的权限检查
  - 通过 API Gateway 的请求/响应转换功能实现模式转换
  - 使用 CloudWatch 实现可观测性
- **复杂度**：高
- **适用场景**：需要在中国区域实现类似的访问控制和工具管理功能，但无法使用 AgentCore Gateway
- **限制**：
  - 需要自行实现 MCP 协议支持
  - 缺少 AgentCore 的原生代理集成能力
  - 需要更多的自定义开发工作

#### 方案2：Application Load Balancer + Lambda 目标

- **实施方式**：使用 Application Load Balancer (ALB) 作为统一入口点
  - 配置 ALB 的认证功能集成 Cognito
  - 使用 Lambda 作为目标实现业务逻辑和访问控制
  - 通过 ALB 规则实现基于路径的路由
  - 在 Lambda 中实现工具过滤和权限验证
- **复杂度**：中
- **适用场景**：需要统一的入口点管理多个后端服务，但不需要完整的 MCP 协议支持
- **限制**：
  - 缺少 AgentCore 的代理编排能力
  - 需要自行实现工具发现和调用机制
  - 可观测性需要额外配置

#### 方案3：自建网关服务

- **实施方式**：在 ECS 或 EKS 上部署自定义网关服务
  - 使用开源 API 网关（如 Kong、Tyk）或自研网关
  - 实现 MCP 协议支持
  - 集成 Cognito 进行身份验证
  - 实现自定义拦截器逻辑
- **复杂度**：高
- **适用场景**：需要完全控制网关行为，且有足够的开发和运维资源
- **限制**：
  - 需要大量开发和维护工作
  - 缺少 AWS 托管服务的便利性
  - 需要自行处理扩展性和高可用性

### 风险提示

- **服务可用性风险**: Amazon Bedrock AgentCore Gateway 在中国区域的上线时间不确定，可能需要较长等待期
- **功能差异风险**: 即使服务未来在中国区域上线，功能特性可能与全球区域存在差异或延迟
- **架构迁移风险**: 如果先采用替代方案，未来迁移到 AgentCore Gateway 可能需要重构代码和架构
- **合规性风险**: 如果选择在全球区域实施，需要确保符合数据本地化和跨境传输的合规要求
- **成本风险**: 替代方案可能需要更多的开发和运维成本，且性能可能不如原生服务

### 配套资源

- **GitHub仓库**: 
  - [Fine-grained access control](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway/09-fine-grained-access-control)
  - [Custom header propagation](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway/08-custom-header-propagation)
- **兼容性**: 这些示例代码依赖 Amazon Bedrock AgentCore Gateway 服务，无法在中国区域直接使用
- **修改建议**: 
  - 代码无法通过简单修改在中国区域运行
  - 如需实现类似功能，建议参考代码逻辑，使用上述替代方案重新实现
  - 重点关注 JWT 验证、权限检查和请求转换的实现逻辑，这些可以应用到替代方案中

### 官方文档

- [Amazon Bedrock AgentCore Gateway 文档](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) - 全球区域文档
- [Fine-grained access control for Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-fine-grained-access-control.html) - 全球区域文档

**注意**: 以上文档链接指向全球区域的服务文档，中国区域暂无对应文档。
