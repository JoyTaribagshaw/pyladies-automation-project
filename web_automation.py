"""
Web Automation Module

This module provides functions to automate web interactions using Selenium WebDriver,
including form filling, button clicking, and web scraping.
"""

import time
import logging
from pathlib import Path
from typing import Optional, Dict, List, Union, Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    WebDriverException
)
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('web_automation.log')
    ]
)
logger = logging.getLogger(__name__)

class WebAutomation:
    """A class to handle web automation tasks using Selenium WebDriver."""
    
    def __init__(
        self,
        headless: bool = False,
        download_dir: Optional[str] = None,
        implicit_wait: int = 10,
        chrome_path: Optional[str] = None
    ):
        """
        Initialize the WebAutomation with Chrome WebDriver.
        
        Args:
            headless: Run browser in headless mode (no GUI)
            download_dir: Directory to save downloaded files
            implicit_wait: Default wait time for finding elements (seconds)
            chrome_path: Path to Chrome/Chromium executable (optional)
        """
        self.driver = None
        self.headless = headless
        self.download_dir = download_dir
        self.implicit_wait = implicit_wait
        self.chrome_path = chrome_path
        
    def start_browser(self) -> None:
        """Start the Chrome browser with configured options."""
        try:
            options = ChromeOptions()
            
            # Add common options
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-notifications')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-extensions')
            options.add_argument('--start-maximized')
            
            # Set download directory if specified
            if self.download_dir:
                prefs = {
                    'download.default_directory': str(Path(self.download_dir).absolute()),
                    'download.prompt_for_download': False,
                    'download.directory_upgrade': True,
                    'safebrowsing.enabled': True
                }
                options.add_experimental_option('prefs', prefs)
            
            # Set headless mode if specified
            if self.headless:
                options.add_argument('--headless=new')
            
            # Set Chrome binary location if specified, or try to find it
            if self.chrome_path:
                options.binary_location = self.chrome_path
            else:
                # Try to find Chrome/Chromium automatically
                import shutil
                possible_paths = [
                    '/usr/bin/chromium',
                    '/usr/bin/chromium-browser', 
                    '/usr/bin/google-chrome',
                    '/usr/bin/google-chrome-stable',
                    '/snap/bin/chromium',
                ]
                for path in possible_paths:
                    if shutil.which(path):
                        options.binary_location = path
                        logger.info(f"Found Chrome/Chromium at: {path}")
                        break
            
            # Try to initialize the WebDriver with better error handling
            try:
                # First try: Use webdriver-manager
                self.driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install()),
                    options=options
                )
            except Exception as e1:
                logger.warning(f"webdriver-manager failed: {e1}")
                try:
                    # Second try: Use system chromedriver
                    system_chromedriver = shutil.which('chromedriver')
                    if system_chromedriver:
                        logger.info(f"Trying system chromedriver: {system_chromedriver}")
                        self.driver = webdriver.Chrome(
                            service=ChromeService(system_chromedriver),
                            options=options
                        )
                    else:
                        # Third try: Let Selenium find chromedriver automatically
                        logger.info("Trying automatic chromedriver detection")
                        self.driver = webdriver.Chrome(options=options)
                except Exception as e2:
                    logger.error(f"All WebDriver initialization attempts failed")
                    logger.error(f"webdriver-manager error: {e1}")
                    logger.error(f"System chromedriver error: {e2}")
                    
                    # Provide helpful error message
                    error_msg = (
                        "Failed to start Chrome WebDriver. This could be due to:\n"
                        "1. Chrome/Chromium version mismatch with ChromeDriver\n"
                        "2. Missing Chrome/Chromium browser\n"
                        "3. Outdated ChromeDriver\n\n"
                        "Try these solutions:\n"
                        "- Install/update Chrome: sudo pacman -S chromium\n" 
                        "- Update ChromeDriver: pip install --upgrade selenium webdriver-manager\n"
                        "- Check browser path in options.binary_location\n"
                    )
                    raise Exception(error_msg)
            
            # Set implicit wait
            self.driver.implicitly_wait(self.implicit_wait)
            logger.info("Browser started successfully")
            
        except Exception as e:
            logger.error(f"Failed to start browser: {e}")
            raise
    
    def close_browser(self) -> None:
        """Close the browser and quit the WebDriver."""
        if self.driver:
            try:
                self.driver.quit()
                logger.info("Browser closed successfully")
            except Exception as e:
                logger.error(f"Error while closing browser: {e}")
            finally:
                self.driver = None
    
    def __enter__(self):
        """Context manager entry."""
        self.start_browser()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close_browser()
    
    def navigate_to(self, url: str) -> bool:
        """Navigate to the specified URL."""
        if not self.driver:
            logger.error("Browser not started. Call start_browser() first.")
            return False
        
        try:
            self.driver.get(url)
            logger.info(f"Navigated to: {url}")
            return True
        except WebDriverException as e:
            logger.error(f"Failed to navigate to {url}: {e}")
            return False
    
    def find_element(self, by: str, value: str, timeout: int = None):
        """
        Find a single web element.
        
        Args:
            by: Locator strategy (id, name, xpath, css_selector, etc.)
            value: Locator value
            timeout: Maximum time to wait (seconds)
            
        Returns:
            WebElement if found, None otherwise
        """
        if not self.driver:
            logger.error("Browser not started. Call start_browser() first.")
            return None
        
        try:
            if timeout:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((by, value))
                )
            else:
                element = self.driver.find_element(by, value)
            return element
        except (TimeoutException, NoSuchElementException) as e:
            logger.warning(f"Element not found: {by}={value}")
            return None
    
    def click_element(self, by: str, value: str, timeout: int = None) -> bool:
        """Click on an element."""
        element = self.find_element(by, value, timeout)
        if element:
            try:
                element.click()
                logger.info(f"Clicked element: {by}={value}")
                return True
            except Exception as e:
                logger.error(f"Failed to click element: {e}")
        return False
    
    def type_text(self, by: str, value: str, text: str, clear: bool = True) -> bool:
        """Type text into an input field."""
        element = self.find_element(by, value)
        if element:
            try:
                if clear:
                    element.clear()
                element.send_keys(text)
                logger.info(f"Typed text into {by}={value}")
                return True
            except Exception as e:
                logger.error(f"Failed to type text: {e}")
        return False
    
    def select_dropdown(self, by: str, value: str, option: str, by_visible_text: bool = True) -> bool:
        """Select an option from a dropdown."""
        element = self.find_element(by, value)
        if element:
            try:
                select = Select(element)
                if by_visible_text:
                    select.select_by_visible_text(option)
                else:
                    select.select_by_value(option)
                logger.info(f"Selected '{option}' from dropdown {by}={value}")
                return True
            except Exception as e:
                logger.error(f"Failed to select dropdown option: {e}")
        return False
    
    def take_screenshot(self, filename: str = None) -> Optional[str]:
        """Take a screenshot and save it to a file."""
        if not self.driver:
            logger.error("Browser not started. Call start_browser() first.")
            return None
        
        try:
            if not filename:
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                filename = f"screenshot_{timestamp}.png"
            
            # Ensure the filename has .png extension
            if not filename.lower().endswith('.png'):
                filename += '.png'
            
            self.driver.save_screenshot(filename)
            logger.info(f"Screenshot saved as {filename}")
            return filename
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
            return None
    
    def wait_for_element(self, by: str, value: str, timeout: int = 10) -> bool:
        """Wait for an element to be present on the page."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            logger.warning(f"Element {by}={value} not found within {timeout} seconds")
            return False
    
    def get_page_source(self) -> Optional[str]:
        """Get the page source HTML."""
        if self.driver:
            return self.driver.page_source
        return None
    
    def execute_js(self, script: str, *args) -> Any:
        """Execute JavaScript code."""
        if self.driver:
            return self.driver.execute_script(script, *args)
        return None

# Example functions for common tasks
def search_google(query: str, headless: bool = True) -> None:
    """Search Google for a query and take a screenshot of the results."""
    with WebAutomation(headless=headless) as auto:
        # Navigate to Google
        auto.navigate_to("https://www.google.com")
        
        # Accept cookies if the banner appears (try multiple possible selectors)
        cookie_selectors = [
            "#L2AGLb",  # Google's main accept button ID
            "[aria-label*='Accept']",  # Buttons with Accept in aria-label
            "[aria-label*='Accept all']",  # Accept all variations
            "button[id*='accept']",  # Buttons with accept in ID
            "button[class*='accept']",  # Buttons with accept in class
        ]
        for selector in cookie_selectors:
            if auto.click_element(By.CSS_SELECTOR, selector):
                logger.info(f"Clicked cookie acceptance button: {selector}")
                break
        else:
            logger.info("No cookie banner found or clicked")
        
        # Type the search query
        search_box = auto.find_element(By.NAME, "q")
        if search_box:
            logger.info(f"Found search box, typing query: {query}")
            auto.type_text(By.NAME, "q", query)
            
            # Try multiple ways to trigger search
            search_triggered = False
            try:
                # Method 1: Press Enter key
                logger.info("Trying Enter key method...")
                search_box.send_keys(Keys.RETURN)
                logger.info("Triggered search with Enter key")
                search_triggered = True
            except Exception as e1:
                logger.warning(f"Enter key method failed: {e1}")
                try:
                    # Method 2: Click the search button (original approach)
                    logger.info("Trying search button click...")
                    if auto.click_element(By.NAME, "btnK"):
                        logger.info("Clicked search button")
                        search_triggered = True
                    else:
                        # Try alternative search button
                        if auto.click_element(By.CSS_SELECTOR, "[aria-label='Google Search']"):
                            logger.info("Clicked alternative search button")
                            search_triggered = True
                except Exception as e2:
                    logger.warning(f"Search button method failed: {e2}")
                    try:
                        # Method 3: Use Google's search URL directly
                        logger.info("Trying direct URL method...")
                        import urllib.parse
                        search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
                        auto.navigate_to(search_url)
                        logger.info("Used direct search URL")
                        search_triggered = True
                    except Exception as e3:
                        logger.error(f"All search methods failed: {e1}, {e2}, {e3}")
                        return
            
            if not search_triggered:
                logger.error("No search method succeeded")
                return
        else:
            logger.error("Could not find Google search box")
            return
        
        # Wait for results and take a screenshot
        import time
        time.sleep(3)  # Give page time to load
        
        # Check if we're on a results page
        if "search?q=" in auto.driver.current_url or auto.find_element(By.ID, "search"):
            auto.take_screenshot(f"google_search_{query.replace(' ', '_')}.png")
            
            # Try to get the first result title
            result_selectors = ["h3", "[data-attrid] h3", ".g h3", ".tF2Cxc h3"]
            first_result = None
            for selector in result_selectors:
                first_result = auto.find_element(By.CSS_SELECTOR, selector)
                if first_result:
                    break
            
            if first_result:
                print(f"First result: {first_result.text}")
            else:
                print("Search completed - screenshot saved!")
        else:
            logger.warning("Search may not have completed successfully")
            auto.take_screenshot(f"google_search_error_{query.replace(' ', '_')}.png")

def fill_contact_form(url: str, form_data: Dict[str, str]) -> bool:
    """Fill out and submit a contact form."""
    with WebAutomation(headless=False) as auto:
        try:
            auto.navigate_to(url)
            
            # Fill in form fields
            for field, value in form_data.items():
                if field == 'message':
                    auto.type_text(By.NAME, field, value)
                else:
                    auto.type_text(By.NAME, field, value)
            
            # Submit the form
            auto.click_element(By.CSS_SELECTOR, "button[type='submit']")
            
            # Wait for success message or redirect
            time.sleep(2)  # Adjust based on the form's behavior
            
            # Take a screenshot of the result
            auto.take_screenshot("form_submission_result.png")
            return True
            
        except Exception as e:
            logger.error(f"Error submitting form: {e}")
            return False

if __name__ == "__main__":
    # Example usage
    print("=== Web Automation Examples ===")
    print("1. Search Google")
    print("2. Fill Contact Form")
    print("3. Demo Mode (no browser needed)")
    
    choice = input("Enter your choice (1-3): ").strip()
    
    if choice == "1":
        query = input("Enter search query: ").strip()
        try:
            search_google(query, headless=False)
            print("Search completed. Check the screenshot in the current directory.")
        except Exception as e:
            print(f"❌ Web automation failed: {e}")
            print("💡 Try Demo Mode (option 3) to see what this script would do")
    
    elif choice == "2":
        form_url = input("Enter form URL: ").strip()
        form_data = {
            'name': input("Name: "),
            'email': input("Email: "),
            'subject': input("Subject: "),
            'message': input("Message: ")
        }
        try:
            if fill_contact_form(form_url, form_data):
                print("Form submitted successfully!")
            else:
                print("Failed to submit form. Check the logs for details.")
        except Exception as e:
            print(f"❌ Web automation failed: {e}")
            print("💡 Try Demo Mode (option 3) to see what this script would do")
    
    elif choice == "3":
        print("\n🎭 DEMO MODE - What this script can do:")
        print("=" * 50)
        
        query = "PyLadies automation"
        print(f"\n🔍 Google Search Demo:")
        print(f"   Query: '{query}'")
        print("   ✅ Would open browser (headless or visible)")
        print("   ✅ Would navigate to https://www.google.com")
        print("   ✅ Would accept cookie banner if present")
        print(f"   ✅ Would type '{query}' in search box")
        print("   ✅ Would click search button")
        print("   ✅ Would wait for results page")
        print("   ✅ Would take screenshot: google_search_PyLadies_automation.png")
        print("   ✅ Would extract first result title")
        
        print(f"\n📝 Form Filling Demo:")
        print("   ✅ Would navigate to any form URL")
        print("   ✅ Would locate input fields by name/id")
        print("   ✅ Would fill in:")
        print("       - Name field")
        print("       - Email field")
        print("       - Subject field")
        print("       - Message field")
        print("   ✅ Would click submit button")
        print("   ✅ Would take screenshot of result")
        
        print(f"\n🚀 Real-world applications:")
        print("   • Automated testing of web applications")
        print("   • Data collection from websites")
        print("   • Form submissions (surveys, registrations)")
        print("   • Price monitoring and alerts")
        print("   • Social media posting")
        print("   • Web scraping for research")
        
        print(f"\n🛠️ To fix browser issues:")
        print("   1. Update Chromium: sudo pacman -S chromium")
        print("   2. Update packages: pip install --upgrade selenium webdriver-manager")
        print("   3. Check the logs: tail web_automation.log")
        
        print(f"\n✨ Once working, you can automate any repetitive web task!")
    
    else:
        print("Invalid choice. Please try again.")
