---
title: Strands Agents 1.0发布：生产就绪的多智能体编排变得简单
publish_date: 2025-07-15
original_url: https://aws.amazon.com/blogs/opensource/introducing-strands-agents-1-0-production-ready-multi-agent-orchestration-made-simple/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: MODERATE
available_services: 2
unavailable_services: 2
---

# Strands Agents 1.0发布：生产就绪的多智能体编排变得简单

[📖 查看原始博客](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-1-0-production-ready-multi-agent-orchestration-made-simple/) | 验证日期: 2025-11-25

## 可行性评估

!!! warning "MODERATE - 谨慎实施"
    核心SDK架构完全可用，但需要使用第三方模型API替代Amazon Bedrock

Strands Agents SDK是一个开源的AI智能体框架，其核心架构、多智能体原语和会话管理功能在AWS中国区域完全可用。虽然默认的Amazon Bedrock模型提供商在中国区不可用，但SDK支持多种第三方模型API（OpenAI、Anthropic、Ollama等），可以完全替代Bedrock实现所有功能。

## 服务分析

### 可用服务 (2个)

- Amazon S3 - 用于会话持久化存储
- AWS Glue - 仅作为参考案例提及

### 不可用服务 (2个)

- **Amazon Bedrock** - 核心服务，SDK默认模型提供商
- **Amazon Q Developer** - 仅作为参考案例提及

### 评估说明

**核心服务可用性分析**：

1. **Amazon Bedrock（不可用但可替代）**：
   - Bedrock是SDK的默认模型提供商，在中国区不可用
   - SDK设计为模型无关架构，支持多种模型提供商
   - 可使用OpenAI、Anthropic、Cohere、Mistral等第三方API
   - 可使用Ollama、llama.cpp等本地模型
   - 替代方案完全不影响SDK的核心功能

2. **Amazon S3（可用）**：
   - S3在中国区完全可用
   - 支持会话持久化和状态管理
   - 生产环境的关键存储服务

3. **参考案例服务**：
   - Q Developer和Glue仅作为使用案例提及
   - 不影响SDK本身的功能和可用性

## 验证结果

### 验证类型

✅ GitHub项目部署验证

### 执行状态

**状态**: ✅ 成功

**验证环境**：
- AWS区域：cn-northwest-1
- Python版本：3.12.12
- SDK版本：strands-agents 1.18.0

### 关键发现

1. **核心架构完全可用**
   - SDK核心模块（Agent、tool装饰器）成功导入和运行
   - 工具系统（内置工具、自定义工具）功能正常
   - 无需任何修改即可使用核心功能

2. **多智能体原语功能正常**
   - Agents-as-Tools（智能体作为工具）：可用
   - Handoffs（控制权移交）：可用
   - Swarms（自组织协作团队）：可用
   - Graphs（确定性工作流控制）：可用
   - 所有多智能体模式均可在中国区域使用

3. **会话管理系统可用**
   - FileSessionManager（文件会话管理器）：测试通过
   - S3SessionManager（S3会话管理器）：类可用，S3服务在中国区可用
   - 支持生产环境的状态持久化需求

4. **模型提供商灵活性**
   - SDK支持多种模型提供商
   - 可使用第三方API（OpenAI、Anthropic等）
   - 可使用本地模型（Ollama、llama.cpp）
   - 模型切换不影响工具和业务逻辑

5. **A2A协议支持**
   - Agent-to-Agent协议类可用
   - 支持跨平台智能体通信
   - 可与外部组织的智能体集成

## 实施建议

### 推荐方案

**可以在中国区域实施，但需要调整模型提供商配置**

**实施步骤**：

1. **安装SDK**
   ```bash
   pip install strands-agents strands-agents-tools
   ```

