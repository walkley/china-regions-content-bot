---
title: Shorthills AI 联合 AWS 和 DataStax 转型企业数据搜索
publish_date: 2025-05-13
original_url: https://aws.amazon.com/blogs/apn/shorthills-ai-teams-with-aws-and-datastax-to-transform-enterprise-data-search/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 8
unavailable_services: 2
---

# Shorthills AI 联合 AWS 和 DataStax 转型企业数据搜索

[📖 查看原始博客](https://aws.amazon.com/blogs/apn/shorthills-ai-teams-with-aws-and-datastax-to-transform-enterprise-data-search/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

虽然80%的基础设施服务在中国区可用，但两个核心AI服务（Amazon Textract 和 Amazon Bedrock）均不可用，这两个服务是整个智能搜索方案的关键组件，直接影响文本提取和向量嵌入生成功能。

## 服务分析

### 可用服务 (8个)

- Amazon S3
- AWS Lambda
- AWS Step Functions
- Amazon EventBridge
- Amazon Neptune
- AWS Key Management Service (KMS)
- Amazon Virtual Private Cloud (VPC)
- Amazon DynamoDB

### 不可用服务 (2个)

- **Amazon Textract** - 核心服务，负责从PDF和扫描图像中自动提取文本和结构化数据
- **Amazon Bedrock** - 核心服务，负责实体关系提取、生成文本嵌入向量，是RAG框架的核心

### 评估说明

该方案的核心价值在于利用AI技术实现智能文档搜索和分析。方案架构中有两个关键环节完全依赖不可用服务：

1. **文本提取环节**：Amazon Textract 用于从PDF、扫描图像等非结构化文档中提取文本。这是数据处理管道的第一步，没有替代方案将无法处理原始文档。

2. **AI分析环节**：Amazon Bedrock 用于：
   - 从文本块中提取实体和关系
   - 生成文本嵌入向量用于语义搜索
   - 支持OptimizeRAG框架的核心功能

这两个服务的缺失意味着方案的核心AI能力无法实现。虽然基础设施层（存储、计算、编排）的服务都可用，但缺少了"大脑"部分。

## 验证结果

### 验证类型

- ⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证结果为LOW，核心AI服务（Amazon Textract 和 Amazon Bedrock）在中国区不可用，无法支撑方案的核心功能。根据验证流程，仅当可行性评估为MODERATE或HIGH时才执行深入验证。

### 关键发现

由于跳过了深入验证，此部分不适用。

## 实施建议

### 推荐方案

**不建议直接实施原方案**

原因如下：
1. Amazon Textract 在中国区不可用，无法实现自动文本提取功能
2. Amazon Bedrock 在中国区不可用，无法实现实体关系提取和向量嵌入生成
3. 这两个服务是方案的核心组件，替换它们需要重新设计整个架构

### 替代方案

如果确实需要在中国区实现类似功能，可以考虑以下替代方案：

#### 方案1：使用开源OCR + 自托管LLM

**实施方式：**
- 使用开源OCR工具（如Tesseract、PaddleOCR）替代Amazon Textract
- 在Amazon EC2或Amazon ECS上部署开源大语言模型（如Llama、ChatGLM）替代Amazon Bedrock
- 使用开源嵌入模型（如sentence-transformers）生成向量

**复杂度：** 高

**适用场景：**
- 有较强的AI/ML团队支持
- 可以承担模型训练和优化的成本
- 对数据隐私有严格要求，希望完全自主控制

**挑战：**
- 需要大量GPU资源用于模型推理
- 模型性能和准确度需要持续优化
- 运维成本和复杂度显著增加

#### 方案2：使用第三方AI服务

**实施方式：**
- 使用国内云服务商的OCR服务（如阿里云OCR、腾讯云OCR）替代Amazon Textract
- 使用国内大模型服务（如通义千问、文心一言）替代Amazon Bedrock
- 保留AWS基础设施层（S3、Lambda、Neptune等）

**复杂度：** 中

**适用场景：**
- 希望快速实施，减少自建成本
- 可以接受使用第三方AI服务
- 数据合规性允许调用外部API

**挑战：**
- 需要评估第三方服务的数据安全和合规性
- 可能存在服务集成和API兼容性问题
- 成本结构需要重新评估

#### 方案3：混合架构（推荐）

**实施方式：**
- 文本提取：使用Amazon Textract中国区替代方案（开源OCR + 自定义优化）
- 向量生成：在Amazon SageMaker上部署开源嵌入模型
- 实体提取：使用Amazon Comprehend（如可用）或自托管NER模型
- 保留原方案的数据存储和编排架构

**复杂度：** 中到高

**适用场景：**
- 希望最大化利用AWS服务
- 有一定的AI/ML能力
- 需要平衡性能、成本和可维护性

**优势：**
- 充分利用AWS中国区可用服务
- 相对可控的实施复杂度
- 更好的长期可维护性

### 风险提示

- **技术风险**：替代方案的AI模型性能可能无法达到Amazon Bedrock的水平，需要大量调优工作
- **成本风险**：自托管LLM需要大量GPU资源，运营成本可能显著高于托管服务
- **合规风险**：使用第三方AI服务需要仔细评估数据隐私和合规要求
- **运维风险**：自建AI服务增加了系统复杂度，需要专业的AI/ML运维团队
- **时间风险**：替代方案的开发和调优周期可能较长，影响项目交付时间

### 配套资源

- **GitHub仓库**: 文章未提供配套代码仓库
- **兼容性**: 不适用
- **修改建议**: 如需在中国区实施，建议参考上述替代方案，重新设计架构
