---
title: AWS CloudFormation堆栈重构功能介绍
publish_date: 2025-02-06
original_url: https://aws.amazon.com/blogs/devops/introducing-aws-cloudformation-stack-refactoring/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 4
unavailable_services: 0
---

# AWS CloudFormation堆栈重构功能介绍

[📖 查看原始博客](https://aws.amazon.com/blogs/devops/introducing-aws-cloudformation-stack-refactoring/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

所有涉及的AWS服务（CloudFormation、Lambda、SNS、IAM）在中国区域均完全可用，Stack Refactoring功能已在cn-northwest-1区域成功验证。

## 服务分析

### 可用服务 (4个)

- AWS CloudFormation
- AWS Lambda
- Amazon SNS
- AWS IAM

### 不可用服务 (0个)

无

### 评估说明

本文介绍的CloudFormation Stack Refactoring是一项新功能，允许在不中断资源的情况下重组CloudFormation堆栈。经过实际验证：

1. 所有核心服务在中国区域完全可用
2. Stack Refactoring功能（create-stack-refactor、describe-stack-refactor、execute-stack-refactor等新API）在cn-northwest-1区域正常工作
3. 资源在堆栈间的移动操作成功执行，保持了资源的物理ID和状态

## 验证结果

### 验证类型

✅ 教程步骤验证

### 执行状态

**状态**: ✅ 成功

### 关键发现

1. **ARN分区适配**
   - 原始模板中使用了 `arn:aws:logs:*:*:*`，在中国区域需要修改为 `arn:aws-cn:logs:*:*:*`
   - 这是中国区域的标准适配要求，不影响功能实现

2. **Stack Refactoring功能完全可用**
   - 成功创建了stack refactor任务（create-stack-refactor）
   - 系统自动检测并识别了需要移动的资源（4个资源：Lambda函数、IAM角色、SNS订阅、Lambda权限）
   - 成功执行了堆栈重构，资源从MySns堆栈移动到新创建的MyLambdaSubscription堆栈
   - 资源的物理ID保持不变，实现了无中断迁移

3. **API参数格式**
   - 中国区域的CloudFormation API对file://协议支持有限制
   - 需要使用JSON格式直接传递模板内容，而不是文件路径
   - 这是实施时需要注意的技术细节

4. **导出/导入功能正常**
   - CloudFormation的Export/Import功能在堆栈间共享资源引用正常工作
   - 重构后的堆栈通过!ImportValue成功引用了SNS Topic ARN

## 实施建议

### 推荐方案

可直接按照原文实施，但需要注意以下配置差异：

- **ARN分区**：所有ARN中的 `arn:aws:` 需要改为 `arn:aws-cn:`
- **API调用方式**：使用AWS CLI时，建议通过JSON格式传递完整参数，而不是使用file://协议
- **区域代码**：确保所有配置中使用正确的中国区域代码（如cn-northwest-1、cn-north-1）

### 替代方案

无需替代方案，功能完全可用。

### 风险提示

- **新功能稳定性**：Stack Refactoring是CloudFormation的新功能（2025年2月发布），建议在生产环境使用前在测试环境充分验证
- **资源依赖关系**：重构前需要仔细分析资源间的依赖关系，确保移动后的堆栈结构合理
- **回滚限制**：Stack Refactoring执行后无法直接回滚，建议在执行前使用describe-stack-refactor和list-stack-refactor-actions仔细检查计划的操作
- **权限要求**：执行Stack Refactoring需要对涉及的所有堆栈和资源有完整的CloudFormation权限

### 配套资源

- **GitHub仓库**: 无（文章提供的是内联示例代码）
- **兼容性**: 示例代码在中国区域完全可用
- **修改建议**: 仅需将IAM策略中的ARN分区从aws改为aws-cn
