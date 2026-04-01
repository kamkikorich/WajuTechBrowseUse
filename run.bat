@echo off
chcp 65001 >nul
color 0A
title Browser-Use Automation

:MENU
cls
echo ============================================================
echo          🤖 BROWSER-USE AUTOMATION WITH OLLAMA
echo ============================================================
echo.
echo   Model: qwen3.5:cloud
echo   Location: D:\BrowseUse
echo.
echo ============================================================
echo                      MAIN MENU
echo ============================================================
echo.
echo   [1] 🧪 Test Browser Visible (Google.com)
echo       - Buka browser dan navigate ke Google
echo       - Verify browser nampak
echo.
echo   [2] ⭐ GitHub Stars Test (Simple)
echo       - Cari GitHub repo browser-use
echo       - Extract stars, forks, issues
echo.
echo   [3] 🚀 Full Agent Test
echo       - Complete automation task
echo       - Save results to file
echo.
echo   [4] 📋 Check Ollama Status
echo       - Verify Ollama running
echo       - Check models available
echo.
echo   [5] 🔧 Install/Repair Dependencies
echo       - Reinstall Python packages
echo       - Fix Chromium browser
echo.
echo   [6] 📖 View Documentation
echo       - Open README file
echo.
echo   [0] ❌ Exit
echo.
echo ============================================================
set /p choice="Enter your choice (0-6): "

if "%choice%"=="1" goto TEST_BROWSER
if "%choice%"=="2" goto GITHUB_TEST
if "%choice%"=="3" goto FULL_AGENT
if "%choice%"=="4" goto CHECK_OLLAMA
if "%choice%"=="5" goto INSTALL_DEPS
if "%choice%"=="6" goto VIEW_DOCS
if "%choice%"=="0" goto EXIT

echo.
echo ❌ Invalid choice! Please enter 0-6
timeout /t 2 >nul
goto MENU

:TEST_BROWSER
cls
echo ============================================================
echo 🧪 BROWSER VISIBILITY TEST
echo ============================================================
echo.
echo Starting browser test...
echo Browser akan terbuka dalam beberapa saat.
echo.
echo Press Ctrl+C to cancel
echo.
timeout /t 3 >nul
python test_browser_visible.py
echo.
echo Test completed!
pause
goto MENU

:GITHUB_TEST
cls
echo ============================================================
echo ⭐ GITHUB STARS TEST
echo ============================================================
echo.
echo Starting GitHub extraction test...
echo.
echo Browser akan terbuka dan:
echo   1. Navigate ke GitHub
echo   2. Cari browser-use repository
echo   3. Extract stars, forks, issues
echo   4. Save ke file
echo.
timeout /t 3 >nul
python test_simple.py
echo.
echo Test completed!
pause
goto MENU

:FULL_AGENT
cls
echo ============================================================
echo 🚀 FULL AGENT TEST
echo ============================================================
echo.
echo Starting full automation...
echo.
echo This will:
echo   1. Buka GitHub
echo   2. Cari browser-use repo
echo   3. Extract semua stats
echo   4. Save ke github_stats.txt
echo.
timeout /t 3 >nul
python agent.py
echo.
echo Automation completed!
pause
goto MENU

:CHECK_OLLAMA
cls
echo ============================================================
echo 📋 CHECK OLLAMA STATUS
echo ============================================================
echo.
echo Checking Ollama installation...
echo.
ollama --version
echo.
echo Checking running models...
ollama ps
echo.
echo Checking available models...
ollama list
echo.
echo ============================================================
echo.
set /p check="Start Ollama serve now? (Y/N): "
if /i "%check%"=="Y" (
    echo.
    echo Starting Ollama serve...
    echo Press Ctrl+C to stop
    echo.
    ollama serve
) else (
    echo Skipping Ollama serve
)
pause
goto MENU

:INSTALL_DEPS
cls
echo ============================================================
echo 🔧 INSTALL/REPAIR DEPENDENCIES
echo ============================================================
echo.
echo This will:
echo   1. Reinstall Python dependencies
echo   2. Reinstall Chromium browser
echo.
echo Make sure you have internet connection!
echo.
set /p confirm="Continue? (Y/N): "
if /i not "%confirm%"=="Y" goto MENU

echo.
echo Step 1: Installing Python dependencies...
pip install -r requirements.txt --upgrade
echo.
echo Step 2: Installing Chromium browser...
uvx browser-use install
echo.
echo ============================================================
echo ✅ Installation completed!
echo ============================================================
pause
goto MENU

:VIEW_DOCS
cls
echo ============================================================
echo 📖 DOCUMENTATION
echo ============================================================
echo.
echo Opening README file...
echo.
type README_BrowserUse.md
echo.
echo ============================================================
pause
goto MENU

:EXIT
cls
echo.
echo ============================================================
echo   👋 Thank you for using Browser-Use Automation!
echo ============================================================
echo.
timeout /t 2 >nul
exit
