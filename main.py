from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
from authenticator import authenticator
from buynow import buynow
from dotenv import load_dotenv
import os
import time

load_dotenv()
tick = time.time()

AMAZON_EMAIL=os.getenv("AMAZON_EMAIL")
AMAZON_PASSWORD=os.getenv("AMAZON_PASSWORD")


with Stealth().use_sync(sync_playwright()) as p:
    print("Starting Playwright with stealth mode...")
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        viewport={'width': 1920, 'height': 1080},
        java_script_enabled=True
    )  # Apply stealth mode to the page
    page = context.new_page()
    
    #url="https://www.amazon.in/Minimalist-Sunscreen-Multi-Vitamins-Cream/dp/B09FPS9D5T?pd_rd_w=dZrdy&content-id=amzn1.sym.4c241eba-0ce0-4f45-a17d-f017b3203e3d&pf_rd_p=4c241eba-0ce0-4f45-a17d-f017b3203e3d&pf_rd_r=TMJBK8MS6XEEWBXYWACA&pd_rd_wg=pqsaf&pd_rd_r=548a6094-8538-44c6-96d5-7cd4449d5433&pd_rd_i=B09FPS9D5T&ref_=pd_bap_d_grid_rp_0_1_ec_nped_pr_pd_hp_d_atf_rp_2_t&th="
    #url="https://www.amazon.in/ZOBRIX-Compatible-Protection-Frameless-Magsafe/dp/B0DRSPK79Y/?_encoding=UTF8&pd_rd_w=koPdp&content-id=amzn1.sym.703f61c9-1331-4a81-9756-2e307bdc550f&pf_rd_p=703f61c9-1331-4a81-9756-2e307bdc550f&pf_rd_r=6M29C7JF168MEVMCH1JZ&pd_rd_wg=nFQQG&pd_rd_r=7b7f1cfd-5494-48da-a7cf-9f875023e04b&ref_=pd_hp_d_btf_LPDEALS&th=1"
    
    #url="https://www.flipkart.com/pw-eajee-handwritten-notes-physical-chemistry-faisal-razaq-jee-exams/p/itmb49cb5893455f?pid=9789368971337&marketplace=FLIPKART"
    #url="https://www.amazon.in/INEFABLE-SmartWatch-Colorfit-Firebolt-Invincible/dp/B0CK2N8T5Y/ref=pd_ci_mcx_mh_mcx_views_0_image?pd_rd_w=hLRqr&content-id=amzn1.sym.fa0aca50-60f7-47ca-a90e-c40e2f4b46a9%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=fa0aca50-60f7-47ca-a90e-c40e2f4b46a9&pf_rd_r=ACJZYQ14GE5D8PRP1HTB&pd_rd_wg=Lhj1H&pd_rd_r=8ef81201-766e-441a-a31e-1c984fef43af&pd_rd_i=B0CK2N8T5Y"
    url=input("Enter the Amazon product URL: ")
    err=buynow(page, url)
    if err == -1:
        print("Error in buynow function")
        
    else:
        print("Buy Now button clicked successfully")
        
        checkout=authenticator(page, AMAZON_EMAIL, AMAZON_PASSWORD)
    

    browser.close()
tock= time.time()
print(f"Checkout URL: {checkout}")
print(f"Time taken: {tock - tick} seconds")