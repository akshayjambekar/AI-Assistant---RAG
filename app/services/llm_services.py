import requests

LLAMA_URL = "http://localhost:8080/completion"

async def ask_llm(prompt: str):

    payload = {
        "prompt": prompt,
        "n_predict": 100
    }

    response = requests.post(
        LLAMA_URL,
        json=payload
    )

    data = response.json()

    return data["content"]