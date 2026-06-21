from playwright.async_api import async_playwright


async def take_screenshot(url, width, height):

    async with async_playwright() as playwright: #playwright opstarten

        chromium = playwright.chromium #browser dat we gebruiken, headless
        browser = await chromium.launch() # browser launch
        page = await browser.new_page() #make a new page
        await page.set_viewport_size({"width": width, "height": height})
        await page.goto(f"{url}") #navigate to the page

        screenshot_bytes = await page.screenshot()
        
        
        await browser.close()
        return screenshot_bytes

