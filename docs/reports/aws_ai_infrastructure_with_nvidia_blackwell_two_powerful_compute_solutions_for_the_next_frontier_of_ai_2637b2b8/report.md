---
title: 配备NVIDIA Blackwell的AWS AI基础设施：面向AI下一前沿的两种强大计算解决方案
publish_date: 2025-07-09
original_url: https://aws.amazon.com/blogs/machine-learning/aws-ai-infrastructure-with-nvidia-blackwell-two-powerful-compute-solutions-for-the-next-frontier-of-ai/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 6
unavailable_services: 0
---

# 配备NVIDIA Blackwell的AWS AI基础设施：面向AI下一前沿的两种强大计算解决方案

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/aws-ai-infrastructure-with-nvidia-blackwell-two-powerful-compute-solutions-for-the-next-frontier-of-ai/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心硬件产品在中国区域不可用，无法实施

本文介绍的P6e-GB200 UltraServers和P6-B200实例是基于NVIDIA Blackwell GPU的最新一代EC2实例类型，目前在AWS中国区域（cn-northwest-1和cn-north-1）尚未推出。这是一篇产品发布公告，核心内容依赖于特定的硬件实例类型，无法通过软件层面的调整或替代方案实现。

## 服务分析

### 可用服务 (6个)

- Amazon EC2（服务本身可用）
- Amazon SageMaker HyperPod
- Amazon EKS (Elastic Kubernetes Service)
- Elastic Fabric Adapter (EFA)
- AWS Nitro System
- Amazon Elastic Compute Cloud

### 不可用服务 (0个)

无AWS服务层面的不可用情况。

### 评估说明

虽然文章中提到的所有AWS服务在中国区域都是可用的，但本文的核心内容是介绍两种特定的EC2实例类型：

1. **P6e-GB200 UltraServers** - 配备最多72个NVIDIA Blackwell GPU，采用GB200 NVL72架构
2. **P6-B200实例** - 配备8个NVIDIA Blackwell GPU

经过实际验证，**P6系列实例在cn-northwest-1区域完全不可用**。中国区域目前可用的最新GPU实例是P3系列（配备NVIDIA V100 GPU），与P6系列在性能和架构上存在代际差距：

- P3实例使用NVIDIA V100 GPU（Volta架构，2017年发布）
- P6实例使用NVIDIA Blackwell GPU（2024-2025年发布）
- 性能差距：P6-B200相比P5en提供2.25倍GPU TFLOPs，而P5系列在中国区域也不可用

这是一个硬件层面的限制，无法通过配置调整或服务替代来解决。文章中介绍的所有先进特性（如NVLink互连、液冷技术、EFAv4网络、第六代Nitro System等）都依赖于这些特定的硬件平台。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 本文为产品发布公告，核心内容是介绍P6e-GB200 UltraServers和P6-B200实例这两种特定的EC2实例类型。经验证，这些实例类型在AWS中国区域（cn-northwest-1）不可用，且无法通过软件配置或服务替代实现相同功能。由于核心硬件产品不可用，无需进行深入验证。

## 实施建议

### 推荐方案

**不建议在中国区域实施本文介绍的方案**，原因如下：

1. **硬件不可用**：P6e-GB200和P6-B200实例在中国区域未推出
2. **无直接替代**：现有P3实例（V100 GPU）与P6系列存在多代技术差距
3. **架构依赖**：文章介绍的许多特性（如GB200 NVL72架构、72 GPU NVLink域、液冷技术等）是硬件特定的

### 替代方案

如果您在中国区域有大规模AI训练和推理需求，可以考虑以下替代方案：

1. **使用P3实例**
   - 实施方式：在cn-northwest-1使用P3.2xlarge、P3.8xlarge或P3.16xlarge实例
   - GPU：NVIDIA V100（16GB显存）
   - 复杂度：低
   - 适用场景：中小规模AI训练和推理工作负载
   - 限制：性能和规模远低于P6系列

2. **跨区域部署**
   - 实施方式：在AWS全球区域（如us-east-1、us-west-2）使用P6实例，通过网络连接中国区域的数据和应用
   - 复杂度：高
   - 适用场景：对性能要求极高且可接受跨境网络延迟的场景
   - 限制：需考虑数据合规性、网络延迟、跨境数据传输成本

3. **等待产品发布**
   - 实施方式：关注AWS中国区域的产品发布公告，等待P6系列或更新GPU实例推出
   - 复杂度：无
   - 适用场景：项目时间线灵活，可等待新硬件上市
   - 限制：发布时间不确定

### 风险提示

- **性能差距**：P3实例与P6系列在计算性能、显存容量、网络带宽等方面存在显著差距，可能无法满足大规模AI模型训练需求
- **架构限制**：P3实例不支持EFA（Elastic Fabric Adapter），限制了大规模分布式训练的性能
- **成本考虑**：如选择跨区域部署方案，需要考虑跨境数据传输费用和潜在的合规成本
- **合规要求**：跨区域部署需要评估数据本地化和隐私保护相关的法律法规要求

### 配套资源

- **GitHub仓库**: 无
- **相关文档**: 
  - [AWS中国区域P3实例文档](https://docs.amazonaws.cn/ec2/latest/userguide/accelerated-computing-instances.html)
  - [Amazon SageMaker HyperPod文档](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)
