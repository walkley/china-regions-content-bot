#!/usr/bin/env python3
"""
AWS China Region Content Validation Tool

This tool validates AWS global region technical content for compatibility with AWS China regions.
It analyzes content to determine if services, features, and architectures can be implemented
in AWS China regions (cn-north-1, cn-northwest-1).
"""

import argparse
import json
import logging
import os
import re
import subprocess
import sys
import uuid
from pathlib import Path
from dotenv import load_dotenv

# Set up logging
def setup_logging(log_level="INFO"):
    """Set up basic logging configuration."""
    logging_level = getattr(logging, log_level.upper())
    logging.basicConfig(
        level=logging_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger("aws-validator")

# Load configuration from environment and arguments
def load_config(args):
    """Load configuration from environment variables and command line arguments."""
    # Define config with command line args, falling back to env vars or defaults
    return {
        "url": args.url or os.environ.get("AWS_VALIDATOR_URL"),
        "region": args.region or os.environ.get("AWS_VALIDATOR_REGION", "cn-northwest-1"),
        "profile": args.profile or os.environ.get("AWS_VALIDATOR_PROFILE", "cn"),
        "deep_mode": args.deep if args.deep is not None else os.environ.get("AWS_VALIDATOR_DEEP_MODE", "").lower() in ["true", "1", "yes"],
        "max_cost": args.max_cost if args.max_cost is not None else float(os.environ.get("AWS_VALIDATOR_MAX_COST", "10.0")),
        "force_regenerate": args.force if args.force is not None else os.environ.get("AWS_VALIDATOR_FORCE_REGENERATE", "").lower() in ["true", "1", "yes"],
        "content_type": args.content_type or os.environ.get("AWS_VALIDATOR_CONTENT_TYPE"),
        "temp_dir": args.temp_dir or os.environ.get("AWS_VALIDATOR_TEMP_DIR", "./data/temp")
    }

# File operations
def file_exists(file_path):
    """Check if a file exists."""
    return Path(file_path).is_file()

def read_file(file_path):
    """Read a file and return its contents."""
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return None

def write_file(file_path, content):
    """Write content to a file."""
    try:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        logging.error(f"Error writing to file {file_path}: {e}")
        return False

def read_json(file_path):
    """Read a JSON file and return its contents."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error reading JSON file {file_path}: {e}")
        return None

def write_json(file_path, data):
    """Write data to a JSON file."""
    try:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        logging.error(f"Error writing to JSON file {file_path}: {e}")
        return False

# Run Q chat command
def run_q_chat(prompt, trust_tools=True, timeout=600):
    """Run Amazon Q chat command and handle output."""
    cmd = ["q", "chat"]
    if trust_tools:
        cmd.append("--trust-tools")
    
    try:
        process = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(input=prompt, timeout=timeout)
        
        if process.returncode != 0:
            logging.error(f"Q chat command failed: {stderr}")
            return {"success": False, "error": stderr, "output": stdout}
        
        return {"success": True, "output": stdout}
    except subprocess.TimeoutExpired:
        process.kill()
        logging.error(f"Q chat command timed out after {timeout} seconds")
        return {"success": False, "error": f"Command timed out after {timeout} seconds"}
    except Exception as e:
        logging.error(f"Error running Q chat command: {e}")
        return {"success": False, "error": str(e)}

# Convert content to Markdown
def convert_content(url, output_file, force_regenerate=False):
    """Convert web content to Markdown format."""
    if file_exists(output_file) and not force_regenerate:
        logging.info(f"Using cached content file: {output_file}")
        return {"success": True, "file_path": output_file}
    
    logging.info(f"Converting content from URL: {url}")
    
    prompt = f"""Please convert the AWS technical content at {url} to clean Markdown format.
    Remove any non-essential elements like navigation, footers, and sidebars.
    Focus on preserving the main content, code examples, and technical information.
    Format the output as valid Markdown with proper headings, code blocks, and formatting.
    
    Write the converted content directly to this file: {output_file}"""
    
    result = run_q_chat(prompt, trust_tools=True, timeout=300)
    
    if not result["success"]:
        return {"success": False, "error": result.get("error", "Unknown error")}
    
    if not file_exists(output_file):
        return {"success": False, "error": "Failed to generate content file"}
    
    return {"success": True, "file_path": output_file}

# Perform basic validation
def basic_validate(content_file, result_file, region, profile, force_regenerate=False):
    """Perform basic validation of AWS service availability."""
    if file_exists(result_file) and not force_regenerate:
        logging.info(f"Using cached validation result: {result_file}")
        return {"success": True, "file_path": result_file}
    
    logging.info(f"Performing basic validation for content in {content_file}")
    
    # 获取摘要文件路径
    summary_file = result_file.replace("_result.json", "_summary.txt")
    
    # Read content file
    content = read_file(content_file)
    if not content:
        return {"success": False, "error": f"Could not read content file: {content_file}"}
    
    # Read unavailable services list
    unavailable_services_path = os.path.join("data", "unavailable_services.txt")
    unavailable_services = read_file(unavailable_services_path)
    
    if not unavailable_services:
        logging.warning("Could not read unavailable services list, proceeding without it")
        unavailable_services = ""
    
    prompt = f"""You are an AWS China Region service availability validator. Your task is to analyze AWS technical content and determine if it can be implemented in AWS China regions (cn-north-1, cn-northwest-1) based on service availability.

First, here is the list of services that are unavailable in AWS China regions:
<unavailable_services>
{unavailable_services}
</unavailable_services>

Here is the technical content to analyze:
<tech_content>
{content}
</tech_content>

Follow these steps to validate the content:

1. Carefully read through the technical content and identify all AWS services mentioned.
2. For each identified service, check if it appears in the unavailable_services list.
3. Analyze the content to identify any GitHub project URLs or step-by-step procedures.
4. Calculate the feasibility assessment:
   - HIGH: All identified services are available
   - MODERATE: >70% of services available with workarounds possible
   - LOW: <70% of services available, requiring major changes

You need to create two outputs:

1. First, write a concise summary of your findings to this file: {summary_file}
   Format the summary as a clear, user-friendly report with:
   - A headline showing the feasibility level (HIGH/MODERATE/LOW)
   - Brief explanation of the assessment
   - Number of available and unavailable services
   - Content type (GitHub Project, Tutorial, or Documentation)
   - List of unavailable services (if any)
   - Use clear formatting with separators and bullet points

2. Second, write your detailed analysis as a JSON object to this file: {result_file}
   Include these fields:
   - content_analysis: identified_services, dependencies, github_project, procedures
   - service_validation_results: available and unavailable services
   - feasibility_assessment: level, reasoning, confidence

Make sure both files are properly formatted."""

    result = run_q_chat(prompt, trust_tools=True, timeout=600)
    
    if not result["success"]:
        return {"success": False, "error": result.get("error", "Unknown error")}
    
    # 检查JSON文件是否已生成
    if not file_exists(result_file):
        return {"success": False, "error": "Result file was not generated"}
    
    return {"success": True, "file_path": result_file}

# Display basic validation results
def display_basic_results(result_file):
    """Display basic validation results."""
    # 获取对应的摘要文件路径
    summary_file = result_file.replace("_result.json", "_summary.txt")
    
    # 如果摘要文件存在，直接显示
    if file_exists(summary_file):
        try:
            with open(summary_file, 'r') as f:
                print(f.read())
            return True
        except Exception as e:
            logging.error(f"Error reading summary file: {e}")
    
    # 如果摘要文件不存在，但JSON文件存在，显示简单消息
    if file_exists(result_file):
        print(f"\n验证结果已保存到: {result_file}")
        print("摘要文件不存在，请查看JSON结果获取详细信息。")
        return True
    
    logging.error(f"结果文件不存在: {result_file}")
    return False

# Perform deep validation
def deep_validate(content_file, basic_result_file, deep_result_file, region, profile, max_cost, temp_dir, content_type=None, force_regenerate=False):
    """Perform deep validation based on content type."""
    if file_exists(deep_result_file) and not force_regenerate:
        logging.info(f"Using cached deep validation result: {deep_result_file}")
        return {"success": True, "file_path": deep_result_file}
    
    # Read basic validation results
    basic_results = read_json(basic_result_file)
    if not basic_results:
        return {"success": False, "error": f"Could not read basic validation results: {basic_result_file}"}
    
    # Check feasibility level
    feasibility = basic_results.get("feasibility_assessment", {}).get("level", "").lower()
    if feasibility == "low":
        logging.warning("Feasibility level is LOW. Deep validation may not be effective.")
        # Continue anyway as requested
    
    # Determine content type if not specified
    if not content_type:
        content_analysis = basic_results.get("content_analysis", {})
        github_project = content_analysis.get("github_project", "")
        has_procedures = len(content_analysis.get("procedures", [])) > 0
        
        if github_project:
            content_type = "project"
        elif has_procedures:
            content_type = "tutorial"
        else:
            content_type = "tutorial"  # Default to tutorial for documentation/articles
    
    logging.info(f"Performing deep validation as {content_type} type")
    
    # Read content file
    content = read_file(content_file)
    if not content:
        return {"success": False, "error": f"Could not read content file: {content_file}"}
    
    # Create temp directory if it doesn't exist
    Path(temp_dir).mkdir(parents=True, exist_ok=True)
    
    # Generate a unique ID for this validation
    validation_id = str(uuid.uuid4())[:8]
    
    if content_type == "project":
        # Extract GitHub URL from basic results
        github_url = basic_results.get("content_analysis", {}).get("github_project", "")
        if not github_url:
            return {"success": False, "error": "No GitHub project URL found in basic validation results"}
        
        prompt = f"""Please validate if this GitHub project can be deployed in AWS China regions.

GitHub URL: {github_url}
Target Region: {region}
AWS Profile: {profile}
Maximum Cost: ${max_cost} USD

1. Clone the repository and analyze the deployment requirements
2. Attempt to deploy the project in the {region} region using the {profile} profile
3. Tag all created resources with Key=ValidationTest, Value={validation_id}
4. Document any issues encountered during deployment
5. IMPORTANT: Clean up all AWS resources created during validation before completing
   - Make sure to terminate all EC2 instances
   - Delete all S3 buckets created during validation
   - Remove all IAM roles and policies
   - Delete all Lambda functions, API Gateways, and other services
   - Verify no resources remain with the ValidationTest tag

Format your response as a JSON object with validation results and adaptation recommendations.
Write your final JSON result directly to this file: {deep_result_file}"""
    else:  # tutorial or documentation
        prompt = f"""Please validate if this AWS tutorial can be executed in AWS China regions.

<content>
{content}
</content>

Target Region: {region}
AWS Profile: {profile}
Maximum Cost: ${max_cost} USD

1. Extract the step-by-step procedures from the tutorial
2. Attempt to execute each step in the {region} region using the {profile} profile
3. Tag all created resources with Key=ValidationTest, Value={validation_id}
4. Document any issues encountered during execution
5. IMPORTANT: Clean up all AWS resources created during validation before completing
   - Make sure to terminate all EC2 instances
   - Delete all S3 buckets created during validation
   - Remove all IAM roles and policies
   - Delete all Lambda functions, API Gateways, and other services
   - Verify no resources remain with the ValidationTest tag

Format your response as a JSON object with validation results and adaptation recommendations.
Write your final JSON result directly to this file: {deep_result_file}"""
    
    result = run_q_chat(prompt, trust_tools=True, timeout=1800)  # 30 minutes timeout
    
    if not result["success"]:
        return {"success": False, "error": result.get("error", "Unknown error")}
    
    if not file_exists(deep_result_file):
        return {"success": False, "error": "Deep result file was not generated"}
    
    return {"success": True, "file_path": deep_result_file}

# Display deep validation results
def display_deep_results(result_file):
    """Display deep validation results."""
    data = read_json(result_file)
    if not data:
        logging.error(f"Could not read deep result file: {result_file}")
        return False
    
    try:
        # Extract key information from the deep validation results
        validation_status = data.get("validation_status", "UNKNOWN")
        issues = data.get("issues", [])
        recommendations = data.get("recommendations", [])
        
        print("\n" + "=" * 60)
        print("DEEP VALIDATION RESULTS")
        print("=" * 60)
        
        print(f"\nVALIDATION STATUS: {validation_status}")
        
        if issues:
            print("\nISSUES ENCOUNTERED:")
            for i, issue in enumerate(issues, 1):
                print(f"  {i}. {issue}")
        
        if recommendations:
            print("\nRECOMMENDATIONS:")
            for i, rec in enumerate(recommendations, 1):
                print(f"  {i}. {rec}")
        
        print("\n" + "=" * 60)
        print(f"Full results available in: {result_file}")
        print("=" * 60 + "\n")
        
        return True
    except Exception as e:
        logging.error(f"Error displaying deep results: {e}")
        return False

# Check for required dependencies
def check_dependencies():
    """Check for required dependencies."""
    dependencies = [
        {"name": "AWS CLI", "command": ["aws", "--version"]},
        {"name": "Amazon Q CLI", "command": ["q", "--version"]}
    ]
    
    all_ok = True
    for dep in dependencies:
        try:
            result = subprocess.run(dep["command"], capture_output=True, text=True)
            if result.returncode == 0:
                logging.info(f"{dep['name']} is installed: {result.stdout.strip()}")
            else:
                logging.error(f"{dep['name']} check failed: {result.stderr.strip()}")
                all_ok = False
        except FileNotFoundError:
            logging.error(f"{dep['name']} is not installed or not in PATH")
            all_ok = False
    
    return all_ok

# Note: Resource cleanup is handled by the Q chat prompt
# The cleanup_resources function was removed as it was incomplete
# and only checked for EC2 instances without actually cleaning them up
def cleanup_resources(region, profile, validation_id=None):
    """Placeholder for AWS resource cleanup - actual cleanup is handled in Q chat prompt."""
    logging.info(f"Note: AWS resource cleanup is primarily handled in the Q chat prompt")
    logging.info(f"This function only performs a basic check for EC2 resources")
    return True

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
    
    # Validation options
    parser.add_argument("-d", "--deep", action="store_true", 
                      help="Enable deep validation mode")
    parser.add_argument("-m", "--max-cost", type=float, default=10.0, 
                      help="Maximum cost limit for deep validation in USD")
    parser.add_argument("-f", "--force", action="store_true", 
                      help="Force regeneration of cached files")
    parser.add_argument("-t", "--content-type", choices=["project", "tutorial"], 
                      help="Content type for deep validation (auto-detected if not specified)")
    
    # Advanced options
    parser.add_argument("--temp-dir", default="./data/temp", 
                      help="Directory for temporary files")
    parser.add_argument("--cleanup-only", action="store_true",
                      help="Only perform cleanup of validation resources and exit")
    
    # Logging options
    parser.add_argument("--log-level", default="INFO", 
                      choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                      help="Set the logging level")
    
    return parser.parse_args()

# Main function
def main():
    """Main entry point for the AWS China Region Content Validation Tool."""
    # Load environment variables
    load_dotenv()
    
    # Parse command line arguments
    args = parse_args()
    
    # Set up logging
    logger = setup_logging(args.log_level)
    
    # Generate a unique execution ID
    execution_id = str(uuid.uuid4())[:8]
    logger.debug(f"Execution ID: {execution_id}")
    
    # Always check dependencies first
    logger.info("Checking for required dependencies")
    if not check_dependencies():
        logger.error("One or more required dependencies are missing")
        return 1
    
    if args.cleanup_only:
        logger.info("Cleanup functionality is now handled in the Q chat prompts")
        logger.info("This command line option is maintained for backwards compatibility")
        return 0
    
    # Load configuration
    config = load_config(args)
    
    # Validate required configuration
    if not config["url"]:
        logger.error("URL is required. Use -u/--url to specify the content URL.")
        return 1
    
    # Create data directory
    Path("./data").mkdir(exist_ok=True)
    Path(config["temp_dir"]).mkdir(parents=True, exist_ok=True)
    
    # Generate file names based on URL
    url_basename = os.path.basename(config["url"].rstrip("/"))
    safe_filename = ''.join(c if c.isalnum() else '_' for c in url_basename)
    
    md_file = f"./data/{safe_filename}.md"
    result_file = f"./data/{safe_filename}_result.json"
    deep_result_file = f"./data/{safe_filename}_deep_result.json"
    
    try:
        # Step 1: Convert content to Markdown
        logger.info("Step 1: Converting content to Markdown")
        conversion_result = convert_content(
            url=config["url"],
            output_file=md_file,
            force_regenerate=config["force_regenerate"]
        )
        
        if not conversion_result["success"]:
            logger.error(f"Content conversion failed: {conversion_result.get('error', 'Unknown error')}")
            return 1
        
        logger.info(f"Content converted successfully: {conversion_result['file_path']}")
        
        # Step 2: Perform basic validation
        logger.info("Step 2: Performing basic validation")
        validation_result = basic_validate(
            content_file=md_file,
            result_file=result_file,
            region=config["region"],
            profile=config["profile"],
            force_regenerate=config["force_regenerate"]
        )
        
        if not validation_result["success"]:
            logger.error(f"Basic validation failed: {validation_result.get('error', 'Unknown error')}")
            return 1
        
        logger.info(f"Basic validation completed successfully: {validation_result['file_path']}")
        
        # Display basic validation results
        display_basic_results(validation_result['file_path'])
        
        # Step 3: Perform deep validation if enabled
        if config["deep_mode"]:
            logger.info("Step 3: Performing deep validation")
            try:
                deep_result = deep_validate(
                    content_file=md_file,
                    basic_result_file=result_file,
                    deep_result_file=deep_result_file,
                    region=config["region"],
                    profile=config["profile"],
                    max_cost=config["max_cost"],
                    temp_dir=config["temp_dir"],
                    content_type=config["content_type"],
                    force_regenerate=config["force_regenerate"]
                )
                
                if not deep_result["success"]:
                    logger.error(f"Deep validation failed: {deep_result.get('error', 'Unknown error')}")
                else:
                    logger.info(f"Deep validation completed: {deep_result['file_path']}")
                    display_deep_results(deep_result['file_path'])
            except Exception as e:
                logger.error(f"Unexpected error during deep validation: {e}")
            finally:
                # Ensure cleanup
                logger.info("Ensuring all AWS resources are cleaned up")
                cleanup_resources(config["region"], config["profile"], execution_id)
        
        logger.info("Validation process completed")
        return 0
    
    except KeyboardInterrupt:
        logger.warning("Process interrupted by user")
        # Try to clean up resources before exiting
        cleanup_resources(config["region"], config["profile"], execution_id)
        return 130
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        # Try to clean up resources before exiting
        cleanup_resources(config["region"], config["profile"], execution_id)
        return 1

if __name__ == "__main__":
    sys.exit(main())