#!/bin/bash

# content-converter.sh - Convert blog content to Markdown
# Author: Amazon Q

# Import common utilities
source src/common-utils.sh

# Function to convert blog content to Markdown
convert_content_to_markdown() {
    local url="$1"
    local output_file="$2"
    
    log_info "Converting blog content to Markdown..."
    
    # Build conversion prompt
    local convert_prompt="Please use the convert_to_markdown tool to extract content from the following URL, then clean it to keep only the main article content (excluding navigation menus, headers, footers, sidebars, ads, and other non-core content), and save the result as Markdown format to $output_file:

URL: $url

Processing steps:
1. Use the convert_to_markdown tool to get the complete webpage content
2. Extract and keep the core content of the article (title, body text, image links, and tables)
3. Remove all navigation menus, headers, footers, sidebars, ads, and comment sections
4. Maintain the original heading hierarchy and formatting
5. IMPORTANT: Do NOT translate any content - keep the original language exactly as it appears
6. Save the cleaned content to the specified Markdown file

Output requirements: Clean Markdown file containing only the main article content in its original language"

    # Execute conversion
    echo -e "$convert_prompt" | q chat --no-interactive --trust-tools=fs_write,fs_read,execute_bash,markitdown_mcp___convert_to_markdown

    # Check if Markdown file was generated
    if [ ! -f "$output_file" ]; then
        log_error "Conversion failed, Markdown file was not generated"
        return 1
    fi

    log_success "Blog content has been converted to Markdown format"
    return 0
}

# If script is run directly (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    # Check for required parameters
    if [ $# -lt 2 ]; then
        log_error "Usage: $0 <blog URL> <output file>"
        exit 1
    fi
    
    # Convert content
    convert_content_to_markdown "$1" "$2"
    exit $?
fi
