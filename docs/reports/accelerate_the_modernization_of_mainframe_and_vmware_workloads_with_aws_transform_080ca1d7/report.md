---
title: 使用 AWS Transform 加速大型机和 VMware 工作负载的现代化
publish_date: 2025-05-15
original_url: https://aws.amazon.com/blogs/aws/accelerate-the-modernization-of-mainframe-and-vmware-workloads-with-aws-transform/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 7
unavailable_services: 1
---

# 使用 AWS Transform 加速大型机和 VMware 工作负载的现代化

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/accelerate-the-modernization-of-mainframe-and-vmware-workloads-with-aws-transform/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，无法在中国区域实施

核心服务 AWS Transform 在中国区域不可用，虽然其他支持服务均可用，但整个现代化解决方案完全依赖于 AWS Transform 服务，因此无法在中国区域实施。

## 服务分析

### 可用服务 (7个)

- AWS IAM Identity Center (IdC)
- AWS Key Management Service (AWS KMS)
- AWS Application Discovery Service
- Amazon Virtual Private Cloud (Amazon VPC)
- Amazon Simple Storage Service (Amazon S3)
- AWS Application Migration Service (MGN)
- Amazon Elastic Compute Cloud (Amazon EC2)

### 不可用服务 (1个)

- **AWS Transform** - 核心服务

### 评估说明

AWS Transform 是本文介绍的核心服务，用于自动化大型机和 VMware 工作负载的现代化迁移。该服务包含两个主要功能：

1. **AWS Transform for mainframe**：首个用于大规模现代化大型机工作负载的代理 AI 服务，支持 IBM z/OS、COBOL、CICS、DB2 和 VSAM 的迁移
2. **AWS Transform for VMware**：首个用于 VMware 现代化的代理 AI 服务，自动化应用发现、依赖映射、迁移规划和网络转换

根据官方文档：
- AWS Transform for mainframe 仅在 US East (N. Virginia) 和 Europe (Frankfurt) 区域可用
- AWS Transform for VMware 有不同的可用性选项，但未包含中国区域

由于 AWS Transform 在中国区域（cn-northwest-1）不可用，整个解决方案无法实施。虽然其他支持服务（IAM Identity Center、KMS、S3、EC2 等）在中国区域均可用，但它们只是辅助服务，无法替代 AWS Transform 的核心功能。

## 验证结果

### 验证类型

⏭️ 已跳过

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务 AWS Transform 在中国区域不可用，可行性评估为 LOW，不执行深入验证。

## 实施建议

### 推荐方案

不建议在中国区域实施此方案。AWS Transform 是整个现代化流程的核心，提供以下关键能力：

- 代码分析和依赖关系映射
- 自动化文档生成
- 业务规则逻辑提取
- 代码分解和重构（COBOL 转 Java Spring Boot）
- 迁移波次规划
- VMware 环境发现和网络转换

这些功能无法通过其他服务替代。

### 替代方案

如果需要在中国区域进行大型机或 VMware 工作负载现代化，可以考虑以下替代方案：

1. **传统迁移方法**
   - 实施方式：使用 AWS Application Migration Service (MGN) 进行 VMware 迁移，使用第三方工具或人工方式进行大型机代码转换
   - 复杂度：高
   - 适用场景：需要在中国区域实施，但缺少 AWS Transform 的自动化能力，需要更多人工介入和时间投入

2. **混合区域方案**
   - 实施方式：在全球区域（如 US East 或 Europe Frankfurt）使用 AWS Transform 进行评估、分析和代码转换，然后将转换后的应用部署到中国区域
   - 复杂度：中
   - 适用场景：可以接受在全球区域进行初期分析和转换工作，最终应用运行在中国区域

3. **等待服务上线**
   - 实施方式：等待 AWS Transform 在中国区域上线后再实施
   - 复杂度：低（一旦服务可用）
   - 适用场景：项目时间线允许等待，希望使用最新的代理 AI 能力

### 风险提示

- **服务可用性**: AWS Transform 在中国区域不可用是最大的阻碍因素
- **功能缺失**: 无法使用代理 AI 进行自动化代码分析、转换和迁移规划
- **时间成本**: 使用传统方法将显著增加迁移时间（从月级别延长到年级别）
- **人力成本**: 需要更多专业人员进行手动代码分析和转换工作
- **跨区域合规**: 如采用混合区域方案，需要考虑数据跨境传输的合规性要求

### 配套资源

- **GitHub仓库**: [Import/Export from NSX](https://github.com/awslabs/import-export-for-nsx)
- **兼容性**: 该工具可在中国区域使用，但仅作为 VMware NSX 配置导入导出的辅助工具，无法替代 AWS Transform 的核心功能
- **修改建议**: 无需修改，但该工具本身不足以完成完整的现代化迁移流程
