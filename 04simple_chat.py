import json
import requests

def chat_session(model="qwen2.5-coder:0.5b"):
   messages = []
   
   while True:
       user_input = input("\nYou: ")
       if user_input.lower() in ['exit', 'quit', 'bye']:
           break
           
       messages.append({"role": "user", "content": user_input})
       
       # Convert messages to prompt format
       prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
       
       response = requests.post(
           "http://localhost:11434/api/generate",
           json={
               "model": model,
               "prompt": prompt,
               "stream": True
           },
           stream=True
       )
       
       print("\nAssistant: ", end='')
       full_response = ""
       for line in response.iter_lines():
           if line:
               json_response = json.loads(line.decode())
               if 'response' in json_response:
                   print(json_response['response'], end='', flush=True)
                   full_response += json_response['response']
                   
       messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
   print("Chat started (type 'exit' to end)")
   chat_session()