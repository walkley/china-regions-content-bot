---
title: 使用LLM实现企业级自然语言到SQL生成：平衡准确性、延迟和规模
publish_date: 2025-04-24
original_url: https://aws.amazon.com/blogs/machine-learning/enterprise-grade-natural-language-to-sql-generation-using-llms-balancing-accuracy-latency-and-scale/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 4
unavailable_services: 1
---

# 使用LLM实现企业级自然语言到SQL生成：平衡准确性、延迟和规模

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/enterprise-grade-natural-language-to-sql-generation-using-llms-balancing-accuracy-latency-and-scale/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Bedrock在中国区域不可用，整个NL2SQL解决方案依赖该服务提供LLM能力，无法直接实施

该方案的核心依赖Amazon Bedrock提供的大语言模型能力进行领域分类、命名实体识别和SQL生成，由于Bedrock在中国区域不可用，方案无法按原文实施。

## 服务分析

### 可用服务 (4个)

- Amazon Aurora
- Amazon API Gateway
- Amazon Cognito
- AWS Lambda

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务

### 评估说明

虽然从数量上看80%的服务可用，但Amazon Bedrock是该解决方案的绝对核心服务，承担了以下关键功能：

1. **领域分类**：使用LLM将用户查询映射到特定数据域
2. **命名实体识别**：从用户查询中提取命名资源
3. **SQL生成**：根据准备好的提示词生成SQL查询语句

文章中明确提到使用Anthropic的Claude Haiku 3模型（通过Bedrock访问），以及Meta的Code Llama 13B模型。整个架构设计围绕Bedrock构建，缺少该服务将导致方案无法运行。

其他可用服务（API Gateway、Lambda、Cognito、Aurora）虽然重要，但都是支撑性服务，无法弥补核心LLM服务的缺失。

## 验证结果

### 验证类型

⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段发现核心服务Amazon Bedrock在中国区域不可用，可行性评估为LOW，根据验证流程跳过深入验证阶段。

## 实施建议

### 推荐方案

不建议在AWS中国区域直接实施该方案。核心服务Amazon Bedrock的缺失使得原方案无法运行。

### 替代方案

如果需要在中国区域实现类似的NL2SQL功能，可以考虑以下替代方案：

1. **使用Amazon SageMaker部署开源LLM**
   - 实施方式：在SageMaker上部署开源大语言模型（如Llama 2、Mistral等），替代Bedrock提供的模型推理能力
   - 复杂度：高
   - 适用场景：有足够的ML工程能力和预算，需要完全控制模型部署和优化
   - 注意事项：
     - 需要自行管理模型部署、扩展和优化
     - 需要处理模型许可证问题
     - 推理成本和延迟可能高于Bedrock
     - 需要额外的MLOps工作

2. **使用第三方LLM API服务**
   - 实施方式：集成国内可用的大语言模型服务（如阿里云通义千问、百度文心一言等），通过API调用替代Bedrock
   - 复杂度：中
   - 适用场景：快速实现功能，不需要完全控制模型
   - 注意事项：
     - 需要评估第三方服务的数据隐私和安全政策
     - API调用延迟可能受网络影响
     - 需要适配不同的API接口和提示词格式
     - 成本结构可能不同

3. **混合架构方案**
   - 实施方式：在AWS全球区域使用Bedrock处理LLM推理，通过专线或VPN连接到中国区域的数据库
   - 复杂度：高
   - 适用场景：数据可以跨境传输，对延迟要求不是特别严格
   - 注意事项：
     - 需要符合数据跨境传输的合规要求
     - 网络延迟会显著增加
     - 需要额外的网络连接成本
     - 架构复杂度高

### 风险提示

- **核心功能缺失**：无法使用Bedrock意味着需要重新构建整个LLM推理层，这是方案的核心部分
- **开发成本**：任何替代方案都需要大量的额外开发和测试工作
- **性能差异**：替代方案的准确性、延迟和成本可能与原方案有显著差异
- **维护负担**：自行部署LLM模型需要持续的维护和优化工作
- **合规风险**：使用第三方服务或跨境数据传输需要仔细评估合规要求

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/blog-natural-language-data-retrieval
- **兼容性**: 代码依赖Amazon Bedrock，无法在中国区域直接使用
- **修改建议**: 需要重构LLM调用层，替换Bedrock为其他LLM服务，工作量大且需要重新验证准确性
