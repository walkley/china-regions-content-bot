#!/bin/bash

# aws-cn-tool.sh - AWS China Region Content Validation Tool
# Author: Amazon Q

# Import common utilities
source common-utils.sh

# Display help information
show_help() {
    echo "AWS China Region Content Validation Tool"
    echo "Usage: $0 -u <blog URL> [-r <region>] [-p <profile>]"
    echo
    echo "Parameters:"
    echo "  -u, --url       Blog URL (required)"
    echo "  -r, --region    AWS China region (default: cn-northwest-1)"
    echo "  -p, --profile   AWS CLI profile (default: cn)"
    echo "  -h, --help      Display this help information"
    echo
    echo "Examples:"
    echo "  $0 -u https://aws.amazon.com/blogs/aws/some-article -r cn-north-1 -p cn"
}

# Default values
URL=""
REGION="cn-northwest-1"
PROFILE="cn"
TEMP_DIR="./data/temp"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
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
if [ -z "$URL" ]; then
    log_error "Blog URL must be provided"
    show_help
    exit 1
fi

# Create temporary and results directories
mkdir -p "$TEMP_DIR"
mkdir -p "./data"
TEMP_MD="$TEMP_DIR/content.md"
RESULT_FILE="./data/$(basename "$URL" | sed 's/[^a-zA-Z0-9]/_/g')_result.json"

# Step 1: Convert blog content to Markdown
log_info "Step 1: Converting blog content to Markdown..."
CONVERT_PROMPT="Please use the convert_to_markdown tool to extract content from the following URL, then clean it to keep only the main article content (excluding navigation menus, headers, footers, sidebars, ads, and other non-core content), and save the result as Markdown format to $TEMP_MD:

URL: $URL

Processing steps:
1. Use the convert_to_markdown tool to get the complete webpage content
2. Extract and keep the core content of the article (title, body text, image links, and tables)
3. Remove all navigation menus, headers, footers, sidebars, ads, and comment sections
4. Maintain the original heading hierarchy and formatting
5. IMPORTANT: Do NOT translate any content - keep the original language exactly as it appears
6. Save the cleaned content to the specified Markdown file

Output requirements: Clean Markdown file containing only the main article content in its original language"

echo -e "$CONVERT_PROMPT" | q chat --no-interactive --trust-tools=fs_write,fs_read,markitdown_mcp___convert_to_markdown > /dev/null

# Check if Markdown file was generated
if [ ! -f "$TEMP_MD" ]; then
    log_error "Conversion failed, Markdown file was not generated"
    exit 1
fi

log_success "Blog content has been converted to Markdown format"

# Step 2: Analyze, validate, and evaluate in one step
log_info "Step 2: Analyzing content and validating service availability..."

# Read Markdown content
CONTENT=$(cat "$TEMP_MD")

# Read unavailable services list
UNAVAILABLE_SERVICES=$(cat ./unavailable_services.txt)

# Build validation prompt
VALIDATION_PROMPT=$(cat << EOF
You are an AWS China Region service availability validator. Your task is to analyze AWS technical content and determine if it can be implemented in AWS China regions (cn-north-1, cn-northwest-1) based on service availability.

First, here is the list of services that are unavailable in AWS China regions:
<unavailable_services>
$UNAVAILABLE_SERVICES
</unavailable_services>

Here is the technical content to analyze:
<tech_content>
$CONTENT
</tech_content>

Follow these steps to validate the content:

1. Carefully read through the technical content and identify all AWS services mentioned. Include both explicitly stated services and those implied by resource types or APIs mentioned.

2. For each identified service:
   a. Check if it appears in the unavailable_services list
   b. If not in the unavailable list, use the use_aws tool in China region '$REGION' with profile name '$PROFILE' to validate specific feature availability:
      - Only use read-only operations (list, get, describe)
      - Example: aws servicename list-features --region $REGION --profile $PROFILE
   c. Record whether each service is available or unavailable

3. Calculate the feasibility assessment:
   - HIGH: All identified services are available
   - MODERATE: >70% of services available with workarounds possible
   - LOW: <70% of services available, requiring major changes

4. Format your response as a JSON object with these fields:
   - identified_services: Array of all AWS services found
   - service_validation_results:
     - available: Array of available services
     - unavailable: Array of unavailable services
   - feasibility_assessment:
     - level: "high", "moderate", or "low"
     - reasoning: Brief explanation of impact
     - confidence: Number between 0 and 1

Before providing your final answer, use <scratchpad> tags to:
1. List out each service you identified
2. Show your availability calculations
3. Draft your reasoning for the feasibility assessment

Write your final JSON result directly to this file: $RESULT_FILE
Make sure the JSON is properly formatted and valid.

Example JSON format to write to file:
{
    "identified_services": ["S3", "Lambda", "DynamoDB"],
    "service_validation_results": {
        "available": ["S3", "Lambda"],
        "unavailable": ["DynamoDB"]
    },
    "feasibility_assessment": {
        "level": "low",
        "reasoning": "Core service DynamoDB unavailable requiring architectural redesign",
        "confidence": 0.9
    }
}

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
echo -e "$VALIDATION_PROMPT" | q chat --no-interactive --trust-tools=use_aws,fs_write > /dev/null

# Check if result file was generated
if [ ! -f "$RESULT_FILE" ]; then
    log_error "Analysis failed, result file was not generated"
    exit 1
fi

# Display result summary
log_success "Analysis complete! Results saved to: $RESULT_FILE"

# Extract key information and display
if command_exists jq; then
    LEVEL=$(jq -r '.feasibility_assessment.level' "$RESULT_FILE" 2>/dev/null)
    REASONING=$(jq -r '.feasibility_assessment.reasoning' "$RESULT_FILE" 2>/dev/null)
else
    LEVEL=$(grep -o '"level": *"[^"]*"' "$RESULT_FILE" | head -1 | cut -d'"' -f4)
    REASONING=$(grep -o '"reasoning": *"[^"]*"' "$RESULT_FILE" | head -1 | cut -d'"' -f4)
fi

echo
echo "===== Analysis Result Summary ====="
echo "Applicability Rating: $LEVEL"
echo "Reason: $REASONING"
echo

# Clean up temporary files
rm -f "$TEMP_MD"

log_info "Complete results saved to: $RESULT_FILE"
