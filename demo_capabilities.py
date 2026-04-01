"""
Demo: BrowseUse Capabilities

This shows the difference between:
1. Simple Chat (Ollama answering questions)
2. Complex Automation (Ollama controlling browser)
"""

from browser_use import Agent, ChatOllama, Browser
import asyncio
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


async def demo_chat():
    """
    DEMO 1: Simple Chat - Ollama answers WITHOUT browser
    Like ChatGPT - just text input/output
    """
    print("\n" + "=" * 60)
    print("DEMO 1: OLLAMA CHAT (No Browser Needed)")
    print("=" * 60)
    print("\nOllama answering questions directly...")
    print("-" * 60)

    llm = ChatOllama(model="qwen3.5:cloud")

    # Just ask questions - no browser
    questions = [
        "What is Python in one sentence?",
        "What is 25 * 4?",
        "Capital of Malaysia?"
    ]

    for q in questions:
        print(f"\nQ: {q}")
        # Use ollama library directly for chat
        import ollama
        response = ollama.chat(model="qwen3.5:cloud", messages=[
            {"role": "user", "content": q}
        ])
        answer = response["message"]["content"]
        print(f"A: {answer[:200]}")

    print("\n" + "-" * 60)
    print("This is CHAT mode - Ollama uses its training data")
    print("No web browsing, no real-time info")
    print("=" * 60)


async def demo_automation():
    """
    DEMO 2: Browser Automation - Ollama CONTROLS browser
    This is where BrowseUse shines!
    """
    print("\n" + "=" * 60)
    print("DEMO 2: BROWSER AUTOMATION (Ollama + Browser)")
    print("=" * 60)
    print("\nOllama will:")
    print("  1. Open browser")
    print("  2. Navigate to website")
    print("  3. Find specific data")
    print("  4. Extract and return info")
    print("-" * 60)

    browser = Browser(headless=False, disable_security=True)
    llm = ChatOllama(model="qwen3.5:cloud")

    # Complex task - Ollama must interact with web
    task = """
    Go to https://news.ycombinator.com (Hacker News)
    and extract the TOP 3 posts with:
    - Title
    - Points
    - Comment count

    Format as a clean list.
    """

    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
        use_vision=True,
    )

    print("\nRunning automation...")
    result = await agent.run()

    # Clean output
    result_str = str(result)
    if sys.platform == 'win32':
        result_str = ''.join(c for c in result_str if c.isascii() or c in 'éèêëàâäùûüôöîïç')

    print("\n" + "-" * 60)
    print("RESULTS FROM LIVE WEBSITE:")
    print("-" * 60)
    print(result_str[:1500])

    await browser.kill()

    print("\n" + "-" * 60)
    print("This is AUTOMATION mode - Ollama uses REAL web data")
    print("It can interact with any website!")
    print("=" * 60)


async def demo_comparison():
    """
    DEMO 3: Show the KEY difference
    """
    print("\n" + "=" * 60)
    print("KEY DIFFERENCE: CHAT vs AUTOMATION")
    print("=" * 60)

    print("""
┌─────────────────────────────────────────────────────────────┐
│                    OLLAMA CHAT                               │
├─────────────────────────────────────────────────────────────┤
│  Input: "What is Hacker News?"                              │
│  Output: "Hacker News is a social news website..."          │
│                                                              │
│  ✗ Cannot access current data                               │
│  ✗ Cannot browse websites                                   │
│  ✗ Uses training data only                                  │
│                                                              │
│  Good for: General knowledge, coding help, explanations     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                 BROWSEUSE + OLLAMA                           │
├─────────────────────────────────────────────────────────────┤
│  Input: "Get top 3 posts from Hacker News"                  │
│  Output:                                                     │
│    1. "New AI Model Released" - 342 pts - 128 comments      │
│    2. "Python 4.0 Announced" - 256 pts - 89 comments        │
│    3. "Startup Raises $50M" - 198 pts - 67 comments         │
│                                                              │
│  ✓ Access REAL-TIME data                                    │
│  ✓ Browse ANY website                                       │
│  ✓ Click, type, extract, fill forms                         │
│                                                              │
│  Good for: Web scraping, form filling, data extraction      │
└─────────────────────────────────────────────────────────────┘
""")


async def main():
    print("\n" + "=" * 60)
    print("       BROWSEUSE + OLLAMA DEMONSTRATION")
    print("=" * 60)

    print("\nWhich demo do you want to run?")
    print("  [1] Chat Demo - Ollama answers questions")
    print("  [2] Automation Demo - Ollama browses website")
    print("  [3] Show comparison")
    print("  [4] Run ALL demos")
    print()

    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        await demo_chat()
    elif choice == "2":
        await demo_automation()
    elif choice == "3":
        await demo_comparison()
    elif choice == "4":
        await demo_chat()
        print("\nPress Enter to continue to automation demo...")
        input()
        await demo_automation()
        await demo_comparison()
    else:
        print("Invalid choice, running automation demo...")
        await demo_automation()


if __name__ == "__main__":
    asyncio.run(main())