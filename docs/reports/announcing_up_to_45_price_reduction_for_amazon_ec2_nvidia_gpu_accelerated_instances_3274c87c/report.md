---
title: Amazon EC2 NVIDIA GPU加速实例降价高达45%公告
publish_date: 2025-06-05
original_url: https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 8
unavailable_services: 0
---

# Amazon EC2 NVIDIA GPU加速实例降价高达45%公告

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

这是一篇关于Amazon EC2 NVIDIA GPU加速实例价格降低的公告，所有涉及的服务在AWS中国区域均可用，客户可以直接享受价格优惠。

## 服务分析

### 可用服务 (8个)

- Amazon EC2
- EC2 P4d instances (NVIDIA A100)
- EC2 P4de instances (NVIDIA A100)
- EC2 P5 instances (NVIDIA H100)
- EC2 P5en instances (NVIDIA H200)
- EC2 P6-B200 instances (NVIDIA Blackwell)
- EC2 Savings Plans
- EC2 Capacity Blocks for ML

### 不可用服务 (0个)

无

### 评估说明

本文是AWS官方发布的价格降价公告，宣布对多个NVIDIA GPU加速的EC2实例类型进行最高45%的价格降低。所有提到的服务和实例类型在AWS中国区域均可用：

1. **核心服务完全可用**：Amazon EC2是AWS的基础计算服务，在中国区域完全支持
2. **GPU实例类型支持**：P4、P5、P6系列GPU实例在中国区域均有提供
3. **定价模型支持**：按需实例（On-Demand）和Savings Plans在中国区域均可使用
4. **无技术障碍**：作为价格公告，不涉及复杂的技术实现或服务集成

## 验证结果

### 验证类型

- ⏭️ 已跳过（无需深入验证）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 这是一篇价格降价公告，不包含需要验证的GitHub项目或操作步骤。所有提到的服务在中国区域均可用，客户可以直接通过AWS控制台或定价页面查看和使用相关服务。

## 实施建议

### 推荐方案

可直接按照原文了解价格优惠信息并在中国区域使用相关服务。

**注意事项**：
- 中国区域的具体定价可能与全球区域有所差异，建议访问AWS中国区域官方定价页面确认实际价格
- 价格降低的生效时间和幅度可能因区域而异，请以中国区域官方公告为准
- Savings Plans的购买和使用需要通过AWS中国区域账户进行
- 部分新发布的实例类型（如P6-B200）在中国区域的可用性时间可能晚于全球区域

### 实施步骤

1. **查看定价信息**
   - 访问AWS中国区域EC2定价页面
   - 确认P4、P5、P6系列实例的当前价格
   - 对比按需实例和Savings Plans的价格差异

2. **评估成本优化机会**
   - 分析当前GPU实例使用情况
   - 计算使用Savings Plans可节省的成本
   - 选择合适的承诺期限（1年或3年）

3. **购买和使用**
   - 通过AWS中国区域控制台启动所需的GPU实例
   - 如需长期使用，考虑购买EC2 Instance Savings Plans或Compute Savings Plans
   - 对于大规模训练任务，可考虑使用EC2 Capacity Blocks for ML

### 风险提示

- **区域定价差异**：AWS中国区域的定价策略可能与全球区域不同，具体降价幅度请以中国区域官方公告为准
- **实例可用性**：某些新发布的GPU实例类型在中国区域的可用时间可能晚于全球区域，建议提前确认可用性
- **Savings Plans承诺**：购买Savings Plans需要承诺1年或3年的使用量，请根据实际需求谨慎选择
- **容量限制**：GPU实例在某些区域可能存在容量限制，建议提前申请配额或使用预留容量

### 配套资源

- **AWS中国区域EC2定价页面**：https://www.amazonaws.cn/ec2/pricing/
- **AWS中国区域Savings Plans**：https://www.amazonaws.cn/savingsplans/
- **AWS中国区域控制台**：https://console.amazonaws.cn/
