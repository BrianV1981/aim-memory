# A.I.M. Benchmark Databases

This directory is the designated storage hub for all compiled LanceDB vector databases used during evaluation. 

> **⚠️ GIT IGNORED:** 
> The contents of this directory (with the exception of this README) are explicitly ignored by Git. 

## Why is this ignored?
A fully embedded RAG 5.21 LanceDB database containing 100,000+ vector fragments typically exceeds 500MB in size. Tracking these binary artifacts in version control would bloat the repository and trigger immediate GitHub Large File Storage (LFS) rejections.

## How to populate this folder
If you cloned this repository and wish to run the benchmarks, you must generate the databases locally on your own machine. 
Navigate to the specific benchmark script folder (e.g., `benchmarks/geminicli/longmemeval_scripts/`) and execute the ingestion pipeline (e.g., `build_memeval_lance.py`). The script will automatically compile the vectors and save the `.lance` database files into this directory.