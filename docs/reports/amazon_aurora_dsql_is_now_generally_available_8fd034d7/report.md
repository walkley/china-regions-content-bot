---
title: Amazon Aurora DSQL 正式发布，最快的无服务器分布式SQL数据库
publish_date: 2025-05-27
original_url: https://aws.amazon.com/blogs/aws/amazon-aurora-dsql-is-now-generally-available/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 10
unavailable_services: 2
---

# Amazon Aurora DSQL 正式发布，最快的无服务器分布式SQL数据库

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/amazon-aurora-dsql-is-now-generally-available/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，无法在中国区域实施

Amazon Aurora DSQL是博客介绍的核心服务，目前在AWS中国区域完全不可用。该服务是一个全新的分布式SQL数据库产品，仅在特定的全球区域提供服务，中国区域尚未推出且无明确上线计划。

## 服务分析

### 可用服务 (10个)

- AWS CloudShell
- AWS Lambda
- AWS Backup
- AWS PrivateLink
- AWS CloudFormation
- AWS CloudTrail
- AWS SDK
- AWS CLI
- AWS IAM
- PostgreSQL兼容工具（psql, DBeaver, DataGrip）

### 不可用服务 (2个)

- **Amazon Aurora DSQL** - 核心服务，博客的主要内容
- **Amazon Q Developer CLI** - 辅助开发工具

### 评估说明

虽然博客中提到的大部分辅助服务（如CloudShell、Lambda、Backup等）在中国区域都可用，但核心服务Amazon Aurora DSQL本身在中国区域完全不可用。这是一个2024年re:Invent大会上发布的全新数据库服务，具有以下特点：

1. **分布式架构**：采用disaggregated架构，包含查询处理器、仲裁器、日志和交叉开关等独立组件
2. **多区域强一致性**：支持active-active多区域部署，提供99.999%可用性
3. **无服务器**：自动扩展，无需管理基础设施
4. **PostgreSQL兼容**：支持PostgreSQL协议和工具

由于这是一个全新的专有服务，没有直接的替代方案可以实现相同的功能特性。

## 验证结果

### 验证类型

⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Aurora DSQL在AWS中国区域不可用，无法进行实际部署验证。该服务是博客的唯一主题，没有可行的实施路径。

## 实施建议

### 推荐方案

**不建议在中国区域实施此方案**

Amazon Aurora DSQL是一个全新的专有数据库服务，目前仅在以下区域可用：
- 美国东部（弗吉尼亚北部）
- 美国东部（俄亥俄）
- 美国西部（俄勒冈）
- 亚太地区（大阪）
- 亚太地区（东京）
- 欧洲（爱尔兰）
- 欧洲（伦敦）
- 欧洲（巴黎）

中国区域（cn-north-1和cn-northwest-1）不在支持列表中，且没有公开的上线时间表。

### 替代方案

如果需要在AWS中国区域实现类似的分布式数据库功能，可以考虑以下替代方案：

1. **Amazon Aurora PostgreSQL（全球数据库）**
   - 实施方式：使用Aurora PostgreSQL的全球数据库功能实现跨区域复制
   - 复杂度：中
   - 适用场景：需要跨区域数据复制，但可以接受最终一致性（而非强一致性）
   - 限制：不支持active-active写入，主区域故障需要手动故障转移

2. **Amazon RDS for PostgreSQL + 自建复制**
   - 实施方式：使用RDS PostgreSQL配合逻辑复制或第三方工具实现多区域部署
   - 复杂度：高
   - 适用场景：需要更多控制权和自定义配置
   - 限制：需要自行管理复制逻辑，运维复杂度高

3. **自建分布式数据库**
   - 实施方式：在EC2上部署开源分布式数据库（如CockroachDB、YugabyteDB）
   - 复杂度：高
   - 适用场景：需要完全控制和自定义能力
   - 限制：需要自行管理所有基础设施和运维工作

### 风险提示

- **服务不可用**：Amazon Aurora DSQL在中国区域完全不可用，无法使用博客中介绍的任何功能
- **无上线时间表**：AWS尚未公布该服务在中国区域的上线计划
- **架构差异**：替代方案无法完全复制Aurora DSQL的独特架构特性（如多区域强一致性、active-active写入）
- **性能差距**：Aurora DSQL声称是"最快的分布式SQL数据库"，替代方案可能无法达到相同的性能水平
- **功能缺失**：Aurora DSQL的特有功能（如自动扩展、零停机维护）在替代方案中可能需要额外开发

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/aurora-dsql-samples
- **兼容性**: 不适用于中国区域
- **Workshop**: https://catalog.workshops.aws/aurora-dsql/ （仅适用于支持Aurora DSQL的区域）
- **修改建议**: 由于核心服务不可用，无法通过简单修改使其在中国区域运行
