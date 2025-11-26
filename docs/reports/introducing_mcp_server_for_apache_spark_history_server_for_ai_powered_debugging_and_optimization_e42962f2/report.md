---
title: 介绍用于Apache Spark History Server的MCP服务器，实现AI驱动的调试和优化
publish_date: 2025-07-23
original_url: https://aws.amazon.com/blogs/big-data/introducing-mcp-server-for-apache-spark-history-server-for-ai-powered-debugging-and-optimization/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 7
unavailable_services: 1
---

# 介绍用于Apache Spark History Server的MCP服务器，实现AI驱动的调试和优化

[📖 查看原始博客](https://aws.amazon.com/blogs/big-data/introducing-mcp-server-for-apache-spark-history-server-for-ai-powered-debugging-and-optimization/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

该项目的所有核心AWS服务（Amazon EMR、AWS Glue、Amazon EKS、Amazon EC2、Amazon S3）在中国区域均可用。唯一不可用的Amazon Q Developer CLI仅是可选的客户端集成之一，不影响MCP服务器的核心功能。

## 服务分析

### 可用服务 (7个)

- Amazon EMR
- AWS Glue
- Amazon EKS (Amazon Elastic Kubernetes Service)
- Amazon EC2 (Amazon Elastic Compute Cloud)
- Amazon S3
- Amazon MWAA (Amazon Managed Workflows for Apache Airflow)
- Amazon SageMaker Data Processing

### 不可用服务 (1个)

- **Amazon Q Developer CLI** - 可选客户端

### 评估说明

1. **核心服务完全可用**：项目依赖的所有核心AWS服务（EMR、Glue、EKS、EC2、S3）在中国区域均完全可用，可以正常部署和运行。

2. **不可用服务影响有限**：Amazon Q Developer CLI虽然在中国区不可用，但它只是MCP服务器支持的多个AI客户端之一。项目同时支持Claude Desktop、LlamaIndex、LangGraph等其他客户端，完全不影响核心功能。

3. **无需替代方案**：由于核心功能不受影响，无需寻找替代方案。用户可以选择使用其他支持的AI客户端（如Claude Desktop）来与MCP服务器交互。

## 验证结果

### 验证类型

✅ GitHub项目部署验证

### 执行状态

**状态**: ✅ 成功

### 关键发现

1. **项目成功部署**
   - 成功克隆GitHub仓库：https://github.com/DeepDiagnostix-AI/mcp-apache-spark-history-server
   - 所有Python依赖（包括boto3、pydantic、requests等）安装成功
   - 项目使用Python 3.12+，与当前环境完全兼容

2. **本地测试环境验证通过**
   - Spark History Server (v3.5.5) 成功启动在端口18080
   - MCP Server成功启动在端口18888
   - 端到端测试(e2e.py)执行成功，验证了MCP服务器的核心功能

3. **AWS服务集成验证**
   - AWS Glue API在cn-northwest-1区域响应正常
   - Amazon EMR API在cn-northwest-1区域响应正常
   - 项目提供的AWS集成示例（Glue和EMR）在中国区域完全适用

4. **架构灵活性**
   - MCP服务器支持多种部署方式：本地、EC2、EKS、Docker容器
   - 支持连接多个Spark History Server实例
   - 支持streamable-http和STDIO两种传输协议

5. **无需修正**
   - 项目在中国区域部署无需任何代码或配置修改
   - 所有依赖包可从标准PyPI源获取
   - AWS SDK (boto3)自动适配中国区域endpoint

## 实施建议

### 推荐方案

可直接按照原文实施，项目在AWS中国区域具有完全兼容性。

**实施步骤**：

1. **环境准备**
   - 确保Python 3.12+已安装
   - 安装uv包管理器和task工具
   - 配置AWS CLI访问中国区域（使用cn-northwest-1或cn-north-1）

2. **部署MCP服务器**
   - 克隆GitHub仓库
   - 根据实际需求选择部署方式：
     - 本地开发：使用Docker容器运行Spark History Server
     - AWS Glue集成：连接到自建或EC2上的Spark History Server
     - Amazon EMR集成：使用EMR Persistent UI功能

3. **配置服务器连接**
   - 编辑config.yaml文件，配置Spark History Server的URL和认证信息
   - 对于AWS Glue：配置EC2实例上的Spark UI URL
   - 对于Amazon EMR：配置EMR集群ARN，MCP服务器会自动管理Persistent UI

4. **选择AI客户端**
   - 推荐使用Claude Desktop（在中国区可用）
   - 或使用LlamaIndex、LangGraph等开源框架
   - 避免使用Amazon Q Developer CLI（中国区不可用）

**注意事项**：

- 确保网络连通性：MCP服务器需要能够访问Spark History Server的HTTP端口
- 对于私有子网中的EMR集群，需要配置SSH隧道或VPN访问
- 使用自签名证书时，在config.yaml中设置`verify_ssl: false`
- 建议为测试资源添加标签以便管理和清理

### 替代方案

无需替代方案。如果不想使用Amazon Q Developer CLI，可以选择以下客户端：

1. **Claude Desktop**
   - 实施方式：按照项目文档配置Claude Desktop集成
   - 复杂度：低
   - 适用场景：桌面环境下的交互式调试和分析

2. **LlamaIndex Agent**
   - 实施方式：使用Python SDK构建自定义AI代理
   - 复杂度：中
   - 适用场景：需要自定义工作流和自动化分析

3. **LangGraph**
   - 实施方式：构建复杂的多步骤分析流程
   - 复杂度：中到高
   - 适用场景：企业级自动化和复杂分析场景

### 风险提示

- **网络访问**：确保MCP服务器能够访问Spark History Server，特别是在私有子网环境中需要配置适当的网络路由
- **认证配置**：妥善管理Spark History Server的认证凭证，避免在配置文件中硬编码敏感信息，建议使用环境变量
- **资源清理**：测试完成后及时清理Docker容器和临时文件，避免占用系统资源
- **版本兼容**：项目要求Python 3.12+，确保运行环境满足版本要求
- **EMR Persistent UI权限**：使用EMR集成时，确保IAM角色具有创建和访问Persistent UI的权限

### 配套资源

- **GitHub仓库**: https://github.com/DeepDiagnostix-AI/mcp-apache-spark-history-server
- **兼容性**: 完全兼容AWS中国区域，无需修改
- **修改建议**: 
  - 无需修改代码
  - 配置文件中选择Claude Desktop或其他可用的AI客户端
  - AWS集成示例（Glue和EMR）可直接使用
  - 确保config.yaml中配置正确的区域endpoint（boto3会自动处理）

**AWS Glue集成示例**：
- 文档路径：examples/aws/glue/README.md
- 支持EC2上的自建Spark History Server
- 支持本地Docker容器部署

**Amazon EMR集成示例**：
- 文档路径：examples/aws/emr/README.md
- 使用EMR Persistent UI功能
- 自动管理认证和访问控制
