import requests

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

def generate_response(prompt: str):
    payload = {
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False  # IMPORTANT: get one JSON, not chunks
    }

    res = requests.post(OLLAMA_URL, json=payload, timeout=120)
    res.raise_for_status()

    data = res.json()

    # Safe extraction
    if "response" in data:
        return data["response"]

    # Fallback (debug)
    return str(data)