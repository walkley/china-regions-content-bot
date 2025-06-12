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
pip install -r requirements.txt
```

### AWS中国区域凭证设置

```bash
aws configure --profile cn
```

设置AWS访问密钥、秘密密钥和区域（cn-north-1或cn-northwest-1）

## 使用方法

### 基本用法

```bash
# 仅基本验证
python main.py -u <blog-url> -r <region> -p <profile>

# 使用深度验证
python main.py -u <blog-url> -d -m <max-cost>

# 强制重新生成缓存文件
python main.py -u <blog-url> -f
```

### 参数

- `-u, --url`: 博客URL（必需）
- `-r, --region`: AWS中国区域（默认：cn-northwest-1）
- `-p, --profile`: AWS CLI配置文件（默认：cn）
- `-d, --deep`: 启用深度验证模式
- `-m, --max-cost`: 深度验证的最大成本限制（美元，默认：10）
- `-f, --force`: 强制重新生成缓存文件
- `-t, --content-type`: 深度验证的内容类型（如果未指定则自动检测）
- `--temp-dir`: 临时文件目录（默认：./data/temp）
- `--log-level`: 日志级别（默认：INFO）
- `--check-dependencies`: 检查所需依赖项并退出
- `--cleanup-only`: 仅执行验证资源清理并退出

## 环境变量

该工具可以通过`.env`文件中的环境变量进行配置：

- `AWS_VALIDATOR_URL`: 要验证的内容URL
- `AWS_VALIDATOR_REGION`: AWS中国区域（默认：cn-northwest-1）
- `AWS_VALIDATOR_PROFILE`: AWS CLI配置文件（默认：cn）
- `AWS_VALIDATOR_DEEP_MODE`: 启用深度验证模式（true/false）
- `AWS_VALIDATOR_MAX_COST`: 深度验证的最大成本限制（美元）
- `AWS_VALIDATOR_FORCE_REGENERATE`: 强制重新生成缓存文件（true/false）
- `AWS_VALIDATOR_CONTENT_TYPE`: 深度验证的内容类型（project/tutorial）
- `AWS_VALIDATOR_TEMP_DIR`: 临时文件目录
- `AWS_VALIDATOR_LOG_LEVEL`: 日志级别（DEBUG/INFO/WARNING/ERROR/CRITICAL）

参见`.env.example`获取模板。

## 项目结构

```
.
├── main.py                  # 主入口脚本
├── requirements.txt         # Python依赖
├── .env.example             # 环境变量示例
├── data/                    # 生成的数据目录
│   ├── unavailable_services.txt # 中国区域不可用服务列表
│   └── temp/                # 临时文件目录
```

## 缓存机制

该工具实现了文件缓存机制以提高性能：

- 转换后的Markdown文件缓存在`./data/`目录中
- 基本验证结果缓存为JSON文件
- 使用`-f`标志强制重新生成缓存文件