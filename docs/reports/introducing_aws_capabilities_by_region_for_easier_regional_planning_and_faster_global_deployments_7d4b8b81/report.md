---
title: Introducing AWS Capabilities by Region for easier Regional planning and faster global deployments
original_url: https://aws.amazon.com/blogs/aws/introducing-aws-capabilities-by-region-for-easier-regional-planning-and-faster-global-deployments/
validation_date: 2025-11-24
target_region: cn-northwest-1
feasibility: HIGH
available_services: 5
unavailable_services: 0
---

# Introducing AWS Capabilities by Region for easier Regional planning and faster global deployments

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/introducing-aws-capabilities-by-region-for-easier-regional-planning-and-faster-global-deployments/) | 验证日期: 2025-11-24

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

文章介绍的AWS Capabilities by Region规划工具及其涉及的所有AWS服务在中国区域均可用，用户可以正常使用文章中提到的所有核心服务进行实践。

## 服务分析

### 可用服务 (5个)

- Amazon S3 (Amazon Simple Storage Service)
- Amazon DynamoDB
- Amazon API Gateway
- Amazon EC2 (Amazon Elastic Compute Cloud)
- AWS CloudFormation

### 不可用服务 (0个)

无

### 评估说明

本文介绍的是AWS推出的一个新的规划工具"AWS Capabilities by Region"，用于帮助用户发现和比较不同区域的AWS服务、功能、API和CloudFormation资源。文章中提到的所有示例服务（S3、DynamoDB、API Gateway、EC2、CloudFormation）在AWS中国区域均完全可用。

经过实际验证，这些服务在cn-northwest-1区域均可正常访问和使用：
- CloudFormation服务正常，可以管理基础设施即代码
- API Gateway服务正常，可以创建和管理API
- S3服务正常，可以进行对象存储操作
- EC2服务正常，可以查询区域信息和管理计算资源
- DynamoDB服务正常，可以进行NoSQL数据库操作

## 验证结果

### 验证类型

- ✅ 教程步骤验证

### 执行状态

**状态**: ✅ 成功

### 关键发现

1. **AWS Builder Center工具可访问**
   - AWS Capabilities by Region工具网站（https://builder.aws.com/capabilities）可以正常访问（HTTP 200）
   - 用户可以通过该工具查询和比较不同区域的服务可用性

2. **所有示例服务在中国区域完全可用**
   - 文章中用作示例的5个AWS服务在cn-northwest-1区域均已验证可用
   - 服务API调用正常，无需任何修正或调整
   - 中国区域支持文章中提到的所有核心功能

3. **AWS Knowledge MCP Server文档链接问题**
   - 文章提到的AWS Knowledge MCP Server文档链接（https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server/）返回404错误
   - 这不影响文章核心内容的实施，因为该MCP Server是可选的自动化工具，不是必需组件

## 实施建议

### 推荐方案

可直接按照原文实施。文章介绍的AWS Capabilities by Region工具是一个Web界面工具，用于查询和比较AWS服务在不同区域的可用性。中国区域用户可以：

1. **直接使用AWS Capabilities by Region工具**
   - 访问 https://builder.aws.com/capabilities
   - 选择中国区域（cn-north-1或cn-northwest-1）进行服务可用性查询
   - 比较中国区域与其他区域的服务差异

2. **使用文章中提到的所有示例服务**
   - 所有示例服务（S3、DynamoDB、API Gateway、EC2、CloudFormation）在中国区域均可用
   - 可以按照文章描述的方式进行服务功能、API操作和CloudFormation资源的查询和使用

### 注意事项

1. **区域选择**
   - 使用工具时，确保选择中国区域（cn-north-1或cn-northwest-1）
   - 中国区域的服务可用性可能与全球区域有差异，建议使用该工具进行详细对比

2. **MCP Server可选功能**
   - AWS Knowledge MCP Server是可选的自动化工具，不影响核心功能使用
   - 如需使用MCP Server，建议查找最新的官方文档链接

3. **网络访问**
   - AWS Builder Center网站可以从中国正常访问
   - 建议使用稳定的网络连接以获得最佳体验

### 替代方案

无需替代方案。所有功能均可直接使用。

### 风险提示

- **服务差异性**: 中国区域的AWS服务可用性与全球区域存在差异，使用AWS Capabilities by Region工具时需要特别关注中国区域的服务列表
- **文档链接**: 部分外部链接（如MCP Server文档）可能存在访问问题，建议通过AWS官方渠道获取最新文档

### 配套资源

- **AWS Capabilities by Region工具**: https://builder.aws.com/capabilities
- **兼容性**: 完全兼容中国区域
- **修改建议**: 无需修改，可直接使用
