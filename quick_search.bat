@echo off
chcp 65001 >nul
REM Quick Search - BrowseUse
REM Usage: Double-click and enter query, or drag this file to desktop

set /p query="🔍 Enter search query: "
if "%query%"=="" (
    echo No query entered!
    timeout /t 2 >nul
    exit
)

echo.
echo Searching DuckDuckGo for: %query%
echo.
python "%~dp0search_engine.py" "%query%" --quick
echo.
pause