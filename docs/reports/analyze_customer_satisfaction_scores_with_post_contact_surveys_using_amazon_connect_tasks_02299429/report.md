---
title: 使用Amazon Connect Tasks通过联系后调查分析客户满意度评分
publish_date: 2025-11-12
original_url: https://aws.amazon.com/blogs/contact-center/analyze-customer-satisfaction-scores-with-post-contact-surveys-using-amazon-connect-tasks/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 10
unavailable_services: 1
---

# 使用Amazon Connect Tasks通过联系后调查分析客户满意度评分

[📖 查看原始博客](https://aws.amazon.com/blogs/contact-center/analyze-customer-satisfaction-scores-with-post-contact-surveys-using-amazon-connect-tasks/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务Amazon Connect在中国区不可用，整个解决方案无法实施

该博客的核心服务Amazon Connect（包括Amazon Connect Tasks）在AWS中国区域完全不可用。由于整个解决方案架构完全依赖于Amazon Connect作为联络中心平台，没有Amazon Connect就无法实现任何功能，因此该方案在中国区域无法实施。

## 服务分析

### 可用服务 (10个)

- Amazon S3
- Amazon CloudFront
- Amazon Cognito
- Amazon DynamoDB
- Amazon Lex
- Amazon API Gateway
- AWS Lambda
- AWS CloudFormation
- AWS IAM
- Contact Lens for Amazon Connect（理论可用但依赖Amazon Connect）

### 不可用服务 (1个)

- **Amazon Connect** - 核心服务，整个解决方案的基础平台

### 评估说明

Amazon Connect是AWS提供的云联络中心服务，是本解决方案的核心和基础。该博客介绍的所有功能都建立在Amazon Connect之上：

1. **核心依赖**：整个解决方案围绕Amazon Connect构建，包括：
   - Contact Flow（联系流程）
   - Contact Flow Module（联系流程模块）
   - Amazon Connect Tasks（任务功能）
   - 语音/聊天/任务的全渠道联络中心能力

2. **架构依赖**：解决方案架构图显示Amazon Connect是数据流的中心节点，所有调查流程都通过Contact Flow Module执行

3. **功能依赖**：
   - 联系后调查的触发和执行
   - 调查结果的任务创建和分配
   - 与客户的交互（语音、聊天）

由于Amazon Connect在中国区域不可用，即使其他10个服务都可用，也无法实现该解决方案的任何核心功能。

## 验证结果

### 验证类型

- ⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Connect在AWS中国区域（cn-northwest-1和cn-north-1）完全不可用。通过AWS CLI测试确认该服务的endpoint在中国区域无法访问。由于整个解决方案完全依赖Amazon Connect作为联络中心平台，没有该服务就无法进行任何实际部署验证。

**技术验证详情**：
- 尝试访问 `https://connect.cn-northwest-1.amazonaws.com.cn/instance` 失败
- AWS CLI命令 `aws connect list-instances` 在中国区域返回endpoint连接错误
- 确认Amazon Connect在不可用服务列表中

## 实施建议

### 推荐方案

**不建议在AWS中国区域实施此解决方案**

由于Amazon Connect服务在中国区域不可用，该博客介绍的完整解决方案无法在AWS中国区域部署和使用。

### 替代方案

如果您需要在中国区域实现类似的客户满意度调查功能，可以考虑以下替代方案：

1. **使用第三方联络中心平台**
   - 实施方式：集成在中国可用的第三方联络中心解决方案（如阿里云呼叫中心、腾讯云联络中心等），结合AWS服务构建调查系统
   - 复杂度：高
   - 适用场景：需要完整联络中心功能的企业
   - 注意事项：需要处理跨平台集成、数据同步、合规性等问题

2. **自建简化版调查系统**
   - 实施方式：使用Amazon Lex（语音识别）+ AWS Lambda + Amazon DynamoDB + Amazon SNS/SES构建独立的调查系统
   - 复杂度：中
   - 适用场景：仅需要调查功能，不需要完整联络中心平台
   - 局限性：
     - 缺少Contact Flow的可视化流程编排
     - 缺少任务管理和分配功能
     - 需要自行实现呼叫/消息触发机制
     - 无法与联络中心座席工作台集成

3. **使用AWS全球区域部署**
   - 实施方式：在AWS全球区域（如新加坡ap-southeast-1）部署Amazon Connect解决方案
   - 复杂度：低（技术实施）/ 高（合规和网络）
   - 适用场景：跨国企业，可以接受数据存储在境外
   - 注意事项：
     - 需要评估数据合规性要求（个人信息保护法等）
     - 网络延迟可能影响用户体验
     - 可能需要ICP备案和跨境数据传输审批

### 风险提示

- **服务不可用风险**：Amazon Connect在可预见的未来可能仍不会在中国区域推出，不建议等待该服务上线
- **合规风险**：如果选择在全球区域部署，需要严格评估中国的数据保护法律法规要求
- **架构复杂度**：任何替代方案都会显著增加系统复杂度和维护成本
- **功能缺失**：替代方案很难完全复刻Amazon Connect的全渠道联络中心能力

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/amazon-connect-contact-surveys
- **兼容性**: 不兼容AWS中国区域
- **修改建议**: 由于核心服务不可用，无法通过修改代码实现兼容性
