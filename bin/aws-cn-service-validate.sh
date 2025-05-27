#!/bin/bash

# aws-cn-service-validate.sh - Generate interactive AWS CLI commands to validate service availability
# Usage: ./aws-cn-service-validate.sh -i <input JSON file> -o <output commands file> -r <region>

# Import common functions
source $(dirname "$0")/aws-cn-common-utils.sh

# Default values
INPUT_JSON=""
OUTPUT_COMMANDS=""
REGION="cn-north-1"  # 默认使用北京区域
PROFILE="cn"  # 默认使用cn profile

# Display help information
show_help() {
    echo "Usage: $0 -i <input JSON file> -o <output commands file> [-r <region>] [-p <profile>]"
    echo
    echo "Parameters:"
    echo "  -i, --input     Input JSON file with identified services (required)"
    echo "  -o, --output    Output file for generated interactive commands (required)"
    echo "  -r, --region    AWS China region to test (default: cn-north-1)"
    echo "  -p, --profile   AWS CLI profile to use (default: cn)"
    echo "  -h, --help      Display this help information"
    echo
    echo "Examples:"
    echo "  $0 -i ./data/services.json -o ./data/interactive_validation.sh -r cn-north-1 -p cn"
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -i|--input)
            INPUT_JSON="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_COMMANDS="$2"
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
if [ -z "$INPUT_JSON" ] || [ -z "$OUTPUT_COMMANDS" ]; then
    log_error "Input JSON and output commands file must be provided"
    show_help
    exit 1
fi

# Check if input file exists
if [ ! -f "$INPUT_JSON" ]; then
    log_error "Input file '$INPUT_JSON' does not exist"
    exit 1
fi

# Create output directory if it doesn't exist
OUTPUT_DIR=$(dirname "$OUTPUT_COMMANDS")
mkdir -p "$OUTPUT_DIR"

# Read the input JSON
SERVICES_JSON=$(cat "$INPUT_JSON")

# Build prompt for Amazon Q
log_info "Generating interactive AWS CLI validation script for $REGION region using profile $PROFILE..."
PROMPT=$(cat << EOF
# AWS China Region Service Validation Commands Generator

## Task Overview
Generate an interactive shell script that will prompt the user for confirmation before executing each AWS CLI command to validate service availability in China regions.

## Input Data
The following JSON contains AWS services identified in technical content:

\`\`\`json
$SERVICES_JSON
\`\`\`

## Required Tasks

1. For each service in the "identified_services" list:
   - Design a simple, read-only AWS CLI command to test its availability in the $REGION region
   - Include the "--profile $PROFILE" parameter in each command
   - Create an interactive prompt that shows the command and asks for user confirmation (y/n) before execution
   - Provide a brief explanation of what the command does and how to interpret its results

2. Generate a shell script with the following structure:
\`\`\`bash
#!/bin/bash
# Interactive AWS Service Validation for China Region
# Generated for: [Original content title]
# Region: $REGION
# Profile: $PROFILE
# Date: [Current date]

# Function to execute command after confirmation
execute_command() {
    local cmd="\$1"
    local description="\$2"
    local expected_output="\$3"
    
    echo "=== Command ==="
    echo "\$cmd"
    echo
    echo "=== Purpose ==="
    echo "\$description"
    echo
    echo "=== Expected successful output ==="
    echo "\$expected_output"
    echo
    
    read -p "Execute this command? (y/n): " confirm
    if [[ \$confirm == [yY] || \$confirm == [yY][eE][sS] ]]; then
        echo "Executing command..."
        eval "\$cmd"
        echo
        echo "Command executed. Review the output above."
        read -p "Press Enter to continue..."
    else
        echo "Command skipped."
    fi
    echo
    echo "----------------------------------------------"
    echo
}

echo "=== AWS Service Validation for China Region ==="
echo "This script will help validate AWS service availability in the $REGION region."
echo "You will be prompted for confirmation before each command is executed."
echo "All commands are read-only operations and should not modify any resources."
echo
echo "----------------------------------------------"
echo

# [Service Name]
echo "=== Testing [Service Name] ==="
execute_command \\
    "aws [service] [command] --region $REGION --profile $PROFILE" \\
    "[Brief explanation of what this command tests]" \\
    "[What success looks like]"

# [Next Service]
...

echo "=== Validation Complete ==="
echo "Review the outputs above to determine service availability in AWS China regions."
echo "Remember that some services may have different feature sets or limitations in China regions."
\`\`\`

3. Important guidelines:
   - Use only read-only operations (describe, list, get) to avoid modifying resources
   - ALWAYS include "--profile $PROFILE" and "--region $REGION" in every AWS CLI command
   - For each service, choose the simplest possible command that confirms availability
   - Include helpful comments about how to interpret the results
   - Make the script user-friendly with clear prompts and explanations

4. Write the generated interactive script to $OUTPUT_COMMANDS

Be thorough in your analysis and provide clear instructions for each validation step.
EOF
)

# Execute Amazon Q CLI
printf "%s" "$PROMPT" | q chat --no-interactive --trust-all-tools > /dev/null 2>&1

# Check if the output file exists to confirm success
if [ -f "$OUTPUT_COMMANDS" ]; then
    log_success "Script generation complete! Interactive validation script has been saved to: $OUTPUT_COMMANDS"
    chmod +x "$OUTPUT_COMMANDS"
    log_info "You can run it with: $OUTPUT_COMMANDS"
else
    log_error "Script generation failed or output file was not created."
    exit 1
fi
