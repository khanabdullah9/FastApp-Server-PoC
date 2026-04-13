from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
import json
from dotenv import load_dotenv

load_dotenv()

llm = create_agent(
    model = "gpt-4-turbo",
    system_prompt = "You are a skill software engineer"
)

form_layout = ""
with open("form_layout.json","r") as f:
    form_layout = json.load(f)

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

chain = prompt | llm

# user_prompt = "Create a form to collect student details for admission"
# response = chain.invoke({
#     "form_layout": form_layout,
#     "user_prompt": user_prompt
# })
# print(response)