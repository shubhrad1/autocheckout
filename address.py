from playwright.sync_api import Page
from element_extractor import form_extractor
from ai import ai_service
from pytesseract import image_to_string
from PIL import Image
import os

def address(page: Page):
    """
    This function extracts the address from a webpage by taking a screenshot of the page,
    processing the image to extract text, and then using an AI service to identify the address.

    Args:
        page (Page): The Playwright page object representing the webpage.
    """
    try:
        page.screenshot(path="address_screenshot.png")
        if not os.path.exists("address_screenshot.png"):
            raise Exception("Screenshot was not created.")
        
        address_image= Image.open("address_screenshot.png")
        address_text = image_to_string(address_image)
        if not address_text.strip():
            raise Exception("No text found in the screenshot. Ensure the screenshot contains address information.")
        os.remove("address_screenshot.png")  # Clean up the screenshot file after processing
        address_list=[]
        address_list.append({
            "text": address_text,

        })
        address=ai_service(address_list, "address")
        if not address:
            print("No address found. Add/Set address manually from URL.")
            return 
        print("Available addresses:", address)
        return
    except Exception as e:
        raise Exception(f"Error in address extraction: {e}")
    




