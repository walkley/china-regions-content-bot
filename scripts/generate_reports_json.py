#!/usr/bin/env python3
"""
Generate reports.json from docs/reports/ directory
"""

import json
from pathlib import Path
from datetime import datetime, UTC
from typing import Optional

from . import utils

# Get logger
logger = utils.get_logger('generate_reports')

def generate_reports_json(base_dir: Optional[Path] = None):
    """
    Generate reports.json from all reports, using only the latest report for each blog

    Args:
        base_dir: Base directory containing docs/ folder (default: auto-detect)
    """
    # Get the correct reports directory
    if base_dir is None:
        base_dir = utils.get_project_root() / 'docs'
    else:
        base_dir = base_dir / 'docs' if not base_dir.name == 'docs' else base_dir

    reports_dir = base_dir / 'reports'
    output_file = base_dir / 'reports.json'

    if not reports_dir.exists():
        logger.error(f"Reports directory not found: {reports_dir}")
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
            latest_report_dir = utils.get_latest_report(url_dir)

            if latest_report_dir:
                metadata = utils.extract_report_metadata(latest_report_dir)
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
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    logger.info(f"Generated reports.json with {stats['total']} reports")
    logger.info(f"  HIGH: {stats['high']}")
    logger.info(f"  MODERATE: {stats['moderate']}")
    logger.info(f"  LOW: {stats['low']}")
    logger.info(f"  NOT_APPLICABLE: {stats['not_applicable']}")

if __name__ == '__main__':
    generate_reports_json()
