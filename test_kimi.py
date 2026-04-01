"""
Test BrowseUse with Kimi K2.5 Model
"""

from browser_use import Agent, ChatOllama, Browser
import asyncio
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


async def test_kimi():
    browser = Browser(
        headless=False,
        disable_security=True,
    )

    # Use Kimi K2.5
    llm = ChatOllama(model="kimi-k2.5:cloud")

    task = """
    Go to https://duckduckgo.com/?q=perkeso+keningau

    Look at the search results.

    Extract the TOP 5 results with:
    - Title
    - URL
    - Brief description

    Return as a numbered list.

    Do NOT click any links - just read the search results page.
    """

    print("\n" + "="*60)
    print("Testing Kimi K2.5 with BrowseUse")
    print("="*60)
    print("\nModel: kimi-k2.5:cloud")
    print("Query: perkeso keningau")
    print("\n" + "-"*60)

    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
        use_vision=True,
        max_actions_per_step=10,
    )

    result = await agent.run()

    # Clean output
    result_str = str(result)
    if sys.platform == 'win32':
        result_str = ''.join(c for c in result_str if c.isascii() or c in 'éèêëàâäùûüôöîïç')

    print("\n" + "="*60)
    print("RESULTS:")
    print("="*60)
    print(result_str[:3000])

    await browser.kill()


if __name__ == "__main__":
    asyncio.run(test_kimi())