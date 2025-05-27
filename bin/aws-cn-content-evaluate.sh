#!/bin/bash

# aws-cn-content-evaluate.sh - Check content applicability for AWS China regions
# Author: Amazon Q
# Usage: ./aws-cn-content-evaluate.sh -i <validation results JSON> -o <applicability report JSON>

# Import common functions
source $(dirname "$0")/aws-cn-common-utils.sh

# Default values
VALIDATION_RESULTS=""
OUTPUT_REPORT=""
THRESHOLD=70  # Default threshold score for applicability (0-100)

# Display help information
show_help() {
    echo "Usage: $0 -i <validation results JSON> -o <applicability report JSON> [-t <threshold>]"
    echo
    echo "Description:"
    echo "  Evaluates the applicability of AWS content for China regions based on"
    echo "  service validation results. Generates a detailed applicability report."
    echo
    echo "Parameters:"
    echo "  -i, --input     Validation results JSON file (required)"
    echo "  -o, --output    Output applicability report JSON file (required)"
    echo "  -t, --threshold Applicability threshold score (0-100, default: 70)"
    echo "  -h, --help      Display this help information"
    echo
    echo "Examples:"
    echo "  $0 -i ./data/aws-article-validation-results.json -o ./data/aws-article-applicability.json"
    echo "  $0 -i ./data/aws-article-validation-results.json -o ./data/aws-article-applicability.json -t 80"
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -i|--input)
            VALIDATION_RESULTS="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_REPORT="$2"
            shift 2
            ;;
        -t|--threshold)
            THRESHOLD="$2"
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
if [ -z "$VALIDATION_RESULTS" ] || [ -z "$OUTPUT_REPORT" ]; then
    log_error "Validation results and output report file must be provided"
    show_help
    exit 1
fi

# Check if input file exists
if [ ! -f "$VALIDATION_RESULTS" ]; then
    log_error "Input file '$VALIDATION_RESULTS' does not exist"
    exit 1
fi

# Validate threshold value
if ! [[ "$THRESHOLD" =~ ^[0-9]+$ ]] || [ "$THRESHOLD" -lt 0 ] || [ "$THRESHOLD" -gt 100 ]; then
    log_error "Threshold must be a number between 0 and 100"
    exit 1
fi

# Create output directory if it doesn't exist
OUTPUT_DIR=$(dirname "$OUTPUT_REPORT")
mkdir -p "$OUTPUT_DIR"

# Read the validation results
log_info "Reading validation results from $VALIDATION_RESULTS"
RESULTS_JSON=$(cat "$VALIDATION_RESULTS")

# Build prompt for Amazon Q
log_info "Evaluating content applicability for AWS China regions..."
PROMPT=$(cat << EOF
# AWS China Region Content Applicability Evaluation

## Task Overview
Evaluate the applicability of AWS technical content for China regions based on service validation results.

## Input Data
The following JSON contains validation results for AWS services in China regions:

\`\`\`json
$RESULTS_JSON
\`\`\`

## Required Tasks

1. Analyze the validation results to determine content applicability:
   - Evaluate the availability of core services in China regions
   - Assess the impact of any unavailable services or features
   - Consider alternatives for unavailable services
   - Calculate an overall applicability score (0-100)

2. Generate a comprehensive applicability report in JSON format with this structure:
\`\`\`json
{
  "applicability_metadata": {
    "content_title": "Original content title",
    "evaluation_timestamp": "Current timestamp",
    "threshold_score": $THRESHOLD
  },
  "applicability_assessment": {
    "overall_score": 0,
    "is_applicable": true|false,
    "summary": "Brief summary of applicability assessment"
  },
  "service_assessments": [
    {
      "service_name": "Service name from validation results",
      "importance": "core|auxiliary",
      "available_in_china": true|false,
      "impact_level": "high|medium|low|none",
      "alternatives": "Suggested alternatives if not available",
      "adaptation_required": "Description of adaptations needed"
    }
  ],
  "decision_factors": [
    {
      "factor": "Factor name (e.g., 'Core service availability')",
      "weight": 0,
      "score": 0,
      "details": "Explanation of the score"
    }
  ],
  "recommendations": {
    "proceed": true|false,
    "justification": "Explanation of the recommendation",
    "adaptation_steps": [
      "Step 1: Description",
      "Step 2: Description"
    ]
  }
}
\`\`\`

3. Important guidelines:
   - Set "is_applicable" to true if the overall score is >= $THRESHOLD, otherwise false
   - Weight core services more heavily than auxiliary services
   - Consider both the quantity and importance of unavailable services
   - Provide actionable recommendations for adaptation if applicable
   - Be thorough in your analysis and clear in your explanations

4. Write the final applicability report to $OUTPUT_REPORT

Provide a comprehensive assessment that helps users decide whether to proceed with content adaptation.
EOF
)

# Execute Amazon Q CLI
log_info "Generating applicability report..."
printf "%s" "$PROMPT" | q chat --no-interactive --trust-all-tools > /dev/null 2>&1

# Check if the output file exists to confirm success
if [ -f "$OUTPUT_REPORT" ]; then
    log_success "Evaluation complete! Applicability report has been saved to: $OUTPUT_REPORT"
    
    # Extract and display the key results
    if command_exists jq; then
        IS_APPLICABLE=$(jq -r '.applicability_assessment.is_applicable' "$OUTPUT_REPORT")
        SCORE=$(jq -r '.applicability_assessment.overall_score' "$OUTPUT_REPORT")
        SUMMARY=$(jq -r '.applicability_assessment.summary' "$OUTPUT_REPORT")
        
        if [ "$IS_APPLICABLE" = "true" ]; then
            log_success "Content is applicable for AWS China regions (Score: $SCORE)"
        else
            log_warning "Content is NOT applicable for AWS China regions (Score: $SCORE)"
        fi
        
        log_info "Summary: $SUMMARY"
    else
        log_info "Applicability report generated. Please review the report for details."
    fi
else
    log_error "Evaluation failed or output file was not created."
    exit 1
fi
