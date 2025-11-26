---
title: AWS API模型和公开可用的AWS API定义资源介绍
publish_date: 2025-06-05
original_url: https://aws.amazon.com/blogs/aws/introducing-aws-api-models-and-publicly-available-resources-for-aws-api-definitions/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 2
unavailable_services: 0
---

# AWS API模型和公开可用的AWS API定义资源介绍

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/introducing-aws-api-models-and-publicly-available-resources-for-aws-api-definitions/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

博客介绍的AWS API模型（Smithy格式）是开源资源，通过GitHub和Maven Central全球发布，不依赖特定AWS区域。示例中使用的AWS服务（EC2、DynamoDB）在中国区完全可用，且已通过实际部署验证。

## 服务分析

### 可用服务 (2个)

- Amazon EC2
- Amazon DynamoDB

### 不可用服务 (0个)

无

### 评估说明

本博客的核心内容是宣布AWS公开发布Smithy格式的API模型，这些模型可用于：
1. 生成自定义SDK客户端
2. 构建开发者工具（CLI、测试工具等）
3. 理解AWS API行为

关键资源均为全球可访问：
- **GitHub仓库**：`aws/api-models-aws` - 包含所有AWS服务的Smithy模型
- **Maven Central**：提供模型包的依赖管理
- **示例项目**：TypeScript和Java示例项目

博客中提到的AWS服务（EC2、DynamoDB）仅作为示例说明，这些服务在中国区域完全可用。核心价值在于开源的API模型和工具链，不受区域限制。

## 验证结果

### 验证类型

✅ GitHub项目部署验证

### 执行状态

**状态**: ✅ 成功

### 关键发现

1. **GitHub资源完全可访问**
   - 成功克隆 `aws/api-models-aws` 仓库
   - 验证了DynamoDB的Smithy模型文件（JSON AST格式）
   - 模型文件结构完整，包含shapes、traits等完整定义

2. **Maven Central可正常访问**
   - 测试访问 `software.amazon.api.models` 命名空间
   - 可正常下载模型包依赖
   - 适合在中国区域使用Maven/Gradle构建工具

3. **DynamoDB在中国区域功能验证**
   - 在cn-northwest-1成功创建DynamoDB表
   - 使用AWS SDK for JavaScript v3成功执行：
     - ListTables操作
     - PutItem操作（写入数据）
     - GetItem操作（读取数据）
   - Endpoint配置：`dynamodb.cn-northwest-1.amazonaws.com.cn`

4. **Endpoint差异需要注意**
   - 中国区域使用 `.amazonaws.com.cn` 后缀
   - 标准区域使用 `.amazonaws.com` 后缀
   - 示例代码需要调整endpoint配置以适配中国区域

## 实施建议

### 推荐方案

可直接按照原文实施，使用AWS API模型构建自定义工具和SDK。

**注意事项**：
1. **Endpoint配置**：在中国区域使用时，需要将endpoint从 `*.amazonaws.com` 修改为 `*.amazonaws.com.cn`
2. **区域代码**：使用中国区域代码（cn-north-1或cn-northwest-1）
3. **网络访问**：GitHub和Maven Central在中国可正常访问，但建议配置镜像以提高下载速度

### 实施步骤

1. **获取API模型**
   ```bash
   # 克隆API模型仓库
   git clone https://github.com/aws/api-models-aws.git
   
   # 或通过Maven添加依赖
   # software.amazon.api.models:dynamodb:(,1.1]
   ```

2. **使用Smithy工具链**
   - 安装Smithy CLI或使用Gradle插件
   - 配置smithy-build.json定义代码生成规则
   - 生成目标语言的SDK客户端

3. **适配中国区域**
   - 修改endpoint配置使用 `.amazonaws.com.cn` 后缀
   - 设置正确的区域代码（cn-north-1或cn-northwest-1）
   - 配置AWS凭证（使用中国区域的Access Key）

### 替代方案

如果不需要自定义SDK，可以直接使用官方AWS SDK：
- AWS SDK for JavaScript v3
- AWS SDK for Java v2
- AWS SDK for Python (Boto3)
- 其他官方SDK

这些SDK已经内置了对中国区域的支持，只需配置正确的region和endpoint即可。

### 风险提示

- **工具链复杂性**：构建自定义SDK需要熟悉Smithy工具链和代码生成流程，有一定学习曲线
- **维护成本**：自定义SDK需要跟随AWS API更新而更新模型和代码
- **服务差异**：部分AWS服务在中国区域不可用，生成SDK前需确认目标服务的可用性
- **Endpoint管理**：需要正确处理中国区域的endpoint差异，避免连接错误

### 配套资源

- **GitHub仓库**: https://github.com/aws/api-models-aws
- **兼容性**: ✅ 完全兼容中国区域
- **修改建议**: 
  - 示例代码中的endpoint需要修改为中国区域格式
  - 区域代码需要使用cn-north-1或cn-northwest-1
  - 其他代码逻辑无需修改

**示例项目**:
- TypeScript最小SDK客户端：https://github.com/smithy-lang/smithy-examples/tree/main/smithy-typescript-examples/minimal-aws-sdk-client
- MCP服务器示例：https://github.com/smithy-lang/smithy-java/tree/main/examples/mcp-server

**学习资源**:
- Smithy官方文档：https://smithy.io/
- 代码生成指南：https://smithy.io/2.0/guides/using-code-generation/
