import requests

response = requests.post(
    "http://localhost:8000/generate",
    json={
        "prompt": "Explain quantum computing in simple terms",
        "config": {
            "model": "deepseek-r1:14b",
            "max_tokens": 1000,
            "temperature": 0.8
        }
    }
)
print(response.json())