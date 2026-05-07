import requests
import json

data = {
    "text": "Random prompt"
}
response = requests.post(f"http://127.0.0.1:8000/generate_mock/", json = data)
print(response.status_code)
if response.status_code == 200:
    print(response.json())
else:
    print(response.text)