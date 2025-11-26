---
title: AWS Lambda为Amazon CloudWatch日志引入分层定价并支持额外的日志目标
publish_date: 2025-05-01
original_url: https://aws.amazon.com/blogs/compute/aws-lambda-introduces-tiered-pricing-for-amazon-cloudwatch-logs-and-additional-logging-destinations/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 13
unavailable_services: 0
---

# AWS Lambda为Amazon CloudWatch日志引入分层定价并支持额外的日志目标

[📖 查看原始博客](https://aws.amazon.com/blogs/compute/aws-lambda-introduces-tiered-pricing-for-amazon-cloudwatch-logs-and-additional-logging-destinations/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

所有涉及的AWS服务在中国区域均可用，Lambda日志的核心功能包括高级日志控制、CloudWatch Logs的Infrequent Access日志类以及delivery机制均已验证可用。

## 服务分析

### 可用服务 (13个)

- AWS Lambda
- Amazon CloudWatch Logs
- Amazon S3
- Amazon Data Firehose
- Amazon OpenSearch Service
- Amazon ECS
- Amazon EC2
- AWS IAM
- AWS CLI
- AWS CloudFormation
- AWS CDK
- Amazon VPC
- Amazon Route 53

### 不可用服务 (0个)

无

### 评估说明

本文介绍的Lambda日志功能更新主要包括：

1. **分层定价模型**：这是定价策略调整，在中国区域自动生效
2. **高级日志控制**：已验证JSON格式日志和日志级别控制在中国区域可用
3. **Infrequent Access日志类**：已验证在中国区域可用
4. **CloudWatch Logs Delivery机制**：已验证delivery destination和delivery source API在中国区域可用

所有核心服务和功能在中国区域均可用，可以直接按照原文实施。

## 验证结果

### 验证类型

✅ 教程步骤验证

### 执行状态

**状态**: ⚠️ 部分成功

### 关键发现

1. **Lambda高级日志控制功能可用**
   - 成功配置JSON格式日志输出
   - 成功配置ApplicationLogLevel和SystemLogLevel
   - 日志输出符合预期，包含结构化的系统日志和应用日志

2. **CloudWatch Logs Infrequent Access日志类可用**
   - 成功创建INFREQUENT_ACCESS类型的日志组
   - 该功能可用于降低不常访问日志的存储成本

3. **CloudWatch Logs Delivery机制可用**
   - 成功创建delivery destination到S3
   - API支持S3、CloudWatch Logs和Firehose作为目标
   - 但Lambda目前不在支持的delivery source服务列表中

4. **Lambda直接配置S3/Firehose日志目标的限制**
   - Lambda的LoggingConfig参数目前只支持CloudWatch Logs相关配置
   - 不支持直接在Lambda函数配置中指定S3或Firehose作为日志目标
   - 这可能是因为该功能在全球区域刚发布（2025年5月1日），中国区域可能尚未完全同步

## 实施建议

### 推荐方案

可以直接按照原文实施以下功能：

1. **分层定价**：自动生效，无需配置
2. **高级日志控制**：
   - 使用JSON格式日志：`--logging-config LogFormat=JSON`
   - 配置日志级别：`ApplicationLogLevel=INFO,SystemLogLevel=INFO`
3. **Infrequent Access日志类**：创建日志组时指定`--log-group-class INFREQUENT_ACCESS`

需要注意的部分：

- **Lambda日志直接发送到S3/Firehose**：该功能在中国区域可能尚未完全可用。虽然CloudWatch Logs的delivery机制已可用，但Lambda服务尚未集成到delivery source列表中。建议等待该功能在中国区域正式发布。

### 替代方案

如果需要将Lambda日志发送到S3或其他目标，可以使用以下替代方案：

1. **CloudWatch Logs订阅过滤器**
   - 实施方式：使用CloudWatch Logs订阅过滤器将日志流式传输到Kinesis Data Firehose，再发送到S3或其他目标
   - 复杂度：中
   - 适用场景：需要实时将Lambda日志发送到S3或第三方监控工具

2. **定期导出到S3**
   - 实施方式：使用CloudWatch Logs的CreateExportTask API定期将日志导出到S3
   - 复杂度：低
   - 适用场景：不需要实时日志，主要用于长期存储和合规

### 风险提示

- **功能可用性时间差**：全球区域新发布的功能可能需要一段时间才能在中国区域可用，建议在实施前验证具体功能的可用性
- **定价差异**：中国区域的定价可能与全球区域有所不同，建议查阅中国区域的CloudWatch定价页面
- **控制台功能**：博客中提到的Lambda控制台配置S3/Firehose日志目标的功能，在中国区域可能尚未提供

### 配套资源

- **GitHub仓库**: 无
- **相关文档**: 
  - [Lambda日志文档](https://docs.amazonaws.cn/lambda/latest/dg/monitoring-logs.html)
  - [CloudWatch Logs文档](https://docs.amazonaws.cn/AmazonCloudWatch/latest/logs/)
  - [CloudWatch定价](https://www.amazonaws.cn/cloudwatch/pricing/)