2. **选择模型提供商**（以下任选其一）：
   
   **方案A：使用OpenAI API**
   ```python
   from strands import Agent
   from strands.models.openai import OpenAIModel
   
   model = OpenAIModel(
       client_args={"api_key": "your-api-key"},
       model_id="gpt-4o",
       params={"temperature": 0.7}
   )
   agent = Agent(model=model, tools=[...])
   ```
   
   **方案B：使用Anthropic API**
   ```python
   from strands import Agent
   from strands.models.anthropic import AnthropicModel
   
   model = AnthropicModel(
       client_args={"api_key": "your-api-key"},
       model_id="claude-3-7-sonnet-20250219",
       params={"temperature": 0.5}
   )
   agent = Agent(model=model, tools=[...])
   ```
   
   **方案C：使用本地Ollama**
   ```python
   from strands import Agent
   from strands.models.ollama import OllamaModel
   
   model = OllamaModel(
       host="http://localhost:11434",
       model_id="llama3"
   )
   agent = Agent(model=model, tools=[...])
   ```

3. **配置S3会话持久化**（可选，用于生产环境）：
   ```python
   from strands import Agent
   from strands.session.s3_session_manager import S3SessionManager
   
   session_manager = S3SessionManager(
       session_id="my_session",
       bucket="my-bucket-name",
       region_name="cn-northwest-1"
   )
   
   agent = Agent(
       id="my_agent",
       session_manager=session_manager,
       model=model,
       tools=[...]
   )
   ```

4. **使用多智能体模式**：
   - 所有博客中介绍的模式（Agents-as-Tools、Swarms、Graphs）均可直接使用
   - 无需修改代码逻辑，只需配置模型提供商

### 替代方案

1. **OpenAI API**
   - 实施方式：使用OpenAI官方API或兼容的API服务
   - 复杂度：低
   - 适用场景：需要高质量模型且可接受API调用成本

2. **Anthropic Claude API**
   - 实施方式：使用Anthropic官方API
   - 复杂度：低
   - 适用场景：需要Claude系列模型的特定能力

3. **本地Ollama部署**
   - 实施方式：在本地或EC2实例上部署Ollama
   - 复杂度：中
   - 适用场景：需要数据隐私、离线运行或降低API成本

4. **LiteLLM代理**
   - 实施方式：使用LiteLLM统一多个模型提供商
   - 复杂度：中
   - 适用场景：需要在多个模型之间灵活切换

### 风险提示

- **模型API成本**：使用第三方模型API会产生调用费用，需要评估成本
- **网络连接**：访问国外API服务可能需要考虑网络连接稳定性
- **数据合规**：使用第三方API需要确保符合数据隐私和合规要求
- **API限流**：第三方API可能有调用频率限制，需要实现重试和限流机制

### 配套资源

- **GitHub仓库**: https://github.com/strands-agents/sdk-python
- **示例仓库**: https://github.com/strands-agents/samples
- **官方文档**: https://strandsagents.com/
- **兼容性**: SDK核心功能在中国区完全可用
- **修改建议**: 
  - 将默认的BedrockModel替换为其他模型提供商
  - 其他代码无需修改
  - 所有工具、多智能体模式、会话管理功能保持不变

### 实施工作量评估

- **开发工作量**：低
  - 只需修改模型提供商配置
  - 核心业务逻辑无需改动
  
- **测试工作量**：低到中
  - 需要测试不同模型提供商的效果
  - 验证多智能体协作功能
  
- **部署工作量**：低
  - 标准Python应用部署流程
  - 如使用S3会话管理，需配置S3访问权限

### 最佳实践建议

1. **模型选择**：
   - 开发测试阶段：使用Ollama本地模型，降低成本
   - 生产环境：根据性能和成本需求选择OpenAI或Anthropic

2. **会话管理**：
   - 开发环境：使用FileSessionManager
   - 生产环境：使用S3SessionManager实现持久化

3. **监控和日志**：
   - 启用SDK的调试日志：`logging.getLogger("strands").setLevel(logging.DEBUG)`
   - 监控模型API调用次数和成本
   - 记录智能体决策过程便于调试

4. **性能优化**：
   - 使用异步API（`stream_async`）提升响应速度
   - 合理设置工具超时时间
   - 对频繁使用的工具实现缓存

5. **安全考虑**：
   - 不要在代码中硬编码API密钥
   - 使用环境变量或密钥管理服务
   - 对用户输入进行验证和清理
