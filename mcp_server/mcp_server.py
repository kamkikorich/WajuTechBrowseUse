"""
BrowseUse MCP Server - AI Browser Automation with Ollama
Custom MCP server for browser-use integration

Run with: python mcp_server.py
Or: uv run mcp run mcp_server.py
"""

from mcp.server.fastmcp import FastMCP
from browser_use import Agent, ChatOllama, Browser
from typing import Optional, List
import asyncio
import json
import sys
import os

# Fix Windows encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Create MCP Server
mcp = FastMCP(
    "BrowseUse",
    title="BrowseUse MCP Server",
    description="AI Browser Automation with Ollama - Automate web tasks using local LLM",
    instructions="""
    Use this server to automate browser tasks with local Ollama models.

    Available models: qwen3.5:cloud, gemma3:27b-cloud, deepseek-v3.2:cloud

    Example tasks:
    - Extract data from websites
    - Fill forms automatically
    - Search and scrape web pages
    - Navigate and interact with web apps
    """,
    json_response=True
)

# Global browser instance
_browser: Optional[Browser] = None
# Kimi K2.5 - Best for browser automation
_current_model: str = "kimi-k2.5:cloud"


def get_browser(headless: bool = False) -> Browser:
    """Get or create browser instance"""
    global _browser
    if _browser is None:
        _browser = Browser(
            headless=headless,
            disable_security=True,
        )
    return _browser


def get_llm(model: str = None) -> ChatOllama:
    """Get LLM instance"""
    model = model or _current_model
    return ChatOllama(model=model)


# ============================================
# TOOLS - Browser Automation
# ============================================

@mcp.tool()
async def browse_task(
    task: str,
    model: str = "qwen3.5:cloud",
    headless: bool = False,
    max_steps: int = 20
) -> str:
    """
    Execute a browser automation task using AI.

    Args:
        task: The task to perform (e.g., "Go to GitHub and find trending repos")
        model: Ollama model to use (default: qwen3.5:cloud)
        headless: Run browser in background (default: False = visible)
        max_steps: Maximum automation steps (default: 20)

    Returns:
        Task result as string
    """
    try:
        browser = get_browser(headless)
        llm = get_llm(model)

        agent = Agent(
            task=task,
            llm=llm,
            browser=browser,
            use_vision=True,
            max_actions_per_step=5,
            max_failures=3,
        )

        result = await agent.run()

        # Clean result for Windows console
        result_str = str(result)
        if sys.platform == 'win32':
            result_str = ''.join(c for c in result_str if c.isascii() or c in 'éèêëàâäùûüôöîïç')

        return f"Task completed: {result_str[:2000]}"

    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
async def extract_website_data(
    url: str,
    extract_task: str,
    model: str = "qwen3.5:cloud"
) -> str:
    """
    Navigate to a URL and extract specific data.

    Args:
        url: Website URL to navigate to
        extract_task: What data to extract (e.g., "Get all product prices")
        model: Ollama model to use

    Returns:
        Extracted data as string
    """
    task = f"Go to {url} and {extract_task}"
    return await browse_task(task, model, headless=False)


@mcp.tool()
async def search_and_extract(
    search_query: str,
    extract_info: str,
    model: str = "qwen3.5:cloud"
) -> str:
    """
    Search Google and extract information from results.

    Args:
        search_query: What to search for
        extract_info: What information to extract
        model: Ollama model to use

    Returns:
        Extracted information
    """
    task = f"Search Google for '{search_query}' and {extract_info}"
    return await browse_task(task, model, headless=False)


@mcp.tool()
async def fill_web_form(
    url: str,
    form_data: str,
    model: str = "qwen3.5:cloud"
) -> str:
    """
    Navigate to a URL and fill out a form.

    Args:
        url: Form URL
        form_data: JSON string with form field values
        model: Ollama model to use

    Returns:
        Result of form submission
    """
    task = f"Go to {url} and fill the form with this data: {form_data}. Then submit the form."
    return await browse_task(task, model, headless=False)


