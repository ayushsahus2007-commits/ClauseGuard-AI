import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.1:8b",
        "prompt": "Explain Retrieval-Augmented Generation (RAG) in simple words.",
        "stream": False
    }
)

print(response.json()["response"])