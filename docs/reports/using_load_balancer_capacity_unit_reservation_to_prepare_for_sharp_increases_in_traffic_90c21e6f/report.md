---
title: 使用负载均衡器容量单元预留为流量激增做准备
publish_date: 2025-01-28
original_url: https://aws.amazon.com/blogs/networking-and-content-delivery/using-load-balancer-capacity-unit-reservation-to-prepare-for-sharp-increases-in-traffic/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 6
unavailable_services: 0
---

# 使用负载均衡器容量单元预留为流量激增做准备

[📖 查看原始博客](https://aws.amazon.com/blogs/networking-and-content-delivery/using-load-balancer-capacity-unit-reservation-to-prepare-for-sharp-increases-in-traffic/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心功能LCU Reservation在中国区域不可用，无法实施

虽然所有基础服务（ALB、NLB、CloudWatch等）在中国区域都可用，但博客介绍的核心功能"LCU Reservation（负载均衡器容量单元预留）"在AWS中国区域尚未推出，导致文章中的主要操作步骤无法执行。

## 服务分析

### 可用服务 (6个)

- Elastic Load Balancing (ALB)
- Elastic Load Balancing (NLB)
- AWS WAF
- AWS Lambda
- Amazon CloudWatch
- AWS CLI

### 不可用服务 (0个)

无

### 评估说明

基础服务层面：所有提到的AWS服务在中国区域都是可用的，包括Application Load Balancer、Network Load Balancer、CloudWatch等。

功能层面：LCU Reservation是ELB在2025年1月推出的新功能特性，该功能允许用户提前预留负载均衡器容量以应对流量激增。经过实际验证，该功能在cn-northwest-1区域不可用：

1. **ALB测试结果**：调用`modify-capacity-reservation`时返回错误"CapacityUnits exceeds the maximum value of '0'"，表明该区域的容量上限为0
2. **NLB测试结果**：调用`modify-capacity-reservation`时返回"InvalidAction: Unknown"错误，表明该操作不被支持
3. **API可用性**：虽然`describe-capacity-reservation` API可以调用，但返回空的状态信息

这是典型的新功能在全球区域和中国区域之间存在发布时间差的情况。

## 验证结果

### 验证类型

✅ 教程步骤验证

### 执行状态

**状态**: ❌ 失败

**原因**: 核心功能LCU Reservation在中国区域不可用

### 关键发现

1. **LCU Reservation功能不可用**
   - 在cn-northwest-1区域创建ALB和NLB后，尝试设置LCU Reservation均失败
   - ALB返回容量限制错误（最大值为0），NLB返回无效操作错误
   - 这表明该功能在中国区域尚未启用

2. **基础服务完全可用**
   - 成功创建和配置ALB和NLB
   - 所有相关的AWS服务（CloudWatch、WAF、Lambda等）在中国区域都可正常使用
   - 负载均衡器的基本功能和自动扩展能力不受影响

3. **API接口部分实现**
   - `describe-capacity-reservation` API可以调用但返回空结果
   - `modify-capacity-reservation` API调用失败
   - 说明API框架已部署但功能未启用

## 实施建议

### 推荐方案

**不建议直接实施**

由于LCU Reservation功能在中国区域不可用，无法按照博客内容进行实施。该功能是博客的核心主题，缺失该功能意味着文章的主要价值无法体现。

### 替代方案

1. **使用传统的预热（Pre-warming）方式**
   - 实施方式：在预期流量激增前，通过AWS支持工单请求负载均衡器预热
   - 复杂度：中
   - 适用场景：计划内的大型活动、产品发布等可预测的流量高峰
   - 注意事项：需要提前至少2-3个工作日提交工单，说明预期流量规模和时间

2. **采用ELB分片（Sharding）策略**
   - 实施方式：使用多个负载均衡器分散流量，通过DNS或其他方式分配请求
   - 复杂度：高
   - 适用场景：超大规模工作负载或无法预测的流量模式
   - 优势：提供更好的容错能力和扩展性
   - 参考：[Scaling strategies for Elastic Load Balancing](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-strategies-for-elastic-load-balancing/)

3. **优化现有扩展策略**
   - 实施方式：
     - 确保ALB/NLB配置了足够的可用区（至少3个）
     - 在每个可用区注册足够的目标实例
     - 使用CloudWatch监控和告警跟踪负载均衡器指标
     - 进行负载测试以了解扩展行为
   - 复杂度：低
   - 适用场景：流量增长符合ELB自动扩展速率的场景
   - 扩展速率参考：
     - ALB：每5分钟可支持流量翻倍
     - NLB：从3 Gbps起始，每分钟增加3 Gbps

### 风险提示

- **流量激增风险**：如果流量增长速度超过ELB自动扩展速率（ALB每5分钟翻倍，NLB每分钟3Gbps），可能出现短暂的性能下降
- **预热流程延迟**：通过支持工单请求预热需要提前规划，无法像LCU Reservation那样自助快速完成
- **功能可用性不确定**：LCU Reservation功能何时在中国区域推出尚无明确时间表，建议定期关注AWS中国区域的功能更新公告

### 配套资源

- **GitHub仓库**: 无
- **相关文档**: 
  - [ALB LCU Reservation文档](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/capacity-unit-reservation.html)（全球区域）
  - [NLB LCU Reservation文档](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/capacity-unit-reservation.html)（全球区域）
  - [ELB扩展策略博客](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-strategies-for-elastic-load-balancing/)
