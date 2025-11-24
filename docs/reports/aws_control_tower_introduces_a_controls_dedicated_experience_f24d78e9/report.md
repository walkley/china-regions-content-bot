---
title: AWS Control Tower introduces a Controls Dedicated experience
original_url: https://aws.amazon.com/blogs/aws/aws-control-tower-introduces-a-controls-dedicated-experience/
validation_date: 2025-11-24
target_region: cn-northwest-1
feasibility: LOW
available_services: 2
unavailable_services: 2
---

# AWS Control Tower introduces a Controls Dedicated experience

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/aws-control-tower-introduces-a-controls-dedicated-experience/) | 验证日期: 2025-11-24

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务AWS Control Tower在中国区不可用，无法实施

AWS Control Tower服务本身在中国区域完全不可用，博客中介绍的Controls Dedicated experience功能依赖于AWS Control Tower服务，因此无法在中国区域实施。

## 服务分析

### 可用服务 (2个)

- AWS Organizations
- AWS Config

### 不可用服务 (2个)

- **AWS Control Tower** - 核心服务
- **Control Catalog** - 核心服务

### 评估说明

本文介绍的是AWS Control Tower的新功能"Controls Dedicated experience"，该功能允许客户在已有的多账户环境中仅使用AWS托管控制，而无需设置完整的landing zone。

通过实际验证发现：

1. **核心服务不可用**：AWS Control Tower服务在中国区域（cn-northwest-1和cn-north-1）完全不可用，无法连接到服务端点
2. **Control Catalog不可用**：Control Catalog服务也不可用，而这是提供托管控制的核心组件
3. **支撑服务可用**：AWS Organizations和AWS Config服务在中国区可用，但这两个服务只是AWS Control Tower的基础依赖，无法替代Control Tower的核心功能
4. **无替代方案**：AWS Control Tower是AWS提供的专有服务，没有直接的替代方案

## 验证结果

### 验证类型

- ✅ 教程步骤验证

### 执行状态

**状态**: ❌ 失败

**原因**: AWS Control Tower服务在中国区域不可用，无法执行博客中描述的任何操作步骤

### 关键发现

1. **AWS Control Tower服务端点不存在**
   - 在cn-northwest-1和cn-north-1区域尝试调用AWS Control Tower API均失败
   - 错误信息：无法连接到服务端点
   - 影响：博客中的所有功能和操作步骤都无法执行

2. **Control Catalog服务不可用**
   - Control Catalog是提供托管控制的核心组件
   - 该服务在中国区域也不可用
   - 影响：即使有其他方式访问控制功能，也无法获取控制目录

3. **基础服务可用但不足**
   - AWS Organizations和AWS Config在中国区可用
   - 但这些服务只能提供基础的组织管理和配置监控功能
   - 无法实现AWS Control Tower的托管控制和治理功能

## 实施建议

### 推荐方案

**不建议在中国区实施此方案**

由于AWS Control Tower服务在中国区域完全不可用，博客中介绍的Controls Dedicated experience功能无法实施。

### 替代方案

虽然无法使用AWS Control Tower，但可以考虑以下替代方案实现类似的治理目标：

1. **使用AWS Organizations + AWS Config手动实现治理**
   - 实施方式：
     - 使用AWS Organizations创建组织结构和账户管理
     - 使用Service Control Policies (SCPs)实现预防性控制
     - 使用AWS Config Rules实现检测性控制
     - 手动创建和维护合规规则
   - 复杂度：高
   - 适用场景：需要多账户治理但无法使用Control Tower的环境
   - 局限性：需要大量手动配置和维护工作，缺少Control Tower的自动化和最佳实践模板

2. **使用第三方治理工具**
   - 实施方式：采用支持中国区的第三方云治理和合规管理平台
   - 复杂度：中
   - 适用场景：需要跨云或更灵活的治理方案
   - 局限性：需要额外成本，可能无法完全复制AWS Control Tower的功能

3. **使用AWS CloudFormation StackSets实现标准化部署**
   - 实施方式：
     - 创建CloudFormation模板定义标准配置
     - 使用StackSets跨账户和区域部署
     - 结合AWS Config监控合规性
   - 复杂度：中
   - 适用场景：需要在多账户环境中标准化资源配置
   - 局限性：主要解决配置标准化问题，不能完全替代Control Tower的治理功能

### 风险提示

- **服务不可用风险**：AWS Control Tower在中国区域不可用是服务层面的限制，短期内不太可能改变
- **功能差距风险**：任何替代方案都无法完全复制AWS Control Tower的功能和自动化能力
- **维护成本风险**：手动实现类似功能需要投入大量的开发和维护资源
- **合规性风险**：缺少AWS Control Tower的预置最佳实践和合规框架，需要自行设计和验证

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 不适用
