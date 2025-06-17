#!/usr/bin/env python3
"""
AWS China Region Content Validation Tool

This tool validates AWS global region technical content for compatibility with AWS China regions.
It analyzes content to determine if services, features, and architectures can be implemented
in AWS China regions (cn-north-1, cn-northwest-1).
"""

import argparse
import logging
import os
import sys
import uuid
from pathlib import Path

# Import functions from converter.py and validator.py
from src.converter import convert_url_to_markdown
from src.validator import validate_content

# Set up logging
def setup_logging(log_level="INFO"):
    """Set up basic logging configuration."""
    logging_level = getattr(logging, log_level.upper())
    logging.basicConfig(
        level=logging_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger("aws-validator")

# Parse command line arguments
def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="AWS China Region Content Validation Tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Required arguments
    parser.add_argument("-u", "--url", help="URL of the content to validate")
    
    # AWS configuration
    parser.add_argument("-r", "--region", default="cn-northwest-1", 
                      help="AWS China region to use for validation")
    parser.add_argument("-p", "--profile", default="cn", 
                      help="AWS CLI profile with China region credentials")
    parser.add_argument("--log-level", default="INFO",
                      help="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)")
    
    return parser.parse_args()
   
def sanitize_filename(url):
    """Generate safe filename from URL"""
    url_basename = os.path.basename(url.rstrip("/"))
    return ''.join(c if c.isalnum() else '_' for c in url_basename)

def main():
    """Main entry point for the AWS China Region Content Validation Tool."""
    # Parse command line arguments
    config = parse_args()
    if not config.url:
        print("URL is required. Use -u/--url to specify the content URL.")
        return 1

    # Set up logging
    logger = setup_logging(config.log_level)

    # Generate a unique execution ID
    validation_id = str(uuid.uuid4())[:8]

    # Create data directory
    Path("./data").mkdir(exist_ok=True)
    
    # Generate file names based on URL
    safe_filename = sanitize_filename(config.url)
    
    try:
        logger.info(f"Validating {config.url}")
    
        # Step 1: Convert content to Markdown
        markdown = convert_url_to_markdown(config.url)
        markdown_file = f"./data/{safe_filename}_{validation_id}.md"
        with open(markdown_file, "w") as f:
            f.write(markdown)

        # Step 2: Validate content
        result_file = f"./data/{safe_filename}_result_{validation_id}.md"
        log_file = f"./data/{safe_filename}_{validation_id}.log"
        result = validate_content(markdown_file, result_file, log_file, validation_id, config.region, config.profile)
        
        logger.info(f"{'Succeeded' if result.get('success') else 'Failed!'}")
        return 0
    
    except KeyboardInterrupt:
        logger.warning("Process interrupted by user")
        return 130
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())