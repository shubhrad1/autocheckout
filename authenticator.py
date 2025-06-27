def authenticator(page, email, password):
    """
    Authenticates the user on the Amazon login page.

    Args:
        page: The Playwright page object.
        email: The user's email address.
        password: The user's password.
    """
    page.goto("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Flog-in%2Fs%3Fk%3Dlog%2Bin%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    page.fill("input[name='email']", email)
    page.click("input#continue")
    page.fill("input[name='password']", password)
    page.click("input#signInSubmit")
    page.wait_for_timeout(5000)  # Wait for 5 seconds to ensure login
    page.screenshot(path="amazon_login.png")  # Take a screenshot after login
    
