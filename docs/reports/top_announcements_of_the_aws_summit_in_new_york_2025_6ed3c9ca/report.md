---
title: AWS Summit New York 2025 重要公告汇总
publish_date: 2025-07-16
original_url: https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2025/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 10
unavailable_services: 1
---

# AWS Summit New York 2025 重要公告汇总

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2025/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Bedrock在中国区不可用，多个重要公告无法实施

虽然91%的服务在中国区可用，但Amazon Bedrock作为多个核心公告的基础服务在中国区不可用，导致AI代理相关的关键功能无法实现。

## 服务分析

### 可用服务 (10个)

- Amazon SageMaker AI
- Amazon EC2
- Amazon S3
- Amazon S3 Metadata
- Amazon QuickSight
- Amazon EventBridge
- Amazon ECS
- Amazon EKS
- Amazon OpenSearch
- AWS Budgets

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务

### 评估说明

本博客汇总了AWS Summit New York 2025的11个重要公告，涉及11个AWS服务。经过分析：

1. **核心服务不可用**：Amazon Bedrock在中国区不可用，这直接影响了以下公告：
   - Amazon Bedrock AgentCore（首要公告）- 完全依赖Bedrock
   - Amazon S3 Vectors与Bedrock Knowledge Bases的集成功能

2. **部分功能受限**：
   - Amazon Nova模型虽然可以通过SageMaker使用，但与Bedrock的原生集成无法实现
   - S3 Vectors的独立存储功能可用，但AI应用集成受限

3. **其他公告可用**：
   - SageMaker新功能（QuickSight集成、S3非结构化数据集成）
   - EventBridge日志增强
   - ECS蓝绿部署
   - EKS超大规模支持（10万节点）
   - AWS Free Tier更新
   - TwelveLabs视频理解模型（依赖Bedrock，不可用）

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 初步可行性评估为LOW。虽然大部分服务可用，但核心服务Amazon Bedrock不可用，导致博客中最重要的AI代理相关公告无法在中国区实施，不满足深入验证的触发条件。

## 实施建议

### 推荐方案

**不建议直接实施**

本博客是公告汇总类内容，其中涉及Amazon Bedrock的公告在中国区无法实施：

**不可实施的公告：**
1. ❌ Amazon Bedrock AgentCore - 完全依赖Bedrock
2. ❌ TwelveLabs视频理解模型 - 通过Bedrock提供
3. ⚠️ Amazon S3 Vectors - 部分功能受限（与Bedrock集成不可用）

**可实施的公告：**
1. ✅ Amazon Nova在SageMaker中的定制化 - 可通过SageMaker使用
2. ✅ AWS AI League - 培训项目，需调整为中国区可用服务
3. ✅ AWS Free Tier更新 - 全球适用
4. ✅ Amazon S3 Metadata增强 - 完全可用
5. ✅ SageMaker新功能（QuickSight集成、数据集成）- 完全可用
6. ✅ Amazon EventBridge日志增强 - 完全可用
7. ✅ Amazon ECS蓝绿部署 - 完全可用
8. ✅ Amazon EKS超大规模支持 - 完全可用

### 替代方案

针对不可用的AI代理功能，可考虑以下替代方案：

1. **使用SageMaker构建AI代理**
   - 实施方式：直接使用SageMaker部署开源大语言模型（如Llama、Qwen等），结合Lambda和Step Functions构建代理逻辑
   - 复杂度：高
   - 适用场景：需要完全控制AI代理架构和模型选择的场景

2. **使用第三方AI服务**
   - 实施方式：集成国内可用的AI服务（如阿里云通义千问、百度文心一言等）与AWS服务
   - 复杂度：中
   - 适用场景：快速实现AI代理功能，但需要跨平台集成

3. **专注于非AI公告**
   - 实施方式：优先实施与Bedrock无关的公告，如ECS/EKS增强、S3新功能、EventBridge日志等
   - 复杂度：低
   - 适用场景：暂不需要AI代理功能，专注于基础设施和数据管理优化

### 风险提示

- **功能缺失风险**: Amazon Bedrock AgentCore作为首要公告，其不可用意味着无法体验AWS最新的AI代理管理能力
- **集成限制风险**: S3 Vectors虽然可用，但与Bedrock Knowledge Bases的原生集成无法实现，需要自行开发向量检索逻辑
- **学习路径差异**: AWS AI League培训项目可能包含Bedrock相关内容，在中国区需要调整学习路径
- **架构复杂度**: 使用替代方案构建AI代理的复杂度和维护成本显著高于使用Bedrock AgentCore

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 不适用
