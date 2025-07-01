# this method connects to AI service
# sends the prompt with all elements
# returns the relevant elements for authentication, checkout, etc.

# from openai import OpenAI
import os
from dotenv import load_dotenv
from mistralai import Mistral, UserMessage, SystemMessage
import json


def ai_service(elements, identifier):

    load_dotenv()
    # token=os.getenv("OPENAI_API_KEY")
    # endpoint = "https://models.github.ai/inference"
    # model_name = "openai/o3"

    # client = OpenAI(
    # base_url=endpoint,
    # api_key=token,
    # )
    token=os.getenv("MISTRAL_API_KEY")
    endpoint = "https://models.github.ai/inference"
    model = "mistral-ai/mistral-medium-2505"

    client = Mistral(api_key=token, server_url=endpoint)


    auth_prompt_stage1="You are an expert at analyzing HTML UI elements. Your task is to find email or phone number input field and the the submit or continue button/input. Order of json:Email/Phone field, then Button"
    auth_prompt_stage2="You analyze HTML UI. Find password or OTP input fields, and the submit/continue button or input. If OTP field is found, add otp: true in the JSON response; otherwise, otp: false. OTP has maxlength 2 to 8. Order of json:Password/OTP field, then Button,then OTP true/false" 
    # auth_button="You are an expert at analyzing HTML UI elements. Your task is to find the continue button or input field with type submit. If not present give the next best fit element like login or sign in button."
    buynow_prompt="You are an expert at analyzing HTML UI elements. Your task is to find element that is related to buy now. If not present give the next best fit element like add to cart or checkout"
    print("Starting AI service with identifier:", identifier)
    # response = client.chat.completions.create(
    # messages=[
    #     {
    #         "role": "system",
    #         "content":auth_prompt if identifier == "auth" else buynow_prompt         
    #         },
    #     {
    #         "role": "user",
    #         "content": f"Here are some elements extracted:{elements},.Return only the relevant elements in JSON format with keys: tag, text, id, class. Do not return any other information.",
            
    #     }
    #     ],
    # model=model_name,
    # )
    syscontent={
        "auth1": auth_prompt_stage1,
        "auth2": auth_prompt_stage2,
        # "auth_button": auth_button,
        "buynow": buynow_prompt
    }
    response = client.chat.complete(
    model=model,
    messages=[
        SystemMessage(content=syscontent[identifier]),
        UserMessage(content=f"Here are some elements extracted:{elements},.Return only the relevant elements in JSON format with keys: tag, text, id, class. Do not return any other information.Keep best match first."),
    ],



    )

    response_content = response.choices[0].message.content
    
    cleaned_json = response_content.strip("`").lstrip("json").strip()

    data=json.loads(cleaned_json)
    
    
    
    return data

