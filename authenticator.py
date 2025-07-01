from element_extractor import form_extractor
from ai import ai_service
import traceback
def authenticator(page, email, password):
    """
    Authenticates the user on the Amazon login page.

    Args:
        page: The Playwright page object.
        email: The user's email address.
        password: The user's password.
    """
    try:
        extracted_elements=form_extractor(page)

        extract_len=len(extracted_elements)
        if extract_len > 2:
        
            stg1_element = ai_service(extracted_elements, "auth1")
        else:
            stg1_element=extracted_elements

        if len(stg1_element) < 2:
            print("No email or phone number input field found.")
            return None
        email_field = stg1_element[0]
        submit_button=stg1_element[1]

        email_selector = f"#{email_field['id']}" if email_field['id'] else f"[class='{email_field['class']}']" 
        submit_selector = f"#{submit_button['id']}" if submit_button['id'] else f"[class='{submit_button['class']}']"

        page.fill(email_selector, email)
        page.click(submit_selector)
        page.wait_for_timeout(500)  
        
        extracted_elements=form_extractor(page)
        
        extract_len=len(extracted_elements)

        if extract_len>2:
            stg2_element = ai_service(extracted_elements, "auth2")
        else:
            stg2_element=extracted_elements
        if len(stg2_element) < 2:
            print("No password input field found.")
            return None
        
        passfield=stg2_element[0]
        submit_button=stg2_element[1]

        password_selector = f"#{passfield['id']}" if passfield['id'] else f"[class='{passfield['class']}']"
        submit_selector = f"#{submit_button['id']}" if submit_button['id'] else f"[class='{submit_button['class']}']"
        
        element_length = len(stg2_element)
        otpfield=stg2_element[2]['otp'] if element_length >= 3 else None
        
        if otpfield or ('maxLength' in stg2_element[0]): 
            if stg2_element[0]['maxLength'] > 3 and stg2_element[0]['maxLength'] < 9:
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
            page.fill(password_selector, password)
            page.click(submit_selector)
            #page.wait_for_timeout(500)
            return page.url

    except Exception as e:
        print(f"Error during authentication: {e}")
        print(traceback.format_exc())
        return None
