from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
from authenticator import authenticator
from buynow import buynow
from dotenv import load_dotenv
import os
import time

load_dotenv()


EMAIL=os.getenv("EMAIL")
PASSWORD=os.getenv("PASSWORD")

if not EMAIL or not PASSWORD:
    print("Please set the EMAIL and PASSWORD environment variables.")
    os._exit(1)


with Stealth().use_sync(sync_playwright()) as p:
    print("Starting Playwright with stealth mode...")
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        viewport={'width': 1920, 'height': 1080},
        java_script_enabled=True
    )  # Apply stealth mode to the page

    page = context.new_page()

    url=input("Enter the Product URL: ")
    t1 = time.time()
    try:
        buynow(page, url)
    except Exception as e:
        print(f"Error during 'Buy Now' process: {e}")
        browser.close()
        os._exit(1)

    try:
        checkout=authenticator(page, EMAIL, PASSWORD)
    except Exception as e:
        print(f"Error during authentication: {e}")
        browser.close()
        os._exit(1)

    browser.close()
t2= time.time()
print(f"Checkout URL: {checkout}")
print(f"Time taken: {t2 - t1} seconds")