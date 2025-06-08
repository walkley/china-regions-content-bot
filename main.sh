#!/bin/bash

# main.sh - AWS China Region Content Validation Tool
# Author: Amazon Q

# Import common utilities
source src/common-utils.sh

# Import specific modules
source src/content-converter.sh
source src/basic-validator.sh
source src/deep-validator.sh

# Display help information
show_help() {
    echo "AWS China Region Content Validation Tool"
    echo "Usage: $0 -u <blog URL> [-r <region>] [-p <profile>] [-d] [-m <max-cost>]"
    echo
    echo "Parameters:"
    echo "  -u, --url       Blog URL (required)"
    echo "  -r, --region    AWS China region (default: cn-northwest-1)"
    echo "  -p, --profile   AWS CLI profile (default: cn)"
    echo "  -d, --deep      Enable deep validation mode (subject to feasibility gate)"
    echo "  -m, --max-cost  Maximum cost limit for deep validation in USD (default: 10)"
    echo "  -h, --help      Display this help information"
    echo
    echo "Validation Modes:"
    echo "  Basic:  Fast service availability analysis (always executed)"
    echo "  Deep:   Actual deployment/execution validation (gated by feasibility)"
    echo
    echo "Intelligent Feasibility Gate:"
    echo "  HIGH:     Deep validation strongly recommended ✅"
    echo "  MODERATE: Deep validation recommended with adaptations ⚠️"
    echo "  LOW:      Deep validation blocked to prevent resource waste ❌"
    echo
    echo "Examples:"
    echo "  $0 -u https://aws.amazon.com/blogs/aws/some-article -r cn-north-1 -p cn"
    echo "  $0 -u https://aws.amazon.com/blogs/aws/some-article -d -m 5"
}

# Default values
URL=""
REGION="cn-northwest-1"
PROFILE="cn"
TEMP_DIR="./data/temp"
DEEP_MODE=false
MAX_COST=10

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -u|--url)
            URL="$2"
            shift 2
            ;;
        -r|--region)
            REGION="$2"
            shift 2
            ;;
        -p|--profile)
            PROFILE="$2"
            shift 2
            ;;
        -d|--deep)
            DEEP_MODE=true
            shift
            ;;
        -m|--max-cost)
            MAX_COST="$2"
            shift 2
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            log_error "Unknown parameter '$1'"
            show_help
            exit 1
            ;;
    esac
done

# Check required parameters
if [ -z "$URL" ]; then
    log_error "Blog URL must be provided"
    show_help
    exit 1
fi

# Create temporary and results directories
mkdir -p "$TEMP_DIR"
mkdir -p "./data"
TEMP_MD="$TEMP_DIR/content.md"
RESULT_FILE="./data/$(basename "$URL" | sed 's/[^a-zA-Z0-9]/_/g')_result.json"
DEEP_RESULT_FILE="./data/$(basename "$URL" | sed 's/[^a-zA-Z0-9]/_/g')_deep_result.json"

# Step 1: Convert blog content to Markdown
convert_content_to_markdown "$URL" "$TEMP_MD"
if [ $? -ne 0 ]; then
    exit 1
fi

# Step 2: Perform basic validation
perform_basic_validation "$TEMP_MD" "$RESULT_FILE" "$REGION" "$PROFILE"
if [ $? -ne 0 ]; then
    exit 1
fi

# Display basic validation results
display_basic_results "$RESULT_FILE"

# Step 3: Perform deep validation if requested and feasible
if [ "$DEEP_MODE" = true ]; then
    log_info "🔍 Deep validation requested - checking feasibility gate..."
    if perform_deep_validation "$TEMP_MD" "$RESULT_FILE" "$DEEP_RESULT_FILE" "$REGION" "$PROFILE" "$MAX_COST" "$TEMP_DIR"; then
        log_success "✅ Deep validation completed successfully!"
    else
        log_warning "⚠️  Deep validation was blocked or failed"
        log_info "💡 Tip: If blocked due to LOW feasibility, improve basic validation results first"
    fi
else
    log_info "Deep validation not requested. Use -d flag to enable deep validation."
    log_info "💡 Note: Deep validation is subject to intelligent feasibility gating"
fi

# Clean up temporary files
rm -f "$TEMP_MD"

exit 0
