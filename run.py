#!/usr/bin/env python3
"""
run.py - AWS China Region Content Validation Tool
Main entry point for all operations
"""
import sys
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description='AWS China Region Content Validation Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  validate          Validate a single blog post
  batch            Batch validate multiple blog posts
  fetch-blogs      Fetch blog posts from AWS API
  generate-reports Generate reports.json from validation reports

Examples:
  # Single validation (replaces ./validate.sh)
  python run.py validate -u https://aws.amazon.com/blogs/...

  # Batch validation (replaces python batch_validate.py)
  python run.py batch -i blogs.json --skip-existing

  # Fetch blogs (replaces python aws_blog_fetcher.py)
  python run.py fetch-blogs -n 50 -o blogs.json

  # Generate reports (replaces python scripts/generate_reports_json.py)
  python run.py generate-reports

For detailed help on a command:
  python run.py <command> --help
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # ========== VALIDATE COMMAND ==========
    validate_parser = subparsers.add_parser(
        'validate',
        help='Validate single blog post',
        description='Validate AWS content for China region compatibility'
    )
    validate_parser.add_argument(
        '-u', '--url',
        required=True,
        help='URL to validate'
    )
    validate_parser.add_argument(
        '-r', '--region',
        default='cn-northwest-1',
        help='AWS China region (default: cn-northwest-1)'
    )
    validate_parser.add_argument(
        '-p', '--profile',
        default='cn',
        help='AWS CLI profile (default: cn)'
    )
    validate_parser.add_argument(
        '--log-level',
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='Logging level (default: INFO)'
    )
    validate_parser.add_argument(
        '--base-dir',
        type=Path,
        help='Base directory for reports (default: auto-detect)'
    )

    # ========== BATCH COMMAND ==========
    batch_parser = subparsers.add_parser(
        'batch',
        help='Batch validate blog posts',
        description='Validate multiple blog posts from JSON file or stdin'
    )
    batch_parser.add_argument(
        '-i', '--input',
        type=str,
        help='Input JSON file (reads from stdin if not specified)'
    )
    batch_parser.add_argument(
        '-r', '--region',
        default='cn-northwest-1',
        help='AWS China region (default: cn-northwest-1)'
    )
    batch_parser.add_argument(
        '-p', '--profile',
        default='cn',
        help='AWS CLI profile (default: cn)'
    )
    batch_parser.add_argument(
        '--log-level',
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='Logging level (default: INFO)'
    )
    batch_parser.add_argument(
        '--continue-on-error',
        action='store_true',
        help='Continue validating remaining blogs even if some fail'
    )
    batch_parser.add_argument(
        '--skip-existing',
        action='store_true',
        help='Skip blogs that already have validation reports'
    )
    batch_parser.add_argument(
        '--limit',
        type=int,
        help='Limit validation to first N blogs'
    )
    batch_parser.add_argument(
        '--reports-dir',
        type=Path,
        help='Base directory for reports (default: auto-detect)'
    )

    # ========== FETCH-BLOGS COMMAND ==========
    fetch_parser = subparsers.add_parser(
        'fetch-blogs',
        help='Fetch blog posts from AWS API',
        description='Fetch AWS blog posts with optional filtering'
    )
    fetch_parser.add_argument(
        '-n', '--count',
        type=int,
        required=True,
        help='Number of articles to fetch (required)'
    )
    fetch_parser.add_argument(
        '-c', '--category',
        type=str,
        help='Category filter(s), comma-separated (e.g., artificial-intelligence,compute)'
    )
    fetch_parser.add_argument(
        '-p', '--post-type',
        type=str,
        help='Post type filter(s), comma-separated (e.g., technical-how-to,announcements)'
    )
    fetch_parser.add_argument(
        '-o', '--output',
        type=str,
        help='Output file path (prints to stdout if not specified)'
    )

    # ========== GENERATE-REPORTS COMMAND ==========
    gen_parser = subparsers.add_parser(
        'generate-reports',
        help='Generate reports.json',
        description='Generate reports.json from validation reports'
    )
    gen_parser.add_argument(
        '--base-dir',
        type=Path,
        help='Base directory containing docs/ (default: auto-detect)'
    )

    # Parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # ========== EXECUTE COMMANDS ==========

    if args.command == 'validate':
        from scripts import validate
        success = validate.validate_url(
            url=args.url,
            region=args.region,
            profile=args.profile,
            log_level=args.log_level,
            base_dir=args.base_dir
        )
        sys.exit(0 if success else 1)

    elif args.command == 'batch':
        from scripts import batch_validate
        # Reconstruct sys.argv for batch_validate.main()
        old_argv = sys.argv
        sys.argv = ['batch_validate.py']
        if args.input:
            sys.argv.extend(['-i', args.input])
        sys.argv.extend(['-r', args.region, '-p', args.profile, '--log-level', args.log_level])
        if args.continue_on_error:
            sys.argv.append('--continue-on-error')
        if args.skip_existing:
            sys.argv.append('--skip-existing')
        if args.limit:
            sys.argv.extend(['--limit', str(args.limit)])
        if args.reports_dir:
            sys.argv.extend(['--reports-dir', str(args.reports_dir)])

        try:
            batch_validate.main()
        finally:
            sys.argv = old_argv

    elif args.command == 'fetch-blogs':
        from scripts import aws_blog_fetcher
        # Reconstruct sys.argv for aws_blog_fetcher.main()
        old_argv = sys.argv
        sys.argv = ['aws_blog_fetcher.py', '-n', str(args.count)]
        if args.category:
            sys.argv.extend(['-c', args.category])
        if args.post_type:
            sys.argv.extend(['-p', args.post_type])
        if args.output:
            sys.argv.extend(['-o', args.output])

        try:
            aws_blog_fetcher.main()
        finally:
            sys.argv = old_argv

    elif args.command == 'generate-reports':
        from scripts import generate_reports_json, utils
        # Setup logging first
        utils.setup_logging()
        generate_reports_json.generate_reports_json(args.base_dir)
        sys.exit(0)


if __name__ == '__main__':
    main()
