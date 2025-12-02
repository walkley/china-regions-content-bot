---
title: 介绍AWS基础设施即代码MCP服务器：AI驱动的CDK和CloudFormation辅助工具
publish_date: 2025-11-28
original_url: https://aws.amazon.com/blogs/devops/introducing-the-aws-infrastructure-as-code-mcp-server-ai-powered-cdk-and-cloudformation-assistance/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: HIGH
available_services: 10
unavailable_services: 0
---

# 介绍AWS基础设施即代码MCP服务器：AI驱动的CDK和CloudFormation辅助工具

[📖 查看原始博客](https://aws.amazon.com/blogs/devops/introducing-the-aws-infrastructure-as-code-mcp-server-ai-powered-cdk-and-cloudformation-assistance/) | 验证日期: 2025-12-02

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文介绍的AWS IaC MCP服务器是一个本地运行的工具，通过Model Context Protocol连接AI助手与AWS基础设施开发工作流。所有涉及的AWS服务在中国区域均可用，工具本身在本地执行，无需依赖海外服务。

## 服务分析

### 可用服务 (10个)

- **AWS CloudFormation** - 核心服务，模板验证和部署管理
- **AWS Cloud Development Kit (CDK)** - 核心服务，基础设施即代码开发
- **AWS CloudTrail** - 用于部署故障排查和事件分析
- **AWS IAM** - 权限管理和访问控制
- **Amazon S3** - 示例中的存储服务
- **AWS Lambda** - 示例中的无服务器计算
- **Amazon DynamoDB** - 示例中的NoSQL数据库
- **Amazon API Gateway** - 示例中的API管理服务
- **Amazon EC2** - 示例中的计算服务
- **Amazon EBS** - 示例中的块存储服务

### 不可用服务 (0个)

无

### 评估说明

1. **核心服务完全可用**：CloudFormation和CDK是本文的核心服务，在中国区域完全支持，功能与全球区域一致。

2. **工具本地执行**：AWS IaC MCP服务器使用Python和uv包管理器在本地运行，通过stdio与AI助手通信，不依赖外部网络服务。

3. **文档搜索功能**：虽然工具提供远程文档搜索功能（连接AWS Knowledge MCP后端），但本地验证和故障排查工具完全独立运行，使用本地AWS凭证访问中国区域的CloudFormation和CloudTrail API。

4. **示例服务全部可用**：文中提到的所有示例服务（S3、Lambda、DynamoDB、API Gateway、EC2、EBS）在中国区域均可用。

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 根据验证流程要求，深入验证阶段统一跳过以节约时间。已通过AWS CLI确认CloudFormation服务在cn-northwest-1区域可用。

## 实施建议

### 推荐方案

可直接按照原文实施，具体步骤：

1. **安装前置条件**
   - Python 3.10或更高版本
   - uv包管理器
   - 配置AWS中国区域凭证（~/.aws/credentials）
   - 安装MCP兼容的AI客户端（如Kiro CLI）

2. **配置MCP服务器**
   
   编辑 `.kiro/settings/mcp.json`：
   ```json
   {
     "mcpServers": {
       "awslabs.aws-iac-mcp-server": {
         "command": "uvx",
         "args": ["awslabs.aws-iac-mcp-server@latest"],
         "env": {
           "AWS_PROFILE": "your-china-profile",
           "AWS_REGION": "cn-northwest-1",
           "FASTMCP_LOG_LEVEL": "ERROR"
         },
         "disabled": false,
         "autoApprove": []
       }
     }
   }
   ```

3. **配置IAM权限**
   
   为中国区域账户创建IAM策略（注意ARN格式使用 `aws-cn`）：
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "cloudformation:DescribeStacks",
           "cloudformation:DescribeStackEvents",
           "cloudformation:DescribeStackResources",
           "cloudtrail:LookupEvents"
         ],
         "Resource": "*"
       }
     ]
   }
   ```

4. **使用场景适配**
   - 文档搜索功能：如果AWS Knowledge MCP后端在中国区不可访问，可使用本地文档或AWS中国官网文档
   - 本地验证工具：cfn-lint和cfn-guard完全本地运行，无需修改
   - 故障排查工具：直接连接中国区域的CloudFormation和CloudTrail API

### 注意事项

1. **区域配置**：确保在MCP配置中明确指定中国区域（cn-north-1或cn-northwest-1）

2. **凭证配置**：使用中国区域的AWS凭证，确保有足够的权限访问CloudFormation和CloudTrail

3. **网络访问**：
   - 本地验证工具无需网络访问
   - 远程文档搜索可能需要访问AWS Knowledge MCP后端，如不可用可使用本地文档替代

4. **ARN格式**：中国区域的ARN使用 `arn:aws-cn` 前缀，而非 `arn:aws`

5. **服务端点**：确保AWS SDK/CLI配置使用中国区域端点（自动处理，无需手动配置）

### 替代方案

如果远程文档搜索功能不可用，可采用以下替代方案：

1. **本地文档方案**
   - 下载AWS CDK和CloudFormation官方文档到本地
   - 使用本地搜索工具（如grep、ripgrep）
   - 复杂度：低
   - 适用场景：网络受限环境

2. **AWS中国官网文档**
   - 访问 https://docs.amazonaws.cn/ 获取中国区域文档
   - 使用浏览器搜索功能
   - 复杂度：低
   - 适用场景：需要中文文档或中国区域特定信息

### 风险提示

- **文档同步延迟**：AWS中国区域文档可能与全球区域存在更新延迟，建议关注版本差异
- **服务功能差异**：虽然核心功能一致，但某些新特性可能在中国区域延迟发布，使用前请确认功能可用性
- **网络连接**：远程文档搜索功能依赖网络连接，如果AWS Knowledge MCP后端在中国不可访问，需使用本地文档替代方案
- **合规要求**：使用AI助手处理基础设施代码时，注意数据隐私和合规要求，敏感信息不应发送给第三方AI服务

### 配套资源

- **GitHub仓库**: https://github.com/awslabs/mcp (AWS Labs MCP项目)
- **文档**: https://awslabs.github.io/mcp/servers/aws-iac-mcp-server
- **兼容性**: 工具本身完全兼容中国区域，本地执行无需修改
- **修改建议**: 
  - 配置文件中添加 `AWS_REGION` 环境变量指定中国区域
  - 使用中国区域的AWS Profile
  - 如需访问远程文档，可能需要配置网络代理
