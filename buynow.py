from element_extractor import element_extractor
from ai import ai_service
def buynow(page,url):
    try:
        print("Starting buynow function...")
        page.goto(url)
        buttons = element_extractor(
            page,
            'button, input[type="submit"]'
        )
        buttonset=set()
        for button in buttons:
            if (button['text'] and button['text'].strip()) or (button['id'] and button['id'].strip()):
                buttonset.add((button['id'], button['text'].strip(), button['class']))

        buyelement=ai_service(buttons,"buynow")[0]
        
        selector = f"#{buyelement['id']}" if buyelement['id'] else f"button:has-text('{buyelement['text']}')"
        page.click(selector)
        page.wait_for_timeout(3000)
        print(f"Clicked on Buy Now button with selector: {selector}")
        return 0
    
    except Exception as e:
        print(f"Error in buynow function: {e}")
        return -1
    
    
