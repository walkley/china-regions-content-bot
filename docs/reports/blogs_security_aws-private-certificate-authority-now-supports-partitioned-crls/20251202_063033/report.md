---
title: AWS Private Certificate Authority 现已支持分区 CRL
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/security/aws-private-certificate-authority-now-supports-partitioned-crls/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: HIGH
available_services: 2
unavailable_services: 0
---

# AWS Private Certificate Authority 现已支持分区 CRL

[📖 查看原始博客](https://aws.amazon.com/blogs/security/aws-private-certificate-authority-now-supports-partitioned-crls/) | 验证日期: 2025-12-02

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

文章介绍的AWS Private CA分区CRL功能在中国区域完全可用，所有涉及的服务和配置步骤均可在cn-northwest-1和cn-north-1区域直接实施。

## 服务分析

### 可用服务 (2个)

- **AWS Private Certificate Authority (AWS Private CA)** - 核心服务，用于创建和管理证书颁发机构
- **Amazon S3** - 用于存储CRL文件

### 不可用服务 (0个)

无

### 评估说明

本文涉及的两个核心服务AWS Private CA和Amazon S3在中国区域（cn-northwest-1和cn-north-1）均完全可用。通过API调用验证，AWS Private CA服务在cn-northwest-1区域响应正常，S3服务也可正常访问。

文章介绍的分区CRL功能是AWS Private CA的原生功能，不依赖任何中国区域不可用的服务。该功能通过将证书吊销列表分区来支持每个CA最多1亿个证书的颁发和吊销，解决了传统完整CRL在大规模场景下的限制。

## 验证结果

### 验证类型

⏭️ 已跳过（配置教程，可行性等级为HIGH）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 文章为服务配置教程，所有涉及服务在中国区域完全可用，无需进行实际部署验证。配置步骤通过AWS管理控制台完成，操作流程在中国区域与全球区域一致。

## 实施建议

### 推荐方案

可直接按照原文实施，配置步骤完全适用于中国区域。

**实施步骤**：
1. 在AWS Private CA控制台选择现有CA或创建新CA
2. 进入"撤销配置"标签页
3. 启用CRL分发并配置S3存储桶
4. 在CRL设置中勾选"启用分区"选项
5. 保存更改后，CA的证书限制将自动从100万提升至1亿

**注意事项**：
- 确保S3存储桶已禁用BPA（Block Public Access）中的相关设置
- 需要为S3存储桶手动附加适当的访问策略，参考AWS文档中的策略模板
- 分区CRL功能无额外费用，仅收取AWS Private CA和S3的标准费用
- 中国区域的ARN格式为`arn:aws-cn:s3:::bucket-name`，与全球区域略有不同

**区域差异**：
- 中国区域使用独立的AWS账户体系和控制台（console.amazonaws.cn）
- S3存储桶的ARN前缀为`arn:aws-cn`而非`arn:aws`
- 其他配置选项和功能特性与全球区域完全一致

### 替代方案

无需替代方案，原方案可直接实施。

### 风险提示

- **S3存储桶策略配置**: 必须正确配置S3存储桶策略以允许AWS Private CA写入CRL文件，否则CRL生成将失败
- **现有证书兼容性**: 启用分区CRL后，新颁发的证书将包含IDP扩展并绑定到特定分区，现有证书不受影响但仍使用完整CRL
- **应用程序兼容性**: 虽然分区CRL保持1MB大小限制以确保兼容性，但建议在生产环境部署前测试关键应用程序的证书验证功能
- **合规性要求**: 如果您的组织有特定的PKI合规要求，建议在启用分区CRL前确认该功能符合相关标准（功能符合RFC5280、WebTrust和ETSI TSP标准）

### 配套资源

- **AWS Private CA 用户指南**: https://docs.aws.amazon.com/privateca/latest/userguide/
- **CRL规划文档**: https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html
- **S3访问策略示例**: https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies
- **中国区域控制台**: https://console.amazonaws.cn/acm-pca/
