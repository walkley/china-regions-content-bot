#!/bin/bash

# aws-cn-setup.sh - Setup script for AWS China Content Conversion Tools
# Author: Amazon Q

# Import common functions
source $(dirname "$0")/aws-cn-common-utils.sh

# Create directory structure
create_directories() {
    log_info "Creating directory structure..."
    
    mkdir -p $(dirname "$0")/../data
    
    log_success "Directory structure created"
}

# Check dependencies
check_required_dependencies() {
    log_info "Checking dependencies..."
    
    local missing_deps=0
    
    # Check for required commands
    for cmd in "q" "aws" "jq"; do
        if ! command_exists "$cmd"; then
            if [ "$cmd" = "q" ]; then
                log_error "Amazon Q CLI (q) is not installed or not in PATH"
                log_info "Please install Amazon Q CLI to use these tools"
            elif [ "$cmd" = "aws" ]; then
                log_error "AWS CLI is not installed or not in PATH"
                log_info "Please install AWS CLI: https://aws.amazon.com/cli/"
            elif [ "$cmd" = "jq" ]; then
                log_warning "jq is not installed (recommended for JSON processing)"
                log_info "Install jq for better JSON handling: https://stedolan.github.io/jq/download/"
            fi
            
            if [ "$cmd" != "jq" ]; then
                missing_deps=1
            fi
        fi
    done
    
    if [ $missing_deps -eq 1 ]; then
        log_error "Please install the required dependencies and run setup again"
        exit 1
    fi
    
    log_success "All required dependencies are installed"
}

# Check AWS configuration
check_aws_config() {
    log_info "Checking AWS configuration..."
    
    if ! aws configure list &>/dev/null; then
        log_warning "AWS CLI is not configured"
        log_info "Please run 'aws configure' to set up your AWS credentials"
    else
        log_success "AWS CLI is configured"
    fi
    
    # Check for China region profile
    if ! aws configure list --profile cn &>/dev/null; then
        log_warning "AWS China profile 'cn' is not configured"
        log_info "To use these tools with AWS China regions, please run:"
        log_info "aws configure --profile cn"
        log_info "and set the appropriate credentials and region (cn-north-1 or cn-northwest-1)"
    else
        log_success "AWS China profile 'cn' is configured"
    fi
}

# Set executable permissions
set_permissions() {
    log_info "Setting executable permissions..."
    
    chmod +x $(dirname "$0")/aws-cn-*.sh
    
    log_success "Permissions set"
}

# Create VERSION file
create_version_file() {
    log_info "Creating version file..."
    
    echo "1.0.0" > $(dirname "$0")/../VERSION
    
    log_success "Version file created"
}

# Main setup function
main() {
    echo "====================================================="
    echo "  AWS China Content Conversion Tools - Setup"
    echo "====================================================="
    echo
    
    check_required_dependencies
    create_directories
    set_permissions
    check_aws_config
    create_version_file
    
    echo
    echo "====================================================="
    log_success "Setup complete!"
    echo
    log_info "You can now use the following commands:"
    echo "  ./bin/aws-cn-content-convert.sh - Convert blog content to Markdown"
    echo "  ./bin/aws-cn-content-analyze.sh - Analyze content for AWS services"
    echo "  ./bin/aws-cn-service-validate.sh - Generate service validation scripts"
    echo "  ./bin/aws-cn-content-evaluate.sh - Evaluate content applicability"
    echo "====================================================="
}

# Run the main function
main
