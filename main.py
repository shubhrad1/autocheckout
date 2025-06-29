from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
from authenticator import authenticator
from ai import ai_service
from element_extractor import element_extractor
from dotenv import load_dotenv
import os
import time

load_dotenv()
tick = time.time()

AMAZON_EMAIL=os.getenv("AMAZON_EMAIL")
AMAZON_PASSWORD=os.getenv("AMAZON_PASSWORD")


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
    
    # authenticator(page, AMAZON_EMAIL, AMAZON_PASSWORD)
    # page.goto("https://www.flipkart.com/boat-stone-350-pro-358-pro-dynamic-rgb-leds-12-hrs-playback-ipx5-tws-feature-14-w-bluetooth-speaker/p/itm509d08be10fe8?pid=ACCHFRH3HE4GCZZF&lid=LSTACCHFRH3HE4GCZZFWTTYVC&marketplace=FLIPKART&store=0pm%2F0o7&srno=b_1_2&otracker=browse&fm=organic&iid=en_FaRF8zi1i4TpKGn2xBhfwjO6mcVePXQ-XAUxSZAzDVTxWYTGN1MmCaGdScuDp8HDwKw0p5KH4HKCC-zWpKSBEw%3D%3D&ppt=browse&ppn=browse&ssid=w8xvk7sq0g0000001751056051071")
    page.goto("https://www.amazon.in/Minimalist-Sunscreen-Multi-Vitamins-Cream/dp/B09FPS9D5T?pd_rd_w=dZrdy&content-id=amzn1.sym.4c241eba-0ce0-4f45-a17d-f017b3203e3d&pf_rd_p=4c241eba-0ce0-4f45-a17d-f017b3203e3d&pf_rd_r=TMJBK8MS6XEEWBXYWACA&pd_rd_wg=pqsaf&pd_rd_r=548a6094-8538-44c6-96d5-7cd4449d5433&pd_rd_i=B09FPS9D5T&ref_=pd_bap_d_grid_rp_0_1_ec_nped_pr_pd_hp_d_atf_rp_2_t&th=1")
    buttons = element_extractor(
        page,
        # 'button, input[type="button"], [role="button"], tag[name="button"]'
        'button, input[type="submit"]'
    )
    buttonset=set()
    for button in buttons:
        if (button['text'] and button['text'].strip()) or (button['id'] and button['id'].strip()):
            buttonset.add((button['id'], button['text'].strip(), button['class']))
    
    with open('amazon_output.txt', 'w') as f:
        for i, button in enumerate(buttonset, 1):
            print(f"Button {i}: {button}", file=f)
        
    
    buyelement=ai_service(buttons,"buynow")

    browser.close()
tock= time.time()
print(f"Time taken: {tock - tick} seconds")