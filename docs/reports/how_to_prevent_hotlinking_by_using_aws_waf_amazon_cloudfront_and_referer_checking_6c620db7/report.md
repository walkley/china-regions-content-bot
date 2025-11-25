---
title: 如何使用Referer检查、AWS WAF和Amazon CloudFront防止盗链
publish_date: 2025-04-17
original_url: https://aws.amazon.com/blogs/security/how-to-prevent-hotlinking-by-using-aws-waf-amazon-cloudfront-and-referer-checking/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 4
unavailable_services: 0
---

# 如何使用Referer检查、AWS WAF和Amazon CloudFront防止盗链

[📖 查看原始博客](https://aws.amazon.com/blogs/security/how-to-prevent-hotlinking-by-using-aws-waf-amazon-cloudfront-and-referer-checking/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    虽然所有服务在中国区可用，但存在关键架构限制导致博客方案无法直接实施

博客中描述的AWS WAF与CloudFront集成方案在AWS中国区域存在架构限制，无法按照原文步骤实施。

## 服务分析

### 可用服务 (4个)

- AWS WAF (WAFv2)
- Amazon CloudFront
- Amazon S3
- Amazon CloudWatch

### 不可用服务 (0个)

无

### 评估说明

虽然所有提到的AWS服务在中国区域均可用，但在实际验证过程中发现了关键的架构限制：

1. **WAF Scope限制**：AWS中国区域的CloudFront仅支持全局scope（CLOUDFRONT）的WAF Web ACL，但中国区域只能创建区域scope（REGIONAL）的WAF Web ACL。尝试将REGIONAL scope的WAF关联到CloudFront时会报错："Only global scoped ARNs are supported"。

2. **跨区域限制**：全局scope的WAF需要在us-east-1区域创建，但中国区域的AWS凭证无法在全球区域使用，导致无法创建适用于CloudFront的WAF配置。

3. **CloudFront Functions不可用**：作为替代方案的CloudFront Functions在中国区域不支持，调用时返回"This operation is not supported in this region"错误。

4. **Lambda@Edge限制**：Lambda@Edge需要在us-east-1创建并与CloudFront关联，在中国区域同样存在跨区域限制。

这些架构差异使得博客中描述的防盗链方案无法在中国区域按原文实施。

## 验证结果

### 验证类型

✅ 教程步骤验证

### 执行状态

**状态**: ❌ 失败

**原因**: 遇到中国区域特有的架构限制，核心功能无法实现

### 关键发现

1. **WAF与CloudFront集成限制**
   - 中国区域CloudFront要求使用全局scope的WAF Web ACL
   - 中国区域只能创建REGIONAL scope的WAF Web ACL
   - 无法将REGIONAL WAF关联到CloudFront分配
   - 错误信息：`InvalidWebACLId: Only global scoped ARNs are supported`

2. **CloudFront Functions不支持**
   - 尝试创建CloudFront Function时失败
   - 错误信息：`UnsupportedOperation: This operation is not supported in this region`
   - 无法使用边缘函数实现Referer检查逻辑

3. **跨区域服务限制**
   - 中国区域与全球区域账号体系隔离
   - 无法在us-east-1创建全局WAF资源
   - Lambda@Edge同样受跨区域限制影响

4. **基础服务可用性良好**
   - CloudFront、S3、WAF服务本身运行正常
   - 成功创建了CloudFront分配和S3源
   - 成功创建了REGIONAL scope的WAF Web ACL
   - 问题在于服务间的集成架构差异

## 实施建议

### 推荐方案

**不建议直接实施博客方案**

由于中国区域的架构限制，博客中描述的AWS WAF + CloudFront防盗链方案无法直接实施。建议考虑以下替代方案。

### 替代方案

1. **源服务器级别的Referer检查**
   - 实施方式：在源服务器（如Nginx、Apache）配置Referer验证规则
   - 复杂度：低
   - 适用场景：适合不使用CDN或可以接受源服务器处理所有请求的场景
   - 限制：无法利用CloudFront的边缘缓存优势，所有请求都会到达源服务器

2. **S3预签名URL**
   - 实施方式：使用S3预签名URL提供临时访问权限，通过应用层控制访问
   - 复杂度：中
   - 适用场景：适合需要精细访问控制的场景
   - 优势：可以设置过期时间，提供更强的安全性
   - 限制：需要修改应用逻辑生成预签名URL

3. **CloudFront签名URL/签名Cookie**
   - 实施方式：使用CloudFront的签名URL或签名Cookie功能限制内容访问
   - 复杂度：中
   - 适用场景：适合需要在CDN层面控制访问的场景
   - 优势：可以利用CloudFront的边缘缓存，同时提供访问控制
   - 限制：需要应用层生成签名，无法基于Referer自动判断

4. **应用层防盗链逻辑**
   - 实施方式：在应用服务器实现Referer检查，结合CloudFront自定义源头
   - 复杂度：中到高
   - 适用场景：需要复杂业务逻辑判断的场景
   - 优势：灵活性高，可以实现复杂的访问控制策略
   - 限制：增加应用复杂度，需要处理缓存失效问题

### 风险提示

- **架构差异风险**：中国区域与全球区域在服务集成方面存在差异，迁移方案时需要充分测试
- **功能限制风险**：CloudFront Functions、Lambda@Edge等边缘计算功能在中国区域不可用或受限
- **跨区域隔离**：中国区域与全球区域账号体系完全隔离，无法使用需要全球区域资源的服务
- **替代方案权衡**：所有替代方案都需要在安全性、性能、复杂度之间做出权衡
- **成本考虑**：源服务器级别的验证会增加源服务器负载和带宽成本

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 不适用

### 后续清理

验证过程中创建的CloudFront分配（E2Q868WP2SXDKZ）已禁用但尚未删除，需要等待状态传播完成后手动删除：

```bash
# 等待CloudFront分配状态变为Deployed后执行
aws cloudfront delete-distribution \
  --id E2Q868WP2SXDKZ \
  --if-match <当前ETag> \
  --profile cn \
  --region cn-northwest-1
```

其他测试资源（S3存储桶、WAF Web ACL）已成功清理。
