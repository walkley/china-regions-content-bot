#!/usr/bin/env python3
"""
AWS Blog API Fetcher
A command-line tool to query AWS blog posts with filtering and pagination support.
"""

import argparse
import json
import sys
from typing import List, Dict, Optional
from urllib.parse import urlencode

try:
    import requests
except ImportError:
    print("Error: 'requests' library is required. Install it with: pip install requests", file=sys.stderr)
    sys.exit(1)


def fetch_aws_blog_posts(
    categories: Optional[List[str]] = None,
    post_types: Optional[List[str]] = None,
    article_count: int = 10
) -> List[Dict]:
    """
    Fetch AWS blog posts from the AWS blog API.

    Args:
        categories: List of category filters (e.g., ['artificial-intelligence', 'compute'])
        post_types: List of post type filters (e.g., ['technical-how-to'])
        article_count: Total number of articles to fetch

    Returns:
        List of dictionaries containing blog post information
    """
    base_url = "https://aws.amazon.com/api/dirs/items/search"
    all_posts = []
    page = 0

    # Determine page size (API limit appears to be around 50)
    page_size = min(article_count, 50)

    while len(all_posts) < article_count:
        # Build query parameters
        params = {
            "item.directoryId": "blog-posts",
            "item.locale": "en_US",
            "sort_by": "item.dateCreated",
            "sort_order": "desc",
            "size": page_size,
            "page": page
        }

        # Build URL with tags
        url_parts = [f"{base_url}?"]

        # Add base parameters
        for key, value in params.items():
            url_parts.append(f"{key}={value}&")

        # Add category tags
        if categories:
            for category in categories:
                url_parts.append(f"tags.id=blog-posts%23category%23{category}&")

        # Add post type tags
        if post_types:
            for post_type in post_types:
                url_parts.append(f"tags.id=blog-posts%23category-post-types%23{post_type}&")

        # Remove trailing '&'
        query_url = ''.join(url_parts).rstrip('&')

        try:
            response = requests.get(query_url, timeout=30)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}", file=sys.stderr)
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"Error parsing API response: {e}", file=sys.stderr)
            sys.exit(1)

        items = data.get('items', [])

        # If no items returned, we've reached the end
        if not items:
            break

        # Extract relevant information from each post
        for item in items:
            if len(all_posts) >= article_count:
                break

            # Access nested structure: item -> item -> additionalFields
            item_data = item.get('item', {})
            additional_fields = item_data.get('additionalFields', {})

            # Parse contributors (comes as comma-separated string, not list)
            contributors_str = additional_fields.get('contributors', '')
            authors = [author.strip() for author in contributors_str.split(',')] if contributors_str else []

            blog_post = {
                'title': additional_fields.get('title', ''),
                'link': additional_fields.get('link', ''),
                'tags': [tag.get('id', '') for tag in item.get('tags', [])],
                'authors': authors,
                'feature_image': additional_fields.get('featuredImageUrl', ''),
                'date_created': item_data.get('dateCreated', ''),
                'description': additional_fields.get('postExcerpt', '')
            }
            all_posts.append(blog_post)

        # Move to next page
        page += 1

        # Safety check to prevent infinite loops
        if page > 100:
            print("Warning: Reached maximum pagination limit", file=sys.stderr)
            break

    return all_posts[:article_count]


def main():
    """Main entry point for the CLI tool."""
    parser = argparse.ArgumentParser(
        description='Fetch AWS blog posts with optional filtering',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Fetch 10 AI blog posts
  %(prog)s --category artificial-intelligence --count 10

  # Fetch 20 technical how-to posts about compute
  %(prog)s --category compute --post-type technical-how-to --count 20

  # Fetch 30 posts with multiple categories and save to file
  %(prog)s --category ai,machine-learning --count 30 --output results.json

  # Fetch latest 50 posts (no filters)
  %(prog)s --count 50
        """
    )

    parser.add_argument(
        '-c', '--category',
        type=str,
        help='Category filter(s), comma-separated (e.g., artificial-intelligence,compute)'
    )

    parser.add_argument(
        '-p', '--post-type',
        type=str,
        help='Post type filter(s), comma-separated (e.g., technical-how-to,announcements)'
    )

    parser.add_argument(
        '-n', '--count',
        type=int,
        required=True,
        help='Number of articles to fetch (required)'
    )

    parser.add_argument(
        '-o', '--output',
        type=str,
        help='Output file path (prints to stdout if not specified)'
    )

    args = parser.parse_args()

    # Validate article count
    if args.count <= 0:
        print("Error: Article count must be greater than 0", file=sys.stderr)
        sys.exit(1)

    # Parse categories and post types
    categories = [c.strip() for c in args.category.split(',')] if args.category else None
    post_types = [p.strip() for p in args.post_type.split(',')] if args.post_type else None

    # Fetch blog posts
    print(f"Fetching {args.count} AWS blog posts...", file=sys.stderr)
    if categories:
        print(f"Categories: {', '.join(categories)}", file=sys.stderr)
    if post_types:
        print(f"Post types: {', '.join(post_types)}", file=sys.stderr)

    blog_posts = fetch_aws_blog_posts(
        categories=categories,
        post_types=post_types,
        article_count=args.count
    )

    print(f"Retrieved {len(blog_posts)} blog posts", file=sys.stderr)

    # Format output
    output_json = json.dumps(blog_posts, indent=2, ensure_ascii=False)

    # Output results
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output_json)
            print(f"Results saved to {args.output}", file=sys.stderr)
        except IOError as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(output_json)


if __name__ == '__main__':
    main()
