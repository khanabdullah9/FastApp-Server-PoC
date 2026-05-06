import requests

data = {
    "text": "Create a form to collect student data for python internship program."
}
response = requests.post(f"http://127.0.0.1:8000/est_token_count/", json = data)
print(response.status_code)
if response.status_code == 200:
    print(response.json())
else:
    print(response.text)