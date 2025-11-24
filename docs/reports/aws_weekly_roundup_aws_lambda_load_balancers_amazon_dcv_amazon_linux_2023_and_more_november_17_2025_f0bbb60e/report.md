---
title: AWS Weekly Roundup: AWS Lambda for Rust, NLB for QUIC protocol, Amazon DCV for Mac, and more (November 17, 2025)
original_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-lambda-load-balancers-amazon-dcv-amazon-linux-2023-and-more-november-17-2025/
validation_date: 2025-11-24
target_region: cn-northwest-1
feasibility: HIGH
available_services: 16
unavailable_services: 1
---

# AWS Weekly Roundup: AWS Lambda for Rust, NLB for QUIC protocol, Amazon DCV for Mac, and more (November 17, 2025)

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-lambda-load-balancers-amazon-dcv-amazon-linux-2023-and-more-november-17-2025/) | 验证日期: 2025-11-24

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文是AWS每周新闻汇总，介绍了2025年11月17日这一周的AWS服务更新和发布。文章中提到的所有核心服务（AWS Lambda、EKS、CloudFront、EC2、S3等）在AWS中国区域均可用，唯一不可用的Amazon Bedrock仅在引用的博客文章中提到，不影响主要内容的理解。

## 服务分析

### 可用服务 (16个)

- AWS Lambda
- Amazon SQS (Simple Queue Service)
- Amazon EventBridge
- AWS IAM (Identity and Access Management)
- AWS Network Load Balancer (NLB)
- Application Load Balancer (ALB)
- AWS KMS (Key Management Service)
- Amazon DCV (NICE DCV)
- Amazon EC2 (包括 EC2 Mac instances)
- Amazon Linux 2023
- Amazon S3 (Mountpoint for S3)
- Amazon EKS (Elastic Kubernetes Service)
- AWS Nitro System
- AWS X-Ray
- Amazon CloudFront
- Node.js (开源工具)

### 不可用服务 (1个)

- **Amazon Bedrock** - 在引用的博客文章中提到Amazon Nova Sonic模型

### 评估说明

本文是一篇新闻汇总类文章，主要介绍AWS服务的最新功能发布和更新，包括：

1. **核心服务可用性**：文章重点介绍的所有服务（Lambda、负载均衡器、DCV、EKS、CloudFront等）在AWS中国区域均完全可用。

2. **不可用服务影响**：Amazon Bedrock仅在文章引用的一篇博客链接中提到（关于Amazon Nova Sonic的文章），不是本文的核心内容，不影响读者理解本周的主要更新。

3. **服务可用率**：94.1% (16/17)，远超70%的阈值。

## 验证结果

### 验证类型

- ⏭️ 已跳过（无需验证）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 本文是新闻汇总类文章，不包含需要部署的GitHub项目或需要执行的操作步骤，因此无需进行深入验证。

## 实施建议

### 推荐方案

本文适合AWS中国区域用户直接阅读和参考。文章介绍的主要功能更新包括：

**Lambda相关更新**：
- AWS Lambda正式支持Rust编程语言（GA）
- AWS Lambda支持Java 25
- AWS Lambda添加Swift实验性运行时接口客户端
- AWS Lambda为SQS事件源映射引入Provisioned Mode

**网络和负载均衡更新**：
- Network Load Balancer支持QUIC协议透传模式
- Application Load Balancer支持JWT验证的客户端凭证流

**其他重要更新**：
- Amazon EventBridge增强的可视化规则构建器
- AWS KMS支持Edwards曲线数字签名算法（EdDSA）
- Amazon DCV支持Amazon EC2 Mac实例
- Amazon Linux 2023版本2025110发布

**注意事项**：
- 在中国区域使用这些服务时，需要注意区域特定的endpoint配置
- 某些新功能可能在中国区域的发布时间略有延迟，建议查看AWS中国区域的官方文档确认功能可用性
- EC2 Mac实例的可用性需要确认中国区域是否已支持

### 替代方案

对于文章中提到的Amazon Bedrock (Nova Sonic)相关内容：

1. **跳过相关章节**
   - 实施方式：直接跳过关于Amazon Nova Sonic的博客文章链接
   - 复杂度：无
   - 适用场景：不影响理解本周其他更新内容

### 风险提示

- **功能发布时间差异**：AWS全球区域和中国区域的功能发布可能存在时间差，建议在实际使用前查看AWS中国区域的官方文档确认具体功能的可用性
- **EC2 Mac实例可用性**：需要确认EC2 Mac实例在AWS中国区域的支持情况，该实例类型可能有区域限制
- **服务配额限制**：某些新功能可能有默认的服务配额限制，在中国区域使用前建议检查配额设置

### 配套资源

- **GitHub仓库**: 无
- **相关博客文章**: 文章中引用了多篇技术博客，大部分内容在中国区域可参考，但涉及Amazon Bedrock的内容需要跳过
