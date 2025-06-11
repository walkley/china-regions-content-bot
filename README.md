# AWS 中国区内容验证工具

这个项目提供了一个强大的工具，用于验证 AWS 全球区域的技术内容是否适用于 AWS 中国区。通过分层自动化分析和验证，帮助用户判断 AWS 全球区域的技术内容是否适合在中国区使用，并提供必要的适配建议和实际验证。

## 项目背景

AWS 中国区与 AWS 全球区域在服务可用性、功能特性和配置要求等方面存在差异。将 AWS 全球区域的技术内容（如博客、文档、解决方案）适配到中国区通常需要大量的手动验证和修改工作。本项目旨在通过自动化工具简化这一过程，提高内容验证的效率和准确性。

## 工具说明

该工具采用分层验证策略，提供两种验证模式：

1. **基本验证 (Basic Validation)**：快速分析内容中涉及的 AWS 服务，验证其在中国区的可用性，并给出整体适用性评估。
2. **深度验证 (Deep Validation)**：对于可行性较高的内容，进行实际部署或执行验证，提供详细的适配方案。

```bash
./main.sh -u <博客URL> [-r <区域>] [-p <配置文件>] [-d] [-m <最大成本>]
```

参数说明：
- `-u, --url`：要验证的博客或文档 URL（必需）
- `-r, --region`：AWS 中国区域（默认：cn-northwest-1）
- `-p, --profile`：AWS CLI 配置文件（默认：cn）
- `-d, --deep`：启用深度验证模式
- `-m, --max-cost`：深度验证的最大成本限制（单位：美元，默认：10）
- `-f, --force`：强制重新生成 Markdown 文件（即使已存在）
- `-h, --help`：显示帮助信息

## 使用流程

1. **设置 AWS 中国区凭证**：
   ```bash
   aws configure --profile cn
   ```
   输入您的 AWS 中国区访问密钥、秘密密钥和区域（cn-north-1 或 cn-northwest-1）

2. **运行基本验证**：
   ```bash
   ./main.sh -u https://aws.amazon.com/blogs/aws/some-article
   ```

3. **运行深度验证**（对于可行性较高的内容）：
   ```bash
   ./main.sh -u https://aws.amazon.com/blogs/aws/some-article -d
   ```

4. **查看验证结果**：
   工具会自动完成以下步骤：
   - 将网页内容转换为 Markdown 格式（如果文件不存在）
   - 分析内容中涉及的 AWS 服务
   - 验证这些服务在中国区的可用性
   - 评估内容的整体适用性
   - （深度验证模式）执行实际部署或步骤验证
   - 生成详细的 JSON 报告

5. **文件缓存机制**：
   - 默认情况下，工具会检查以下文件是否已存在：
     - 转换的 Markdown 文件
     - 基本验证结果文件
   - 如果文件已存在，会跳过相应的步骤，直接使用现有文件
   - 使用 `-f` 或 `--force` 参数可以强制重新生成所有缓存文件
   ```bash
   # 强制重新生成所有文件
   ./main.sh -u https://aws.amazon.com/blogs/aws/some-article -f
   ```
   - 这个缓存机制可以：
     - 加快重复验证的速度
     - 保留历史验证结果
     - 方便比较不同时间点的验证结果
     - 减少对外部服务的请求

## 验证模式

### 基本验证 (Basic Validation)
- **适用范围**：所有内容通用
- **验证内容**：
  - AWS服务清单提取
  - 实际API调用验证服务可用性
  - 整体可行性级别评估
- **输出级别**：
  - **HIGH**：核心服务全部可用，强烈推荐Deep验证
  - **MODERATE**：部分核心服务可用，可以进行Deep验证
  - **LOW**：核心服务大量缺失，不建议Deep验证

### 深度验证 (Deep Validation)
- **智能门控机制**：基于Basic验证结果的智能决策
  - **HIGH**：✅ 强烈推荐，自动允许Deep验证
  - **MODERATE**：⚠️ 推荐执行，可能需要适配方案
  - **LOW**：❌ 智能阻止，防止资源浪费
