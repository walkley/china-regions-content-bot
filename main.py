#!/usr/bin/env python3
"""
AWS China Region Content Validation Tool

This tool validates AWS global region technical content for compatibility with AWS China regions.
It analyzes content to determine if services, features, and architectures can be implemented
in AWS China regions (cn-north-1, cn-northwest-1).
"""

import argparse
import logging
import os
import subprocess
import sys
import uuid
from pathlib import Path
from datetime import datetime
from markdown_converter import convert_url_to_markdown

# Set up logging
def setup_logging(log_level="INFO"):
    """Set up basic logging configuration."""
    logging_level = getattr(logging, log_level.upper())
    logging.basicConfig(
        level=logging_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger("aws-validator")

# Parse command line arguments
def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="AWS China Region Content Validation Tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Required arguments
    parser.add_argument("-u", "--url", help="URL of the content to validate")
    
    # AWS configuration
    parser.add_argument("-r", "--region", default="cn-northwest-1", 
                      help="AWS China region to use for validation")
    parser.add_argument("-p", "--profile", default="cn", 
                      help="AWS CLI profile with China region credentials")
    parser.add_argument("--log-level", default="INFO",
                      help="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)")
    
    return parser.parse_args()

# Run Q chat command
def run_q_chat(prompt: str, trust_tools: str, model: str = "claude-4-sonnet", timeout=1800):
    """Run Amazon Q chat command and handle output in real-time."""
    cmd = ["q", "chat", f"--model={model}"]
    if trust_tools:
        cmd.append(f"--trust-tools={trust_tools}")
    
    try:
        process = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1  # Line buffered
        )
        
        # Send the prompt to stdin
        process.stdin.write(prompt)
        process.stdin.close()
        
        # Collect output
        full_output = ""
        
        # Read and print stdout in real-time
        for line in process.stdout:
            print(line, end="")  # Print in real-time
            sys.stdout.flush()   # Ensure output is flushed immediately
            full_output += line
        
        # Get any stderr output
        stderr = process.stderr.read()
        
        # Wait for process to complete
        process.wait()
        
        if process.returncode != 0:
            logging.error(f"Q chat command failed: {stderr}")
            return {"success": False, "error": stderr, "output": full_output}
        
        return {"success": True, "output": full_output}
    except subprocess.TimeoutExpired:
        process.kill()
        logging.error(f"Q chat command timed out after {timeout} seconds")
        return {"success": False, "error": f"Command timed out after {timeout} seconds"}
    except Exception as e:
        logging.error(f"Error running Q chat command: {e}")
        return {"success": False, "error": str(e)}

