from ..element_extractor import form_extractor
import pytest
from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth

@pytest.fixture
def mock_page():
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
        page.goto("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fcheckout%2Fentry%2Fbuynow%3FclientName%3DOffersX_OfferDisplay_DetailPage%26ASIN%3DB0825623MN%26storeID%3D%26qid%3D%26anti-csrftoken-a2z%3DhC0VGRHS1W38H0HkQmxYV73FNedc6tPJ67OBZRc0tqtBAAAAAGhijExjODA1YzE5MS1lODRiLTQ2NTMtODkxZC0wOWM5MTcwNjU0ZmI%253D%26anti-csrftoken-a2z%3DhEqI%252Ba3ZrNGKAAUx5pl0te2aqOY1iT0SQ9RDZfJCwGTrAAAAAGhijExjODA1YzE5MS1lODRiLTQ2NTMtODkxZC0wOWM5MTcwNjU0ZmI%253D%26sellingCustomerID%3D%26sourceCustomerOrgListID%3D%26dropdown-selection-ubb%3Dadd-new%26viewID%3Dglance%26ctaDeviceType%3Ddesktop%26isAddon%3D0%26ref_%3Ddp_start-bbf_1_glance_chw%26dropdown-selection%3Dadd-new%26nodeID%3D%26items%255B0.base%255D%255Bquantity%255D%3D1%26sr%3D%26items%255B0.base%255D%255BcustomerVisiblePrice%255D%255BdisplayString%255D%3D%25E2%2582%25B9297.00%26tagActionCode%3D%26usePrimeHandler%3D0%26ctaPageType%3Ddetail%26quantity%3D1%26smokeTestEnabled%3Dfalse%26rsid%3D260-1560676-0648103%26isBuyNow%3D1%26items%255B0.base%255D%255BcustomerVisiblePrice%255D%255Bamount%255D%3D297.0%26pageLoadTimestampUTC%3D2025-06-30T13%253A08%253A28.683131415Z%26isEligibilityLogicDisabled%3D1%26items%255B0.base%255D%255Basin%255D%3DB0825623MN%26referrer%3Ddetail%26isMerchantExclusive%3D0%26merchantID%3DA2N66YEQWVPA4I%26items%255B0.base%255D%255BcustomerVisiblePrice%255D%255BcurrencyCode%255D%3DINR%26items%255B0.base%255D%255BofferListingId%255D%3Da1XdYOhkVsd37teZszTyoVnjrRCTcIigrqkbTF2VoLEHNhj9n3lJzIN2KrFOW8cwccVMmaDRKbvUtvDvs9a6saMG0JsG8YECc6%25252BSHZ0xmIbJ8N0LeZXRS8qbARlwCBgYD4FVkbawt1JGLswQs604QzDaNgw2XOaGyYL3Dhep5mgbfjFxjlpVjbJoUPmRBxsh%26sourceCustomerOrgListItemID%3D%26submit.buy-now%3DSubmit%26pipelineType%3DChewbacca%26rebateId%3D%26offerListingID%3Da1XdYOhkVsd37teZszTyoVnjrRCTcIigrqkbTF2VoLEHNhj9n3lJzIN2KrFOW8cwccVMmaDRKbvUtvDvs9a6saMG0JsG8YECc6%25252BSHZ0xmIbJ8N0LeZXRS8qbARlwCBgYD4FVkbawt1JGLswQs604QzDaNgw2XOaGyYL3Dhep5mgbfjFxjlpVjbJoUPmRBxsh%26session-id%3D260-1560676-0648103%26wlPopCommand%3D%26isUnrec%3D1&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amazon_checkout_in&openid.mode=checkid_setup&language=en_IN&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        # page.goto("https://www.flipkart.com/checkout/init?otracker=browse")
        yield page
        browser.close()
    

def test_element_extractor(mock_page):
    inputs = form_extractor(
        mock_page,
    )
    print("Extracted elements: ", inputs)
    assert isinstance(inputs, list), "Expected a list of elements"


