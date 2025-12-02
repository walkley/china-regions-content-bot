# AWS 中国区内容兼容性验证工具

自动化验证 AWS 技术博客在中国区的兼容性，通过 AI 智能分析服务可用性并生成详细报告。

## ✨ 核心特性

- 🔍 **智能服务识别** - 自动识别所有 AWS 服务和功能
- 🌏 **兼容性分析** - 评估中国区实施可行性
- 📊 **四级评估** - HIGH/MODERATE/LOW/NOT_APPLICABLE
- 📝 **详细报告** - 包含服务清单和实施建议
- ⚙️ **批量处理** - 支持大规模自动化验证
- 🤖 **AI 驱动** - 基于 Amazon Q Developer CLI

## 快速开始

### 安装

```bash
# 1. 克隆项目
git clone <repository-url>
cd china-regions-content-bot-1

# 2. 安装依赖
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. 配置 AWS 中国区凭证
aws configure --profile cn
```

**前置要求**：
- Python 3.12+
- [Amazon Q Developer CLI](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-getting-started-installing.html)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

## 基本使用

### 验证单篇博客

```bash
python run.py validate -u "https://aws.amazon.com/blogs/..."
```

### 批量验证

```bash
# 获取博客列表
python run.py fetch-blogs -n 50 -o blogs.json

# 批量验证（跳过已验证的）
python run.py batch -i blogs.json --skip-existing --continue-on-error

# 生成报告索引
python run.py generate-reports
```

### 常用选项

```bash
# 指定区域和配置
python run.py validate -u <url> -r cn-north-1 -p cn

# 开启调试日志
python run.py validate -u <url> --log-level DEBUG

# 限制验证数量
python run.py batch -i blogs.json --limit 10
```

查看完整帮助：`python run.py <command> --help`

## 项目结构

```text
china-regions-content-bot-1/
├── run.py                           # 主入口程序
├── scripts/                         # Python 核心模块
│   ├── validate.py                  # 验证逻辑
│   ├── batch_validate.py            # 批量处理
│   ├── content_convert.py           # 内容转换
│   ├── aws_blog_fetcher.py          # 博客 API
│   └── generate_reports_json.py     # 报告生成
├── .kiro/agents/                    # AI Agent 配置
│   ├── china-validator.json         # Agent 配置
│   └── china-validator-prompt.md    # 提示词
├── unavailable_services.txt         # 不可用服务清单
└── docs/reports/                    # 验证报告输出
```

## 工作流程

1. **内容获取** - 从 URL 抓取并转换为 Markdown
2. **AI 分析** - 识别服务、评估兼容性
3. **生成报告** - 输出详细验证结果

详见 [技术架构文档](ARCHITECTURE.md)

## 验证报告

每次验证会在 `docs/reports/` 下生成：

- **source.md** - 原始博客 Markdown 版本
- **report.md** - 兼容性验证报告
- **validation.log** - 详细验证日志

### 报告内容

- 📋 验证概览（标题、时间、区域、可行性等级）
- 🔍 服务兼容性分析（可用/不可用服务清单）
- 📊 可行性评估（HIGH/MODERATE/LOW/NOT_APPLICABLE）
- 💡 实施建议（步骤、配置、替代方案）
- ⚠️ 风险与限制（潜在问题和注意事项）

## 常见问题

**Q: 验证一篇博客需要多长时间？**

A: 静态验证通常 30-60 秒，取决于博客长度和网络速度。但如需实际部署验证，可能需要 15-30 分钟。

**Q: 如何查看报告？**

A: 直接查看 `docs/reports/` 目录下的 Markdown 文件，或使用 GitHub Pages 托管 Web 界面。

**Q: 验证失败怎么办？**

A: 查看 `validation.log` 了解详细错误。常见问题：URL 不可访问、Kiro CLI 配置错误、目录权限问题。

**Q: 可以自定义验证逻辑吗？**

A: 可以，编辑 `.kiro/agents/china-validator-prompt.md` 文件调整 Agent 行为。

更多技术细节请参考 [技术架构文档](ARCHITECTURE.md)

## 贡献

欢迎贡献！主要方向：

- 改进 Agent 提示词
- 更新服务可用性清单
- 修复 Bug 和改进文档

## 许可证

MIT License

## 相关资源

- [Amazon Q Developer CLI](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line.html)
- [AWS 中国区域文档](https://docs.amazonaws.cn/)
- [技术架构文档](ARCHITECTURE.md)
