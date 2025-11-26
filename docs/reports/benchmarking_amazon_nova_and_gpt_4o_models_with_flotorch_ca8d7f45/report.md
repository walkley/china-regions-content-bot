---
title: 使用FloTorch对Amazon Nova和GPT-4o模型进行基准测试
publish_date: 2025-03-11
original_url: https://aws.amazon.com/blogs/machine-learning/benchmarking-amazon-nova-and-gpt-4o-models-with-flotorch/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 7
unavailable_services: 2
---

# 使用FloTorch对Amazon Nova和GPT-4o模型进行基准测试

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/benchmarking-amazon-nova-and-gpt-4o-models-with-flotorch/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Bedrock在中国区域不可用,无法访问Amazon Nova模型和Amazon Titan嵌入模型,导致整个方案无法实施

本文介绍的FloTorch RAG评估平台依赖Amazon Bedrock服务来访问Amazon Nova模型系列和Amazon Titan Text Embeddings V2模型。经过实际验证,Amazon Bedrock服务在AWS中国区域(cn-northwest-1和cn-north-1)完全不可用,这使得文章中描述的核心功能无法在中国区域实现。

## 服务分析

### 可用服务 (7个)

- Amazon OpenSearch Service - 向量数据库
- Amazon EC2 - OpenSearch集群节点
- AWS Lambda - 函数计算
- Amazon DynamoDB - 数据存储
- Amazon ECR - 容器镜像仓库
- Amazon ECS (Fargate) - 容器运行环境
- AWS Step Functions - 工作流编排

### 不可用服务 (2个)

- **Amazon Bedrock** - 核心服务,用于访问基础模型
- **AWS App Runner** - 应用托管服务

### 评估说明

**核心服务不可用的影响:**

1. **Amazon Bedrock (核心服务)** - 这是整个方案的基础,文章中的所有模型评估都依赖于此服务:
   - Amazon Nova Pro、Amazon Nova Lite、Amazon Nova Micro模型完全无法访问
   - Amazon Titan Text Embeddings V2嵌入模型无法使用
   - 无法进行文章中描述的模型性能对比测试
   - RAG评估管道的核心推理和嵌入功能无法实现

2. **AWS App Runner** - FloTorch使用此服务托管Web应用界面:
   - 可以使用Amazon ECS + Application Load Balancer替代
   - 需要额外的配置工作,但技术上可行

**验证过程:**

通过AWS CLI实际测试,确认了以下情况:
- 尝试访问Bedrock服务端点时返回连接错误: "Could not connect to the endpoint URL: https://bedrock.cn-northwest-1.amazonaws.com.cn/"
- 尝试访问App Runner服务端点时返回连接错误: "Could not connect to the endpoint URL: https://apprunner.cn-northwest-1.amazonaws.com.cn/"
- 其他基础设施服务(OpenSearch、Lambda、DynamoDB、ECR、ECS、Step Functions)均可正常访问

## 验证结果

### 验证类型

- ✅ GitHub项目部署验证(部分验证)
- ⚠️ 服务可用性验证(已完成)

### 执行状态

**状态**: ❌ 失败

**原因**: 核心依赖服务Amazon Bedrock在AWS中国区域不可用,导致项目无法部署和运行

### 关键发现

1. **Amazon Bedrock服务完全不可用**
   - 在cn-northwest-1和cn-north-1区域均无法访问Bedrock服务
   - 所有Amazon Nova模型(Pro、Lite、Micro)无法使用
   - Amazon Titan Text Embeddings V2模型无法使用
   - 这是阻断性问题,无法通过配置调整解决

2. **AWS App Runner服务不可用**
   - FloTorch使用App Runner托管Web应用
   - 可以使用ECS + ALB作为替代方案
   - 需要修改CloudFormation模板和部署脚本

3. **FloTorch项目架构分析**
   - 项目包含完整的CloudFormation模板,用于自动化部署
   - 部署需要创建VPC、Lambda、DynamoDB、OpenSearch、ECR、ECS等多个资源
   - 项目设计为在AWS Marketplace发布,支持订阅式部署
   - 核心功能严重依赖Bedrock服务,无法简单替换

4. **成本考虑**
   - 根据install.md文档,完整部署的日成本约为$56.53-$75.69
   - 主要成本来自OpenSearch集群(r7g.2xlarge实例)
   - 如果进行完整部署测试,会产生显著费用

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此方案**

由于Amazon Bedrock服务在中国区域不可用,文章中描述的核心功能无法实现:
- 无法使用Amazon Nova模型进行推理
- 无法使用Amazon Titan嵌入模型
- 无法复现文章中的性能基准测试
- FloTorch平台的核心价值(多模型对比评估)无法体现

