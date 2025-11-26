---
title: 关于CLOUD Act实际运作方式的五个事实
publish_date: 2025-07-22
original_url: https://aws.amazon.com/blogs/security/five-facts-about-how-the-cloud-act-actually-works/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 3
unavailable_services: 0
---

# 关于CLOUD Act实际运作方式的五个事实

[📖 查看原始博客](https://aws.amazon.com/blogs/security/five-facts-about-how-the-cloud-act-actually-works/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文是一篇关于美国CLOUD Act（云数据法案）的政策性和法律合规性博客文章，主要阐述AWS如何处理政府数据请求以及相关的法律保护措施。文章提到的所有AWS技术服务在中国区域均可用，内容完全适用于中国区域客户了解AWS的数据保护承诺。

## 服务分析

### 可用服务 (3个)

- Amazon EC2 (Amazon Elastic Compute Cloud)
- AWS Nitro System
- AWS KMS (AWS Key Management Service)

### 不可用服务 (0个)

无

### 评估说明

本文是一篇政策性博客，重点讨论：
1. **CLOUD Act的法律框架**：解释该法案不授予美国政府无限制或自动访问云数据的权力
2. **AWS的数据保护承诺**：自2020年以来，AWS未向美国政府披露任何存储在美国境外的企业或政府客户内容数据
3. **技术保护措施**：介绍AWS Nitro System的零操作员访问设计和AWS KMS的加密能力

文章提到的三个AWS服务（EC2、Nitro System、KMS）在中国区域均完全可用。这些服务的技术特性和安全保护措施在全球范围内保持一致，包括中国区域。

## 验证结果

### 验证类型

- ⏭️ 无需深入验证（政策性内容）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 本文为政策性和法律合规性博客，不包含需要部署的技术方案或操作步骤。文章主要讨论CLOUD Act的法律框架和AWS的数据保护政策，所有提到的技术服务在中国区域均可用。

### 关键发现

虽然无需技术验证，但以下要点值得中国区域客户关注：

1. **数据主权和法律适用性**
   - 文章讨论的CLOUD Act是美国法律，主要适用于美国司法管辖范围
   - 中国区域由光环新网（北京区域）和西云数据（宁夏区域）运营，受中国法律管辖
   - AWS中国区域的数据保护遵循中国相关法律法规

2. **技术保护措施的全球一致性**
   - AWS Nitro System的零操作员访问设计在全球所有区域保持一致
   - AWS KMS的加密能力和FIPS 140-3 Level 3认证标准全球适用
   - 这些技术保护措施为客户数据提供了强大的安全保障

## 实施建议

### 推荐方案

中国区域客户可以直接参考本文了解AWS的数据保护技术和承诺，但需注意以下几点：

1. **法律管辖差异**
   - 本文讨论的CLOUD Act适用于美国司法管辖范围
   - AWS中国区域受中国法律管辖，数据处理遵循《网络安全法》、《数据安全法》、《个人信息保护法》等中国法律法规
   - 建议客户咨询法律顾问了解中国区域的具体合规要求

2. **技术措施的应用**
   - 文章介绍的技术保护措施（Nitro System、KMS加密）在中国区域完全可用
   - 建议客户充分利用这些技术能力加强数据保护
   - 可参考AWS中国区域的合规文档了解本地化的最佳实践

3. **数据保护策略**
   - 使用AWS KMS进行数据加密，客户完全控制加密密钥
   - 利用Nitro System的零操作员访问特性保护工作负载
   - 实施最小权限原则和访问控制策略

### 替代方案

无需替代方案。本文为政策性内容，所有提到的技术服务在中国区域均可用。

### 风险提示

- **法律适用性理解**：本文主要讨论美国法律框架，中国区域客户应理解其运营环境受中国法律管辖
- **合规咨询**：对于数据保护和合规要求，建议咨询专业法律顾问以确保符合中国相关法律法规
- **区域运营差异**：AWS中国区域由本地合作伙伴运营，在服务条款和运营模式上与全球区域存在差异

### 配套资源

- **相关文档**：
  - [AWS中国区域合规性](https://www.amazonaws.cn/compliance/)
  - [AWS Nitro System技术文档](https://docs.aws.amazon.com/ec2/latest/userguide/ec2-nitro-instances.html)
  - [AWS KMS用户指南](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
  
- **GitHub仓库**：无

- **兼容性说明**：本文为政策性博客，内容适用于全球所有区域的客户了解AWS的数据保护承诺和技术能力
