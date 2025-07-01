from element_extractor import element_extractor
from ai import ai_service

# This function automates the "Buy Now" process on a webpage.
def buynow(page,url):
    """
    This function automates the "Buy Now" process on a webpage.
    It navigates to the specified URL, extracts all buttons and submit inputs,
    filters them to find the relevant "Buy Now" button, and clicks it.

    Args:
        page: The Playwright page object.
        url (str): The URL of the webpage to navigate to.
    Returns:
        int: Returns 0 on success, -1 on failure.

    """

    print("Starting buynow function...")
    page.goto(url)
    
    #Extracting all buttons and submit inputs from the page
    buttons = element_extractor(
        page,
        'button, input[type="submit"]'
    )

    # Filtering out buttons that are not relevant and Duplicates
    buttonset=set()
    for button in buttons:
        if button['text'].strip() or button['id'].strip():
            buttonset.add((button['id'].strip(), button['text'].strip(), button['class']))

    # Running AI service to identify the "Buy Now" button
    buyelement=ai_service(buttons,"buynow")[0]
    
    # Convert returned element from AI to a selector
    selector = f"#{buyelement['id']}" if buyelement['id'] else f"button:has-text('{buyelement['text']}')"
    page.click(selector)    # Click the "Buy Now" button or equivalent
    page.wait_for_timeout(500) # Wait for the action to complete
    return 0


    
    
