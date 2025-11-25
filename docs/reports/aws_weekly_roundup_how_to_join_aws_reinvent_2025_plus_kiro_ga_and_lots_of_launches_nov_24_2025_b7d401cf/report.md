---
title: AWS每周综述：如何参加AWS re:Invent 2025，以及Kiro正式发布和大量新功能上线（2025年11月24日）
publish_date: 2025-11-24
original_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-how-to-join-aws-reinvent-2025-plus-kiro-ga-and-lots-of-launches-nov-24-2025/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: MODERATE
available_services: 16
unavailable_services: 3
---

# AWS每周综述：如何参加AWS re:Invent 2025，以及Kiro正式发布和大量新功能上线（2025年11月24日）

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-how-to-join-aws-reinvent-2025-plus-kiro-ga-and-lots-of-launches-nov-24-2025/) | 验证日期: 2025-11-25

## 可行性评估

!!! warning "MODERATE - 谨慎实施"
    大部分服务可用，需要适当调整

这是一篇AWS新闻汇总类博客，主要介绍AWS re:Invent 2025活动预告、Kiro工具正式发布以及上周的多项服务更新。84.2%的提及服务在中国区可用，不可用服务仅作为功能更新列举，不影响信息获取。

## 服务分析

### 可用服务 (16个)

- Amazon EC2
- Amazon EKS
- Amazon ECS
- Amazon ECR
- Amazon Aurora DSQL
- Amazon API Gateway
- Amazon CloudWatch
- AWS CloudFormation
- AWS NAT Gateway
- Amazon OpenSearch Service
- Amazon S3
- Amazon SageMaker
- AWS Lambda
- AWS Step Functions
- AWS IAM
- AWS Billing

### 不可用服务 (3个)

- **Amazon Bedrock**
- **Amazon Connect**
- **AWS Control Tower**

### 评估说明

本文是AWS每周新闻综述，主要目的是传递AWS服务的最新动态和功能更新信息，而非提供具体的技术实施指导。文中提到的19个AWS服务中，有16个在中国区域可用，可用率达84.2%。

不可用的三个服务（Bedrock、Connect、Control Tower）在文中仅作为功能更新的列举项出现，并非文章的核心内容或实施重点。中国区用户可以：
1. 了解全球AWS服务的发展趋势
2. 关注在中国区可用服务的新功能
3. 参考技术方向进行架构规划

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 本文为新闻汇总类内容，不包含配套GitHub项目或具体操作步骤，无需进行实际部署验证。

## 实施建议

### 推荐方案

作为新闻汇总类内容，中国区用户可以：

1. **信息获取**：阅读文章了解AWS全球服务动态和技术趋势
2. **选择性关注**：重点关注在中国区可用的16个服务的新功能更新
3. **技术规划**：基于可用服务的新特性进行架构设计和优化

**具体可关注的更新**：
- Amazon EC2 P6-B300实例（需确认中国区可用性）
- Amazon EKS增强功能（Provisioned Control Plane、AI故障排查）
- Amazon ECR新功能（镜像签名、归档存储类）
- Amazon Aurora DSQL改进（查询编辑器、成本估算）
- Amazon API Gateway新特性（响应流式传输、开发者门户）
- AWS Lambda多租户隔离模式
- AWS Step Functions本地测试增强
- Amazon S3基于属性的访问控制
- VPC加密控制

### 替代方案

对于文中提到的不可用服务，中国区用户可考虑：

1. **Amazon Bedrock替代**
   - 实施方式：使用Amazon SageMaker部署开源大语言模型
   - 复杂度：中
   - 适用场景：需要生成式AI能力的应用

2. **Amazon Connect替代**
   - 实施方式：使用Amazon Chime SDK或第三方呼叫中心解决方案
   - 复杂度：中到高
   - 适用场景：需要云联络中心功能

3. **AWS Control Tower替代**
   - 实施方式：使用AWS Organizations + AWS Config + AWS CloudFormation StackSets手动构建多账户治理
   - 复杂度：高
   - 适用场景：需要多账户管理和治理

### 风险提示

- **服务可用性差异**：文中提到的某些新功能可能在中国区域有延迟上线或不可用的情况，使用前需确认
- **区域特性**：部分服务在中国区域可能有功能限制或配置差异，需查阅中国区域文档
- **合规要求**：在中国区域使用AWS服务需遵守当地法律法规和合规要求

### 配套资源

本文无配套GitHub项目或代码示例，为纯新闻资讯内容。

---

**验证说明**：本报告基于静态内容分析生成，未进行实际部署验证。建议用户在使用文中提到的服务新功能前，查阅AWS中国区域官方文档确认可用性和配置要求。
