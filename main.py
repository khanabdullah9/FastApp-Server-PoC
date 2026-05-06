from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import time

from LLM.llm import chain, form_layout
from LLM.infer_ollama import is_ollama_running, ollama_chain, calculate_num_tokens
import json
from utils import log_error, log_info, parse_llm_response
from models import Prompt, create_ollama_response

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



@api.post("/generate/")
def generate(prompt: Prompt):
    log_info("Returning pre generated json")
    with open("pre_gen.json", "r") as f:
        return json.load(f)

@api.post("/generate/")
def generate(prompt: Prompt):
    log_info(f"Prompt received: {prompt.text}")
    try:
        response = chain.invoke({
            "form_layout": form_layout,
            "user_prompt": prompt.text
        })
        log_info("Response generated")
        ai_message = response["messages"][1].content
        data_dict = json.loads(ai_message.replace("json","").replace("```",""))
        log_info("Content ready to be returned")
        return json.dumps(data_dict)
    except Exception as err:
        log_error(str(err))

@api.post("/generate_ollama/", status_code=status.HTTP_200_OK)
def generate_ollama(prompt: Prompt):
    try:
        if not is_ollama_running():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Ollama is unresponsive")
        
        start = time.perf_counter()
        response = ollama_chain.invoke({
                "form_layout": form_layout,
                "user_prompt": prompt.text
            })
        end = time.perf_counter()
        exec_time = end - start

        if not response:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Ollama response is None")
        
        log_info(prompt.text); log_info(exec_time); log_info(f"token count: {calculate_num_tokens(prompt.text)}")

        return json.dumps(response)
    except Exception as err:
        log_error(str(err))

@api.get("/test_conn_ollama/")
def test_conn_ollama():
    return "YES" if is_ollama_running() else "NO"

@api.post("/est_token_count/", status_code=status.HTTP_200_OK)
def est_token_count(prompt: Prompt):
    return {"num_tokens": calculate_num_tokens(prompt.text)}
    
