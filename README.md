# AWS China Region Content Validation Tool

这个工具用于验证AWS全球区域技术内容在中国区域的兼容性。它分析内容以确定服务、功能和架构是否可以在AWS中国区域（cn-north-1、cn-northwest-1）实现。

## 核心功能

- **基本验证**：分析内容中AWS服务在中国区域的兼容性
- **深度验证**：对可行内容执行实际部署/执行验证
- **智能可行性门控**：防止在不可行内容上浪费资源
- **内容类型检测**：自动识别项目与教程内容
- **AI驱动分析**：使用Amazon Q Developer CLI custom agent进行智能验证

## 安装

### 前提条件

- `markitdown` - URL内容转换工具
- `kiro-cli` (Amazon Q Developer CLI) - AI agent运行环境
- AWS CLI - AWS操作
- AWS中国区域凭证

### 安装依赖

```bash
# 安装 markitdown (推荐使用 pipx)
pipx install markitdown
# 或使用 pip
pip install markitdown

# 安装 kiro-cli (Amazon Q Developer CLI)
# 参考: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-getting-started-installing.html

# 安装 AWS CLI
# 参考: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```

> **注意**: `pipx` 是安装命令行工具的推荐方式，它会为每个工具创建独立的虚拟环境。如果你还没有安装 `pipx`，可以通过 `pip install pipx` 或 `brew install pipx` (macOS) 安装。

### AWS中国区域凭证设置

```bash
aws configure --profile cn
```

设置AWS访问密钥、秘密密钥和区域（cn-north-1或cn-northwest-1）

## 使用方法

### 基本用法

```bash
# 验证内容
./validate.sh -u <content-url> -r <region> -p <profile>
```

### 参数

- `-u, --url`: 内容URL（必需）
- `-r, --region`: AWS中国区域（默认：cn-northwest-1）
- `-p, --profile`: AWS CLI配置文件（默认：cn）
- `--log-level`: 日志级别（默认：INFO）
- `-h, --help`: 显示帮助信息

### 示例

```bash
# 验证AWS博客文章
./validate.sh -u "https://aws.amazon.com/blogs/big-data/introducing-managed-query-results-for-amazon-athena/"

# 指定区域和配置文件
./validate.sh -u "https://aws.amazon.com/blogs/..." -r cn-north-1 -p my-cn-profile
```

## 项目结构

```
.
├── validate.sh                           # 主入口脚本
├── .kiro/agents/                         # Kiro CLI agent配置
│   ├── china-validator.json             # Agent配置文件
│   ├── china-validator-prompt.md        # Agent提示词
│   └── inject-validation-context.sh     # 上下文注入hook
├── unavailable_services.txt              # 中国区域不可用服务列表
├── README.md                             # 项目说明文档
└── data/                                 # 生成的验证结果目录
```

## 工作流程

1. **内容获取**：使用 `markitdown` 将URL内容转换为Markdown格式
2. **AI验证**：调用 `china-validator` custom agent进行智能分析
3. **基础验证**：
   - 识别内容中使用的AWS服务
   - 对比中国区域服务可用性
   - 评估初步可行性（HIGH/MODERATE/LOW）
4. **深度验证**（条件触发）：
   - 对于HIGH/MODERATE等级的内容
   - 实际部署GitHub项目或执行教程步骤
   - 在AWS中国区域真实环境中测试
   - 智能修正和重试机制（最多3次）
5. **报告生成**：生成详细的中文兼容性验证报告
6. **资源清理**：自动清理所有测试资源

## 验证报告

验证报告包含以下内容：

### 📋 验证概览
- 内容标题、验证时间、目标区域、验证ID

### 🔍 基础验证结果
- 可行性评估等级（🟢 HIGH / 🟡 MODERATE / 🔴 LOW）
- 识别的AWS服务列表
- 可用/不可用服务统计
- 评估说明

### 🚀 深入验证结果（条件触发）
- 验证类型（GitHub项目部署 / 教程步骤验证）
- 执行状态（✅ 成功 / ⚠️ 部分成功 / ❌ 失败）
- 遇到的问题和解决方案
- 修正尝试记录

### 📊 最终结论
- 综合可行性评估
- 推荐实施方案
- 风险提示和注意事项

## 输出文件

每次验证会生成唯一的验证ID（8位UUID），所有文件存储在 `./data/` 目录：

- `{文件名}_{validation_id}.md` - 转换后的Markdown内容
- `{文件名}_result_{validation_id}.md` - 验证结果报告
- `{文件名}_{validation_id}.log` - 完整的验证过程日志

## 技术架构

本工具采用 **AI Agent驱动架构**：

- **Shell脚本入口**：命令行接口
- **Markitdown**：内容提取和转换工具
- **Kiro CLI Custom Agent**：智能验证引擎
  - 静态提示词定义验证流程
  - Hook机制注入动态上下文
  - 自主决策和执行能力
  - 智能错误处理和重试

## 注意事项

1. **资源清理**：深入验证会在AWS中创建实际资源，工具会自动清理，但建议验证后检查
2. **成本控制**：深入验证可能产生AWS费用，建议在测试账户中运行
3. **凭证安全**：确保AWS凭证安全，不要在公共环境中运行
4. **网络访问**：需要访问AWS中国区域和目标URL