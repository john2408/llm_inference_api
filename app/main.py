import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import ollama
from app.config import InferenceRequest, ModelConfig

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get Ollama port from environment variable (default to 11434)
OLLAMA_PORT = int(os.getenv("OLLAMA_PORT", 11434))

@app.post("/generate")
async def generate(request: InferenceRequest):
    """Inference endpoint using composed config"""
    try:
        # Set the Ollama client to use the custom port
        ollama_client = ollama.Client(host=f"http://host.docker.internal:{OLLAMA_PORT}")
        response = ollama_client.generate(
            model=request.config.model,
            prompt=request.prompt,
            options={
                "num_predict": request.config.max_tokens,
                "temperature": request.config.temperature
            }
        )
        return {"response": response['response']}
    except Exception as e:
        return {"error": str(e)}