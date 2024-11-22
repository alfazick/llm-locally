import gradio as gr
import json
import requests

def chat_with_ollama(message, history):
    # Format chat history
    messages = []
    for human, assistant in history:
        messages.extend([
            {"role": "user", "content": human},
            {"role": "assistant", "content": assistant}
        ])
    messages.append({"role": "user", "content": message})
    
    prompt = "Chat history:\n" + "\n".join([f"{m['role']}: {m['content']}" for m in messages])
    
    # Stream the response
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5-coder:0.5b",
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    partial_response = ""
    for line in response.iter_lines():
        if line:
            json_response = json.loads(line.decode())
            if 'response' in json_response:
                partial_response += json_response['response']
                yield partial_response
    
    return partial_response

demo = gr.ChatInterface(
    fn=chat_with_ollama,
    title="Ollama Chat (Qwen 0.5b)",
    description="Chat with Qwen model via Ollama.",
)

if __name__ == "__main__":
    demo.launch()