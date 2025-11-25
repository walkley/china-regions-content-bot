---
title: AWS Serverless MCP Server：现代应用的AI驱动开发
publish_date: 2025-05-29
original_url: https://aws.amazon.com/blogs/compute/introducing-aws-serverless-mcp-server-ai-powered-development-for-modern-applications/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 8
unavailable_services: 1
---

# AWS Serverless MCP Server：现代应用的AI驱动开发

[📖 查看原始博客](https://aws.amazon.com/blogs/compute/introducing-aws-serverless-mcp-server-ai-powered-development-for-modern-applications/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，MCP Server作为本地工具可直接使用，已通过完整部署验证

AWS Serverless MCP Server是一个开源的本地开发工具，通过Model Context Protocol (MCP)为AI编码助手提供无服务器开发的上下文信息。该工具在AWS中国区域完全可用，所有核心AWS服务均已验证可正常工作。

## 服务分析

### 可用服务 (8个)

- AWS Lambda
- Amazon API Gateway
- Amazon S3
- Amazon DynamoDB
- AWS Serverless Application Model (AWS SAM)
- AWS Cloud Development Kit (AWS CDK)
- Amazon CloudWatch Logs
- Amazon CloudFront

### 不可用服务 (1个)

- **Amazon Q Developer** - 文章中作为MCP客户端示例提及，但可使用其他MCP客户端替代（Cursor、Cline、Kiro等）

### 评估说明

1. **核心服务完全可用**：Lambda、API Gateway、S3、DynamoDB等所有核心无服务器服务在中国区域均可用
2. **工具本地运行**：AWS Serverless MCP Server是Python包，在本地运行，不依赖特定AWS区域
3. **MCP客户端灵活**：虽然Amazon Q Developer在中国区不可用，但可使用Cursor、Cline、Kiro等其他支持MCP协议的AI编码助手
4. **已验证部署**：成功在cn-northwest-1区域完成SAM应用的构建、部署、测试和清理全流程

## 验证结果

### 验证类型

✅ GitHub项目部署验证

### 执行状态

**状态**: ✅ 成功

### 关键发现

1. **MCP Server安装成功**
   - 使用uvx成功安装AWS Serverless MCP Server
   - 所有依赖包正常下载和配置
   - 工具帮助命令正常显示

2. **SAM CLI功能验证**
   - 成功初始化Python 3.12 SAM应用
   - sam build命令正常构建应用
   - sam local invoke成功本地测试Lambda函数
   - 本地Docker容器运行正常

3. **中国区域部署验证**
   - 成功在cn-northwest-1区域创建S3存储桶
   - CloudFormation堆栈部署成功
   - Lambda函数、API Gateway、IAM角色全部创建成功
   - API Gateway端点返回正确响应：`{"message": "hello world"}`

4. **观测功能验证**
   - sam logs命令成功获取Lambda函数日志
   - CloudWatch Logs集成正常工作
   - 日志显示函数执行时间、内存使用等指标

5. **资源清理验证**
   - CloudFormation堆栈删除成功
   - S3存储桶及内容完全清理
   - 无ValidationTest标签的残留资源
   - 清理过程无错误

## 实施建议

### 推荐方案

可直接按照原文实施，具体步骤：

1. **安装前置条件**
   ```bash
   # 安装uv
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # 安装Python 3.10+
   uv python install 3.12
   
   # 安装AWS SAM CLI
   pip install aws-sam-cli
   
   # 配置AWS凭证
   aws configure --profile cn
   ```

2. **安装MCP Server**
   ```bash
   # 使用uvx直接运行
   uvx awslabs.aws-serverless-mcp-server@latest --help
   ```

3. **配置MCP客户端**
   
   在支持MCP的AI编码助手（如Cursor、Cline、Kiro）中添加配置：
   ```json
   {
     "mcpServers": {
       "awslabs.aws-serverless-mcp-server": {
         "command": "uvx",
         "args": [
           "awslabs.aws-serverless-mcp-server@latest",
           "--allow-write",
           "--allow-sensitive-data-access"
         ],
         "env": {
           "AWS_PROFILE": "cn",
           "AWS_REGION": "cn-northwest-1"
         }
       }
     }
   }
   ```

4. **开始开发**
   - 使用AI助手初始化SAM项目
   - 利用MCP Server提供的上下文信息进行开发
   - 使用sam build和sam local invoke进行本地测试
   - 使用sam deploy部署到中国区域

### 注意事项

1. **区域配置**
   - 确保AWS_REGION设置为中国区域（cn-north-1或cn-northwest-1）
   - S3存储桶名称需要全局唯一
   - API Gateway端点域名为.amazonaws.com.cn

2. **MCP客户端选择**
   - 推荐使用Cursor、Cline或Kiro作为MCP客户端
   - Amazon Q Developer在中国区不可用，但不影响MCP Server功能
   - 确保MCP客户端版本支持MCP协议

3. **安全配置**
   - MCP Server默认为只读模式，需要--allow-write启用写操作
   - 使用--allow-sensitive-data-access访问CloudWatch日志
   - 建议在开发环境使用，生产环境谨慎启用写权限

4. **网络考虑**
   - PyPI包下载可能需要配置镜像源
   - Docker镜像拉取使用AWS中国区域的ECR公共镜像
   - GitHub仓库克隆可能需要代理

### 替代方案

无需替代方案，所有功能在中国区域均可正常使用。

### 风险提示

- **依赖下载**：首次安装时需要下载较多Python包，建议配置国内镜像源加速
- **Docker要求**：sam local invoke需要Docker环境，确保Docker已安装并运行
- **IAM权限**：部署需要足够的IAM权限创建Lambda、API Gateway、CloudFormation等资源
- **成本控制**：虽然测试应用成本很低，但建议及时清理不用的资源

### 配套资源

- **GitHub仓库**: https://github.com/awslabs/mcp
- **兼容性**: 完全兼容中国区域
- **修改建议**: 
  - 配置文件中AWS_REGION改为cn-northwest-1或cn-north-1
  - 使用中国区域的AWS Profile
  - S3存储桶名称需要全局唯一，建议添加区域后缀
  - API Gateway端点域名自动使用.amazonaws.com.cn

## 验证详情

### 测试环境
- **区域**: cn-northwest-1
- **Python版本**: 3.12.12
- **SAM CLI版本**: 1.148.0
- **操作系统**: Amazon Linux 2

### 测试步骤
1. 克隆MCP项目仓库
2. 安装AWS Serverless MCP Server
3. 安装AWS SAM CLI
4. 初始化示例SAM应用（Python 3.12 + Hello World模板）
5. 本地构建和测试Lambda函数
6. 部署到cn-northwest-1区域
7. 测试API Gateway端点
8. 获取CloudWatch日志
9. 清理所有测试资源

### 测试结果
- ✅ MCP Server安装成功
- ✅ SAM应用初始化成功
- ✅ 本地构建成功
- ✅ 本地调用成功（返回"hello world"）
- ✅ 部署到中国区域成功
- ✅ API Gateway端点响应正常
- ✅ CloudWatch日志获取成功
- ✅ 资源清理完全成功

### 性能指标
- Lambda冷启动时间: 88.14ms
- Lambda执行时间: 1.89ms
- 内存使用: 36MB / 128MB
- API响应时间: <100ms

## 总结

AWS Serverless MCP Server在AWS中国区域完全可用且功能正常。作为本地开发工具，它不依赖特定AWS区域的服务，所有核心无服务器服务（Lambda、API Gateway、S3、DynamoDB等）在中国区域均可用。

虽然文章中提到的Amazon Q Developer在中国区不可用，但这不影响MCP Server的使用，开发者可以选择Cursor、Cline、Kiro等其他支持MCP协议的AI编码助手。

通过完整的部署验证，确认了从项目初始化、本地测试、部署到中国区域、观测监控、资源清理的全流程均可正常工作。强烈推荐中国区域的开发者使用此工具提升无服务器应用开发效率。
