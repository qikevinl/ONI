#!/usr/bin/env python3
"""
ONI Framework - Continuous Research Delivery Monitor
=====================================================

Monitors academic sources for new publications related to brain-computer
interfaces, neural security, and AI safety. Saves discovered research
to the CICD/incoming folder for review and integration.

Usage:
    python research_monitor.py [--days 7] [--sources all]

Options:
    --days      Number of days to look back (default: 7)
    --sources   Comma-separated list of sources or 'all' (default: all)
                Available: arxiv, pubmed, biorxiv, semantic_scholar

Author: ONI Framework
Version: 1.0
Last Updated: January 2026
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
from urllib.parse import quote_plus
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import xml.etree.ElementTree as ET

# Configuration
SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent.parent.parent  # Up to ONI/
CICD_INCOMING = PROJECT_ROOT / "MAIN" / "CICD" / "incoming"

# Search terms for ONI Framework relevant research
SEARCH_TERMS = [
    # Core BCI Security
    "brain computer interface security",
    "neural interface cybersecurity",
    "BCI attack vector",
    "neural implant security",
    "neurosecurity",

    # Neural Data Privacy
    "neural data privacy",
    "brain data protection",
    "cognitive privacy",
    "mental privacy",

    # AI Safety & Alignment
    "AI safety neural",
    "artificial intelligence brain interface",
    "neural network adversarial attack",

    # Specific Technologies
    "Neuralink security",
    "deep brain stimulation security",
    "EEG security vulnerability",
    "neural signal encryption",

    # Emerging Threats
    "neural ransomware",
    "brain hacking",
    "cognitive manipulation attack",
]

# Alternative simplified terms for broader coverage
SIMPLIFIED_TERMS = [
    "brain computer interface",
    "neural interface",
    "BCI security",
    "neurotechnology",
    "brain machine interface",
]


class ResearchMonitor:
    """Monitor academic sources for relevant research."""

    def __init__(self, days_back: int = 7, verbose: bool = True):
        self.days_back = days_back
        self.verbose = verbose
        self.results = []
        self.start_date = datetime.now() - timedelta(days=days_back)

    def log(self, message: str):
        """Print message if verbose mode is enabled."""
        if self.verbose:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

    def search_arxiv(self) -> list:
        """Search arXiv for relevant papers."""
        self.log("Searching arXiv...")
        papers = []

        # Use simplified terms for arXiv (more likely to return results)
        for term in SIMPLIFIED_TERMS[:3]:  # Limit to avoid rate limiting
            try:
                query = quote_plus(term)
                url = (
                    f"http://export.arxiv.org/api/query?"
                    f"search_query=all:{query}&"
                    f"start=0&max_results=10&"
                    f"sortBy=submittedDate&sortOrder=descending"
                )

                req = Request(url, headers={'User-Agent': 'ONI-Research-Monitor/1.0'})
                with urlopen(req, timeout=30) as response:
                    data = response.read().decode('utf-8')

                # Parse Atom feed
                root = ET.fromstring(data)
                ns = {'atom': 'http://www.w3.org/2005/Atom'}

                for entry in root.findall('atom:entry', ns):
                    title = entry.find('atom:title', ns)
                    summary = entry.find('atom:summary', ns)
                    published = entry.find('atom:published', ns)
                    link = entry.find('atom:id', ns)

                    if title is not None and published is not None:
                        pub_date = datetime.fromisoformat(
                            published.text.replace('Z', '+00:00')
                        ).replace(tzinfo=None)

                        if pub_date >= self.start_date:
                            papers.append({
                                'title': title.text.strip().replace('\n', ' '),
                                'abstract': summary.text.strip() if summary is not None else '',
                                'date': pub_date.strftime('%Y-%m-%d'),
                                'url': link.text if link is not None else '',
                                'source': 'arxiv',
                                'search_term': term
                            })

            except (URLError, HTTPError, ET.ParseError) as e:
                self.log(f"  Warning: arXiv search failed for '{term}': {e}")
                continue

        # Deduplicate by title
        seen = set()
        unique_papers = []
        for paper in papers:
            if paper['title'] not in seen:
                seen.add(paper['title'])
                unique_papers.append(paper)

        self.log(f"  Found {len(unique_papers)} papers from arXiv")
        return unique_papers

    def search_pubmed(self) -> list:
        """Search PubMed for relevant papers."""
        self.log("Searching PubMed...")
        papers = []

        # PubMed E-utilities base URL
        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

        for term in SIMPLIFIED_TERMS[:2]:  # Limit queries
            try:
                # Search for IDs
                search_url = (
                    f"{base_url}/esearch.fcgi?"
                    f"db=pubmed&term={quote_plus(term)}&"
                    f"retmax=10&sort=date&retmode=json"
                )

                req = Request(search_url, headers={'User-Agent': 'ONI-Research-Monitor/1.0'})
                with urlopen(req, timeout=30) as response:
                    search_data = json.loads(response.read().decode('utf-8'))

                id_list = search_data.get('esearchresult', {}).get('idlist', [])

                if not id_list:
                    continue

                # Fetch details for each ID
                ids = ','.join(id_list)
                fetch_url = (
                    f"{base_url}/esummary.fcgi?"
                    f"db=pubmed&id={ids}&retmode=json"
                )

                req = Request(fetch_url, headers={'User-Agent': 'ONI-Research-Monitor/1.0'})
                with urlopen(req, timeout=30) as response:
                    fetch_data = json.loads(response.read().decode('utf-8'))

                results = fetch_data.get('result', {})

                for pmid in id_list:
                    if pmid in results:
                        paper = results[pmid]
                        pub_date_str = paper.get('pubdate', '')

                        # Parse various date formats
                        try:
                            if len(pub_date_str) >= 4:
                                year = int(pub_date_str[:4])
                                if year >= self.start_date.year:
                                    papers.append({
                                        'title': paper.get('title', 'Unknown'),
                                        'abstract': '',  # Summary doesn't include abstract
                                        'date': pub_date_str,
                                        'url': f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                                        'source': 'pubmed',
                                        'search_term': term
                                    })
                        except ValueError:
                            continue

            except (URLError, HTTPError, json.JSONDecodeError) as e:
                self.log(f"  Warning: PubMed search failed for '{term}': {e}")
                continue

        # Deduplicate
        seen = set()
        unique_papers = []
        for paper in papers:
            if paper['title'] not in seen:
                seen.add(paper['title'])
                unique_papers.append(paper)

        self.log(f"  Found {len(unique_papers)} papers from PubMed")
        return unique_papers

    def search_biorxiv(self) -> list:
        """Search bioRxiv for relevant preprints."""
        self.log("Searching bioRxiv...")
        papers = []

        # bioRxiv API
        start = self.start_date.strftime('%Y-%m-%d')
        end = datetime.now().strftime('%Y-%m-%d')

        try:
            url = f"https://api.biorxiv.org/details/biorxiv/{start}/{end}/0/50"
            req = Request(url, headers={'User-Agent': 'ONI-Research-Monitor/1.0'})

            with urlopen(req, timeout=30) as response:
                data = json.loads(response.read().decode('utf-8'))

            collection = data.get('collection', [])

            # Filter for relevant papers
            keywords = ['brain', 'neural', 'bci', 'interface', 'cognitive', 'neuro']

            for paper in collection:
                title = paper.get('title', '').lower()
                abstract = paper.get('abstract', '').lower()

                if any(kw in title or kw in abstract for kw in keywords):
                    papers.append({
                        'title': paper.get('title', 'Unknown'),
                        'abstract': paper.get('abstract', ''),
                        'date': paper.get('date', ''),
                        'url': f"https://www.biorxiv.org/content/{paper.get('doi', '')}",
                        'source': 'biorxiv',
                        'search_term': 'neural/brain keywords'
                    })

        except (URLError, HTTPError, json.JSONDecodeError) as e:
            self.log(f"  Warning: bioRxiv search failed: {e}")

        self.log(f"  Found {len(papers)} papers from bioRxiv")
        return papers

    def run_search(self, sources: list) -> list:
        """Run search across specified sources."""
        all_papers = []

        source_methods = {
            'arxiv': self.search_arxiv,
            'pubmed': self.search_pubmed,
            'biorxiv': self.search_biorxiv,
        }

        for source in sources:
            if source in source_methods:
                try:
                    papers = source_methods[source]()
                    all_papers.extend(papers)
                except Exception as e:
                    self.log(f"Error searching {source}: {e}")

        self.results = all_papers
        return all_papers

    def save_results(self) -> list:
        """Save results to CICD/incoming folder."""
        saved_files = []

        # Ensure directory exists
        CICD_INCOMING.mkdir(parents=True, exist_ok=True)

        for paper in self.results:
            # Generate filename
            date = paper.get('date', datetime.now().strftime('%Y-%m-%d'))
            if len(date) > 10:
                date = date[:10]

            # Sanitize title for filename
            title_slug = re.sub(r'[^\w\s-]', '', paper['title'].lower())
            title_slug = re.sub(r'[\s_]+', '-', title_slug)[:50]

            filename = f"{date}_{paper['source']}_{title_slug}.md"
            filepath = CICD_INCOMING / filename

            # Skip if already exists
            if filepath.exists():
                continue

            # Create markdown content
            content = f"""# {paper['title']}

