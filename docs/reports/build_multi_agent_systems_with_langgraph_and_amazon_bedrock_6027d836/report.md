---
title: 使用LangGraph和Amazon Bedrock构建多智能体系统
publish_date: 2025-04-14
original_url: https://aws.amazon.com/blogs/machine-learning/build-multi-agent-systems-with-langgraph-and-amazon-bedrock/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 1
unavailable_services: 2
---

# 使用LangGraph和Amazon Bedrock构建多智能体系统

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/build-multi-agent-systems-with-langgraph-and-amazon-bedrock/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Bedrock在中国区不可用，无法直接实施

本博客的核心依赖服务Amazon Bedrock目前在AWS中国区域（cn-north-1和cn-northwest-1）均不可用。经过实际连接测试，Bedrock服务endpoint在中国区域无法访问，这使得博客中介绍的多智能体系统无法在中国区域部署。

## 服务分析

### 可用服务 (1个)

- AWS Identity and Access Management (IAM)

### 不可用服务 (2个)

- **Amazon Bedrock** - 核心服务
- **Amazon Bedrock Agents** - 核心服务

### 评估说明

Amazon Bedrock是本博客的核心基础服务，用于提供大语言模型（LLM）能力。博客中的所有示例代码都依赖于Bedrock服务来：

1. **提供LLM推理能力**：使用Claude 3 Sonnet和Claude 3.5 Sonnet模型进行自然语言理解和生成
2. **支持多智能体协作**：通过Bedrock Agents实现智能体之间的协调和任务分配
3. **工具调用和决策**：LLM通过Bedrock API进行推理、工具选择和执行

验证过程中，我们尝试在cn-northwest-1和cn-north-1两个中国区域连接Bedrock服务，均遇到endpoint连接失败的问题。这证实了Amazon Bedrock服务目前在AWS中国区域不可用。

**服务可用性比例**：33% (1/3)

由于核心服务不可用，即使IAM服务可用，整个解决方案也无法在中国区域实施。

## 验证结果

### 验证类型

- ✅ GitHub项目部署验证

### 执行状态

**状态**: ❌ 失败

**失败原因**: 核心依赖服务Amazon Bedrock在AWS中国区域不可用

### 关键发现

1. **Amazon Bedrock服务不可用**
   - 在cn-northwest-1和cn-north-1区域均无法连接Bedrock服务endpoint
   - 错误信息：`Could not connect to the endpoint URL: "https://bedrock.cn-northwest-1.amazonaws.com.cn/foundation-models"`
   - 影响：无法使用Claude模型进行LLM推理，整个多智能体系统无法运行

2. **GitHub项目结构分析**
   - 项目包含完整的多智能体实现（supervisor_agent、flight_agent、hotel_agent、destination_agent）
   - 所有agent的graph.py文件都硬编码使用Bedrock客户端
   - 依赖的模型：`anthropic.claude-3-5-sonnet-20240620-v1:0`和`anthropic.claude-3-haiku-20240307-v1:0`

3. **LangGraph框架本身可用**
   - LangGraph是开源框架，可以在中国区域安装和使用
   - 但其价值在于与LLM服务的集成，单独使用意义有限

4. **无法进行修正**
   - 按照验证规则，不允许替换核心服务（Bedrock）
   - Endpoint调整无法解决服务不可用的问题
   - 修正尝试次数：0次（因为服务根本不存在，无修正可能）

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此方案**

由于Amazon Bedrock服务在中国区域不可用，本博客介绍的解决方案无法直接在AWS中国区域部署。建议考虑以下替代方案：

### 替代方案

1. **使用Amazon SageMaker部署开源LLM**
   - 实施方式：在SageMaker上部署开源大语言模型（如Llama 2、ChatGLM等），然后将LangGraph与自部署的模型集成
   - 复杂度：高
   - 适用场景：需要完全控制模型部署和数据隐私的企业场景
   - 注意事项：
     - 需要自行管理模型推理基础设施
     - 需要处理模型许可证和合规性问题
     - 推理成本和性能需要自行优化
     - 需要修改所有agent代码中的LLM客户端实现

2. **使用第三方LLM服务**
   - 实施方式：将LangGraph与在中国可用的第三方LLM API集成（如阿里云通义千问、百度文心一言等）
   - 复杂度：中
   - 适用场景：快速原型开发和测试
   - 注意事项：
     - 需要评估第三方服务的数据隐私和安全政策
     - API接口可能与Bedrock不同，需要适配
     - 服务可用性和性能依赖第三方提供商

3. **在AWS全球区域部署**
   - 实施方式：在支持Bedrock的AWS全球区域（如us-west-2）部署完整方案
   - 复杂度：低
   - 适用场景：数据可以存储在中国境外的场景
   - 注意事项：
     - 需要考虑数据跨境传输的合规性要求
     - 网络延迟可能影响用户体验
     - 可能需要ICP备案等额外手续

### 风险提示

- **服务可用性风险**: Amazon Bedrock在中国区域的上线时间未知，短期内无法使用
- **架构依赖风险**: 博客方案深度依赖Bedrock服务，替换核心服务需要重新设计架构
- **成本风险**: 使用SageMaker自部署模型的成本可能显著高于Bedrock托管服务
- **合规风险**: 使用全球区域或第三方服务需要评估数据合规性要求
- **技术债务风险**: 采用替代方案后，未来迁移到Bedrock可能需要大量重构工作

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/aim323_build_agents_with_bedrock_oss/tree/main/bedrock-multi-agent-langgraph-studio
- **兼容性**: 代码无法在中国区直接使用
- **修改建议**: 
  - 如果采用替代方案1（SageMaker），需要：
    - 替换所有`ChatBedrockConverse`调用为自定义LLM客户端
    - 修改模型初始化代码，指向SageMaker endpoint
    - 调整prompt格式以适配不同模型的要求
  - 如果采用替代方案2（第三方API），需要：
    - 实现LangChain兼容的第三方LLM包装器
    - 适配不同的API调用格式和响应结构
    - 处理token计费和限流逻辑

## 总结

本博客展示了一个优秀的多智能体系统架构设计，使用LangGraph框架实现了supervisor模式的智能体协作。然而，由于核心依赖服务Amazon Bedrock在AWS中国区域不可用，该方案目前无法在中国区域实施。

如果您的业务必须在AWS中国区域运行，建议等待Amazon Bedrock服务在中国区域正式上线，或者考虑使用Amazon SageMaker部署开源模型的替代方案。如果数据合规性允许，在AWS全球区域部署是最简单可行的选择。
