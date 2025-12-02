# 技术架构文档

本文档详细说明 AWS 中国区内容兼容性验证工具的技术实现细节。

## 系统架构

本工具采用 **模块化 + AI Agent 驱动** 的混合架构。

### 架构层次

```
┌──────────────────────────────────────────────────────────┐
│               CLI 层 (run.py)                            │
│  • 统一命令入口                                           │
│  • 参数解析和路由                                         │
│  • 错误处理和退出码                                       │
└────────────────────┬─────────────────────────────────────┘
                     │
┌────────────────────▼─────────────────────────────────────┐
│            Python 模块层 (scripts/)                      │
│  • validate.py        - 核心验证流程编排                  │
│  • batch_validate.py  - 批量任务管理                     │
│  • content_convert.py - HTTP → Markdown 转换             │
│  • aws_blog_fetcher.py- AWS API 集成                     │
│  • generate_reports_json.py - 报告聚合                   │
│  • utils.py           - 共享工具函数                     │
└────────────────────┬─────────────────────────────────────┘
                     │
┌────────────────────▼─────────────────────────────────────┐
│       AI Agent 层 (Amazon Q Developer CLI)               │
│  • china-validator Agent                                │
│  • 基于 Claude Sonnet 4.5                               │
│  • 静态提示词 (china-validator-prompt.md)               │
│  • 动态上下文注入 (inject-validation-context.sh)        │
└────────────────────┬─────────────────────────────────────┘
                     │
┌────────────────────▼─────────────────────────────────────┐
│              外部依赖                                     │
│  • AWS CLI           - 中国区资源访问                     │
│  • requests          - HTTP 请求                         │
│  • BeautifulSoup     - HTML 解析                         │
│  • markdownify       - Markdown 转换                     │
└──────────────────────────────────────────────────────────┘
```

## 核心设计理念

### 1. 关注点分离

- **Python 层**：负责 I/O、网络请求、文件操作、流程编排
- **AI Agent 层**：负责智能分析、服务识别、可行性评估、报告生成

这种分离使得：
- 可以独立优化 Python 代码的性能和错误处理
- 可以单独迭代 AI Agent 的提示词和分析逻辑
- 系统各部分职责清晰，易于维护和测试

### 2. 可扩展性

- **模块化设计**：每个 Python 模块专注于单一职责
- **提示词驱动**：Agent 行为由提示词文件定义，无需修改代码
- **Hook 机制**：支持在 Agent 生命周期的关键节点注入动态上下文

### 3. 可维护性

- **统一日志系统**：所有模块使用相同的日志配置
- **标准化错误处理**：一致的异常处理和错误报告
- **规范化报告格式**：结构化的输出便于后续处理

## 详细工作流程

### 单次验证完整流程

```
┌─────────────────────────────────────────────────────────────┐
│  1. 📥 内容获取 (content_convert.py)                        │
│     • 从 URL 抓取博客内容                                    │
│     • 使用 BeautifulSoup 解析 HTML                          │
│     • 使用 markdownify 转换为 Markdown                      │
│     • 保存为 source.md                                      │
└─────────────────┬───────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────┐
│  2. 🤖 启动 AI Agent (validate.py)                          │
│     • 调用 Amazon Q Developer CLI (kiro-cli)                │
│     • 加载 china-validator Agent 配置                       │
│     • 注入动态验证上下文（Hook）                             │
│     • 使用 Claude Sonnet 4.5 模型                           │
└─────────────────┬───────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────┐
│  3. 🔍 智能服务识别 (AI Agent)                              │
│     • 分析博客内容中提到的所有 AWS 服务                      │
│     • 识别使用的具体功能和特性                               │
│     • 检测架构模式和部署方式                                 │
│     • 解析代码示例中的服务调用                               │
└─────────────────┬───────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────┐
│  4. 🌏 中国区兼容性分析 (AI Agent)                          │
│     • 对照 unavailable_services.txt 清单                    │
│     • 评估每个服务在中国区的可用性                           │
│     • 分析服务依赖关系和替代方案                             │
│     • 计算整体可行性等级                                     │
└─────────────────┬───────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────┐
│  5. 📊 可行性分级评估 (AI Agent)                            │
│     • HIGH: 完全可行，无需修改或仅需微调                     │
│     • MODERATE: 基本可行，需要部分调整                       │
│     • LOW: 困难，需要大量替换或重构                          │
│     • NOT_APPLICABLE: 不适用（公告、理论等非技术内容）       │
└─────────────────┬───────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────┐
│  6. 📝 生成验证报告 (AI Agent)                              │
│     • 服务清单（可用/不可用）                                │
│     • 可行性评估结果                                         │
│     • 实施建议和替代方案                                     │
│     • 潜在问题和注意事项                                     │
│     • 保存为 report.md                                      │
└─────────────────┬───────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────┐
│  7. 📦 更新报告索引 (generate-reports)                      │
│     • 扫描所有报告目录                                       │
│     • 提取元数据和统计信息                                   │
│     • 生成 reports.json                                     │
│     • 用于 Web 页面展示                                     │
└─────────────────────────────────────────────────────────────┘
```

