from pydantic import BaseModel, Field
from typing import Optional, Any

class Prompt(BaseModel):
    text: str

class OllamaResponse(BaseModel):
    user_prompt: str
    model_response: str
    infer_time: int

def create_ollama_response(prompt, response, exec_time):
    if not response or not exec_time:
        return {}
    
    obj = OllamaResponse()
    obj.user_prompt = prompt
    obj.model_response = response
    obj.infer_time = exec_time
    return obj.model_dump_json(indent=2)

class Option(BaseModel):
    label: str = Field(alias = "Label", description = "Label for the option tag for the select tag")
    value: Any = Field(alias = "Value", desciprtion = "Actual value of the select tag. Can store any type")

class FormField(BaseModel):
    type: str = Field(alias = "Type", description = "Type of the input field. Example text, select etc.")
    label: str = Field(alias = "Label", description = "Label for the field")
    name: str = Field(alias = "Name", description = "Name of the field")
    placeholder: str = Field(alias = "Placeholder", description = "Description of the field")
    required: bool = Field(alias = "Required", description = "Whether the field is mandatory or not")
    options: Optional[list[Option]] = Field(alias = "Options", description = "Options tag/s for the select tag")

