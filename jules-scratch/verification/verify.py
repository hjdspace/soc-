import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        try:
            # Go to the React app
            await page.goto("http://localhost:8001")

            # Wait for the main heading
            await expect(page.get_by_role("heading", name="SOC Project Management")).to_be_visible(timeout=10000)

            # Wait for the "Projects" subheading
            await expect(page.get_by_role("heading", name="Projects")).to_be_visible()

            # Wait for the specific project created by the management command
            await expect(page.get_by_text("Test Project")).to_be_visible()

            # Take a screenshot
            await page.screenshot(path="jules-scratch/verification/screenshot.png")

            print("Screenshot taken successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
