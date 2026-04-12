import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "http://127.0.0.1:8000/ai-agent"

headers = {
    "x-api-key": os.getenv("API_KEY"),
    "Content-Type": "application/json"
}

data = {
    "prompt": "Latest news about AI"
}

response = requests.post(url, headers=headers, json=data)

print(response.json())
