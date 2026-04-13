import requests

prompt = "Create a HR form to collect data of new employees."
response = requests.get(f"http://127.0.0.1:8000/llm/{prompt}", )
print(response.status_code)
if response.status_code == 200:
    print(response.json())