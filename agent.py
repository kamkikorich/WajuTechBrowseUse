from browser_use import Agent, ChatOllama, Browser, Tools
import asyncio
import sys
from dotenv import load_dotenv

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()


async def main():
    # ============================================
    # 1. BROWSER CONFIGURATION
    # ============================================
    browser = Browser(
        headless=False,              # False = browser nampak, True = hidden
        user_data_dir="./browser_profile",  # Save cookies/session
        disable_security=True,       # Disable security for automation
    )

    # ============================================
    # 2. LLM CONFIGURATION (Ollama - Kimi K2.5)
    # ============================================
    llm = ChatOllama(
        model="kimi-k2.5:cloud",
    )

    # ============================================
    # 3. CUSTOM TOOLS
    # ============================================
    tools = Tools()

    @tools.action(description="Save data to a file. Use this to save results.")
    def save_to_file(filename: str, content: str) -> str:
        """Save content to a file"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Saved to {filename}"

    @tools.action(description="Read data from a file")
    def read_from_file(filename: str) -> str:
        """Read content from a file"""
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()

    @tools.action(description="Search for information online")
    def search_web(query: str) -> str:
        """Search the web for information"""
        return f"Search query: {query}"

    @tools.action(description="Get current date and time")
    def get_datetime() -> str:
        """Get current date and time"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ============================================
    # 4. CREATE AGENT
    # ============================================
    agent = Agent(
        task="Buka GitHub dan cari repository browser-use. Cari jumlah stars, forks, dan issues. Simpan hasil dalam file github_stats.txt",
        llm=llm,
        browser=browser,
        tools=tools,
        use_vision=True,           # Enable vision for better element detection
        max_actions_per_step=5,    # Max actions per step
        max_failures=3,            # Max failures before stopping
    )

    # ============================================
    # 5. RUN AGENT
    # ============================================
    result = await agent.run()

    print("\n" + "=" * 50)
    print("TASK COMPLETED")
    print("=" * 50)
    # Safe print - remove emojis for Windows compatibility
    result_str = str(result)
    if sys.platform == 'win32':
        # Strip emojis and special Unicode chars
        result_str = ''.join(c for c in result_str if c.isascii() or c in 'éèêëàâäùûüôöîïç')
    print(f"Result: {result_str}")


# ================================================
# EXAMPLE TASKS YOU CAN TRY
# ================================================

async def task_github_stars():
    """Example 1: Get GitHub repository stats"""
    browser = Browser(headless=False)
    llm = ChatOllama(model="kimi-k2.5:cloud")

    agent = Agent(
        task="Go to github.com, search for 'browser-use', and tell me the number of stars, forks, and watchers",
        llm=llm,
        browser=browser,
        use_vision=True,
    )
    await agent.run()


async def task_web_search():
    """Example 2: Web search and extract information"""
    browser = Browser(headless=False)
    llm = ChatOllama(model="kimi-k2.5:cloud")

    agent = Agent(
        task="Search for 'latest AI news today' on Google and summarize the top 5 results",
        llm=llm,
        browser=browser,
        use_vision=True,
    )
    await agent.run()


async def task_form_fill():
    """Example 3: Fill out a form"""
    browser = Browser(headless=False)
    llm = ChatOllama(model="kimi-k2.5:cloud")

    agent = Agent(
        task="Go to https://httpbin.org/forms/post and fill out the form with sample data, then submit it",
        llm=llm,
        browser=browser,
        use_vision=True,
    )
    await agent.run()


async def task_ecommerce():
    """Example 4: E-commerce product search"""
    browser = Browser(headless=False)
    llm = ChatOllama(model="kimi-k2.5:cloud")

    agent = Agent(
        task="Search for 'mechanical keyboard' on Amazon and find the top 3 products with their prices and ratings",
        llm=llm,
        browser=browser,
        use_vision=True,
    )
    await agent.run()


async def task_data_extraction():
    """Example 5: Extract data from a webpage"""
    browser = Browser(headless=False)
    llm = ChatOllama(model="kimi-k2.5:cloud")
    tools = Tools()

    @tools.action(description="Save extracted data")
    def save_data(data: str) -> str:
        with open("extracted_data.json", "w", encoding="utf-8") as f:
            f.write(data)
        return "Data saved"

    agent = Agent(
        task="Go to hackernews.com, extract the top 10 posts with their titles, points, and comment counts. Save as JSON.",
        llm=llm,
        browser=browser,
        tools=tools,
        use_vision=True,
    )
    await agent.run()


# ================================================
# MAIN EXECUTION
# ================================================

if __name__ == "__main__":
    # Run the main example
    asyncio.run(main())

    # Uncomment to run other examples:
    # asyncio.run(task_github_stars())
    # asyncio.run(task_web_search())
    # asyncio.run(task_form_fill())
    # asyncio.run(task_ecommerce())
    # asyncio.run(task_data_extraction())
