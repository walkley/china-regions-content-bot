#!/bin/bash

# basic-validator.sh - Basic validation of AWS content for China regions
# Author: Amazon Q

# Import common utilities
source src/common-utils.sh

# Function to perform basic validation
perform_basic_validation() {
    local content_file="$1"
    local result_file="$2"
    local region="$3"
    local profile="$4"
    
    log_info "Analyzing content and validating service availability..."
    
    # Read Markdown content
    local content=$(cat "$content_file")
    
    # Read unavailable services list
    local unavailable_services=$(cat ./src/unavailable_services.txt)
    
    # Build validation prompt
    local validation_prompt=$(cat << EOF
You are an AWS China Region service availability validator. Your task is to analyze AWS technical content and determine if it can be implemented in AWS China regions (cn-north-1, cn-northwest-1) based on service availability.

First, here is the list of services that are unavailable in AWS China regions:
<unavailable_services>
$unavailable_services
</unavailable_services>

Here is the technical content to analyze:
<tech_content>
$content
</tech_content>

Follow these steps to validate the content:

1. Carefully read through the technical content and identify all AWS services mentioned. Include both explicitly stated services and those implied by resource types or APIs mentioned.

2. For each identified service:
   a. Check if it appears in the unavailable_services list
   b. If not in the unavailable list, use the use_aws tool in China region '$region' with profile name '$profile' to validate specific feature availability:
      - Only use read-only operations (list, get, describe)
      - Example: aws servicename list-features --region $region --profile $profile
   c. Record whether each service is available or unavailable

3. Analyze the content to identify:
   a. Any GitHub project URLs or code repositories mentioned
   b. Any step-by-step procedures or tutorials
   c. Key dependencies between services

4. Calculate the feasibility assessment:
   - HIGH: All identified services are available
   - MODERATE: >70% of services available with workarounds possible
   - LOW: <70% of services available, requiring major changes

5. Format your response as a JSON object with these fields:
   - content_analysis:
     - identified_services: Array of all AWS services found
     - dependencies: Array of service dependencies
     - github_project: URL to GitHub project if found, otherwise empty string
     - procedures: Array of step-by-step procedures if found
   - service_validation_results:
     - available: Array of available services
     - unavailable: Array of unavailable services
     - api_test_results: Object with service names as keys and test results as values
   - feasibility_assessment:
     - level: "high", "moderate", or "low"
     - reasoning: Brief explanation of impact
     - confidence: Number between 0 and 1

Before providing your final answer, use <scratchpad> tags to:
1. List out each service you identified
2. Show your availability calculations
3. Draft your reasoning for the feasibility assessment

Write your final JSON result directly to this file: $result_file
Make sure the JSON is properly formatted and valid.

Remember:
- Only use read-only AWS CLI operations
- Include all services mentioned in the content
- Base feasibility on service criticality, not just count
- Provide clear reasoning for your assessment
- Format output as valid JSON
- Write the result directly to the specified file path

Begin your analysis now.
EOF
)

    # Execute validation
    log_info "Analyzing content and validating service availability, this may take a few minutes..."
    echo -e "$validation_prompt" | q chat --no-interactive --trust-tools=use_aws,fs_write > /dev/null

    # Check if result file was generated
    if [ ! -f "$result_file" ]; then
        log_error "Analysis failed, result file was not generated"
        return 1
    fi

    log_success "Basic validation complete! Results saved to: $result_file"
    return 0
}

# Function to display basic validation results
display_basic_results() {
    local result_file="$1"
    
    # Extract key information and display
    if command_exists jq; then
        local level=$(jq -r '.feasibility_assessment.level' "$result_file" 2>/dev/null)
        local reasoning=$(jq -r '.feasibility_assessment.reasoning' "$result_file" 2>/dev/null)
    else
        local level=$(grep -o '"level": *"[^"]*"' "$result_file" | head -1 | cut -d'"' -f4)
        local reasoning=$(grep -o '"reasoning": *"[^"]*"' "$result_file" | head -1 | cut -d'"' -f4)
    fi

    echo
    echo "===== Analysis Result Summary ====="
    echo "Applicability Rating: $level"
    echo "Reason: $reasoning"
    echo
    
    return 0
}

# If script is run directly (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Check for required parameters
    if [ $# -lt 4 ]; then
        log_error "Usage: $0 <content file> <result file> <region> <profile>"
        exit 1
    fi
    
    # Perform basic validation
    perform_basic_validation "$1" "$2" "$3" "$4"
    exit_code=$?
    
    if [ $exit_code -eq 0 ]; then
        display_basic_results "$2"
    fi
    
    exit $exit_code
fi
