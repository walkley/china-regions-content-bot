---
title: 介绍Amazon EventBridge事件总线的跨账号目标功能
publish_date: 2025-01-21
original_url: https://aws.amazon.com/blogs/compute/introducing-cross-account-targets-for-amazon-eventbridge-event-buses/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 7
unavailable_services: 0
---

# 介绍Amazon EventBridge事件总线的跨账号目标功能

[📖 查看原始博客](https://aws.amazon.com/blogs/compute/introducing-cross-account-targets-for-amazon-eventbridge-event-buses/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文介绍的EventBridge跨账号目标功能所依赖的所有AWS服务在中国区域均完全可用，配套的GitHub示例项目已在cn-northwest-1区域成功部署和验证。

## 服务分析

### 可用服务 (7个)

- Amazon EventBridge
- Amazon SQS (Simple Queue Service)
- AWS Lambda
- Amazon SNS (Simple Notification Service)
- AWS IAM (Identity and Access Management)
- Amazon CloudWatch Logs
- AWS Serverless Application Model (AWS SAM)

### 不可用服务 (0个)

无

### 评估说明

本文介绍的是Amazon EventBridge的新功能——跨账号目标支持。该功能允许EventBridge事件总线直接将事件发送到其他AWS账号中的目标服务（如SQS、Lambda、SNS），无需在目标账号中创建额外的事件总线作为桥接。

所有涉及的服务在AWS中国区域均完全可用：
1. **Amazon EventBridge** - 核心服务，支持跨账号事件传递
2. **Amazon SQS** - 作为跨账号目标接收事件
3. **AWS Lambda** - 作为跨账号目标处理事件
4. **Amazon SNS** - 作为跨账号目标分发事件
5. **AWS IAM** - 管理跨账号权限和信任关系
6. **Amazon CloudWatch Logs** - 监控和日志记录
7. **AWS SAM** - 用于部署示例项目

该功能在中国区域的实现与全球区域完全一致，包括权限模型、资源策略配置等。

## 验证结果

### 验证类型

✅ GitHub项目部署验证

### 执行状态

**状态**: ✅ 成功

**验证环境**:
- AWS区域: cn-northwest-1
- AWS Profile: cn
- GitHub仓库: https://github.com/aws-samples/eventbridge-cross-account-targets

### 关键发现

1. **部署成功**
   - 成功部署destination-eb-stack（目标账号栈），创建了SQS队列、Lambda函数和SNS主题
   - 成功部署source-eb-stack（源账号栈），创建了EventBridge事件总线和跨账号传递规则
   - 所有CloudFormation资源创建无错误

2. **跨账号事件传递验证成功**
   - 通过EventBridge发送测试事件，事件源设置为"demo.sqs"
   - SQS队列成功接收到跨账号事件，消息体包含完整的事件详情
   - Lambda函数成功被触发，CloudWatch日志显示接收到事件内容
   - SNS主题配置正常（需要邮箱确认订阅）

3. **中国区域特性**
   - ARN格式使用`arn:aws-cn`前缀，符合中国区域规范
   - SQS队列URL使用`.amazonaws.com.cn`域名
   - 所有服务endpoint自动适配中国区域

4. **资源清理**
   - 成功删除所有测试资源
   - 未发现资源残留

## 实施建议

### 推荐方案

可直接按照原文实施，无需任何修改。

**注意事项**：
- 确保源账号和目标账号之间建立了正确的IAM信任关系
- 目标资源（SQS、Lambda、SNS）必须配置资源策略，允许源账号的IAM角色访问
- 在生产环境中，建议为SNS和SQS启用加密（必须使用客户管理的KMS密钥以支持跨账号访问）
- EventBridge规则建议配置死信队列（DLQ）以处理传递失败的事件

### 实施步骤

1. **目标账号配置**
   - 创建目标资源（SQS队列、Lambda函数、SNS主题）
   - 配置资源策略，允许源账号访问
   - 记录目标资源的ARN

2. **源账号配置**
   - 创建EventBridge事件总线
   - 创建IAM执行角色，授予向目标资源发送事件的权限
   - 创建EventBridge规则，配置跨账号目标和执行角色

3. **测试验证**
   - 发送测试事件到源事件总线
   - 验证目标资源是否成功接收事件
   - 检查CloudWatch日志和指标

### 风险提示

- **权限配置复杂性**: 跨账号访问需要在源账号和目标账号两侧都正确配置权限，配置错误会导致事件传递失败
- **成本考虑**: 跨账号事件传递会产生额外的数据传输费用，建议查看EventBridge定价页面
- **监控和调试**: 跨账号场景下的问题排查相对复杂，建议配置完善的日志和监控

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/eventbridge-cross-account-targets
- **兼容性**: 完全兼容中国区域，无需修改
- **修改建议**: 无需修改，可直接使用

### 最佳实践

1. **安全性**
   - 使用最小权限原则配置IAM角色和资源策略
   - 在生产环境启用加密（使用客户管理的KMS密钥）
   - 定期审计跨账号访问权限

2. **可靠性**
   - 为EventBridge规则配置死信队列
   - 设置CloudWatch告警监控事件传递失败
   - 实施重试和错误处理机制

3. **成本优化**
   - 评估跨账号事件传递的频率和数据量
   - 考虑在同一区域内进行跨账号传递以降低成本
   - 使用事件过滤减少不必要的事件传递

## 验证总结

本文介绍的Amazon EventBridge跨账号目标功能在AWS中国区域完全可用，所有核心服务和功能特性与全球区域保持一致。通过实际部署验证，确认了该功能在cn-northwest-1区域的可行性，包括跨账号事件传递、权限配置、以及与SQS、Lambda、SNS的集成。

建议中国区域用户可以放心采用此功能来简化跨账号事件驱动架构，减少中间组件，降低延迟。配套的GitHub示例项目可直接在中国区域使用，无需任何代码或配置修改。
