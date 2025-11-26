---
title: 发布AWS Well-Architected生成式AI框架
publish_date: 2025-04-17
original_url: https://aws.amazon.com/blogs/architecture/announcing-the-aws-well-architected-generative-ai-lens/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 4
unavailable_services: 0
---

# 发布AWS Well-Architected生成式AI框架

[📖 查看原始博客](https://aws.amazon.com/blogs/architecture/announcing-the-aws-well-architected-generative-ai-lens/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

这是一篇纯公告性博客，介绍AWS Well-Architected Generative AI Lens框架文档。所有提到的服务和工具在AWS中国区域完全可用，内容可直接应用于中国区的生成式AI架构设计。

## 服务分析

### 可用服务 (4个)

- AWS Well-Architected Framework
- AWS Well-Architected Tool
- AWS Solutions Architecture
- AWS Professional Services

### 不可用服务 (0个)

无

### 评估说明

本文介绍的AWS Well-Architected Generative AI Lens是一个架构设计框架和最佳实践指南，不涉及具体的AWS服务部署。文中提到的所有相关服务和工具在AWS中国区域均可用：

1. **Well-Architected Framework**：这是AWS的架构最佳实践框架，在全球和中国区域通用
2. **Well-Architected Tool**：该工具在中国区域可用，可用于评估和审查架构
3. **专业服务和解决方案架构**：AWS中国区域提供相应的支持服务

该框架提供的六大支柱（运营卓越、安全性、可靠性、性能效率、成本优化、可持续性）和生成式AI生命周期的六个阶段指导，均为云无关的最佳实践，完全适用于中国区域。

## 验证结果

### 验证类型

- ⏭️ 已跳过（无需实际验证）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 这是一篇纯公告性博客，介绍概念性框架文档，不包含具体的技术实施步骤或配套代码项目。Well-Architected Lens是指导性文档，无需进行实际部署验证。

### 关键发现

无需实际验证，但有以下重要说明：

1. **框架文档可用性**
   - AWS Well-Architected Generative AI Lens文档在中国区可访问
   - 可通过AWS中国区的文档站点获取相关内容

2. **工具可用性**
   - AWS Well-Architected Tool在中国区域控制台可用
   - 可用于对生成式AI工作负载进行架构审查

## 实施建议

### 推荐方案

可直接按照原文实施，该框架完全适用于AWS中国区域的生成式AI架构设计。

**注意事项：**
- Well-Architected Framework的设计原则和最佳实践是云无关的，可直接应用
- 在使用Well-Architected Tool进行架构审查时，需要访问AWS中国区域控制台
- 框架中提到的某些具体AWS服务（如Amazon Bedrock等生成式AI服务）在中国区可能不可用，在实际应用时需要注意服务可用性
- 建议结合中国区域的实际服务可用性，调整具体的技术实施方案

### 应用场景

该框架特别适用于以下场景：

1. **架构设计阶段**：在设计生成式AI工作负载时，使用该框架指导架构决策
2. **架构审查**：对现有的生成式AI应用进行Well-Architected审查
3. **持续改进**：在生产环境中持续优化生成式AI工作负载

### 目标受众

- **业务领导者**：了解生成式AI的端到端实施和价值
- **数据科学家和工程师**：理解如何大规模使用、保护和获取数据洞察
- **风险和合规负责人**：了解如何负责任地实施生成式AI并满足监管要求

### 风险提示

- **服务可用性差异**：框架中的实施指导可能引用某些在中国区不可用的AWS服务（如Amazon Bedrock、Amazon Kendra等），需要寻找替代方案
- **文档访问**：确保团队能够访问AWS中国区的Well-Architected文档资源
- **专业支持**：如需专业支持，应联系AWS中国区的解决方案架构师或客户代表

### 配套资源

- **官方文档**: [AWS Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html)
- **相关框架**: [AWS Well-Architected Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html)
- **兼容性**: 框架文档完全适用于中国区，但具体实施时需注意服务可用性
- **使用建议**: 将该框架作为架构设计和审查的指导原则，结合中国区实际可用服务进行技术选型
