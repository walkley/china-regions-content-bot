---
title: Amazon Bedrock 现已可供合作伙伴转售
publish_date: 2025-10-14
original_url: https://aws.amazon.com/blogs/apn/amazon-bedrock-now-available-for-partner-resale/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 0
unavailable_services: 1
---

# Amazon Bedrock 现已可供合作伙伴转售

[📖 查看原始博客](https://aws.amazon.com/blogs/apn/amazon-bedrock-now-available-for-partner-resale/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，无法在中国区域实施

Amazon Bedrock 服务在 AWS 中国区域不可用，这是一篇关于合作伙伴转售计划的商业公告，不涉及技术实施内容。

## 服务分析

### 可用服务 (0个)

无

### 不可用服务 (1个)

- **Amazon Bedrock** - 核心服务
  - Amazon Nova（Bedrock 模型系列）
  - Amazon Titan（Bedrock 模型系列）

### 评估说明

1. **核心服务不可用**：Amazon Bedrock 是本文的唯一核心服务，目前在 AWS 中国区域（北京和宁夏）均不可用。

2. **内容性质**：这是一篇面向 AWS 合作伙伴的商业公告，宣布 Amazon Bedrock 加入授权服务列表，可由 AWS 解决方案提供商和分销商合作伙伴进行转售。文章不包含技术实施步骤或代码示例。

3. **无替代方案**：Amazon Bedrock 提供的多模型基础模型访问能力（包括 AI21、Anthropic、Cohere、Meta、Mistral、OpenAI 等提供商的模型）在中国区域没有直接的 AWS 服务替代方案。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务 Amazon Bedrock 在中国区域不可用，且文章为商业公告性质，不包含技术实施内容，无需进行深入验证。

## 实施建议

### 推荐方案

**不建议在中国区域实施**

由于 Amazon Bedrock 服务在 AWS 中国区域不可用，本文描述的合作伙伴转售计划无法在中国区域开展。

### 替代方案

如需在中国区域使用生成式 AI 能力，可考虑以下替代方案：

1. **使用国内大模型服务**
   - 实施方式：集成国内云服务商提供的大模型 API（如阿里云通义千问、腾讯云混元、百度文心一言等）
   - 复杂度：中
   - 适用场景：需要在中国境内合规运营的生成式 AI 应用

2. **自建模型服务**
   - 实施方式：在 AWS 中国区域使用 Amazon SageMaker 部署开源大模型（如 Llama、Qwen 等）
   - 复杂度：高
   - 适用场景：对数据隐私有严格要求，需要完全自主控制的场景

3. **混合架构**
   - 实施方式：核心业务在中国区域运行，AI 推理服务部署在 AWS 全球区域（需考虑数据合规和网络延迟）
   - 复杂度：高
   - 适用场景：对延迟不敏感且数据可出境的应用场景

### 风险提示

- **服务不可用**: Amazon Bedrock 及其所有模型（包括 Amazon Nova、Amazon Titan 以及第三方模型）在中国区域均不可用
- **商业模式限制**: AWS 合作伙伴转售计划在中国区域的运作模式可能与全球区域有所不同
- **数据合规**: 使用全球区域的 AI 服务需要考虑中国的数据出境和隐私保护相关法规
- **网络连接**: 跨境访问全球区域服务可能面临网络延迟和稳定性问题

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 不适用
