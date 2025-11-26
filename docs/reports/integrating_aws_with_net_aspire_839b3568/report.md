---
title: 将AWS与.NET Aspire集成
publish_date: 2025-02-11
original_url: https://aws.amazon.com/blogs/developer/integrating-aws-with-net-aspire/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 6
unavailable_services: 0
---

# 将AWS与.NET Aspire集成

[📖 查看原始博客](https://aws.amazon.com/blogs/developer/integrating-aws-with-net-aspire/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文介绍的.NET Aspire AWS集成方案完全兼容AWS中国区域。所有涉及的AWS服务（CloudFormation、DynamoDB、SNS、SQS、Lambda、CDK）均在中国区域可用，且经过实际部署验证，CloudFormation模板可以成功在cn-northwest-1区域创建和管理资源。

## 服务分析

### 可用服务 (6个)

- AWS CloudFormation
- Amazon DynamoDB
- Amazon SNS (Simple Notification Service)
- Amazon SQS (Simple Queue Service)
- AWS Lambda
- AWS CDK (Cloud Development Kit)

### 不可用服务 (0个)

无

### 评估说明

所有核心服务在AWS中国区域完全可用：

1. **AWS CloudFormation** - 中国区域完全支持，可用于自动化资源配置
2. **Amazon DynamoDB** - 包括DynamoDB服务和DynamoDB Local容器，完全兼容
3. **Amazon SNS/SQS** - 消息服务在中国区域正常工作，ARN格式使用`arn:aws-cn`前缀
4. **AWS Lambda** - 支持本地开发和调试集成
5. **AWS CDK** - 可用于定义基础设施即代码

AWS SDK for .NET使用标准的RegionEndpoint配置，自动适配中国区域的endpoint（amazonaws.com.cn），无需额外修改。

## 验证结果

### 验证类型

✅ GitHub项目部署验证

### 执行状态

**状态**: ✅ 成功

**验证详情**:
- GitHub仓库: https://github.com/aws/integrations-on-dotnet-aspire-for-aws
- 验证区域: cn-northwest-1
- 验证时间: 2025-11-25T17:02-17:06 UTC

### 关键发现

1. **CloudFormation模板完全兼容**
   - 成功在cn-northwest-1区域创建CloudFormation栈
   - 栈名称: aspire-china-validation-test
   - 创建的资源包括SNS主题、SQS队列及相关策略
   - 所有输出参数正确返回，URL使用中国区域endpoint（amazonaws.com.cn）

2. **区域自动适配**
   - AWS SDK自动识别中国区域并使用正确的endpoint
   - SNS主题ARN格式: `arn:aws-cn:sns:cn-northwest-1:账号:主题名`
   - SQS队列URL格式: `https://sqs.cn-northwest-1.amazonaws.com.cn/账号/队列名`
   - 无需修改代码或配置即可在中国区域运行

3. **参数传递正常**
   - CloudFormation参数（DefaultVisibilityTimeout=30）正确应用
   - 标签系统正常工作，支持资源标记和跟踪
   - 输出参数可通过IConfiguration接口访问

4. **资源清理完整**
   - CloudFormation栈删除成功
   - 所有相关资源（SNS主题、SQS队列、策略）自动清理
   - 无资源残留

## 实施建议

### 推荐方案

**可直接按照原文实施**，.NET Aspire AWS集成在中国区域开箱即用。

**实施步骤**:

1. **安装.NET Aspire工作负载**
   ```bash
   dotnet workload install aspire
   ```

2. **添加NuGet包到AppHost项目**
   ```bash
   dotnet add package Aspire.Hosting.AWS
   ```

3. **配置AWS SDK使用中国区域**
   ```csharp
   var awsConfig = builder.AddAWSSDKConfig()
                          .WithProfile("your-profile")
                          .WithRegion(RegionEndpoint.CNNorthWest1);  // 或 CNNorth1
   ```

4. **定义CloudFormation资源**
   ```csharp
   var awsResources = builder.AddAWSCloudFormationTemplate("ResourceName", "template.json")
                             .WithReference(awsConfig);
   ```

5. **在项目中引用AWS资源**
   ```csharp
   builder.AddProject<Projects.YourProject>("ProjectName")
          .WithReference(awsResources);
   ```

**注意事项**:

- 确保AWS凭证配置文件包含中国区域的访问密钥
- 使用`RegionEndpoint.CNNorthWest1`（宁夏）或`RegionEndpoint.CNNorth1`（北京）
- DynamoDB Local容器在中国区域网络环境下可能需要配置镜像加速
- CloudFormation模板中的资源类型需确保在中国区域可用

### 替代方案

无需替代方案，原方案完全适用。

### 风险提示

- **网络连接**: 确保开发环境可以访问AWS中国区域的API endpoint（*.amazonaws.com.cn）
- **容器镜像**: DynamoDB Local容器镜像可能需要从国内镜像源拉取以提高速度
- **服务配额**: 首次使用某些服务时，注意检查账户的服务配额限制
- **IAM权限**: 确保使用的IAM用户或角色具有CloudFormation、SNS、SQS等服务的必要权限

### 配套资源

- **GitHub仓库**: https://github.com/aws/integrations-on-dotnet-aspire-for-aws
- **兼容性**: 完全兼容中国区域，无需修改
- **修改建议**: 
  - 将示例代码中的`RegionEndpoint.USWest2`改为`RegionEndpoint.CNNorthWest1`或`RegionEndpoint.CNNorth1`
  - 其他代码无需修改
- **NuGet包**: [Aspire.Hosting.AWS](https://www.nuget.org/packages/Aspire.Hosting.AWS/)
- **文档**: [.NET Aspire官方文档](https://learn.microsoft.com/en-us/dotnet/aspire/get-started/aspire-overview)
- **视频教程**: [Building .NET Applications Across Clouds with .NET Aspire](https://www.youtube.com/watch?v=yVgr6cRYOPk)
