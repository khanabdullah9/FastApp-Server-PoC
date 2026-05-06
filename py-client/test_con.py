import requests

response = requests.get("http://127.0.0.1:8000/test_conn_ollama/")
print(response.status_code)
print(response.text)
    