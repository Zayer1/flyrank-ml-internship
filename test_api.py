import requests

url = "http://127.0.0.1:8000/api/score"
file_path = "data/raw/content_refresh_anonymized.csv"

with open(file_path, "rb") as f:
    response = requests.post(url, files={"file": f})

print(response.status_code)
print(response.json())
