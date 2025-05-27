#!/bin/bash

# aws-cn-tool.sh - 主入口脚本
# Author: Amazon Q

source ./bin/aws-cn-common-utils.sh

# 显示帮助信息
show_help() {
    echo "AWS 中国区内容转换工具"
    echo "用法: $0 <命令> [选项]"
    echo
    echo "可用命令:"
    echo "  convert   - 将博客转换为Markdown"
    echo "  analyze   - 分析内容中的AWS服务"
    echo "  validate  - 验证服务在中国区的可用性"
    echo "  evaluate  - 评估内容适用性"
    echo "  setup     - 设置环境"
    echo
    echo "运行 '$0 <命令> --help' 获取特定命令的帮助"
}

# 检查是否提供了命令
if [ $# -eq 0 ]; then
    show_help
    exit 1
fi

# 命令路由
case "$1" in
    convert)
        shift
        ./bin/aws-cn-content-convert.sh "$@"
        ;;
    analyze)
        shift
        ./bin/aws-cn-content-analyze.sh "$@"
        ;;
    validate)
        shift
        ./bin/aws-cn-service-validate.sh "$@"
        ;;
    evaluate)
        shift
        ./bin/aws-cn-content-evaluate.sh "$@"
        ;;
    setup)
        shift
        ./bin/aws-cn-setup.sh "$@"
        ;;
    help|--help|-h)
        show_help
        exit 0
        ;;
    *)
        log_error "未知命令: $1"
        show_help
        exit 1
        ;;
esac
