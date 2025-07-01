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

    url=input("Enter the Amazon product URL: ")
    t1 = time.time()
    err=buynow(page, url)
    
    if err == -1:
        print("Error in buynow function")
        
    else:
        print("Buy Now button clicked successfully")
        
        checkout=authenticator(page, EMAIL, PASSWORD)
    

    browser.close()
t2= time.time()
print(f"Checkout URL: {checkout}")
print(f"Time taken: {t2 - t1} seconds")