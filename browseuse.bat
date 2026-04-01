@echo off
chcp 65001 >nul
color 0A
title BrowseUse - AI Browser Automation

:MENU
cls
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║           🌐 BROWSEUSE - AI Browser Automation               ║
echo  ║              Powered by Ollama (qwen3.5:cloud)               ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
echo  ┌─────────────────────────────────────────────────────────────┐
echo  │                    📋 MAIN MENU                              │
echo  └─────────────────────────────────────────────────────────────┘
echo.
echo   [1] 🔍 Web Search          - Search DuckDuckGo
echo   [2] ⭐ GitHub Stats         - Get repository info
echo   [3] 📄 Extract Website      - Scrape data from URL
echo   [4] 📝 Fill Web Form        - Auto-fill forms
echo   [5] 📰 News Search          - Search news articles
echo   [6] 🖼️  Image Search          - Find images
echo   [7] 🔬 Deep Research        - Multi-page research
echo   [8] 🤖 Custom Task          - Run custom automation
echo   [9] ⚙️  Settings             - Change model/config
echo.
echo   [0] ❌ Exit
echo.
echo  ───────────────────────────────────────────────────────────────
set /p choice="Enter your choice (0-9): "

if "%choice%"=="1" goto SEARCH
if "%choice%"=="2" goto GITHUB
if "%choice%"=="3" goto EXTRACT
if "%choice%"=="4" goto FORM
if "%choice%"=="5" goto NEWS
if "%choice%"=="6" goto IMAGES
if "%choice%"=="7" goto RESEARCH
if "%choice%"=="8" goto CUSTOM
if "%choice%"=="9" goto SETTINGS
if "%choice%"=="0" goto EXIT

echo.
echo ❌ Invalid choice!
timeout /t 2 >nul
goto MENU

:SEARCH
cls
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                    🔍 WEB SEARCH                             ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
set /p query="Enter search query: "
echo.
echo 🔄 Searching DuckDuckGo for: %query%
echo.
python "%~dp0search_engine.py" "%query%" --quick
echo.
pause
goto MENU

:GITHUB
cls
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                    ⭐ GITHUB STATS                            ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
echo  Example: browser-use/browser-use
echo.
set /p repo="Enter repository (owner/repo): "
echo.
echo 🔄 Fetching stats for: %repo%
echo.
python "%~dp0search_engine.py" "github.com/%repo% stars forks issues" --quick
echo.
pause
goto MENU

:EXTRACT
cls
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                    📄 EXTRACT WEBSITE                         ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
set /p url="Enter website URL: "
echo.
set /p data="What data to extract?: "
echo.
echo 🔄 Extracting from: %url%
echo.
python "%~dp0search_engine.py" "Go to %url% and %data%" --quick
echo.
pause
goto MENU

:FORM
cls
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                    📝 FILL WEB FORM                           ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
set /p url="Enter form URL: "
echo.
echo Enter form data as JSON (e.g., {"name": "John", "email": "john@example.com"})
set /p data="Form data: "
echo.
echo 🔄 Filling form at: %url%
echo.
python "%~dp0search_engine.py" "Go to %url% and fill the form with: %data%" --quick
echo.
pause
goto MENU

:NEWS
cls
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                    📰 NEWS SEARCH                             ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
set /p query="Enter news topic: "
echo.
echo 🔄 Searching news for: %query%
echo.
python "%~dp0search_engine.py" "%query%" --news
echo.
pause
goto MENU

:IMAGES
cls
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                    🖼️  IMAGE SEARCH                           ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
set /p query="Enter image search: "
echo.
echo 🔄 Searching images for: %query%
echo.
python "%~dp0search_engine.py" "%query%" --images
echo.
pause
goto MENU

:RESEARCH
cls
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                    🔬 DEEP RESEARCH                           ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
set /p query="Enter research topic: "
echo.
set /p depth="How many pages to visit? (1-5, default 3): "
if "%depth%"=="" set depth=3
echo.
echo 🔄 Researching: %query% (visiting %depth% pages)
echo.
python "%~dp0search_engine.py" "%query%" --research %depth%
echo.
pause
goto MENU

:CUSTOM
cls
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                    🤖 CUSTOM TASK                             ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
echo  Enter your custom automation task.
echo  Example: "Go to Amazon and find the best laptop under $500"
echo.
set /p task="Task: "
echo.
echo 🔄 Running task: %task%
echo.
python "%~dp0search_engine.py" "%task%" --quick
echo.
pause
goto MENU

:SETTINGS
cls
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                    ⚙️  SETTINGS                               ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
echo  Current Settings:
echo  ───────────────────────────────────────────────────────────────
echo  📍 Location: %~dp0
echo  🤖 Default Model: qwen3.5:cloud
echo  🌐 Search Engine: DuckDuckGo (No CAPTCHA)
echo.
echo  Available Models:
echo    1. qwen3.5:cloud        (Recommended)
echo    2. gemma3:27b-cloud     (Fast)
echo    3. deepseek-v3.2:cloud  (General)
echo    4. qwen3-coder:480b-cloud (Coding)
echo.
echo  [1] Check Ollama Status
echo  [2] List Available Models
echo  [3] Update Dependencies
echo  [0] Back to Main Menu
echo.
set /p setchoice="Enter choice: "

if "%setchoice%"=="1" goto CHECK_OLLAMA
if "%setchoice%"=="2" goto LIST_MODELS
if "%setchoice%"=="3" goto UPDATE_DEPS
if "%setchoice%"=="0" goto MENU
goto SETTINGS

:CHECK_OLLAMA
cls
echo.
echo  📋 Ollama Status
echo  ───────────────────────────────────────────────────────────────
echo.
ollama ps
echo.
ollama list
echo.
pause
goto SETTINGS

:LIST_MODELS
cls
echo.
echo  📋 Available Ollama Models
echo  ───────────────────────────────────────────────────────────────
echo.
ollama list
echo.
pause
goto SETTINGS

:UPDATE_DEPS
cls
echo.
echo  🔄 Updating Dependencies
echo  ───────────────────────────────────────────────────────────────
echo.
pip install --upgrade browser-use ollama python-dotenv mcp
echo.
echo ✅ Dependencies updated!
echo.
pause
goto SETTINGS

:EXIT
cls
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║           👋 Thank you for using BrowseUse!                  ║
echo  ║                                                              ║
echo  ║   GitHub: https://github.com/kamkikorich/WajuTechBrowseUse   ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
timeout /t 2 >nul
exit