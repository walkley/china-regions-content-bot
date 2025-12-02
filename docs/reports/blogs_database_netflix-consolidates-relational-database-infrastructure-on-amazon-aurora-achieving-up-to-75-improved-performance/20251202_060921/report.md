---
title: Netflix在Amazon Aurora上整合关系数据库基础设施,实现高达75%的性能提升
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/database/netflix-consolidates-relational-database-infrastructure-on-amazon-aurora-achieving-up-to-75-improved-performance/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: HIGH
available_services: 4
unavailable_services: 0
---

# Netflix在Amazon Aurora上整合关系数据库基础设施,实现高达75%的性能提升

[📖 查看原始博客](https://aws.amazon.com/blogs/database/netflix-consolidates-relational-database-infrastructure-on-amazon-aurora-achieving-up-to-75-improved-performance/) | 验证日期: 2025-12-02

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用,可直接实施

文章中提到的所有AWS服务在AWS中国区域(宁夏区域 cn-northwest-1)均完全可用,包括核心的Amazon Aurora PostgreSQL、Aurora Global Database、Amazon EC2和Amazon S3服务。该案例研究的技术架构和实施方案可以在中国区域完整复现。

## 服务分析

### 可用服务 (4个)

- Amazon Aurora PostgreSQL-Compatible Edition
- Aurora Global Database
- Amazon EC2 (Amazon Elastic Compute Cloud)
- Amazon S3 (Amazon Simple Storage Service)

### 不可用服务 (0个)

无

### 评估说明

本文是Netflix将自管理的分布式PostgreSQL兼容数据库迁移到Amazon Aurora PostgreSQL的技术案例研究。文章详细介绍了:

1. **业务挑战**: Netflix面临的数据库碎片化问题,包括运维开销、许可成本和开发体验不一致
2. **评估标准**: 开发者生产力、运维效率、性能可靠性和可扩展性四个维度
3. **技术架构**: Aurora的日志写入机制、共享存储架构和跨可用区复制
4. **迁移成果**: 实现高达75%的性能提升和28%的成本节约

经验证,所有核心服务在中国区域均可用:
- **Amazon Aurora PostgreSQL**: 在cn-northwest-1区域支持多个版本(11.x至17.x),包括最新的PostgreSQL 17.5兼容版本
- **Aurora Global Database**: 已验证在宁夏区域可用,支持跨区域异步复制
- **Amazon EC2**: 中国区域完全支持
- **Amazon S3**: 中国区域完全支持,用于Aurora的持续增量备份

## 验证结果

### 验证类型

⏭️ 已跳过(案例研究类文章)

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 本文为Netflix的技术案例研究,描述了其数据库迁移的决策过程和结果,不包含可部署的代码或配套GitHub项目。文章重点在于分享架构决策、性能对比和最佳实践,而非提供具体的实施教程。按照验证流程,此类案例研究文章在确认服务可用性后无需进行深入验证。

### 关键发现

通过静态分析和服务可用性验证,确认:

1. **服务完全兼容**
   - Aurora PostgreSQL在中国区域提供与全球区域一致的功能
   - 支持共享存储架构、自动故障转移和读副本
   - 存储自动扩展至256 TB,与文章描述一致

2. **Global Database支持**
   - Aurora Global Database在宁夏区域可用
   - 支持跨区域异步复制,复制延迟通常小于1秒
   - 适用于需要多区域部署的场景

3. **性能特性**
   - 日志写入机制和共享存储架构在中国区域完全支持
   - 跨可用区的高可用性架构可在中国区域实现
   - 自动备份到S3的功能完全可用

## 实施建议

### 推荐方案

可直接参考文章中的架构设计和迁移策略在中国区域实施:

1. **评估现有数据库**
   - 使用文章提到的四个维度评估标准
   - 识别单区域和多区域工作负载
   - 评估是否需要Aurora Global Database

2. **选择合适的Aurora版本**
   - 中国区域支持PostgreSQL 11至17的多个版本
   - 建议选择与现有PostgreSQL版本兼容的Aurora版本
   - 考虑使用较新版本以获得更好的性能

3. **迁移实施**
   - 利用Aurora的PostgreSQL兼容性最小化代码更改
   - 使用AWS Database Migration Service进行数据迁移
   - 参考文章中的性能优化建议

4. **配置注意事项**
   - 确保在三个可用区部署以实现高可用性
   - 配置适当数量的读副本(最多15个)
   - 启用自动备份和存储自动扩展
   - 使用Aurora Serverless v2以优化成本(中国区域支持)

### 替代方案

如果Aurora PostgreSQL不适合特定场景,可考虑:

1. **Amazon RDS for PostgreSQL**
   - 实施方式: 使用托管的PostgreSQL服务
   - 复杂度: 低
   - 适用场景: 不需要Aurora高级特性的标准PostgreSQL工作负载

2. **自管理PostgreSQL on EC2**
   - 实施方式: 在EC2上部署PostgreSQL
   - 复杂度: 高
   - 适用场景: 需要完全控制数据库配置的特殊需求

### 风险提示

- **区域限制**: 如需使用Aurora Global Database进行跨境复制,需注意中国区域与全球区域的网络连接和合规要求
- **功能差异**: 某些最新的Aurora功能可能在中国区域的发布时间略晚于全球区域,建议在实施前确认具体功能的可用性
- **成本考虑**: 中国区域的定价可能与全球区域有所不同,建议使用AWS中国区域定价计算器进行成本评估
- **迁移规划**: 大规模数据库迁移需要详细的测试和回滚计划,建议先在非生产环境验证

### 配套资源

- **GitHub仓库**: 无(本文为案例研究,不包含配套代码)
- **相关文档**: 
  - [Amazon Aurora 用户指南(中国区域)](https://docs.amazonaws.cn/AmazonRDS/latest/AuroraUserGuide/)
  - [Aurora PostgreSQL 最佳实践](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.BestPractices.html)
  - [数据库迁移服务文档](https://docs.amazonaws.cn/dms/)
