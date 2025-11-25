---
title: 使用容器网络可观测性监控EKS集群的网络性能和流量
publish_date: 2025-11-19
original_url: https://aws.amazon.com/blogs/aws/monitor-network-performance-and-traffic-across-your-eks-clusters-with-container-network-observability/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 5
unavailable_services: 1
---

# 使用容器网络可观测性监控EKS集群的网络性能和流量

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/monitor-network-performance-and-traffic-across-your-eks-clusters-with-container-network-observability/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心依赖服务CloudWatch Network Flow Monitor在中国区域不可用，Container Network Observability功能无法使用

博客介绍的Container Network Observability是Amazon EKS的新功能，用于监控和可视化Kubernetes集群的网络性能和流量模式。该功能完全依赖于Amazon CloudWatch Network Flow Monitor服务，但经过实际验证，该服务在AWS中国区域尚未部署，导致核心功能无法实施。

## 服务分析

### 可用服务 (5个)

- Amazon Elastic Kubernetes Service (Amazon EKS)
- Amazon CloudWatch
- Amazon Managed Grafana
- Amazon DynamoDB
- Amazon S3

### 不可用服务 (1个)

- **Amazon CloudWatch Network Flow Monitor** - 核心服务，Container Network Observability的基础依赖

### 评估说明

虽然Amazon EKS和Amazon CloudWatch基础服务在中国区域完全可用，但Container Network Observability功能的核心依赖服务CloudWatch Network Flow Monitor在中国区域不可用。具体验证发现：

1. **EKS服务可用**：可以正常创建和管理EKS集群
2. **CloudWatch基础服务可用**：CloudWatch监控、日志、告警等功能正常
3. **Network Flow Monitor不可用**：
   - API endpoint无法连接（`https://networkflowmonitor.cn-northwest-1.api.amazonwebservices.com.cn`）
   - 在cn-northwest-1和cn-north-1区域均无法访问
   - 这直接导致以下功能无法使用：
     - Service Map（服务拓扑图）
     - Flow Table（流量表）
     - Performance Metrics Endpoint（性能指标端点）
     - Network Flow Monitor Agent

博客中明确提到该功能"available in all commercial AWS regions where Amazon CloudWatch Network Flow Monitor is available"，而Network Flow Monitor目前未在中国区域部署。

## 验证结果

### 验证类型

- ✅ 教程步骤验证

### 执行状态

**状态**: ❌ 失败

**原因**: 核心依赖服务CloudWatch Network Flow Monitor在AWS中国区域不可用，无法完成功能验证

### 关键发现

1. **Network Flow Monitor服务不可用**
   - 在cn-northwest-1和cn-north-1区域尝试访问networkflowmonitor API均失败
   - 错误信息：`Could not connect to the endpoint URL`
   - 影响：Container Network Observability的所有核心功能（Service Map、Flow Table、Performance Metrics）均无法使用

2. **EKS控制台功能缺失**
   - EKS create-cluster API中没有Container Network Observability相关配置参数
   - 无法在集群创建时启用网络可观测性功能
   - EKS控制台中缺少"Configure network observability"配置选项

3. **替代方案存在但功能受限**
   - `amazon-cloudwatch-observability` addon在中国区域可用，但主要用于应用可观测性（Application Signals）
   - 该addon不包含Network Flow Monitor功能
   - 可以使用传统的Prometheus + Grafana方案监控网络指标，但无法获得Service Map和Flow Table等高级功能

## 实施建议

### 推荐方案

**不建议直接实施**

由于核心服务CloudWatch Network Flow Monitor在中国区域不可用，博客中介绍的Container Network Observability功能无法在中国区域实施。建议等待AWS在中国区域正式发布该服务后再考虑使用。

### 替代方案

如果需要在EKS集群中实现网络监控和可观测性，可以考虑以下替代方案：

1. **Prometheus + Grafana方案**
   - 实施方式：
     - 部署Prometheus Node Exporter收集节点级网络指标
     - 使用kube-state-metrics收集Kubernetes资源指标
     - 配置Grafana可视化网络流量和性能数据
   - 复杂度：中
   - 适用场景：需要基础网络监控和可视化，但不需要Service Map等高级功能
   - 限制：无法提供pod级别的流量拓扑图和详细的流量分析

2. **VPC Flow Logs + CloudWatch Logs Insights**
   - 实施方式：
     - 启用VPC Flow Logs捕获网络流量
     - 使用CloudWatch Logs Insights查询和分析流量模式
     - 创建CloudWatch Dashboard可视化关键指标
   - 复杂度：低
   - 适用场景：需要网络流量审计和基础分析
   - 限制：粒度较粗，无法精确到pod级别，缺少实时可视化

3. **第三方网络可观测性工具**
   - 实施方式：
     - 部署Cilium Hubble（如果使用Cilium CNI）
     - 使用Weave Scope进行网络可视化
     - 集成Istio Service Mesh的可观测性功能
   - 复杂度：高
   - 适用场景：需要完整的网络可观测性解决方案，愿意投入额外的运维成本
   - 限制：需要额外的学习成本和运维开销

### 风险提示

- **功能缺失风险**：Container Network Observability的核心功能在中国区域完全不可用，包括Service Map、Flow Table和Network Flow Monitor Agent
- **服务可用性不确定**：目前无法确定AWS何时会在中国区域发布CloudWatch Network Flow Monitor服务
- **替代方案局限性**：现有替代方案无法完全替代Container Network Observability的功能，特别是在pod级别的流量可视化和分析方面
- **架构差异风险**：如果未来在全球区域和中国区域部署相同的应用，网络监控方案会存在差异，增加运维复杂度

### 配套资源

- **GitHub仓库**: 无专门配套代码仓库
- **兼容性**: 不适用
- **修改建议**: 不适用

---

**建议**: 持续关注AWS中国区域的服务发布公告，等待CloudWatch Network Flow Monitor服务在中国区域上线后再考虑实施Container Network Observability功能。在此之前，建议使用Prometheus + Grafana等替代方案满足基础的网络监控需求。
