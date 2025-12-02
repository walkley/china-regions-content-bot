---
title: 使用AWS Backup S3分层降低Amazon S3备份成本
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/storage/lower-your-amazon-s3-backup-cost-with-aws-backup-s3-tiering/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: LOW
available_services: 2
unavailable_services: 1
---

# 使用AWS Backup S3分层降低Amazon S3备份成本

[📖 查看原始博客](https://aws.amazon.com/blogs/storage/lower-your-amazon-s3-backup-cost-with-aws-backup-s3-tiering/) | 验证日期: 2025-12-02

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心功能AWS Backup S3 tiering在中国区域不可用，无法按照原文实施

文章介绍的核心功能"AWS Backup低成本暖存储层（low-cost warm storage tier）"是AWS Backup在2025年11月推出的新功能，目前在AWS中国区域尚未发布。该功能允许自动将S3备份数据在保存60天后转移到低成本存储层，从而降低长期备份存储成本最多30%。由于这一核心功能在中国区域不可用，文章中描述的所有配置步骤和成本优化方案均无法实施。

## 服务分析

### 可用服务 (2个)

- **Amazon S3** - 对象存储服务，在中国区域完全可用
- **AWS Backup** - 统一备份服务，在中国区域可用（但不支持S3 tiering功能）

### 不可用服务 (1个)

- **AWS Backup S3 Tiering** - 核心功能，S3备份的低成本暖存储层功能在中国区域不可用

### 评估说明

通过对cn-northwest-1区域的实际验证，确认了以下情况：

1. **AWS Backup基础服务可用**：可以在中国区域创建backup vault、执行备份任务等基本操作
2. **S3 Tiering功能缺失**：
   - AWS CLI中没有任何与tiering相关的命令（如`create-tiering-configuration`、`list-tiering-configurations`等）
   - Backup vault的配置中不包含tiering相关的属性
   - 控制台中也没有"S3 backup tiering"菜单选项
3. **功能发布时间**：该功能于2025年11月26日在全球区域发布，属于最新功能，通常需要数月时间才会在中国区域上线

由于文章的核心内容就是配置和使用AWS Backup的S3 tiering功能来降低成本，而这一功能在中国区域完全不可用，因此整个方案无法实施。

## 验证结果

### 验证类型

- ⏭️ 已跳过（核心功能不可用）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: AWS Backup S3 tiering功能在中国区域（cn-northwest-1）不可用，无法进行实际部署验证。通过CLI命令对比和API调用确认该功能尚未在中国区域发布。

### 关键发现

1. **功能可用性验证**
   - 在cn-northwest-1区域执行`aws backup help`命令，对比全球区域和中国区域的可用命令列表
   - 确认中国区域缺少所有与tiering相关的API操作
   - 创建测试backup vault，确认vault配置中不包含tiering相关属性

2. **服务基础能力确认**
   - AWS Backup基础服务在中国区域正常运行
   - Amazon S3服务完全可用
   - 可以正常创建backup vault和执行S3备份任务

3. **功能发布时间分析**
   - 该功能于2025年11月26日发布，属于最新功能
   - AWS新功能通常需要3-6个月或更长时间才会在中国区域上线
   - 需要等待AWS官方公告确认中国区域的发布时间

## 实施建议

### 推荐方案

**不建议在中国区域实施此方案**，原因如下：

1. **核心功能缺失**：AWS Backup S3 tiering功能在中国区域完全不可用
2. **无替代API**：没有任何CLI命令或API可以配置S3备份的存储层转换
3. **等待官方发布**：建议关注AWS中国区域的功能发布公告，等待该功能正式上线

### 替代方案

虽然无法使用AWS Backup的S3 tiering功能，但可以考虑以下替代方案来降低S3备份存储成本：

1. **S3生命周期策略**
   - 实施方式：直接在S3存储桶上配置生命周期规则，将对象转换到S3 Glacier或S3 Glacier Deep Archive
   - 复杂度：低
   - 适用场景：适用于不需要AWS Backup统一管理的场景，可以自行管理备份数据的生命周期
   - 限制：
     - 失去AWS Backup的统一管理能力
     - 无法使用AWS Backup的恢复测试、合规性报告等功能
     - 需要自行管理备份保留策略和恢复流程

2. **S3 Intelligent-Tiering**
   - 实施方式：为S3存储桶启用Intelligent-Tiering存储类，自动优化存储成本
   - 复杂度：低
   - 适用场景：访问模式不确定的备份数据
   - 限制：
     - 成本节省可能不如手动配置生命周期策略
     - 有监控和自动化费用
     - 同样失去AWS Backup的统一管理能力

3. **跨区域复制到低成本存储类**
   - 实施方式：使用S3跨区域复制，将备份数据复制到另一个区域并直接存储到Glacier存储类
   - 复杂度：中
   - 适用场景：需要异地灾备且对恢复时间要求不高的场景
   - 限制：
     - 增加跨区域数据传输成本
     - 恢复时间较长
     - 管理复杂度增加

### 风险提示

- **功能等待风险**：AWS Backup S3 tiering功能在中国区域的上线时间不确定，可能需要数月甚至更长时间
- **成本优化受限**：在该功能上线前，无法享受文章中提到的最多30%的存储成本节省
- **替代方案局限**：使用S3原生生命周期策略虽然可以降低成本，但会失去AWS Backup提供的统一数据保护、恢复测试、合规性审计等企业级功能
- **架构一致性**：如果在全球区域和中国区域都有部署，需要维护不同的备份成本优化策略，增加运维复杂度

### 配套资源

- **GitHub仓库**: 无
- **相关文档**: 
  - [AWS Backup 中国区域文档](https://docs.amazonaws.cn/aws-backup/)
  - [Amazon S3 生命周期管理](https://docs.amazonaws.cn/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
  - [AWS Backup 定价（全球区域）](https://aws.amazon.com/backup/pricing/)

### 后续关注

建议定期检查以下资源，了解功能上线情况：

1. AWS中国区域新功能发布公告
2. AWS Backup中国区域文档更新
3. AWS CLI版本更新说明（关注backup服务的新增命令）

一旦该功能在中国区域上线，可以按照原文的步骤进行配置，预期可以获得与全球区域相同的成本优化效果。
