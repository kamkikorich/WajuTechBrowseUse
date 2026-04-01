# BrowseUse MCP Server

AI Browser Automation MCP Server with Ollama integration.

## Features

- **8 MCP Tools** for browser automation
- **Local LLM** via Ollama (qwen3.5, gemma3, deepseek)
- **Async execution** for fast automation
- **Cross-platform** (Windows, macOS, Linux)

## Installation

```bash
# Install dependencies
pip install mcp browser-use ollama python-dotenv

# Or use uv
uv pip install -e .
```

## Usage

### With Claude Code

Add to `~/.claude.json`:

```json
{
  "mcpServers": {
    "browseuse": {
      "command": "python",
      "args": ["D:/BrowseUse/mcp_server/mcp_server.py"],
      "description": "Local browser automation with Ollama"
    }
  }
}
```

### Run Directly

```bash
python mcp_server.py
```

## Available Tools

| Tool | Description |
|------|-------------|
| `browse_task` | Execute any browser automation task |
| `extract_website_data` | Navigate to URL and extract data |
| `search_and_extract` | Search Google and extract info |
| `fill_web_form` | Fill out web forms |
| `github_repo_stats` | Get GitHub repository stats |
| `close_browser` | Close browser instance |
| `set_model` | Change Ollama model |
| `list_available_models` | List available models |
| `get_server_status` | Get server status |

## Example Tasks

```
# Web scraping
browse_task(task="Go to hackernews.com and get top 5 posts")

# Data extraction
extract_website_data(url="https://github.com", extract_task="find trending repos")

# Form filling
fill_web_form(url="https://example.com/contact", form_data='{"name": "John", "email": "john@example.com"}')

# GitHub stats
github_repo_stats(repo_name="browser-use/browser-use")
```

## Supported Models

- `qwen3.5:cloud` - Recommended for general tasks
- `qwen3-coder:480b-cloud` - Best for coding
- `qwen3-vl:235b-instruct-cloud` - Best for vision
- `gemma3:27b-cloud` - Fast and lightweight
- `deepseek-v3.2:cloud` - General purpose

## Requirements

- Python 3.10+
- Ollama running locally
- Chrome/Chromium browser