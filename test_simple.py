# Simple Browser-Use Test with Ollama
# Test script untuk verify installation

from browser_use import Agent, ChatOllama, Browser
import asyncio
import sys

# Set console encoding untuk Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


async def simple_task():
    """Simple test: Get GitHub stars"""
    print("=" * 60)
    print("🚀 BROWSER-USE TEST WITH OLLAMA (qwen3.5:cloud)")
    print("=" * 60)
    
    browser = Browser(
        headless=False,  # Browser akan nampak
    )
    
    llm = ChatOllama(model="qwen3.5:cloud")
    
    agent = Agent(
        task="Go to github.com/browser-use/browser-use and tell me the number of stars, forks, and issues",
        llm=llm,
        browser=browser,
        use_vision=True,
    )
    
    print("\n🤖 Agent starting...\n")
    
    result = await agent.run()
    
    print("\n" + "=" * 60)
    print("✅ TASK COMPLETED")
    print("=" * 60)
    print(f"\n{result}\n")


async def search_task():
    """Search task: Find information"""
    print("=" * 60)
    print("🔍 SEARCH TEST")
    print("=" * 60)
    
    browser = Browser(headless=False)
    llm = ChatOllama(model="qwen3.5:cloud")
    
    agent = Agent(
        task="Search for 'AI news today' on Google and summarize the top 3 results",
        llm=llm,
        browser=browser,
        use_vision=True,
    )
    
    print("\n🤖 Agent starting...\n")
    result = await agent.run()
    
    print("\n" + "=" * 60)
    print("✅ TASK COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    print("\nSelect test to run:")
    print("1. GitHub Stars Test (simple)")
    print("2. Google Search Test")
    print("3. Exit")
    
    choice = input("\nEnter choice (1/2/3): ").strip()
    
    if choice == "1":
        asyncio.run(simple_task())
    elif choice == "2":
        asyncio.run(search_task())
    elif choice == "3":
        print("👋 Goodbye!")
    else:
        print("❌ Invalid choice")
