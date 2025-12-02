---
title: CBRE如何使用Amazon Bedrock支持统一的物业管理搜索和数字助手
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/machine-learning/how-cbre-powers-unified-property-management-search-and-digital-assistant-using-amazon-bedrock/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 6
unavailable_services: 3
---

# CBRE如何使用Amazon Bedrock支持统一的物业管理搜索和数字助手

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/how-cbre-powers-unified-property-management-search-and-digital-assistant-using-amazon-bedrock/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

本方案的核心依赖Amazon Bedrock及其基础模型（Amazon Nova Pro、Claude Haiku）来实现自然语言查询转SQL、文档语义搜索和对话式AI助手功能。经验证，Amazon Bedrock在AWS中国区域（cn-northwest-1）完全不可用，且Amazon Nova和Claude系列模型均无法在中国区域使用。这些服务是整个解决方案的核心引擎，缺失后无法实现方案的主要价值。

## 服务分析

### 可用服务 (6个)

- Amazon OpenSearch Service
- Amazon RDS (PostgreSQL, MS SQL)
- Amazon ECS
- AWS Lambda
- Amazon DynamoDB
- Amazon ElastiCache for Redis

### 不可用服务 (3个)

- **Amazon Bedrock** - 核心服务
- **Amazon Nova Pro** - 核心服务（用于SQL查询生成）
- **Claude Haiku** - 核心服务（用于文档交互）

### 评估说明

该方案的架构高度依赖生成式AI能力：

1. **核心服务完全不可用**：Amazon Bedrock是整个解决方案的AI引擎，负责自然语言理解、SQL生成和文档对话功能。该服务在中国区域不可用。

2. **基础模型缺失**：方案特别依赖Amazon Nova Pro（实现67%的SQL生成性能提升）和Claude Haiku（支持智能文档交互）。这些模型均无法在中国区域访问。

3. **核心功能受影响**：
   - 自然语言查询转SQL功能无法实现
   - 文档语义搜索能力缺失
   - "Chat with Document"数字助手功能无法部署
   - 向量嵌入生成（Amazon Titan Text Embeddings v2）不可用

4. **可用服务的局限性**：虽然OpenSearch、RDS、Lambda等基础设施服务可用，但它们只是数据存储和计算层，无法替代生成式AI的核心能力。

## 验证结果

### 验证类型

⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Bedrock在中国区域完全不可用，无法进行实际部署验证。即使部署基础设施组件，也无法实现方案的核心AI功能。

## 实施建议

### 推荐方案

**不建议直接实施**

该方案在AWS中国区域无法按原设计实施，因为：

1. **核心AI服务缺失**：Amazon Bedrock及其所有基础模型在中国区域不可用
2. **功能完整性无法保证**：方案的主要价值（自然语言搜索、智能文档交互）依赖不可用的服务
3. **性能优化无法复现**：文章强调的67%性能提升来自Amazon Nova Pro，该模型在中国区域不可用

### 替代方案

如果必须在AWS中国区域实现类似功能，需要考虑以下替代方案：

1. **使用第三方LLM服务**
   - 实施方式：集成国内可用的大语言模型服务（如通义千问、文心一言等）替代Amazon Bedrock
   - 复杂度：高
   - 适用场景：需要完全在中国区域部署的场景
   - 注意事项：
     - 需要重新设计整个AI交互层
     - 提示工程需要针对不同模型重新优化
     - 性能指标可能与原方案差异较大
     - 需要处理不同API接口和认证机制

2. **混合云架构**
   - 实施方式：将AI推理层部署在AWS全球区域，数据层保留在中国区域
   - 复杂度：高
   - 适用场景：数据合规允许跨境传输的情况
   - 注意事项：
     - 需要评估数据跨境传输的合规性
     - 网络延迟会影响用户体验
     - 需要设计安全的跨区域数据传输机制
     - 成本会显著增加

3. **自托管开源模型**
   - 实施方式：在Amazon ECS或Amazon SageMaker上部署开源LLM（如Llama、ChatGLM等）
   - 复杂度：高
   - 适用场景：对数据隐私要求极高，且有充足的技术团队支持
   - 注意事项：
     - 需要大量GPU资源，成本高昂
     - 模型性能和效果需要充分测试
     - 需要专业团队进行模型微调和维护
     - 推理延迟可能高于托管服务

### 风险提示

- **技术风险**：替代方案需要大量的架构重新设计和开发工作，技术复杂度显著提升
- **成本风险**：无论采用哪种替代方案，成本都会显著高于原方案（第三方服务费用或自托管GPU成本）
- **性能风险**：替代方案无法保证达到原方案的性能指标（如67%的SQL生成性能提升）
- **合规风险**：混合云方案需要仔细评估数据跨境传输的法律合规性
- **维护风险**：自托管方案需要持续的运维投入和专业团队支持

### 配套资源

- **GitHub仓库**: 文章未提供配套的GitHub代码仓库
- **兼容性**: 不适用
- **修改建议**: 不适用

## 总结

CBRE的这个解决方案展示了Amazon Bedrock在企业级应用中的强大能力，但由于核心服务在AWS中国区域的不可用性，该方案无法直接在中国区域实施。如果有在中国区域实现类似功能的需求，建议：

1. 重新评估业务需求，确定是否必须在中国区域部署
2. 如果必须在中国区域部署，需要投入大量资源进行架构重新设计
3. 充分评估替代方案的技术可行性、成本和合规性
4. 考虑在AWS全球区域部署，如果数据合规允许的话

对于希望使用生成式AI能力的中国区域客户，建议关注AWS中国区域未来的服务更新，或考虑在全球区域部署类似解决方案。
