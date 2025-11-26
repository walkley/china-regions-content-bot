#!/usr/bin/env python3
"""
Generate reports.json from docs/reports/ directory
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime, UTC

def parse_yaml_front_matter(content):
    """Parse YAML front matter from markdown content"""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return {}
    
    front_matter = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            front_matter[key.strip()] = value.strip()
    
    return front_matter

def extract_report_metadata(report_dir):
    """Extract metadata from a report directory"""
    report_md = report_dir / 'report.md'
    
    if not report_md.exists():
        return None
    
    try:
        with open(report_md, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metadata = parse_yaml_front_matter(content)
        
        # Extract required fields
        return {
            'title': metadata.get('title', report_dir.name),
            'publish_date': metadata.get('publish_date', ''),
            'url': f'reports/{report_dir.name}/',
            'original_url': metadata.get('original_url', ''),
            'validation_date': metadata.get('validation_date', ''),
            'target_region': metadata.get('target_region', 'cn-northwest-1'),
            'feasibility': metadata.get('feasibility', 'UNKNOWN'),
            'available_services': int(metadata.get('available_services', 0)),
            'unavailable_services': int(metadata.get('unavailable_services', 0))
        }
    except Exception as e:
        print(f"Error processing {report_dir.name}: {e}")
        return None

def get_latest_report(url_dir):
    """Get the latest report from a URL directory"""
    timestamp_dirs = []

    for timestamp_dir in url_dir.iterdir():
        if timestamp_dir.is_dir():
            timestamp_dirs.append(timestamp_dir)

    if not timestamp_dirs:
        return None

    # Sort by directory name (timestamp format YYYYMMDD_HHMMSS ensures correct ordering)
    latest_dir = sorted(timestamp_dirs, key=lambda x: x.name, reverse=True)[0]
    return latest_dir


def generate_reports_json():
    """Generate reports.json from all reports, using only the latest report for each blog"""
    reports_dir = Path('./docs/reports')

    if not reports_dir.exists():
        print("Error: docs/reports/ directory not found")
        return

    reports = []
    stats = {
        'total': 0,
        'high': 0,
        'moderate': 0,
        'low': 0,
        'not_applicable': 0
    }

    # Scan all URL directories
    for url_dir in sorted(reports_dir.iterdir()):
        if url_dir.is_dir():
            # Get the latest report for this URL
            latest_report_dir = get_latest_report(url_dir)

            if latest_report_dir:
                metadata = extract_report_metadata(latest_report_dir)
                if metadata:
                    # Update URL to include the full path: url_dir/timestamp_dir
                    metadata['url'] = f'reports/{url_dir.name}/{latest_report_dir.name}/'
                    reports.append(metadata)
                    stats['total'] += 1

                    feasibility = metadata['feasibility'].upper()
                    if feasibility == 'HIGH':
                        stats['high'] += 1
                    elif feasibility == 'MODERATE':
                        stats['moderate'] += 1
                    elif feasibility == 'LOW':
                        stats['low'] += 1
                    elif feasibility == 'NOT_APPLICABLE':
                        stats['not_applicable'] += 1
    
    # Sort by validation date (newest first)
    reports.sort(key=lambda x: x['validation_date'], reverse=True)
    
    # Generate output
    output = {
        'generated_at': datetime.now(UTC).isoformat().replace('+00:00', 'Z'),
        'statistics': stats,
        'reports': reports
    }
    
    # Write to file
    output_file = Path('./docs/reports.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"Generated reports.json with {stats['total']} reports")
    print(f"  HIGH: {stats['high']}")
    print(f"  MODERATE: {stats['moderate']}")
    print(f"  LOW: {stats['low']}")
    print(f"  NOT_APPLICABLE: {stats['not_applicable']}")

if __name__ == '__main__':
    generate_reports_json()
