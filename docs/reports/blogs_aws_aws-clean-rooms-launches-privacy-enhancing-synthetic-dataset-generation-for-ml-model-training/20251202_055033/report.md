---
title: AWS Clean Rooms推出用于机器学习模型训练的隐私增强合成数据集生成功能
publish_date: 2025-11-30
original_url: https://aws.amazon.com/blogs/aws/aws-clean-rooms-launches-privacy-enhancing-synthetic-dataset-generation-for-ml-model-training/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: NOT_APPLICABLE
available_services: 0
unavailable_services: 0
---

# AWS Clean Rooms推出用于机器学习模型训练的隐私增强合成数据集生成功能

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/aws-clean-rooms-launches-privacy-enhancing-synthetic-dataset-generation-for-ml-model-training/) | 验证日期: 2025-12-02

## 可行性评估

!!! info "NOT_APPLICABLE - 不适用"
    文章不包含技术实现内容，无需进行兼容性验证

这是一篇产品功能发布公告，主要介绍AWS Clean Rooms在2025年11月30日推出的新功能"隐私增强合成数据集生成"。文章内容以功能介绍和概念说明为主，包含少量控制台操作截图，但不包含具体的技术实现步骤、代码示例或配套的GitHub项目，因此不适用于技术兼容性验证。

## 内容概述

### 文章类型
产品功能发布公告 / 新闻通知

### 主要内容

**功能介绍**：
- AWS Clean Rooms推出隐私增强合成数据集生成功能
- 允许组织和合作伙伴从集体数据生成合成数据集用于训练回归和分类机器学习模型
- 合成数据保留原始数据的统计模式，但不包含原始记录，解决隐私保护问题

**核心技术特点**：
- 使用高级机器学习技术生成保持统计特性的合成数据
- 通过模型容量降低技术降低个人信息记忆风险
- 提供隐私参数控制，包括噪声水平和成员推理攻击防护
- 提供保真度评分（KL散度）和隐私评分指标

**工作流程**：
1. 创建配置表和分析规则
2. 加入或创建协作并关联表
3. 在分析模板中指定生成合成数据
4. 定义列分类和隐私阈值
5. 生成合成数据集并查看质量指标
6. 使用合成数据训练ML模型

**可用性**：
- 在所有支持AWS Clean Rooms的商业AWS区域可用
- 按使用量计费（合成数据生成单元SDGU）
- 初始版本支持表格数据的分类和回归模型训练

### 涉及的AWS服务

文章提到的服务：
- **AWS Clean Rooms** - 安全数据协作服务
- **AWS Clean Rooms ML** - 机器学习功能扩展

**中国区域可用性说明**：
- AWS Clean Rooms和AWS Clean Rooms ML的基础服务在中国区域（cn-northwest-1和cn-north-1）可用
- 但文章介绍的"隐私增强合成数据集生成"是2025年11月30日刚发布的新功能，该特定功能在中国区域的上线时间可能有所延迟
- 建议在实际使用前通过AWS中国官方渠道确认此新功能的可用性

## 实施建议

### 文章价值

**适用场景**：
- 了解AWS Clean Rooms的最新功能发展
- 评估隐私保护机器学习解决方案
- 规划数据协作和模型训练策略

**建议**：
- 此类功能发布公告主要用于了解AWS服务的最新能力
- 如需在中国区域实施，建议：
  1. 联系AWS中国团队确认新功能的上线时间表
  2. 查阅AWS中国官方文档获取最新的功能支持信息
  3. 在功能正式上线后，参考AWS Clean Rooms用户指南进行实际操作

### 相关资源

- [AWS Clean Rooms 文档](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html)
- [AWS Clean Rooms 定价页面](https://aws.amazon.com/clean-rooms/pricing/)
- AWS中国区域服务可用性需通过官方渠道确认

### 注意事项

- 新功能在全球区域和中国区域的上线时间可能存在差异
- 建议在规划使用前确认功能在目标区域的可用性
- 隐私和合规要求需要与法律和合规团队协商确定