- **阻止策略**：LOW级别时强制阻止Deep验证，即使用户明确要求
- **设计理念**：让AI基于技术分析做出权威判断，避免无意义的资源消耗
- **验证类型**：
  - **Project类型**：GitHub项目实际部署验证
  - **Tutorial类型**：操作步骤实际执行验证

## 工作原理

该工具使用模块化设计，分为多个独立的组件：

1. **内容转换器 (src/content-converter.sh)**：
   - 使用 `convert_to_markdown` 工具将网页内容转换为 Markdown 格式
   - 清理非核心内容（导航栏、页脚等）

2. **基本验证器 (src/basic-validator.sh)**：
   - 分析内容中涉及的 AWS 服务
   - 检查服务是否在不可用服务列表中
   - 使用 AWS CLI 验证服务在中国区的可用性
   - 计算整体适用性评分并生成报告

3. **深度验证器 (src/deep-validator.sh)**：
   - 确定内容类型（项目或教程）
   - 检查可行性级别
   - 调用相应的验证器

4. **项目验证器 (src/project-validator.sh)**：
   - 分析 GitHub 项目
   - 验证项目在中国区的可部署性
   - 生成项目验证报告

5. **教程验证器 (src/tutorial-validator.sh)**：
   - 分析教程步骤
   - 验证步骤在中国区的可执行性
   - 生成教程验证报告

## 项目结构

```
.
├── main.sh                  # 主脚本
├── src/                     # 源代码目录
│   ├── content-converter.sh # 内容转换模块
│   ├── basic-validator.sh   # 基本验证模块
│   ├── deep-validator.sh    # 深度验证协调模块
│   ├── project-validator.sh # 项目验证模块
│   ├── tutorial-validator.sh # 教程验证模块
│   ├── common-utils.sh      # 通用工具函数
│   └── unavailable_services.txt # 中国区不可用服务列表
└── data/                    # 数据目录（存放生成的文件）
```

## 依赖项

- Amazon Q CLI (`q`)
- AWS CLI (`aws`)
- jq（可选，用于 JSON 处理）
- Bash 4.0+

## 示例

### 验证 EKS 博客文章（基本验证）

```bash
# 设置 AWS 中国区凭证
aws configure --profile cn

# 验证 EKS 博客
./main.sh -u https://aws.amazon.com/blogs/containers/ensuring-fair-bandwidth-allocation-for-amazon-eks-workloads/
```

输出示例：
```
[INFO] Converting blog content to Markdown...
[SUCCESS] Blog content has been converted to Markdown format
[INFO] Analyzing content and validating service availability...
[INFO] Analyzing content and validating service availability, this may take a few minutes...
[SUCCESS] Basic validation complete! Results saved to: ./data/ensuring-fair-bandwidth-allocation-for-amazon-eks-workloads_result.json

===== Analysis Result Summary =====
Applicability Rating: high
Reason: All core services are available in China regions, no major modifications required

[INFO] Deep validation not requested. Use -d flag to enable deep validation.
```

### 验证 Lambda 博客文章（深度验证）

```bash
# 验证 Lambda 博客（带深度验证）
./main.sh -u https://aws.amazon.com/blogs/compute/building-serverless-applications-with-aws-lambda/ -d
```

输出示例：
```
[INFO] Converting blog content to Markdown...
[SUCCESS] Blog content has been converted to Markdown format
[INFO] Analyzing content and validating service availability...
[INFO] Analyzing content and validating service availability, this may take a few minutes...
[SUCCESS] Basic validation complete! Results saved to: ./data/building-serverless-applications-with-aws-lambda_result.json

===== Analysis Result Summary =====
Applicability Rating: high
Reason: All core services are available in China regions, no major modifications required

[INFO] Content type detected: Tutorial (Step-by-step procedures found)
[INFO] Starting deep validation (type: tutorial)...
[INFO] Analyzing and validating tutorial steps, this may take some time...
[SUCCESS] Deep validation complete! Results saved to: ./data/building-serverless-applications-with-aws-lambda_deep_result.json

===== Deep Validation Result Summary =====
Validation Type: tutorial_execution
Execution Time: 12:45
Confidence: 0.92
Executable Steps: 8/10 (80%)

[INFO] Complete deep validation results saved to: ./data/building-serverless-applications-with-aws-lambda_deep_result.json
```
