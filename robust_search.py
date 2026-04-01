"""
Robust Search - Fixed version that handles errors better
"""

from browser_use import Agent, ChatOllama, Browser
import asyncio
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


async def robust_search(query: str, max_retries: int = 2):
    """
    More robust search with retry logic and simpler tasks
    """
    browser = Browser(
        headless=False,
        disable_security=True,
    )

    llm = ChatOllama(model="qwen3.5:cloud")

    # SIMPLER TASK - Just extract search results, don't visit pages
    # This avoids navigation errors
    simple_task = f"""
    Go to https://duckduckgo.com/?q={query.replace(' ', '+')}

    Look at the search results page.

    Extract the TOP 5 results with:
    - Title
    - URL
    - Brief description from snippet

    Return as a numbered list.

    IMPORTANT: Do NOT click any links. Just read the search results page.
    """

    print(f"\n{'='*60}")
    print(f"Searching: {query}")
    print(f"{'='*60}\n")

    for attempt in range(max_retries):
        try:
            agent = Agent(
                task=simple_task,
                llm=llm,
                browser=browser,
                use_vision=True,
                max_actions_per_step=8,  # Fewer steps = less chance of error
                max_failures=2,           # Fail fast
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
            return result_str

        except Exception as e:
            print(f"\nAttempt {attempt + 1} failed: {str(e)[:100]}")
            if attempt < max_retries - 1:
                print("Retrying...")
                await asyncio.sleep(2)
            else:
                print("\nAll retries failed. Here's a simpler approach...")

    await browser.kill()
    return None


async def deep_search_single_page(query: str, result_index: int = 0):
    """
    Visit ONE specific result page (more reliable)
    """
    browser = Browser(headless=False, disable_security=True)
    llm = ChatOllama(model="qwen3.5:cloud")

    task = f"""
    Step 1: Go to https://duckduckgo.com/?q={query.replace(' ', '+')}
    Step 2: Find result number {result_index + 1} in the search results
    Step 3: Click on it to visit the page
    Step 4: Read and summarize the main content
    Step 5: Return a summary of what you found
    """

    agent = Agent(task=task, llm=llm, browser=browser, use_vision=True)
    result = await agent.run()
    await browser.kill()
    return str(result)


async def main():
    if len(sys.argv) < 2:
        print("\nRobust Search - Handles errors better")
        print("="*50)
        print("\nUsage:")
        print('  python robust_search.py "your query"')
        print('  python robust_search.py "perkeso keningau"')
        print()
        return

    query = " ".join(sys.argv[1:])
    await robust_search(query)


if __name__ == "__main__":
    asyncio.run(main())