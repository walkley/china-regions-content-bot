---
title: 使用AWS代理AI迁移基于VMware的工作负载的选项
publish_date: 2025-06-04
original_url: https://aws.amazon.com/blogs/migration-and-modernization/aws-agentic-ai-options-for-migrating-vmware-based-workloads/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 7
unavailable_services: 3
---

# 使用AWS代理AI迁移基于VMware的工作负载的选项

[📖 查看原始博客](https://aws.amazon.com/blogs/migration-and-modernization/aws-agentic-ai-options-for-migrating-vmware-based-workloads/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

博客介绍的两个核心方案（AWS Transform for VMware 和 Amazon Bedrock multi-agent collaboration）所依赖的关键AI服务在AWS中国区域均不可用，导致方案无法按原文实施。

## 服务分析

### 可用服务 (7个)

- AWS Application Migration Service (MGN)
- Amazon S3
- AWS Lambda
- AWS Migration Portfolio Assessment (MPA)
- Migration Evaluator
- Amazon EC2
- Amazon VPC

### 不可用服务 (3个)

- **Amazon Bedrock** - 核心服务（包括 Bedrock Knowledge Base, Bedrock Agents, Bedrock Action Groups, Bedrock multi-agent collaboration）
- **AWS Transform for VMware** - 核心服务
- **AWS Control Tower** - 核心服务

### 评估说明

虽然70%的基础服务在中国区域可用，但博客的核心价值在于利用AI驱动的自动化工具来简化VMware工作负载迁移。两个主要方案都完全依赖于中国区域不可用的服务：

1. **Option 1 (AWS Transform for VMware)**：该服务在中国区域完全不可用，无法使用其自动化评估、网络配置转换和迁移规划功能。

2. **Option 2 (Amazon Bedrock multi-agent collaboration)**：Amazon Bedrock服务在中国区域不可用，无法构建多代理协作框架。

3. 虽然AWS Application Migration Service (MGN)、S3、Lambda等基础服务可用，但失去了AI驱动的自动化能力，迁移过程将回归传统的手动方式，无法实现博客所描述的效率提升（如80倍的网络配置转换速度）。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证显示核心AI服务（Amazon Bedrock和AWS Transform for VMware）在中国区域不可用，两个主要方案均无法实施，因此跳过深入验证阶段。

## 实施建议

### 推荐方案

不建议直接实施此博客中描述的AI驱动迁移方案。核心的AI自动化服务在中国区域不可用，无法实现博客所描述的主要价值：自动化评估、智能规划和多代理协作。

### 替代方案

1. **传统VMware迁移方案**
   - 实施方式：使用AWS Application Migration Service (MGN)进行标准的VMware到AWS迁移，配合手动评估和规划
   - 复杂度：中
   - 适用场景：标准的rehost迁移场景，可接受手动评估和规划的工作量
   - 说明：虽然失去了AI自动化能力，但MGN服务在中国区域可用，可以完成基本的服务器迁移

2. **使用第三方迁移评估工具**
   - 实施方式：结合RVTools等工具进行手动评估，使用AWS Migration Hub进行迁移跟踪
   - 复杂度：中到高
   - 适用场景：需要详细评估和规划的复杂迁移项目
   - 说明：需要更多人工参与，无法实现博客中提到的80倍速度提升

3. **分阶段迁移策略**
   - 实施方式：
     - 评估阶段：使用Migration Evaluator和MPA进行成本和资源评估
     - 规划阶段：手动设计VPC、子网、安全组等网络架构
     - 迁移阶段：使用AWS MGN进行服务器复制和迁移
     - 优化阶段：迁移后进行手动优化和调整
   - 复杂度：高
   - 适用场景：大规模VMware迁移项目，有专业迁移团队支持
   - 说明：这是传统的迁移方法，需要更长的时间周期和更多的人力投入

### 风险提示

- **功能缺失风险**: 无法使用AI驱动的自动化评估和规划功能，迁移效率大幅降低
- **时间成本风险**: 网络配置转换等任务需要手动完成，从1小时增加到2周左右
- **准确性风险**: 缺少AI辅助的依赖关系分析和资源优化建议，可能导致配置不够优化
- **学习曲线风险**: 团队需要深入了解AWS服务和VMware迁移最佳实践，无法依赖AI代理的指导
- **成本优化风险**: 缺少自动化的成本分析和许可证优化建议，可能导致迁移后成本高于预期

### 配套资源

- **GitHub仓库**: 无专门配套的代码仓库
- **相关文档**: 博客中引用了多个AWS迁移相关的文档和最佳实践，但核心的AI功能在中国区域不可用
- **建议**: 关注AWS中国区域的服务更新，等待Amazon Bedrock和AWS Transform服务在中国区域上线后再考虑实施此方案