## Metadata
- **Source:** {paper['source']}
- **Date:** {paper['date']}
- **URL:** {paper['url']}
- **Search Term:** {paper['search_term']}
- **Retrieved:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Abstract

{paper['abstract'] if paper['abstract'] else '*Abstract not available - visit URL for full paper*'}

## Relevance to ONI Framework

*To be assessed during review*

- [ ] Relevant to neural security
- [ ] Relevant to BCI architecture
- [ ] Relevant to AI safety
- [ ] Contains novel attack vectors
- [ ] Contains defensive strategies
- [ ] Background/foundational research

## Notes

*Add review notes here*

---
*Auto-generated by ONI Research Monitor*
"""

            try:
                filepath.write_text(content, encoding='utf-8')
                saved_files.append(str(filepath))
                self.log(f"  Saved: {filename}")
            except IOError as e:
                self.log(f"  Error saving {filename}: {e}")

        return saved_files

    def generate_summary(self) -> str:
        """Generate a summary report of the search."""
        summary = f"""
# ONI Research Monitor - Summary Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Search Period: Last {self.days_back} days

## Results Overview
- **Total papers found:** {len(self.results)}

### By Source:
"""
        # Count by source
        source_counts = {}
        for paper in self.results:
            source = paper['source']
            source_counts[source] = source_counts.get(source, 0) + 1

        for source, count in sorted(source_counts.items()):
            summary += f"- {source}: {count}\n"

        summary += "\n## Papers Found\n\n"

        for i, paper in enumerate(self.results, 1):
            summary += f"{i}. **{paper['title'][:80]}{'...' if len(paper['title']) > 80 else ''}**\n"
            summary += f"   - Source: {paper['source']} | Date: {paper['date']}\n"
            summary += f"   - URL: {paper['url']}\n\n"

        return summary


def main():
    parser = argparse.ArgumentParser(
        description='ONI Framework Research Monitor - Fetch latest academic publications'
    )
    parser.add_argument(
        '--days', type=int, default=7,
        help='Number of days to look back (default: 7)'
    )
    parser.add_argument(
        '--sources', type=str, default='all',
        help='Comma-separated sources: arxiv,pubmed,biorxiv or "all" (default: all)'
    )
    parser.add_argument(
        '--quiet', action='store_true',
        help='Suppress progress output'
    )
    parser.add_argument(
        '--summary-only', action='store_true',
        help='Only print summary, do not save files'
    )

    args = parser.parse_args()

    # Parse sources
    if args.sources == 'all':
        sources = ['arxiv', 'pubmed', 'biorxiv']
    else:
        sources = [s.strip().lower() for s in args.sources.split(',')]

    print("=" * 60)
    print("ONI Framework - Continuous Research Delivery Monitor")
    print("=" * 60)
    print(f"Searching for papers from the last {args.days} days...")
    print(f"Sources: {', '.join(sources)}")
    print()

    # Run monitor
    monitor = ResearchMonitor(days_back=args.days, verbose=not args.quiet)
    monitor.run_search(sources)

    print()
    print("-" * 60)

    if not args.summary_only:
        saved = monitor.save_results()
        print(f"\nSaved {len(saved)} new papers to: {CICD_INCOMING}")

    # Print summary
    print(monitor.generate_summary())

    print("-" * 60)
    print("Monitor complete. Review papers in CICD/incoming/ folder.")
    print("Move reviewed papers to CICD/processed/ when done.")


if __name__ == '__main__':
    main()
