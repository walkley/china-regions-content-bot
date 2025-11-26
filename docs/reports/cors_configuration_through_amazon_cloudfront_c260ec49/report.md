---
title: 通过Amazon CloudFront配置CORS
publish_date: 2025-05-16
original_url: https://aws.amazon.com/blogs/networking-and-content-delivery/cors-configuration-through-amazon-cloudfront/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 4
unavailable_services: 0
---

# 通过Amazon CloudFront配置CORS

[📖 查看原始博客](https://aws.amazon.com/blogs/networking-and-content-delivery/cors-configuration-through-amazon-cloudfront/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

文章介绍的所有AWS服务（CloudFront、Lambda@Edge、CloudFront Functions、S3）在AWS中国区域均完全可用，可以直接按照原文实施CORS配置方案。

## 服务分析

### 可用服务 (4个)

- Amazon CloudFront
- Lambda@Edge
- CloudFront Functions
- Amazon S3

### 不可用服务 (0个)

无

### 评估说明

本文介绍了在Amazon CloudFront中配置跨域资源共享（CORS）的三种方法：

1. **响应头策略（Response Header Policies）** - CloudFront原生功能，无需编写代码
2. **CloudFront Functions/Lambda@Edge** - 边缘函数，支持条件逻辑和动态CORS处理
3. **源站CORS处理** - 在S3或自定义源站配置CORS

所有涉及的服务在中国区域均可用，包括：
- CloudFront的响应头策略功能完全支持
- Lambda@Edge在中国区域可正常使用
- CloudFront Functions在中国区域可正常使用
- S3的CORS配置功能完全支持

文章提供的示例代码和配置方法可直接应用于中国区域，无需任何修改。

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 文章为概念性介绍和配置方法说明，不包含需要逐步执行的完整部署教程。所有涉及的服务在中国区域均可用，可行性评估为HIGH，无需进行实际部署验证。

## 实施建议

### 推荐方案

可直接按照原文实施，文章介绍的三种CORS配置方法均适用于AWS中国区域：

**方法一：响应头策略（推荐用于简单场景）**
- 适用场景：简单CORS需求或预检请求（OPTIONS）
- 优势：无需编写代码，免费，配置简单
- 实施方式：在CloudFront控制台或通过API配置响应头策略
- 注意事项：
  - 可使用AWS托管策略：SimpleCORS 或 CORS-With-Preflight
  - 如需自定义策略，可创建自己的响应头策略

**方法二：CloudFront Functions/Lambda@Edge（推荐用于复杂场景）**
- 适用场景：需要条件逻辑或动态CORS处理
- 优势：灵活性高，可实现复杂的CORS规则
- 实施方式：
  - CloudFront Functions：在viewer-request事件处理OPTIONS请求
  - Lambda@Edge：在origin-response事件处理错误场景的CORS头
- 注意事项：
  - CloudFront Functions和Lambda@Edge会产生额外费用
  - 需要评估成本效益

**方法三：源站CORS处理**
- 适用场景：需要细粒度控制或多CDN架构
- 优势：统一的CORS策略，跨多个CDN一致
- 实施方式：在S3桶或自定义源站配置CORS
- 注意事项：
  - 需要通过缓存策略或源请求策略转发特定头部
  - S3源站：转发Origin、Access-Control-Request-Headers、Access-Control-Request-Method
  - 自定义源站：根据需求转发相应头部
  - 注意缓存一致性问题，建议使用CloudFront Function添加Origin头部

### 配置差异说明

AWS中国区域与全球区域在CloudFront CORS配置方面**无差异**，以下功能均完全支持：

- ✅ 响应头策略（Response Header Policies）
- ✅ AWS托管策略（SimpleCORS、CORS-With-Preflight）
- ✅ 自定义响应头策略
- ✅ CloudFront Functions
- ✅ Lambda@Edge
- ✅ S3 CORS配置
- ✅ 缓存策略和源请求策略

### 最佳实践建议

1. **优先使用响应头策略**：对于大多数标准CORS需求，响应头策略是最简单且免费的方案

2. **处理OPTIONS请求**：如果需要在边缘直接响应OPTIONS请求以降低延迟，使用CloudFront Functions

3. **错误场景处理**：当源站出错时需要返回CORS头，使用Lambda@Edge的origin-response事件

4. **缓存优化**：
   - 使用源请求策略转发必要的CORS头部
   - 避免使用CachingOptimized策略与CORS结合，可能导致缓存不一致
   - 考虑使用CloudFront Function确保每个请求都包含Origin头部

5. **成本考虑**：评估边缘函数的成本效益，响应头策略免费但功能有限，边缘函数灵活但有额外费用

### 风险提示

- **缓存一致性问题**：如果在源站配置CORS并启用缓存，首个不含Origin头的请求可能导致后续请求无法获得正确的CORS响应头。建议使用CloudFront Function确保所有请求都包含Origin头部。

- **成本管理**：Lambda@Edge和CloudFront Functions会产生额外费用，需要根据请求量评估成本。

- **配置复杂度**：多种CORS配置方法可能导致配置冲突，建议选择一种主要方法并保持配置一致性。

### 配套资源

- **GitHub仓库**: 无专门配套仓库
- **示例代码**: 文章中提供了CloudFront Function示例代码，可直接在中国区域使用
- **官方文档**: 
  - [CloudFront响应头策略](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/understanding-response-headers-policies.html)
  - [CloudFront Functions示例](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/example-function-add-cors-header-response.html)
  - [Lambda@Edge](https://aws.amazon.com/lambda/edge/)
