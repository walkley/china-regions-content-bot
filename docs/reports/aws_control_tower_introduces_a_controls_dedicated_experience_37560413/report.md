---
title: AWS Control Tower 推出专用控制体验
publish_date: 2025-11-19
original_url: https://aws.amazon.com/blogs/aws/aws-control-tower-introduces-a-controls-dedicated-experience/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 2
unavailable_services: 1
---

# AWS Control Tower 推出专用控制体验

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/aws-control-tower-introduces-a-controls-dedicated-experience/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，无法在中国区实施

核心服务AWS Control Tower在AWS中国区域不可用，该博客介绍的Controls Dedicated体验功能完全依赖于AWS Control Tower，因此无法在中国区实施。

## 服务分析

### 可用服务 (2个)

- AWS Organizations
- AWS Config

### 不可用服务 (1个)

- **AWS Control Tower** - 核心服务

### 评估说明

虽然可用服务占比为66.7%，但AWS Control Tower是本文的核心服务，整篇博客都在介绍AWS Control Tower的新功能"Controls Dedicated experience"。该功能允许客户在已有完善的多账户环境中，仅使用AWS Control Tower的托管控制功能，而无需设置完整的Landing Zone。

由于AWS Control Tower在中国区不可用，该功能及其所有特性都无法在中国区使用。虽然AWS Organizations和AWS Config在中国区可用，但它们只是支撑服务，无法替代AWS Control Tower的核心功能。

## 验证结果

### 验证类型

- ⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务AWS Control Tower在AWS中国区域不可用，无法进行实际部署验证。

## 实施建议

### 推荐方案

不建议在AWS中国区域实施此方案。AWS Control Tower是该功能的核心依赖，在中国区完全不可用。

### 替代方案

如果您需要在AWS中国区域实现类似的多账户治理和控制功能，可以考虑以下替代方案：

1. **手动配置AWS Organizations + AWS Config**
   - 实施方式：使用AWS Organizations管理多账户结构，结合AWS Config Rules实现合规性检查
   - 复杂度：高
   - 适用场景：需要完全自定义的治理策略，有专业团队维护
   - 局限性：需要手动创建和维护所有控制规则，无法使用AWS Control Tower的托管控制库

2. **使用Service Control Policies (SCPs)**
   - 实施方式：通过AWS Organizations的SCP功能实现预防性控制
   - 复杂度：中
   - 适用场景：主要需要预防性控制（阻止某些操作）的场景
   - 局限性：仅提供预防性控制，不包含检测性控制和自动修复功能

3. **第三方治理工具**
   - 实施方式：使用支持AWS中国区域的第三方云治理和合规性管理工具
   - 复杂度：中到高
   - 适用场景：需要跨云平台统一治理的企业
   - 局限性：需要额外成本，可能需要与第三方供应商合作

### 风险提示

- **功能缺失**: AWS Control Tower的所有功能在中国区均不可用，包括托管控制、自动账户注册、Control Catalog等
- **维护成本**: 替代方案需要更多的人工维护和管理工作
- **合规性差距**: 无法直接使用AWS提供的预配置合规性控制，需要自行实现和维护
- **更新滞后**: 手动实现的控制无法自动获得AWS的最佳实践更新

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 不适用
