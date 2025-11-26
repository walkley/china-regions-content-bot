---
title: AWS发布账单和成本管理MCP服务器
publish_date: 2025-08-22
original_url: https://aws.amazon.com/blogs/aws-cloud-financial-management/aws-announces-billing-and-cost-management-mcp-server/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 12
unavailable_services: 0
---

# AWS发布账单和成本管理MCP服务器

[📖 查看原始博客](https://aws.amazon.com/blogs/aws-cloud-financial-management/aws-announces-billing-and-cost-management-mcp-server/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

该博客介绍的AWS Billing and Cost Management MCP Server所依赖的所有AWS服务在中国区域均完全可用，GitHub项目已成功部署验证，可以直接在中国区域实施使用。

## 服务分析

### 可用服务 (12个)

- AWS Cost Explorer
- AWS Cost Optimization Hub
- AWS Compute Optimizer
- AWS Savings Plans
- AWS Budgets
- Amazon S3 Storage Lens
- AWS Cost Anomaly Detection
- AWS CLI
- AWS IAM
- Amazon S3
- AWS Athena
- AWS Glue

### 不可用服务 (0个)

无

### 评估说明

本博客介绍了AWS Billing and Cost Management MCP Server，这是一个Model Context Protocol (MCP)服务器，用于将AWS成本分析和优化功能集成到AI助手中。经过全面验证：

1. **核心服务完全可用**：所有12个依赖的AWS服务在中国区域均可正常使用
2. **API功能正常**：Cost Explorer、Compute Optimizer、Budgets、Pricing等关键API在cn-northwest-1区域测试通过
3. **GitHub项目可部署**：成功克隆并安装了配套的MCP服务器项目，所有依赖包正常安装
4. **无架构限制**：MCP服务器基于boto3 SDK，与区域无关，只需配置正确的AWS_REGION和AWS_PROFILE即可

## 验证结果

### 验证类型

✅ GitHub项目部署验证

### 执行状态

**状态**: ✅ 成功

### 关键发现

1. **服务API完全兼容**
   - 在cn-northwest-1区域成功调用了Cost Explorer、Compute Optimizer、Budgets、Pricing等所有核心API
   - 所有API返回正常，数据格式与全球区域一致
   - 无需任何代码修改即可在中国区域使用

2. **项目部署顺利**
   - 使用uv包管理器成功创建虚拟环境
   - 所有Python依赖包（boto3、fastmcp、pydantic等）正常安装
   - MCP服务器成功启动，显示14个可用工具和2个提示模板

3. **配置简单直接**
   - 只需设置AWS_PROFILE和AWS_REGION环境变量
   - 支持通过~/.aws/amazonq/mcp.json配置文件集成到Amazon Q Developer CLI
   - 支持Docker部署方式

4. **功能测试通过**
   - Cost Explorer API：成功获取成本数据
   - Compute Optimizer API：成功获取优化建议状态
   - Budgets API：成功查询预算信息
   - Pricing API：成功获取服务定价信息

## 实施建议

### 推荐方案

可直接按照原文实施，具体步骤：

1. **安装前置依赖**
   ```bash
   # 安装uv包管理器
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # 安装Python 3.10+
   uv python install 3.12
   ```

2. **配置AWS凭证**
   ```bash
   # 配置中国区域凭证
   aws configure --profile cn
   # 设置区域为 cn-northwest-1 或 cn-north-1
   ```

3. **配置MCP服务器**
   
   编辑 `~/.aws/amazonq/mcp.json`（Linux/MacOS）：
   ```json
   {
     "mcpServers": {
       "awslabs.billing-cost-management-mcp-server": {
         "command": "uvx",
         "args": [
            "awslabs.billing-cost-management-mcp-server@latest"
         ],
         "env": {
           "FASTMCP_LOG_LEVEL": "ERROR",
           "AWS_PROFILE": "cn",
           "AWS_REGION": "cn-northwest-1"
         },
         "disabled": false,
         "autoApprove": []
       }
     }
   }
   ```

4. **启动使用**
   - 重启Amazon Q Developer CLI或其他MCP客户端
   - 开始使用自然语言查询AWS成本数据

**注意事项**：
- 确保IAM用户/角色具有必要的Cost Explorer、Compute Optimizer等服务权限
- Cost Explorer需要在AWS账户中启用（首次使用需要24小时初始化）
- 中国区域使用cn-northwest-1或cn-north-1作为AWS_REGION
- API调用会产生费用，建议查看各服务的定价页面

### 替代方案

无需替代方案，原方案完全适用。

### 风险提示

- **API调用费用**：每次API调用都会产生费用，建议合理控制查询频率
- **权限配置**：需要配置较多的IAM权限，建议遵循最小权限原则
- **Cost Explorer初始化**：首次启用Cost Explorer需要等待24小时才能获取数据
- **Storage Lens配置**：如需使用S3 Storage Lens功能，需要额外配置Storage Lens仪表板和数据导出

### 配套资源

- **GitHub仓库**: https://github.com/awslabs/mcp/tree/main/src/billing-cost-management-mcp-server
- **兼容性**: ✅ 完全兼容中国区域，无需修改
- **修改建议**: 
  - 将配置文件中的`AWS_REGION`改为`cn-northwest-1`或`cn-north-1`
  - 将`AWS_PROFILE`改为指向中国区域的AWS凭证配置
  - 其他配置保持不变

**文档资源**：
- [MCP服务器官方文档](https://awslabs.github.io/mcp/servers/billing-cost-management-mcp-server/)
- [AWS Cost Explorer用户指南](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [AWS Compute Optimizer用户指南](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)
