---
title: Amazon Elastic Kubernetes Service 零操作员访问设计获得独立验证
publish_date: 2025-11-12
original_url: https://aws.amazon.com/blogs/security/amazon-elastic-kubernetes-service-gets-independent-affirmation-of-its-zero-operator-access-design/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 7
unavailable_services: 0
---

# Amazon Elastic Kubernetes Service 零操作员访问设计获得独立验证

[📖 查看原始博客](https://aws.amazon.com/blogs/security/amazon-elastic-kubernetes-service-gets-independent-affirmation-of-its-zero-operator-access-design/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文介绍了Amazon EKS零操作员访问架构设计及其独立安全验证，所有涉及的AWS服务在中国区域均可用，内容完全适用于中国区域的Amazon EKS用户。

## 服务分析

### 可用服务 (7个)

- Amazon Elastic Kubernetes Service (Amazon EKS)
- AWS Key Management Service (AWS KMS)
- Amazon Elastic Compute Cloud (Amazon EC2)
- AWS Nitro System
- AWS Lambda
- AWS Fargate
- AWS Wickr

### 不可用服务 (0个)

无

### 评估说明

本文是一篇关于Amazon EKS安全架构设计的公告性文章，重点介绍了：

1. **核心服务完全可用**：文章提到的所有AWS服务（Amazon EKS、AWS KMS、Amazon EC2、AWS Nitro System、AWS Lambda、AWS Fargate、AWS Wickr）在AWS中国区域均可用。

2. **架构设计理念通用**：文章阐述的零操作员访问（Zero Operator Access）设计理念、AWS Nitro System的安全基线、多方审批流程、加密机制等安全架构设计，在全球区域和中国区域的Amazon EKS中均采用相同的实现方式。

3. **无区域特定限制**：文章内容为安全架构和设计理念的介绍，不涉及区域特定的配置或限制，完全适用于中国区域。

## 验证结果

### 验证类型

⏭️ 无需验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 本文为纯理论性、公告性内容，介绍Amazon EKS的零操作员访问安全架构设计理念和NCC Group的独立验证报告。文章不包含配套的GitHub项目或具体的操作步骤，无需进行实际部署或步骤验证。

### 关键发现

本文重点介绍的Amazon EKS安全特性在中国区域同样适用：

1. **零操作员访问架构**
   - AWS人员无技术手段访问Kubernetes控制平面实例
   - AWS人员无法读取、复制、提取、修改或访问客户内容
   - 该架构设计在全球区域和中国区域保持一致

2. **AWS Nitro System安全基线**
   - Amazon EKS在中国区域同样使用基于AWS Nitro System的实例
   - 提供机密计算基线保护

3. **加密和密钥管理**
   - etcd数据库的信封加密机制在中国区域可用
   - AWS KMS在中国区域完全支持

4. **审计和日志**
   - 客户可在中国区域启用Amazon EKS集群审计日志
   - 所有AWS人员对集群API端点的操作对客户可见

## 实施建议

### 推荐方案

可直接按照原文理解和应用Amazon EKS的安全架构设计理念。

**适用场景**：
- 需要了解Amazon EKS安全架构设计的客户
- 有严格数据隐私和合规要求的客户
- 希望在中国区域运行关键和数据敏感工作负载的客户

**注意事项**：
- NCC Group报告链接指向国际网站，在中国访问可能需要特殊网络环境
- 文章中引用的AWS白皮书和文档链接为国际站点，建议访问AWS中国官网获取对应的中文文档

### 替代方案

无需替代方案，所有内容直接适用。

### 风险提示

- **文档访问**: 文章中引用的外部链接（NCC Group报告、AWS白皮书等）可能需要特殊网络环境才能访问
- **合规咨询**: 如有具体的合规和数据主权要求，建议联系AWS中国团队获取针对性的咨询和支持

### 配套资源

本文为理论性内容，无配套GitHub项目或代码示例。

**相关资源**：
- Amazon EKS中国区域文档
- AWS中国区域合规和安全资源
- AWS Nitro System技术文档