### 替代方案

如果需要在AWS中国区域实现类似的RAG评估功能,可以考虑以下替代方案:

1. **使用Amazon SageMaker部署开源模型**
   - 实施方式:
     - 在SageMaker上部署开源LLM(如Llama、Mistral等)
     - 使用开源嵌入模型(如sentence-transformers)
     - 修改FloTorch代码以支持SageMaker端点
   - 复杂度: 高
   - 适用场景: 需要完全自主控制模型,有足够的技术团队支持
   - 局限性: 
     - 无法使用Amazon Nova模型
     - 需要大量代码修改
     - 模型性能和成本可能不如Bedrock优化

2. **使用第三方API服务**
   - 实施方式:
     - 使用OpenAI API(如文章中的GPT-4o)
     - 使用其他支持中国区域的LLM API服务
     - 修改FloTorch以支持外部API
   - 复杂度: 中
   - 适用场景: 可以接受数据传输到境外,主要用于测试和评估
   - 局限性:
     - 数据隐私和合规性问题
     - 网络延迟较高
     - 无法评估Amazon Nova模型

3. **等待Amazon Bedrock在中国区域上线**
   - 实施方式: 关注AWS中国区域服务更新
   - 复杂度: 低
   - 适用场景: 不急于实施,可以等待服务上线
   - 局限性: 上线时间不确定

### 风险提示

- **服务不可用风险**: Amazon Bedrock是核心依赖,在中国区域完全不可用,无法通过技术手段绕过
- **成本风险**: 如果尝试使用SageMaker替代方案,部署和运行大型LLM的成本可能显著高于Bedrock
- **合规风险**: 使用境外API服务可能涉及数据跨境传输的合规问题
- **维护风险**: 大幅修改FloTorch代码以适配替代方案,会增加后续维护难度
- **功能缺失风险**: 无法评估Amazon Nova模型,失去了文章的核心价值

### 配套资源

- **GitHub仓库**: https://github.com/FissionAI/FloTorch
- **兼容性**: 不兼容AWS中国区域
- **修改建议**: 
  - 需要完全重构模型访问层,替换Bedrock调用
  - 需要修改CloudFormation模板,移除App Runner,改用ECS + ALB
  - 需要重新设计嵌入和推理策略
  - 修改工作量巨大,不建议进行

## 技术细节

### 项目结构分析

FloTorch是一个企业级RAG评估平台,包含以下主要组件:

1. **基础设施层** (CloudFormation模板):
   - VPC和网络配置
   - OpenSearch集群(向量数据库)
   - Lambda函数(索引、检索、评估)
   - DynamoDB表(配置和结果存储)
   - ECR仓库(容器镜像)
   - ECS Fargate(批处理任务)
   - App Runner(Web应用托管)
   - Step Functions(工作流编排)

2. **应用层** (Python代码):
   - Web API (FastAPI)
   - 分块策略(固定分块、层次分块)
   - 嵌入处理(Bedrock Titan)
   - 检索和重排序
   - 推理处理(Bedrock模型)
   - 评估框架(RAGAS)

3. **前端层** (Nuxt.js):
   - 实验配置界面
   - 结果可视化
   - 成本计算

### Bedrock依赖分析

通过代码分析,发现以下文件直接依赖Bedrock服务:

- `util/bedrock_utils.py` - Bedrock客户端工具
- `core/embedding/bedrock/` - Bedrock嵌入实现
- `core/inference/bedrock/` - Bedrock推理实现
- `core/guardrails/bedrock_guardrails.py` - Bedrock护栏
- `app/routes/bedrock_config.py` - Bedrock配置API

这些核心模块的替换需要大量工作,且无法保证功能等价性。

## 结论

本文介绍的使用FloTorch对Amazon Nova和GPT-4o模型进行基准测试的方案,由于核心依赖的Amazon Bedrock服务在AWS中国区域不可用,**无法在中国区域实施**。

虽然FloTorch是一个设计优秀的RAG评估平台,但其核心价值(评估Amazon Nova等Bedrock模型)在中国区域无法实现。如果需要在中国区域进行类似的RAG评估工作,建议:

1. 使用SageMaker部署开源模型,但需要大量开发工作
2. 关注AWS中国区域服务更新,等待Bedrock服务上线
3. 考虑在AWS全球区域进行评估,然后将结果应用于中国区域的架构设计

对于希望了解RAG评估方法论和最佳实践的读者,本文仍有参考价值,但实际实施需要等待服务支持或采用替代方案。
