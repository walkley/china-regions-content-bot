---
title: 使用CrewAI和Amazon Bedrock构建智能体系统
publish_date: 2025-03-31
original_url: https://aws.amazon.com/blogs/machine-learning/build-agentic-systems-with-crewai-and-amazon-bedrock/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 10
unavailable_services: 1
---

# 使用CrewAI和Amazon Bedrock构建智能体系统

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/build-agentic-systems-with-crewai-and-amazon-bedrock/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Bedrock在中国区域不可用，无法实施

虽然90.9%的服务在中国区域可用，但Amazon Bedrock作为整个解决方案的核心基础服务不可用，导致方案无法实施。

## 服务分析

### 可用服务 (10个)

- Amazon CloudWatch
- AWS Lambda
- Amazon ECS (Elastic Container Service)
- Amazon EC2 (Elastic Compute Cloud)
- Amazon S3
- Amazon IAM
- Amazon RDS
- Amazon VPC
- Amazon Bedrock Agents
- Amazon Bedrock Knowledge Bases

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务

### 评估说明

Amazon Bedrock是本文的核心服务，整篇博客的主题就是"使用CrewAI和Amazon Bedrock构建智能体系统"。该服务提供以下关键能力：

1. **基础模型访问**：提供Anthropic Claude、Amazon Nova等先进语言模型的访问能力，这是CrewAI智能体进行决策、理解复杂指令和生成响应的认知基础
2. **企业级安全与合规**：为组织提供严格的数据控制和合规性保障
3. **可扩展性和可靠性**：基于AWS基础设施的稳定性保障

文章中的所有代码示例、架构设计和实施方案都依赖于Amazon Bedrock作为LLM提供者。没有Amazon Bedrock：
- CrewAI智能体无法获得语言模型能力
- 文章中的安全审计示例无法运行
- 多智能体协作系统无法构建

虽然其他基础设施服务（EC2、S3、IAM等）都可用，但它们只是支撑服务，无法替代Amazon Bedrock的核心功能。

## 验证结果

### 验证类型

⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Bedrock在AWS中国区域不可用，即使其他支撑服务可用，也无法实现文章描述的CrewAI智能体系统。深入验证无实际意义。

## 实施建议

### 推荐方案

不建议在AWS中国区域直接实施此方案。Amazon Bedrock的缺失使得整个CrewAI智能体系统无法按照文章描述的方式构建和运行。

### 替代方案

1. **使用其他LLM服务提供商**
   - 实施方式：将CrewAI配置为使用中国区域可用的其他LLM服务（如阿里云通义千问、百度文心一言等）
   - 复杂度：中
   - 适用场景：需要在中国区域实现类似智能体功能，但可以接受使用非AWS的LLM服务
   - 注意事项：需要修改所有LLM配置代码，可能面临API兼容性、性能和合规性差异

2. **等待Amazon Bedrock在中国区域上线**
   - 实施方式：关注AWS中国区域服务更新，待Amazon Bedrock正式上线后再实施
   - 复杂度：低
   - 适用场景：对AWS生态系统有强依赖，希望使用原生AWS服务
   - 注意事项：上线时间不确定，可能需要较长等待期

3. **使用自托管开源模型**
   - 实施方式：在Amazon EC2或Amazon ECS上部署开源LLM（如Llama、Mistral等），CrewAI连接到自托管模型
   - 复杂度：高
   - 适用场景：有较强的技术团队，对数据隐私有严格要求，愿意承担模型运维成本
   - 注意事项：需要处理模型部署、优化、监控等复杂问题，成本可能较高

### 风险提示

- **服务依赖风险**：整个方案高度依赖Amazon Bedrock，该服务在中国区域的可用性直接决定方案可行性
- **替代方案局限性**：使用其他LLM服务可能面临API不兼容、性能差异、数据合规等问题
- **成本风险**：自托管模型方案可能产生较高的基础设施和运维成本
- **技术复杂度**：CrewAI框架本身的学习曲线，加上替代方案的额外复杂性，可能延长项目实施周期

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/3P-Agentic-Frameworks/tree/main/crewai/aws-security-auditor-crew
- **兼容性**: 代码无法在中国区直接使用，因为所有示例都配置为使用Amazon Bedrock作为LLM提供者
- **修改建议**: 
  - 需要修改所有LLM初始化代码，替换为可用的LLM服务
  - 需要调整认证和配置方式以适配新的LLM提供商
  - 需要测试CrewAI与替代LLM服务的兼容性和性能表现
