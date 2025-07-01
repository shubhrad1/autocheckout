# this method connects to AI service
# sends the prompt with all elements
# returns the relevant elements for authentication, checkout, etc.

# from openai import OpenAI
import os
from dotenv import load_dotenv
from mistralai import Mistral, UserMessage, SystemMessage
import json


def ai_service(elements, identifier):
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
    model = "mistral-ai/mistral-medium-2505"

    client = Mistral(api_key=token, server_url=endpoint)

    # Define the prompts for different stages
    # Auth_Stage 1: Find email or phone number input field and submit button
    # Auth_Stage 2: Find password or OTP input fields and submit button
    # Buy Now: Find the buy now button or equivalent

    auth_prompt_stage1="You analyze HTML UI. Find email or phone number input field and submit or continue button/input. Order of json:Email/Phone field, then Button"
    auth_prompt_stage2="You analyze HTML UI. Find password or OTP input fields, and the submit/continue button or input. If OTP field is found, add otp: true in the JSON response; otherwise, otp: false. OTP has maxlength 2 to 8. Order of json:Password/OTP field, then Button,then OTP true/false" 
    buynow_prompt="You analyzing HTML UI. Find element buy now button/input. If not present give the next best fit element like add to cart or checkout"
    
    print("Starting AI service with identifier:", identifier)

    # System content mapping based on identifier
    syscontent={
        "auth1": auth_prompt_stage1,
        "auth2": auth_prompt_stage2,
        "buynow": buynow_prompt
    }

    #Generate response from Mistral AI
    response = client.chat.complete(
    model=model,
    messages=[
        SystemMessage(content=syscontent[identifier]),
        UserMessage(content=f"Here are some elements extracted:{elements},.Return only the relevant elements in JSON format with keys: tag, text, id, class. Do not return any other information.Keep best match first."),
    ],
    )
    # Extract the content from the response
    response_content = response.choices[0].message.content
    # Clean the response content to remove any formatting artifacts
    cleaned_json = response_content.strip("`").lstrip("json").strip()
    # Parse the cleaned JSON string into a Python dictionary
    data=json.loads(cleaned_json)

    return data

