from fastapi import FastAPI
from llm import chain, form_layout
import json
from utils import log_error

api = FastAPI()

@api.get("/")
def root():
    return "Server is running!"

@api.get("/llm/{prompt}")
def get_layout(prompt: str):
    try:
        response = chain.invoke({
            "form_layout": form_layout,
            "user_prompt": prompt
        })
        ai_message = response["messages"][1].content
        data_dict = json.loads(ai_message.replace("json","").replace("```",""))
        print(data_dict)
        return json.dumps(data_dict)
    except Exception as err:
        log_error(str(err))