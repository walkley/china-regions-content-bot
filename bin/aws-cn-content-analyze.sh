#!/bin/bash

# aws-cn-content-analyze.sh - Analyze AWS technical content to identify services and configurations
# Author: Amazon Q
# Usage: ./aws-cn-content-analyze.sh -f <markdown file> -o <output JSON file>

# Import common functions
source $(dirname "$0")/aws-cn-common-utils.sh

# Function to display help information
show_help() {
    echo "Usage: $0 [options]"
    echo
    echo "Description:"
    echo "  Analyzes AWS technical content in a Markdown file to identify AWS services,"
    echo "  resources, configurations, and their dependencies."
    echo
    echo "Options:"
    echo "  -f, --file FILE        Path to the Markdown file containing AWS technical content (required)"
    echo "  -o, --output FILE      Path to output JSON file (required)"
    echo "  -h, --help             Display this help message and exit"
    echo
    echo "Example:"
    echo "  $0 --file ./data/aws-article.md --output ./data/aws-article-services.json"
}

# Check if no arguments provided
if [ $# -eq 0 ]; then
    show_help
    exit 1
fi

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -h|--help)
            show_help
            exit 0
            ;;
        -f|--file)
            CONTENT_FILE="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_JSON="$2"
            shift 2
            ;;
        *)
            log_error "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
done

# Validate required parameters
if [ -z "$CONTENT_FILE" ]; then
    log_error "Content file path is required"
    show_help
    exit 1
fi

if [ ! -f "$CONTENT_FILE" ]; then
    log_error "Content file '$CONTENT_FILE' does not exist"
    exit 1
fi

if [ -z "$OUTPUT_JSON" ]; then
    log_error "Output JSON file path is required"
    show_help
    exit 1
fi

# Create output directory if it doesn't exist
OUTPUT_DIR=$(dirname "$OUTPUT_JSON")
mkdir -p "$OUTPUT_DIR"

# Check file size and exit if too large
FILE_SIZE=$(wc -c < "$CONTENT_FILE")
MAX_SIZE=204800  # 200KB in bytes

if [ $FILE_SIZE -gt $MAX_SIZE ]; then
    log_error "File size ($(($FILE_SIZE / 1024)) KB) exceeds maximum allowed size (200KB)"
    exit 1
fi

# Read file content
log_info "Reading content from $CONTENT_FILE"
CONTENT=$(cat "$CONTENT_FILE")

# Create prompt with embedded content
log_info "Analyzing content for AWS services and configurations..."
PROMPT=$(cat << EOF
# AWS Service Identification and Analysis

## Task Overview
Analyze the provided AWS technical content to identify all AWS services, resource types, configurations, and dependencies.

## Analysis Parameters
- Output: Write a comprehensive JSON service inventory to $OUTPUT_JSON

## Content to Analyze

===CONTENT_START===
$CONTENT
===CONTENT_END===

## Required Analysis Tasks

1. Identify all AWS services and resources
   - Service names and API versions
   - Importance classification (core/auxiliary)
   - Usage context within the document

2. Extract configuration parameters
   - Region identifiers
   - Service endpoints
   - ARN formats and examples
   - Account IDs
   - Key configuration options

3. Catalog all code snippets
   - Language and type (CloudFormation, Terraform, SDK)
   - Location within document
   - Key configurations present in code

4. Map service dependencies
   - Service-to-service relationships
   - Dependency types (triggers, data flow, etc.)

5. Generate JSON output to $OUTPUT_JSON with this structure:
\`\`\`json
{
  "content_metadata": {
    "title": "Title extracted from content",
    "type": "Content type determined from analysis"
  },
  "identified_services": [
    {
      "service_name": "Service Name",
      "importance": "core|auxiliary",
      "usage_context": "Description of how the service is used",
      "configurations": [
        {
          "type": "parameter_type",
          "value": "parameter_value",
          "location": "location in document"
        }
      ],
      "code_snippets": [
        {
          "language": "language_name",
          "location": "location in document",
          "purpose": "purpose of code"
        }
      ]
    }
  ],
  "dependencies": [
    {
      "source": "Source Service",
      "target": "Target Service",
      "type": "dependency_type",
      "description": "Description of dependency"
    }
  ]
}
\`\`\`

Be thorough in your analysis, capturing all service references, configurations, and dependencies.
EOF
)

# Execute Amazon Q CLI
log_info "Executing content analysis task..."
printf "%s" "$PROMPT" | q chat --no-interactive --trust-all-tools > /dev/null 2>&1

# Check if the output file exists
if [ -f "$OUTPUT_JSON" ]; then
    log_success "Analysis complete! Results saved to $OUTPUT_JSON"
    
    # Display summary of identified services
    SERVICE_COUNT=$(grep -o '"service_name"' "$OUTPUT_JSON" | wc -l)
    log_info "Identified $SERVICE_COUNT AWS services in the content"
else
    log_error "Analysis failed or output file was not created"
    exit 1
fi
