import requests

test_prompt = [
    "Create a form to collect student data for python internship program.",
    "Create a form to collect data of students who wish to go on the industrial visit.",
    "Create a job application form for a Senior DevOps Engineer including a file upload for resumes and a dropdown for years of experience.",
    "Generate a customer satisfaction survey with a 1-5 star rating for service, a checkbox list for 'What did you order?', and a text area for feedback.",
    "Build a hackathon registration form that collects a team name, a dynamic list of up to 4 team members' emails, and a GitHub profile URL.",
    "Create a patient intake form with fields for full name, date of birth (date picker), a phone number field, and a checklist for medical history.",
    "Generate a product return request form asking for Order ID, purchase date, a 'Reason for Return' dropdown, and a toggle for 'Refund' vs 'Exchange'.",
    "Create a form for a corporate retreat to collect meal preferences (Vegan, Halal, GF), t-shirt size (S-XXL), and a slider for 'Number of Guests'.",
    "Build a real estate listing form with a currency-formatted field for 'Asking Price', numeric input for 'Bedrooms', and a checkbox for 'Pet Friendly'.",
    "Generate a summer camp enrollment form that validates student age between 5 and 15 and includes a mandatory 'Parental Waiver' checkbox.",
    "Create a small business loan application asking for annual revenue, loan amount, and a multi-select for 'Intended use of funds'.",
    "Design a simple newsletter signup form with a validated email field and a 'Terms and Conditions' toggle."
]

data = {
    "text": test_prompt[4]
}
response = requests.post(f"http://127.0.0.1:8000/generate_ollama/", json = data)
print(response.status_code)
if response.status_code == 200:
    print(response.json())
else:
    print(response.text)