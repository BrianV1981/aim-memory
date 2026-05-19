# LoCoMo V2 Benchmarking Suite (OpenCode)

This folder houses the specialized runners and evaluators built to test the `aim-opencode` fork (powered by DeepSeek V4) on the LoCoMo V2 benchmark.

## 📁 Subdirectories & Files

### `/runners`
*   **`opencode_ghost_operator_v2.py`**: The main execution engine. It spawns the OpenCode TUI in a headless `tmux` session, injects the benchmark prompts, and monitors the log files. It features specific handling for OpenCode's `deepseek-chat` model invocation.
*   **`opencode_continuation.py`**: A specialized script designed to handle context continuation or recovery during massive multi-session evaluation runs.
*   **`opencode_build_locomo_lance.py`**: The tailored LanceDB ingestion pipeline optimized for OpenCode's specific data structures.

### `/evaluators`
*   **`opencode_ghost_judge_v2.py`**: The scoring mechanism used to grade the final OpenCode JSON outputs against the LoCoMo V2 ground truth.

### Configuration
*   **`opencode_AGENTS.md`**: The specific system prompt and mandate definitions used by the OpenCode agent during the benchmark run. It overrides the default A.I.M. rules to instruct the agent on how to use DeepSeek-specific tools.