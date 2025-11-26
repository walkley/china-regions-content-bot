---
title: 使用Docker容器在本地开发和测试AWS Glue 5.0作业
publish_date: 2025-03-12
original_url: https://aws.amazon.com/blogs/big-data/develop-and-test-aws-glue-5-0-jobs-locally-using-a-docker-container/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 9
unavailable_services: 0
---

# 使用Docker容器在本地开发和测试AWS Glue 5.0作业

[📖 查看原始博客](https://aws.amazon.com/blogs/big-data/develop-and-test-aws-glue-5-0-jobs-locally-using-a-docker-container/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文介绍的AWS Glue 5.0 Docker容器本地开发方案完全适用于中国区域。所有涉及的AWS服务均在中国区域可用，Docker镜像可正常拉取和运行，仅需调整endpoint配置即可。

## 服务分析

### 可用服务 (9个)

- AWS Glue
- Amazon SageMaker
- Amazon EC2
- Amazon ECR (Elastic Container Registry)
- Amazon S3
- Amazon Redshift
- Amazon DynamoDB
- AWS IAM
- AWS Lake Formation

### 不可用服务 (0个)

无

### 评估说明

1. **核心服务完全可用**：AWS Glue、Amazon ECR、Amazon S3等所有核心服务均在中国区域（cn-northwest-1和cn-north-1）可用
2. **Docker镜像可访问**：ECR Public Gallery的AWS Glue镜像可以正常拉取，支持x86_64和arm64架构
3. **本地开发特性**：本文主要介绍本地Docker容器开发，不依赖特定AWS区域的云端资源
4. **区域配置简单**：只需配置正确的endpoint URL即可适配中国区域

## 验证结果

### 验证类型

✅ 教程步骤验证

### 执行状态

**状态**: ✅ 成功

### 关键发现

1. **Docker镜像拉取成功**
   - 成功从ECR Public Gallery拉取`public.ecr.aws/glue/aws-glue-libs:5`镜像
   - 镜像大小约4.82GB，包含完整的Glue 5.0运行环境
   - 包含Spark 3.5.4、Python 3.11、Iceberg 1.7.1、Hudi 0.15.0、Delta Lake 3.3.0等组件

2. **spark-submit方式验证通过**
   - 成功运行Glue ETL脚本
   - GlueContext和Job初始化正常
   - Spark DataFrame操作正常

3. **pytest单元测试验证通过**
   - 成功执行pytest测试框架
   - GlueContext创建测试通过
   - Spark DataFrame操作测试通过
   - 测试执行时间约7.6秒

4. **中国区域endpoint配置验证**
   - 成功配置S3 endpoint为`s3.cn-northwest-1.amazonaws.com.cn`
   - 区域配置`cn-northwest-1`生效
   - Glue服务endpoint自动识别为`https://glue.cn-northwest-1.amazonaws.com.cn`
   - Lake Formation endpoint自动识别为`https://lakeformation.cn-northwest-1.amazonaws.com.cn`

5. **区域差异说明**
   - 示例代码中使用的`s3://awsglue-datasets`存储桶位于全球区域，中国区域无法访问
   - 这是预期的区域隔离，不影响功能可用性
   - 用户需要使用中国区域的S3存储桶

## 实施建议

### 推荐方案

可直接按照原文实施，仅需注意以下配置调整：

**必要的配置调整**：

1. **S3 Endpoint配置**
   ```python
   spark.conf.set("spark.hadoop.fs.s3a.endpoint", "s3.cn-northwest-1.amazonaws.com.cn")
   spark.conf.set("spark.hadoop.fs.s3a.endpoint.region", "cn-northwest-1")
   ```

2. **AWS Profile配置**
   - 使用中国区域的AWS凭证
   - 确保IAM权限配置正确

3. **S3存储桶**
   - 使用中国区域的S3存储桶（cn-northwest-1或cn-north-1）
   - 不要使用全球区域的示例数据集

**开发环境设置**：

1. **Docker环境要求**
   - Docker已安装并运行
   - 至少7GB磁盘空间
   - 支持Linux容器（Windows需切换到Linux容器模式）

2. **AWS凭证配置**
   ```bash
   # 配置中国区域profile
   aws configure --profile cn
   # 设置区域为cn-northwest-1或cn-north-1
   ```

3. **运行容器示例**
   ```bash
   docker run -it --rm \
       -v ~/.aws:/home/hadoop/.aws \
       -v $WORKSPACE_LOCATION:/home/hadoop/workspace/ \
       -e AWS_PROFILE=cn \
       -e AWS_REGION=cn-northwest-1 \
       --name glue5_dev \
       public.ecr.aws/glue/aws-glue-libs:5 \
       pyspark
   ```

### 替代方案

无需替代方案，原方案完全适用。

### 风险提示

- **网络访问**：确保能够访问ECR Public Gallery拉取Docker镜像，首次拉取需要较长时间
- **存储空间**：Docker镜像约5GB，确保有足够的磁盘空间
- **区域隔离**：中国区域与全球区域资源隔离，不能跨区域访问S3等资源
- **功能限制**：文章末尾列出的不支持功能（如Job bookmarks、Data Quality等）在容器环境中不可用，这是容器本身的限制，不是区域限制
- **Lake Formation**：虽然Lake Formation在中国区域可用，但容器镜像不支持Lake Formation权限管理功能

### 配套资源

- **Docker镜像**：`public.ecr.aws/glue/aws-glue-libs:5`
- **兼容性**：完全兼容中国区域
- **架构支持**：x86_64和arm64
- **修改建议**：
  - 在代码中添加中国区域endpoint配置
  - 使用中国区域的S3存储桶替换示例中的全球区域存储桶
  - 确保AWS凭证配置为中国区域

### 最佳实践

1. **本地开发流程**
   - 使用Docker容器进行本地开发和测试
   - 通过pytest编写单元测试
   - 使用Visual Studio Code进行交互式开发

2. **CI/CD集成**
   - 将Docker容器集成到CI/CD流程
   - 在部署到AWS Glue之前进行本地验证
   - 使用pytest进行自动化测试

3. **版本管理**
   - 使用Glue 5.0获得最新的Spark 3.5.4性能优化
   - 注意Glue 4.0到5.0的迁移变化（用户名从glue_user改为hadoop等）

4. **扩展功能**
   - 可以通过Dockerfile扩展添加JupyterLab和Livy
   - 可以添加自定义JDBC驱动和Python库
   - 可以配置Spark history server进行调试
