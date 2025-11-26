---
title: 为AWS WAF和AWS Shield Advanced客户推出新的应用层（L7）DDoS防护
publish_date: 2025-06-12
original_url: https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-the-aws-waf-application-layer-ddos-protection/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 4
unavailable_services: 2
---

# 为AWS WAF和AWS Shield Advanced客户推出新的应用层（L7）DDoS防护

[📖 查看原始博客](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-the-aws-waf-application-layer-ddos-protection/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，无法实施

博客介绍的核心功能AntiDDoS AMR托管规则组和AWS Shield Advanced服务在AWS中国区域均不可用，导致文章的主要内容无法在中国区域实施。

## 服务分析

### 可用服务 (4个)

- AWS WAF (Web Application Firewall)
- Amazon CloudFront
- Application Load Balancer (ALB)
- Amazon CloudWatch

### 不可用服务 (2个)

- **AWS Shield Advanced** - 核心服务
- **AntiDDoS AMR (AWSManagedRulesAntiDDoSRuleSet)** - 核心服务

### 评估说明

本文的核心主题是介绍AWS WAF的新功能AntiDDoS AMR托管规则组，用于自动检测和缓解应用层DDoS攻击。经过验证：

1. **核心功能不可用**：通过API验证，cn-northwest-1区域的AWS WAF托管规则组列表中不包含`AWSManagedRulesAntiDDoSRuleSet`，这是博客介绍的核心新功能。

2. **Shield Advanced不可用**：AWS Shield Advanced在中国区域不可用服务列表中，而博客中大量内容涉及Shield Advanced客户的特殊定价和功能。

3. **基础WAF可用**：虽然AWS WAF服务本身在中国区域可用，但缺少本文介绍的核心AntiDDoS AMR功能，使得文章的主要价值无法体现。

4. **无替代方案**：AntiDDoS AMR是AWS专门开发的托管规则组，具有自动流量基线学习、秒级检测和缓解等特性，无法通过其他现有服务完全替代。

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 基础验证阶段发现核心服务（AntiDDoS AMR和AWS Shield Advanced）在中国区域不可用，可行性评估为LOW，根据验证流程跳过深入验证阶段。

### 关键发现

通过AWS CLI验证发现：

1. **AntiDDoS AMR不可用**：执行`list-available-managed-rule-groups`命令，返回的托管规则组列表中不包含`AWSManagedRulesAntiDDoSRuleSet`。

2. **Shield Advanced在不可用列表**：AWS Shield（包括Shield Advanced）明确列在中国区域不可用服务列表中。

3. **CloudFront WAF限制**：尝试查询CloudFront scope的WAF规则时返回错误，表明中国区域CloudFront的WAF集成存在限制。

## 实施建议

### 推荐方案

**不建议直接实施**

本文介绍的AntiDDoS AMR功能是AWS在2025年6月推出的新功能，专门用于应对不断演变的应用层DDoS攻击。由于该功能在中国区域不可用，文章内容无法在中国区域实施。

### 替代方案

虽然无法使用AntiDDoS AMR，但可以考虑以下替代方案来应对应用层DDoS攻击：

1. **使用现有AWS WAF托管规则组**
   - 实施方式：组合使用`AWSManagedRulesBotControlRuleSet`和`AWSManagedRulesAmazonIpReputationList`等现有规则组
   - 复杂度：中
   - 适用场景：需要基础的DDoS防护，但缺少AntiDDoS AMR的自动学习和秒级响应能力
   - 局限性：需要手动配置和调整规则，无法实现自动流量基线学习

2. **自定义WAF规则配合Rate Limiting**
   - 实施方式：创建自定义WAF规则，使用速率限制功能限制来自单一IP或特定URI的请求频率
   - 复杂度：中到高
   - 适用场景：了解应用流量模式，能够设定合理的速率阈值
   - 局限性：需要持续监控和调整，无法自动适应流量变化，可能产生误报

3. **结合CloudWatch告警和自动化响应**
   - 实施方式：设置CloudWatch指标监控异常流量，通过Lambda函数自动更新WAF规则
   - 复杂度：高
   - 适用场景：有开发资源，需要自动化响应机制
   - 局限性：响应时间较慢，需要自行开发和维护自动化逻辑

### 风险提示

- **功能差距**：替代方案无法提供AntiDDoS AMR的核心能力，包括自动流量基线学习、秒级检测和缓解、智能suspicion scoring等
- **运维成本**：替代方案需要更多的手动配置、监控和调整工作
- **检测延迟**：自定义方案的检测和响应时间远慢于AntiDDoS AMR的秒级响应
- **误报风险**：缺少智能流量分析，可能将合法的流量突增（flash crowd）误判为DDoS攻击
- **定价差异**：无法享受AntiDDoS AMR的"DDoS流量不计费"特性，所有流量都会按标准WAF定价计费

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 不适用
