import requests

test_prompt = [
    "Create a form to collect student data for python internship program.",
    "Create a form to collect data of students who wish to go on the industrial visit."
]

data = {
    "text": test_prompt[1]
}
response = requests.post(f"http://127.0.0.1:8000/generate_ollama/", json = data)
print(response.status_code)
if response.status_code == 200:
    print(response.json())
else:
    print(response.text)