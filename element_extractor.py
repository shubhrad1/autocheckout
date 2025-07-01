def element_extractor(page,selector):
    """

    This function extracts elements from a webpage using Playwright.
    Args:
        page: The Playwright page object.
        selector (str): The CSS selector to find elements on the page.
    Returns:
        list: A list of dictionaries containing information about the elements found.
    
    """
    
    elements= page.eval_on_selector_all(
        selector,
        '''elements => elements.map(el => ({
            tag: el.tagName,
            text: el.innerText || el.value || '',
            id: el.id,
            class: el.className
        }))'''
    )
    return elements

def form_extractor(page):
    """
    This function extracts form elements from a webpage using Playwright.
    Args:
        page: The Playwright page object.
    Returns:
        list: A list of dictionaries containing information about the form elements found.
    
    """
    form_elements= page.eval_on_selector_all(
        "form input:not([type='hidden']), form button[type='submit'],form div input:not([type='hidden']), form div button[type='submit']",
        '''elements => elements.filter(el => !el.readOnly).map(el => ({
            tag: el.tagName,
            text: el.innerText || el.value || '',
            id: el.id,
            class: el.className,
            type: el.type || '',
            title: el.title || '',
            name: el.name || '',
            maxLength: el.maxLength || '',
        }))'''
    )
    return form_elements