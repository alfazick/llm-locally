import json
import requests

prompt = "write a for loop in cpp"
api_endpoint = "http://localhost:11434/api/generate"
request_body = {
    "model": "qwen2.5-coder:0.5b",
    "prompt":prompt,
    "stream": True
}

response = requests.post(url=api_endpoint, json=request_body, stream=True)
for line in response.iter_lines():
    if line:
        json_response = json.loads(line.decode())
        if 'response' in json_response:
            print(json_response['response'], end='', flush=True)