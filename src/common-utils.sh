#!/bin/bash

# common-utils.sh - Common utility functions
# Author: Amazon Q

# ANSI color codes for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
}

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check required dependencies
check_dependencies() {
    local missing_deps=0
    
    for cmd in "$@"; do
        if ! command_exists "$cmd"; then
            log_error "Required dependency '$cmd' is not installed."
            missing_deps=1
        fi
    done
    
    if [ $missing_deps -eq 1 ]; then
        log_error "Please install the missing dependencies and try again."
        exit 1
    fi
}

# Function to validate AWS profile
validate_aws_profile() {
    local profile="$1"
    
    if ! aws configure list --profile "$profile" &>/dev/null; then
        log_error "AWS profile '$profile' does not exist or is not properly configured."
        log_info "Please run 'aws configure --profile $profile' to set up the profile."
        exit 1
    fi
    
    log_info "Using AWS profile: $profile"
}

# Function to create a temporary isolated environment
create_isolated_environment() {
    local env_name="$1"
    local env_dir="$TEMP_DIR/$env_name"
    
    log_info "Creating isolated environment at $env_dir"
    mkdir -p "$env_dir"
    
    echo "$env_dir"
}

# Function to clean up AWS resources by tag
cleanup_aws_resources() {
    local tag_key="$1"
    local tag_value="$2"
    local region="$3"
    local profile="$4"
    
    log_info "Cleaning up AWS resources with tag $tag_key=$tag_value"
    
    # List of services to check for resources
    local services=("ec2" "s3" "lambda" "dynamodb" "cloudformation")
    
    for service in "${services[@]}"; do
        log_info "Cleaning up $service resources..."
        
        case "$service" in
            ec2)
                # Terminate EC2 instances
                aws ec2 describe-instances \
                    --filters "Name=tag:$tag_key,Values=$tag_value" \
                    --query "Reservations[].Instances[].InstanceId" \
                    --output text \
                    --region "$region" \
                    --profile "$profile" | \
                xargs -I {} aws ec2 terminate-instances \
                    --instance-ids {} \
                    --region "$region" \
                    --profile "$profile" 2>/dev/null
                ;;
            s3)
                # Empty and delete S3 buckets
                aws s3api list-buckets \
                    --query "Buckets[?contains(Name, '$tag_value')].Name" \
                    --output text \
                    --profile "$profile" | \
                xargs -I {} sh -c "aws s3 rm s3://{} --recursive --profile $profile && aws s3api delete-bucket --bucket {} --profile $profile" 2>/dev/null
                ;;
            lambda)
                # Delete Lambda functions
                aws lambda list-functions \
                    --query "Functions[?contains(FunctionName, '$tag_value')].FunctionName" \
                    --output text \
                    --region "$region" \
                    --profile "$profile" | \
                xargs -I {} aws lambda delete-function \
                    --function-name {} \
                    --region "$region" \
                    --profile "$profile" 2>/dev/null
                ;;
            dynamodb)
                # Delete DynamoDB tables
                aws dynamodb list-tables \
                    --region "$region" \
                    --profile "$profile" \
                    --output text | \
                grep "$tag_value" | \
                xargs -I {} aws dynamodb delete-table \
                    --table-name {} \
                    --region "$region" \
                    --profile "$profile" 2>/dev/null
                ;;
            cloudformation)
                # Delete CloudFormation stacks
                aws cloudformation list-stacks \
                    --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE \
                    --query "StackSummaries[?contains(StackName, '$tag_value')].StackName" \
                    --output text \
                    --region "$region" \
                    --profile "$profile" | \
                xargs -I {} aws cloudformation delete-stack \
                    --stack-name {} \
                    --region "$region" \
                    --profile "$profile" 2>/dev/null
                ;;
        esac
    done
    
    log_success "Resource cleanup completed"
}

# Check for required tools at script startup
check_dependencies "q" "aws"
