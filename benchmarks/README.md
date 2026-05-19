# A.I.M. Benchmarks & Proof Logs

This directory serves as the centralized hub for reproducing the mathematical performance of the A.I.M. Memory module against rigorous academic datasets. 

Because A.I.M. is designed to operate as an exoskeleton wrapping around specific CLI tools, the benchmarking execution scripts are grouped by the underlying agent framework being tested.

## 📁 Directory Structure

### `/geminicli`
Contains all execution scripts, LanceDB ingestion logic, and immutable JSON proof logs specific to the core A.I.M. engine running the official **Google Gemini CLI**.
*   **[LongMemEval (RAG 5.21)](geminicli/longmemeval_scripts/README.md):** The scripts used to achieve the verified **95.6% Recall@5** score on the massive 19,195-session ICLR 2025 dataset.

### `/opencode`
Contains all execution scripts, TUI spawners, and evaluators adapted for the `aim-opencode` fork, which tests the A.I.M. architecture using DeepSeek V4 and Claude.

---

> **⚠️ Note on Databases:**
> The `benchmarks/databases/` directory (which houses the 500MB+ compiled LanceDB columnar vectors) is explicitly ignored by Git. 
> To reproduce the benchmarks, you must first execute the corresponding ingestion scripts (e.g., `build_memeval_lance.py`) to generate the local database on your machine before running the evaluators.
