#!/bin/sh

# Start Ollama in background
ollama serve &

# Wait for Ollama to initialize
sleep 5

# Start FastAPI
uvicorn app.main:app --host 0.0.0.0 --port 8000