---
title: Myriad Genetics如何使用AWS开源生成式AI智能文档处理加速器实现快速、准确且经济高效的文档处理
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/machine-learning/how-myriad-genetics-achieved-fast-accurate-and-cost-efficient-document-processing-using-the-aws-open-source-generative-ai-intelligent-document-processing-accelerator/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 5
unavailable_services: 3
---

# Myriad Genetics如何使用AWS开源生成式AI智能文档处理加速器实现快速、准确且经济高效的文档处理

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/how-myriad-genetics-achieved-fast-accurate-and-cost-efficient-document-processing-using-the-aws-open-source-generative-ai-intelligent-document-processing-accelerator/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心生成式AI服务（Amazon Bedrock和Amazon Nova）在中国区域不可用，无法直接实施该解决方案

该解决方案完全依赖Amazon Bedrock和Amazon Nova模型进行文档分类和关键信息提取，这两个服务是整个架构的核心组件。由于这些服务在AWS中国区域不可用，原方案无法直接部署。虽然其他基础设施服务（如DynamoDB、Step Functions、SQS）可用，但缺少核心AI能力使得该方案需要重大架构调整。

## 服务分析

### 可用服务 (5个)

- Amazon Textract - OCR文本提取服务
- Amazon DynamoDB - 并发管理和状态跟踪
- AWS Step Functions - 工作流编排
- Amazon SQS - 消息队列服务
- Amazon SageMaker - 机器学习平台

### 不可用服务 (3个)

- **Amazon Bedrock** - 核心服务，提供基础模型访问
- **Amazon Nova (Pro, Premier, Lite)** - 核心服务，用于文档分类和信息提取
- **Amazon Comprehend** - 原有方案使用的文档分类服务

### 评估说明

1. **核心服务不可用**：Amazon Bedrock和Amazon Nova是该解决方案的核心，负责：
   - 文档分类（使用Amazon Nova Pro）
   - 关键信息提取（使用Amazon Nova Premier）
   - 提示工程和少样本学习
   - 思维链推理

2. **架构依赖性**：整个GenAI IDP Accelerator的Pattern 2模式完全基于Bedrock和Nova模型构建，无法简单替换

3. **业务价值受限**：原方案实现的关键优势（98%分类准确率、77%成本降低、90%提取准确率）都依赖于这些不可用的生成式AI服务

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 可行性评估为LOW，核心服务Amazon Bedrock和Amazon Nova在中国区域不可用，无法进行实际部署验证

### 关键发现

由于跳过深入验证，此部分基于静态分析：

1. **服务依赖性分析**
   - 解决方案的三个Pattern都依赖Amazon Bedrock或其他生成式AI服务
   - Pattern 1依赖Amazon Bedrock Data Automation
   - Pattern 2依赖Amazon Bedrock + Nova模型
   - Pattern 3依赖Amazon Bedrock + SageMaker

2. **GitHub项目兼容性**
   - 项目地址：https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws
   - 项目配置文件硬编码了对Bedrock和Nova的依赖
   - 需要大量代码修改才能适配中国区域

## 实施建议

### 推荐方案

**不建议直接实施原方案**

由于核心生成式AI服务不可用，建议考虑以下替代路径：

1. **等待服务上线**：关注Amazon Bedrock在AWS中国区域的上线计划
2. **采用替代架构**：使用中国区域可用的服务重新设计解决方案
3. **混合云方案**：在全球区域使用Bedrock服务，通过API集成到中国区域应用

### 替代方案

#### 方案1：Amazon SageMaker + 自托管大语言模型

- **实施方式**：
  - 使用Amazon SageMaker部署开源大语言模型（如Llama、Qwen等）
  - 保留Amazon Textract进行OCR处理
  - 使用SageMaker Endpoint替代Bedrock进行文档分类和信息提取
  - 需要自行实现提示工程和模型优化

- **复杂度**：高
  - 需要模型选型、部署和调优
  - 需要管理推理基础设施
  - 需要重写GenAI IDP Accelerator的核心逻辑

- **适用场景**：
  - 有机器学习团队支持
  - 对数据主权有严格要求
  - 愿意投入较高的初期开发成本

- **成本考虑**：
  - SageMaker实例持续运行成本
  - 可能需要GPU实例以获得合理的推理性能
  - 开发和维护成本较高

#### 方案2：Amazon Comprehend Custom + Amazon Textract

- **实施方式**：
  - 使用Amazon Textract进行OCR（中国区域可用）
  - 等待Amazon Comprehend在中国区域上线，或使用自定义分类模型
  - 使用规则引擎或传统NLP方法进行信息提取
  - 简化架构，降低对生成式AI的依赖

- **复杂度**：中
  - 需要标注数据训练自定义分类器
  - 信息提取准确率可能低于生成式AI方案
  - 需要更多人工规则和后处理逻辑

- **适用场景**：
  - 文档类型相对固定
  - 可以接受较低的自动化程度
  - 预算有限

- **局限性**：
  - 无法实现原方案的高级功能（如思维链推理、少样本学习）
  - 准确率可能无法达到98%的水平

#### 方案3：混合云架构

- **实施方式**：
  - 在AWS全球区域（如us-east-1）部署Bedrock相关服务
  - 通过API Gateway或VPN连接中国区域应用
  - 敏感数据处理在中国区域完成，仅发送脱敏文本到全球区域进行AI处理

- **复杂度**：中
  - 需要处理跨境数据传输
  - 需要考虑网络延迟和可靠性
  - 需要额外的安全和合规措施

- **适用场景**：
  - 对AI能力有强需求
  - 可以接受跨境数据传输（符合合规要求）
  - 能够容忍一定的网络延迟

- **风险**：
  - 跨境数据传输的合规性风险
  - 网络稳定性影响服务可用性
  - 可能产生额外的数据传输成本

### 风险提示

- **服务可用性风险**：核心生成式AI服务在中国区域的上线时间不确定，可能影响项目规划
- **合规风险**：医疗文档处理涉及敏感数据，跨境传输需要严格遵守数据保护法规
- **成本风险**：替代方案（特别是SageMaker自托管模型）的成本可能显著高于原方案
- **技术债务风险**：采用临时替代方案后，未来迁移到Bedrock可能需要重构
- **准确率风险**：替代方案可能无法达到原方案98%的分类准确率和90%的提取准确率
- **维护成本**：自托管模型方案需要持续的模型优化和基础设施维护

### 配套资源

- **GitHub仓库**: https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws
- **兼容性**: 不兼容中国区域，代码硬编码了对Amazon Bedrock和Nova模型的依赖
- **修改建议**: 
  - 需要重写核心的分类和提取模块
  - 需要替换所有Bedrock API调用
  - 需要重新设计配置文件结构
  - 建议工作量：至少4-6周的开发时间

## 总结

该博客展示了一个先进的生成式AI文档处理解决方案，但由于核心依赖的Amazon Bedrock和Amazon Nova服务在AWS中国区域不可用，**不建议在中国区域直接实施**。

如果必须在中国区域实现类似功能，建议：
1. 优先考虑使用Amazon SageMaker部署开源大语言模型的方案
2. 密切关注Amazon Bedrock在中国区域的上线进展
3. 评估业务需求是否可以接受传统机器学习方法的准确率
4. 如果合规允许，可以考虑混合云架构

对于有类似文档处理需求的中国区域客户，建议与AWS解决方案架构师团队联系，根据具体业务场景设计适合的替代方案。
