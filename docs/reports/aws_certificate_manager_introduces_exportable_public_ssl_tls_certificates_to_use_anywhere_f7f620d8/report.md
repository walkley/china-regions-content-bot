---
title: AWS Certificate Manager推出可导出的公共SSL/TLS证书
publish_date: 2025-06-17
original_url: https://aws.amazon.com/blogs/aws/aws-certificate-manager-introduces-exportable-public-ssl-tls-certificates-to-use-anywhere/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 8
unavailable_services: 0
---

# AWS Certificate Manager推出可导出的公共SSL/TLS证书

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/aws-certificate-manager-introduces-exportable-public-ssl-tls-certificates-to-use-anywhere/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心功能在中国区域不可用，无法实施

虽然所有相关AWS服务在中国区域均可用，但博客介绍的核心功能"可导出公共证书"在中国区域被明确禁用，无法实现文章描述的主要用例。

## 服务分析

### 可用服务 (8个)

- AWS Certificate Manager (ACM)
- Elastic Load Balancing (ELB)
- Amazon CloudFront
- Amazon API Gateway
- Amazon EC2
- AWS CLI
- AWS IAM
- Amazon EventBridge

### 不可用服务 (0个)

无

### 评估说明

所有提到的AWS服务在中国区域均可用，但这并不意味着功能完全一致。经过实际验证发现：

1. **核心功能缺失**：ACM的"可导出公共证书"功能在中国区域被明确禁用
2. **API限制**：虽然`export-certificate` API存在，但执行时返回错误："Accounts managed by Amazon or AWS are disallowed from exporting public certificates"
3. **参数限制**：`request-certificate`命令的`Export=ENABLED`选项在中国区域无法使用
4. **功能差异**：中国区域ACM仅支持传统的非导出证书功能

## 验证结果

### 验证类型

- ✅ 教程步骤验证

### 执行状态

**状态**: ❌ 失败

**详细说明**: 在cn-northwest-1区域尝试执行博客中的核心操作时遇到功能限制

### 关键发现

1. **可导出公共证书功能不可用**
   - 尝试使用`Export=ENABLED`参数请求证书时，系统返回ValidationException错误
   - 错误信息："Accounts managed by Amazon or AWS are disallowed from exporting public certificates"
   - 这表明该功能在中国区域被明确禁用，不是临时性问题

2. **API存在但功能受限**
   - `export-certificate` CLI命令在中国区域存在
   - 命令帮助文档显示支持导出私有和公共证书
   - 但实际执行时会被区域策略拦截

3. **账户配置无相关选项**
   - `get-account-configuration` API返回的配置中不包含Export相关设置
   - 无法通过账户级别配置启用此功能

4. **传统ACM功能正常**
   - 可以正常请求非导出的公共证书
   - 证书可用于ELB、CloudFront、API Gateway等集成服务
   - DNS验证流程正常工作

## 实施建议

### 推荐方案

**不建议在中国区域实施此方案**

博客介绍的核心价值是"导出公共证书并在任意位置使用"，这一功能在中国区域完全不可用。虽然ACM服务本身可用，但无法实现文章描述的主要用例。

### 替代方案

1. **使用第三方证书颁发机构**
   - 实施方式：从Let's Encrypt、DigiCert等第三方CA获取证书，然后导入到ACM
   - 复杂度：中
   - 适用场景：需要在EC2实例、容器或本地主机上使用证书
   - 注意事项：需要自行管理证书续期流程

2. **使用ACM私有证书颁发机构**
   - 实施方式：创建ACM Private CA，签发私有证书并导出使用
   - 复杂度：高
   - 适用场景：内部应用、私有网络环境
   - 注意事项：私有证书不被公共浏览器信任，仅适用于内部系统

3. **继续使用ACM非导出证书**
   - 实施方式：使用传统ACM证书，仅部署到ELB、CloudFront、API Gateway
   - 复杂度：低
   - 适用场景：证书仅用于AWS托管服务
   - 注意事项：无法在EC2实例或容器中直接使用

### 风险提示

- **功能差异风险**：中国区域与全球区域在ACM功能上存在显著差异，迁移或复制架构时需特别注意
- **文档不一致**：AWS CLI帮助文档显示支持导出公共证书，但实际功能被禁用，可能导致误解
- **成本考虑**：如采用第三方CA方案，需要额外的证书购买成本
- **运维复杂度**：使用第三方证书需要建立独立的证书管理和续期流程

### 配套资源

- **GitHub仓库**: 无
- **相关文档**: [ACM用户指南](https://docs.amazonaws.cn/acm/latest/userguide/)
- **建议**: 在中国区域使用ACM时，建议参考中国区域专用文档，避免依赖全球区域的新功能
