---
title: 如何使用AWS License Manager配置基于用户订阅许可证的Microsoft远程桌面服务
publish_date: 2025-01-27
original_url: https://aws.amazon.com/blogs/modernizing-with-aws/how-to-configure-microsoft-remote-desktop-services-using-user-based-subscription-licenses-with-aws-license-manager/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 4
unavailable_services: 1
---

# 如何使用AWS License Manager配置基于用户订阅许可证的Microsoft远程桌面服务

[📖 查看原始博客](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-configure-microsoft-remote-desktop-services-using-user-based-subscription-licenses-with-aws-license-manager/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务AWS License Manager User-based Subscriptions在中国区域不可用，无法实现用户订阅许可证管理功能

博客的核心功能依赖于AWS License Manager的User-based Subscriptions特性，该服务在AWS中国区域（cn-north-1和cn-northwest-1）均不可用，导致整个解决方案无法在中国区域实施。

## 服务分析

### 可用服务 (4个)

- Amazon EC2
- AWS Secrets Manager
- AWS Directory Service (AWS Managed Microsoft AD)
- AWS Marketplace (部分功能)

### 不可用服务 (1个)

- **AWS License Manager User-based Subscriptions** - 核心服务

### 评估说明

1. **核心服务不可用**：AWS License Manager User-based Subscriptions是本解决方案的核心服务，负责管理Microsoft RDS的用户订阅许可证。该服务在中国区域的endpoint无法访问（https://license-manager-user-subscriptions.cn-northwest-1.amazonaws.com.cn 和 cn-north-1均不可用）。

2. **功能完全依赖**：博客中描述的所有关键步骤都依赖于User-based Subscriptions服务：
   - 订阅Remote Desktop Services SAL
   - 注册Active Directory
   - 配置RDS License Server
   - 订阅用户
   - 管理许可证

3. **无直接替代方案**：虽然基础服务（EC2、Directory Service、Secrets Manager）都可用，但缺少User-based Subscriptions服务意味着无法通过AWS提供的托管方式获取和管理Microsoft RDS用户订阅许可证。

4. **AWS Marketplace限制**：即使Marketplace服务端点可访问，但Remote Desktop Services SAL产品在中国区Marketplace中不可用。

## 验证结果

### 验证类型

- ⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务AWS License Manager User-based Subscriptions在中国区域不可用，无法执行教程步骤验证。通过API调用确认服务endpoint在cn-northwest-1和cn-north-1区域均无法连接。

### 关键发现

1. **服务端点不可用**
   - 测试区域：cn-northwest-1, cn-north-1
   - 错误信息：Could not connect to the endpoint URL
   - 影响：无法访问User-based Subscriptions的任何功能

2. **基础服务正常**
   - EC2、Secrets Manager、Directory Service在中国区域均可正常使用
   - 但这些服务无法弥补核心许可证管理服务的缺失

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此解决方案**

由于核心服务不可用，该博客描述的AWS托管RDS许可证方案无法在中国区域实现。

### 替代方案

1. **传统BYOL模式**
   - 实施方式：使用自建的RD Licensing服务器，通过BYOL模式管理Microsoft RDS许可证
   - 复杂度：中
   - 适用场景：已有Microsoft Software Assurance或RDS CAL许可证的企业
   - 注意事项：需要自行管理许可证服务器基础设施，无法享受AWS托管服务的便利性

2. **使用Windows Server自带的2个免费管理连接**
   - 实施方式：如果只需要少量远程连接（≤2个并发会话），可以使用Windows Server自带的免费RDP连接
   - 复杂度：低
   - 适用场景：小规模管理需求，不需要多用户并发访问
   - 限制：仅限管理用途，无法支持生产环境的多用户场景

3. **考虑其他远程访问方案**
   - 实施方式：评估使用AWS Systems Manager Session Manager、AWS Client VPN等替代远程访问方案
   - 复杂度：中到高
   - 适用场景：不强制要求使用Windows RDS的场景
   - 注意事项：需要重新设计访问架构，可能无法满足特定的Windows GUI应用需求

### 风险提示

- **许可证合规性**：如果选择BYOL模式，必须确保符合Microsoft的许可证条款，特别是在云环境中使用RDS许可证的相关规定
- **管理复杂度**：自建RD Licensing服务器需要额外的运维工作，包括服务器维护、许可证跟踪、故障排除等
- **成本考虑**：BYOL模式可能需要前期购买许可证，与AWS托管的按需付费模式相比，成本结构完全不同
- **功能限制**：中国区域无法使用AWS提供的Visual Studio和Microsoft Office用户订阅许可证功能

### 配套资源

- **GitHub仓库**: 无
- **相关文档**: 
  - [Microsoft RDS角色配置文档](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-roles)
  - [AWS Directory Service用户指南](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/)
