---
title: 使用代理式AI将企业工作负载转换速度提升4倍
publish_date: 2025-05-15
original_url: https://aws.amazon.com/blogs/migration-and-modernization/aws-transform-generally-available/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 4
unavailable_services: 1
---

# 使用代理式AI将企业工作负载转换速度提升4倍

[📖 查看原始博客](https://aws.amazon.com/blogs/migration-and-modernization/aws-transform-generally-available/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务AWS Transform在中国区域不可用，无法实施

本文介绍的AWS Transform服务是整个解决方案的核心，该服务在AWS中国区域不可用，导致文章中描述的所有功能（.NET应用现代化、大型机现代化、VMware迁移）均无法实施。

## 服务分析

### 可用服务 (4个)

- Amazon ECS
- AWS Fargate
- Amazon EC2
- Amazon VPC

### 不可用服务 (1个)

- **AWS Transform** - 核心服务

### 评估说明

AWS Transform是本文的唯一核心服务，整篇博客都在介绍该服务的三个AI代理功能：
1. AWS Transform agent for .NET - 将Windows .NET应用迁移到Linux
2. AWS Transform agent for mainframe - 大型机COBOL应用现代化
3. AWS Transform agent for VMware - VMware环境迁移到AWS

虽然文章提到的其他AWS服务（ECS、Fargate、EC2、VPC）在中国区域都可用，但这些只是迁移后的目标运行环境，不是本文的重点。没有AWS Transform服务，文章描述的自动化迁移和现代化能力完全无法实现。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务AWS Transform在中国区域不可用，无需进行深入验证

## 实施建议

### 推荐方案

不建议在AWS中国区域实施本文介绍的方案。AWS Transform是一个专门的AI驱动迁移和现代化服务，目前仅在全球区域提供。

### 替代方案

如果需要在中国区域进行类似的迁移和现代化工作，可以考虑以下传统方案：

1. **.NET应用现代化**
   - 实施方式：使用传统的手动代码迁移和重构方法，配合开源工具（如Porting Assistant for .NET的本地版本）
   - 复杂度：高
   - 适用场景：小规模.NET应用迁移，有充足的开发资源和时间

2. **大型机应用现代化**
   - 实施方式：使用AWS专业服务团队或合作伙伴提供的人工迁移服务
   - 复杂度：高
   - 适用场景：有预算和时间进行长期迁移项目的企业

3. **VMware迁移**
   - 实施方式：使用AWS Application Migration Service (MGN)进行服务器迁移，手动规划迁移波次和网络配置
   - 复杂度：中
   - 适用场景：VMware环境迁移，可接受较长的规划和实施周期

### 风险提示

- **服务不可用**: AWS Transform服务在中国区域完全不可用，无法使用其AI代理功能
- **时间成本**: 传统迁移方法需要的时间可能是文章中提到的AI加速方案的4倍以上
- **人力成本**: 需要大量经验丰富的迁移工程师和开发人员参与
- **准确性风险**: 缺少AI辅助的自动化分析和转换，可能出现更多的人为错误

### 配套资源

本文没有提供配套的GitHub项目，主要介绍AWS Transform服务本身的功能和使用方式。
