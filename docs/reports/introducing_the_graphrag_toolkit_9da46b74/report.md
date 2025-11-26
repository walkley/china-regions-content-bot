---
title: GraphRAG工具包介绍
publish_date: 2025-01-27
original_url: https://aws.amazon.com/blogs/database/introducing-the-graphrag-toolkit/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: MODERATE
available_services: 7
unavailable_services: 1
---

# GraphRAG工具包介绍

[📖 查看原始博客](https://aws.amazon.com/blogs/database/introducing-the-graphrag-toolkit/) | 验证日期: 2025-11-25

## 可行性评估

!!! warning "MODERATE - 谨慎实施"
    大部分服务可用，但核心的Amazon Bedrock服务在中国区不可用，需要替换LLM提供商才能实施。

虽然图数据库和向量存储服务在中国区完全可用，但博客中的所有示例和CloudFormation模板都依赖Amazon Bedrock提供基础模型。需要配置替代的LLM和embedding模型才能在中国区域使用。

## 服务分析

### 可用服务 (7个)

- Amazon Neptune
- Amazon Neptune Analytics
- Amazon OpenSearch Serverless
- Amazon SageMaker
- AWS CloudFormation
- Amazon S3
- AWS IAM
- Amazon VPC

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务，用于提供LLM和embedding模型

### 评估说明

GraphRAG Toolkit是一个开源Python库，用于构建图增强的RAG工作流。该工具包的核心功能包括：
1. 从非结构化数据自动构建带向量嵌入的图
2. 组合问答策略来查询图并检索结构相关信息

**核心服务可用性：**
- ✅ 图存储：Neptune Database和Neptune Analytics在中国区完全可用
- ✅ 向量存储：OpenSearch Serverless在中国区完全可用
- ❌ 基础模型：Amazon Bedrock在中国区不可用

**不可用服务的影响：**
Amazon Bedrock是该方案的核心依赖，用于：
- 提取LLM：从文档中提取图结构（默认：Claude 3.7 Sonnet）
- 响应LLM：生成问答响应（默认：Claude 3.7 Sonnet）
- Embedding模型：生成向量嵌入（默认：Cohere Embed English v3）

**替代方案可行性：**
根据项目文档，GraphRAG Toolkit支持通过LlamaIndex配置其他LLM后端，这为在中国区域实施提供了可能性。

## 验证结果

### 验证类型

✅ GitHub项目部署验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 博客提供的CloudFormation模板和示例代码完全依赖Amazon Bedrock服务。虽然项目理论上支持配置其他LLM后端，但这需要替换核心服务，超出了智能修正策略的允许范围（禁止替换不可用服务）。直接部署会因Bedrock不可用而失败。

### 关键发现

1. **项目架构灵活性**
   - GraphRAG Toolkit通过LlamaIndex支持多种LLM后端
   - 可以配置自定义的LLM和embedding模型
   - 但所有官方示例和文档都基于Bedrock

2. **本地开发环境**
   - 项目提供了本地开发环境（使用Neo4j + PostgreSQL）
   - 本地环境配置使用sentence-transformers作为embedding模型
   - 但LLM配置仍需要用户自行解决

3. **CloudFormation模板限制**
   - 所有CloudFormation模板都硬编码了Bedrock模型ARN
   - IAM策略包含Bedrock权限
   - 无法在中国区域直接使用这些模板

## 实施建议

### 推荐方案

**主要实施路径：**
可以在中国区域实施该方案，但需要进行以下关键调整：

1. **替换LLM提供商**
   - 使用支持中国区域的LLM服务（如通过API调用的第三方模型）
   - 或部署自托管的开源LLM（如在EC2上运行Ollama）
   - 通过LlamaIndex的LLM接口进行集成

2. **替换Embedding模型**
   - 使用HuggingFace的sentence-transformers模型
   - 或使用支持中国区域的embedding API服务
   - 通过LlamaIndex的BaseEmbedding接口进行集成

3. **修改部署方式**
   - 不使用提供的CloudFormation模板
   - 手动创建Neptune和OpenSearch Serverless资源
   - 使用Python代码直接配置GraphRAG Toolkit

**需要调整的部分：**
- CloudFormation模板无法使用，需要手动创建基础设施
- 所有示例代码中的模型配置需要修改
- 需要额外的LLM服务部署或API集成工作

**预计工作量：**
中等 - 需要2-3天的额外工作来配置替代LLM方案和修改示例代码

### 替代方案

#### 方案1：使用自托管LLM

**实施方式：**
1. 在EC2实例上部署Ollama或vLLM
2. 运行开源模型（如Llama 3、Qwen等）
3. 通过LlamaIndex的Ollama集成连接到GraphRAG Toolkit

**配置示例：**
```python
from llama_index.llms.ollama import Ollama
from graphrag_toolkit.lexical_graph import GraphRAGConfig

# 配置自托管LLM
GraphRAGConfig.extraction_llm = Ollama(
    model="llama3.1:70b",
    base_url="http://your-ec2-instance:11434"
)
GraphRAGConfig.response_llm = Ollama(
    model="llama3.1:70b", 
    base_url="http://your-ec2-instance:11434"
)

# 配置本地embedding模型
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
GraphRAGConfig.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-large-zh-v1.5"
)
GraphRAGConfig.embed_dimensions = 1024
```

**复杂度：** 中
**适用场景：** 需要完全控制模型和数据隐私的场景

#### 方案2：使用第三方API服务

**实施方式：**
1. 使用支持中国区域的LLM API服务（如阿里云通义千问、百度文心一言等）
2. 通过LlamaIndex的自定义LLM包装器集成
3. 配置到GraphRAG Toolkit

**复杂度：** 低
**适用场景：** 快速验证和原型开发，不需要自己管理模型基础设施

#### 方案3：混合部署

**实施方式：**
1. 核心图数据库和向量存储使用AWS中国区域服务
2. LLM服务使用全球区域的Bedrock（通过VPN或专线）
3. 或使用本地embedding + 远程LLM的组合

**复杂度：** 高
**适用场景：** 已有跨区域网络连接的企业客户

### 风险提示

- **性能风险**: 自托管LLM需要GPU实例，成本较高（如p3.2xlarge约$3/小时）
- **兼容性风险**: 开源模型的效果可能不如Claude 3.7 Sonnet，需要充分测试
- **维护成本**: 自托管方案需要额外的运维工作来管理模型服务
- **网络延迟**: 如果使用跨区域方案，网络延迟可能影响用户体验
- **API限制**: 第三方API服务可能有调用频率和并发限制

### 配套资源

- **GitHub仓库**: https://github.com/awslabs/graphrag-toolkit
- **兼容性**: 核心代码可在中国区使用，但需要替换LLM提供商
- **修改建议**: 
  1. 跳过CloudFormation模板，手动创建Neptune和OpenSearch资源
  2. 参考本地开发环境示例（lexical-graph-local-dev）了解非Bedrock配置
  3. 使用GraphRAGConfig配置自定义LLM和embedding模型
  4. 所有示例代码中的模型ID需要替换为可用的模型

### 实施步骤建议

1. **准备阶段**
   - 在中国区域创建Neptune Database集群
   - 创建OpenSearch Serverless集合
   - 决定LLM方案（自托管或API）

2. **LLM配置阶段**
   - 如选择自托管：部署Ollama/vLLM到EC2
   - 如选择API：申请并测试第三方LLM API
   - 配置embedding模型（推荐使用HuggingFace模型）

3. **集成测试阶段**
   - 克隆GraphRAG Toolkit仓库
   - 修改配置文件，指向中国区域资源
   - 运行简单的索引和查询测试

4. **优化阶段**
   - 调整模型参数以优化性能
   - 测试不同的查询策略
   - 监控成本和性能指标
