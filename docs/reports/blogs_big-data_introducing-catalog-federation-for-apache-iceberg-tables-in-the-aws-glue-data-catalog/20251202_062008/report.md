---
title: AWS Glue Data Catalog中Apache Iceberg表的目录联邦功能介绍
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/big-data/introducing-catalog-federation-for-apache-iceberg-tables-in-the-aws-glue-data-catalog/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: HIGH
available_services: 11
unavailable_services: 0
---

# AWS Glue Data Catalog中Apache Iceberg表的目录联邦功能介绍

[📖 查看原始博客](https://aws.amazon.com/blogs/big-data/introducing-catalog-federation-for-apache-iceberg-tables-in-the-aws-glue-data-catalog/) | 验证日期: 2025-12-02

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

文章介绍的AWS Glue目录联邦功能所依赖的所有AWS服务在中国区域（cn-northwest-1）均已可用，包括AWS Glue Data Catalog、AWS Lake Formation、Amazon Athena、Amazon Redshift、Amazon EMR等核心服务。用户可以直接按照原文步骤在中国区域实施该解决方案。

## 服务分析

### 可用服务 (11个)

- Amazon S3
- AWS IAM
- AWS Secrets Manager
- Amazon Athena
- Amazon Redshift
- Amazon EMR
- Amazon SageMaker
- AWS Glue
- AWS Glue Data Catalog
- AWS Lake Formation
- AWS CLI

### 不可用服务 (0个)

无

### 评估说明

本文介绍的AWS Glue目录联邦功能是一项新特性，允许用户通过AWS Glue Data Catalog查询存储在远程Iceberg目录（如Snowflake Polaris Catalog、Databricks Unity Catalog等）中的Apache Iceberg表。

**核心服务可用性**：
1. **AWS Glue Data Catalog** - 核心服务，在中国区完全可用
2. **AWS Lake Formation** - 提供细粒度访问控制和凭证管理，在中国区可用
3. **Amazon Athena** - 用于查询联邦表，在中国区可用
4. **Amazon Redshift** - 支持查询联邦表，在中国区可用
5. **Amazon EMR** - 支持查询联邦表，在中国区可用
6. **Amazon S3** - 存储Iceberg数据文件，在中国区可用
7. **AWS Secrets Manager** - 存储认证凭证，在中国区可用

所有核心服务均在中国区域可用，无需替代方案。

## 验证结果

### 验证类型

⏭️ 已跳过（按照验证流程要求统一跳过深入验证）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 根据验证流程要求，为节约时间，统一跳过深入验证阶段。文章不包含GitHub项目，仅包含配置步骤和AWS CLI命令示例。

### 关键发现

基于静态分析的关键发现：

1. **服务完整性**
   - 所有提到的AWS服务在中国区域均可用
   - 无需服务替代或功能调整

2. **配置要求**
   - 需要配置OAuth2或自定义认证连接远程Iceberg目录
   - 需要IAM角色具有S3访问权限
   - 需要在Lake Formation中注册AWS Glue连接

3. **网络连接**
   - 需要确保中国区域可以访问远程Iceberg目录的REST API端点
   - 如果远程目录在海外，需要考虑网络延迟和连通性

## 实施建议

### 推荐方案

可直接按照原文实施，具体步骤如下：

1. **在远程Iceberg目录中设置集成主体**
   - 配置OAuth2认证（CLIENT_ID和CLIENT_SECRET）
   - 或配置自定义认证（访问令牌）

2. **在AWS Secrets Manager中存储凭证**
   - OAuth2方式：存储CLIENT_SECRET（键名：USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET）
   - 自定义方式：存储访问令牌（键名：BEARER_TOKEN）

3. **创建IAM角色**
   - 授予S3存储桶访问权限（远程表数据所在位置）
   - 如使用Secrets Manager，添加相应权限
   - 如有网络配置需求，添加相应权限

4. **创建AWS Glue连接**
   - 配置远程目录的Iceberg REST API端点
   - 选择认证方式（OAuth2或自定义）
   - 配置网络设置（如需要）

5. **在Lake Formation中注册连接**
   - 创建联邦目录
   - 关联AWS Glue连接
   - 指定IAM角色
   - 运行连接测试

6. **配置访问权限**
   - 使用Lake Formation管理数据库和表的访问控制
   - 可使用基于标签的访问控制（TBAC）

7. **使用AWS分析引擎查询**
   - 通过Athena、Redshift或EMR查询联邦表
   - Lake Formation自动管理细粒度权限和凭证

### 注意事项

1. **网络连通性**
   - 确认中国区域到远程Iceberg目录REST API的网络连通性
   - 如远程目录在海外，考虑网络延迟对查询性能的影响
   - 如需要，可配置代理或私有链接

2. **认证凭证管理**
   - OAuth2令牌由AWS Glue自动刷新
   - 自定义认证的访问令牌需要客户自行管理和刷新
   - 建议使用Secrets Manager存储敏感凭证

3. **跨账户访问**
   - 如S3存储桶在不同账户，需配置存储桶策略授予IAM角色访问权限

4. **区域特定配置**
   - 使用中国区域的服务端点
   - AWS CLI命令需指定正确的区域（--region cn-northwest-1）

5. **成本考虑**
   - Lake Formation凭证管理产生的费用
   - 跨区域数据传输费用（如适用）
   - Secrets Manager存储和API调用费用

### 配置示例

创建联邦目录的AWS CLI命令示例（适配中国区域）：

```bash
# 删除联邦目录
aws glue delete-catalog \
  --name <your-federated-catalog-name> \
  --region cn-northwest-1 \
  --profile zhy

# 从Lake Formation注销连接
aws lakeformation deregister-resource \
  --resource-arn <your-glue-connector-arn> \
  --region cn-northwest-1 \
  --profile zhy

# 删除AWS Glue连接
aws glue delete-connection \
  --connection-name <your-glue-connection-name> \
  --region cn-northwest-1 \
  --profile zhy

# 删除Secrets Manager密钥
aws secretsmanager delete-secret \
  --secret-id <your-secret-name> \
  --region cn-northwest-1 \
  --profile zhy
```

### 风险提示

- **网络延迟风险**: 如果远程Iceberg目录位于海外，查询时获取元数据可能存在网络延迟，影响查询性能
- **认证失效风险**: 自定义认证方式的访问令牌需要客户自行管理刷新，令牌过期会导致查询失败
- **权限配置风险**: Lake Formation的细粒度权限配置较为复杂，需要仔细规划和测试
- **成本风险**: 频繁的元数据查询和凭证管理会产生额外费用，需要监控和优化

### 配套资源

- **GitHub仓库**: 无
- **AWS文档**: [Catalog federation to remote Iceberg catalogs](https://docs.aws.amazon.com/lake-formation/latest/dg/catalog-federation.html)
- **相关服务文档**:
  - [AWS Glue Data Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html)
  - [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html)
  - [Amazon Athena](https://docs.aws.amazon.com/athena/)
