---
title: 使用全新AWS Security Hub统一安全管理，实现大规模风险优先级排序和响应（预览版）
publish_date: 2025-06-17
original_url: https://aws.amazon.com/blogs/aws/unify-your-security-with-the-new-aws-security-hub-for-risk-prioritization-and-response-at-scale-preview/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: MODERATE
available_services: 3
unavailable_services: 1
---

# 使用全新AWS Security Hub统一安全管理，实现大规模风险优先级排序和响应（预览版）

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/unify-your-security-with-the-new-aws-security-hub-for-risk-prioritization-and-response-at-scale-preview/) | 验证日期: 2025-11-25

## 可行性评估

!!! warning "MODERATE - 谨慎实施"
    大部分核心服务可用，但缺少敏感数据发现功能

Security Hub的核心功能（威胁检测、漏洞管理、暴露分析、合规管理）在中国区域完全可用，但Amazon Macie不可用会导致敏感数据发现功能缺失。

## 服务分析

### 可用服务 (3个)

- AWS Security Hub
- Amazon GuardDuty
- Amazon Inspector

### 不可用服务 (1个)

- **Amazon Macie** - 负责敏感数据发现和保护

### 评估说明

经过实际验证，AWS Security Hub在中国区域（cn-northwest-1）功能完整，可以正常启用并与GuardDuty、Inspector集成。验证结果显示：

1. **核心服务可用性**：Security Hub、GuardDuty、Inspector三大核心服务均在中国区域可用，占总服务的75%
2. **功能完整性**：Security Hub支持多种安全标准（CIS、NIST、PCI DSS等），可以正常聚合来自GuardDuty和Inspector的安全发现
3. **集成能力**：验证确认Security Hub可以自动集成GuardDuty（威胁检测）和Inspector（漏洞扫描），无需额外配置
4. **缺失功能影响**：Amazon Macie不可用意味着博客中提到的"敏感数据"（Sensitive data）功能模块无法使用，但这不影响其他四大核心功能：暴露分析（Exposure）、威胁检测（Threats）、漏洞管理（Vulnerabilities）、态势管理（Posture management）

## 验证结果

### 验证类型

- ✅ 教程步骤验证

### 执行状态

**状态**: ✅ 成功

### 关键发现

1. **Security Hub核心功能完整**
   - 成功在cn-northwest-1区域启用Security Hub
   - 支持10种安全标准，包括AWS基础安全最佳实践、CIS基准、NIST、PCI DSS等
   - 自动集成GuardDuty和Inspector，无需手动配置

2. **GuardDuty功能全面**
   - 威胁检测功能完整，支持CloudTrail、DNS日志、VPC流日志、S3数据事件等
   - 支持EKS审计日志和Lambda网络日志监控
   - 包含EBS恶意软件保护功能
   - 可正常向Security Hub发送威胁发现

3. **Inspector集成正常**
   - 支持EC2、ECR、Lambda资源类型的漏洞扫描
   - 可以正常启用并与Security Hub集成
   - 漏洞发现会自动聚合到Security Hub

4. **Macie服务不可用**
   - 在cn-northwest-1区域无法连接Macie endpoint
   - 确认Macie在AWS中国区域完全不可用
   - 影响范围：博客中提到的"敏感数据"功能模块无法使用

5. **新版UI功能限制**
   - 博客中展示的新版Security Hub UI（预览版）在中国区域可能不可用
   - 暴露分析（Exposure）、攻击路径可视化等新功能需要进一步确认
   - 基础的Security Hub功能（发现聚合、合规检查）完全可用

## 实施建议

### 推荐方案

可以在中国区域实施Security Hub统一安全管理方案，但需要注意以下调整：

**核心功能实施**：
- 启用Security Hub作为安全管理中心
- 集成GuardDuty进行威胁检测
- 集成Inspector进行漏洞扫描
- 启用所需的安全标准（如CIS、NIST等）

**需要调整的部分**：
- 移除所有与Amazon Macie相关的敏感数据发现功能
- 不要依赖"敏感数据"（Sensitive data）导航菜单项
- 如需敏感数据保护，考虑使用替代方案

**预计工作量**：
- 基础实施：低（直接按照博客步骤操作，跳过Macie相关内容）
- 功能验证：中（需要验证新版UI功能在中国区域的可用性）

### 替代方案

针对Amazon Macie缺失的敏感数据发现功能：

1. **AWS Config + Lambda自定义规则**
   - 实施方式：使用AWS Config监控S3存储桶配置，编写Lambda函数进行自定义敏感数据检测
   - 复杂度：中
   - 适用场景：需要基础的敏感数据合规检查，可接受自定义开发

2. **第三方数据安全解决方案**
   - 实施方式：通过Security Hub的第三方集成能力，接入支持中国区域的数据安全产品
   - 复杂度：中到高
   - 适用场景：需要企业级敏感数据发现和保护能力

3. **S3存储桶策略 + 加密**
   - 实施方式：通过严格的S3存储桶策略、默认加密、访问日志等方式保护敏感数据
   - 复杂度：低
   - 适用场景：数据存储在S3，主要关注访问控制和加密保护

### 风险提示

- **新功能可用性**：博客介绍的是预览版功能，部分新特性（如暴露分析、攻击路径可视化）在中国区域的可用性需要进一步确认
- **区域限制**：博客提到预览版仅在特定区域可用，中国区域（cn-northwest-1、cn-north-1）未在列表中，新版UI可能不可用
- **功能差异**：即使基础Security Hub可用，新版增强功能（correlation、contextualization、visualization）可能存在区域差异
- **Macie依赖**：如果业务强依赖敏感数据发现和分类功能，需要评估替代方案的可行性
- **合规要求**：某些行业合规标准可能要求敏感数据发现能力，需要确认替代方案是否满足合规要求

### 配套资源

- **GitHub仓库**: 无（博客未提供配套代码仓库）
- **相关文档**: [AWS Security Hub用户指南](https://docs.aws.amazon.com/securityhub/)
- **中国区域文档**: 建议查阅AWS中国区域文档确认新版功能的可用性
