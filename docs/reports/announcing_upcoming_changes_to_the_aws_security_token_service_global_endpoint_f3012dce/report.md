---
title: AWS Security Token Service 全局端点即将变更公告
publish_date: 2025-01-27
original_url: https://aws.amazon.com/blogs/security/announcing-upcoming-changes-to-the-aws-security-token-service-global-endpoint/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 3
unavailable_services: 0
---

# AWS Security Token Service 全局端点即将变更公告

[📖 查看原始博客](https://aws.amazon.com/blogs/security/announcing-upcoming-changes-to-the-aws-security-token-service-global-endpoint/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

该博客为AWS STS服务端变更公告，所有涉及的服务在AWS中国区域均可用，内容完全适用于中国区域客户。

## 服务分析

### 可用服务 (3个)

- AWS Security Token Service (STS)
- AWS CloudTrail
- Amazon VPC

### 不可用服务 (0个)

无

### 评估说明

本博客公告了AWS STS全局端点的重要变更，所有涉及的服务在AWS中国区域均完全可用：

1. **核心服务可用性**：AWS STS是核心服务，在中国区域完全支持，包括全局端点和区域端点
2. **配套服务支持**：CloudTrail日志服务和VPC网络服务在中国区域均可正常使用
3. **变更适用性**：虽然博客提到变更将在"默认启用的区域"推出，但STS的区域端点建议同样适用于中国区域

## 验证结果

### 验证类型

- ⏭️ 无需验证（公告性质内容）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 该博客为AWS服务端变更公告，不包含需要客户侧部署或操作的内容，无需进行实际验证。

## 实施建议

### 推荐方案

可直接参考博客内容，建议如下：

1. **使用区域端点**：在中国区域部署应用时，建议使用STS区域端点而非全局端点
   - 宁夏区域：`https://sts.cn-northwest-1.amazonaws.com.cn`
   - 北京区域：`https://sts.cn-north-1.amazonaws.com.cn`

2. **配置SDK**：如使用AWS SDK，可通过配置启用区域化STS端点：
   - 环境变量：`AWS_STS_REGIONAL_ENDPOINTS=regional`
   - SDK配置文件设置

3. **监控CloudTrail日志**：关注STS调用的CloudTrail日志，确认使用的端点类型

### 注意事项

- **端点域名差异**：中国区域使用`.amazonaws.com.cn`域名后缀，而非`.amazonaws.com`
- **全局端点行为**：中国区域的STS全局端点行为可能与标准区域有所不同，建议直接使用区域端点
- **IAM条件键**：使用`aws:RequestedRegion`等条件键时，需注意中国区域的特殊性

### 风险提示

- **网络连通性**：确保应用可以访问中国区域的STS端点
- **DNS解析**：在VPC内使用Amazon DNS服务器以获得最佳性能
- **配额管理**：区域端点和全局端点有独立的请求配额

### 配套资源

- **相关文档**: [AWS STS 区域化端点](https://docs.amazonaws.cn/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html)
- **最佳实践**: [如何使用区域化 AWS STS 端点](https://aws.amazon.com/cn/blogs/china/how-to-use-regional-aws-sts-endpoints/)
