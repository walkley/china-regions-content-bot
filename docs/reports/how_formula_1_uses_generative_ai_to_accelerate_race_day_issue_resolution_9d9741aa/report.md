---
title: Formula 1如何使用生成式AI加速比赛日问题解决
publish_date: 2025-02-18
original_url: https://aws.amazon.com/blogs/machine-learning/how-formula-1-uses-generative-ai-to-accelerate-race-day-issue-resolution/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 10
unavailable_services: 3
---

# Formula 1如何使用生成式AI加速比赛日问题解决

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/how-formula-1-uses-generative-ai-to-accelerate-race-day-issue-resolution/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

该方案的核心依赖Amazon Bedrock及其相关组件（Agents、Knowledge Bases），这些服务在AWS中国区域均不可用，导致整个生成式AI根因分析助手的核心功能无法实现。

## 服务分析

### 可用服务 (10个)

- Amazon CloudWatch
- Amazon S3 (Simple Storage Service)
- Amazon EventBridge
- AWS Glue
- Amazon ECS (Elastic Container Service)
- AWS Fargate
- Amazon EC2 (Elastic Compute Cloud)
- Apache Spark（开源技术）
- Streamlit（开源框架）
- Boto3（AWS SDK）

### 不可用服务 (3个)

- **Amazon Bedrock** - 核心服务
- **Amazon Bedrock Agents** - 核心服务
- **Amazon Bedrock Knowledge Bases** - 核心服务

### 评估说明

虽然可用服务占比达到76.9%，但不可用的三个服务是整个解决方案的核心：

1. **Amazon Bedrock** - 提供基础的生成式AI能力和大语言模型（Claude 3 Sonnet）
2. **Amazon Bedrock Agents** - 实现智能编排、任务分解和工具调用的核心组件
3. **Amazon Bedrock Knowledge Bases** - 提供RAG（检索增强生成）能力，用于查询日志和文档

这三个服务构成了整个RCA（根因分析）助手的AI能力基础。其他可用服务（如S3、Glue、CloudWatch等）仅提供数据存储、转换和监控等支撑功能，无法替代核心的生成式AI能力。

## 验证结果

### 验证类型

- ⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Bedrock及其相关组件在AWS中国区域不可用，即使存在配套GitHub项目（https://github.com/yhou-uk/streamlit-app-for-amazon-bedrock/tree/main），也无法在中国区域部署和运行该方案。

## 实施建议

### 推荐方案

不建议在AWS中国区域直接实施此方案。该解决方案的核心价值在于使用Amazon Bedrock的生成式AI能力来实现智能根因分析，而这一核心能力在中国区域无法获得。

### 替代方案

如果需要在AWS中国区域实现类似的根因分析能力，可以考虑以下替代方案：

1. **使用第三方LLM服务**
   - 实施方式：集成国内可用的大语言模型服务（如阿里云通义千问、百度文心一言等），替代Amazon Bedrock
   - 复杂度：高
   - 适用场景：需要完整的生成式AI根因分析能力，且愿意投入较大开发成本
   - 注意事项：需要重新设计整个AI编排逻辑，包括Agent框架、RAG实现、工具调用机制等

2. **传统规则引擎方案**
   - 实施方式：使用AWS Step Functions + Lambda构建基于规则的故障诊断流程，结合CloudWatch Logs Insights进行日志分析
   - 复杂度：中
   - 适用场景：故障模式相对固定，可以预定义诊断规则和流程
   - 注意事项：缺乏生成式AI的灵活性和自然语言交互能力，需要维护大量规则

3. **混合方案**
   - 实施方式：保留数据处理管道（S3、Glue、EventBridge），使用AWS Lambda调用外部LLM API，实现部分智能分析能力
   - 复杂度：中到高
   - 适用场景：希望保留部分AI能力，但不需要完整的Agent编排功能
   - 注意事项：需要处理外部API调用的延迟、成本和数据安全问题

### 风险提示

- **核心功能缺失**: 无法使用Amazon Bedrock的生成式AI能力，失去方案的核心价值
- **开发成本高**: 替代方案需要大量自定义开发，技术复杂度显著增加
- **维护难度大**: 第三方LLM集成需要持续维护和适配，增加运维负担
- **数据合规性**: 使用外部LLM服务需要考虑数据出境和隐私合规问题
- **性能差异**: 替代方案可能无法达到原方案使用Claude 3 Sonnet的性能水平

### 配套资源

- **GitHub仓库**: https://github.com/yhou-uk/streamlit-app-for-amazon-bedrock/tree/main
- **兼容性**: 不兼容AWS中国区域
- **修改建议**: 该仓库是基于Amazon Bedrock构建的Streamlit聊天应用，核心依赖Amazon Bedrock Agents。如需在中国区域使用，需要完全重构AI后端，替换为可用的LLM服务，工作量巨大且技术风险高。
