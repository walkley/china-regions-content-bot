---
title: 介绍Amazon Application Recovery Controller区域切换：多区域应用程序恢复服务
publish_date: 2025-08-01
original_url: https://aws.amazon.com/blogs/aws/introducing-amazon-application-recovery-controller-region-switch-a-multi-region-application-recovery-service/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 11
unavailable_services: 1
---

# 介绍Amazon Application Recovery Controller区域切换：多区域应用程序恢复服务

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/introducing-amazon-application-recovery-controller-region-switch-a-multi-region-application-recovery-service/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Application Recovery Controller (ARC) Region Switch在中国区域不可用，无法实施

虽然文章中提到的大部分支持服务在AWS中国区域都可用，但核心服务 **Amazon Application Recovery Controller (ARC) Region Switch** 本身在中国区域尚未部署，导致整个解决方案无法实施。

## 服务分析

### 可用服务 (11个)

- Amazon EC2 Auto Scaling
- Amazon Aurora
- Aurora Global Database
- AWS Lambda
- Amazon Route 53
- Amazon Elastic Kubernetes Service (Amazon EKS)
- Amazon Elastic Container Service (Amazon ECS)
- AWS Identity and Access Management (IAM)
- AWS Resource Access Manager (AWS RAM)
- Amazon CloudWatch
- AWS CloudFormation

### 不可用服务 (1个)

- **Amazon Application Recovery Controller (ARC) Region Switch** - 核心服务

### 评估说明

本文介绍的是Amazon Application Recovery Controller的新功能 **Region Switch**，这是一个2025年8月1日刚发布的全新服务能力。经过实际验证：

1. **核心服务不可用**：ARC Region Switch服务的endpoint在中国区域不存在
   - 尝试访问 `arc-region-switch-control-plane.cn-north-1.api.amazonwebservices.com.cn` 失败
   - DNS解析失败，说明该服务尚未在中国区域部署

2. **支持服务可用**：文章中提到的所有支持服务（EC2 Auto Scaling、Aurora Global Database、Lambda、Route 53、EKS、ECS等）在中国区域都可用

3. **无替代方案**：ARC Region Switch是一个专门的托管服务，提供跨区域故障转移的编排和自动化能力，目前在中国区域没有直接的等效服务

## 验证结果

### 验证类型

- ⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Application Recovery Controller (ARC) Region Switch在AWS中国区域不可用，无法进行实际部署验证。通过API调用和endpoint连通性测试确认该服务尚未在中国区域部署。

### 关键发现

1. **服务endpoint不存在**
   - 尝试连接 `https://arc-region-switch-control-plane.cn-north-1.api.amazonwebservices.com.cn/` 失败
   - DNS解析失败，确认该服务在中国区域未部署

2. **新服务部署延迟**
   - ARC Region Switch是2025年8月1日发布的新服务
   - 新服务通常需要一段时间才会在中国区域上线

3. **ARC其他功能也不可用**
   - 验证发现ARC的routing control功能在中国区域也无法访问
   - 说明整个ARC服务在中国区域的支持有限

## 实施建议

### 推荐方案

**不建议直接实施**

由于核心服务ARC Region Switch在中国区域不可用，无法按照原文实施该解决方案。建议等待AWS在中国区域正式发布该服务后再考虑使用。

### 替代方案

如果需要在AWS中国区域实现多区域故障转移能力，可以考虑以下替代方案：

1. **自建编排方案**
   - 实施方式：使用AWS Step Functions或Lambda编排跨区域故障转移流程
   - 复杂度：高
   - 适用场景：需要完全自定义的故障转移逻辑，有足够的开发和维护资源
   - 主要组件：
     - AWS Step Functions：编排故障转移步骤
     - Lambda函数：执行具体的切换操作（更新Auto Scaling、Aurora故障转移、Route 53更新等）
     - CloudWatch Alarms：监控和触发故障转移
     - DynamoDB：存储故障转移状态和配置

2. **基于Route 53的DNS故障转移**
   - 实施方式：使用Route 53健康检查和故障转移路由策略实现流量切换
   - 复杂度：中
   - 适用场景：主要依赖DNS层面的流量切换，应用架构相对简单
   - 局限性：只能处理流量路由，无法自动化处理计算资源扩展、数据库故障转移等操作

3. **Aurora Global Database手动故障转移**
   - 实施方式：使用Aurora Global Database的跨区域复制，手动或脚本化执行故障转移
   - 复杂度：中
   - 适用场景：数据库层面的跨区域容灾
   - 注意事项：需要配合应用层和DNS层的切换

4. **基础设施即代码(IaC)快速部署**
   - 实施方式：使用CloudFormation或Terraform在备用区域预定义基础设施，故障时快速部署
   - 复杂度：中到高
   - 适用场景：可以接受较长RTO（恢复时间目标）的场景
   - 优势：成本较低，备用区域只需要最小资源

### 风险提示

- **服务可用性风险**：ARC Region Switch在中国区域的上线时间不确定，可能需要较长等待期
- **功能差异风险**：即使未来在中国区域上线，功能可能与全球区域有差异
- **替代方案复杂度**：自建方案需要大量开发和测试工作，维护成本高
- **测试难度**：跨区域故障转移测试需要完整的多区域环境，成本和复杂度较高
- **合规要求**：中国区域的数据跨境传输需要符合相关法律法规要求

### 配套资源

- **GitHub仓库**: 无
- **官方文档**: [Amazon Application Recovery Controller文档](https://docs.aws.amazon.com/amazonarc/)（全球区域）
- **建议**: 持续关注AWS中国区域的服务发布公告，等待ARC Region Switch正式上线

### 后续跟进

建议定期检查以下资源以了解服务上线情况：

1. AWS中国区域服务公告页面
2. AWS CLI更新日志（检查中国区域endpoint支持）
3. 联系AWS中国团队获取服务路线图信息
