# Browser-Use dengan Ollama (qwen3.5:cloud)

🤖 AI Browser Automation menggunakan Browser-Use + Ollama

## ✅ Status

- [x] Browser-Use 0.12.5 installed
- [x] Custom MCP Server created
- [x] DuckDuckGo Search Engine (No CAPTCHA)
- [x] Batch files for easy access
- [x] GitHub repo initialized

## 📁 Struktur Fail

```
D:\BrowseUse\
├── browseuse.bat         # 🆕 Main menu (double-click to run)
├── quick_search.bat      # 🆕 Quick search shortcut
├── search_engine.py      # 🆕 DuckDuckGo search tool
├── agent.py              # Main automation script
├── test_simple.py        # Simple test script
├── test_browser_visible.py
├── run.bat               # Old menu
├── requirements.txt
├── .env.example
├── .gitignore
│
└── mcp_server/           # 🆕 Custom MCP Server
    ├── mcp_server.py     # 8 MCP tools
    ├── pyproject.toml
    └── README.md
```

## 🚀 Cara Guna

### Option 1: Batch Menu (Termudah)

```bash
# Double-click browseuse.bat
# atau run dalam terminal:
browseuse.bat
```

Menu:
```
[1] 🔍 Web Search      - Search DuckDuckGo
[2] ⭐ GitHub Stats     - Get repository info
[3] 📄 Extract Website  - Scrape data from URL
[4] 📝 Fill Web Form    - Auto-fill forms
[5] 📰 News Search      - Search news articles
[6] 🖼️  Image Search    - Find images
[7] 🔬 Deep Research    - Multi-page research
[8] 🤖 Custom Task      - Run custom automation
[9] ⚙️  Settings        - Change model/config
```

### Option 2: Quick Search

```bash
# Double-click quick_search.bat
# Enter query dan tekan Enter
```

### Option 3: Command Line

```bash
# Quick search
python search_engine.py "AI news 2026" --quick

# Normal search (5 results)
python search_engine.py "Python tutorial"

# Deep research
python search_engine.py "machine learning" --research 5

# News search
python search_engine.py "tech updates" --news

# Image search
python search_engine.py "cats" --images
```

### Option 4: MCP Server (Dalam Claude Code)

Tambah ke `~/.claude/settings.json`:
```json
{
  "enabledMcpjsonServers": ["browseros", "browseuse-local"]
}
```

Kemudian guna:
```
mcp__browseuse_local__search_and_extract("query", "extract info")
mcp__browseuse_local__github_repo_stats("owner/repo")
```

## 🤖 Model Ollama

| Model | Kegunaan |
|-------|----------|
| `qwen3.5:cloud` | **Recommended** - General tasks |
| `gemma3:27b-cloud` | Fast & lightweight |
| `deepseek-v3.2:cloud` | General purpose |
| `qwen3-coder:480b-cloud` | Coding tasks |
| `qwen3-vl:235b-instruct-cloud` | Vision tasks |

## 📦 Dependencies

```bash
pip install browser-use ollama python-dotenv mcp
```

## 🔧 Troubleshooting

### Ollama tidak running
```bash
ollama serve
```

### Model tidak found
```bash
ollama pull qwen3.5:cloud
```

### Browser tidak nampak
- Set `headless=False` dalam script
- Check ada Chrome/Chromium installed

### CAPTCHA issues
- Script guna DuckDuckGo (tiada CAPTCHA)
- Jika perlu Google, guna Browser Use Cloud

## 📚 Resources

- GitHub Repo: https://github.com/kamkikorich/WajuTechBrowseUse
- Browser-Use: https://github.com/browser-use/browser-use
- Docs: https://docs.browser-use.com
- Ollama: https://ollama.com

## 📝 Contoh Tasks

```
# Web search
"Latest AI news 2026"

# GitHub stats
"github.com/browser-use/browser-use stars forks issues"

# Extract data
"Go to amazon.com and find best laptop under $500"

# Fill form
"Fill contact form with name: John, email: john@example.com"

# Research
"Climate change effects in 2026" --research 5
```

---

**Made with ❤️ for AI Browser Automation**