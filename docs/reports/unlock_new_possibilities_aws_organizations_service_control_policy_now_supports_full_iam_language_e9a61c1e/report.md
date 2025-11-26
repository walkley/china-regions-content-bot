---
title: 解锁新可能：AWS Organizations服务控制策略现已支持完整IAM语言
publish_date: 2025-09-19
original_url: https://aws.amazon.com/blogs/security/unlock-new-possibilities-aws-organizations-service-control-policy-now-supports-full-iam-language/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 10
unavailable_services: 1
---

# 解锁新可能：AWS Organizations服务控制策略现已支持完整IAM语言

[📖 查看原始博客](https://aws.amazon.com/blogs/security/unlock-new-possibilities-aws-organizations-service-control-policy-now-supports-full-iam-language/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文介绍的AWS Organizations服务控制策略（SCP）增强功能完全适用于AWS中国区域。核心服务AWS Organizations和IAM在中国区域完全可用，文章中的策略语法和最佳实践可以直接应用。

## 服务分析

### 可用服务 (10个)

- AWS Organizations
- AWS IAM (Identity and Access Management)
- IAM Access Analyzer
- Amazon S3
- Amazon EC2
- Amazon RDS
- AWS Lambda
- AWS CloudFormation
- Amazon CloudWatch
- Amazon VPC

### 不可用服务 (1个)

- **Amazon Bedrock**

### 评估说明

1. **核心服务完全可用**：文章的核心主题是AWS Organizations的SCP功能增强，该服务在中国区域完全可用且功能一致。

2. **不可用服务影响极小**：Amazon Bedrock仅在示例2中作为策略编写的演示案例出现，用于说明如何使用`NotResource`元素限制对特定模型的访问。这个示例的目的是展示策略语法，而非实际部署Bedrock服务。

3. **策略语法通用性**：文章介绍的所有SCP语法增强（`NotResource`、`NotAction`、条件语句、通配符等）都是IAM策略语言的标准特性，适用于所有AWS服务和区域。

4. **替代示例可用**：如需在中国区域演示相同的策略模式，可以使用其他可用服务（如S3、EC2、RDS等）替换Bedrock示例，策略逻辑完全相同。

## 验证结果

### 验证类型

- ⏭️ 无需深入验证（内容为概念性介绍和策略语法说明）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 本文为AWS Organizations SCP功能的概念性介绍和策略语法说明，不包含需要部署的GitHub项目或具体操作步骤。文章重点在于策略语言的语法增强和最佳实践，这些内容在中国区域完全适用。

## 实施建议

### 推荐方案

可直接按照原文实施，文章中介绍的所有SCP语法增强功能在AWS中国区域完全支持。

**实施要点：**

1. **策略语法完全兼容**：所有新支持的SCP元素（`NotResource`、`NotAction`、`Condition`、通配符等）在中国区域与全球区域保持一致。

2. **示例策略可直接使用**：
   - 示例1（资源边界控制）：可直接应用于S3等服务
   - 示例2（Bedrock模型限制）：虽然Bedrock不可用，但策略模式可应用于其他服务
   - 示例3（区域限制）：可直接使用，只需调整为中国区域代码（`cn-north-1`、`cn-northwest-1`）

3. **IAM Access Analyzer验证**：中国区域支持IAM Access Analyzer，可用于验证SCP策略的正确性和安全性。

4. **区域代码调整**：在使用区域限制策略时，将示例中的全球区域代码替换为中国区域代码：
   - `us-east-1` → `cn-north-1`（北京）
   - `us-west-2` → `cn-northwest-1`（宁夏）

### 注意事项

1. **组织ID格式一致**：AWS Organizations的组织ID格式在中国区域与全球区域相同（`o-xxxxxxxxxx`）。

2. **服务端点差异**：虽然策略语法相同，但在策略中引用服务端点时，需注意中国区域使用`.cn`域名（如`s3.cn-northwest-1.amazonaws.com.cn`）。

3. **Bedrock示例替代**：如需演示类似的资源限制策略，可使用以下中国区域可用的服务：
   - Amazon S3（限制特定存储桶访问）
   - Amazon EC2（限制特定实例类型）
   - Amazon RDS（限制特定数据库引擎）

### 最佳实践建议

1. **优先使用Deny语句**：遵循文章建议，使用显式的`Deny`语句而非依赖隐式拒绝，确保策略独立且可强制执行。

2. **谨慎使用通配符**：在`Action`元素中使用通配符时要特别小心，因为AWS新增的操作会自动匹配现有通配符模式。

3. **策略验证流程**：在应用SCP之前，使用IAM Access Analyzer进行策略验证，确保符合安全最佳实践。

4. **渐进式部署**：建议先在测试组织单元（OU）中应用新策略，验证无误后再推广到生产环境。

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/data-perimeter-policy-examples
- **兼容性**: 该仓库中的策略示例可在中国区域使用，但需注意：
  - 将区域代码调整为中国区域
  - 跳过涉及不可用服务的示例
  - 服务拥有的资源列表可能因区域而异，需根据实际情况调整
- **修改建议**: 
  - 将示例中的全球区域代码替换为`cn-north-1`或`cn-northwest-1`
  - 移除或替换涉及Amazon Bedrock的策略示例
  - 验证服务拥有资源的ARN格式是否与中国区域一致
