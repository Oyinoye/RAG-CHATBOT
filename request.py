import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = os.getenv("APP_BASE_URL")
url = f"{BASE_URL}/query"
headers = {
    'accept': 'application/json'
}
params = {
    'query': 'What do you know about football?',
}

response = requests.post(url, headers=headers, data=json.dumps(params))

print(response.json())
