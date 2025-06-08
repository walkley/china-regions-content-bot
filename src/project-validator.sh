#!/bin/bash

# project-validator.sh - Deep validation for GitHub projects
# Author: Amazon Q

# Import common utilities
source src/common-utils.sh

# Function to execute project-based deep validation
execute_project_validation() {
    local github_url="$1"
    local basic_result_file="$2"
    local deep_result_file="$3"
    local region="$4"
    local profile="$5"
    local max_cost="$6"
    local temp_dir="$7"
    
    log_info "Executing project-based deep validation..."
    
    # Validate GitHub URL
    if [ -z "$github_url" ] || [ "$github_url" = "null" ]; then
        log_warning "No GitHub project URL found in basic validation results."
        read -p "Please enter GitHub project URL manually: " github_url
        
        if [ -z "$github_url" ]; then
            log_error "No GitHub URL provided. Cannot proceed with project validation."
            return 1
        fi
    fi
    
    # Create a temporary directory for project deployment
    local project_dir="$temp_dir/project"
    mkdir -p "$project_dir"
    
    # Build project validation prompt
    local project_validation_prompt=$(cat << EOF
You are an AWS China Region Intelligent Validator. Your task is to analyze a GitHub project and validate its deployability in AWS China regions. Follow these instructions carefully:

First, note the AWS configuration you\'ll be working with:
<aws_config>
Region: $region
Profile: $profile
</aws_config>

Here is the GitHub project to analyze:
<github_project>
$github_url
</github_project>

Here is the basic validation result:
<basic_validation>
\$(cat "$basic_result_file")
</basic_validation>

Begin your analysis by examining the GitHub project:

1. Document the repository URL and branch information
2. List the deployment prerequisites
3. Note any immediate compatibility concerns with China regions
4. Document any required modifications for China region deployment
5. Create a deployment plan with specific steps

For deployment validation:
1. Clone the repository to a temporary directory
2. Make any necessary modifications for China region compatibility
3. Deploy the solution using the minimum resources necessary
4. Validate that the deployment works as expected
5. Clean up all resources after validation

Important constraints:
- Maximum cost limit: $max_cost USD
- Use the smallest/cheapest resource sizes possible
- Set short timeouts and TTLs for all resources
- Ensure all resources are properly tagged for tracking
- Clean up ALL resources after validation

Provide your final output in this JSON format:
{
  "validation_type": "project_deployment",
  "agent_used": "project_deployment_agent",
  "validation_results": {
    "project_analysis": {
      "repository": "URL",
      "branch": "main",
      "prerequisites": ["list", "of", "prerequisites"],
      "compatibility_concerns": ["list", "of", "concerns"]
    },
    "china_compatibility": {
      "required_modifications": ["list", "of", "modifications"],
      "unavailable_services": ["list", "of", "unavailable", "services"],
      "alternative_solutions": ["list", "of", "alternatives"]
    },
    "deployment_solution": {
      "modified_files": ["list", "of", "modified", "files"],
      "deployment_steps": ["step1", "step2", "..."],
      "validation_results": ["result1", "result2", "..."],
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
- Do not attempt to deploy solutions that are clearly incompatible with China regions
- Document all assumptions made during deployment
- If a service is not available in China regions, note it as a blocker
- Always verify IAM permissions before deployment
- Follow AWS China region best practices for networking and security
- Clean up ALL resources after validation

Begin your analysis now.
EOF
)

    # Execute project validation
    log_info "Analyzing and validating GitHub project, this may take some time..."
    echo -e "$project_validation_prompt" | q chat --no-interactive --trust-tools=use_aws,fs_write,fs_read,execute_bash > /dev/null

    # Check if result file was generated
    if [ ! -f "$deep_result_file" ]; then
        log_error "Project validation failed, result file was not generated"
        return 1
    fi

    log_success "Project validation complete! Results saved to: $deep_result_file"
    
    # Clean up project directory
    rm -rf "$project_dir"
    
    return 0
}

# If script is run directly (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Check for required parameters
    if [ $# -lt 7 ]; then
        log_error "Usage: $0 <github_url> <basic_result_file> <deep_result_file> <region> <profile> <max_cost> <temp_dir>"
        exit 1
    fi
    
    # Execute project validation
    execute_project_validation "$1" "$2" "$3" "$4" "$5" "$6" "$7"
    exit $?
fi
