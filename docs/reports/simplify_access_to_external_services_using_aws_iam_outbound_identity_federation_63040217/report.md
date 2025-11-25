---
title: 使用AWS IAM出站身份联合简化对外部服务的访问
publish_date: 2025-11-19
original_url: https://aws.amazon.com/blogs/aws/simplify-access-to-external-services-using-aws-iam-outbound-identity-federation/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 6
unavailable_services: 0
---

# 使用AWS IAM出站身份联合简化对外部服务的访问

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/simplify-access-to-external-services-using-aws-iam-outbound-identity-federation/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

该功能在AWS中国区域完全可用，所有涉及的服务和API均已验证通过，可以直接按照原文实施。

## 服务分析

### 可用服务 (6个)

- AWS Identity and Access Management (IAM)
- AWS Security Token Service (AWS STS)
- Amazon EC2
- AWS Lambda
- AWS CLI
- AWS SDK

### 不可用服务 (0个)

无

### 评估说明

AWS IAM Outbound Identity Federation是IAM和STS的核心功能，在中国区域完全支持。经过实际验证：

1. **核心功能完全可用**：`enable-outbound-web-identity-federation` API在中国区域正常工作
2. **OIDC端点可访问**：issuer URL使用中国区域专用域名 `amazonwebservices.com.cn`，OIDC discovery endpoints和JWKS endpoints均可正常访问
3. **Token生成和验证**：ES384和RS256两种签名算法均验证成功，token包含完整的claims信息
4. **自定义标签支持**：request tags功能正常，可用于细粒度访问控制

## 验证结果

### 验证类型

✅ 教程步骤验证

### 执行状态

**状态**: ✅ 成功

### 关键发现

1. **功能完全兼容**
   - 在cn-northwest-1区域成功启用IAM outbound identity federation
   - Issuer URL格式：`https://{uuid}.tokens.sts.global.api.amazonwebservices.com.cn`
   - 注意域名后缀为 `.com.cn`，与全球区域的 `.aws` 不同

2. **OIDC端点验证通过**
   - OpenID Configuration endpoint正常返回元数据
   - JWKS endpoint成功提供RSA和EC384公钥
   - 支持的签名算法：RS256和ES384

3. **Token生成和验证成功**
   - 使用ES384算法生成token成功
   - 使用RS256算法生成token成功
   - Python PyJWT库成功验证token签名
   - Token包含标准OIDC claims和AWS特定claims（account ID, org ID, source region等）

4. **自定义标签功能正常**
   - 通过tags参数成功添加自定义claims
   - 自定义标签出现在token的`request_tags`字段中
   - 可用于实现细粒度访问控制

5. **IAM权限控制**
   - `sts:GetWebIdentityToken`权限正常工作
   - 可通过IAM策略控制token生成权限
   - 支持条件键：`sts:SigningAlgorithm`、`sts:IdentityTokenAudience`、`sts:DurationSeconds`

## 实施建议

### 推荐方案

可直接按照原文实施，注意以下中国区域特定配置：

1. **Issuer URL域名差异**
   - 中国区域使用 `.amazonwebservices.com.cn` 后缀
   - 全球区域使用 `.api.aws` 后缀
   - 外部服务配置信任关系时需使用正确的issuer URL

2. **服务端点配置**
   - EC2服务主体：`ec2.amazonaws.com.cn`（而非`ec2.amazonaws.com`）
   - 其他服务主体也需使用 `.com.cn` 后缀

3. **ARN格式**
   - 使用 `arn:aws-cn:` 前缀（而非`arn:aws:`）
   - 示例：`arn:aws-cn:iam::ACCOUNT_ID:role/RoleName`

4. **实施步骤**
   - 在IAM控制台或使用CLI启用outbound identity federation
   - 配置IAM角色/用户的`sts:GetWebIdentityToken`权限
   - 在外部服务中注册AWS账户的issuer URL作为可信身份提供商
   - 应用程序调用`GetWebIdentityToken` API获取JWT
   - 外部服务验证JWT签名并授予访问权限

### 替代方案

无需替代方案，功能完全可用。

### 风险提示

- **Token有效期限制**：最短60秒，最长3600秒（1小时），需要应用程序实现token刷新逻辑
- **网络连通性**：外部服务需要能够访问中国区域的JWKS endpoint（`*.amazonwebservices.com.cn`）来验证token
- **时钟同步**：token验证依赖时间戳（iat、exp），确保系统时钟准确
- **Issuer URL唯一性**：每个AWS账户有唯一的issuer URL，账户间不可共享

### 配套资源

- **官方文档**：[Federating AWS Identities to External Services](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound.html)
- **Getting Started指南**：[Getting Started with Outbound Identity Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_getting_started.html)
- **兼容性**：完全兼容中国区域，无需修改
- **定价**：免费功能，无额外费用
