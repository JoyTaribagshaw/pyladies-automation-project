#!/usr/bin/env python3
"""
Simple Web Automation Demo

A simplified version that focuses on the core functionality for presentations.
"""

import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import shutil

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def simple_google_search(query: str, headless: bool = True, timeout: int = 10):
    """Simple Google search that just works."""
    
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-notifications')
    
    if headless:
        options.add_argument('--headless=new')
    
    # Find Chrome binary
    chrome_paths = ['/usr/bin/chromium', '/usr/bin/google-chrome', '/usr/bin/chromium-browser']
    for path in chrome_paths:
        if shutil.which(path):
            options.binary_location = path
            logger.info(f"Using Chrome at: {path}")
            break
    
    driver = None
    try:
        # Try system chromedriver first (skip webdriver-manager to avoid version conflicts)
        chromedriver_path = shutil.which('chromedriver')
        if chromedriver_path:
            logger.info(f"Using system chromedriver: {chromedriver_path}")
            service = ChromeService(chromedriver_path)
        else:
            # Fallback to automatic detection
            service = ChromeService()
        
        driver = webdriver.Chrome(service=service, options=options)
        logger.info("✅ Browser started successfully")
        
        # Go directly to Google search with the query (bypass cookie banners)
        import urllib.parse
        search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
        logger.info(f"Navigating to: {search_url}")
        driver.get(search_url)
        
        # Wait a moment for page to load
        time.sleep(3)
        
        # Take screenshot
        screenshot_name = f"google_search_{query.replace(' ', '_')}.png"
        driver.save_screenshot(screenshot_name)
        logger.info(f"✅ Screenshot saved: {screenshot_name}")
        
        # Try to get first result
        try:
            first_result = driver.find_element(By.CSS_SELECTOR, "h3")
            if first_result and first_result.text:
                print(f"🎯 First result: {first_result.text}")
        except:
            logger.info("Could not extract first result (but search worked)")
        
        print(f"✅ Google search completed successfully!")
        print(f"📸 Screenshot saved as: {screenshot_name}")
        return True
        
    except Exception as e:
        logger.error(f"❌ Search failed: {e}")
        return False
    finally:
        if driver:
            driver.quit()
            logger.info("Browser closed")

if __name__ == "__main__":
    print("🔍 Simple Google Search Demo")
    print("=" * 40)
    
    query = input("Enter search query (or press Enter for 'PyLadies automation'): ").strip()
    if not query:
        query = "PyLadies automation"
    
    headless_choice = input("Run in headless mode? (y/n, default=y): ").strip().lower()
    headless = headless_choice != 'n'
    
    print(f"\n🚀 Searching Google for: '{query}'")
    print("🌐 Opening browser..." if not headless else "🌐 Opening headless browser...")
    
    success = simple_google_search(query, headless=headless)
    
    if success:
        print("\n🎉 Demo completed successfully!")
        print("💡 This shows how Python can automate web interactions")
        print("📂 Check the current directory for the screenshot")
    else:
        print("\n❌ Demo failed - but that's okay!")
        print("💡 In a real presentation, you'd use Demo Mode or pre-recorded screenshots")