# LoCoMo V2 Benchmarking Suite (Gemini CLI)

This folder contains the specific evaluation tools designed to test A.I.M. against the LoCoMo V2 dataset. Because A.I.M. is an interactive CLI agent, it cannot be tested using standard programmatic APIs. Instead, these scripts spin up "Ghost Operators" that physically type questions into a terminal.

## 📁 Subdirectories

### `/runners`
The core execution engines that orchestrate the benchmark.
*   **`locomo_v2_runner.py`**: The primary runner. It launches a headless `tmux` session, loads the A.I.M. agent, and uses state-aware JSONL parsing to dynamically inject the benchmark questions and wait for the `[ANSWER]` tag.
*   **`ghost_runner_resume.py`**: A resilient version of the runner designed to pick up execution exactly where it left off in the event of a catastrophic API crash or rate limit block.
*   **`build_locomo_lance.py`**: The ingestion script that parses the raw LoCoMo transcripts and embeds them into LanceDB using speaker-boundary chunking.
*   **`benchmark_tracker.py`**: A utility script used to monitor the live progress of a running benchmark session.

### `/evaluators`
The grading logic. Once the `runners` have collected all the generated answers, the scripts in this folder use a deterministic or LLM-based judge to score the agent's performance against the official Ground Truth cheatsheets.
*   **`ghost_judge_pro_tmux.py`**: A specialized evaluator that grades the final output files.