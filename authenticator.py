from element_extractor import form_extractor
from ai import ai_service
import traceback
def authenticator(page, email, password):
    """
    Authenticates the user on the Login Page.

    Args:
        page: The Playwright page object.
        email: The user's email address.
        password: The user's password.

    Returns:
        str: The URL of the page after successful login, or None if authentication fails.
    """
    try: 
        # Extracting all form elements from the page
        extracted_elements=form_extractor(page)
        extract_len=len(extracted_elements)

        # If the length of extracted elements is greater than 2, use AI service to filter them.
        # Otherwise, use the extracted elements directly, assuming they are already relevant.
        if extract_len > 2:
                stage1_element = ai_service(extracted_elements, "auth1")
        else:
            stage1_element=extracted_elements

        # Check if the authentication stage 1 elements contain at least two elements (email/phone field and submit button)
        if len(stage1_element) < 2:
            raise Exception("No email or phone number input field found.")
        
        email_field = stage1_element[0]
        submit_button=stage1_element[1]

        # Constructing selectors for email/phone field and submit button
        email_selector = f"#{email_field['id']}" if email_field['id'] else f"[class='{email_field['class']}']" 
        submit_selector = f"#{submit_button['id']}" if submit_button['id'] else f"[class='{submit_button['class']}']"

        page.fill(email_selector, email)    # Fill the email or phone number input field
        page.click(submit_selector)   # Click the submit button
        page.wait_for_timeout(500)  # Wait for the action to complete
        
        ## Upon successful submission, the page should redirect to the password input stage.
        extracted_elements=form_extractor(page) # Extracting form elements again after the first submission
        extract_len=len(extracted_elements) 

        # If the length of extracted elements is greater than 2, use AI service to filter them.
        # Otherwise, use the extracted elements directly, assuming they are already relevant.
        if extract_len>2:
                stage2_element = ai_service(extracted_elements, "auth2")
        else:
            stage2_element=extracted_elements

        # Check if the authentication stage 2 elements contain at least two elements (password field and submit button)
        if len(stage2_element) < 2:
            raise Exception("No password or OTP input field found.")
        
        passfield=stage2_element[0]
        submit_button=stage2_element[1]

        # Constructing selectors for password field and submit button
        password_selector = f"#{passfield['id']}" if passfield['id'] else f"[class='{passfield['class']}']"
        submit_selector = f"#{submit_button['id']}" if submit_button['id'] else f"[class='{submit_button['class']}']"
        
        element_length = len(stage2_element)
        otpfield=stage2_element[2]['otp'] if element_length >= 3 else None
        
        # Check if the password field is an OTP field based on its maxLength or presence of otp key
        if otpfield or ('maxLength' in stage2_element[0]): 
            # Assuming OTP fields have a maxLength between 4 and 8, if not, treat it as a password field
            if stage2_element[0]['maxLength'] > 3 and stage2_element[0]['maxLength'] < 9:
                print("OTP field found, please enter the OTP manually.....")
                otp=input("Enter the OTP: ")
                page.fill(password_selector,otp)
                page.click(submit_selector)
                #page.wait_for_timeout(500)
                return page.url  # Return the current URL after login
            else:
                page.fill(password_selector, password)
                page.click(submit_selector)
                #page.wait_for_timeout(500)
                return page.url
        
        else:   
            # If it's a regular password field, fill it with the provided password
            page.click(submit_selector)
            page.fill(password_selector, password)
            return page.url
            #page.wait_for_timeout(500)

    except Exception as e:
        raise Exception(f"Error during authentication: {e}")