# Perform deep validation
def validate_content(content_file: str, result_file: str, validation_id: str, region: str, profile: str):
    """Perform deep validation based on content type."""

    prompt = f"""# AWS中国区域兼容性验证专家

你是AWS中国区域兼容性验证专家。你的任务是对AWS技术博客内容进行分层验证，评估其在AWS中国区域的可行性。

## 待验证的AWS技术博客Markdown文件路径
{content_file}

## 验证流程

### 第一阶段：基础验证（静态分析）

#### 1. 内容解析
- 仔细阅读技术内容，识别所有提到的AWS服务
- **检测是否包含配套的GitHub项目**：
  - ✅ 需要验证：文章专门配套的代码仓库、教程实现代码、专门介绍的项目
  - ❌ 无需验证：引用参考、举例说明、第三方项目链接
- 识别是否包含具体的操作步骤

#### 2. 服务可用性检查
- 将识别的服务与不可用服务列表文件"./unavailable_services.txt"中的内容对照
- 统计可用和不可用服务的数量和比例

#### 3. 初步可行性评估
- **HIGH**：所有服务都可用
- **MODERATE**：>70%服务可用，有替代方案
- **LOW**：<70%服务可用，需要重大修改

### 第二阶段：深入验证（条件触发）

#### 触发条件
仅当基础验证结果为MODERATE或HIGH时执行

#### 验证类型选择
- 如果内容包含**配套的GitHub项目** → 执行GitHub项目部署验证
- 如果内容包含操作步骤但无配套GitHub项目 → 执行教程步骤验证

#### GitHub项目部署验证流程
1. 克隆GitHub仓库到临时目录
2. 深入分析研究该项目的部署流程和要求，在AWS {region}区域使用profile {profile}真实部署该方案
3. **智能修正策略**：部署过程中如遇到部署问题，最多尝试3次修正，修正范围限定为：
   - ✅ 允许修正：endpoint URL调整、区域特定配置参数、网络配置优化
   - ❌ 禁止修正：替换不可用服务、修改核心架构、改变主要功能逻辑
   - 每次修正后重新尝试部署，记录修正内容和结果
4. 记录部署过程中遇到的问题和修正尝试
5. **重要**：验证完成前清理所有AWS资源

#### 教程步骤验证流程
1. 从内容中提取具体的操作步骤
2. 在{region}区域使用profile {profile}配置逐步执行
3. 为所有创建的资源添加标签：Key=ValidationTest, Value={validation_id}
4. **智能修正策略**：如遇到执行问题，最多尝试3次修正，修正范围限定为：
   - ✅ 允许修正：endpoint URL调整、区域特定配置参数、网络配置优化
   - ❌ 禁止修正：替换不可用服务、修改核心架构、改变主要功能逻辑
   - 每次修正后重新尝试执行，记录修正内容和结果
5. 记录每个步骤的执行结果和问题
6. **重要**：完整清理所有测试资源
   - 删除所有带ValidationTest标签的资源
   - **二次确认**：清理完成后再次检查，确保没有ValidationTest标签的资源残留
   - 如发现残留资源，记录详情并强制清理

## 输出要求

生成统一的中文可行性验证报告，使用Markdown格式：

```markdown
# AWS中国区域兼容性验证报告

## 📋 验证概览
- **内容标题**：[从blog post提取]
- **验证时间**：{datetime.now().astimezone().isoformat()}
- **目标区域**：{region}
- **验证ID**：{validation_id}

## 🔍 基础验证结果

### 可行性评估
**等级**：🟢 HIGH / 🟡 MODERATE / 🔴 LOW

### 服务分析
**识别的AWS服务**：
- 服务1
- 服务2
- ...

**✅ 可用服务 ([实际数量]个)**：
- 可用服务列表

**❌ 不可用服务 ([实际数量]个)**：
- 不可用服务列表

**📝 评估说明**：
[基于服务可用性的初步分析]

## 🚀 深入验证结果
> 仅当基础验证为MODERATE或HIGH时执行

### 验证类型
- [ ] GitHub项目部署验证
- [ ] 教程步骤验证

### 执行结果
**状态**：✅ 成功 / ⚠️ 部分成功 / ❌ 失败

### 遇到的问题
1. **问题描述**
   - 具体问题说明
   - 影响程度

### 适配建议
1. **替代方案**
   - 具体建议
   - 实施难度

## 📊 最终结论

### 综合可行性评估
**结论**：🟢 推荐实施 / 🟡 谨慎实施 / 🔴 不建议实施

### 推荐实施方案
[具体的实施建议和步骤]

### ⚠️ 风险提示
- 风险点1
- 风险点2
```

## 重要提醒

1. **资源清理**：深入验证过程中创建的所有AWS资源必须完全清理，避免产生不必要的费用
2. **标签管理**：使用ValidationTest标签便于跟踪和清理测试资源
3. **错误处理**：详细记录验证过程中遇到的所有问题，为后续优化提供参考
4. **安全考虑**：验证过程中注意AWS账号安全，避免暴露敏感信息
5. **修正策略**：深入验证中遇到问题时，采用渐进式修正方法，最多3次尝试，超出范围或次数限制则标记为失败
6. **清理验证**：资源清理后必须二次确认，防止产生意外费用

将最终验证报告写入文件：{result_file}

请开始验证分析。
"""
    
    result = run_q_chat(prompt, "fs_read,fs_write,use_aws,execute_bash")
    return result

# Main function
def main():
    """Main entry point for the AWS China Region Content Validation Tool."""
    # Parse command line arguments
    config = parse_args()
    if not config.url:
        print("URL is required. Use -u/--url to specify the content URL.")
        return 1

    # Set up logging
    logger = setup_logging(config.log_level)

    # Generate a unique execution ID
    validation_id = str(uuid.uuid4())[:8]

    # Create data directory
    Path("./data").mkdir(exist_ok=True)
    
    # Generate file names based on URL
    url_basename = os.path.basename(config.url.rstrip("/"))
    safe_filename = ''.join(c if c.isalnum() else '_' for c in url_basename)
    
    try:
        # Step 1: Convert content to Markdown
        logger.info("Converting content to Markdown...")
        markdown = convert_url_to_markdown(config.url)
        markdown_file = f"./data/{safe_filename}_{validation_id}.md"
        with open(markdown_file, "w") as f:
            f.write(markdown)
        logger.info("Validating content...")
        result_file = f"./data/{safe_filename}_result_{validation_id}.md"
        result = validate_content(markdown_file, result_file, validation_id, config.region, config.profile)
        # logger.info(f"Validation process completed:\n{result["output"]}")
        return 0
    
    except KeyboardInterrupt:
        logger.warning("Process interrupted by user")
        return 130
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())