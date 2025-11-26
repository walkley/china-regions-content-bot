#!/bin/bash
# AWS China Region Content Validation Tool
# Shell script version

set -e

# Default values
REGION="cn-northwest-1"
PROFILE="cn"
LOG_LEVEL="INFO"

# Logging function
log() {
    local level=$1
    shift
    local message="$@"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] - $level - $message"
}

log_info() {
    log "INFO" "$@"
}

log_error() {
    log "ERROR" "$@"
}

log_warning() {
    log "WARNING" "$@"
}

# Check required commands
check_dependencies() {
    local missing_deps=()

    # # Check markitdown (Comment out since markitdown no longer needed)
    # if ! command -v markitdown &> /dev/null; then
    #     missing_deps+=("markitdown (install: pipx install markitdown)")
    # fi

    # Check kiro-cli
    if ! command -v kiro-cli &> /dev/null; then
        missing_deps+=("kiro-cli (Amazon Q Developer CLI)")
    fi

    # Check aws cli
    if ! command -v aws &> /dev/null; then
        missing_deps+=("aws (AWS CLI)")
    fi

    # Check uuidgen
    if ! command -v uuidgen &> /dev/null; then
        missing_deps+=("uuidgen (usually pre-installed on macOS/Linux)")
    fi

    if [ ${#missing_deps[@]} -ne 0 ]; then
        log_error "Missing required dependencies:"
        for dep in "${missing_deps[@]}"; do
            echo "  - $dep"
        done
        exit 1
    fi
}

# Check AWS profile configuration
check_aws_profile() {
    local profile=$1

    if ! aws configure list --profile "$profile" &> /dev/null; then
        log_error "AWS profile '$profile' not found or not configured properly."
        echo "Please run: aws configure --profile $profile"
        exit 1
    fi

    # Check if profile has credentials
    if ! aws sts get-caller-identity --profile "$profile" &> /dev/null; then
        log_warning "AWS profile '$profile' credentials may be invalid or expired."
        echo "Continuing anyway, but validation may fail..."
    fi
}

# Run dependency checks
check_dependencies

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
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
        --log-level)
            LOG_LEVEL="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 -u <url> [-r <region>] [-p <profile>] [--log-level <level>]"
            echo ""
            echo "Options:"
            echo "  -u, --url         URL of the content to validate (required)"
            echo "  -r, --region      AWS China region (default: cn-northwest-1)"
            echo "  -p, --profile     AWS CLI profile (default: cn)"
            echo "  --log-level       Logging level (default: INFO)"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Check required arguments
if [ -z "$URL" ]; then
    log_error "URL is required. Use -u/--url to specify the content URL."
    exit 1
fi

# Check AWS profile configuration
check_aws_profile "$PROFILE"

# Generate timestamp for validation
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')

# Extract blog URL path (remove protocol and domain, convert to safe directory name)
# Example: https://aws.amazon.com/blogs/aws/my-blog/ -> blogs_aws_my-blog
URL_PATH=$(echo "$URL" | sed -E 's|https?://[^/]+/||' | sed 's|/$||' | sed 's|/|_|g')

# Create directory structure for this validation: docs/reports/<url_path>/<timestamp>
VALIDATION_DIR="./docs/reports/${URL_PATH}/${TIMESTAMP}"
mkdir -p "$VALIDATION_DIR"

# File paths
MARKDOWN_FILE="${VALIDATION_DIR}/source.md"
RESULT_FILE="${VALIDATION_DIR}/report.md"
LOG_FILE="${VALIDATION_DIR}/validation.log"

log_info "Validating $URL"

# Step 1: Convert URL to Markdown using markitdown
log_info "Converting URL to Markdown..."
if ! python3 content-convert.py -u "$URL" -o "$MARKDOWN_FILE" 2>&1; then
    log_error "Failed to convert URL to Markdown"
    exit 1
fi

# Step 2: Run validation with kiro-cli agent
log_info "Starting validation with china-validator agent"
log_info "Content file: $MARKDOWN_FILE"
log_info "Result file: $RESULT_FILE"
log_info "Region: $REGION, Profile: $PROFILE"

# Set environment variables for the agent
export VALIDATION_CONTENT_FILE="$MARKDOWN_FILE"
export VALIDATION_RESULT_FILE="$RESULT_FILE"
export VALIDATION_AWS_REGION="$REGION"
export VALIDATION_AWS_PROFILE="$PROFILE"

# Run kiro-cli agent
echo "开始验证" | kiro-cli chat --no-interactive --agent=china-validator > "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
    log_info "Succeeded"
    exit 0
else
    log_error "Failed!"
    exit 1
fi
