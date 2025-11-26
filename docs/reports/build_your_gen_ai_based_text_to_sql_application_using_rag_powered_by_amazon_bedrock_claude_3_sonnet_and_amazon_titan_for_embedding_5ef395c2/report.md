---
title: 使用RAG构建基于生成式AI的文本转SQL应用程序，由Amazon Bedrock（Claude 3 Sonnet和Amazon Titan嵌入）提供支持
publish_date: 2025-03-18
original_url: https://aws.amazon.com/blogs/machine-learning/build-your-gen-ai-based-text-to-sql-application-using-rag-powered-by-amazon-bedrock-claude-3-sonnet-and-amazon-titan-for-embedding/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 2
unavailable_services: 1
---

# 使用RAG构建基于生成式AI的文本转SQL应用程序，由Amazon Bedrock（Claude 3 Sonnet和Amazon Titan嵌入）提供支持

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/build-your-gen-ai-based-text-to-sql-application-using-rag-powered-by-amazon-bedrock-claude-3-sonnet-and-amazon-titan-for-embedding/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Bedrock在中国区域不可用，整个解决方案无法实施

该解决方案完全依赖Amazon Bedrock服务及其基础模型（Claude 3.5 Sonnet和Titan Embeddings v2），而Amazon Bedrock目前在AWS中国区域不可用，导致整个方案无法在中国区域部署。

## 服务分析

### 可用服务 (2个)

- Amazon S3 (Simple Storage Service)
- Amazon SageMaker Studio

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务
  - Anthropic's Claude 3.5 Sonnet模型（通过Bedrock访问）
  - Amazon Titan Text Embeddings v2模型（通过Bedrock访问）

### 评估说明

1. **核心服务不可用**：Amazon Bedrock是该解决方案的核心服务，提供了两个关键功能：
   - 使用Claude 3.5 Sonnet生成SQL查询
   - 使用Titan Embeddings v2进行文本嵌入和向量化

2. **架构依赖性**：整个RAG（检索增强生成）架构完全建立在Amazon Bedrock之上，包括：
   - LLM推理能力
   - 文本嵌入生成
   - 向量相似度搜索的基础

3. **无直接替代方案**：虽然Amazon S3和SageMaker在中国区可用，但它们只是辅助服务，无法替代Bedrock的核心功能。

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段确认核心服务Amazon Bedrock在AWS中国区域不可用，可行性评级为LOW。根据验证流程，当基础验证结果为LOW时，跳过深入验证阶段，因为即使进行部署测试也无法成功。

## 实施建议

### 推荐方案

不建议在AWS中国区域直接实施此解决方案。核心服务Amazon Bedrock的缺失使得原方案无法运行。

### 替代方案

如果需要在AWS中国区域实现类似的文本转SQL功能，可以考虑以下替代方案：

1. **使用Amazon SageMaker部署开源LLM**
   - 实施方式：
     - 在SageMaker上部署开源大语言模型（如Llama 2、ChatGLM等）
     - 使用开源嵌入模型（如sentence-transformers）替代Titan Embeddings
     - 自行实现RAG框架和向量数据库（如FAISS、Milvus）
   - 复杂度：高
   - 适用场景：有充足的ML工程资源和预算，需要完全控制模型和数据
   - 注意事项：
     - 需要自行管理模型训练、优化和部署
     - 推理成本可能较高，需要合理配置实例类型
     - 模型性能可能不如Claude 3.5 Sonnet

2. **使用第三方AI服务API**
   - 实施方式：
     - 集成国内可用的大语言模型服务（如阿里云通义千问、百度文心一言等）
     - 在AWS中国区域部署应用逻辑和数据存储
     - 通过API调用外部LLM服务
   - 复杂度：中
   - 适用场景：快速实现功能，不需要完全在AWS生态内部署
   - 注意事项：
     - 需要评估数据出境合规性
     - API调用延迟可能影响用户体验
     - 依赖第三方服务的可用性和定价

3. **混合云架构**
   - 实施方式：
     - 在AWS全球区域（如us-east-1）部署Amazon Bedrock相关服务
     - 在AWS中国区域部署数据存储和应用前端
     - 通过专线或VPN连接两个区域
   - 复杂度：高
   - 适用场景：对Amazon Bedrock有强依赖，且可以接受跨区域架构
   - 注意事项：
     - 需要考虑数据跨境传输的合规性要求
     - 网络延迟会影响用户体验
     - 架构复杂度和运维成本显著增加

### 风险提示

- **服务不可用风险**：Amazon Bedrock在中国区域的上线时间不确定，短期内无法使用该服务
- **替代方案复杂度**：所有替代方案都需要重大架构调整，开发和运维成本显著增加
- **性能差异**：替代方案中使用的开源模型在SQL生成准确性和性能上可能不如Claude 3.5 Sonnet
- **合规性风险**：如果采用跨境或第三方服务方案，需要仔细评估数据安全和合规性要求
- **成本考虑**：自行部署和管理LLM的成本可能远高于使用托管服务

### 配套资源

- **代码包**: https://aws-blogs-artifacts-public.s3.us-east-1.amazonaws.com/artifacts/ML-16850/code_repo.zip
- **兼容性**: 不兼容AWS中国区域
- **修改建议**: 代码完全依赖Amazon Bedrock API，无法通过简单修改在中国区域运行。如需实施，必须采用上述替代方案之一，并进行大规模代码重构。
