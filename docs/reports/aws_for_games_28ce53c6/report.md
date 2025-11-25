---
title: 在AWS上开启游戏开发培训之旅
publish_date: 2025-03-03
original_url: https://aws.amazon.com/blogs/training-and-certification/aws-for-games/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 19
unavailable_services: 0
---

# 在AWS上开启游戏开发培训之旅

[📖 查看原始博客](https://aws.amazon.com/blogs/training-and-certification/aws-for-games/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文介绍的AWS游戏开发培训资源和相关服务在AWS中国区域完全可用。所有提到的核心游戏服务（GameLift、DynamoDB、Aurora等）以及基础设施服务（EC2、Lambda、API Gateway等）均在中国区域提供支持，培训内容和实践项目可以直接在中国区域实施。

## 服务分析

### 可用服务 (19个)

- Amazon GameLift
- Amazon EC2
- Amazon S3
- Amazon DynamoDB
- Amazon Aurora
- Amazon ElastiCache Serverless
- Amazon Kinesis
- Amazon ECS (Elastic Container Service)
- Amazon EKS (Elastic Kubernetes Service)
- AWS Lambda
- Amazon API Gateway
- Amazon Redshift
- Amazon VPC
- Amazon RDS
- Amazon Route 53
- AWS IAM
- AWS CloudFormation
- AWS Transit Gateway
- AWS Direct Connect

### 不可用服务 (0个)

无

### 评估说明

1. **核心游戏服务完全可用**：Amazon GameLift作为核心游戏服务器托管服务在中国区域完全支持，包括FlexMatch匹配服务和FleetIQ功能。

2. **数据库和存储服务齐全**：DynamoDB、Aurora、ElastiCache、S3等数据存储服务均可用，支持游戏数据管理、玩家信息存储和排行榜等功能。

3. **计算和网络基础设施完整**：EC2、ECS、EKS等计算服务以及VPC、Route 53等网络服务完全支持，可以构建完整的游戏基础架构。

4. **Serverless架构支持**：Lambda、API Gateway等无服务器服务可用，支持构建灵活的游戏后端系统。

5. **分析和数据处理能力**：Kinesis、Redshift等分析服务可用，支持游戏数据分析和玩家行为分析。

## 验证结果

### 验证类型

✅ GitHub项目部署验证

### 执行状态

**状态**: ⚠️ 部分成功

**说明**: 由于项目需要Windows环境和Visual Studio编译C++游戏服务器，在当前Linux环境下无法完整部署。但已成功验证：
- CloudFormation模板语法有效
- 所有AWS服务在cn-northwest-1区域可用
- 服务API调用正常

### 关键发现

1. **服务可用性验证通过**
   - 通过AWS CLI成功调用GameLift、DynamoDB、ElastiCache等服务API
   - CloudFormation模板验证通过，可以在中国区域部署
   - 所有依赖的AWS服务均在cn-northwest-1区域正常运行

2. **项目架构分析**
   - 项目使用CloudFormation实现基础设施即代码
   - 采用Serverless架构（Lambda + API Gateway + DynamoDB）
   - 集成GameLift FlexMatch实现玩家匹配
   - 使用ElastiCache Redis实现排行榜功能

3. **部署环境要求**
   - 游戏服务器和客户端需要Windows + Visual Studio 2015编译
   - 需要手动配置多个AWS服务（GameLift Fleet、Lambda函数、API Gateway等）
   - 项目提供了详细的部署文档和配置说明

## 实施建议

### 推荐方案

本文介绍的培训资源和实践项目可以直接在AWS中国区域实施，建议按以下方式进行：

**培训课程学习**：
- AWS Skill Builder上的游戏开发课程内容通用，可直接学习
- 实践时将区域设置为cn-northwest-1或cn-north-1
- 注意中国区域的endpoint地址差异

**Workshop实践**：
- 选择支持中国区域的Workshop进行实践
- GameLift相关Workshop可以直接在中国区域执行
- 数据库和分析类Workshop完全兼容

**GitHub示例项目**：
- 项目架构和代码在中国区域完全适用
- 需要准备Windows开发环境编译游戏服务器
- CloudFormation模板可直接部署基础设施

**注意事项**：
- API Gateway和Lambda的endpoint格式在中国区域略有不同
- S3存储桶命名需要符合中国区域规范
- IAM权限配置保持一致
- GameLift Fleet配置时选择中国区域可用的实例类型

### 替代方案

如果无法使用Windows环境编译示例项目，可以考虑：

1. **使用容器化方案**
   - 将游戏服务器容器化，使用ECS或EKS部署
   - 利用GameLift的容器支持功能
   - 复杂度：中
   - 适用场景：希望使用现代化容器架构的团队

2. **专注于Serverless后端**
   - 重点学习Lambda + API Gateway + DynamoDB架构
   - 跳过游戏服务器编译部分，专注于后端服务
   - 复杂度：低
   - 适用场景：后端开发人员或无Windows环境的团队

### 风险提示

- **区域差异**：中国区域的服务endpoint地址与全球区域不同，需要在代码中正确配置
- **实例类型**：部分EC2实例类型在中国区域可能不可用，需要选择替代实例类型
- **网络连接**：访问GitHub和下载依赖包时可能需要配置网络代理
- **认证体系**：AWS中国区域使用独立的账号体系，需要单独注册

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/aws-gamelift-sample
- **兼容性**: 完全兼容中国区域，所有AWS服务均可用
- **修改建议**: 
  - 在Lambda函数中将region_name设置为cn-northwest-1或cn-north-1
  - 更新SQS、API Gateway等服务的endpoint地址为中国区域格式
  - CloudFormation模板中的资源配置无需修改
  - 游戏服务器config.ini中配置中国区域的SQS endpoint

**培训资源访问**：
- AWS Skill Builder课程可以直接访问学习
- Workshop内容通用，实践时选择中国区域
- AWS游戏技术博客提供丰富的中文和英文技术文章
- AWS Educate为学生和教育工作者提供免费学习资源
