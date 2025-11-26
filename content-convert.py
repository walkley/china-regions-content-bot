#!/usr/bin/env python3
"""
content-convert.py - Convert AWS blog posts to Markdown format
Usage: ./content-convert.py -u <blog URL> -o <output file path>
"""

import argparse
import os
import sys
import requests
from bs4 import BeautifulSoup
import markdownify
from urllib.parse import urljoin, urlparse


def log_info(message):
    """Log info message"""
    print(f"[INFO] {message}")


def log_error(message):
    """Log error message"""
    print(f"[ERROR] {message}", file=sys.stderr)


def log_success(message):
    """Log success message"""
    print(f"[SUCCESS] {message}")


def fetch_html(url):
    """Fetch HTML content from URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        log_error(f"Failed to fetch URL: {e}")
        return None


def extract_main_content(html, base_url):
    """Extract main article content from AWS blog HTML using specific selectors"""
    soup = BeautifulSoup(html, 'html.parser')

    # Extract title using specific selector
    title_element = soup.select_one('#aws-page-content-main > article > h1')
    title_text = title_element.get_text().strip() if title_element else "Untitled"

    # Extract main content using specific selector
    main_content = soup.select_one('#aws-page-content-main > article > section.blog-post-content')
    if not main_content:
        # Fallback to broader selector
        main_content = soup.select_one('.blog-post-content')
        if not main_content:
            log_error("Could not find blog post content section")
            return None

    # Extract metadata and convert to plain text (remove links)
    metadata_section = soup.select_one('#aws-page-content-main > article > footer.blog-post-meta')
    metadata_text = ""
    if metadata_section:
        # Get text content and clean it up
        metadata_text = metadata_section.get_text()
        # Clean up metadata text - remove extra whitespace and newlines
        metadata_lines = [line.strip() for line in metadata_text.split('\n') if line.strip()]
        # Remove unwanted metadata elements
        cleaned_lines = []
        for line in metadata_lines:
            if line not in ['Permalink', 'Comments', 'Share']:
                cleaned_lines.append(line)
        metadata_text = '\n'.join(cleaned_lines)

    # Convert relative URLs to absolute URLs for images
    for img in main_content.find_all('img'):
        if img.get('src'):
            img['src'] = urljoin(base_url, img['src'])
        if img.get('data-src'):
            img['data-src'] = urljoin(base_url, img['data-src'])

    # Convert relative URLs for links
    for link in main_content.find_all('a'):
        if link.get('href'):
            link['href'] = urljoin(base_url, link['href'])

    return main_content, title_text, metadata_text


def html_to_markdown(html_content, title, metadata_text=""):
    """Convert HTML content to Markdown"""
    # Custom markdownify settings
    md_content = markdownify.markdownify(
        str(html_content),
        heading_style="ATX",
        bullets="-",
        strip=['script', 'style', 'nav', 'header', 'footer']
    )

    # Clean up the markdown
    lines = md_content.split('\n')
    cleaned_lines = []
    prev_empty = False

    for line in lines:
        line = line.strip()
        if not line:
            if not prev_empty:
                cleaned_lines.append('')
            prev_empty = True
        else:
            cleaned_lines.append(line)
            prev_empty = False

    # Build final content with title and optional metadata
    final_content = f"# {title}\n\n"
    if metadata_text:
        final_content += f"{metadata_text}\n\n"
    final_content += '\n'.join(cleaned_lines).strip()

    return final_content


def main():
    parser = argparse.ArgumentParser(
        description="Convert AWS blog posts to clean Markdown format"
    )
    parser.add_argument('-u', '--url', required=True, help='Blog URL to convert')
    parser.add_argument('-o', '--output', required=True, help='Output Markdown file path')

    args = parser.parse_args()

    # Validate URL
    parsed_url = urlparse(args.url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        log_error("Invalid URL provided")
        sys.exit(1)

    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        log_info(f"Creating output directory: {output_dir}")
        os.makedirs(output_dir, exist_ok=True)

    log_info(f"Converting blog: {args.url}")

    # Fetch HTML content
    html = fetch_html(args.url)
    if not html:
        sys.exit(1)

    # Extract main content
    content_result = extract_main_content(html, args.url)
    if not content_result:
        sys.exit(1)

    main_content, title, metadata_text = content_result

    # Convert to markdown
    log_info("Converting HTML to Markdown...")
    markdown_content = html_to_markdown(main_content, title, metadata_text)

    # Save to file
    try:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        log_success(f"Conversion complete! Markdown file saved to: {args.output}")
    except IOError as e:
        log_error(f"Failed to write output file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()