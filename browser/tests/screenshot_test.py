import asyncio
from browser.browser import Browser, BrowserConfig  # Adjust the import if necessary
from dom.service import DomService  # Adjust the import to your project structure

async def main():
    # Create a Browser instance with headless mode disabled so the window is visible.
    browser_service = Browser(config=BrowserConfig(headless=False))
    
    # Initialize and spawn the Playwright browser using our custom class.
    playwright_browser = await browser_service.get_playwright_browser()
    
    # Open a new page.
    page = await playwright_browser.new_page()
    
    # Navigate to a page (for example, google.com) and wait for it to load.
    await page.goto("https://news.ycombinator.com/")
    await page.wait_for_load_state("networkidle")
    
    # Initialize DomService with the current page.
    dom_service = DomService(page)
    
    # Get clickable elements (or the full DOM tree) with bounding boxes included.
    dom_state = await dom_service.get_clickable_elements(highlight_elements=True)
    print(dom_state)
    
    # Pause to allow inspection of the browser window (adjust delay as needed).
    await asyncio.sleep(100)
    
    # Close the browser instance.
    await browser_service.close()

if __name__ == "__main__":
    asyncio.run(main())




