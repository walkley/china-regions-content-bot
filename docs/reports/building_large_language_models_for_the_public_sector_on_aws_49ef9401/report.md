---
title: 在AWS上为公共部门构建大型语言模型
publish_date: 2025-10-27
original_url: https://aws.amazon.com/blogs/publicsector/building-large-language-models-for-the-public-sector-on-aws/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 13
unavailable_services: 1
---

# 在AWS上为公共部门构建大型语言模型

[📖 查看原始博客](https://aws.amazon.com/blogs/publicsector/building-large-language-models-for-the-public-sector-on-aws/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文提供的LLM开发方法论和最佳实践完全适用于AWS中国区域。所有核心基础设施服务（计算、存储、网络、机器学习）均可用，唯一不可用的Amazon Bedrock仅作为可选托管服务提及，文章已提供多种替代部署方案。

## 服务分析

### 可用服务 (13个)

- Amazon EC2
- Amazon SageMaker
- Amazon SageMaker HyperPod
- Amazon SageMaker AI
- Amazon SageMaker Training Plans
- Amazon S3
- Amazon FSx for Lustre
- Amazon EKS
- AWS Parallel Computing Service (AWS PCS)
- Elastic Fabric Adapter (EFA)
- AWS IAM
- AWS KMS
- AWS CloudTrail
- Amazon VPC

### 不可用服务 (1个)

- **Amazon Bedrock** - 作为托管模型部署选项之一提及，非核心必需

### 评估说明

本文是一篇关于公共部门LLM开发的综合性方法论指南，涵盖从需求定义到生产部署的完整生命周期。文章的核心价值在于：

1. **核心服务完全可用**：所有用于LLM训练和部署的基础设施服务（EC2、SageMaker、S3、EKS等）在中国区域均可用
2. **架构灵活性**：文章提供了多种部署选项（EC2、SageMaker、EKS），不依赖单一服务
3. **方法论通用性**：六阶段开发流程、数据处理策略、评估框架等内容与具体云区域无关
4. **替代方案明确**：对于Amazon Bedrock，文章明确指出可使用自托管方案（EC2/EKS/SageMaker）满足数据主权要求

唯一不可用的Amazon Bedrock在文章中仅作为三种部署选项之一，且文章特别强调对于有严格数据主权要求的公共部门，自托管开源模型是更优选择。

## 验证结果

### 验证类型

- ⏭️ 已跳过深入验证

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 本文是LLM开发方法论和最佳实践指南，不包含需要部署验证的配套代码仓库或具体操作命令。文章内容为概念性和架构性指导，所有核心服务在中国区域可用，无需实际部署验证。

## 实施建议

### 推荐方案

本文可作为在AWS中国区域开发定制LLM的权威指南直接使用。建议实施路径：

**1. 基础设施选择**
- 优先使用Amazon SageMaker HyperPod进行大规模训练，提供自动故障检测和节点替换
- 使用Amazon EC2 with Capacity Blocks获得更大灵活性和成本控制
- 通过AWS PCS使用SLURM调度器，适合有HPC背景的团队

**2. 数据主权合规**
- 采用文章推荐的自托管方案（EC2/EKS/SageMaker），确保数据不出境
- 使用客户管理的KMS密钥加密
- 配置VPC私有子网和VPC端点
- 所有训练和推理固定在cn-northwest-1或cn-north-1区域

**3. 网络和存储优化**
- 启用EFA（Elastic Fabric Adapter）实现低延迟GPU间通信
- 使用Amazon S3存储训练数据，Amazon FSx for Lustre作为高性能文件系统
- 配置S3与FSx for Lustre的数据仓库关联实现高效数据访问

**4. 开发流程实施**
- 按照文章的六阶段流程：需求定义 → 评估框架 → 模型选择 → 数据准备 → 训练 → 部署
- 使用LM Harness建立评估基准
- 采用NeMo Curator进行数据清洗和去重
- 实施文章建议的PII检测和数据主权控制

**注意事项：**
- 跳过Amazon Bedrock相关内容，专注于自托管部署方案
- 确保所有第三方工具（LM Harness、vLLM、NeMo Curator）可从GitHub或PyPI获取
- 考虑网络访问限制，可能需要配置镜像源或离线安装包

### 替代方案

文章已充分考虑不同场景的替代方案：

1. **训练基础设施**
   - 实施方式：根据团队技能选择SageMaker HyperPod（托管）、AWS PCS（SLURM）或EKS（Kubernetes）
   - 复杂度：SageMaker HyperPod（低）、AWS PCS（中）、EKS（高）
   - 适用场景：SageMaker适合快速启动，AWS PCS适合HPC团队，EKS适合容器化团队

2. **模型部署**
   - 实施方式：SageMaker AI（托管推理）、EC2（完全控制）、EKS（容器化）
   - 复杂度：SageMaker AI（低）、EC2（中）、EKS（中-高）
   - 适用场景：根据运维能力和定制需求选择

3. **数据处理**
   - 实施方式：使用开源NeMo Curator替代任何专有数据处理服务
   - 复杂度：中
   - 适用场景：所有LLM数据准备场景

### 风险提示

- **网络访问限制**：部分开源工具和模型权重托管在GitHub和Hugging Face，可能需要配置代理或使用国内镜像
- **GPU资源可用性**：P4d、P5等高端GPU实例在中国区域可能需要提前申请配额
- **成本管理**：大规模LLM训练成本高昂，建议先进行小规模POC验证TCO模型
- **合规要求**：公共部门需确保满足《数据安全法》和《个人信息保护法》要求，文章提供的数据主权框架需结合具体法规实施
- **技术支持**：某些新服务（如AWS PCS）在中国区域的文档和支持可能相对有限

### 配套资源

本文引用的开源工具和资源：

- **LM Harness**: https://github.com/EleutherAI/lm-evaluation-harness - 模型评估框架
- **vLLM**: https://github.com/vllm-project/vllm - 高性能推理引擎
- **NVIDIA NeMo Curator**: https://github.com/NVIDIA/NeMo-Curator - 数据处理工具
- **GenAI-Perf**: NVIDIA Triton性能测试工具

**兼容性**: 所有工具均为开源项目，可在中国区域使用

**修改建议**: 
- 确保从可访问的源下载工具和依赖
- 模型权重下载可能需要配置Hugging Face镜像
- 考虑将常用工具和模型打包到私有S3存储桶
