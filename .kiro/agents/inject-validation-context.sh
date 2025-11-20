#!/bin/bash
# Hook script to inject dynamic validation context

# Read hook event from stdin (required by hook protocol)
EVENT=$(cat)

# Extract variables from environment
VALIDATION_CONTENT_FILE="${VALIDATION_CONTENT_FILE:-}"
VALIDATION_RESULT_FILE="${VALIDATION_RESULT_FILE:-}"
VALIDATION_ID="${VALIDATION_ID:-}"
VALIDATION_AWS_REGION="${VALIDATION_AWS_REGION:-cn-northwest-1}"
VALIDATION_AWS_PROFILE="${VALIDATION_AWS_PROFILE:-cn}"
VALIDATION_TIME=$(date -u +"%Y-%m-%dT%H:%M:%S%z")

# Output dynamic context that supplements the static prompt
cat << EOF

## 当前验证任务上下文

- **待验证内容文件**：${VALIDATION_CONTENT_FILE}
- **验证结果输出文件**：${VALIDATION_RESULT_FILE}
- **验证ID**：${VALIDATION_ID}
- **目标AWS区域**：${VALIDATION_AWS_REGION}
- **AWS Profile**：${VALIDATION_AWS_PROFILE}
- **验证时间**：${VALIDATION_TIME}

请按照你的系统提示中定义的验证流程，对上述内容文件进行完整的兼容性验证分析，并将最终报告写入结果输出文件。

在深入验证阶段，请使用以下配置：
- AWS区域：${VALIDATION_AWS_REGION}
- AWS Profile：${VALIDATION_AWS_PROFILE}
- 资源标签：Key=ValidationTest, Value=${VALIDATION_ID}

EOF