### 批量验证流程

批量验证使用以下策略：

1. **串行处理**：按顺序处理每篇博客，避免资源竞争
2. **错误隔离**：单个博客失败不影响其他博客（使用 `--continue-on-error`）
3. **跳过已完成**：自动检测已有报告（使用 `--skip-existing`）
4. **进度追踪**：实时显示处理进度和成功/失败统计

## Agent 配置详解

### china-validator.json 配置

```json
{
  "name": "china-validator",
  "description": "AWS中国区域兼容性验证专家",
  "prompt": "file://./china-validator-prompt.md",
  "tools": ["*"],
  "toolsSettings": {
    "fs_write": {
      "allowedPaths": ["./docs/reports/**"]
    }
  },
  "hooks": {
    "agentSpawn": [
      {
        "command": "./.kiro/agents/inject-validation-context.sh"
      }
    ]
  },
  "model": "claude-sonnet-4.5"
}
```

**配置说明**：

- `name`: Agent 标识符，用于调用时指定
- `description`: Agent 的简短描述
- `prompt`: 提示词文件路径，定义 Agent 的行为逻辑
- `tools`: 允许 Agent 使用的工具集，`["*"]` 表示所有工具
- `toolsSettings.fs_write`: 限制文件写入权限，仅允许写入报告目录
- `hooks.agentSpawn`: Agent 启动时执行的 Hook 脚本
- `model`: 使用的 LLM 模型

### Hook 机制

`inject-validation-context.sh` 脚本在 Agent 启动时执行，负责：

1. 读取 `unavailable_services.txt` 文件
2. 读取博客的 `source.md` 内容
3. 读取环境变量（AWS region、profile 等）
4. 将这些上下文信息注入到 Agent 的提示词中

这种动态注入机制使得：
- 提示词文件保持静态和可维护
- 每次验证使用最新的服务清单
- 支持不同的配置参数

## 核心模块说明

### validate.py

**职责**：单个 URL 的验证流程编排

**主要功能**：
- 接收 URL 和配置参数
- 调用 content_convert 获取 Markdown
- 准备 Agent 执行环境
- 调用 kiro-cli 执行 Agent
- 处理 Agent 输出和错误
- 返回验证结果

### batch_validate.py

**职责**：批量验证任务管理

**主要功能**：
- 从 JSON 文件或标准输入读取博客列表
- 检查已有报告（skip-existing）
- 串行执行验证任务
- 错误处理和继续执行（continue-on-error）
- 统计和报告生成

### content_convert.py

**职责**：将 Web 内容转换为 Markdown

**主要功能**：
- HTTP 请求获取网页内容
- HTML 解析和清理
- 转换为 Markdown 格式
- 保留代码块和链接
- 移除无关元素（导航、广告等）

### aws_blog_fetcher.py

