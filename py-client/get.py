import requests

data = {
    "text": "Create a form to collect student's data for admission"
}
response = requests.post(f"http://127.0.0.1:8000/generate/", json = data)
print(response.status_code)
if response.status_code == 200:

    # try:
    #     with open("pre_gen.json", "w") as f:
    #         f.write(response.json())
    # except Exception as err:
    #     print("Could not write json")

    print(response.json())