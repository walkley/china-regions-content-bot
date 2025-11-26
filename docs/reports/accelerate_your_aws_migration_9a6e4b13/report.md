---
title: 通过AWS培训和认证加速您的AWS迁移
publish_date: 2025-04-09
original_url: https://aws.amazon.com/blogs/training-and-certification/accelerate-your-aws-migration/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 6
unavailable_services: 1
---

# 通过AWS培训和认证加速您的AWS迁移

[📖 查看原始博客](https://aws.amazon.com/blogs/training-and-certification/accelerate-your-aws-migration/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文主要介绍AWS迁移过程中的培训资源和认证路径，所有核心服务（培训、认证、迁移工具）在AWS中国区域均可用，可以直接按照文章指导实施。

## 服务分析

### 可用服务 (6个)

- AWS Training and Certification
- AWS Database Migration Service
- AWS Application Migration Service
- AWS Server Migration Service
- Amazon Database Migration Accelerator
- AWS Mainframe Modernization Service

### 不可用服务 (1个)

- **AWS Migration Hub**

### 评估说明

文章涉及的7个AWS服务中，6个在中国区域可用，可用率达85.7%。唯一不可用的AWS Migration Hub是一个迁移跟踪和可视化工具，主要用于集中查看和管理多个迁移工具的进度。它的缺失不影响实际的迁移操作，因为：

1. **核心迁移服务完全可用**：AWS Database Migration Service、AWS Application Migration Service等实际执行迁移的服务都可用
2. **培训资源完全可用**：文章重点推荐的所有培训课程、认证路径和学习资源在中国区域都可以访问
3. **替代方案存在**：可以通过各个迁移服务的独立控制台或使用CloudWatch、CloudTrail等服务来跟踪迁移进度

## 验证结果

### 验证类型

- ⏭️ 已跳过（无需深入验证）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 本文为培训资源指导类内容，不包含配套GitHub项目或具体技术操作步骤，无需进行部署验证。基础服务可用性分析已足够评估可行性。

## 实施建议

### 推荐方案

可直接按照原文实施，文章提供的迁移方法论和培训资源完全适用于AWS中国区域：

**评估阶段**：
- 使用AWS Technical Essentials和AWS Cloud Essentials for Business Leaders课程了解AWS服务
- 通过AWS Migration Essentials学习迁移方法论

**动员阶段**：
- 建立核心迁移团队并制定迁移计划
- 利用Migration Foundations Knowledge Badge Readiness Path提升团队技能

**迁移和现代化阶段**：
- 使用AWS Database Migration Service、AWS Application Migration Service等工具执行迁移
- 针对大型机迁移场景，可使用AWS Mainframe Modernization Service

**注意事项**：
- AWS Migration Hub不可用，需要通过各迁移服务的独立控制台管理迁移进度
- 培训课程和认证考试在中国区域可能需要通过AWS中国官网或授权培训合作伙伴访问
- 部分英文培训资源可能需要一定的英语能力

### 替代方案

针对AWS Migration Hub不可用的情况，可采用以下替代方案：

1. **使用独立服务控制台**
   - 实施方式：直接在各迁移服务（DMS、Application Migration Service等）的控制台中监控进度
   - 复杂度：低
   - 适用场景：迁移项目规模较小，使用的迁移服务种类较少

2. **自建迁移跟踪仪表板**
   - 实施方式：使用CloudWatch、CloudTrail和QuickSight构建自定义迁移监控仪表板
   - 复杂度：中
   - 适用场景：大规模迁移项目，需要集中可视化和报告功能

3. **使用第三方迁移管理工具**
   - 实施方式：采用支持AWS中国区域的第三方迁移管理平台
   - 复杂度：中
   - 适用场景：需要高级项目管理功能或跨云迁移场景

### 风险提示

- **培训资源访问**：部分AWS培训资源和认证考试可能需要通过AWS中国官网或授权培训合作伙伴访问，建议提前确认访问方式
- **迁移进度跟踪**：由于AWS Migration Hub不可用，大规模迁移项目需要提前规划替代的进度跟踪方案
- **文档和支持**：部分迁移服务的中文文档可能不如全球区域完善，建议团队具备一定的英文技术文档阅读能力

### 配套资源

本文无配套GitHub项目，主要推荐的资源为：
- AWS Training and Certification官方课程
- AWS Skill Builder学习平台
- AWS认证考试（Cloud Practitioner等）

这些资源在AWS中国区域均可通过官方渠道访问。
