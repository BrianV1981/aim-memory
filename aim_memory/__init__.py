import os
import json
from typing import List, Dict, Any, Optional

from .engine import VectorBackend
from .embeddings import get_embedding
from .retrieval import perform_search_internal

class MemoryClient:
    """
    A unified API client for the A.I.M. RAG 5.21 Memory Engine.
    Powered by LanceDB, Nomic Embeddings (Ollama), and Tantivy FTS.
    """
    from typing import Callable

    def __init__(self, db_path: str = "./memory_lance", embedding_task: str = "RETRIEVAL_DOCUMENT", embedding_fn: Callable = None):
        self.embedding_fn = embedding_fn
        self.db_path = db_path
        self.embedding_task = embedding_task
        self.backend = VectorBackend(path=self.db_path)
        self.table = self.backend.get_table()

    def search(self, query: str, top_k: int = 10, session_filter: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Executes a native Hybrid Search (Vector + FTS) using the EntityIntersectionReranker
        with a 1.5x proper-noun multiplier.
        """
        return perform_search_internal(query, top_k=top_k, session_filter=session_filter, db_path=self.db_path, embedding_fn=self.embedding_fn)

    def ingest_text(self, text: str, session_id: str, metadata: Dict[str, Any] = None) -> bool:
        """
        Chunks and natively embeds a raw string of text into the database.
        """
        metadata = metadata or {}
        # Basic 1000-char chunking if not pre-chunked
        chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
        
        records = []
        df = self.table.to_pandas() if self.table else None
        rid = int(df['fragment_id'].max()) + 1 if (df is not None and not df.empty and 'fragment_id' in df.columns) else 0

        for chunk in chunks:
            vec = self.embedding_fn(chunk) if self.embedding_fn else get_embedding(chunk, task_type=self.embedding_task)
            if vec:
                records.append({
                    "fragment_id": rid,
                    "session_id": session_id,
                    "type": "modular_ingest",
                    "content": chunk,
                    "timestamp": "",
                    "metadata": json.dumps(metadata),
                    "parent_id": 0,
                    "source_db": "aim_memory",
                    "vector": vec
                })
                rid += 1

        if records:
            self.table.add(records)
            self.table.create_fts_index("content", replace=True)
            return True
        return False
