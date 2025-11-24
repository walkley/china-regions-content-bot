---
title: AWS Weekly Roundup: OpenAI partnership, Jane Goodall Institute research archive, and more (November 10, 2025)
original_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-s3-amazon-ec2-and-more-november-10-2025/
validation_date: 2025-11-24
target_region: cn-northwest-1
feasibility: MODERATE
available_services: 10
unavailable_services: 1
---

# AWS Weekly Roundup: OpenAI partnership, Jane Goodall Institute research archive, and more (November 10, 2025)

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-amazon-s3-amazon-ec2-and-more-november-10-2025/) | 验证日期: 2025-11-24

## 可行性评估

!!! warning "MODERATE - 谨慎实施"
    大部分服务可用，需要适当调整

本文是AWS新闻综述类文章，介绍了多项服务更新和合作伙伴关系。90.9%的提及服务在中国区可用，仅Amazon Bedrock不可用，但不影响核心技术内容的理解和应用。

## 服务分析

### 可用服务 (10个)

- Amazon SageMaker
- Amazon S3 Tables
- Amazon EC2
- EC2 Auto Scaling
- AWS IAM
- AWS Billing and Cost Management
- AWS Nitro System
- AWS CloudFormation
- Amazon Bedrock AgentCore Runtime
- AWS Knowledge MCP server

### 不可用服务 (1个)

- **Amazon Bedrock**

### 评估说明

本文主要介绍了以下几个方面的内容：

1. **AWS与OpenAI合作伙伴关系** - 涉及EC2 UltraServers和NVIDIA GPU基础设施，这些计算资源在中国区可用
2. **Jane Goodall Institute研究档案数字化项目** - 提到使用Amazon Bedrock和Amazon SageMaker，其中Bedrock在中国区不可用，但这仅是新闻报道内容，不影响读者理解
3. **上周的服务发布**：
   - S3 Tables标签支持 - 完全可用
   - EC2 R8a内存优化实例 - 完全可用
   - EC2 Auto Scaling warm pools混合实例策略支持 - 完全可用
   - Amazon Bedrock AgentCore Runtime直接代码部署 - 可用
   - AWS Capabilities by Region工具 - 完全可用

核心技术更新（S3、EC2、Auto Scaling等）都在中国区可用。Amazon Bedrock仅在Jane Goodall Institute项目的新闻报道中提及，不是技术实施的核心内容。

## 验证结果

### 验证类型

- ⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 本文为AWS新闻综述类文章，不包含需要验证的GitHub项目或具体操作步骤。文章主要介绍服务更新公告、合作伙伴关系和即将举行的活动，属于信息发布性质。

## 实施建议

### 推荐方案

本文作为新闻综述类内容，中国区用户可以正常阅读和了解AWS的最新动态。对于文中提到的具体服务更新：

**可直接使用的功能：**
- **S3 Tables标签功能** - 可直接在中国区使用，用于ABAC访问控制和成本分配
- **EC2 R8a实例** - 如果在中国区可用，可直接使用这些内存优化实例
- **EC2 Auto Scaling warm pools混合实例策略** - 可直接配置使用
- **AWS Capabilities by Region工具** - 可用于规划中国区的服务部署

**需要注意的内容：**
- Jane Goodall Institute项目中提到的Amazon Bedrock在中国区不可用，如需类似功能可考虑使用Amazon SageMaker部署自定义模型

### 替代方案

对于Amazon Bedrock不可用的情况：

1. **Amazon SageMaker + 开源LLM**
   - 实施方式：在SageMaker上部署开源大语言模型（如Llama、ChatGLM等）
   - 复杂度：中
   - 适用场景：需要在中国区实现类似Bedrock的生成式AI功能

2. **第三方AI服务**
   - 实施方式：集成国内AI服务提供商的API
   - 复杂度：低
   - 适用场景：快速实现AI功能，不需要完全在AWS环境内运行

### 风险提示

- **区域可用性**: 文中提到的某些新实例类型（如EC2 R8a）可能尚未在中国区域发布，使用前需确认区域可用性
- **功能时间差**: 全球区域的新功能通常会晚于中国区发布，建议通过AWS中国官网确认具体功能的上线时间
- **Bedrock依赖**: 如果未来需要实施类似Jane Goodall Institute的AI项目，需要提前规划替代方案

### 配套资源

本文为新闻综述，不包含配套的GitHub项目或代码示例。

---

**验证总结**: 本文作为AWS Weekly Roundup新闻综述，90.9%的服务在中国区可用。文章主要价值在于了解AWS最新动态和服务更新，中国区用户可以正常阅读。对于具体的技术实施，建议参考各服务的官方文档并确认中国区的可用性。
