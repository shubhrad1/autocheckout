def element_extractor(page,selector):
    
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