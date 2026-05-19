# Gemini CLI Benchmark Ecosystem

This directory contains the testing harnesses and ingestion scripts specifically designed to evaluate the A.I.M. architecture when it is wrapping the official **Google Gemini CLI**.

## 📁 Directory Contents

### `/locomo-v2`
Contains the execution scripts, evaluators, and runners used to test the A.I.M. system against the LoCoMo V2 (Long-term Conversational Memory) dataset. It utilizes Ghost Operator scripts to simulate human interactions over long context windows.

### `/longmemeval_scripts`
Contains the RAG 5.21 ingestion pipelines and mathematical proof generators used to evaluate A.I.M. against the rigorous 19,195-session LongMemEval benchmark, achieving the 95.6% Recall@5 score.