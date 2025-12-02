---
title: 加州大学洛杉矶分校使用AWS生成式AI服务打造沉浸式剧场体验
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/machine-learning/university-of-california-los-angeles-delivers-an-immersive-theater-experience-with-aws-generative-ai-services/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 11
unavailable_services: 3
---

# 加州大学洛杉矶分校使用AWS生成式AI服务打造沉浸式剧场体验

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/university-of-california-los-angeles-delivers-an-immersive-theater-experience-with-aws-generative-ai-services/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心生成式AI服务在中国区不可用，架构需要重大修改才能实施

本方案的核心依赖Amazon Bedrock及其托管的多个基础模型（Anthropic Claude、Amazon Nova、Stable Diffusion），这些服务目前在AWS中国区域均不可用。虽然大部分基础设施服务可用，但缺少关键的生成式AI能力使得原方案无法直接实施。

## 服务分析

### 可用服务 (11个)

- Amazon SageMaker AI
- AWS Lambda
- Amazon SQS
- Amazon SNS
- Amazon DynamoDB
- Amazon S3
- Amazon EFS
- Amazon EC2 (G5实例系列，可替代G6)
- AWS CodeBuild
- Amazon CloudWatch
- AWS CloudFormation
- Amazon EKS
- Amazon EventBridge

### 不可用服务 (3个)

- **Amazon Bedrock** - 核心服务
- **Anthropic Claude 3.5 Sonnet** - 核心模型
- **Amazon Nova Canvas** - 核心模型
- **EC2 G6实例类型** - 可用G5系列替代

### 评估说明

文章方案严重依赖Amazon Bedrock提供的托管基础模型服务，特别是：

1. **Anthropic Claude 3.5 Sonnet**：用于生成用户草图和参考图像的文本描述
2. **Amazon Nova Canvas**：用于从低分辨率图像快速生成高质量2048x512像素图像
3. **Stable Diffusion 3.5 (Bedrock托管版本)**：用于图像生成和增强

这些服务在AWS中国区域完全不可用。虽然Amazon SageMaker AI可用且文章中也使用了自托管的HuggingFace模型，但Bedrock的缺失意味着需要重新设计整个AI工作流程。

GPU实例方面，文章使用的G6系列（g6.4xlarge和g6.12xlarge）在中国区不可用，但可以使用G5系列（g5.2xlarge、g5.4xlarge等）作为替代，这些实例配备NVIDIA A10G GPU，性能相近。

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 可行性评估为LOW，核心生成式AI服务Amazon Bedrock在中国区域不可用，无法进行实际部署验证。根据验证流程，统一输出跳过验证以节约时间。

## 实施建议

### 推荐方案

**不建议直接实施原方案**，但可以考虑以下替代路径：

**方案A：完全基于SageMaker AI的自托管方案**
- 将所有AI模型部署到Amazon SageMaker AI端点
- 使用开源替代模型：
  - 用Qwen-VL或LLaVA替代Claude 3.5 Sonnet进行视觉理解
  - 用开源Stable Diffusion XL或SD3.5替代Nova Canvas
  - 保留文章中已使用的HuggingFace模型
- 复杂度：高
- 预计额外工作量：需要重新设计AI工作流程，增加模型部署和调优工作

**方案B：混合架构**
- 基础设施层使用AWS中国区域服务（Lambda、SQS、S3等）
- AI推理层使用海外区域的Bedrock服务（需考虑网络延迟和合规性）
- 复杂度：中
- 适用场景：对延迟要求不严格且符合数据合规要求的场景

### 替代方案

1. **开源模型完全替代方案**
   - 实施方式：
     - 视觉理解：部署Qwen2-VL-7B或LLaVA-1.6到SageMaker
     - 图像生成：部署SDXL Turbo或SD3.5-Large到SageMaker
     - 图像增强：使用Real-ESRGAN或CodeFormer
   - 复杂度：高
   - 适用场景：需要完全在中国区域部署的场景
   - 挑战：需要自行管理模型版本、优化推理性能、实现内容安全过滤

2. **简化AI工作流方案**
   - 实施方式：
     - 减少AI处理步骤，直接使用单一模型完成任务
     - 使用ControlNet + SDXL的组合替代多模型流水线
     - 预处理和后处理在Lambda中完成
   - 复杂度：中
   - 适用场景：对输出质量要求可以适当降低的场景

### 风险提示

- **性能风险**：开源模型的推理速度和质量可能无法达到Bedrock托管模型的水平，影响用户体验（文章要求2分钟内完成往返）
- **成本风险**：自托管大型模型需要持续运行GPU实例，成本可能显著高于按需使用的Bedrock服务
- **维护负担**：需要自行管理模型更新、安全补丁、性能优化等工作
- **合规风险**：如采用混合架构，需确保数据跨境传输符合相关法规要求
- **GPU配额限制**：G5实例在中国区域可能有配额限制，需提前申请足够的实例配额以支持24个端点的部署需求

### 配套资源

- **GitHub仓库**：文章未提供配套代码仓库
- **兼容性**：N/A
- **修改建议**：如要在中国区实施，建议：
  1. 创建模型选择抽象层，支持灵活切换不同的视觉理解和图像生成模型
  2. 实现模型性能基准测试框架，对比不同开源模型的效果
  3. 建立模型版本管理和A/B测试机制
  4. 增加内容安全检测模块（如NSFW检测、敏感内容过滤）
  5. 优化SageMaker端点的自动扩缩容策略以控制成本
