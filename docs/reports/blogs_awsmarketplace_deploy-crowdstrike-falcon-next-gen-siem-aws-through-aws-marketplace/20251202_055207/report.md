---
title: 通过AWS Marketplace部署CrowdStrike Falcon下一代SIEM
publish_date: 2025-12-01
original_url: https://aws.amazon.com/blogs/awsmarketplace/deploy-crowdstrike-falcon-next-gen-siem-aws-through-aws-marketplace/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 6
unavailable_services: 4
---

# 通过AWS Marketplace部署CrowdStrike Falcon下一代SIEM

[📖 查看原始博客](https://aws.amazon.com/blogs/awsmarketplace/deploy-crowdstrike-falcon-next-gen-siem-aws-through-aws-marketplace/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

本方案严重依赖AWS Marketplace作为部署入口，同时需要AWS Organizations、Amazon GuardDuty和AWS Security Hub等多个在中国区域不可用的核心服务。整个自动化部署流程无法在中国区域实现。

## 服务分析

### 可用服务 (6个)

- AWS IAM
- AWS CloudFormation
- AWS CloudTrail
- Amazon EventBridge
- Amazon SNS
- Amazon SQS

### 不可用服务 (4个)

- **AWS Marketplace** - 核心服务（部署入口）
- **AWS Organizations** - 核心服务（多账户管理）
- **Amazon GuardDuty** - 核心服务（威胁检测数据源）
- **AWS Security Hub** - 核心服务（安全发现聚合）

### 评估说明

1. **AWS Marketplace不可用**：这是整个方案的部署入口，中国区域无法通过AWS Marketplace订阅和部署第三方SaaS产品。这是最根本的阻碍。

2. **AWS Organizations不可用**：方案设计用于跨AWS Organizations中的所有账户部署，中国区域不支持AWS Organizations的多账户统一管理功能。

3. **核心安全服务缺失**：Amazon GuardDuty和AWS Security Hub是方案的主要数据源，用于提供威胁检测和安全发现。这两个服务在中国区域均不可用，导致SIEM系统失去关键的安全数据输入。

4. **第三方SaaS限制**：CrowdStrike Falcon Next-Gen SIEM是托管在AWS全球区域的SaaS服务，其与中国区域的网络连接和数据传输可能面临合规性和性能问题。

## 验证结果

### 验证类型

⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务AWS Marketplace、AWS Organizations、Amazon GuardDuty和AWS Security Hub在中国区域均不可用，方案无法实施，跳过深入验证以节约时间和资源。

## 实施建议

### 推荐方案

**不建议在中国区域实施此方案**，原因如下：

1. **部署入口不可用**：AWS Marketplace在中国区域不可用，无法通过原文描述的自动化流程订阅和部署CrowdStrike产品。

2. **架构基础缺失**：方案依赖AWS Organizations进行多账户管理，中国区域需要使用独立账户管理方式。

3. **数据源缺失**：Amazon GuardDuty和AWS Security Hub是SIEM的核心数据源，这两个服务的缺失使得SIEM系统失去主要价值。

4. **跨境数据传输**：即使能够部署，将中国区域的安全日志发送到全球区域的CrowdStrike SaaS平台可能涉及数据合规性问题。

### 替代方案

#### 方案1：使用中国区域可用的SIEM解决方案

- **实施方式**：
  - 选择在中国区域可用的SIEM产品（如Splunk、IBM QRadar等自建方案）
  - 使用AWS CloudTrail作为主要日志源
  - 通过Amazon EventBridge、SNS、SQS构建日志收集管道
  - 在Amazon EC2上部署SIEM分析平台
  
- **复杂度**：高
- **适用场景**：需要完整SIEM功能且必须在中国区域运行的场景

#### 方案2：直接联系CrowdStrike中国团队

- **实施方式**：
  - 联系CrowdStrike在中国的合作伙伴或销售团队
  - 了解是否有针对中国区域的特殊部署方案
  - 可能需要通过非AWS Marketplace渠道部署
  
- **复杂度**：中
- **适用场景**：企业已有CrowdStrike产品使用经验，希望保持技术栈一致性

#### 方案3：构建自定义安全监控方案

- **实施方式**：
  - 使用AWS CloudTrail + Amazon CloudWatch Logs进行日志收集
  - 使用Amazon OpenSearch Service进行日志分析和可视化
  - 使用AWS Lambda进行自动化响应
  - 集成第三方威胁情报源
  
- **复杂度**：中
- **适用场景**：预算有限，需要灵活定制的安全监控方案

### 风险提示

- **合规性风险**：跨境数据传输可能违反中国数据安全法规，特别是涉及敏感安全日志时
- **网络性能**：中国区域与全球区域的网络延迟可能影响实时安全监控效果
- **服务限制**：中国区域缺少多个核心安全服务，安全监控能力受限
- **供应商支持**：第三方SaaS供应商对中国区域的支持可能有限
- **成本考虑**：自建SIEM方案的初期投入和运维成本较高

### 配套资源

- **GitHub仓库**: 无
- **官方文档**: [CrowdStrike Falcon for AWS](https://www.crowdstrike.com/en-us/platform/next-gen-siem/)
- **建议**: 如需在中国区域实施类似方案，建议直接联系CrowdStrike中国团队咨询专门的部署选项
