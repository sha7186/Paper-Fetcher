# PubMed Paper Fetcher

## Overview
A command-line tool to fetch PubMed research papers based on a query, identifying papers with at least one author affiliated with pharmaceutical or biotech companies.

## Features
- Search PubMed with full query support.
- Filter authors by non-academic affiliations.
- Save results to CSV or display on console.
- Typed Python with modular code.

## Installation
```bash
poetry install
```

## Usage
```bash
poetry run get-papers-list "cancer immunotherapy" -f results.csv --debug
```

## Tools Used
- [PubMed API](https://www.ncbi.nlm.nih.gov/home/develop/api/)
- [Poetry](https://python-poetry.org/)

## Structure
- `fetcher.py`: Core module for fetching and filtering.
- `cli.py`: Command-line interface.
- `pyproject.toml`: Dependency management.

## Heuristics for Non-Academic Authors
Affiliations were analyzed for keywords common in pharma/biotech companies. Email addresses were also used to detect corresponding authors.

