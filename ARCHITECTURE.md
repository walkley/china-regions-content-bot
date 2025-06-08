# AWS China Region Content Bot - 架构设计文档

## 项目概述

AWS中国区域内容适配性验证工具，采用分层验证策略，为客户提供务实的AWS SA级别的验证服务。

## 核心设计理念

- **务实导向**：像真正的AWS SA一样工作，提供hands-on验证和可执行方案
- **分层验证**：Basic快速筛选 + Deep深度验证，平衡效率和准确性
- **智能决策**：基于LLM推理进行验证策略选择
- **资源高效**：避免无意义的深度验证，节省时间和成本

## 整体架构流程

```
Blog URL → Content Converter → Basic Validator → Deep Validator
         (Clean Markdown)   (HIGH/MODERATE/LOW)  (Project/Tutorial)
```

## 模块化设计

项目采用模块化设计，每个主要功能都封装在独立的脚本中：

1. **aws-cn-tool.sh** - 主脚本
   - 处理命令行参数
   - 协调各模块工作
   - 管理整体验证流程

2. **content-converter.sh** - 内容转换模块
   - 将网页内容转换为Markdown格式
   - 清理非核心内容（导航栏、页脚等）

3. **basic-validator.sh** - 基本验证模块
   - 分析内容中涉及的AWS服务
   - 验证服务在中国区的可用性
   - 生成基本验证报告

4. **deep-validator.sh** - 深度验证协调模块
   - 确定内容类型（项目或教程）
   - 检查可行性级别
   - 调用相应的验证器

5. **project-validator.sh** - 项目验证模块
   - 分析GitHub项目
   - 验证项目在中国区的可部署性
   - 生成项目验证报告

6. **tutorial-validator.sh** - 教程验证模块
   - 分析教程步骤
   - 验证步骤在中国区的可执行性
   - 生成教程验证报告

7. **common-utils.sh** - 通用工具函数
   - 日志记录
   - 依赖检查
   - 资源清理

## 验证模式定义

### 1. Basic验证
- **适用范围**：所有内容通用
- **验证内容**：
  - AWS服务清单提取
  - 实际API调用验证服务可用性
  - 整体可行性级别评估
- **输出级别**：
  - **HIGH**：核心服务全部可用，强烈推荐Deep验证
  - **MODERATE**：部分核心服务可用，可以进行Deep验证
  - **LOW**：核心服务大量缺失，不建议Deep验证

### 2. Deep验证
- **触发条件**：Basic验证结果为HIGH或MODERATE
- **阻止条件**：Basic验证结果为LOW时强制停止
- **验证类型**：
  - **Project类型**：GitHub项目实际部署验证
  - **Tutorial类型**：操作步骤实际执行验证

## 决策逻辑

### Basic验证级别判断
- **HIGH**：核心服务全部可用，或有成熟可靠的替代方案
- **MODERATE**：部分核心服务可用，需要一些适配工作但可行
- **LOW**：核心服务大量缺失，基本不可行或需要重大架构调整

### Deep验证触发规则
- **允许执行**：Basic验证结果为HIGH或MODERATE
- **强制阻止**：Basic验证结果为LOW，即使用户选择deep模式也要停止

### 内容类型识别
- **Project类型**：检测到GitHub项目链接或代码仓库
- **Tutorial类型**：检测到操作步骤但无GitHub项目

## 用户交互流程

### 场景1：HIGH级别 + Project类型
```
🔄 转换Blog URL为Markdown...
🔍 执行Basic验证...
📈 可行性级别: HIGH
💭 评估理由: 核心服务Lambda、DynamoDB、S3全部在中国区可用
✅ 开始Deep验证...
🚀 检测到GitHub项目，执行项目部署验证...
```

### 场景2：MODERATE级别 + Tutorial类型
```
🔄 转换Blog URL为Markdown...
🔍 执行Basic验证...
📈 可行性级别: MODERATE
💭 评估理由: 主要服务可用，但需要替代方案
✅ 开始Deep验证...
🚀 检测到操作步骤，执行教程验证...
```

### 场景3：LOW级别（强制阻止）
```
🔄 转换Blog URL为Markdown...
🔍 执行Basic验证...
📈 可行性级别: LOW
💭 评估理由: 核心服务大量缺失，且缺乏有效替代方案
❌ 可行性级别过低，停止Deep验证
💡 建议: 先解决Basic验证中发现的核心问题
```

## 技术实现要点
- 实际部署验证在隔离环境中进行
- 自动清理测试资源
- 成本控制和安全保障

## 预期输出

### Basic验证输出
```json
{
  "content_analysis": {
    "identified_services": [...],
    "dependencies": [...],
    "github_project": "...",
    "procedures": [...]
  },
  "service_validation_results": {
    "available_services": [...],
    "unavailable_services": [...],
    "api_test_results": {...}
  },
  "feasibility_assessment": {
    "level": "high|moderate|low",
    "reasoning": "详细判断理由",
    "confidence": 0.0-1.0
  }
}
```

### Deep验证输出
```json
{
  "validation_type": "project_deployment|tutorial_execution",
  "agent_used": "project_deployment_agent|tutorial_execution_agent",
  "validation_results": {
    // Project类型输出
    "project_analysis": {...},
    "china_compatibility": {...},
    "deployment_solution": {...},
    
    // 或Tutorial类型输出  
    "steps_analysis": {...},
    "china_compatibility": {...},
    "executable_guide": {...}
  },
  "confidence": 0.0-1.0,
  "execution_time": "...",
  "recommendations": [...]
}
```

## 成功指标

- **准确性**：Basic验证的可行性判断准确率 > 90%
- **效率**：Basic验证时间 < 5分钟，Deep验证时间 < 30分钟
- **实用性**：Deep验证输出的方案客户可直接使用
- **成本控制**：Deep验证的AWS资源成本 < $10/次
