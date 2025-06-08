#!/bin/bash

# tutorial-validator.sh - Deep validation for tutorials and step-by-step guides
# Author: Amazon Q

# Import common utilities
source src/common-utils.sh

# Function to execute tutorial-based deep validation
execute_tutorial_validation() {
    local content_file="$1"
    local basic_result_file="$2"
    local deep_result_file="$3"
    local region="$4"
    local profile="$5"
    local max_cost="$6"
    
    log_info "Executing tutorial-based deep validation..."
    
    # Build tutorial validation prompt
    local tutorial_validation_prompt=$(cat << EOF
You are an AWS China Region Intelligent Validator. Your task is to analyze a tutorial/guide and validate its executability in AWS China regions. Follow these instructions carefully:

First, note the AWS configuration you\'ll be working with:
<aws_config>
Region: $region
Profile: $profile
</aws_config>

Here is the technical content to analyze:
<tech_content>
\$(cat "$content_file")
</tech_content>

Here is the basic validation result:
<basic_validation>
\$(cat "$basic_result_file")
</basic_validation>

Begin your analysis by examining the tutorial content:

1. Extract all operational steps/tutorials
2. Verify service availability in China regions
3. Extract all configuration parameters
4. Generate either:
   - A CloudFormation template (if the solution involves multiple resources)
   - A shell script with AWS CLI commands (if the solution is primarily operational)

For tutorial validation:
1. Execute each step in the tutorial
2. Make any necessary modifications for China region compatibility
3. Validate that each step works as expected
4. Document any errors or issues encountered
5. Clean up all resources after validation

Important constraints:
- Maximum cost limit: $max_cost USD
- Use the smallest/cheapest resource sizes possible
- Set short timeouts and TTLs for all resources
- Ensure all resources are properly tagged for tracking
- Clean up ALL resources after validation

Provide your final output in this JSON format:
{
  "validation_type": "tutorial_execution",
  "agent_used": "tutorial_execution_agent",
  "validation_results": {
    "steps_analysis": {
      "total_steps": 10,
      "executable_steps": 8,
      "non_executable_steps": 2,
      "step_details": [
        {"step": 1, "description": "...", "executable": true, "issues": []},
        {"step": 2, "description": "...", "executable": false, "issues": ["reason"]}
      ]
    },
    "china_compatibility": {
      "required_modifications": ["list", "of", "modifications"],
      "unavailable_services": ["list", "of", "unavailable", "services"],
      "alternative_solutions": ["list", "of", "alternatives"]
    },
    "executable_guide": {
      "modified_steps": ["step1", "step2", "..."],
      "execution_results": ["result1", "result2", "..."],
      "cleanup_steps": ["step1", "step2", "..."]
    }
  },
  "confidence": 0.0-1.0,
  "execution_time": "minutes:seconds",
  "recommendations": ["recommendation1", "recommendation2", "..."]
}

Write your final JSON result directly to this file: $deep_result_file
Make sure the JSON is properly formatted and valid.

Important rules:
- Do not attempt to execute steps that are clearly incompatible with China regions
- Document all assumptions made during execution
- If a service is not available in China regions, note it as a blocker
- Always verify IAM permissions before execution
- Follow AWS China region best practices for networking and security
- Clean up ALL resources after validation

Begin your analysis now.
EOF
)

    # Execute tutorial validation
    log_info "Analyzing and validating tutorial steps, this may take some time..."
    echo -e "$tutorial_validation_prompt" | q chat --no-interactive --trust-tools=use_aws,fs_write,fs_read,execute_bash > /dev/null

    # Check if result file was generated
    if [ ! -f "$deep_result_file" ]; then
        log_error "Tutorial validation failed, result file was not generated"
        return 1
    fi

    log_success "Tutorial validation complete! Results saved to: $deep_result_file"
    
    return 0
}

# If script is run directly (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Check for required parameters
    if [ $# -lt 6 ]; then
        log_error "Usage: $0 <content_file> <basic_result_file> <deep_result_file> <region> <profile> <max_cost>"
        exit 1
    fi
    
    # Execute tutorial validation
    execute_tutorial_validation "$1" "$2" "$3" "$4" "$5" "$6"
    exit $?
fi
