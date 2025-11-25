---
title: 自定义 IAM Access Analyzer 未使用访问分析的范围
publish_date: 2025-01-08
original_url: https://aws.amazon.com/blogs/security/customize-the-scope-of-iam-access-analyzer-unused-access-analysis/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 4
unavailable_services: 0
---

# 自定义 IAM Access Analyzer 未使用访问分析的范围

[📖 查看原始博客](https://aws.amazon.com/blogs/security/customize-the-scope-of-iam-access-analyzer-unused-access-analysis/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心功能在中国区不可用，无法实施

博客介绍的核心功能"未使用访问分析（Unused Access Analysis）"在AWS中国区域不可用。虽然IAM Access Analyzer服务本身可用，但其unused access分析功能及相关的配置排除规则功能均不支持。

## 服务分析

### 可用服务 (4个)

- AWS Identity and Access Management (IAM)
- AWS IAM Access Analyzer（仅基础功能）
- AWS Organizations
- AWS CLI

### 不可用服务 (0个)

无服务完全不可用，但核心功能受限。

### 评估说明

1. **IAM Access Analyzer基础服务可用**：可以在中国区域创建ACCOUNT和ORGANIZATION类型的analyzer，用于分析外部访问权限。

2. **Unused Access Analysis功能不可用**：
   - 无法创建ACCOUNT_UNUSED_ACCESS类型的analyzer
   - 无法创建ORGANIZATION_UNUSED_ACCESS类型的analyzer
   - 创建时返回错误："Unsupported analyzer type"

3. **配置排除规则功能不可用**：
   - update-analyzer操作返回"Unsupported operation"
   - 无法配置账户排除（accountIds exclusions）
   - 无法配置标签排除（resourceTags exclusions）
   - get-analyzer返回的配置中不包含configuration字段

4. **功能差异**：中国区域的IAM Access Analyzer仅支持外部访问分析（External Access），不支持未使用访问分析（Unused Access）功能。

## 验证结果

### 验证类型

- ✅ 教程步骤验证

### 执行状态

**状态**: ❌ 失败

**原因**: 核心功能在中国区域不可用

### 关键发现

1. **Unused Access Analyzer类型不支持**
   - 尝试创建ACCOUNT_UNUSED_ACCESS类型analyzer失败
   - 尝试创建ORGANIZATION_UNUSED_ACCESS类型analyzer失败
   - 错误信息：ValidationException - Unsupported analyzer type
   - 影响：无法使用博客介绍的核心功能

2. **配置排除规则API不支持**
   - update-analyzer操作在中国区域返回"Unsupported operation"
   - 无法配置博客中介绍的账户排除和标签排除功能
   - 影响：即使有unused access analyzer，也无法自定义分析范围

3. **功能限制确认**
   - 中国区域仅支持ACCOUNT和ORGANIZATION类型的analyzer
   - 这些类型仅用于外部访问分析，不包含unused access功能
   - analyzer配置中不包含configuration字段，无法设置exclusions

## 实施建议

### 推荐方案

**不建议在中国区域实施此方案**

博客介绍的所有核心功能在AWS中国区域均不可用：
- 未使用访问分析（Unused Access Analysis）
- 自定义分析范围（Exclusions配置）
- 未使用角色、凭证和权限的检测

中国区域的IAM Access Analyzer仅支持外部访问分析功能，用于识别与外部实体共享的资源。

### 替代方案

1. **使用IAM Access Analyzer的外部访问分析**
   - 实施方式：创建ACCOUNT或ORGANIZATION类型的analyzer
   - 复杂度：低
   - 适用场景：识别与外部实体共享的S3存储桶、IAM角色、KMS密钥等资源
   - 限制：无法分析未使用的权限

2. **使用IAM Access Advisor**
   - 实施方式：通过IAM控制台或API查看服务最后访问时间
   - 复杂度：中
   - 适用场景：手动识别长期未使用的权限
   - 限制：需要手动分析，无自动化排除规则

3. **自建权限使用分析方案**
   - 实施方式：使用CloudTrail日志分析IAM权限使用情况
   - 复杂度：高
   - 适用场景：需要详细的权限使用分析和自定义报告
   - 限制：需要自行开发和维护分析工具

### 风险提示

- **功能缺失风险**：中国区域无法使用unused access analysis功能，可能导致过度授权的IAM权限无法及时发现
- **合规风险**：如果组织的安全合规要求包含最小权限原则的自动化检测，需要寻找替代方案
- **运维成本**：需要使用手动方法或自建工具来实现类似功能，增加运维复杂度

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 不适用
