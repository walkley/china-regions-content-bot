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
    for cmd in "python3" "pip3" "q" "aws" "jq"; do
        if ! command_exists "$cmd"; then
            if [ "$cmd" = "python3" ]; then
                log_error "Python 3 is not installed or not in PATH"
                log_info "Please install Python 3: https://www.python.org/downloads/"
            elif [ "$cmd" = "pip3" ]; then
                log_error "pip3 is not installed or not in PATH"
                log_info "Please install pip3 for Python package management"
            elif [ "$cmd" = "q" ]; then
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

# Setup Python virtual environment
setup_python_venv() {
    log_info "Setting up Python virtual environment..."
    
    local venv_path="$(dirname "$0")/../venv"
    
    if [ ! -d "$venv_path" ]; then
        log_info "Creating virtual environment..."
        python3 -m venv "$venv_path"
        if [ $? -ne 0 ]; then
            log_error "Failed to create virtual environment"
            exit 1
        fi
    else
        log_info "Virtual environment already exists"
    fi
    
    # Activate virtual environment and install requirements
    log_info "Installing Python packages..."
    source "$venv_path/bin/activate"
    
    local requirements_file="$(dirname "$0")/../requirements.txt"
    if [ -f "$requirements_file" ]; then
        pip install --upgrade pip
        pip install -r "$requirements_file"
        if [ $? -ne 0 ]; then
            log_error "Failed to install Python packages"
            exit 1
        fi
        log_success "Python packages installed successfully"
    else
        log_warning "requirements.txt not found, skipping package installation"
    fi
    
    deactivate
    log_success "Python virtual environment setup complete"
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
    chmod +x $(dirname "$0")/aws-cn-*.py
    
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
    setup_python_venv
    set_permissions
    check_aws_config
    create_version_file
    
    echo
    echo "====================================================="
    log_success "Setup complete!"
    echo
    log_info "You can now use the following commands:"
    echo "  ./aws-cn-tool.sh convert -u <URL> -o <output.md> - Convert blog content to Markdown"
    echo "  ./aws-cn-tool.sh analyze - Analyze content for AWS services"
    echo "  ./aws-cn-tool.sh validate - Generate service validation scripts"
    echo "  ./aws-cn-tool.sh evaluate - Evaluate content applicability"
    echo "  ./bin/aws-cn-content-convert.py - Direct Python script usage (requires venv activation)"
    echo "====================================================="
}

# Run the main function
main
