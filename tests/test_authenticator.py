from ..authenticator import authenticator
from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
import pytest
import os
@pytest.fixture
def mock_page():
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
        yield page
        browser.close()

def test_authenticator(mock_page):
    """
    Test the authenticator function with a mock page.
    """
    email = os.getenv("AMAZON_EMAIL")
    password = os.getenv("AMAZON_PASSWORD")
    
    # Navigate to the Amazon login page
    mock_page.goto("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fcheckout%2Fentry%2Fbuynow%3FclientName%3DOffersX_OfferDisplay_DetailPage%26ASIN%3DB0CY5HVDS2%26storeID%3D%26qid%3D%26anti-csrftoken-a2z%3DhJu5dQl%252B3q1IE334YQu1fQIqj0XlDOn2HAgwOK945omvAAAAAGhidyBjODA1YzE5MS1lODRiLTQ2NTMtODkxZC0wOWM5MTcwNjU0ZmI%253D%26anti-csrftoken-a2z%3DhHdSYivsDlbwkBmW9%252BSoa7F52azuwf6p5BSSoK8KDfufAAAAAGhidyBjODA1YzE5MS1lODRiLTQ2NTMtODkxZC0wOWM5MTcwNjU0ZmI%253D%26sellingCustomerID%3D%26sourceCustomerOrgListID%3D%26dropdown-selection-ubb%3Dadd-new%26viewID%3Dglance%26ctaDeviceType%3Ddesktop%26isAddon%3D0%26ref_%3Ddp_start-bbf_1_glance_chw%26dropdown-selection%3Dadd-new%26nodeID%3D%26sr%3D%26items%255B0.base%255D%255BcustomerVisiblePrice%255D%255BdisplayString%255D%3D%25E2%2582%25B954%252C990.00%26tagActionCode%3D%26usePrimeHandler%3D0%26ctaPageType%3Ddetail%26smokeTestEnabled%3Dfalse%26rsid%3D258-0406218-1114631%26isBuyNow%3D1%26items%255B0.base%255D%255BcustomerVisiblePrice%255D%255Bamount%255D%3D54990.0%26pageLoadTimestampUTC%3D2025-06-30T11%253A38%253A07.896476035Z%26isEligibilityLogicDisabled%3D1%26items%255B0.base%255D%255Basin%255D%3DB0CY5HVDS2%26referrer%3Ddetail%26isMerchantExclusive%3D0%26merchantID%3DA2GTG1HPYW8M2P%26items%255B0.base%255D%255BcustomerVisiblePrice%255D%255BcurrencyCode%255D%3DINR%26items%255B0.base%255D%255BofferListingId%255D%3D9kevU3yr%25252BI2dL8KC3Y1L4bZUz6skxmLEhnIPvGEy3cRSDqdOLmn6a9%25252BRrx2zb5SChk9pF7xqpWqvvrHu%25252FXTJWHH340xC9AVN1XBIWZrUB6pk3L0kPk84PFh7WEkKkDFZyedJ5jLmmNBLSURf4HwYD9s1Cxw%25252BjwUg%26sourceCustomerOrgListItemID%3D%26submit.buy-now%3DSubmit%26pipelineType%3DChewbacca%26rebateId%3D%26offerListingID%3D9kevU3yr%25252BI2dL8KC3Y1L4bZUz6skxmLEhnIPvGEy3cRSDqdOLmn6a9%25252BRrx2zb5SChk9pF7xqpWqvvrHu%25252FXTJWHH340xC9AVN1XBIWZrUB6pk3L0kPk84PFh7WEkKkDFZyedJ5jLmmNBLSURf4HwYD9s1Cxw%25252BjwUg%26session-id%3D258-0406218-1114631%26wlPopCommand%3D%26isUnrec%3D1&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amazon_checkout_in&openid.mode=checkid_setup&language=en_IN&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    
    # Call the authenticator function
    result_url = authenticator(mock_page, email, password)

    assert "https://www.amazon.in/checkout" in result_url, "Did not navigate to the checkout page after authentication"


