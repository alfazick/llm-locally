from typing import Generator
import requests
import json

api_endpoint = "http://localhost:11434/api/generate"
model = "qwen2.5-coder:0.5b"


prompt = "write a for loop in cpp"
request_body = {
    "model": model,
    "prompt":prompt,
    "stream": False,
}

response = requests.post(url=api_endpoint, json=request_body)
print(response.json()['response'])