---
title: Monitor network performance and traffic across your EKS clusters with Container Network Observability
original_url: https://aws.amazon.com/blogs/aws/monitor-network-performance-and-traffic-across-your-eks-clusters-with-container-network-observability/
validation_date: 2025-11-24
target_region: cn-northwest-1
feasibility: LOW
available_services: 4
unavailable_services: 1
---

# Monitor network performance and traffic across your EKS clusters with Container Network Observability

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/monitor-network-performance-and-traffic-across-your-eks-clusters-with-container-network-observability/) | 验证日期: 2025-11-24

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon CloudWatch Network Flow Monitor在中国区域不可用，无法实施

本文介绍的Container Network Observability功能完全依赖于Amazon CloudWatch Network Flow Monitor服务，该服务目前在AWS中国区域（cn-north-1和cn-northwest-1）不可用。尽管Amazon EKS本身在中国区可用，但缺少核心的网络监控服务使得文章中描述的所有功能都无法实现。

## 服务分析

### 可用服务 (4个)

- Amazon Elastic Kubernetes Service (Amazon EKS)
- Amazon Managed Grafana
- Amazon DynamoDB
- Amazon S3

### 不可用服务 (1个)

- **Amazon CloudWatch Network Flow Monitor** - 核心服务

### 评估说明

1. **核心服务不可用**：Amazon CloudWatch Network Flow Monitor是实现Container Network Observability的核心依赖服务，在中国区域完全不可用。通过API测试确认，该服务的endpoint在中国区域无法访问。

2. **功能完全依赖**：文章中介绍的所有功能都基于Network Flow Monitor：
   - Service Map（服务地图）
   - Flow Table（流量表）
   - Performance Metrics（性能指标）
   - AWS Network Flow Monitor Agent

3. **无直接替代方案**：虽然EKS本身可用，但Container Network Observability是一个集成的新功能，没有等效的替代服务可以提供相同的网络可观测性能力。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon CloudWatch Network Flow Monitor在AWS中国区域不可用，经过API测试确认服务endpoint无法连接。由于核心依赖服务缺失，无法进行实际部署验证。

### 技术验证详情

在验证过程中进行了以下技术确认：

1. **EKS插件检查**：在cn-northwest-1区域查询`aws-network-flow-monitor`插件，返回空列表，确认该插件在中国区不可用。

2. **Network Flow Monitor API测试**：尝试访问`networkflowmonitor`服务API，返回错误：
   ```
   Could not connect to the endpoint URL: "https://networkflowmonitor.cn-northwest-1.api.amazonwebservices.com.cn/monitors"
   ```

3. **对比全球区域**：在us-east-1区域测试相同API调用成功，确认服务仅在全球区域可用。

## 实施建议

### 推荐方案

**不建议直接实施**

由于核心服务Amazon CloudWatch Network Flow Monitor在中国区域不可用，文章中介绍的Container Network Observability功能无法在AWS中国区域实现。建议等待该服务在中国区域上线后再考虑实施。

### 替代方案

虽然无法使用Container Network Observability，但可以考虑以下替代方案来实现EKS集群的网络监控：

1. **Prometheus + Grafana方案**
   - 实施方式：部署Prometheus监控EKS集群网络指标，使用Amazon Managed Grafana或自建Grafana进行可视化
   - 复杂度：中
   - 适用场景：需要自定义网络监控指标和可视化的场景
   - 局限性：需要手动配置监控指标，无法获得AWS原生的服务地图和流量分析功能

2. **AWS VPC Flow Logs + CloudWatch Logs Insights**
   - 实施方式：启用VPC Flow Logs捕获网络流量，使用CloudWatch Logs Insights进行分析
   - 复杂度：中
   - 适用场景：需要分析VPC级别的网络流量模式
   - 局限性：粒度较粗，无法提供pod级别的详细网络可观测性

3. **第三方网络监控工具**
   - 实施方式：使用Cilium Hubble、Weave Scope等开源工具，或Datadog、New Relic等商业APM工具
   - 复杂度：中到高
   - 适用场景：需要深度网络可观测性和服务网格功能
   - 局限性：需要额外的部署和维护成本，与AWS原生服务集成度较低

4. **Service Mesh方案（Istio/App Mesh）**
   - 实施方式：部署服务网格获取服务间通信的可观测性
   - 复杂度：高
   - 适用场景：已经或计划使用服务网格架构的应用
   - 局限性：引入额外的架构复杂度，有一定的性能开销

### 风险提示

- **功能缺失**：所有替代方案都无法完全复制Container Network Observability提供的原生集成体验和功能深度
- **维护成本**：替代方案通常需要额外的部署、配置和维护工作
- **数据粒度**：大多数替代方案无法提供pod级别的详细网络性能指标
- **服务等待**：建议关注AWS中国区域的服务更新公告，等待Network Flow Monitor服务上线

### 配套资源

- **GitHub仓库**: 无
- **官方文档**: [Container Network Observability in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/network-observability.html)
- **兼容性**: 该功能在AWS中国区域不可用
