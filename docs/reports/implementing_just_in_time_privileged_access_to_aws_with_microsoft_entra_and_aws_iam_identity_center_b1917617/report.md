---
title: 使用Microsoft Entra和AWS IAM Identity Center实现AWS即时特权访问
publish_date: 2025-06-03
original_url: https://aws.amazon.com/blogs/security/implementing-just-in-time-privileged-access-to-aws-with-microsoft-entra-and-aws-iam-identity-center/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 4
unavailable_services: 0
---

# 使用Microsoft Entra和AWS IAM Identity Center实现AWS即时特权访问

[📖 查看原始博客](https://aws.amazon.com/blogs/security/implementing-just-in-time-privileged-access-to-aws-with-microsoft-entra-and-aws-iam-identity-center/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

该方案在AWS中国区域完全可行。所有涉及的AWS服务（IAM Identity Center、IAM、Organizations、EC2）均在中国区域可用，且核心功能已通过实际验证。

## 服务分析

### 可用服务 (4个)

- AWS IAM Identity Center (AWS Single Sign-On)
- AWS IAM (Identity and Access Management)
- AWS Organizations
- Amazon EC2

### 不可用服务 (0个)

无

### 评估说明

本方案的核心是通过Microsoft Entra ID（前身为Azure AD）的Privileged Identity Management (PIM)功能与AWS IAM Identity Center集成，实现即时特权访问管理。所有涉及的AWS服务在中国区域均完全可用：

1. **AWS IAM Identity Center**：核心服务，支持SAML 2.0和SCIM协议，可与外部身份提供商集成
2. **AWS Organizations**：提供多账户管理能力，支持IAM Identity Center的组织级部署
3. **AWS IAM**：提供托管策略（如AmazonEC2FullAccess）用于权限集配置
4. **Amazon EC2**：作为示例服务展示权限管理

该方案的关键依赖是Microsoft Entra ID（外部SaaS服务），不受AWS区域限制。SAML和SCIM是标准协议，在中国区域的IAM Identity Center中完全支持。

## 验证结果

### 验证类型

✅ 教程步骤验证

### 执行状态

**状态**: ✅ 成功

### 关键发现

1. **IAM Identity Center完全可用**
   - 在cn-northwest-1区域成功验证IAM Identity Center实例
   - 权限集创建、策略附加、删除等核心功能正常
   - 支持自定义会话持续时间（测试使用1小时）
   - Identity Store服务可用，支持用户和组管理

2. **AWS Organizations集成正常**
   - Organizations服务在中国区域完全可用
   - 支持多账户管理和IAM Identity Center的组织级部署
   - 账户列表和组织描述功能正常

3. **AWS托管策略可用**
   - AmazonEC2FullAccess等AWS托管策略在中国区域可用
   - ARN格式使用`arn:aws-cn`前缀（中国区域特定格式）
   - 策略附加到权限集功能正常

4. **SAML/SCIM协议支持**
   - IAM Identity Center支持SAML 2.0身份联合
   - 支持SCIM 2.0协议进行用户和组自动同步
   - 可与Microsoft Entra ID等外部IdP集成

5. **区域特定配置**
   - 资源ARN使用`arn:aws-cn`前缀
   - IAM Identity Center实例ARN格式：`arn:aws-cn:sso:::instance/ssoins-*`
   - 权限集ARN格式：`arn:aws-cn:sso:::permissionSet/ssoins-*/ps-*`

## 实施建议

### 推荐方案

可直接按照原文实施，但需注意以下中国区域特定配置：

**配置注意事项**：

1. **ARN格式差异**
   - 中国区域使用`arn:aws-cn`前缀，而非`arn:aws`
   - 在配置SAML断言和API调用时需使用正确的ARN格式

2. **IAM Identity Center访问门户**
   - 中国区域的访问门户URL格式可能略有不同
   - 确保用户可以访问中国区域的AWS服务端点

3. **Microsoft Entra ID连接**
   - Microsoft Entra ID是全球SaaS服务，需确保网络连接稳定
   - SAML和SCIM端点需要能够访问AWS中国区域的IAM Identity Center端点

4. **会话持续时间配置**
   - AWS访问门户会话：默认8小时（可配置15分钟至7天）
   - 权限集会话：默认1小时（可配置1-12小时）
   - Entra PIM激活持续时间：默认8小时（可配置30分钟至24小时）
   - 需要综合考虑这三个时间设置，实际访问窗口可能长达3小时

5. **同步延迟**
   - Entra ID到IAM Identity Center的同步通常在2-10分钟内完成
   - 在高负载情况下可能回退到40分钟的标准间隔
   - 用户激活后需等待同步完成才能看到权限集

### 实施步骤摘要

1. **前置条件准备**
   - 启用AWS Organizations和IAM Identity Center
   - 准备Azure订阅和Entra ID P1/P2许可证
   - 配置Entra ID作为IAM Identity Center的外部IdP（SAML + SCIM）

2. **创建安全组**
   - 在Entra ID中创建安全组（如"AWS - Amazon EC2 Admin"）
   - 将组分配给IAM Identity Center企业应用
   - 启用自动同步

3. **配置IAM Identity Center**
   - 创建权限集（如EC2AdminAccess）
   - 附加AWS托管策略或自定义策略
   - 将权限集分配给Entra ID安全组和目标AWS账户

4. **启用Entra PIM**
   - 为安全组启用PIM管理
   - 配置成员角色设置（激活持续时间、MFA、审批流程等）
   - 添加符合条件的用户

5. **测试验证**
   - 用户通过My Apps门户激活组成员资格
   - 等待同步完成（2-10分钟）
   - 访问IAM Identity Center门户验证权限集可见性
   - 验证会话过期和权限撤销

### 替代方案

无需替代方案。该解决方案在中国区域可直接实施。

如果不使用Microsoft Entra ID，可以考虑以下替代方案：

1. **使用其他SAML 2.0兼容IdP**
   - 实施方式：使用Okta、OneLogin等支持SAML和SCIM的IdP
   - 复杂度：中
   - 适用场景：已有其他IdP基础设施的组织

2. **使用IAM Identity Center内置目录**
   - 实施方式：直接在IAM Identity Center中管理用户和组，结合AWS Lambda实现临时访问
   - 复杂度：高
   - 适用场景：不需要与外部IdP集成的小型组织

### 风险提示

- **网络连接性**：Microsoft Entra ID是全球服务，需确保从中国区域到Azure服务的网络连接稳定可靠
- **同步延迟**：Entra PIM组成员变更到IAM Identity Center的同步可能需要2-10分钟，在高负载时可能延长至40分钟
- **会话管理复杂性**：需要理解三层会话持续时间（AWS访问门户、权限集、Entra PIM激活）的交互关系，避免意外的访问延长
- **许可证要求**：需要Entra ID P1或P2许可证才能使用PIM功能
- **审计日志**：确保同时启用Entra ID和AWS CloudTrail的审计日志，以获得完整的访问审计轨迹
- **MFA配置**：建议在Entra PIM中强制要求MFA，增强安全性

### 配套资源

- **GitHub仓库**：无
- **相关文档**：
  - [AWS IAM Identity Center文档](https://docs.amazonaws.cn/singlesignon/latest/userguide/what-is.html)
  - [Microsoft Entra PIM文档](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure)
  - [配置SAML和SCIM与Microsoft Entra ID](https://docs.aws.amazon.com/singlesignon/latest/userguide/idp-microsoft-entra.html)
