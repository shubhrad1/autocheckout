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
