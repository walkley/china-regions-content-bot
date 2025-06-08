#!/bin/bash

# deep-validator.sh - Deep validation for AWS content in China regions
# Author: Amazon Q

# Import common utilities
source src/common-utils.sh

# Import specific validators
source src/project-validator.sh
source src/tutorial-validator.sh

# Function to determine content type
determine_content_type() {
    local result_file="$1"
    
    # Extract GitHub project URL and procedures from basic validation result
    if command_exists jq; then
        local github_project=$(jq -r '.content_analysis.github_project // ""' "$result_file" 2>/dev/null)
        local has_procedures=$(jq -r '.content_analysis.procedures | length > 0' "$result_file" 2>/dev/null)
    else
        local github_project=$(grep -o '"github_project": *"[^"]*"' "$result_file" | head -1 | cut -d'"' -f4)
        local has_procedures=$(grep -o '"procedures": *\[[^\]]*\]' "$result_file" | grep -v '\[\]' | wc -l)
        if [ "$has_procedures" -gt 0 ]; then
            has_procedures="true"
        else
            has_procedures="false"
        fi
    fi
    
    # Determine content type
    local content_type=""
    if [ -n "$github_project" ] && [ "$github_project" != "null" ]; then
        content_type="project"
        log_info "Content type detected: Project (GitHub repository found)"
    elif [ "$has_procedures" = "true" ]; then
        content_type="tutorial"
        log_info "Content type detected: Tutorial (Step-by-step procedures found)"
    else
        log_warning "Could not determine content type automatically."
        echo "Please select content type for deep validation:"
        echo "1. Project (GitHub repository or code samples)"
        echo "2. Tutorial (Step-by-step procedures)"
        read -p "Enter choice (1/2): " type_choice
        
        if [ "$type_choice" = "1" ]; then
            content_type="project"
        elif [ "$type_choice" = "2" ]; then
            content_type="tutorial"
        else
            log_error "Invalid choice. Exiting."
            return 1
        fi
    fi
    
    echo "$content_type"
    return 0
}

# Function to check feasibility level with intelligent blocking
check_feasibility_level() {
    local result_file="$1"
    
    # Extract feasibility level and reasoning from basic validation result
    if command_exists jq; then
        local level=$(jq -r '.feasibility_assessment.level' "$result_file" 2>/dev/null)
        local reasoning=$(jq -r '.feasibility_assessment.reasoning' "$result_file" 2>/dev/null)
    else
        local level=$(grep -o '"level": *"[^"]*"' "$result_file" | head -1 | cut -d'"' -f4)
        local reasoning=$(grep -o '"reasoning": *"[^"]*"' "$result_file" | head -1 | cut -d'"' -f4)
    fi
    
    # Intelligent feasibility gate with detailed feedback
    case "$level" in
        "high")
            log_success "✅ Feasibility: HIGH - Strongly recommended for deep validation"
            log_info "All core services are available, deep validation should provide valuable insights"
            return 0
            ;;
        "moderate") 
            log_info "⚠️  Feasibility: MODERATE - Deep validation recommended with adaptations"
            log_info "Some services may need workarounds, but validation is still worthwhile"
            return 0
            ;;
        "low")
            log_error "❌ Feasibility: LOW - Deep validation blocked by intelligent gate"
            log_error "Reason: $reasoning"
            log_info "💡 Why blocked: Deep validation would waste resources on unfeasible content"
            log_info "📋 Suggestion: Address basic validation issues first, then retry"
            log_info "🔧 Focus on: Service availability, alternative solutions, or architecture changes"
            return 1
            ;;
        *)
            log_error "❓ Unknown feasibility level: $level - Cannot proceed safely"
            log_error "Please check the basic validation results for errors"
            return 1
            ;;
    esac
}

