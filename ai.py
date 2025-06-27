# this method connects to AI service
# sends the prompt with all elements
# returns the relevant elements for authentication, checkout, etc.

from openai import OpenAI
import os
from dotenv import load_dotenv


def ai_service(elements):
    load_dotenv()
    token=os.getenv("OPENAI_API_KEY")
    endpoint = "https://models.github.ai/inference"
    model_name = "openai/o3"

    client = OpenAI(
    base_url=endpoint,
    api_key=token,
    )

    response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an expert at analyzing HTML UI elements. Your task is to find elements related to user authentication like login, sign in, register, etc.",
        },
        {
            "role": "user",
            "content": f"Here are some elements extracted:{elements}, determine which elements are related to user authentication.Return only the relevant elements in JSON format with keys: tag, text, id, class. Do not return any other information.",
            
        }
        ],
    model=model_name
    )

    print(response.choices[0].message.content)
