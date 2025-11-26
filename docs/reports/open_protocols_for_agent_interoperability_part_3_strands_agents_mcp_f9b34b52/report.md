---
title: 开放协议实现Agent互操作性第3部分：Strands Agents与MCP
publish_date: 2025-07-10
original_url: https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-3-strands-agents-mcp/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 5
unavailable_services: 1
---

# 开放协议实现Agent互操作性第3部分：Strands Agents与MCP

[📖 查看原始博客](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-3-strands-agents-mcp/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心AI推理服务Amazon Bedrock在中国区域不可用，需要替换为其他LLM服务，涉及架构级修改

该博客展示了如何使用Strands Agents SDK和Model Context Protocol (MCP)构建多Agent协作系统。虽然基础设施服务（ECS、Fargate、Lambda等）在中国区域可用，但核心的AI推理服务Amazon Bedrock不可用，这是整个系统运行的基础，无法通过简单配置调整解决。

## 服务分析

### 可用服务 (5个)

- AWS Lambda
- AWS Fargate
- Amazon ECS
- Elastic Load Balancing
- AWS CloudFormation

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务，用于AI推理（示例使用Nova Micro模型）

### 评估说明

虽然可用服务占比达到83.3%，但Amazon Bedrock是整个Agent系统的核心推理引擎，所有Agent的智能决策都依赖于它。示例代码中硬编码使用了：
- 模型：`amazon.nova-micro-v1:0`
- 区域：`us-east-1`

这不是简单的endpoint或区域配置问题，而是需要替换整个AI推理服务，属于架构级修改。中国区域虽然有其他LLM服务选项（如自部署模型、第三方API等），但需要重写Agent的模型调用逻辑。

## 验证结果

### 验证类型

- ✅ GitHub项目部署验证

### 执行状态

**状态**: ❌ 失败

**原因**: 核心服务Amazon Bedrock在中国区域不可用，代码中硬编码使用Bedrock API和Nova模型。替换为其他LLM服务需要修改核心架构和功能逻辑，超出允许的修正范围（endpoint调整、区域配置、网络优化）。

### 关键发现

1. **核心依赖不可用**
   - 项目完全依赖Amazon Bedrock作为AI推理引擎
   - 代码中使用 `BedrockModel` 类和 `amazon.nova-micro-v1:0` 模型
   - 无法通过配置调整解决，需要替换整个推理服务

2. **架构耦合度高**
   - Strands Agents SDK与Bedrock深度集成
   - 三个组件（employee-server、employee-agent、hr-agent）都依赖Bedrock
   - 替换推理服务需要重写Agent初始化和调用逻辑

3. **区域硬编码**
   - 代码中硬编码 `region_name="us-east-1"`
   - 即使调整为中国区域，Bedrock服务仍不可用

## 实施建议

### 推荐方案

**不建议直接实施**

该示例的核心价值在于展示MCP协议如何实现Agent间通信，但由于依赖中国区域不可用的Bedrock服务，无法直接部署。如果希望在中国区域实现类似功能，需要进行重大架构调整。

### 替代方案

1. **使用自部署开源LLM**
   - 实施方式：在ECS/EKS上部署开源模型（如Llama、Qwen等），修改Strands Agents代码以支持自定义模型endpoint
   - 复杂度：高
   - 适用场景：有足够的技术团队和计算资源，需要完全控制模型部署
   - 额外成本：需要GPU实例（如p3、g4dn等）

2. **集成第三方LLM API**
   - 实施方式：修改Agent代码，将Bedrock调用替换为国内可用的LLM API（如阿里云通义千问、百度文心一言等）
   - 复杂度：中
   - 适用场景：快速验证概念，不需要自建模型基础设施
   - 注意事项：需要评估第三方API的稳定性、成本和数据隐私政策

3. **学习MCP协议概念**
   - 实施方式：将此博客作为学习资料，理解MCP协议和Agent间通信模式，但不实际部署
   - 复杂度：低
   - 适用场景：学习和研究目的，等待Bedrock在中国区域上线后再实施

### 风险提示

- **服务可用性风险**: Amazon Bedrock目前在中国区域不可用，未来上线时间不确定
- **架构修改风险**: 替换推理服务需要深度修改代码，可能引入新的bug和兼容性问题
- **成本风险**: 自部署LLM需要昂贵的GPU实例，成本可能远高于托管服务
- **维护复杂度**: 自建LLM基础设施需要专业的运维团队和持续维护
- **性能差异**: 替代方案的推理性能和质量可能与Bedrock Nova模型存在差异

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/sample-agentic-ai-demos/tree/main/modules/strands-mcp-inter-agent
- **兼容性**: 不兼容中国区域，核心依赖Bedrock服务
- **修改建议**: 
  1. 替换 `BedrockModel` 为支持自定义endpoint的模型类
  2. 修改所有Agent代码中的模型初始化逻辑
  3. 调整CloudFormation模板，添加GPU实例支持（如使用自部署模型）
  4. 更新环境变量配置，支持自定义LLM endpoint
  5. 测试并验证替代LLM的推理质量和性能

---

**验证说明**: 本报告基于2025-11-25的服务可用性状态。AWS服务在中国区域的可用性可能随时间变化，建议在实施前再次确认最新的服务状态。
