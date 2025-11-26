#!/usr/bin/env python3
"""
Batch Validation Script for AWS Blog Posts
Reads output from aws_blog_fetcher.py and validates each blog using validate.sh
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Optional


def read_blog_posts(input_source: Optional[str] = None) -> List[Dict]:
    """
    Read blog posts from a JSON file or stdin.

    Args:
        input_source: Path to JSON file, or None to read from stdin

    Returns:
        List of blog post dictionaries
    """
    try:
        if input_source:
            with open(input_source, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = json.load(sys.stdin)

        if not isinstance(data, list):
            print(f"Error: Expected a list of blog posts, got {type(data)}", file=sys.stderr)
            sys.exit(1)

        return data
    except FileNotFoundError:
        print(f"Error: File '{input_source}' not found", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)


def get_url_path(url: str) -> str:
    """
    Convert URL to the path format used in report directories.

    Args:
        url: Blog post URL

    Returns:
        URL path component suitable for directory name
    """
    # Remove protocol and domain
    url_path = re.sub(r'https?://[^/]+/', '', url)
    # Remove trailing slash
    url_path = url_path.rstrip('/')
    # Convert slashes to underscores
    url_path = url_path.replace('/', '_')
    return url_path


def check_existing_report(url: str, reports_dir: str = "./docs/reports") -> bool:
    """
    Check if a report already exists for the given URL.

    Args:
        url: Blog post URL
        reports_dir: Base directory for reports

    Returns:
        True if report exists, False otherwise
    """
    url_path = get_url_path(url)
    report_path = Path(reports_dir) / url_path

    if report_path.exists() and report_path.is_dir():
        # Check if there's at least one report inside
        subdirs = [d for d in report_path.iterdir() if d.is_dir()]
        return len(subdirs) > 0

    return False


def validate_blog(
    url: str,
    region: str = "cn-northwest-1",
    profile: str = "cn",
    log_level: str = "INFO",
    validate_script: str = "./validate.sh"
) -> bool:
    """
    Call validate.sh for a single blog post URL.

    Args:
        url: Blog post URL to validate
        region: AWS China region
        profile: AWS CLI profile name
        log_level: Logging level
        validate_script: Path to validate.sh script

    Returns:
        True if validation succeeded, False otherwise
    """
    cmd = [
        validate_script,
        "-u", url,
        "-r", region,
        "-p", profile,
        "--log-level", log_level
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=1800  # 30 minute timeout per validation
        )

        # Print output for visibility
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)

        return result.returncode == 0

    except subprocess.TimeoutExpired:
        print(f"Error: Validation timed out for {url}", file=sys.stderr)
        return False
    except FileNotFoundError:
        print(f"Error: validate.sh script not found at {validate_script}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error running validation for {url}: {e}", file=sys.stderr)
        return False


def main():
    """Main entry point for batch validation."""
    parser = argparse.ArgumentParser(
        description='Batch validate AWS blog posts from aws_blog_fetcher.py output',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Read from file and validate all blogs
  %(prog)s -i blogs.json

  # Pipe from aws_blog_fetcher.py
  python3 aws_blog_fetcher.py --count 10 | %(prog)s

  # Fetch and validate in one command, custom region/profile
  python3 aws_blog_fetcher.py --count 5 | %(prog)s -r cn-north-1 -p china

  # Continue on errors and show summary
  %(prog)s -i blogs.json --continue-on-error

  # Skip blogs that already have reports
  %(prog)s -i blogs.json --skip-existing --continue-on-error

  # Limit validation to first 3 blogs
  %(prog)s -i blogs.json --limit 3
        """
    )

    parser.add_argument(
        '-i', '--input',
        type=str,
        help='Input JSON file (reads from stdin if not specified)'
    )

    parser.add_argument(
        '-r', '--region',
        type=str,
        default='cn-northwest-1',
        help='AWS China region (default: cn-northwest-1)'
    )

    parser.add_argument(
        '-p', '--profile',
        type=str,
        default='cn',
        help='AWS CLI profile name (default: cn)'
    )

    parser.add_argument(
        '--log-level',
        type=str,
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='Logging level (default: INFO)'
    )

    parser.add_argument(
        '--validate-script',
        type=str,
        default='./validate.sh',
        help='Path to validate.sh script (default: ./validate.sh)'
    )

    parser.add_argument(
        '--continue-on-error',
        action='store_true',
        help='Continue validating remaining blogs even if some fail'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Limit validation to first N blogs'
    )

    parser.add_argument(
        '--skip-existing',
        action='store_true',
        help='Skip blogs that already have validation reports'
    )

    parser.add_argument(
        '--reports-dir',
        type=str,
        default='./docs/reports',
        help='Base directory for reports (default: ./docs/reports)'
    )

    args = parser.parse_args()

    # Check if validate.sh exists and is executable
    validate_path = Path(args.validate_script)
    if not validate_path.exists():
        print(f"Error: validate.sh not found at {args.validate_script}", file=sys.stderr)
        sys.exit(1)
    if not validate_path.is_file():
        print(f"Error: {args.validate_script} is not a file", file=sys.stderr)
        sys.exit(1)

    # Make sure validate.sh is executable
    try:
        validate_path.chmod(0o755)
    except Exception as e:
        print(f"Warning: Could not set execute permissions on {args.validate_script}: {e}", file=sys.stderr)

    # Read blog posts
    print(f"Reading blog posts from {'stdin' if not args.input else args.input}...", file=sys.stderr)
    blog_posts = read_blog_posts(args.input)

    # Apply limit if specified
    if args.limit:
        blog_posts = blog_posts[:args.limit]
        print(f"Limiting validation to first {args.limit} blogs", file=sys.stderr)

    total_blogs = len(blog_posts)
    print(f"Found {total_blogs} blog posts to validate\n", file=sys.stderr)

    # Track results
    successful = 0
    failed = 0
    skipped = 0
    failed_urls = []

    # Validate each blog
    for idx, blog in enumerate(blog_posts, 1):
        url = blog.get('link', '')
        title = blog.get('title', 'Unknown')

        if not url:
            print(f"[{idx}/{total_blogs}] Skipping blog with no URL: {title}", file=sys.stderr)
            failed += 1
            continue

        # Check if report exists and skip if requested
        if args.skip_existing and check_existing_report(url, args.reports_dir):
            print(f"[{idx}/{total_blogs}] Skipping (report exists): {title}", file=sys.stderr)
            skipped += 1
            continue

        print(f"\n{'='*80}", file=sys.stderr)
        print(f"[{idx}/{total_blogs}] Validating: {title}", file=sys.stderr)
        print(f"URL: {url}", file=sys.stderr)
        print(f"{'='*80}\n", file=sys.stderr)

        success = validate_blog(
            url=url,
            region=args.region,
            profile=args.profile,
            log_level=args.log_level,
            validate_script=args.validate_script
        )

        if success:
            successful += 1
            print(f"\n✓ Successfully validated [{idx}/{total_blogs}]", file=sys.stderr)
        else:
            failed += 1
            failed_urls.append({'title': title, 'url': url})
            print(f"\n✗ Failed to validate [{idx}/{total_blogs}]", file=sys.stderr)

            if not args.continue_on_error:
                print("\nStopping due to validation failure. Use --continue-on-error to continue.", file=sys.stderr)
                break

    # Print summary
    print(f"\n{'='*80}", file=sys.stderr)
    print("VALIDATION SUMMARY", file=sys.stderr)
    print(f"{'='*80}", file=sys.stderr)
    print(f"Total blogs: {total_blogs}", file=sys.stderr)
    print(f"Successful: {successful}", file=sys.stderr)
    print(f"Failed: {failed}", file=sys.stderr)
    if args.skip_existing:
        print(f"Skipped (existing): {skipped}", file=sys.stderr)

    if failed_urls:
        print(f"\nFailed URLs:", file=sys.stderr)
        for item in failed_urls:
            print(f"  - {item['title']}", file=sys.stderr)
            print(f"    {item['url']}", file=sys.stderr)

    # Exit with appropriate code
    sys.exit(0 if failed == 0 else 1)


if __name__ == '__main__':
    main()
