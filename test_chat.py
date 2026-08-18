import requests
import json

url = "http://127.0.0.1:8000/api/chat"
payload = {
    "message": "Hello!",
    "context": "{}"
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.text)
