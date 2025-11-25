---
title: 使用Amazon Q CLI和MCP构建AWS架构图
publish_date: 2025-06-30
original_url: https://aws.amazon.com/blogs/machine-learning/build-aws-architecture-diagrams-using-amazon-q-cli-and-mcp/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 26
unavailable_services: 3
---

# 使用Amazon Q CLI和MCP构建AWS架构图

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/build-aws-architecture-diagrams-using-amazon-q-cli-and-mcp/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

核心工具Amazon Q Developer CLI在中国区域不可用，这是整个解决方案的基础，导致方案无法在中国区域实施。

## 服务分析

### 可用服务 (26个)

- Amazon EC2
- Amazon S3
- Amazon VPC
- Amazon RDS
- Application Load Balancer (ELB)
- Amazon ECS
- AWS Fargate
- Amazon Aurora
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- Amazon Cognito
- Amazon CloudFront
- Amazon Kinesis Data Streams
- Amazon Data Firehose
- Amazon SQS
- AWS Glue
- Amazon Athena
- Amazon QuickSight
- Amazon ElastiCache
- Amazon SNS
- Amazon Route 53
- AWS WAF
- AWS Secrets Manager
- Amazon CloudWatch
- Amazon SageMaker

### 不可用服务 (3个)

- **Amazon Q Developer** - 核心服务
- **Amazon Textract** - IDP示例中的核心服务
- **Amazon Comprehend** - IDP示例中的辅助服务

### 评估说明

虽然文章中提到的大部分AWS服务（89.7%）在中国区域可用，但核心工具Amazon Q Developer CLI不可用，这是致命的限制：

1. **核心依赖不可用**：Amazon Q Developer CLI是整个解决方案的基础，所有功能都依赖于它，包括：
   - MCP服务器的集成和使用
   - 通过自然语言生成架构图
   - 与AWS Diagram MCP和AWS Documentation MCP的交互

2. **无替代方案**：Amazon Q Developer是AWS专有的生成式AI工具，在中国区域没有直接的替代服务

3. **示例服务缺失**：智能文档处理（IDP）示例中的Amazon Textract也不可用，进一步限制了方案的完整性

## 验证结果

### 验证类型

⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证结果为LOW，核心服务Amazon Q Developer CLI在中国区域不可用，无法进行实际部署验证。

## 实施建议

### 推荐方案

**不建议直接实施**

由于核心工具Amazon Q Developer CLI在中国区域不可用，该方案无法在中国区域实施。建议考虑以下替代方案：

### 替代方案

1. **使用传统架构图工具**
   - 实施方式：使用draw.io、Lucidchart、Microsoft Visio等传统工具手动创建AWS架构图
   - 复杂度：低
   - 适用场景：需要创建标准AWS架构图，但不需要AI辅助生成功能

2. **使用Python Diagrams库**
   - 实施方式：直接使用开源的Python diagrams库编写代码生成架构图，无需Amazon Q CLI
   - 复杂度：中
   - 适用场景：有Python编程能力，希望通过代码自动化生成架构图

3. **使用AWS CloudFormation Designer**
   - 实施方式：利用CloudFormation Designer可视化工具查看和设计基础设施
   - 复杂度：低
   - 适用场景：已有CloudFormation模板，需要可视化展示架构

4. **使用第三方AI工具**
   - 实施方式：探索其他支持中国区域的AI辅助架构图工具（如Claude Desktop + MCP，但需要API访问）
   - 复杂度：中到高
   - 适用场景：需要AI辅助功能，愿意探索非AWS原生解决方案

### 风险提示

- **功能缺失**：无法使用文章中介绍的核心功能（AI驱动的自然语言架构图生成）
- **学习成本**：替代方案需要学习不同的工具和工作流程
- **维护负担**：传统工具需要手动维护架构图，无法享受AI自动化的便利
- **最佳实践验证**：无法使用AWS Documentation MCP自动验证架构是否符合AWS最佳实践

### 配套资源

- **GitHub仓库**: https://github.com/awslabs/mcp
- **兼容性**: 不兼容中国区域，因为依赖Amazon Q Developer CLI
- **修改建议**: 无法通过简单修改使其在中国区域工作，需要完全不同的实现方案
