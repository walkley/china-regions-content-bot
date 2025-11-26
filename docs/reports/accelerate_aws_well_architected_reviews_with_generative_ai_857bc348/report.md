---
title: 使用生成式AI加速AWS Well-Architected审查
publish_date: 2025-03-04
original_url: https://aws.amazon.com/blogs/machine-learning/accelerate-aws-well-architected-reviews-with-generative-ai/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 13
unavailable_services: 3
---

# 使用生成式AI加速AWS Well-Architected审查

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/accelerate-aws-well-architected-reviews-with-generative-ai/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

该方案的两个核心服务Amazon Bedrock和Amazon Textract在AWS中国区域不可用，这两个服务是整个解决方案的基础架构组件，无法通过简单替换实现相同功能。

## 服务分析

### 可用服务 (13个)

- AWS Lambda
- Amazon SQS (Simple Queue Service)
- Amazon S3 (Simple Storage Service)
- Amazon OpenSearch Serverless
- Amazon CloudFront
- Amazon Cognito
- Amazon EC2 (Elastic Compute Cloud)
- AWS Step Functions
- Amazon DynamoDB
- AWS PrivateLink
- AWS Well-Architected Tool
- AWS CDK (Cloud Development Kit)
- Amazon Bedrock Guardrails

### 不可用服务 (3个)

- **Amazon Bedrock** - 核心服务
- **Amazon Textract** - 核心服务
- **Amazon Rekognition** - 文中提到但非核心使用

### 评估说明

虽然可用服务占比达到81.25%（13/16），但不可用的服务恰恰是该解决方案的核心：

1. **Amazon Bedrock的关键作用**：
   - 提供生成式AI能力，是整个方案的核心引擎
   - 支持RAG（检索增强生成）架构
   - 提供Knowledge Bases功能用于向量数据库和知识检索
   - 驱动AI聊天界面进行交互式探索
   - 生成WAFR评估报告和建议

2. **Amazon Textract的关键作用**：
   - 从上传的PDF架构文档中提取文本内容
   - 是文档处理流程的第一步，为后续AI分析提供输入
   - 无此服务，无法处理用户上传的架构文档

3. **架构依赖性**：
   - 整个解决方案的工作流程高度依赖这两个服务
   - 替换这些服务需要重新设计核心架构
   - 无法保持原方案的功能完整性和用户体验

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 初步可行性评估为LOW，核心服务Amazon Bedrock和Amazon Textract在中国区域不可用，无法进行实际部署验证。

## 实施建议

### 推荐方案

**不建议直接实施**

该解决方案在AWS中国区域无法实施，原因如下：

1. **核心服务缺失**：Amazon Bedrock是整个生成式AI方案的基础，在中国区域不可用
2. **文档处理受限**：Amazon Textract用于PDF文档内容提取，无可用替代方案能提供相同的准确性和易用性
3. **架构完整性**：即使替换部分组件，也无法保持原方案的功能完整性和性能表现

### 替代方案

如果确实需要在AWS中国区域实现类似的Well-Architected审查加速功能，可以考虑以下替代思路：

1. **使用第三方LLM服务**
   - 实施方式：集成国内可用的大语言模型服务（如通义千问、文心一言等）替代Amazon Bedrock
   - 复杂度：高
   - 适用场景：需要完全重新设计架构，包括：
     - 重写所有与Bedrock交互的代码
     - 重新实现RAG架构和知识库功能
     - 调整提示工程以适配不同的模型
     - 处理数据隐私和合规性问题
   - 注意事项：需要评估第三方服务的数据安全性、合规性和成本

2. **使用开源OCR工具替代Textract**
   - 实施方式：使用Tesseract、PaddleOCR等开源OCR工具处理PDF文档
   - 复杂度：中
   - 适用场景：文档格式相对标准，对提取准确率要求不是极高的情况
   - 注意事项：
     - 需要自行部署和维护OCR服务
     - 准确率可能低于Textract
     - 需要额外的文档预处理和后处理逻辑

3. **混合云架构**
   - 实施方式：在AWS全球区域部署核心AI处理组件，中国区域部署应用层和数据存储
   - 复杂度：高
   - 适用场景：对数据出境有明确合规路径的组织
   - 注意事项：
     - 需要处理跨境数据传输的合规性问题
     - 网络延迟可能影响用户体验
     - 需要设计数据脱敏和加密方案

### 风险提示

- **架构重构风险**：任何替代方案都需要大规模重构，开发和测试成本高
- **功能差异风险**：替代服务可能无法完全复制Amazon Bedrock的能力，导致功能降级
- **合规性风险**：使用第三方LLM服务或跨境数据传输需要仔细评估合规性要求
- **维护成本风险**：自建或集成第三方服务会增加长期维护成本和复杂度
- **性能风险**：替代方案可能无法达到原方案的性能和响应速度

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/sample-well-architected-acceleration-with-generative-ai
- **兼容性**: 不兼容AWS中国区域
- **修改建议**: 由于核心依赖服务不可用，无法通过简单修改实现兼容。如需在中国区域实施，建议参考上述替代方案进行完全重构。
