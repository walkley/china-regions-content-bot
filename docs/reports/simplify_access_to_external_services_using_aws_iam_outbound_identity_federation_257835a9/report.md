---
title: Simplify access to external services using AWS IAM Outbound Identity Federation
original_url: https://aws.amazon.com/blogs/aws/simplify-access-to-external-services-using-aws-iam-outbound-identity-federation/
validation_date: 2025-11-24
target_region: cn-northwest-1
feasibility: HIGH
available_services: 4
unavailable_services: 0
---

# Simplify access to external services using AWS IAM Outbound Identity Federation

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/simplify-access-to-external-services-using-aws-iam-outbound-identity-federation/) | 验证日期: 2025-11-24

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

文章介绍的AWS IAM Outbound Identity Federation功能已在AWS中国区域正式发布，所有核心服务完全可用。该功能允许AWS工作负载使用短期JWT令牌安全访问外部服务，无需存储长期凭证。经过实际验证，功能在中国区域运行完全正常，与全球区域保持一致。

## 服务分析

### 可用服务 (4个)

- AWS Identity and Access Management (IAM)
- AWS Security Token Service (AWS STS)
- Amazon EC2
- AWS Lambda

### 不可用服务 (0个)

无

### 评估说明

1. **核心服务完全可用**：IAM和STS是该功能的核心服务，在中国区域完全可用且功能完整
2. **官方明确支持**：文章明确说明"AWS IAM outbound identity federation is available at no additional cost in all AWS commercial Regions, AWS GovCloud (US) Regions, and China Regions"
3. **无架构差异**：中国区域实现与全球区域保持一致，仅域名后缀不同（使用.amazonwebservices.com.cn）

## 验证结果

### 验证类型

✅ 教程步骤验证

### 执行状态

**状态**: ✅ 成功

在cn-northwest-1区域完成了完整的功能验证，所有操作步骤均成功执行，无需任何修正。

### 关键发现

1. **功能启用成功**
   - 成功启用Outbound Web Identity Federation功能
   - 获得账户特定的issuer URL：`https://<uuid>.tokens.sts.global.api.amazonwebservices.com.cn`
   - OIDC发现端点（.well-known/openid-configuration）正常工作
   - JWKS端点（.well-known/jwks.json）正常提供公钥

2. **JWT令牌生成验证**
   - ES384算法签名：✅ 成功
   - RS256算法签名：✅ 成功
   - 令牌包含标准OIDC声明（aud, sub, iss, exp, iat, jti）
   - 令牌包含AWS特定元数据（aws_account, source_region, principal_id, org_id, ou_path）
   - 自定义标签功能（request_tags）正常工作

3. **JWT令牌验证测试**
   - 使用Python PyJWT库成功验证令牌签名
   - JWKS端点可被外部服务正常访问
   - 令牌验证流程与文章描述完全一致

4. **中国区域特性**
   - Issuer URL使用`.amazonwebservices.com.cn`域名
   - ARN格式使用`arn:aws-cn`前缀
   - 功能行为与全球区域完全一致

5. **IAM权限控制**
   - `sts:GetWebIdentityToken`权限配置正常
   - 支持条件键控制（sts:SigningAlgorithm, sts:IdentityTokenAudience, sts:DurationSeconds）
   - 权限策略在中国区域完全兼容

## 实施建议

### 推荐方案

可直接按照原文实施，无需任何修改。具体步骤：

1. **启用功能**
   ```bash
   aws iam enable-outbound-web-identity-federation --region cn-northwest-1
   ```

2. **配置IAM权限**
   - 为需要生成令牌的IAM角色或用户添加`sts:GetWebIdentityToken`权限
   - 可选：使用条件键限制签名算法、受众和令牌有效期

3. **获取JWT令牌**
   ```python
   import boto3
   
   sts_client = boto3.client('sts', region_name='cn-northwest-1')
   response = sts_client.get_web_identity_token(
       Audience=['your-app'],
       SigningAlgorithm='ES384',  # 或 'RS256'
       DurationSeconds=300
   )
   jwt_token = response['WebIdentityToken']
   ```

4. **配置外部服务**
   - 将账户的issuer URL注册为可信身份提供商
   - 配置外部服务验证JWT签名（使用JWKS端点）
   - 根据JWT声明实现访问控制逻辑

### 注意事项

1. **域名差异**：中国区域的issuer URL使用`.amazonwebservices.com.cn`后缀，配置外部服务时需使用正确的URL
2. **ARN格式**：JWT中的ARN使用`arn:aws-cn`前缀，外部服务解析时需考虑这一差异
3. **网络访问**：确保外部服务可以访问OIDC发现端点和JWKS端点（公网可访问）
4. **令牌有效期**：令牌有效期为60-3600秒，建议根据实际需求设置合理的过期时间
5. **签名算法选择**：ES384提供更好的安全性和性能，RS256兼容性更广，根据外部服务支持情况选择

### 替代方案

无需替代方案，功能完全可用。

### 风险提示

- **令牌泄露风险**：虽然JWT是短期令牌，但仍需妥善保管，避免在日志或不安全渠道中暴露
- **时钟同步**：JWT验证依赖时间戳，确保系统时钟准确同步
- **JWKS缓存**：外部服务应适当缓存JWKS公钥，避免频繁请求，但需定期刷新以支持密钥轮换
- **受众验证**：外部服务必须验证JWT的`aud`声明，确保令牌是为其颁发的

### 配套资源

- **官方文档**: [Federating AWS Identities to External Services](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound.html)
- **快速入门**: [Getting Started with Outbound Identity Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_getting_started.html)
- **JWT声明参考**: [Token Claims Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_token_claims.html)
- **兼容性**: 完全兼容中国区域，无需修改