# Function to perform deep validation
perform_deep_validation() {
    local content_file="$1"
    local basic_result_file="$2"
    local deep_result_file="$3"
    local region="$4"
    local profile="$5"
    local max_cost="$6"
    local temp_dir="$7"
    
    # Check feasibility level
    check_feasibility_level "$basic_result_file"
    if [ $? -ne 0 ]; then
        return 1
    fi
    
    # Determine content type
    local content_type=$(determine_content_type "$basic_result_file")
    if [ -z "$content_type" ]; then
        return 1
    fi
    
    # Execute deep validation based on content type
    log_info "Starting deep validation (type: $content_type)..."
    
    if [ "$content_type" = "project" ]; then
        # Extract GitHub project URL
        if command_exists jq; then
            local github_url=$(jq -r '.content_analysis.github_project' "$basic_result_file" 2>/dev/null)
        else
            local github_url=$(grep -o '"github_project": *"[^"]*"' "$basic_result_file" | head -1 | cut -d'"' -f4)
        fi
        
        # Execute project validation
        execute_project_validation "$github_url" "$basic_result_file" "$deep_result_file" "$region" "$profile" "$max_cost" "$temp_dir"
    else
        # Execute tutorial validation
        execute_tutorial_validation "$content_file" "$basic_result_file" "$deep_result_file" "$region" "$profile" "$max_cost"
    fi
    
    return $?
}

# Function to display deep validation results
display_deep_results() {
    local deep_result_file="$1"
    
    # Extract key information and display
    if command_exists jq; then
        local validation_type=$(jq -r '.validation_type' "$deep_result_file" 2>/dev/null)
        local confidence=$(jq -r '.confidence' "$deep_result_file" 2>/dev/null)
        local execution_time=$(jq -r '.execution_time' "$deep_result_file" 2>/dev/null)
        
        if [ "$validation_type" = "project_deployment" ]; then
            local modifications=$(jq -r '.validation_results.china_compatibility.required_modifications | length' "$deep_result_file" 2>/dev/null)
            local unavailable=$(jq -r '.validation_results.china_compatibility.unavailable_services | length' "$deep_result_file" 2>/dev/null)
        else
            local executable_steps=$(jq -r '.validation_results.steps_analysis.executable_steps' "$deep_result_file" 2>/dev/null)
            local total_steps=$(jq -r '.validation_results.steps_analysis.total_steps' "$deep_result_file" 2>/dev/null)
            local executable_percent=$((executable_steps * 100 / total_steps))
        fi
    else
        local validation_type=$(grep -o '"validation_type": *"[^"]*"' "$deep_result_file" | head -1 | cut -d'"' -f4)
        local confidence=$(grep -o '"confidence": *[0-9.]*' "$deep_result_file" | head -1 | awk '{print $2}')
        local execution_time=$(grep -o '"execution_time": *"[^"]*"' "$deep_result_file" | head -1 | cut -d'"' -f4)
        
        if [ "$validation_type" = "project_deployment" ]; then
            local modifications=$(grep -o '"required_modifications": *\[[^\]]*\]' "$deep_result_file" | grep -o ',' | wc -l)
            modifications=$((modifications + 1))
            local unavailable=$(grep -o '"unavailable_services": *\[[^\]]*\]' "$deep_result_file" | grep -o ',' | wc -l)
            unavailable=$((unavailable + 1))
        else
            local executable_steps=$(grep -o '"executable_steps": *[0-9]*' "$deep_result_file" | head -1 | awk '{print $2}')
            local total_steps=$(grep -o '"total_steps": *[0-9]*' "$deep_result_file" | head -1 | awk '{print $2}')
            local executable_percent=$((executable_steps * 100 / total_steps))
        fi
    fi
    
    echo
    echo "===== Deep Validation Result Summary ====="
    echo "Validation Type: $validation_type"
    echo "Execution Time: $execution_time"
    echo "Confidence: $confidence"
    
    if [ "$validation_type" = "project_deployment" ]; then
        echo "Required Modifications: $modifications"
        echo "Unavailable Services: $unavailable"
    else
        echo "Executable Steps: $executable_steps/$total_steps ($executable_percent%)"
    fi
    
    echo
    log_info "Complete deep validation results saved to: $deep_result_file"
}

# If script is run directly (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Check for required parameters
    if [ $# -lt 7 ]; then
        log_error "Usage: $0 <content_file> <basic_result_file> <deep_result_file> <region> <profile> <max_cost> <temp_dir>"
        exit 1
    fi
    
    # Perform deep validation
    perform_deep_validation "$1" "$2" "$3" "$4" "$5" "$6" "$7"
    exit_code=$?
    
    if [ $exit_code -eq 0 ]; then
        display_deep_results "$3"
    fi
    
    exit $exit_code
fi
