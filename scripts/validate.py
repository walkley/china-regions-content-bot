#!/usr/bin/env python3
"""
validate.py - Single blog post validation orchestrator
Converted from validate.sh to Python - maintains exact same behavior
"""
import os
import sys
import argparse
import subprocess
from pathlib import Path
from typing import Optional, Tuple

from . import utils

# Module logger
logger = utils.get_logger('validate')


def check_dependencies() -> bool:
    """
    Check required external commands (matches validate.sh lines 34-64)

    Returns:
        bool: True if all dependencies exist, False otherwise
    """
    required_commands = {
        'kiro-cli': 'kiro-cli (Amazon Q Developer CLI)',
        'aws': 'aws (AWS CLI)',
    }

    missing = []
    for cmd, description in required_commands.items():
        if not utils.check_command_exists(cmd):
            missing.append(description)

    if missing:
        logger.error("Missing required dependencies:")
        for dep in missing:
            logger.error(f"  - {dep}")
        return False

    return True


def create_validation_dirs(
    url: str,
    base_dir: Optional[Path] = None
) -> Tuple[Path, Path, Path, Path]:
    """
    Create directory structure for validation output
    Matches validate.sh lines 132-145

    Args:
        url: Blog post URL
        base_dir: Optional base directory for reports

    Returns:
        Tuple[Path, Path, Path, Path]: (validation_dir, source_file, report_file, log_file)
    """
    validation_dir, timestamp = utils.create_validation_dir(url, base_dir)

    source_file = validation_dir / "source.md"
    report_file = validation_dir / "report.md"
    log_file = validation_dir / "validation.log"

    return validation_dir, source_file, report_file, log_file


def run_content_conversion(url: str, output_file: Path) -> bool:
    """
    Convert URL to Markdown using content_convert module
    Matches validate.sh lines 149-154

    Args:
        url: Blog post URL
        output_file: Path where markdown should be saved

    Returns:
        bool: True if conversion succeeded, False otherwise
    """
    try:
        # Import content_convert and call as function
        from . import content_convert

        logger.info("Converting URL to Markdown...")
        return content_convert.convert_url_to_markdown(url, output_file)
    except Exception as e:
        logger.error(f"Failed to convert URL to Markdown: {e}")
        return False


def run_kiro_validation(
    source_file: Path,
    report_file: Path,
    log_file: Path,
    region: str,
    profile: str
) -> bool:
    """
    Run kiro-cli agent for validation
    Matches validate.sh lines 156-177

    Args:
        source_file: Path to source markdown file
        report_file: Path where report should be written
        log_file: Path where validation log should be written
        region: AWS China region
        profile: AWS CLI profile name

    Returns:
        bool: True if validation succeeded, False otherwise
    """
    # Set environment variables (lines 163-166)
    env = os.environ.copy()
    env.update({
        'VALIDATION_CONTENT_FILE': str(source_file.absolute()),
        'VALIDATION_RESULT_FILE': str(report_file.absolute()),
        'VALIDATION_AWS_REGION': region,
        'VALIDATION_AWS_PROFILE': profile,
    })

    logger.info("Starting validation with china-validator agent")
    logger.info(f"Content file: {source_file}")
    logger.info(f"Result file: {report_file}")
    logger.info(f"Region: {region}, Profile: {profile}")

    try:
        # Run kiro-cli (line 169)
        cmd = ['kiro-cli', 'chat', '--no-interactive', '--agent=china-validator']

        result = subprocess.run(
            cmd,
            input="开始验证\n",
            capture_output=True,
            text=True,
            env=env,
            timeout=3600  # 1 hour timeout
        )

        # Write output to log file
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write(result.stdout)
            if result.stderr:
                f.write("\n--- STDERR ---\n")
                f.write(result.stderr)

        return result.returncode == 0

    except subprocess.TimeoutExpired:
        logger.error("Validation timed out after 1 hour")
        return False
    except FileNotFoundError:
        logger.error("kiro-cli command not found. Is it installed?")
        return False
    except Exception as e:
        logger.error(f"Failed to run kiro-cli validation: {e}")
        return False


def validate_url(
    url: str,
    region: str = "cn-northwest-1",
    profile: str = "cn",
    log_level: str = "INFO",
    base_dir: Optional[Path] = None
) -> bool:
    """
    Main validation function - can be called from other scripts
    This is the main entry point for batch_validate.py

    Args:
        url: Blog post URL to validate
        region: AWS China region (default: cn-northwest-1)
        profile: AWS CLI profile name (default: cn)
        log_level: Logging level (default: INFO)
        base_dir: Optional base directory for reports

    Returns:
        bool: True if validation succeeded, False otherwise
    """
    # Setup logging
    global logger
    logger = utils.setup_logging(log_level)
    logger = utils.get_logger('validate')

    # Check dependencies (matches line 84)
    if not check_dependencies():
        return False

    # Check AWS profile (matches line 129)
    if not utils.check_aws_profile(profile, region):
        return False

    # Create output directories (matches lines 132-145)
    validation_dir, source_file, report_file, log_file = create_validation_dirs(url, base_dir)

    logger.info(f"Validating {url}")
    logger.info(f"Output directory: {validation_dir}")

    # Step 1: Convert URL to Markdown (matches lines 149-154)
    if not run_content_conversion(url, source_file):
        logger.error("Failed to convert URL to Markdown")
        return False

    # Step 2: Run validation with kiro-cli (matches lines 156-177)
    if run_kiro_validation(source_file, report_file, log_file, region, profile):
        logger.info("Validation succeeded")
        return True
    else:
        logger.error("Validation failed")
        return False


def main():
    """CLI entry point (matches validate.sh lines 86-127)"""
    parser = argparse.ArgumentParser(
        description='AWS China Region Content Validation Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -u https://aws.amazon.com/blogs/...
  %(prog)s -u <url> -r cn-north-1 -p my-profile
        """
    )

    parser.add_argument(
        '-u', '--url',
        required=True,
        help='URL of the content to validate (required)'
    )
    parser.add_argument(
        '-r', '--region',
        default='cn-northwest-1',
        help='AWS China region (default: cn-northwest-1)'
    )
    parser.add_argument(
        '-p', '--profile',
        default='cn',
        help='AWS CLI profile (default: cn)'
    )
    parser.add_argument(
        '--log-level',
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='Logging level (default: INFO)'
    )
    parser.add_argument(
        '--base-dir',
        type=Path,
        help='Base directory for reports (default: project_root/docs)'
    )

    args = parser.parse_args()

    success = validate_url(
        url=args.url,
        region=args.region,
        profile=args.profile,
        log_level=args.log_level,
        base_dir=args.base_dir
    )

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
