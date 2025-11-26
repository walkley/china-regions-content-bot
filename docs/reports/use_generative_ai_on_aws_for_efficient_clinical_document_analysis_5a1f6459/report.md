---
title: 在AWS上使用生成式AI进行高效临床文档分析
publish_date: 2025-02-05
original_url: https://aws.amazon.com/blogs/architecture/use-generative-ai-on-aws-for-efficient-clinical-document-analysis/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 10
unavailable_services: 2
---

# 在AWS上使用生成式AI进行高效临床文档分析

[📖 查看原始博客](https://aws.amazon.com/blogs/architecture/use-generative-ai-on-aws-for-efficient-clinical-document-analysis/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

该方案依赖的两个核心服务 Amazon Textract 和 Amazon Bedrock 在中国区域均不可用，这两个服务分别负责文档解析和大语言模型推理，是整个生成式AI文档分析方案的基础。缺失这些核心服务将导致方案无法按原架构实施。

## 服务分析

### 可用服务 (10个)

- Amazon Comprehend
- Amazon OpenSearch Service
- Amazon EC2
- Amazon EKS
- Amazon S3
- Amazon SageMaker
- AWS Lambda
- AWS Direct Connect
- Amazon MQ
- Amazon RDS

### 不可用服务 (2个)

- **Amazon Textract** - 核心服务
- **Amazon Bedrock** - 核心服务

### 评估说明

虽然服务可用率达到83.3%（10/12），但两个不可用服务都是方案的核心组件：

1. **Amazon Textract** - 负责从临床文档中提取文本、图像和表格，是整个文档解析流程的起点。该服务的缺失意味着需要寻找完全不同的文档解析方案。

2. **Amazon Bedrock** - 提供大语言模型推理能力，用于文档分类、信息提取和生成结构化输出。这是生成式AI方案的核心，无法简单替代。

这两个服务的缺失会导致整个架构需要从底层重新设计，包括：
- 文档解析策略的完全重构
- LLM推理服务的替换和重新集成
- AI编排引擎的重大调整

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段评估为LOW可行性，核心服务Amazon Textract和Amazon Bedrock在中国区域不可用，方案无法按原架构实施，因此跳过深入验证。

## 实施建议

### 推荐方案

不建议直接实施该方案。如需在中国区域实现类似功能，需要进行架构级别的重新设计。

### 替代方案

1. **自建文档解析服务**
   - 实施方式：使用开源OCR工具（如Tesseract、PaddleOCR）结合自定义表格识别模型，部署在Amazon EC2或Amazon EKS上
   - 复杂度：高
   - 适用场景：有足够的技术团队和时间投入，且对文档解析精度要求可以通过迭代优化达到

2. **使用SageMaker部署开源LLM**
   - 实施方式：在Amazon SageMaker上部署开源大语言模型（如Llama、ChatGLM、Qwen等），替代Amazon Bedrock
   - 复杂度：高
   - 适用场景：有GPU资源预算，技术团队具备LLM部署和优化经验

3. **混合方案**
   - 实施方式：结合自建文档解析服务和SageMaker部署的开源LLM，重新构建AI编排引擎
   - 复杂度：高
   - 适用场景：需要完整的端到端解决方案，有充足的开发资源和时间

### 风险提示

- **开发成本**: 替代方案需要大量的开发和调优工作，时间和人力成本显著高于使用托管服务
- **性能差异**: 自建服务的性能和准确度可能无法达到Amazon Textract和Amazon Bedrock的水平，需要持续优化
- **运维复杂度**: 自建服务需要团队负责模型更新、性能监控、故障处理等运维工作
- **合规性**: 医疗行业对数据处理有严格的合规要求，自建服务需要确保满足相关法规
- **成本控制**: GPU实例和大规模存储的成本可能较高，需要仔细评估和优化

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 不适用
