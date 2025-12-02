"""
Shared utilities for AWS China Region Content Validation Tool
Provides path management, logging, command execution, and AWS helpers
"""
import os
import re
import sys
import shutil
import logging
import subprocess
from pathlib import Path
from typing import Optional, Tuple, Dict, List
from datetime import datetime


# ============================================================================
# Path Management
# ============================================================================

def get_project_root() -> Path:
    """
    Get project root directory (where run.py lives)

    Returns:
        Path: Project root directory
    """
    # Try to find project root by looking for marker files
    current = Path(__file__).resolve().parent.parent

    # Verify it's the project root (has run.py or .git)
    if (current / 'run.py').exists() or (current / '.git').exists():
        return current

    # Fallback to environment variable or cwd
    return Path(os.environ.get('PROJECT_ROOT', os.getcwd()))


def get_reports_dir(base_dir: Optional[Path] = None) -> Path:
    """
    Get reports directory with optional custom base

    Args:
        base_dir: Optional custom base directory

    Returns:
        Path: Reports directory path
    """
    if base_dir:
        return base_dir / 'reports'
    return get_project_root() / 'docs' / 'reports'


def get_url_path(url: str) -> str:
    """
    Convert URL to directory-safe path (matches bash version logic)
    Example: https://aws.amazon.com/blogs/aws/my-blog/ -> blogs_aws_my-blog

    Args:
        url: Blog post URL

    Returns:
        str: URL path component suitable for directory name
    """
    # Remove protocol and domain
    url_path = re.sub(r'https?://[^/]+/', '', url)
    # Remove trailing slash
    url_path = url_path.rstrip('/')
    # Convert slashes to underscores
    url_path = url_path.replace('/', '_')
    return url_path


def create_validation_dir(
    url: str,
    base_dir: Optional[Path] = None
) -> Tuple[Path, str]:
    """
    Create validation directory structure

    Args:
        url: Blog post URL
        base_dir: Optional custom base directory

    Returns:
        Tuple[Path, str]: (validation_dir, timestamp)
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    url_path = get_url_path(url)
    reports_dir = get_reports_dir(base_dir)

    validation_dir = reports_dir / url_path / timestamp
    validation_dir.mkdir(parents=True, exist_ok=True)

    return validation_dir, timestamp


# ============================================================================
# Logging
# ============================================================================

def setup_logging(
    level: str = "INFO",
    log_file: Optional[Path] = None
) -> logging.Logger:
    """
    Setup centralized logging configuration

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_file: Optional file path for file logging

    Returns:
        logging.Logger: Configured logger
    """
    log_level = getattr(logging, level.upper(), logging.INFO)

    # Create formatter matching validate.sh format
    formatter = logging.Formatter(
        '[%(asctime)s] - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logger = logging.getLogger('aws_china_validator')
    logger.setLevel(log_level)
    logger.handlers.clear()  # Remove existing handlers

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler if specified
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get logger instance for module

    Args:
        name: Module name

    Returns:
        logging.Logger: Module logger
    """
    return logging.getLogger(f'aws_china_validator.{name}')


# ============================================================================
# Command Execution
# ============================================================================

def check_command_exists(cmd: str) -> bool:
    """
    Check if command exists in PATH

    Args:
        cmd: Command name to check

    Returns:
        bool: True if command exists, False otherwise
    """
    return shutil.which(cmd) is not None


def run_command(
    cmd: List[str],
    timeout: int = 300,
    capture_output: bool = True,
    check: bool = False,
    **kwargs
) -> subprocess.CompletedProcess:
    """
    Wrapper for subprocess.run with consistent defaults

    Args:
        cmd: Command and arguments as list
        timeout: Timeout in seconds (default: 300)
        capture_output: Whether to capture stdout/stderr
        check: Whether to raise exception on non-zero exit
        **kwargs: Additional arguments passed to subprocess.run

    Returns:
        subprocess.CompletedProcess: Result of command execution
    """
    return subprocess.run(
        cmd,
        capture_output=capture_output,
        text=True,
        timeout=timeout,
        check=check,
        **kwargs
    )


