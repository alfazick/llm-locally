import json
import requests

def generate_text(prompt, model="qwen2.5-coder:0.5b", stream=False):
   response = requests.post(
       "http://localhost:11434/api/generate",
       json={"model": model, "prompt": prompt, "stream": stream},
       stream=stream
   )
   if stream:
       for line in response.iter_lines():
           if line:
               json_response = json.loads(line.decode())
               if 'response' in json_response:
                   print(json_response['response'], end='', flush=True)
   else:
       return response.text

if __name__ == "__main__":
   prompt = "Write a for loop in cpp"
   # Streaming
   generate_text(prompt, stream=True)