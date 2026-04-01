# Browser-Use dengan Ollama (qwen3.5:cloud)

🤖 AI Browser Automation menggunakan Browser-Use + Ollama

## ✅ Status Pemasangan

- [x] Browser-Use 0.12.5 installed
- [x] Dependencies installed
- [x] Test berjaya dijalankan
- [x] File github_stats.txt created

## 📋 Struktur Fail

```
D:\BrowseUse\
├── agent.py           # Main script dengan 6 contoh tasks
├── test_simple.py     # Simple test script (pilih test 1/2/3)
├── requirements.txt   # Python dependencies
├── .env.example      # Template environment variables
└── README_BrowserUse.md  # Dokumentasi ini
```

## 🚀 Cara Jalankan

### Option 1: Simple Test (Recommended untuk first run)

```bash
python test_simple.py
```

Menu akan muncul:
```
Select test to run:
1. GitHub Stars Test (simple)
2. Google Search Test
3. Exit

Enter choice (1/2/3):
```

### Option 2: Full Agent Script

```bash
python agent.py
```

## 📦 Dependencies

Semua dependencies dah install:
- browser-use 0.12.5
- python-dotenv 1.2.1
- ollama 0.6.1
- anthropic 0.76.0
- openai 2.16.0
- google-genai 1.65.0
- Dan lain-lain...

## 🤖 Model Ollama Tersedia

Dari list anda, model yang sesuai untuk Browser-Use:

| Model | Saiz | Kegunaan |
|-------|------|----------|
| `qwen3.5:cloud` | - | **PILIHAN UTAMA** - Balance speed & accuracy |
| `qwen3-coder:480b-cloud` | 480B | Coding tasks yang kompleks |
| `qwen3-vl:235b-instruct-cloud` | 235B | Vision + Language tasks |
| `devstral-2:123b-cloud` | 123B | Development tasks |
| `gemma3:27b-cloud` | 27B | Ringan, pantas |
| `deepseek-v3.2:cloud` | - | General purpose |

## 🔧 Cara Tukar Model

Edit file `agent.py` atau `test_simple.py`:

```python
llm = ChatOllama(model="qwen3.5:cloud")  # Tukar model di sini
```

Contoh:
```python
llm = ChatOllama(model="qwen3-coder:480b-cloud")
llm = ChatOllama(model="gemma3:27b-cloud")
llm = ChatOllama(model="devstral-2:123b-cloud")
```

## 📝 Contoh Tasks Yang Ada

### 1. GitHub Stats (Default)
```python
task="Buka GitHub dan cari repository browser-use. Cari jumlah stars, forks, dan issues."
```

### 2. Web Search
```python
task="Search for 'AI news today' on Google and summarize the top 5 results"
```

### 3. Form Fill
```python
task="Go to https://httpbin.org/forms/post and fill out the form with sample data"
```

### 4. E-commerce
```python
task="Search for 'mechanical keyboard' on Amazon and find the top 3 products"
```

### 5. Data Extraction
```python
task="Go to hackernews.com, extract the top 10 posts with titles and points"
```

### 6. Custom Tools
```python
@tools.action(description="Save data to file")
def save_to_file(filename: str, content: str):
    with open(filename, "w") as f:
        f.write(content)
```

## ⚙️ Browser Configuration

```python
browser = Browser(
    headless=False,              # False = browser nampak
    user_data_dir="./profile",   # Save cookies/session (optional)
    disable_security=True,       # Disable security warnings
)
```

## 🎯 Tips Untuk Prestasi Terbaik

1. **Gunakan model yang betul:**
   - `qwen3.5:cloud` - General tasks (recommended)
   - `qwen3-vl:235b-instruct-cloud` - Tasks dengan banyak images
   - `qwen3-coder:480b-cloud` - Coding/technical tasks

2. **Enable vision untuk element detection:**
   ```python
   agent = Agent(
       task="...",
       llm=llm,
       browser=browser,
       use_vision=True,  # Enable vision
   )
   ```

3. **Save session untuk reuse cookies:**
   ```python
   browser = Browser(
       user_data_dir="./browser_profile",
   )
   ```

4. **Headless mode untuk production:**
   ```python
   browser = Browser(headless=True)  # Hidden browser
   ```

## 🔧 Troubleshooting

### Error: "Connection refused" / "Cannot connect to Ollama"
```bash
# Pastikan Ollama running
ollama serve
```

### Error: "Model not found"
```bash
# Pull model
ollama pull qwen3.5:cloud
```

### Error: Encoding issues di Windows
Script dah ada fix untuk Windows console encoding.

### Browser tak buka
```bash
# Reinstall Chromium
uvx browser-use install
```

## 📚 Resources

- GitHub: https://github.com/browser-use/browser-use
- Docs: https://docs.browser-use.com
- Ollama: https://ollama.com
- Supported Models: https://docs.browser-use.com/open-source/supported-models

## 🎓 Contoh Penggunaan Sebenar

### Auto Apply Job
```python
task="Fill in this job application with my resume and information"
```

### Grocery Shopping
```python
task="Put this list of items into my instacart: milk, eggs, bread"
```

### Research
```python
task="Find the latest news about quantum computing and summarize"
```

### Price Comparison
```python
task="Find the best price for iPhone 15 Pro across Amazon, Best Buy, and Apple Store"
```

## ⚠️ Important Notes

1. **Telemetry**: Browser-Use collect anonymized telemetry by default
2. **API Usage**: Ollama models are free (run locally)
3. **Browser**: Chromium akan auto-download masa first run
4. **Session**: Cookies saved jika guna `user_data_dir`

## 📞 Support

Jika ada masalah:
1. Check Ollama running: `ollama list`
2. Check model available: `ollama ps`
3. Restart Ollama: `ollama serve`

---

**Made with ❤️ for Browser Automation**
