# AWS 中国区内容验证工具

这个项目提供了一个简单的工具，用于验证 AWS 全球区域的技术内容是否适用于 AWS 中国区。通过自动化分析和验证，帮助用户判断 AWS 全球区域的技术内容是否适合在中国区使用，并提供必要的适配建议。

## 项目背景

AWS 中国区与 AWS 全球区域在服务可用性、功能特性和配置要求等方面存在差异。将 AWS 全球区域的技术内容（如博客、文档、解决方案）适配到中国区通常需要大量的手动验证和修改工作。本项目旨在通过自动化工具简化这一过程，提高内容验证的效率和准确性。

## 工具说明

该工具可以一步完成内容分析、服务验证和适用性评估，直接提供内容适用性评估结果。

```bash
./aws-cn-tool.sh -u <博客URL> [-r <区域>] [-p <配置文件>]
```

参数说明：
- `-u, --url`：要验证的博客或文档 URL（必需）
- `-r, --region`：AWS 中国区域（默认：cn-northwest-1）
- `-p, --profile`：AWS CLI 配置文件（默认：cn）
- `-h, --help`：显示帮助信息

## 使用流程

1. **设置 AWS 中国区凭证**：
   ```bash
   aws configure --profile cn
   ```
   输入您的 AWS 中国区访问密钥、秘密密钥和区域（cn-north-1 或 cn-northwest-1）

2. **运行验证工具**：
   ```bash
   ./aws-cn-tool.sh -u https://aws.amazon.com/blogs/aws/some-article
   ```

3. **查看验证结果**：
   工具会自动完成以下步骤：
   - 将网页内容转换为 Markdown 格式
   - 分析内容中涉及的 AWS 服务
   - 验证这些服务在中国区的可用性
   - 评估内容的整体适用性
   - 生成详细的 JSON 报告

## 工作原理

该工具使用 Amazon Q CLI 结合自定义提示词来完成整个验证流程：

1. 首先使用 `convert_to_markdown` 工具将网页内容转换为 Markdown 格式
2. 然后使用自定义提示词分析内容中涉及的 AWS 服务
3. 对每个服务进行可用性验证：
   - 检查是否在不可用服务列表中
   - 使用 AWS CLI 验证服务在中国区的可用性
4. 计算整体适用性评分并生成报告

## 项目结构

```
.
├── aws-cn-tool.sh           # 主脚本
├── bin/                     # 工具脚本目录
│   └── aws-cn-common-utils.sh  # 通用工具函数
├── data/                    # 数据目录（存放生成的文件）
├── china-content-validation.txt  # 验证提示词模板
└── unavailable_services.txt      # 中国区不可用服务列表
```

## 依赖项

- Amazon Q CLI (`q`)
- AWS CLI (`aws`)
- jq（可选，用于 JSON 处理）
- Bash 4.0+

## 示例

### 验证 EKS 博客文章

```bash
# 设置 AWS 中国区凭证
aws configure --profile cn

# 验证 EKS 博客
./aws-cn-tool.sh -u https://aws.amazon.com/blogs/containers/ensuring-fair-bandwidth-allocation-for-amazon-eks-workloads/
```

输出示例：
```
[INFO] Step 1: Converting blog content to Markdown...
[SUCCESS] Blog content has been converted to Markdown format
[INFO] Step 2: Analyzing content and validating service availability...
[INFO] Analyzing content and validating service availability, this may take a few minutes...
[SUCCESS] Analysis complete! Results saved to: ./data/ensuring-fair-bandwidth-allocation-for-amazon-eks-workloads_result.json

===== Analysis Result Summary =====
Applicability Rating: high
Reason: All core services are available in China regions, no major modifications required

[INFO] Complete results saved to: ./data/ensuring-fair-bandwidth-allocation-for-amazon-eks-workloads_result.json
```
