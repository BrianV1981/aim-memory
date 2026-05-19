#!/usr/bin/env python3
import sys
import argparse
from aim_memory import MemoryClient

def main():
    parser = argparse.ArgumentParser(description="A.I.M. Memory Module - Standalone RAG 5.21 CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Search Command
    search_parser = subparsers.add_parser("search", help="Execute a Hybrid Search against the LanceDB engine")
    search_parser.add_argument("query", type=str, help="The search query")
    search_parser.add_argument("--db", type=str, default="./memory_lance", help="Path to LanceDB database")
    search_parser.add_argument("--top_k", type=int, default=10, help="Number of results to return")

    args = parser.parse_args()

    if args.command == "search":
        client = MemoryClient(db_path=args.db)
        results = client.search(query=args.query, top_k=args.top_k)
        
        print("\n=== A.I.M. SEARCH RESULTS ===")
        for i, res in enumerate(results):
            print(f"\n[Rank {i+1}] Score: {res.get('score', 0):.4f} | Session: {res.get('session_id')}")
            print(f"{res.get('content')}")
            print("-" * 40)
        
        if not results:
            print("\nNo results found.")

if __name__ == "__main__":
    main()
