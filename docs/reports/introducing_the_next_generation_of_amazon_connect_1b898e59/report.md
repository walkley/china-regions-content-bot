---
title: 介绍下一代Amazon Connect：AI驱动的交互增强客户关系并改善业务成果
publish_date: 2025-03-18
original_url: https://aws.amazon.com/blogs/contact-center/introducing-the-next-generation-of-amazon-connect/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 0
unavailable_services: 4
---

# 介绍下一代Amazon Connect：AI驱动的交互增强客户关系并改善业务成果

[📖 查看原始博客](https://aws.amazon.com/blogs/contact-center/introducing-the-next-generation-of-amazon-connect/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

本文介绍的Amazon Connect及其所有AI功能在AWS中国区域均不可用，包括核心服务Amazon Connect、Amazon Bedrock、Amazon Q in Connect和Contact Lens，无法在中国区域实施。

## 服务分析

### 可用服务 (0个)

无

### 不可用服务 (4个)

- **Amazon Connect** - 核心服务
- **Amazon Bedrock** - 核心服务
- **Amazon Q Business (Amazon Q in Connect)** - 核心服务
- **Contact Lens** - 核心功能

### 评估说明

本文的核心主题是Amazon Connect的新一代AI功能发布，所有涉及的服务和功能在AWS中国区域均不可用：

1. **Amazon Connect**：文章的核心服务，是AWS的云联络中心解决方案，在中国区域不可用
2. **Amazon Bedrock**：为Amazon Connect提供AI模型支持，在中国区域不可用
3. **Amazon Q in Connect**：代理助手功能，属于Amazon Q Business服务范畴，在中国区域不可用
4. **Contact Lens**：对话分析、情感分析、质量管理等功能，是Amazon Connect的核心组件，在中国区域不可用

由于所有核心服务均不可用，且这些服务高度集成，没有直接的替代方案可以实现相同的功能体验。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证显示所有核心服务在中国区域均不可用（可用率0%），可行性评估为LOW，不满足深入验证的触发条件。

## 实施建议

### 推荐方案

不建议在AWS中国区域实施本文介绍的方案。Amazon Connect及其所有AI功能在中国区域完全不可用，无法通过简单调整或配置实现。

### 替代方案

如需在中国区域构建类似的AI驱动联络中心解决方案，可考虑以下替代方案：

1. **自建联络中心方案**
   - 实施方式：使用Amazon EC2、Amazon ECS等计算服务，结合开源联络中心软件（如Asterisk、FreeSWITCH）自建联络中心平台
   - 复杂度：高
   - 适用场景：有较强技术团队，需要完全自主控制的场景

2. **第三方联络中心服务**
   - 实施方式：使用在中国区域可用的第三方云联络中心服务提供商
   - 复杂度：中
   - 适用场景：希望使用托管服务，但不依赖AWS特定服务的场景

3. **混合架构方案**
   - 实施方式：在AWS中国区域使用可用的AI服务（如自建NLP模型）结合第三方联络中心平台
   - 复杂度：高
   - 适用场景：需要定制化AI能力，同时希望利用AWS中国区域其他服务的场景

### 风险提示

- **服务不可用风险**：Amazon Connect及相关AI服务在中国区域完全不可用，无法直接使用
- **功能差异风险**：替代方案无法完全复制Amazon Connect的原生AI集成体验和统一定价模式
- **技术复杂度风险**：自建方案需要大量技术投入和运维成本
- **合规性风险**：联络中心涉及通信和数据合规要求，需确保替代方案符合中国相关法规

### 配套资源

文章中提到的GitHub资源均为文档和API参考，不是可部署的项目代码：
- Amazon Connect User Guide（用户指南文档）
- Amazon Connect Admin Guide（管理员指南文档）
- Amazon Connect Streams API（API参考文档）

这些资源仅供参考学习，无法在中国区域实际使用。