# ============================================================================
# AWS Helpers
# ============================================================================

def check_aws_profile(profile: str, region: str) -> bool:
    """
    Validate AWS profile configuration (matches validate.sh logic)

    Args:
        profile: AWS CLI profile name
        region: AWS region

    Returns:
        bool: True if profile is configured, False otherwise
    """
    logger = get_logger('aws_helpers')

    # Check if profile is configured
    try:
        result = run_command(
            ['aws', 'configure', 'list', '--profile', profile],
            capture_output=True
        )
        if result.returncode != 0:
            logger.error(f"AWS profile '{profile}' not found or not configured")
            logger.error(f"Please run: aws configure --profile {profile}")
            return False
    except subprocess.TimeoutExpired:
        logger.error("AWS CLI command timed out")
        return False
    except FileNotFoundError:
        logger.error("AWS CLI not found. Please install AWS CLI.")
        return False
    except Exception as e:
        logger.error(f"Failed to check AWS profile: {e}")
        return False

    # Check credentials validity (warning only, like bash version)
    try:
        result = run_command(
            ['aws', 'sts', 'get-caller-identity', '--profile', profile],
            capture_output=True,
            timeout=30
        )
        if result.returncode != 0:
            logger.warning(f"AWS profile '{profile}' credentials may be invalid or expired")
            logger.warning("Continuing anyway, but validation may fail...")
    except subprocess.TimeoutExpired:
        logger.warning("AWS credentials check timed out")
    except Exception:
        pass  # Warning only

    return True


# ============================================================================
# Validation Helpers
# ============================================================================

def parse_yaml_front_matter(content: str) -> Dict:
    """
    Parse YAML front matter from markdown content

    Args:
        content: Markdown content with potential YAML front matter

    Returns:
        Dict: Parsed front matter as dictionary
    """
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return {}

    front_matter = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            front_matter[key.strip()] = value.strip()

    return front_matter


def extract_report_metadata(report_path: Path) -> Optional[Dict]:
    """
    Extract metadata from report.md file

    Args:
        report_path: Path to report directory

    Returns:
        Optional[Dict]: Metadata dictionary or None if error
    """
    logger = get_logger('validation_helpers')
    report_file = report_path / 'report.md'

    if not report_file.exists():
        return None

    try:
        with open(report_file, 'r', encoding='utf-8') as f:
            content = f.read()

        metadata = parse_yaml_front_matter(content)
        return {
            'title': metadata.get('title', report_path.name),
            'publish_date': metadata.get('publish_date', ''),
            'url': f'reports/{report_path.name}/',
            'original_url': metadata.get('original_url', ''),
            'validation_date': metadata.get('validation_date', ''),
            'target_region': metadata.get('target_region', 'cn-northwest-1'),
            'feasibility': metadata.get('feasibility', 'UNKNOWN'),
            'available_services': int(metadata.get('available_services', 0)),
            'unavailable_services': int(metadata.get('unavailable_services', 0))
        }
    except Exception as e:
        logger.error(f"Error processing {report_path.name}: {e}")
        return None


def get_latest_report(url_dir: Path) -> Optional[Path]:
    """
    Get the latest report from a URL directory

    Args:
        url_dir: Directory containing timestamped report subdirectories

    Returns:
        Optional[Path]: Path to latest report directory or None
    """
    timestamp_dirs = []

    for timestamp_dir in url_dir.iterdir():
        if timestamp_dir.is_dir():
            timestamp_dirs.append(timestamp_dir)

    if not timestamp_dirs:
        return None

    # Sort by directory name (timestamp format YYYYMMDD_HHMMSS ensures correct ordering)
    latest_dir = sorted(timestamp_dirs, key=lambda x: x.name, reverse=True)[0]
    return latest_dir
