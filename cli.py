import argparse
from pubmed_paper_fetcher.fetcher import search_pubmed, fetch_details, save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results")

    args = parser.parse_args()

    if args.debug:
        print(f"Searching for query: {args.query}")

    ids = search_pubmed(args.query)
    if args.debug:
        print(f"Found {len(ids)} IDs")

    data = fetch_details(ids)
    if args.debug:
        print(f"Fetched {len(data)} papers with non-academic authors")

    if args.file:
        save_to_csv(data, args.file)
        print(f"Results saved to {args.file}")
    else:
        for entry in data:
            print(entry)

if __name__ == "__main__":
    main()
