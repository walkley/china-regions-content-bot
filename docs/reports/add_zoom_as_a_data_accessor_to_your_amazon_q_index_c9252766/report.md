---
title: 将Zoom添加为Amazon Q索引的数据访问器
publish_date: 2025-04-17
original_url: https://aws.amazon.com/blogs/machine-learning/add-zoom-as-a-data-accessor-to-your-amazon-q-index/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: LOW
available_services: 1
unavailable_services: 1
---

# 将Zoom添加为Amazon Q索引的数据访问器

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/add-zoom-as-a-data-accessor-to-your-amazon-q-index/) | 验证日期: 2025-11-25

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

核心服务Amazon Q Business在AWS中国区域不可用，整个解决方案无法实施。

## 服务分析

### 可用服务 (1个)

- AWS IAM Identity Center

### 不可用服务 (1个)

- **Amazon Q Business** - 核心服务

### 评估说明

本博客介绍的解决方案完全依赖于Amazon Q Business服务，该服务是整个架构的核心组件。方案的主要功能包括：

1. **核心依赖**：Amazon Q Business是整个解决方案的基础，用于创建企业知识索引
2. **数据访问器功能**：通过Amazon Q Business的数据访问器特性，允许Zoom AI Companion访问企业索引数据
3. **SearchRelevantContent API**：该API是Amazon Q Business的核心接口，用于实时检索相关内容

由于Amazon Q Business在中国区域完全不可用，且该服务是方案的唯一核心服务，因此：
- 无法创建Amazon Q Business应用程序
- 无法配置数据访问器
- 无法使用SearchRelevantContent API
- 整个Zoom与Amazon Q的集成方案无法实现

虽然AWS IAM Identity Center在中国区域可用，但它仅作为身份认证的辅助服务，无法独立支撑该解决方案。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Q Business在AWS中国区域不可用，无法进行实际部署验证。该服务是整个解决方案的基础，缺失后方案无法实施。

## 实施建议

### 推荐方案

不建议在AWS中国区域实施此解决方案。Amazon Q Business是该方案的核心且唯一的主要服务，其不可用性导致整个集成方案无法实现。

### 替代方案

目前在AWS中国区域没有直接的替代方案可以实现相同的功能。如果企业需要类似的企业知识检索和AI助手集成能力，可以考虑以下替代思路：

1. **自建企业搜索方案**
   - 实施方式：使用Amazon OpenSearch Service + 自定义向量嵌入 + Lambda函数构建企业知识检索系统
   - 复杂度：高
   - 适用场景：有较强技术团队，愿意投入开发资源构建定制化解决方案
   - 局限性：需要自行实现文档连接器、ACL控制、身份传播等功能，开发工作量大

2. **使用全球区域服务**
   - 实施方式：在AWS全球区域（如us-east-1）部署Amazon Q Business，通过网络连接访问
   - 复杂度：中
   - 适用场景：数据合规允许跨境传输，且网络延迟可接受
   - 局限性：需要考虑数据主权、网络延迟、跨境数据传输合规性等问题

### 风险提示

- **服务不可用风险**：Amazon Q Business在中国区域无上线计划公告，短期内无法使用
- **数据合规风险**：如选择使用全球区域服务，需评估企业数据跨境传输的合规性要求
- **成本风险**：自建替代方案需要投入大量开发和维护成本
- **功能差距风险**：任何替代方案都难以完全复制Amazon Q Business的托管能力和与Zoom的原生集成

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/sample-amazon-q-business-isv-workshop
- **兼容性**: 不可在中国区使用
- **修改建议**: 由于核心服务不可用，无法通过修改代码实现兼容
