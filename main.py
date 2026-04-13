from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from llm import chain, form_layout
import json
from utils import log_error, log_info

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/")
def root():
    return "Server is running!"

@api.get("/llm/{prompt}")
def get_layout(prompt: str):
    with open("pre_gen.json", "r") as f:
        return json.load(f)

# @api.get("/llm/{prompt}")
# def get_layout(prompt: str):
#     log_info(f"Prompt received: {prompt}")
#     try:
#         response = chain.invoke({
#             "form_layout": form_layout,
#             "user_prompt": prompt
#         })
#         log_info("Response generated")
#         ai_message = response["messages"][1].content
#         data_dict = json.loads(ai_message.replace("json","").replace("```",""))
#         log_info("Content ready to be returned")
#         return json.dumps(data_dict)
#     except Exception as err:
#         log_error(str(err))