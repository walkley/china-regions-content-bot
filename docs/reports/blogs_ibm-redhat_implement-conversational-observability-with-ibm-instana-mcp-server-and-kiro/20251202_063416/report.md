---
title: 使用IBM Instana MCP服务器和Kiro实现对话式可观测性
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/ibm-redhat/implement-conversational-observability-with-ibm-instana-mcp-server-and-kiro/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: MODERATE
available_services: 13
unavailable_services: 2
---

# 使用IBM Instana MCP服务器和Kiro实现对话式可观测性

[📖 查看原始博客](https://aws.amazon.com/blogs/ibm-redhat/implement-conversational-observability-with-ibm-instana-mcp-server-and-kiro/) | 验证日期: 2025-12-02

## 可行性评估

!!! warning "MODERATE - 谨慎实施"
    大部分AWS服务在中国区可用，但核心第三方服务（Kiro CLI/IDE和AWS Marketplace订阅流程）存在访问限制，需要适当调整实施方案

本文介绍了如何通过IBM Instana MCP服务器与Kiro CLI/IDE集成，实现AI驱动的对话式可观测性工作流。虽然文章中涉及的AWS基础设施服务在中国区域基本可用，但实施过程中需要注意以下关键因素：

1. **AWS Marketplace访问限制**：中国区域的AWS Marketplace功能受限，无法直接通过Marketplace订阅IBM Instana MCP Server容器镜像
2. **Kiro服务可用性**：Kiro CLI和Kiro IDE是由AWS提供的AI助手工具，在中国区域的访问和功能可能受到限制
3. **容器镜像获取**：需要通过替代方案获取Instana MCP Server容器镜像

## 服务分析

### 可用服务 (13个)

- Amazon Elastic Container Registry (Amazon ECR)
- AWS Identity and Access Management (IAM)
- Amazon Elastic Compute Cloud (Amazon EC2)
- Amazon Elastic Kubernetes Service (Amazon EKS)
- Amazon Elastic Container Service (Amazon ECS)
- AWS Secrets Manager
- AWS Systems Manager Parameter Store
- AWS Key Management Service (AWS KMS)
- Amazon Virtual Private Cloud (Amazon VPC)
- Amazon CloudWatch Logs
- AWS Fargate
- AWS PrivateLink
- AWS CLI

### 不可用或受限服务 (2个)

- **AWS Marketplace** - 核心服务（中国区域功能受限，无法直接订阅第三方容器镜像）
- **Amazon Bedrock** - 在相关内容中提到（中国区域不可用）

### 第三方服务依赖

- **IBM Instana Observability** - 核心服务（需要单独订阅，支持SaaS和自托管部署）
- **Kiro CLI / Kiro IDE** - 核心工具（AWS AI助手，中国区域访问可能受限）
- **Docker** - 必需工具（可用）

### 评估说明

**服务可用性分析：**

1. **AWS基础设施服务**：文章中涉及的13个AWS核心服务（EC2、EKS、ECS、ECR、IAM、Secrets Manager等）在AWS中国区域（宁夏和北京）均完全可用，可以正常部署和运行Instana MCP Server容器。

2. **AWS Marketplace限制**：
   - 中国区域的AWS Marketplace功能与全球区域不同，无法直接订阅和拉取第三方容器镜像
   - 文章中的核心步骤（从Marketplace订阅并通过ECR拉取镜像）在中国区域无法直接执行
   - 需要通过IBM官方渠道或Docker Hub等替代方式获取Instana MCP Server镜像

3. **Kiro工具可用性**：
   - Kiro CLI和Kiro IDE是AWS提供的AI助手工具，基于Amazon Q技术
   - 中国区域对这些工具的访问可能受到网络限制
   - 需要验证Kiro服务在中国区域的实际可用性和功能完整性

4. **IBM Instana服务**：
   - IBM Instana Observability本身支持SaaS和自托管两种部署模式
   - 自托管模式可以在AWS中国区域的EC2、EKS或ECS上部署
   - SaaS模式需要确认IBM是否在中国区域提供服务端点

5. **网络连接考虑**：
   - MCP Server需要与Instana后端API通信
   - Kiro需要与MCP Server通信
   - 需要确保网络连接的稳定性和合规性

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 根据验证策略，统一跳过深入验证阶段以节约时间。基于静态分析，已完成服务可用性评估和实施建议。

### 关键发现

基于静态分析，识别出以下关键问题：

1. **AWS Marketplace订阅流程不适用**
   - 中国区域无法通过Marketplace直接订阅IBM Instana MCP Server
   - 需要寻找替代的镜像获取方式

2. **Kiro工具访问限制**
   - Kiro CLI/IDE在中国区域的可用性需要单独验证
   - 可能需要配置代理或使用VPN访问

3. **网络架构调整**
   - 如果使用Instana SaaS，需要确保中国区域可以访问Instana服务端点
   - 建议使用自托管模式以获得更好的控制和性能

## 实施建议

### 推荐方案

**主要实施路径：**

由于AWS Marketplace和Kiro工具的限制，建议采用以下调整后的实施方案：

1. **容器镜像获取替代方案**：
   - 联系IBM官方获取Instana MCP Server容器镜像的直接下载链接
   - 或从Docker Hub等公共镜像仓库获取（如果IBM提供）
   - 将镜像推送到AWS中国区域的Amazon ECR私有仓库

2. **Instana部署模式选择**：
   - **推荐**：使用Instana自托管模式，部署在AWS中国区域
   - 优势：数据本地化、网络延迟低、合规性好
   - 部署位置：Amazon EKS或Amazon ECS

3. **Kiro工具替代方案**：
   - 如果Kiro CLI/IDE无法在中国区域正常使用，可以考虑：
     - 使用标准的MCP客户端工具
     - 开发自定义的命令行工具调用MCP Server API
     - 使用Postman或curl直接测试MCP Server的HTTP端点

4. **网络配置**：
   - 在VPC内部署MCP Server和Instana后端
   - 使用VPC Endpoints和PrivateLink确保内网通信
   - 配置安全组严格控制访问

**需要调整的部分：**

1. **订阅和镜像获取**（步骤1-4）：
   - 跳过AWS Marketplace订阅步骤
   - 通过IBM官方渠道获取镜像
   - 手动推送到中国区域ECR

2. **Kiro配置**（步骤6-20）：
   - 如果Kiro不可用，使用替代的MCP客户端
   - 或直接使用HTTP API调用MCP Server

3. **API端点配置**：
   - 确保所有配置中的Instana租户URL指向可访问的端点
   - 如果使用自托管Instana，使用内网地址

**预计工作量：**

- **镜像迁移和部署**：2-4小时
- **Instana自托管部署**（如选择）：1-2天
- **MCP Server配置和测试**：4-8小时
- **客户端工具适配**（如Kiro不可用）：1-2天
- **总计**：3-5天（取决于是否需要部署自托管Instana）

### 替代方案

#### 方案1：完全自托管架构

**实施方式：**
- 在Amazon EKS上部署Instana自托管版本
- 在Amazon ECS或EC2上部署MCP Server容器
- 开发自定义CLI工具或Web界面与MCP Server交互

**复杂度**：高

**适用场景**：
- 需要完全的数据主权和控制
- 对网络延迟敏感
- 有足够的运维资源

**优势**：
- 完全在中国区域内运行，无外部依赖
- 数据不出境，符合合规要求
- 可定制化程度高

**劣势**：
- 初始部署和维护成本高
- 需要自行管理Instana和MCP Server的更新

#### 方案2：混合模式（Instana SaaS + 本地MCP Server）

**实施方式：**
- 使用IBM Instana SaaS服务（如果在中国有服务节点）
- 在AWS中国区域部署MCP Server
- 使用开源MCP客户端或自定义工具

**复杂度**：中

**适用场景**：
- 希望减少运维负担
- IBM在中国提供Instana SaaS服务
- 可以接受数据传输到Instana SaaS

**优势**：
- Instana由IBM管理，减少运维工作
- MCP Server本地部署，响应快

**劣势**：
- 依赖Instana SaaS的可用性和网络连接
- 可能存在数据出境问题

#### 方案3：仅使用Instana REST API

**实施方式：**
- 跳过MCP Server和Kiro
- 直接使用Instana REST API
- 开发自定义脚本或工具进行查询

**复杂度**：低

**适用场景**：
- 只需要基本的查询功能
- 不需要AI对话式交互
- 快速验证概念

**优势**：
- 实施简单，无额外依赖
- 完全控制查询逻辑

**劣势**：
- 失去AI对话式交互的便利性
- 需要熟悉Instana API文档

### 风险提示

- **网络连接风险**：如果使用Instana SaaS，需要确保中国区域到Instana服务端点的网络稳定性和合规性，可能存在延迟或连接中断问题
- **工具可用性风险**：Kiro CLI/IDE在中国区域的可用性未经验证，可能无法正常使用或功能受限，需要准备替代方案
- **镜像获取风险**：无法通过AWS Marketplace获取官方镜像，需要通过其他渠道获取，可能存在版本更新不及时的问题
- **合规性风险**：使用Instana SaaS可能涉及数据跨境传输，需要评估是否符合中国的数据安全和隐私法规要求
- **成本风险**：自托管Instana需要额外的基础设施成本（EC2、EKS、存储等），需要提前评估和预算
- **技术支持风险**：在中国区域实施可能无法获得与全球区域相同级别的技术支持，问题解决周期可能较长
- **API兼容性风险**：Instana MCP Server的API调用可能因网络或配置问题导致超时或失败，需要实施重试和错误处理机制

### 配套资源

- **GitHub仓库**: https://github.com/instana/mcp-instana
- **兼容性**: 开源项目，代码可在任何区域使用
- **修改建议**: 
  - 修改容器镜像来源，从IBM官方渠道或Docker Hub获取
  - 调整配置文件中的Instana端点URL，指向中国区域可访问的地址
  - 如果Kiro不可用，参考项目文档实现自定义MCP客户端
  - 添加网络重试和超时配置以应对网络不稳定情况

### 实施检查清单

在开始实施前，建议完成以下检查：

- [ ] 确认IBM Instana在中国区域的服务模式（SaaS或自托管）
- [ ] 验证Kiro CLI/IDE在目标环境的可用性
- [ ] 获取Instana MCP Server容器镜像的访问权限
- [ ] 评估数据合规性要求（数据存储位置、传输加密等）
- [ ] 准备AWS中国区域的基础设施（VPC、EKS/ECS、ECR等）
- [ ] 配置网络连接和安全组规则
- [ ] 准备Instana API Token和租户信息
- [ ] 制定备份和灾难恢复计划（如果自托管）

### 相关文档

- [AWS中国区域服务列表](https://www.amazonaws.cn/en/about-aws/regional-product-services/)
- [Amazon ECR用户指南（中国区域）](https://docs.amazonaws.cn/AmazonECR/latest/userguide/)
- [IBM Instana文档](https://www.ibm.com/docs/en/instana-observability)
- [Model Context Protocol规范](https://modelcontextprotocol.io/docs/getting-started/intro)
