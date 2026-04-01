"""
Browser-Use as Search Engine
Replace Chrome with AI-powered search using DuckDuckGo (no CAPTCHA)

Run: python search_engine.py "your search query"
"""

from browser_use import Agent, ChatOllama, Browser
import asyncio
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# DuckDuckGo - No CAPTCHA, privacy-focused
SEARCH_ENGINE = "https://duckduckgo.com"


# Kimi K2.5 - Best for browser automation tasks
DEFAULT_MODEL = "kimi-k2.5:cloud"


async def search(query: str, model: str = None):
    """
    Search the web using AI browser automation.
    Uses DuckDuckGo to avoid CAPTCHA issues.
    """
    model = model or DEFAULT_MODEL
    browser = Browser(
        headless=False,
        disable_security=True,
    )

    llm = ChatOllama(model=model)

    # Use DuckDuckGo directly - no CAPTCHA
    task = f"""
    Go to {SEARCH_ENGINE} and search for '{query}'.
    Extract the top 5 search results with:
    - Title
    - URL
    - Brief description

    Format as a clean numbered list.
    """

    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
        use_vision=True,
        max_actions_per_step=10,
    )

    print(f"\n🔍 Searching for: {query}")
    print("=" * 50)

    result = await agent.run()

    # Clean result
    result_str = str(result)
    if sys.platform == 'win32':
        result_str = ''.join(c for c in result_str if c.isascii() or c in 'éèêëàâäùûüôöîïç')

    print("\n📋 Results:")
    print("=" * 50)
    print(result_str[:3000])

    await browser.kill()
    return result_str


async def quick_search(query: str):
    """
    Quick search - extract just the key info
    """
    browser = Browser(headless=False, disable_security=True)
    llm = ChatOllama(model=DEFAULT_MODEL)

    # Direct URL to DuckDuckGo search
    search_url = f"{SEARCH_ENGINE}/?q={query.replace(' ', '+')}"

    task = f"""
    Go to {search_url} and extract the top 3 search results.
    Return only: Title and URL for each result.
    """

    agent = Agent(task=task, llm=llm, browser=browser, use_vision=True)
    result = await agent.run()

    await browser.kill()
    return str(result)


async def research(query: str, depth: int = 3):
    """
    Deep research - visit multiple pages and summarize
    """
    browser = Browser(headless=False, disable_security=True)
    llm = ChatOllama(model=DEFAULT_MODEL)

    task = f"""
    Research the topic: '{query}'

    Steps:
    1. Search on {SEARCH_ENGINE} for '{query}'
    2. Click on and visit the top {depth} result pages
    3. Extract key information from each page
    4. Create a comprehensive summary with sources

    Format:
    ## Summary
    [Key findings]

    ## Sources
    1. [Title] - [URL]: [Key info]
    2. ...
    """

    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
        use_vision=True,
        max_actions_per_step=20,
    )

    result = await agent.run()
    await browser.kill()
    return str(result)


async def news_search(query: str):
    """
    Search for news articles
    """
    browser = Browser(headless=False, disable_security=True)
    llm = ChatOllama(model=DEFAULT_MODEL)

    # DuckDuckGo news search
    search_url = f"{SEARCH_ENGINE}/?q={query.replace(' ', '+')}&iar=news"

    task = f"""
    Go to {search_url} (DuckDuckGo News search).
    Extract the top 5 news articles with:
    - Headline
    - Source
    - Date
    - URL
    - Brief summary
    """

    agent = Agent(task=task, llm=llm, browser=browser, use_vision=True)
    result = await agent.run()

    await browser.kill()
    return str(result)


async def image_search(query: str):
    """
    Search for images
    """
    browser = Browser(headless=False, disable_security=True)
    llm = ChatOllama(model=DEFAULT_MODEL)

    search_url = f"{SEARCH_ENGINE}/?q={query.replace(' ', '+')}&iax=images&ia=images"

    task = f"""
    Go to {search_url} (DuckDuckGo Images).
    Find and describe the top 5 images for '{query}'.
    Include image URLs if available.
    """

    agent = Agent(task=task, llm=llm, browser=browser, use_vision=True)
    result = await agent.run()

    await browser.kill()
    return str(result)


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\n📌 Browser-Use Search Engine (DuckDuckGo - No CAPTCHA)")
        print("=" * 50)
        print("\nUsage:")
        print("   python search_engine.py \"query\"           # Normal search")
        print("   python search_engine.py \"query\" --quick    # Quick search")
        print("   python search_engine.py \"query\" --research # Deep research")
        print("   python search_engine.py \"query\" --news     # News search")
        print("   python search_engine.py \"query\" --images   # Image search")
        print("\nExamples:")
        print("   python search_engine.py \"AI trends 2026\"")
        print("   python search_engine.py \"Python tutorial\" --quick")
        print("   python search_engine.py \"climate change\" --research")
        print("   python search_engine.py \"tech updates\" --news")
        print()
        sys.exit(1)

    query = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "normal"

    if mode == "--quick":
        asyncio.run(quick_search(query))
    elif mode == "--research":
        depth = int(sys.argv[3]) if len(sys.argv) > 3 else 3
        asyncio.run(research(query, depth))
    elif mode == "--news":
        asyncio.run(news_search(query))
    elif mode == "--images":
        asyncio.run(image_search(query))
    else:
        asyncio.run(search(query))