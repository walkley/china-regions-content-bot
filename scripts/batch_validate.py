#!/usr/bin/env python3
"""
Batch Validation Script for AWS Blog Posts
Reads blog posts from JSON and validates each using the validate module
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List, Dict, Optional

from . import utils, validate


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


def check_existing_report(url: str, reports_dir: Optional[Path] = None) -> bool:
    """
    Check if a report already exists for the given URL.

    Args:
        url: Blog post URL
        reports_dir: Base directory for reports

    Returns:
        True if report exists, False otherwise
    """
    if reports_dir is None:
        reports_dir = utils.get_reports_dir()

    url_path = utils.get_url_path(url)
    report_path = reports_dir / url_path

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
    reports_dir: Optional[Path] = None
) -> bool:
    """
    Validate a single blog post URL using validate module

    Args:
        url: Blog post URL to validate
        region: AWS China region
        profile: AWS CLI profile name
        log_level: Logging level
        reports_dir: Base directory for reports

    Returns:
        True if validation succeeded, False otherwise
    """
    try:
        # Call validate.validate_url directly (no subprocess)
        base_dir = reports_dir.parent if reports_dir else None
        success = validate.validate_url(
            url=url,
            region=region,
            profile=profile,
            log_level=log_level,
            base_dir=base_dir
        )
        return success
    except Exception as e:
        logger = utils.get_logger('batch_validate')
        logger.error(f"Error validating {url}: {e}")
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
        type=Path,
        default=None,
        help='Base directory for reports (default: auto-detect)'
    )

    args = parser.parse_args()

    # Get reports directory
    reports_dir = args.reports_dir or utils.get_reports_dir()

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
        if args.skip_existing and check_existing_report(url, reports_dir):
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
            reports_dir=reports_dir
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
