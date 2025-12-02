---
title: 在 Amazon EKS 上运行 ML 推理时增强和监控网络性能
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/containers/enhancing-and-monitoring-network-performance-when-running-ml-inference-on-amazon-eks/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: MODERATE
available_services: 13
unavailable_services: 2
---

# 在 Amazon EKS 上运行 ML 推理时增强和监控网络性能

[📖 查看原始博客](https://aws.amazon.com/blogs/containers/enhancing-and-monitoring-network-performance-when-running-ml-inference-on-amazon-eks/) | 验证日期: 2025-12-02

## 可行性评估

!!! warning "MODERATE - 谨慎实施"
    核心 ML 推理工作负载可以在中国区域实施，但网络观测性功能需要使用替代方案

核心的 ML 推理工作负载（基于 Amazon EKS 的 Stable Diffusion 图像生成）可以在中国区域完整部署。然而，文章重点介绍的 Container Network Observability 功能所依赖的 Amazon Managed Service for Prometheus 和 Amazon Managed Grafana 在中国区域不可用，需要使用自建或替代的观测性解决方案。

## 服务分析

### 可用服务 (13个)

- Amazon EKS (Elastic Kubernetes Service)
- Amazon EC2 (Elastic Compute Cloud)
- Amazon S3 (Simple Storage Service)
- Amazon API Gateway
- AWS Lambda
- Amazon SNS (Simple Notification Service)
- Amazon SQS (Simple Queue Service)
- Amazon CloudWatch
- AWS CDK (Cloud Development Kit)
- AWS CloudFormation
- Amazon DynamoDB
- AWS IAM (Identity and Access Management)
- Container Storage Interface (CSI) drivers (包括 Mountpoint for Amazon S3 CSI Driver)

### 不可用服务 (2个)

- **Amazon Managed Service for Prometheus** - 核心观测性服务
- **Amazon Managed Grafana** - 核心观测性服务

### 评估说明

文章的核心内容分为两部分：

1. **ML 推理工作负载部署**（完全可用）：使用 Amazon EKS 部署 Stable Diffusion 图像生成服务，包括 KEDA 自动扩展、Karpenter 节点管理、S3 存储模型权重等功能，所有相关服务在中国区域均可用。

2. **Container Network Observability 功能**（部分可用）：
   - CloudWatch Network Flow Monitor 和 EKS Network Flow Monitor Agent 的可用性需要确认
   - 文章使用 Amazon Managed Service for Prometheus 和 Amazon Managed Grafana 进行指标收集和可视化，这两个服务在中国区域不可用
   - 网络观测性指标以 Open Metrics 格式暴露，可以被其他观测性工具采集

关键影响：
- ML 推理工作负载本身可以完整实施
- 网络性能监控和观测功能需要使用替代方案（如自建 Prometheus + Grafana，或使用其他 APM 工具）
- Container Network Observability 的核心功能（Service Map、Flow Table、Performance Metrics）如果在中国区域可用，仍然可以通过 EKS 控制台和 CloudWatch 访问

## 验证结果

### 验证类型

⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 根据验证流程要求，深入验证阶段统一跳过以节约时间。

## 实施建议

### 推荐方案

文章内容可以在中国区域实施，但需要针对观测性部分进行调整：

**第一部分：ML 推理工作负载部署**（可直接实施）
- 按照文章步骤部署 Stable Diffusion 图像生成解决方案
- 所有核心服务（EKS、EC2、S3、Lambda、API Gateway、SNS、SQS）在中国区域完全可用
- GitHub 仓库可以正常克隆和使用
- 注意事项：
  - 确认 EC2 G5 实例在目标中国区域的配额
  - 使用中国区域的 S3 存储桶
  - API Gateway 和 Lambda 配置需要使用中国区域的端点

**第二部分：网络观测性功能**（需要替代方案）
- Container Network Observability 功能需要先确认在中国区域的可用性
- 如果 Network Flow Monitor Agent 可用，指标仍然可以被采集
- 使用替代的观测性方案收集和可视化指标

**预计工作量**：
- ML 推理工作负载部署：中等（与原文相同，约1小时）
- 观测性方案调整：中等（需要额外配置自建观测性工具）

### 替代方案

#### 方案1：自建 Prometheus + Grafana

- **实施方式**：
  - 在 EKS 集群中部署开源 Prometheus（使用 Helm Chart）
  - 在 EKS 集群中部署开源 Grafana（使用 Helm Chart）
  - 配置 Prometheus 抓取 Network Flow Monitor Agent 的指标（端口 9101，路径 /metrics）
  - 导入文章提供的 Grafana Dashboard JSON
- **复杂度**：中
- **适用场景**：
  - 需要完整的网络观测性功能
  - 团队有 Kubernetes 运维经验
  - 可以接受自行管理观测性基础设施

#### 方案2：使用 CloudWatch Container Insights

- **实施方式**：
  - 启用 CloudWatch Container Insights for EKS
  - 使用 CloudWatch Logs Insights 查询网络指标
  - 在 CloudWatch 控制台创建自定义仪表板
  - 如果 Network Flow Monitor 在中国区域可用，可以直接使用 EKS 控制台的 Network 标签页
- **复杂度**：低
- **适用场景**：
  - 希望使用 AWS 托管服务
  - 不需要高度自定义的可视化
  - 已经在使用 CloudWatch 作为主要观测性工具

#### 方案3：使用第三方 APM 工具

- **实施方式**：
  - 集成 Datadog、New Relic、Dynatrace 等在中国区域可用的 APM 工具
  - 配置工具采集 Prometheus 格式的指标
  - 使用工具提供的 Kubernetes 网络监控功能
- **复杂度**：中
- **适用场景**：
  - 已经在使用第三方 APM 工具
  - 需要统一的观测性平台
  - 预算允许使用商业工具

### 风险提示

- **服务可用性风险**：Container Network Observability 是较新的功能（2024年发布），需要确认在中国区域的可用性和功能完整性
- **功能差异风险**：即使 Network Flow Monitor 在中国区域可用，某些高级功能可能存在延迟或限制
- **成本风险**：自建 Prometheus + Grafana 需要额外的计算和存储资源，CloudWatch 指标和日志会产生额外费用
- **运维复杂度**：自建观测性方案需要团队具备相应的运维能力，包括高可用配置、数据持久化、告警配置等
- **网络性能**：从中国区域访问 GitHub 可能较慢，建议使用镜像或将代码同步到国内代码托管平台
- **GPU 实例配额**：G5 实例在中国区域可能需要申请配额提升

### 配套资源

- **GitHub仓库**: https://github.com/aws-solutions-library-samples/guidance-for-asynchronous-inference-with-stable-diffusion-on-aws
- **兼容性**: 代码本身与中国区域兼容，但需要注意：
  - CDK 部署时使用中国区域的参数
  - 容器镜像可能需要推送到中国区域的 ECR 或使用镜像加速
  - S3 存储桶需要在中国区域创建
- **修改建议**：
  - 修改 CDK 代码中的区域配置为中国区域
  - 确认所有 AWS 服务端点使用中国区域的端点
  - 观测性相关的配置需要替换为自建或替代方案
  - 如果使用自建 Prometheus，修改 scraper 配置指向自建的 Prometheus 服务

### 实施步骤建议

1. **部署 ML 推理工作负载**（按原文步骤）：
   - 克隆 GitHub 仓库
   - 修改区域配置为 cn-northwest-1
   - 运行 deploy.sh 部署解决方案
   - 验证 Stable Diffusion 服务正常运行

2. **配置网络观测性**（使用替代方案）：
   - 选择合适的替代方案（推荐方案1或方案2）
   - 部署观测性工具
   - 如果 Network Flow Monitor Agent 可用，配置指标采集
   - 创建监控仪表板和告警规则

3. **测试和验证**：
   - 发送图像生成请求测试 ML 推理功能
   - 验证网络指标是否正常采集
   - 测试性能监控和故障排查功能

4. **优化和调整**：
   - 根据实际网络性能调整实例类型
   - 优化模型加载时间
   - 配置自动扩展策略