@mcp.tool()
async def github_repo_stats(
    repo_name: str,
    model: str = "qwen3.5:cloud"
) -> str:
    """
    Get GitHub repository statistics.

    Args:
        repo_name: Repository name (e.g., "browser-use/browser-use")
        model: Ollama model to use

    Returns:
        Repository stats (stars, forks, issues)
    """
    task = f"Go to github.com/{repo_name} and get the number of stars, forks, and open issues"
    return await browse_task(task, model, headless=False)


@mcp.tool()
async def close_browser() -> str:
    """
    Close the current browser instance.
    """
    global _browser
    if _browser:
        try:
            await _browser.kill()
            _browser = None
            return "Browser closed successfully"
        except Exception as e:
            return f"Error closing browser: {str(e)}"
    return "No browser instance to close"


# ============================================
# TOOLS - Configuration
# ============================================

@mcp.tool()
def set_model(model: str) -> str:
    """
    Set the default Ollama model.

    Args:
        model: Model name (e.g., qwen3.5:cloud, gemma3:27b-cloud)

    Returns:
        Confirmation message
    """
    global _current_model
    _current_model = model
    return f"Model set to: {model}"


@mcp.tool()
def list_available_models() -> str:
    """
    List available Ollama models for browser automation.
    """
    models = [
        "kimi-k2.5:cloud - RECOMMENDED for browser automation",
        "deepseek-v3.2:cloud - Alternative for general tasks",
        "qwen3.5:cloud - General purpose",
        "qwen3-coder:480b-cloud - Coding tasks",
        "gemma3:27b-cloud - Fast and lightweight",
    ]
    return "Available models:\n" + "\n".join(f"- {m}" for m in models)


@mcp.tool()
def get_server_status() -> str:
    """
    Get current server status and configuration.
    """
    status = {
        "server": "BrowseUse MCP Server",
        "version": "1.0.0",
        "current_model": _current_model,
        "browser_active": _browser is not None,
        "platform": sys.platform,
    }
    return json.dumps(status, indent=2)


# ============================================
# RESOURCES
# ============================================

@mcp.resource("browseuse://config")
def get_config() -> str:
    """Get server configuration"""
    return json.dumps({
        "default_model": _current_model,
        "browser_profile": "./browser_profile",
        "supported_tasks": [
            "Web scraping",
            "Form filling",
            "Data extraction",
            "Search and summarize",
            "GitHub stats",
        ]
    }, indent=2)


@mcp.resource("browseuse://models")
def get_models_resource() -> str:
    """Get available models"""
    return json.dumps({
        "recommended": "qwen3.5:cloud",
        "models": [
            {"name": "qwen3.5:cloud", "type": "general", "recommended": True},
            {"name": "qwen3-coder:480b-cloud", "type": "coding"},
            {"name": "qwen3-vl:235b-instruct-cloud", "type": "vision"},
            {"name": "gemma3:27b-cloud", "type": "fast"},
        ]
    }, indent=2)


# ============================================
# PROMPTS
# ============================================

@mcp.prompt()
def web_scraping_prompt(url: str, data_to_extract: str) -> str:
    """Generate a web scraping prompt"""
    return f"""
    Please help me scrape data from {url}.

    I want to extract: {data_to_extract}

    Use the browse_task tool to:
    1. Navigate to the URL
    2. Find and extract the requested data
    3. Return it in a structured format
    """


@mcp.prompt()
def form_filling_prompt(url: str) -> str:
    """Generate a form filling prompt"""
    return f"""
    I need to fill out a form at {url}.

    Please:
    1. Use the fill_web_form tool
    2. Provide the form data as JSON
    3. Submit the form
    """


@mcp.prompt()
def research_prompt(topic: str) -> str:
    """Generate a research prompt"""
    return f"""
    Research the topic: {topic}

    Use search_and_extract to:
    1. Search for relevant information
    2. Extract key facts and data
    3. Summarize findings
    """


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("BrowseUse MCP Server Starting...")
    print("=" * 50)
    print(f"Default Model: {_current_model}")
    print(f"Platform: {sys.platform}")
    print("=" * 50)

    # Run with stdio transport (for Claude Code)
    mcp.run(transport="stdio")