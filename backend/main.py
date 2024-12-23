from typing import List
from fastapi import FastAPI
from openai import OpenAI


from request import MessageRequestBody
from response import MessageResponseBody
from chatgpt import recomend_response, clean_description, get_url, true_get_url, description_change

app = FastAPI()

@app.post("/spi/jaljal", response_model = MessageResponseBody)
def jaljal_question(requests: List[MessageRequestBody]):
    """
    対話内容からジャルジャル動画を返却する
    """
    description_jaljal = recomend_response(requests)
    
    cleaned_description = clean_description(description_jaljal)
    
    got_url = get_url(cleaned_description)
    
    true_url = true_get_url(got_url)
    
    description_all = description_change(cleaned_description)
    
    return MessageResponseBody(
        data=true_url,
        description=description_all
    )