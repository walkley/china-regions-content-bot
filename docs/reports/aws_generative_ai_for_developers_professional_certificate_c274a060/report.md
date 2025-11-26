---
title: AWS开发者生成式AI专业证书
publish_date: 2025-07-22
original_url: https://aws.amazon.com/blogs/training-and-certification/aws-generative-ai-for-developers-professional-certificate/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 1
unavailable_services: 2
---

# AWS开发者生成式AI专业证书

[📖 查看原始博客](https://aws.amazon.com/blogs/training-and-certification/aws-generative-ai-for-developers-professional-certificate/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，无法实施

该培训课程完全依赖Amazon Bedrock和Amazon Q Developer两个核心服务，这两个服务目前在AWS中国区域均不可用，导致课程内容无法在中国区实施。

## 服务分析

### 可用服务 (1个)

- AWS Management Console

### 不可用服务 (2个)

- **Amazon Bedrock** - 核心服务
- **Amazon Q Developer** - 核心服务

### 评估说明

本课程是AWS推出的生成式AI开发者专业证书培训项目，包含三门课程：

1. **Getting Started with AWS Generative AI for Developers** - 学习使用Amazon Bedrock APIs调用基础模型
2. **Generative AI Applications with Amazon Bedrock** - 深入学习Amazon Bedrock Knowledge Bases、Prompt Management、Flows和Agents
3. **Amazon Bedrock Customization, Optimization & Automation** - 学习模型定制、优化和自动化

整个课程体系完全围绕Amazon Bedrock和Amazon Q Developer构建，这两个服务是课程的绝对核心：

- **Amazon Bedrock**：课程的主要技术平台，涵盖Runtime APIs、Knowledge Bases、Prompt Management、Flows、Agents、Evaluations、Data Automation等所有功能模块
- **Amazon Q Developer**：课程中用于演示AI辅助软件开发和命令行自动化的核心工具

由于这两个核心服务在中国区不可用，课程中的所有实践内容（包括Python Jupyter notebook实验和AWS Console操作）都无法在中国区域执行。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Bedrock和Amazon Q Developer在AWS中国区域不可用，课程内容完全依赖这两个服务，无实施可能性，因此跳过深入验证。

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此培训课程**

该课程是专门针对Amazon Bedrock和Amazon Q Developer的培训项目，没有可行的替代方案能够保持课程的完整性和学习目标。建议：

1. **使用AWS全球区域账号学习**：如果目标是学习生成式AI开发技能，建议使用AWS全球区域（如us-east-1）的账号进行课程学习
2. **关注中国区域服务更新**：持续关注AWS中国区域的服务发布计划，等待Amazon Bedrock服务在中国区域上线

### 替代方案

目前没有在AWS中国区域实现等效学习效果的替代方案。如需在中国区域学习生成式AI相关技术，可考虑：

1. **其他云服务商的生成式AI服务**
   - 实施方式：使用国内云服务商提供的大模型服务和AI开发平台
   - 复杂度：中
   - 适用场景：需要在中国区域部署生成式AI应用的场景

2. **自建模型推理服务**
   - 实施方式：在AWS中国区域的EC2或EKS上部署开源大模型（如Llama、ChatGLM等）
   - 复杂度：高
   - 适用场景：有足够技术能力和资源，需要完全自主控制的场景

### 风险提示

- **学习目标无法达成**：课程设计的所有学习目标和实践环节都无法在中国区域完成
- **证书获取受限**：即使完成理论学习，缺少实践环节可能影响证书获取
- **技能应用受限**：即使在全球区域学习了相关技能，也无法直接应用到中国区域的项目中

### 配套资源

- **课程平台**: [Coursera](https://www.coursera.org/professional-certificates/aws-generative-ai-developers) 和 [edX](https://www.edx.org/certificates/professional-certificate/aws-generative-ai-for-developers)
- **兼容性**: 课程内容不适用于AWS中国区域
- **修改建议**: 无法通过修改使其适配中国区域，建议使用AWS全球区域账号学习
