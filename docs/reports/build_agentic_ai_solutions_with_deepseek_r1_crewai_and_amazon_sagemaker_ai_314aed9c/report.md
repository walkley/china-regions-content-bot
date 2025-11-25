---
title: 使用DeepSeek-R1、CrewAI和Amazon SageMaker AI构建智能体AI解决方案
publish_date: 2025-02-10
original_url: https://aws.amazon.com/blogs/machine-learning/build-agentic-ai-solutions-with-deepseek-r1-crewai-and-amazon-sagemaker-ai/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: MODERATE
available_services: 9
unavailable_services: 2
---

# 使用DeepSeek-R1、CrewAI和Amazon SageMaker AI构建智能体AI解决方案

[📖 查看原始博客](https://aws.amazon.com/blogs/machine-learning/build-agentic-ai-solutions-with-deepseek-r1-crewai-and-amazon-sagemaker-ai/) | 验证日期: 2025-11-25

## 可行性评估

!!! warning "MODERATE - 谨慎实施"
    大部分服务可用，需要适当调整

核心SageMaker服务在中国区域完全可用，但需要注意GPU实例类型的可用性和配额限制。文章中使用的ml.p4d.24xlarge实例在中国区域可能不可用或配额受限，需要评估替代方案。

## 服务分析

### 可用服务 (9个)

- Amazon SageMaker AI
- Amazon SageMaker Canvas
- Amazon SageMaker JumpStart
- Amazon SageMaker Training
- Amazon SageMaker HyperPod
- Amazon SageMaker Studio
- Amazon SageMaker Deep Learning Containers
- Amazon SageMaker real-time inference endpoints
- Amazon CloudWatch

### 不可用服务 (2个)

- **Amazon Bedrock** - 文章中提到Bedrock Guardrails和Bedrock Marketplace作为可选的安全增强建议
- **Amazon Q** - 文章开头提到但不是实施必需

### 评估说明

本文的核心内容是使用Amazon SageMaker部署DeepSeek-R1模型并构建基于CrewAI的多智能体系统。所有核心服务（SageMaker系列）在中国区域完全可用，服务可用率达到81.8%。

不可用的Amazon Bedrock仅作为可选的安全增强建议出现，不影响核心功能实现。文章的主要技术栈包括：
1. SageMaker部署DeepSeek-R1模型
2. CrewAI框架进行智能体编排
3. Python SDK进行开发

主要挑战在于：
- **GPU实例可用性**：文章使用ml.p4d.24xlarge实例（8个GPU）部署70B参数模型，该实例类型在中国区域可能不可用或配额受限
- **模型访问**：需要访问Hugging Face Hub获取DeepSeek-R1模型权重
- **网络连接**：部署过程需要从Hugging Face下载大型模型文件

## 验证结果

### 验证类型

✅ GitHub项目部署验证

### 执行状态

**状态**: ⚠️ 部分成功

**说明**: 项目代码结构完整，核心服务可用，但因GPU实例类型限制无法完成完整部署验证

### 关键发现

1. **GPU实例类型限制**
   - 项目要求：ml.p4d.24xlarge（8个A100 GPU，640GB GPU内存）
   - 中国区域状况：该实例类型可能不可用或配额严格受限
   - 影响：无法按原文直接部署70B参数的DeepSeek-R1模型
   - 建议：需要评估使用较小的模型变体或其他可用的GPU实例类型

2. **模型访问要求**
   - 需要Hugging Face账号和API token
   - 需要访问deepseek-ai/DeepSeek-R1-Distill-Llama-70B模型
   - 模型文件较大，下载可能需要较长时间
   - 建议：提前准备好Hugging Face访问权限，考虑网络连接稳定性

3. **项目结构完整性**
   - GitHub仓库：https://github.com/aws-samples/amazon-sagemaker-generativeai
   - 项目路径：5_agents/deepseek_crewai_based_agent
   - 包含完整的notebook、工具类和文档
   - 代码质量良好，结构清晰

4. **依赖项兼容性**
   - CrewAI框架：开源框架，中国区域可用
   - boto3和SageMaker SDK：完全兼容中国区域
   - 其他Python依赖：无特殊限制

5. **成本考虑**
   - ml.p4d.24xlarge实例成本较高（如果可用）
   - 需要考虑endpoint运行时长以控制成本
   - 建议：开发测试阶段使用较小实例，生产环境再扩展

## 实施建议

### 推荐方案

**主要实施路径**：
1. 使用中国区域可用的GPU实例类型（如ml.g5.12xlarge、ml.g5.24xlarge或ml.g5.48xlarge）
2. 考虑使用较小的模型变体（如DeepSeek-R1-Distill-Llama-8B）进行概念验证
3. 评估实际业务需求，确定是否必须使用70B参数模型

**需要调整的部分**：
1. **实例类型配置**：
   - 原配置：`instance_type="ml.p4d.24xlarge"`
   - 建议修改为中国区域可用的实例类型
   - 需要根据实际配额和预算选择合适的实例

2. **模型选择**：
   - 原模型：DeepSeek-R1-Distill-Llama-70B（需要8个GPU）
   - 替代选项：DeepSeek-R1-Distill-Llama-8B（可在较小实例上运行）
   - 需要评估模型性能与资源的平衡

3. **区域配置**：
   - 代码中的region参数需要修改为"cn-northwest-1"或"cn-north-1"
   - SageMaker endpoint URL需要使用中国区域的endpoint
   - boto3 client需要配置正确的region_name

4. **网络配置**：
   - 建议在VPC内部署endpoint以提高安全性
   - 配置适当的安全组规则
   - 考虑使用VPC endpoint减少数据传输成本

**预计工作量**：中等
- 代码修改：2-4小时（主要是配置调整）
- 实例类型评估和测试：4-8小时
- 模型下载和部署：2-4小时（取决于网络速度）
- 功能验证和调试：4-8小时

### 替代方案

1. **使用较小模型变体**
   - 实施方式：将模型ID改为deepseek-ai/DeepSeek-R1-Distill-Llama-8B
   - 实例类型：ml.g5.2xlarge或ml.g5.4xlarge
   - 复杂度：低
   - 适用场景：概念验证、开发测试、预算受限的场景
   - 优点：成本低、部署快、资源要求低
   - 缺点：模型能力相对较弱，可能影响复杂任务的表现

2. **使用量化模型**
   - 实施方式：使用GPTQ或AWQ量化版本的DeepSeek-R1
   - 实例类型：ml.g5.12xlarge
   - 复杂度：中
   - 适用场景：需要平衡性能和成本的生产环境
   - 优点：降低GPU内存需求，保持较好的模型性能
   - 缺点：需要额外的量化配置，可能略微影响精度

3. **分阶段部署策略**
   - 实施方式：
     - 第一阶段：使用8B模型验证整体架构和CrewAI工作流
     - 第二阶段：申请GPU实例配额，部署70B模型
   - 复杂度：中
   - 适用场景：长期项目，需要逐步扩展的场景
   - 优点：降低初期风险和成本，验证技术可行性
   - 缺点：需要较长的实施周期

### 风险提示

- **实例可用性风险**：ml.p4d.24xlarge在中国区域可能不可用，需要提前确认实例类型和配额
- **成本风险**：大型GPU实例成本较高，建议设置预算告警和自动停止策略
- **网络访问风险**：从Hugging Face下载大型模型可能受网络限制，建议提前测试连接性
- **配额限制风险**：GPU实例配额可能不足，需要提前申请配额提升
- **模型性能风险**：使用较小模型或量化模型可能影响智能体的推理能力，需要充分测试
- **区域特定配置**：需要确保所有AWS服务调用使用正确的中国区域endpoint

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/amazon-sagemaker-generativeai/tree/main/agents-with-sagemaker/deepseek_crewai_based_agent
- **兼容性**: 代码结构完整，可在中国区使用，需要修改实例类型和区域配置
- **修改建议**: 
  1. 将所有region参数改为"cn-northwest-1"或"cn-north-1"
  2. 评估并修改instance_type为中国区域可用的类型
  3. 考虑使用较小的模型变体进行初步验证
  4. 添加VPC配置以提高安全性
  5. 配置适当的IAM角色和权限
  6. 实施成本控制措施（如自动停止策略）

### 实施检查清单

**部署前准备**：
- [ ] 确认Hugging Face账号和API token
- [ ] 检查SageMaker服务配额，特别是GPU实例配额
- [ ] 准备S3存储桶用于模型artifacts
- [ ] 配置IAM角色和权限
- [ ] 评估预算和成本控制策略

**代码修改**：
- [ ] 修改region配置为cn-northwest-1或cn-north-1
- [ ] 调整instance_type为可用的GPU实例类型
- [ ] 根据实例类型调整模型选择（如需要）
- [ ] 配置VPC和安全组（推荐）
- [ ] 添加endpoint自动停止逻辑

**部署验证**：
- [ ] 测试模型部署成功
- [ ] 验证CrewAI智能体工作流
- [ ] 测试研究和写作任务
- [ ] 监控成本和资源使用
- [ ] 验证清理脚本正常工作

**生产准备**：
- [ ] 实施监控和告警
- [ ] 配置日志记录
- [ ] 准备故障恢复方案
- [ ] 文档化部署流程
- [ ] 培训运维团队
