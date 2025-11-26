---
title: AWS免费套餐更新：新客户可获得高达200美元积分开始探索AWS
publish_date: 2025-07-15
original_url: https://aws.amazon.com/blogs/aws/aws-free-tier-update-new-customers-can-get-started-and-explore-aws-with-up-to-200-in-credits/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 5
unavailable_services: 1
---

# AWS免费套餐更新：新客户可获得高达200美元积分开始探索AWS

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/aws-free-tier-update-new-customers-can-get-started-and-explore-aws-with-up-to-200-in-credits/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    该功能在中国区域不可用，无法实施

博客明确说明："The new AWS Free Tier features are generally available in all AWS Regions, except the AWS GovCloud (US) Regions and **the China Regions**"。这意味着整个增强版AWS免费套餐计划（包括200美元积分系统、免费账户计划、付费账户计划）在AWS中国区域均不可用。

## 服务分析

### 可用服务 (5个)

- Amazon EC2 (Amazon Elastic Compute Cloud)
- Amazon RDS (Amazon Relational Database Service)
- AWS Lambda
- AWS Budgets
- AWS Billing and Cost Management

### 不可用服务 (1个)

- **Amazon Bedrock** - 用于获取额外20美元积分的5个活动之一

### 评估说明

虽然博客中提到的大部分AWS服务（83.3%）在中国区域可用，但核心功能本身——增强版AWS免费套餐计划——在中国区域不可用。具体包括：

1. **新的免费套餐计划不可用**：包括免费账户计划和付费账户计划
2. **200美元积分系统不可用**：注册时获得100美元积分，完成活动获得额外100美元积分的机制
3. **5个服务活动不可用**：通过完成EC2、RDS、Lambda、Bedrock、Budgets活动获取积分的功能
4. **6个月免费期限制不可用**：新的免费账户计划的6个月期限和相关限制

中国区域的AWS账户仍然使用传统的免费套餐计划（Legacy Free Tier），包括短期试用、12个月试用和永久免费套餐服务。

## 验证结果

### 验证类型

- ⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 博客明确说明该功能在中国区域不可用，无需进行深入验证。

## 实施建议

### 推荐方案

**不建议在中国区域实施此方案**

该博客介绍的增强版AWS免费套餐计划在中国区域完全不可用。中国区域的AWS用户应继续使用传统的免费套餐计划。

### 替代方案

1. **使用传统AWS免费套餐**
   - 实施方式：中国区域账户自动使用传统免费套餐计划
   - 复杂度：低
   - 适用场景：所有在2025年7月15日之前创建的账户，以及中国区域的所有账户
   - 包含内容：
     - 短期试用服务
     - 12个月试用服务
     - 永久免费套餐服务（Always Free Tier）

2. **手动学习相关AWS服务**
   - 实施方式：虽然无法通过积分活动学习，但可以手动创建和配置EC2、RDS、Lambda、Budgets等服务
   - 复杂度：中
   - 适用场景：希望学习AWS服务基础知识的新用户
   - 注意事项：需要注意成本控制，建议配置AWS Budgets进行预算管理

### 风险提示

- **区域限制**：增强版免费套餐计划在中国区域不可用，这是AWS官方明确的区域限制
- **成本管理**：中国区域用户需要更加主动地管理成本，因为没有200美元积分缓冲
- **服务差异**：Amazon Bedrock在中国区域不可用，无法体验生成式AI相关功能
- **文档适用性**：针对新免费套餐的文档和教程可能不适用于中国区域

### 配套资源

- **AWS中国免费套餐页面**: https://www.amazonaws.cn/free/
- **传统免费套餐文档**: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html
- **AWS中国区域服务列表**: https://www.amazonaws.cn/en/about-aws/regional-product-services/
