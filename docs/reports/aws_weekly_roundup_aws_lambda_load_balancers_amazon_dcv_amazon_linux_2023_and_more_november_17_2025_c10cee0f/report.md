---
title: AWS每周综述：AWS Lambda支持Rust、网络负载均衡器支持QUIC协议、Amazon DCV支持Mac等（2025年11月17日）
publish_date: 2025-11-17
original_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-lambda-load-balancers-amazon-dcv-amazon-linux-2023-and-more-november-17-2025/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 15
unavailable_services: 1
---

# AWS每周综述：AWS Lambda支持Rust、网络负载均衡器支持QUIC协议、Amazon DCV支持Mac等（2025年11月17日）

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-lambda-load-balancers-amazon-dcv-amazon-linux-2023-and-more-november-17-2025/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

这是一篇AWS每周新闻汇总博客，介绍了多项服务更新。所有提及的核心服务在AWS中国区域均可用，仅有一个非核心服务（Amazon Bedrock）不可用。

## 服务分析

### 可用服务 (15个)

- AWS Lambda
- Amazon EventBridge
- Amazon SQS (Simple Queue Service)
- AWS Network Load Balancer (NLB)
- Application Load Balancer (ALB)
- AWS KMS (Key Management Service)
- Amazon DCV (NICE DCV)
- Amazon EC2 (Mac instances)
- Amazon Linux 2023
- Amazon S3 (Mountpoint for S3)
- Amazon EKS (Elastic Kubernetes Service)
- AWS Nitro System
- AWS X-Ray
- Amazon CloudFront
- OpenTelemetry

### 不可用服务 (1个)

- **Amazon Bedrock** - 仅在一篇引用的博客文章中提及（Amazon Nova Sonic模型），非本文核心内容

### 评估说明

本文是AWS每周新闻汇总，涵盖了多个服务的更新公告：

1. **核心服务可用性**：所有主要介绍的服务（Lambda、负载均衡器、DCV、EKS等）在中国区域均可用
2. **不可用服务影响**：Amazon Bedrock仅在一个引用的博客链接中提及，不影响本文的整体价值
3. **内容类型**：这是新闻汇总类文章，不包含需要部署的项目或操作步骤，主要用于了解AWS服务的最新动态

主要更新包括：
- AWS Lambda支持Rust、Java 25和Swift运行时
- Lambda新增SQS事件源映射的预配置模式
- EventBridge增强的可视化规则构建器
- 网络负载均衡器支持QUIC协议透传模式
- 应用负载均衡器支持JWT验证
- KMS支持EdDSA加密算法
- DCV支持EC2 Mac实例
- Amazon Linux 2023新版本发布

## 验证结果

### 验证类型

- ⏭️ 已跳过（无需验证）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 这是一篇新闻汇总博客，不包含配套的GitHub项目或具体的操作步骤，无需进行深入验证。文章主要用于了解AWS服务的最新功能更新和公告。

## 实施建议

### 推荐方案

可直接阅读和参考本文内容，了解AWS服务的最新动态。

**关注要点**：
- **Lambda运行时更新**：Rust、Java 25和Swift的支持在中国区域同样适用
- **负载均衡器新功能**：NLB的QUIC协议支持和ALB的JWT验证功能可在中国区域使用
- **区域差异**：部分功能可能在中国区域的发布时间略有延迟，建议查看中国区域的"新功能"页面确认具体可用性
- **文档参考**：文章中引用的技术博客和文档大部分可以直接参考，但涉及Amazon Bedrock的内容需要寻找替代方案

### 替代方案

针对不可用的Amazon Bedrock (Amazon Nova Sonic)：

1. **语音识别替代方案**
   - 实施方式：使用第三方语音服务（如科大讯飞、阿里云语音服务）结合AWS Lambda进行集成
   - 复杂度：中
   - 适用场景：需要在中国区域实现语音交互功能的应用

2. **自建语音模型**
   - 实施方式：在Amazon SageMaker上部署开源语音模型（如Whisper）
   - 复杂度：高
   - 适用场景：对数据隐私有严格要求，需要完全自主控制的场景

### 风险提示

- **功能发布时间差**：某些新功能可能在全球区域和中国区域之间存在发布时间差，使用前请确认具体可用性
- **文档链接**：部分外部链接可能在中国网络环境下访问受限
- **服务配额**：某些服务在中国区域的默认配额可能与全球区域不同

### 配套资源

- **GitHub仓库**: 无（新闻汇总文章）
- **相关文档**: 
  - AWS中国区域服务列表：https://www.amazonaws.cn/en/about-aws/regional-product-services/
  - AWS中国区域新功能：https://www.amazonaws.cn/new/
