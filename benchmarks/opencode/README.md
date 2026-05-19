# OpenCode Fork Benchmark Ecosystem

This directory contains the testing harnesses designed for the `aim-opencode` fork. The OpenCode fork modifies the base A.I.M. architecture to utilize alternative LLMs (specifically **DeepSeek V4** and **Claude**) instead of the Google Gemini CLI.

## 📁 Directory Contents

### `/locomo-v2`
Contains the customized execution scripts, evaluators, and runners required to test the OpenCode adaptations against the LoCoMo V2 dataset. These scripts differ from the `geminicli` versions as they must interact with the distinct OpenCode TUI and its specific terminal output formatting.