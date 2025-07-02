from element_extractor import element_extractor
from ai import ai_service
from playwright.sync_api import Page
# This function automates the "Buy Now" process on a webpage.
def buynow(page: Page,url: str)-> None:
    """
    This function automates the "Buy Now" process on a webpage.
    It navigates to the specified URL, extracts all buttons and submit inputs,
    filters them to find the relevant "Buy Now" button, and clicks it.

    Args:
        page: The Playwright page object.
        url (str): The URL of the webpage to navigate to.


    """
    try:

        print("Starting buynow function...")
        page.goto(url)
        
        #Extracting all buttons and submit inputs from the page
        buttons = element_extractor(
            page,
            'button, input[type="submit"]'
        )

        # Filtering out buttons that are not relevant and Duplicates
        seen=set()
        unique_buttons = []

        for button in buttons:
            identifier=frozenset(button.items())
            if identifier not in seen:
                seen.add(identifier)
                unique_buttons.append(button)
        buttons = unique_buttons
        if not buttons or len(buttons) == 0:
            raise Exception("No buttons or submit inputs found on the page. Please check the page structure or the selector used.")



        #Running AI service to identify the "Buy Now" button
        buyelement=ai_service(buttons,"buynow")

        if not buyelement or len(buyelement)==0:
            raise Exception("No 'Buy Now' button found. Please check the page or the AI service response.")
        buyelement = buyelement[0]  # Assuming the first element is the most relevant one

        
        # Convert returned element from AI to a selector
        selector = f"#{buyelement['id']}" if buyelement['id'] else f"button:has-text('{buyelement['text']}')"
        page.click(selector)    # Click the "Buy Now" button or equivalent
        page.wait_for_timeout(500) # Wait for the action to complete
    except Exception as e:
        raise Exception(f"Error in buynow function: {e}")


    
    
