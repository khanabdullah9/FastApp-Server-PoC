# FastApp 🚀

**Transform Prompts into Production-Ready React Form Layouts.**

FastApp is a specialized FastAPI backend that leverages the power of Large Language Models (LLMs) to generate structured JSON layouts for React forms from simple natural language descriptions.
---

## ✨ Key Features

- **Prompt-to-JSON**: Just describe your form in plain English.
- **React-Ready**: Structured JSON output optimized for dynamic row-based React rendering.
- **Intelligent Design**: Automatically selects appropriate input types (text, select, etc.) and validation rules.
- **FastAPI Powered**: High-performance, asynchronous API.
- **LLM Integration**: Built with LangChain and OpenAI GPT-4.

---

## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Orchestration**: [LangChain](https://www.langchain.com/)
- **Intelligence**: [OpenAI GPT-4](https://openai.com/)
- **Environment**: Python 3.x

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.11+
- OpenAI API Key

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/khanabdullah9/FastApp-Server-PoC.git
cd FastApp-Server-PoC
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file in the root directory and add your OpenAI API Key:
```env
OPENAI_API_KEY=your_api_key_here
```

### 4. Run the Server
```bash
fastapi dev main.py
```

---

## 📖 Usage

Send a POST request to the `/generate/` endpoint.

**Example Request:**
```http
POST http://localhost:8000/generate/ 

# form body
# {
#   "text" : "Create a form to collect student's data for admission"
# }
```

**Example Response:**
```json
{
  "Row1": [
    {
      "Type": "text",
      "Label": "First Name",
      "Name": "first_name",
      "Placeholder": "Enter First Name",
      "Required": true
    },
    {
      "Type": "text",
      "Label": "Last Name",
      "Name": "last_name",
      "Placeholder": "Enter Last Name",
      "Required": true
    }
  ],
  "Row2": [
    {
      "Type": "select",
      "Label": "Gender",
      "Name": "gender",
      "Options": [
        {"Label": "Male", "Value": "male"},
        {"Label": "Female", "Value": "female"}
      ]
    }
  ]
}
```

---

## 📂 Project Structure

- `main.py`: Entry point for the FastAPI application.
- `llm.py`: LangChain logic and prompt templates.
- `form_layout.json`: Reference JSON schema for the AI.
- `utils.py`: Utility functions (logging, etc.).
- `py-client/`: Python client for interacting with the API.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

