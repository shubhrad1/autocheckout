import os
from dotenv import load_dotenv
from mistralai import Mistral, UserMessage, SystemMessage, models
import json
from typing import List, Dict


def ai_service(elements, identifier:str) -> Dict:
    """
    This function connects to the Mistral AI service to process HTML elements

    Args:
        elements (list): A list of HTML elements extracted from the page.
        identifier (str): A string that identifies the type of processing to be done (e.g., "auth1", "auth2", "buynow").
    
    Returns:
        dict: A dictionary containing the relevant elements in JSON format.
    
    """

    load_dotenv()
    
    #Using Mistral AI service
    token=os.getenv("MISTRAL_API_KEY")
    endpoint=os.getenv("MISTRAL_API_ENDPONT")
    model=os.getenv("MISTRAL_MODEL")

    if not token :
        raise KeyError("MISTRAL_API_KEY not found in environment variables. Please set it to use the AI service.")
    if not endpoint:
        raise KeyError("MISTRAL_API_ENDPOINT not found in environment variables. Please set it to use the AI service.")
    if not model:
        raise KeyError("MISTRAL_MODEL not found in environment variables. Please set it to use the AI service.")
        



    client = Mistral(api_key=token, server_url=endpoint)    #Initialize the Mistral client with API key and endpoint

    # Define the prompts for different stages
    # Auth_Stage 1: Find email or phone number input field and submit button
    # Auth_Stage 2: Find password or OTP input fields and submit button
    # Buy Now: Find the buy now button or equivalent

    auth_prompt_stage1="You analyze HTML UI. Find email or phone number input field and submit or continue button/input. Order of json:Email/Phone field, then Button"
    auth_prompt_stage2="You analyze HTML UI. Find password or OTP input fields, and the submit/continue button or input. If OTP field is found, add otp: true in the JSON response; otherwise, otp: false. OTP has maxlength 2 to 8. Order of json:Password/OTP field, then Button,then OTP true/false" 
    buynow_prompt="You analyzing HTML UI. Find element buy now button/input. If not present give the next best fit element like add to cart or checkout"
    address_extractor="You analyze a string. Find if Home Address/Office Address/Shipping Address is present and return the address in json format with keys: Phone, Name, Address, City, State, Zipcode. If not present return empty json."

    html_extraction_prompt=f"Here are some elements extracted:{elements},.Return only the relevant elements in JSON format with keys: tag, text, id, class. Do not return any other information.Keep best match first."
    address_extraction_prompt=f"Here is a string {elements[0]['text']}. Extract the address from here. Dot not return any other information or chat. Just the JSON. If present return topmost address in json .If not present return empty json."
    print("Starting AI service with identifier:", identifier)

    # System content mapping based on identifier
    syscontent={
        "auth1": auth_prompt_stage1,
        "auth2": auth_prompt_stage2,
        "buynow": buynow_prompt,
        "address": address_extractor
    }
    
    #Generate response from Mistral AI
    try:
        response = client.chat.complete(
            model=model,
            messages=[
                SystemMessage(content=syscontent[identifier]),
                UserMessage(content=html_extraction_prompt if identifier in ["auth1", "auth2", "buynow"] else address_extraction_prompt),
            ],
        )
    except models.HTTPValidationError as e:
        raise Exception(f"HTTP Validation Error: {e}")
    except models.SDKError as e:
        raise Exception(f"SDK Error: {e}")
    except Exception as e:
        raise Exception(f"An error occurred while calling the Mistral AI service: {e}")
    
    response_content = None
    try:
        # Extract the content from the response
        response_content = response.choices[0].message.content
        
        # Ensure response_content is a string
        if isinstance(response_content, list):
            response_content = "".join(str(chunk) for chunk in response_content)
        elif response_content is None:
            raise Exception("Response content is None.")
        else:
            response_content = str(response_content)
        # Clean the response content to remove any formatting artifacts
        cleaned_json = response_content.strip("`").lstrip("json").strip()
        # Parse the cleaned JSON string into a Python dictionary
        data=json.loads(cleaned_json)
    except json.JSONDecodeError as e:
        raise Exception(f"JSON Decode Error: {e}. Response content was: {response_content}")

    return data

