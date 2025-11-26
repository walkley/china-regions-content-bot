---
title: 将关系数据库归档到Amazon S3 Glacier存储类以优化成本
publish_date: 2025-01-28
original_url: https://aws.amazon.com/blogs/storage/archiving-relational-databases-to-amazon-s3-glacier-storage-classes-for-cost-optimization/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 14
unavailable_services: 0
---

# 将关系数据库归档到Amazon S3 Glacier存储类以优化成本

[📖 查看原始博客](https://aws.amazon.com/blogs/storage/archiving-relational-databases-to-amazon-s3-glacier-storage-classes-for-cost-optimization/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

该解决方案使用的所有AWS服务在中国区域均可用，架构设计完整且成熟，可以直接在cn-northwest-1区域实施。

## 服务分析

### 可用服务 (14个)

- Amazon S3 (包括S3 Glacier存储类)
- AWS Batch
- AWS Lambda
- AWS Secrets Manager
- Amazon DynamoDB
- Amazon EventBridge
- AWS Fargate
- Amazon ECR (Elastic Container Registry)
- Amazon SNS (Simple Notification Service)
- Amazon RDS
- Amazon Aurora
- Amazon CloudWatch
- Amazon VPC (VPC Endpoints)
- Amazon SQS

### 不可用服务 (0个)

无

### 评估说明

该解决方案的所有核心服务在AWS中国区域（cn-northwest-1和cn-north-1）均完全可用：

1. **存储服务**：Amazon S3及其所有Glacier存储类（Instant Retrieval、Flexible Retrieval、Deep Archive）在中国区域完全支持，包括生命周期策略功能。

2. **计算服务**：AWS Batch、AWS Lambda和AWS Fargate在中国区域均可用，支持容器化工作负载的调度和执行。

3. **数据库服务**：Amazon RDS和Amazon Aurora在中国区域完全支持，包括MySQL和PostgreSQL引擎。

4. **编排和监控**：Amazon EventBridge、CloudWatch、SNS和SQS在中国区域均可用，支持完整的事件驱动架构和监控告警。

5. **安全服务**：AWS Secrets Manager在中国区域可用，支持数据库凭证的安全存储和轮换。

## 验证结果

### 验证类型

✅ GitHub项目部署验证

### 执行状态

**状态**: ⚠️ 部分成功

**说明**: 成功验证了所有AWS服务的可用性和基础设施组件的创建，但由于测试环境磁盘空间限制，未能完成完整的Docker镜像构建。

### 关键发现

1. **服务可用性验证**
   - 所有14个AWS服务在cn-northwest-1区域均可用
   - 成功创建了S3存储桶和ECR仓库
   - VPC和子网配置正常，支持Fargate部署

2. **容器镜像构建**
   - 基础镜像（public.ecr.aws/docker/library/ubuntu:24.04）可以正常访问
   - Dockerfile中使用的所有工具（postgresql-client、mariadb-client、AWS CLI）在中国区域均可安装
   - EFS工具需要从源码编译，构建过程较为复杂

3. **中国区域特定配置**
   - ECR endpoint使用.amazonaws.com.cn域名
   - S3 endpoint使用.amazonaws.com.cn域名
   - IAM ARN使用aws-cn分区前缀
   - 所有AWS服务endpoint均需使用中国区域特定的域名

4. **CloudFormation模板兼容性**
   - 模板结构完整，支持中国区域部署
   - IAM角色和策略配置正确使用了AWS::Partition伪参数
   - 需要确保VPC endpoints配置正确以保持流量在AWS内部网络

## 实施建议

### 推荐方案

该解决方案可以直接在AWS中国区域实施，建议按照以下步骤进行：

**部署前准备**：
1. 确保有足够的磁盘空间（至少20GB）用于构建Docker镜像
2. 准备VPC和子网，配置必要的VPC endpoints（S3、ECR、Secrets Manager、DynamoDB）
3. 创建S3存储桶并配置生命周期策略

**部署步骤**：
1. 在有足够资源的环境中构建Docker镜像（推荐使用EC2实例或本地开发环境）
2. 将镜像推送到中国区域的ECR仓库
3. 部署CloudFormation模板，注意使用中国区域的参数
4. 在Secrets Manager中创建数据库凭证（使用cold-archiving/前缀）
5. 配置EventBridge定时任务
6. 为需要归档的RDS实例添加标签

**注意事项**：
- 确保所有AWS服务endpoint使用.amazonaws.com.cn域名
- IAM策略中的ARN需要使用aws-cn分区
- 建议在私有子网中运行Fargate任务，通过VPC endpoints访问AWS服务
- S3 Glacier存储类的最小存储期限要求（90天或180天）需要纳入成本计算

### 替代方案

如果不希望使用容器化方案，可以考虑以下替代方案：

1. **Lambda函数方案**
   - 实施方式：使用Lambda函数直接执行数据库备份，将备份文件上传到S3
   - 复杂度：中
   - 适用场景：小型数据库（<10GB），备份时间<15分钟
   - 限制：Lambda执行时间限制为15分钟，临时存储空间限制为10GB

2. **EC2定时任务方案**
   - 实施方式：在EC2实例上配置cron任务执行数据库备份
   - 复杂度：低
   - 适用场景：需要更灵活的备份策略，或数据库规模较大
   - 优势：无执行时间限制，可以处理大型数据库

### 风险提示

- **恢复时间**：从S3 Glacier Flexible Retrieval或Deep Archive恢复数据需要数分钟到数小时，不适合需要快速恢复的场景
- **成本考虑**：S3 Glacier存储类有最小存储期限要求，提前删除会产生额外费用
- **数据完整性**：数据库dump文件需要定期验证完整性，建议实施恢复测试流程
- **网络依赖**：备份过程依赖网络连接，大型数据库备份可能需要较长时间
- **凭证管理**：确保Secrets Manager中的数据库凭证定期轮换，遵循安全最佳实践

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/Archiving-RDBMs-for-cost-reduction.git
- **兼容性**: 完全兼容中国区域
- **修改建议**: 
  - 在资源受限的环境中构建Docker镜像时，建议使用更大的实例类型或增加磁盘空间
  - 可以考虑预构建镜像并存储在ECR中，避免每次都重新构建
  - 建议在CloudFormation模板中添加更多的中国区域特定配置说明
  - 可以优化Dockerfile，使用多阶段构建减少最终镜像大小
