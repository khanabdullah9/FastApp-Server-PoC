from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import requests

from utils import get_ollama_conf

OLLAMA_CONF = get_ollama_conf()
POD_ID = OLLAMA_CONF["POD_ID"]
PORT =   OLLAMA_CONF["PORT"]
BASE_URL = f"https://{POD_ID}-{str(PORT)}.proxy.runpod.net"

llm = ChatOllama(
    model="llama3:8b", 
    base_url=BASE_URL
)

prompt = ChatPromptTemplate.from_template(
    """
        You are an experienced software engineer. 
        You are supposed to design the layout for react based forms and describe them in json.

        Here is an example json file: 
        <form_layout_start>
        {form_layout}
        <form_layout_end>

        Here is the prompt from the end user: {user_prompt}

        Return ONLY the JSON object
    """
)

ollama_chain = prompt | llm

def is_ollama_running():
    try:
        response = requests.get(f"{BASE_URL}/api/tags", timeout = 5)
        return response.status_code == 200
    except Exception as err:
        return False