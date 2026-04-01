# Test script untuk verify browser NAMPAK
# Jalankan script ini untuk test

from browser_use import Agent, ChatOllama, Browser
import asyncio
import sys

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


async def test_browser_visible():
    """Test ini akan BUKA browser yang NAMPAK"""
    
    print("=" * 60)
    print("🧪 BROWSER VISIBILITY TEST")
    print("=" * 60)
    print()
    print("📌 Script ini akan:")
    print("   1. Buka browser Chrome (SEPAATNYA NAMPAK)")
    print("   2. Navigate ke Google.com")
    print("   3. Tunggu 5 saat")
    print("   4. Close browser")
    print()
    print("⚠️  JIKA BROWSER TAK NAMPAK:")
    print("   - Check taskbar untuk Chrome window")
    print("   - Check ada multiple Chrome windows")
    print("   - Close semua Chrome dan try lagi")
    print()
    print("🔓 Opening browser in 2 seconds...")
    await asyncio.sleep(2)
    print()
    
    # Force browser untuk NAMPAK
    browser = Browser(
        headless=False,           # FALSE = browser NAMPAK
        disable_security=True,    # Disable security warnings
    )
    
    print("✅ Browser instance created...")
    print()
    
    llm = ChatOllama(model="qwen3.5:cloud")
    
    agent = Agent(
        task="Go to google.com and wait 5 seconds, then tell me what you see",
        llm=llm,
        browser=browser,
        use_vision=True,
    )
    
    print("🚀 Starting agent...")
    print()
    
    try:
        result = await agent.run()
        
        print()
        print("=" * 60)
        print("✅ TEST COMPLETED")
        print("=" * 60)
        print()
        print(f"Result: {result}\n")
        
    except Exception as e:
        print()
        print("=" * 60)
        print("❌ ERROR")
        print("=" * 60)
        print()
        print(f"Error: {e}\n")
    
    finally:
        # Close browser
        try:
            await browser.close()
            print("🔒 Browser closed")
        except:
            pass


async def test_simple_navigation():
    """Simple test tanpa AI - just test browser buka"""
    
    print("=" * 60)
    print("🧪 SIMPLE BROWSER TEST (No AI)")
    print("=" * 60)
    print()
    
    browser = Browser(
        headless=False,
        disable_security=True,
    )
    
    print("✅ Browser created - check if window is visible!")
    print()
    print("⏳ Tunggu 10 saat...")
    print()
    
    await asyncio.sleep(10)
    
    # Navigate manually
    session = await browser.new_session()
    await session.navigate_to_url("https://www.google.com")
    
    print("🌐 Navigated to google.com")
    print()
    print("⏳ Tunggu 5 saat lagi...")
    
    await asyncio.sleep(5)
    
    await browser.close()
    print("🔒 Browser closed")


if __name__ == "__main__":
    # Auto run test 1 (Full AI Test)
    print()
    print("🚀 Running Full AI Test (navigate + AI reasoning)")
    print()
    asyncio.run(test_browser_visible())
