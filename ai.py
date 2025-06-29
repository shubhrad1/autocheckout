# this method connects to AI service
# sends the prompt with all elements
# returns the relevant elements for authentication, checkout, etc.

from openai import OpenAI
import os
from dotenv import load_dotenv


def ai_service(elements, identifier):
    load_dotenv()
    token=os.getenv("OPENAI_API_KEY")
    endpoint = "https://models.github.ai/inference"
    model_name = "openai/o3"

    client = OpenAI(
    base_url=endpoint,
    api_key=token,
    )

    auth_prompt="You are an expert at analyzing HTML UI elements. Your task is to find elements related to user authentication like login, sign in, register, etc."
    buynow_prompt="You are an expert at analyzing HTML UI elements. Your task is to find element that is related to buy now or checkout. If not present give the next best fit element like add to cart"

    response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content":{auth_prompt if identifier == "auth" else buynow_prompt}         
            },
        {
            "role": "user",
            "content": f"Here are some elements extracted:{elements},.Return only the relevant elements in JSON format with keys: tag, text, id, class. Do not return any other information.",
            
        }
        ],
    model=model_name,
    )

    return response.choices[0].message.content[0]
