from aim_memory import MemoryClient

def main():
    print("🚀 Initializing A.I.M. Memory Engine (LanceDB + Ollama)...")
    # Initialize the client. This automatically connects to (or creates) the LanceDB at the given path.
    mem = MemoryClient(db_path="./example_memory_db")

    print("\n📚 Ingesting sample data...")
    # Ingest some dummy data
    mem.ingest_text(
        text="Jack went camping in the mountains last July and caught a huge fish.",
        session_id="session_001",
        metadata={"source": "user_diary"}
    )
    mem.ingest_text(
        text="Jessica went camping in the forest last June and saw a bear.",
        session_id="session_002",
        metadata={"source": "user_diary"}
    )
    print("✅ Data ingested and natively embedded!")

    print("\n🔍 Executing Hybrid Search (Query: 'Who went camping?')")
    # Standard search (no proper noun multiplier triggered)
    results = mem.search(query="who went camping?", top_k=2)
    for i, res in enumerate(results):
        print(f"[Rank {i+1}] Score: {res.get('score'):.4f} | {res.get('content')}")

    print("\n🔍 Executing RAG 5.21 Search (Query: 'When did Jessica go camping?')")
    # This query contains the Proper Noun 'Jessica', which triggers the 1.5x Entity Reranker multiplier!
    results = mem.search(query="When did Jessica go camping?", top_k=2)
    for i, res in enumerate(results):
        print(f"[Rank {i+1}] Score: {res.get('score'):.4f} | {res.get('content')}")

    print("\n🎉 Quickstart complete!")

if __name__ == "__main__":
    main()
