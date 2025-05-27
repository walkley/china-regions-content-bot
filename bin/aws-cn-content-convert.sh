#!/bin/bash

# aws-cn-content-convert.sh - Convert blog links to Markdown files
# Author: Amazon Q
# Usage: ./aws-cn-content-convert.sh -u <blog URL> -o <output file path>

# Import common functions
source $(dirname "$0")/aws-cn-common-utils.sh

# Default values
URL=""
OUTPUT=""

# Display help information
show_help() {
    echo "Usage: $0 -u <blog URL> -o <output file path>"
    echo
    echo "Description:"
    echo "  Converts a blog post or web article to clean Markdown format,"
    echo "  removing navigation, headers, footers, and other non-content elements."
    echo
    echo "Parameters:"
    echo "  -u, --url      Blog URL to convert (required)"
    echo "  -o, --output   Output Markdown file path (required)"
    echo "  -h, --help     Display this help information"
    echo
    echo "Examples:"
    echo "  $0 -u https://aws.amazon.com/blogs/aws/some-article -o ./data/aws-article.md"
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -u|--url)
            URL="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT="$2"
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
if [ -z "$URL" ] || [ -z "$OUTPUT" ]; then
    log_error "URL and output file path must be provided"
    show_help
    exit 1
fi

# Create output directory if it doesn't exist
OUTPUT_DIR=$(dirname "$OUTPUT")
if [ ! -d "$OUTPUT_DIR" ]; then
    log_info "Creating output directory: $OUTPUT_DIR"
    mkdir -p "$OUTPUT_DIR"
fi

# Build prompt
log_info "Converting blog: $URL"
PROMPT="Please use the convert_to_markdown tool to extract content from the following URL, then clean it to keep only the main article content (excluding navigation menus, headers, footers, sidebars, ads, and other non-core content), and save the result as Markdown format to $OUTPUT:

URL: $URL

Processing steps:
1. Use the convert_to_markdown tool to get the complete webpage content
2. Extract and keep the core content of the article (title, body text, image links, and tables)
3. Remove all navigation menus, headers, footers, sidebars, ads, and comment sections
4. Maintain the original heading hierarchy and formatting
5. IMPORTANT: Do NOT translate any content - keep the original language exactly as it appears
6. Save the cleaned content to the specified Markdown file

Output requirements: Clean Markdown file containing only the main article content in its original language"

# Execute Q CLI with suppressed standard output
log_info "Converting blog to Markdown..."
echo -e "$PROMPT" | q chat --no-interactive --trust-tools=fs_write,fs_read,markitdown_mcp___convert_to_markdown > /dev/null 2>&1

# Check if the output file exists to confirm success
if [ -f "$OUTPUT" ]; then
    log_success "Conversion complete! Markdown file has been saved to: $OUTPUT"
else
    log_error "Conversion failed or output file was not created."
    exit 1
fi
