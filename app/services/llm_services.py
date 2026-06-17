import requests
import logging
LLAMA_URL = "http://localhost:8080/completion"

logger = logging.getLogger(__name__)

async def ask_llm(prompt: str):
    logger.info(
        f"Sending request to LLM. Prompt length: {len(prompt)}"
    )

    try:
        payload = {
            "prompt": prompt,
            "n_predict": 100
        }

        response = requests.post(
            LLAMA_URL,
            json=payload
        )

        logger.info(
            f"LLM response status: {response.status_code}"
        )

        data = response.json()

        logger.info(
            "LLM response received successfully"
        )

        return data["content"]
    except Exception as e:
        logger.error(f"ask_llm failed: {str(e)}")
        raise