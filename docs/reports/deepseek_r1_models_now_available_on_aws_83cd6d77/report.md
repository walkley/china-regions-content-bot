---
title: DeepSeek-R1模型现已在AWS上可用
publish_date: 2025-01-30
original_url: https://aws.amazon.com/blogs/aws/deepseek-r1-models-now-available-on-aws/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 14
unavailable_services: 6
---

# DeepSeek-R1模型现已在AWS上可用

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/deepseek-r1-models-now-available-on-aws/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Bedrock在中国区不可用，博客介绍的4种部署方式中有3种无法使用

博客重点介绍的Amazon Bedrock Marketplace、Amazon Bedrock Custom Model Import等核心部署方式在中国区完全不可用，仅有部分替代方案可行，需要完全不同的实施路径。

## 服务分析

### 可用服务 (14个)

- Amazon SageMaker AI
- Amazon SageMaker JumpStart
- Amazon SageMaker Pipelines
- Amazon SageMaker Debugger
- Amazon SageMaker Model Registry
- Amazon SageMaker Unified Studio
- Amazon SageMaker Studio
- Amazon EC2
- Amazon EKS
- Amazon S3
- AWS Deep Learning AMIs
- GPU实例 (P3, G4dn, G5系列)

### 不可用服务 (6个)

- **Amazon Bedrock** - 核心服务
- **Amazon Bedrock Marketplace** - 核心服务
- **Amazon Bedrock Guardrails** - 核心服务
- **Amazon Bedrock Custom Model Import** - 核心服务
- **Amazon Bedrock Agents** - 核心服务
- **Amazon Bedrock Knowledge Bases** - 核心服务
- **AWS Trainium (Trn1实例)** - 博客推荐的成本优化方案
- **AWS Inferentia (Inf2实例)** - 博客推荐的成本优化方案

### 评估说明

1. **核心服务不可用**：博客的主要内容围绕Amazon Bedrock展开，介绍了4种部署方式：
   - ❌ Amazon Bedrock Marketplace（不可用）
   - ✅ Amazon SageMaker JumpStart（可用，但需验证模型支持）
   - ❌ Amazon Bedrock Custom Model Import（不可用）
   - ⚠️ Amazon EC2 with Trainium/Inferentia（实例类型不可用，需使用GPU替代）

2. **成本优化方案受限**：博客强调的AWS Trainium和Inferentia芯片在中国区不可用，这是DeepSeek-R1的主要成本优势所在

3. **安全防护缺失**：Amazon Bedrock Guardrails在中国区不可用，无法使用博客推荐的模型安全防护机制

## 验证结果

### 验证类型

- ✅ 教程步骤验证

### 执行状态

**状态**: ⚠️ 部分成功

**说明**: 完成了中国区可用服务的验证，发现关键限制

### 关键发现

1. **Amazon Bedrock完全不可用**
   - 博客中3种主要部署方式（Bedrock Marketplace、Custom Model Import、Guardrails）在中国区无法使用
   - 这占据了博客内容的约75%篇幅
   - 影响：无法按照博客主要推荐方式部署

2. **AWS Trainium和Inferentia实例不可用**
   - 验证结果：cn-northwest-1区域无Trn1和Inf2实例
   - 可用替代：P3、G4dn、G5系列GPU实例
   - 影响：成本显著增加，失去博客强调的"90-95%成本优势"

3. **SageMaker JumpStart模型支持未知**
   - SageMaker服务在中国区可用
   - 但DeepSeek-R1模型是否在中国区JumpStart中提供需要进一步确认
   - JumpStart模型目录在不同区域可能有差异

4. **安全防护机制缺失**
   - Amazon Bedrock Guardrails不可用
   - 需要自行实现内容过滤和安全控制
   - 增加了开发和维护成本

## 实施建议

### 推荐方案

**不建议直接按照博客实施**，原因如下：

1. 博客核心内容（Amazon Bedrock相关）在中国区不适用
2. 推荐的成本优化方案（Trainium/Inferentia）无法使用
3. 需要完全不同的技术路径和更高的实施成本

### 替代方案

如确实需要在中国区部署DeepSeek-R1模型，可考虑以下方案：

1. **方案1：Amazon SageMaker + GPU实例**
   - 实施方式：
     - 从Hugging Face下载DeepSeek-R1或Distill模型
     - 使用SageMaker自定义容器部署
     - 选择G5或P3实例类型
   - 复杂度：中
   - 适用场景：需要企业级管理和监控
   - 成本：高（GPU实例成本显著高于Trainium/Inferentia）

2. **方案2：Amazon EC2 + vLLM**
   - 实施方式：
     - 启动GPU实例（G5.12xlarge或更大）
     - 使用Deep Learning AMI
     - 通过vLLM部署模型
   - 复杂度：中
   - 适用场景：需要更多自定义控制
   - 成本：高

3. **方案3：Amazon EKS + GPU节点**
   - 实施方式：
     - 创建EKS集群
     - 配置GPU节点组
     - 使用Kubernetes部署模型服务
   - 复杂度：高
   - 适用场景：已有Kubernetes基础设施，需要弹性扩展
   - 成本：高

### 风险提示

- **成本风险**: 由于无法使用Trainium/Inferentia，GPU实例成本可能是原方案的5-10倍
- **功能缺失**: 无Amazon Bedrock Guardrails，需自行实现安全控制，增加开发工作量
- **模型可用性**: DeepSeek-R1在中国区SageMaker JumpStart的可用性未经确认，可能需要手动导入
- **区域限制**: 某些新功能和模型可能延迟或不会在中国区发布
- **合规考虑**: 使用开源模型需要自行评估合规性和安全性

### 配套资源

- **GitHub仓库**: 
  - [DeepSeek-R1官方仓库](https://github.com/deepseek-ai/DeepSeek-R1)
  - [DeepSeek-V3官方仓库](https://github.com/deepseek-ai/DeepSeek-V3)
- **兼容性**: 模型本身可在中国区使用，但需要自行部署基础设施
- **修改建议**: 
  - 使用GPU实例替代Trainium/Inferentia
  - 从Hugging Face或官方GitHub下载模型权重
  - 自行实现内容安全过滤机制
  - 参考社区文章中的EC2和EKS部署方案

### 成本估算参考

以部署DeepSeek-R1-Distill-Llama-70B为例：

- **博客推荐方案（美国区域）**: Trn1.32xlarge约$21.50/小时
- **中国区替代方案**: G5.48xlarge约$16.29/小时（按需实例）
- **注意**: 中国区GPU实例供应可能紧张，建议使用预留实例或Savings Plans降低成本