**职责**：从 AWS 官方 API 获取博客列表

**主要功能**：
- 调用 AWS 博客 API
- 支持分类和类型筛选
- 分页处理获取指定数量
- 格式化为标准 JSON 输出

### generate_reports_json.py

**职责**：生成报告索引文件

**主要功能**：
- 递归扫描 docs/reports/ 目录
- 解析每个报告的元数据
- 统计可行性等级分布
- 生成结构化的 reports.json
- 供 Web 页面展示使用

### utils.py

**职责**：共享工具函数库

**主要功能**：
- 日志系统配置
- 文件路径处理
- 目录创建和清理
- 时间戳生成
- 通用验证函数

## 报告格式规范

### report.md 结构

```markdown
# AWS 中国区兼容性验证报告

## 验证概览
- 博客标题：...
- 原始链接：...
- 验证时间：...
- 目标区域：...
- 可行性等级：...

## 服务兼容性分析

### 中国区可用服务 (X 个)
- Service 1
- Service 2
...

### 中国区不可用服务 (X 个)
- Service A
- Service B
...

## 可行性评估

[详细的可行性分析]

## 实施建议

[具体的实施步骤和建议]

## 风险与限制

[潜在问题和注意事项]
```

### reports.json 结构

```json
{
  "generated_at": "2025-11-26T10:30:30.123319Z",
  "statistics": {
    "total": 100,
    "high": 45,
    "moderate": 20,
    "low": 25,
    "not_applicable": 10
  },
  "reports": [
    {
      "title": "博客标题",
      "publish_date": "2025-11-25",
      "url": "reports/[blog_title]/[timestamp]/",
      "original_url": "https://aws.amazon.com/blogs/...",
      "validation_date": "2025-11-26",
      "target_region": "cn-northwest-1",
      "feasibility": "HIGH",
      "available_services": 15,
      "unavailable_services": 2
    }
  ]
}
```

## 扩展和定制

### 修改验证逻辑

编辑 `.kiro/agents/china-validator-prompt.md` 文件：

```markdown
# 修改可行性评估标准
将 HIGH 的阈值从 90% 调整为 95%

# 添加新的验证维度
在报告中增加成本估算章节

# 调整输出格式
修改报告的 Markdown 结构
```

### 添加新的服务清单

更新 `unavailable_services.txt`：

```bash
# 添加新的不可用服务
echo "New Service Name" >> unavailable_services.txt

# 移除已可用的服务
sed -i '/Service Name/d' unavailable_services.txt
```

### 扩展批量处理

在 `batch_validate.py` 中添加：

```python
# 并行处理支持
from concurrent.futures import ThreadPoolExecutor

# 自定义过滤逻辑
def should_validate(blog):
    # 自定义过滤条件
    return True
```

## 性能优化建议

1. **缓存机制**：为 content_convert 添加 HTTP 缓存
2. **并行处理**：批量验证时使用线程池
3. **增量更新**：仅处理新增或更新的博客
4. **报告压缩**：对历史报告进行压缩存储

## 安全考虑

1. **凭证管理**：使用 AWS CLI 配置文件，避免硬编码
2. **文件权限**：限制 Agent 的写入路径
3. **输入验证**：验证 URL 格式和来源
4. **错误信息**：避免在日志中泄露敏感信息

## 故障排查

### Agent 启动失败

检查项：
- Kiro CLI 是否正确安装
- Agent 配置文件路径是否正确
- 提示词文件是否存在
- Hook 脚本是否有执行权限

### 内容获取失败

检查项：
- 网络连接是否正常
- URL 是否可访问
- 是否需要代理设置
- 超时设置是否合理

### 报告生成失败

检查项：
- docs/reports/ 目录权限
- Agent 工具权限配置
- 磁盘空间是否充足

### 批量验证中断

检查项：
- 使用 `--continue-on-error` 参数
- 检查 validation.log 了解具体错误
- 使用 `--skip-existing` 避免重复处理
