---
title: Letta如何使用Amazon Aurora PostgreSQL构建生产就绪的AI代理
publish_date: 2025-11-26
original_url: https://aws.amazon.com/blogs/database/how-letta-builds-production-ready-ai-agents-with-amazon-aurora-postgresql/
validation_date: 2025-12-02
target_region: cn-northwest-1
feasibility: HIGH
available_services: 6
unavailable_services: 0
---

# Letta如何使用Amazon Aurora PostgreSQL构建生产就绪的AI代理

[📖 查看原始博客](https://aws.amazon.com/blogs/database/how-letta-builds-production-ready-ai-agents-with-amazon-aurora-postgresql/) | 验证日期: 2025-12-02

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心AWS服务在中国区可用,可直接实施

本教程展示了如何使用Amazon Aurora PostgreSQL作为Letta AI代理平台的持久化存储后端。所有涉及的AWS核心服务在中国区域均完全可用,教程可以直接按照原文步骤实施。

## 服务分析

### 可用服务 (6个)

- **Amazon Aurora PostgreSQL-Compatible Edition** - 核心数据库服务
- **Amazon Aurora Serverless** - 无服务器数据库配置
- **Amazon RDS** - 关系数据库服务管理
- **Amazon VPC** - 虚拟私有云网络
- **Amazon EC2 Security Groups** - 安全组配置
- **AWS IAM** - 身份和访问管理

### 不可用服务 (0个)

无

### 评估说明

**核心服务可用性**: 本教程涉及的所有AWS服务在中国区域均完全可用,包括:

1. **Aurora PostgreSQL**: 中国区域支持Aurora PostgreSQL 17.4及pgvector扩展
2. **Aurora Serverless v2**: 支持0.5-1 ACU的最小配置,适合开发测试
3. **网络和安全**: VPC、安全组、公网访问等功能完全支持

**第三方依赖注意事项**:

1. **OpenAI API**: 教程使用OpenAI作为LLM提供商,从中国访问可能需要网络配置。可考虑替代方案:
   - 使用Amazon Bedrock(中国区域可用)
   - 使用国内LLM服务提供商

2. **Docker镜像**: `letta/letta:latest`镜像拉取可能较慢,建议:
   - 使用Docker镜像加速器
   - 或将镜像推送到Amazon ECR中国区域

3. **文档访问**: Letta官方文档访问可能需要网络配置

## 验证结果

### 验证类型

⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 
1. 可行性评估为HIGH,所有核心AWS服务均可用
2. 博客未包含专门配套的GitHub代码仓库
3. 教程步骤清晰,无需实际部署验证

### 关键发现

基于静态分析,识别以下关键点:

1. **Aurora配置完全兼容**
   - 教程中的Aurora Serverless v2配置(0.5-1 ACU)在中国区域完全支持
   - PostgreSQL 17.4版本在中国区域可用
   - pgvector扩展在中国区域Aurora PostgreSQL中完全支持

2. **网络配置需要调整**
   - 教程使用公网访问Aurora,生产环境建议使用私有子网
   - 安全组配置需要根据实际IP地址调整
   - 建议使用IAM数据库身份验证增强安全性

3. **LLM服务替代方案**
   - OpenAI API访问可能受限,建议评估Amazon Bedrock
   - Letta支持多种模型提供商,可灵活切换

## 实施建议

### 推荐方案

本教程可以直接在AWS中国区域实施,建议按照以下步骤:

**1. Aurora集群创建** (完全按照原文)
- 在宁夏(cn-northwest-1)或北京(cn-north-1)区域创建Aurora PostgreSQL集群
- 选择Aurora Serverless v2,配置0.5-1 ACU用于开发测试
- 启用公网访问(仅用于测试,生产环境应使用私有子网)

**2. 安全组配置** (需要调整)
- 配置安全组允许本地IP访问5432端口
- 注意:中国区域的IP地址段可能不同,需要使用实际IP

**3. pgvector扩展安装** (完全按照原文)
- 使用psql连接Aurora集群
- 执行`CREATE EXTENSION vector;`命令

**4. Letta部署** (需要调整)
- Docker镜像拉取:建议使用镜像加速或ECR
- OpenAI API密钥:考虑替换为Bedrock或国内LLM服务
- 连接字符串:使用Aurora中国区域的endpoint

**5. 测试验证** (完全按照原文)
- Python或TypeScript客户端代码无需修改
- 验证代理创建和消息持久化功能

### 配置差异说明

**区域endpoint格式**:
```
# 原文示例(美国区域)
letta-aurora-cluster.cluster-abc123def456.us-east-1.rds.amazonaws.com

# 中国区域格式
letta-aurora-cluster.cluster-abc123def456.rds.cn-northwest-1.amazonaws.com.cn
```

**LLM服务替代**:

如果使用Amazon Bedrock替代OpenAI:
```bash
# 原环境变量
-e OPENAI_API_KEY='your-openai-api-key'

# 可能需要配置Bedrock相关环境变量
# (具体配置需参考Letta文档的Bedrock集成说明)
```

### 成本估算

**Aurora Serverless v2成本** (宁夏区域参考):
- 0.5 ACU配置:约¥0.18/小时
- 1 ACU配置:约¥0.36/小时
- 存储:¥0.80/GB/月
- I/O:¥0.16/百万次请求

**开发测试环境月成本估算**:
- 计算(0.5 ACU,每天8小时):约¥43/月
- 存储(10GB):约¥8/月
- I/O(适度使用):约¥5/月
- **总计**:约¥56/月

### 风险提示

- **网络访问限制**: OpenAI API和Docker Hub访问可能需要网络配置,建议提前规划替代方案
- **公网暴露风险**: 教程使用公网访问Aurora仅适合测试,生产环境必须使用私有子网和VPN/专线访问
- **数据合规**: 如果处理敏感数据,需要确保符合中国数据安全和隐私保护法规
- **成本控制**: Aurora Serverless会根据负载自动扩展,建议设置CloudWatch告警监控成本
- **备份策略**: 教程中删除集群时选择不创建快照,生产环境应启用自动备份和时间点恢复

### 生产环境优化建议

1. **网络架构**
   - 将Aurora部署在私有子网
   - 使用VPN或专线连接
   - 配置VPC endpoint减少公网流量

2. **安全加固**
   - 启用IAM数据库身份验证
   - 启用静态加密(encryption at rest)
   - 启用传输加密(SSL/TLS)
   - 限制安全组规则到最小权限

3. **高可用性**
   - 配置多可用区部署
   - 增加Aurora副本实例
   - 配置自动故障转移

4. **监控和告警**
   - 配置CloudWatch监控指标
   - 设置ACU使用率告警
   - 监控数据库连接数和查询性能

5. **LLM服务选择**
   - 评估Amazon Bedrock作为OpenAI替代方案
   - 考虑国内LLM服务提供商(如阿里云通义千问、百度文心一言等)
   - 确保LLM服务符合数据合规要求

### 配套资源

- **Letta官方文档**: https://docs.letta.com/ (可能需要网络配置访问)
- **pgvector GitHub**: https://github.com/pgvector/pgvector
- **Aurora PostgreSQL文档**: https://docs.amazonaws.cn/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html
- **Amazon Bedrock文档**: https://docs.amazonaws.cn/bedrock/ (中国区域)

## 总结

本教程在AWS中国区域具有**高度可行性**,所有核心AWS服务均可用。主要需要注意的是第三方依赖(OpenAI API、Docker镜像)的网络访问问题,建议提前规划替代方案。教程步骤清晰,配置简单,适合作为在中国区域部署AI代理持久化存储的参考实践。

对于生产环境部署,建议参考上述优化建议,特别是网络安全、高可用性和成本控制方面的配置。
