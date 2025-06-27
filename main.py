from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
from authenticator import authenticator
from ai import ai_service
from dotenv import load_dotenv
import os
import time

load_dotenv()
tick = time.time()

AMAZON_EMAIL=os.getenv("AMAZON_EMAIL")
AMAZON_PASSWORD=os.getenv("AMAZON_PASSWORD")


with Stealth().use_sync(sync_playwright()) as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        viewport={'width': 1920, 'height': 1080},
        java_script_enabled=True
    )  # Apply stealth mode to the page
    page = context.new_page()
    
    # authenticator(page, AMAZON_EMAIL, AMAZON_PASSWORD)
    page.goto("https://www.flipkart.com/boat-stone-350-pro-358-pro-dynamic-rgb-leds-12-hrs-playback-ipx5-tws-feature-14-w-bluetooth-speaker/p/itm509d08be10fe8?pid=ACCHFRH3HE4GCZZF&lid=LSTACCHFRH3HE4GCZZFWTTYVC&marketplace=FLIPKART&store=0pm%2F0o7&srno=b_1_2&otracker=browse&fm=organic&iid=en_FaRF8zi1i4TpKGn2xBhfwjO6mcVePXQ-XAUxSZAzDVTxWYTGN1MmCaGdScuDp8HDwKw0p5KH4HKCC-zWpKSBEw%3D%3D&ppt=browse&ppn=browse&ssid=w8xvk7sq0g0000001751056051071")
    buttons = page.eval_on_selector_all(
        'button, input[type="button"], [role="button"]',
        '''elements => elements.map(el => ({
            tag: el.tagName,
            text: el.innerText || el.value || '',
            id: el.id,
            class: el.className
        }))'''
    )

    for i, button in enumerate(buttons, 1):
        print(f"Button {i}: {button}")
    ai_service(buttons)

    browser.close()
tock= time.time()
print(f"Time taken: {tock - tick} seconds")