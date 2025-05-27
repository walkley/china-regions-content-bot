# AWS 中国区内容转换工具

这个项目提供了一套简单工具，用于验证并转换AWS海外区域的技术内容到AWS中国区。通过自动化分析和验证，帮助用户判断AWS全球区域的技术内容是否适用于中国区，并提供必要的转换建议。

## 项目背景

AWS中国区与AWS全球区域在服务可用性、功能特性和配置要求等方面存在差异。将AWS全球区域的技术内容（如博客、文档、解决方案）适配到中国区通常需要大量的手动验证和修改工作。本项目旨在通过自动化工具简化这一过程，提高内容转换的效率和准确性。

## 工具说明

### 1. 博客转换工具 (aws-cn-content-convert.sh)

将网页博客内容转换为Markdown格式，便于后续分析和处理。

```bash
./aws-cn-tool.sh convert -u <博客URL> -o <输出文件路径>
```

### 2. 内容分析工具 (aws-cn-content-analyze.sh)

分析Markdown内容，识别其中涉及的AWS服务、资源和配置。

```bash
./aws-cn-tool.sh analyze -f <Markdown文件> -o <输出JSON文件>
```

### 3. 服务验证工具 (aws-cn-service-validate.sh)

生成交互式脚本，验证识别出的AWS服务在中国区的可用性。

```bash
./aws-cn-tool.sh validate -i <服务JSON文件> -o <输出脚本文件> -r <区域> -p <配置文件>
```

### 4. 适用性检查工具 (aws-cn-content-evaluate.sh)

评估内容是否适用于AWS中国区，并生成详细报告。

```bash
./aws-cn-tool.sh evaluate -i <验证结果JSON> -o <适用性报告JSON> -t <阈值>
```

## 使用流程

1. **设置环境**：
   ```bash
   ./aws-cn-tool.sh setup
   ```

2. **转换博客内容**：
   ```bash
   ./aws-cn-tool.sh convert -u https://aws.amazon.com/blogs/aws/some-article -o ./data/aws-article.md
   ```

3. **分析内容中的AWS服务**：
   ```bash
   ./aws-cn-tool.sh analyze -f ./data/aws-article.md -o ./data/aws-article-services.json
   ```

4. **生成服务验证脚本**：
   ```bash
   ./aws-cn-tool.sh validate -i ./data/aws-article-services.json -o ./data/aws-article-validation.sh
   ```

5. **运行验证脚本并保存结果**：
   ```bash
   ./data/aws-article-validation.sh > ./data/aws-article-validation-results.json
   ```

6. **评估内容适用性**：
   ```bash
   ./aws-cn-tool.sh evaluate -i ./data/aws-article-validation-results.json -o ./data/aws-article-applicability.json
   ```

## 项目结构

```
.
├── aws-cn-tool.sh          # 主入口脚本
├── bin/                    # 可执行脚本目录
│   ├── aws-cn-common-utils.sh       # 通用工具函数
│   ├── aws-cn-content-convert.sh    # 博客转换脚本
│   ├── aws-cn-content-analyze.sh    # 内容分析脚本
│   ├── aws-cn-service-validate.sh   # 服务验证脚本
│   ├── aws-cn-content-evaluate.sh   # 适用性检查脚本
│   └── aws-cn-setup.sh              # 环境设置脚本
├── data/                   # 数据目录（存放所有生成的文件）
└── VERSION                 # 版本信息
```

## 依赖项

- Amazon Q CLI (`q`)
- AWS CLI (`aws`)
- jq (可选，用于JSON处理)
- Bash 4.0+

## 示例

### 验证EKS博客文章

```bash
# 设置环境
./aws-cn-tool.sh setup

# 转换EKS博客
./aws-cn-tool.sh convert -u https://aws.amazon.com/blogs/containers/ensuring-fair-bandwidth-allocation-for-amazon-eks-workloads/ -o ./data/eks-bandwidth.md

# 分析内容
./aws-cn-tool.sh analyze -f ./data/eks-bandwidth.md -o ./data/eks-services.json

# 生成验证脚本
./aws-cn-tool.sh validate -i ./data/eks-services.json -o ./data/eks-validation.sh

# 运行验证脚本
./data/eks-validation.sh > ./data/eks-validation-results.json

# 评估适用性
./aws-cn-tool.sh evaluate -i ./data/eks-validation-results.json -o ./data/eks-applicability.json
```
