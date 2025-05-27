#!/bin/bash

# aws-cn-common-utils.sh - Common utility functions for AWS China content conversion tools
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

# Check for required tools at script startup
check_dependencies "q" "aws"
