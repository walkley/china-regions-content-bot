# AWS China Region Content Validation Tool

这个工具用于验证AWS全球区域技术内容在中国区域的兼容性。它分析内容以确定服务、功能和架构是否可以在AWS中国区域（cn-north-1、cn-northwest-1）实现。

## 核心功能

- **基本验证**：分析内容中AWS服务在中国区域的兼容性
- **深度验证**：对可行内容执行实际部署/执行验证
- **智能可行性门控**：防止在不可行内容上浪费资源
- **内容类型检测**：自动识别项目与教程内容

## 安装

### 前提条件

- Python 3.6+
- Amazon Q CLI (`q`)
- AWS CLI
- AWS中国区域凭证

### 设置

```bash
# 克隆仓库
git clone https://github.com/yourusername/aws-china-validator.git
cd aws-china-validator

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 安装依赖
pip install -e .
```

### AWS中国区域凭证设置

```bash
aws configure --profile cn
```

设置AWS访问密钥、秘密密钥和区域（cn-north-1或cn-northwest-1）

## 使用方法

### 基本用法

```bash
# 验证内容
python main.py -u <content-url> -r <region> -p <profile>
```

### 参数

- `-u, --url`: 内容URL（必需）
- `-r, --region`: AWS中国区域（默认：cn-northwest-1）
- `-p, --profile`: AWS CLI配置文件（默认：cn）
- `--log-level`: 日志级别（默认：INFO）

## 项目结构

```
.
├── main.py                  # 主入口脚本
├── converter.py            # URL内容转Markdown转换器
├── pyproject.toml          # 项目配置和依赖
├── README.md               # 项目说明文档
├── unavailable_services.txt # 中国区域不可用服务列表
├── data/                   # 生成的数据目录
└── temp/                   # 临时文件目录
```

## 工作流程

1. 将URL内容转换为Markdown格式
2. 分析内容中使用的AWS服务
3. 检查服务在中国区域的可用性
4. 生成验证报告
5. 对可行内容执行深度验证（如果启用）

## 验证报告

验证报告包含以下内容：

- 验证概览（内容标题、验证时间、目标区域、验证ID）
- 基础验证结果（可行性评估、服务分析）
- 深入验证结果（如果执行）
- 最终结论和建议

## 缓存机制

该工具实现了文件存储机制以保存验证过程和结果：

- 每次验证会生成唯一验证ID（validation_id），用于标识验证会话
- 所有生成的文件都存储在`./data/`目录中，包括：
  - 转换后的Markdown文件：`{文件名}_{validation_id}.md`
  - 验证结果报告：`{文件名}_result_{validation_id}.md`
  - 验证过程日志：`{文件名}_{validation_id}.log`
- 文件名基于URL生成，确保唯一性和可追溯性
- 这些文件可用于后续分析、审计和问题排查