---
title: 使用Amazon EC2和SageMaker AI优化构建AI模型的成本
publish_date: 2025-03-28
original_url: https://aws.amazon.com/blogs/aws-cloud-financial-management/optimizing-cost-for-developing-custom-ai-models-with-amazon-ec2-and-sagemaker-ai/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 24
unavailable_services: 0
---

# 使用Amazon EC2和SageMaker AI优化构建AI模型的成本

[📖 查看原始博客](https://aws.amazon.com/blogs/aws-cloud-financial-management/optimizing-cost-for-developing-custom-ai-models-with-amazon-ec2-and-sagemaker-ai/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文介绍的所有AWS服务和成本优化策略在AWS中国区域完全可用，包括Amazon EC2、SageMaker AI及其所有相关功能。文章聚焦于成本优化最佳实践，不涉及任何中国区域不可用的服务。

## 服务分析

### 可用服务 (24个)

- Amazon EC2
- Amazon SageMaker AI
- Amazon CloudWatch
- AWS Compute Optimizer
- AWS Graviton
- AWS Trainium
- AWS Inferentia
- AWS Cost Explorer
- AWS Cost and Usage Reports (CUR)
- AWS Health Dashboard
- AWS Instance Scheduler
- Amazon RDS
- AWS CloudFormation
- AWS Savings Plans (Instance Savings Plans & Compute Savings Plans)
- SageMaker JumpStart
- SageMaker Studio Notebooks
- SageMaker On-Demand Notebooks
- SageMaker Processing
- SageMaker Data Wrangler
- SageMaker Training
- SageMaker Real-Time Inference
- SageMaker Batch Transform
- SageMaker Serverless Inference
- SageMaker Asynchronous Inference

### 不可用服务 (0个)

无

### 评估说明

本文是一篇关于生成式AI工作负载成本优化的最佳实践指南，重点介绍了在Amazon EC2和SageMaker AI上构建和部署自定义AI模型的成本优化策略。文章涵盖的所有服务和功能在AWS中国区域（宁夏和北京）均完全可用，包括：

1. **核心计算服务**：Amazon EC2、AWS Graviton、AWS Trainium、AWS Inferentia等加速实例类型
2. **机器学习平台**：Amazon SageMaker AI及其所有子服务（训练、推理、数据处理等）
3. **成本管理工具**：AWS Compute Optimizer、Cost Explorer、Cost and Usage Reports、Savings Plans
4. **运维工具**：CloudWatch、Instance Scheduler、CloudFormation

文章提到的FM Bench工具是一个开源基准测试工具，可用于评估不同实例类型的性能和成本效益，在中国区域同样适用。

## 验证结果

### 验证类型

⏭️ 已跳过（无需深入验证）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 本文是成本优化最佳实践和策略指导文章，不包含需要实际部署验证的配套GitHub项目或具体操作步骤。所有提到的服务在中国区域100%可用，可直接应用文章中的优化建议。

## 实施建议

### 推荐方案

可直接按照原文实施所有成本优化策略，包括：

**Amazon EC2优化策略**：
- 使用AWS Compute Optimizer进行实例类型选择和优化
- 利用On-Demand Capacity Reservations (ODCRs)确保GPU/加速器实例容量
- 通过Instance Scheduler自动化实例启停以降低成本
- 采用Savings Plans（ISP或CSP）获得最高72%的折扣
- 使用CloudWatch监控GPU利用率以最大化资源效率

**Amazon SageMaker AI优化策略**：
- 使用FM Bench工具进行实例类型和规模的性能测试
- 通过SageMaker JumpStart快速开始模型开发
- 采用Machine Learning Savings Plans节省最高64%的成本
- 使用Managed Spot Training降低最高90%的训练成本
- 根据工作负载特性选择合适的推理策略（实时、无服务器、批处理或异步）

**注意事项**：
- AWS Trainium和Inferentia实例在中国区域可用，可提供30-50%的性价比优势
- Savings Plans和Spot Instances在中国区域的定价和折扣率可能与全球区域略有差异，建议通过AWS定价计算器确认具体价格
- 使用Instance Scheduler时需要通过CloudFormation部署，确保使用中国区域的CloudFormation模板
- 访问AWS Marketplace和某些开源工具（如FM Bench）时，可能需要考虑网络连接性

### 替代方案

无需替代方案，所有策略均可直接实施。

### 风险提示

- **定价差异**：中国区域的定价可能与全球区域不同，建议使用AWS定价计算器（https://calculator.aws）进行成本估算
- **服务限制**：某些新发布的实例类型可能在中国区域的上线时间略晚于全球区域，建议在实施前确认所需实例类型的可用性
- **网络访问**：访问GitHub上的开源工具（如FM Bench）时可能需要配置适当的网络环境
- **文档语言**：部分AWS服务的中文文档可能更新不如英文文档及时，建议参考英文文档获取最新信息

### 配套资源

- **FM Bench工具**: https://aws-samples.github.io/foundation-model-benchmarking-tool/
- **兼容性**: 可在中国区使用，用于基准测试和性能评估
- **修改建议**: 无需修改，直接使用即可
