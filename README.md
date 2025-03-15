# LLL Inference API

A lightweight API for running LLM (Large Language Model) inference using Ollama and FastAPI. This project allows you to deploy a local inference endpoint for small LLMs, making it easy to integrate with other applications.

## Features

- **FastAPI**: High-performance API framework for building the inference endpoint.
- **Ollama Integration**: Seamlessly interact with Ollama for LLM inference.
- **Docker Support**: Containerized deployment for easy setup and scalability.
- **Composition-Based Design**: Clean and modular code structure using composition for configuration.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Docker**: Install Docker
- **Ollama**: Install Ollama
- **Python 3.9+**: (Optional, for local development)

## Project Structure
.
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app
│   └── config.py        # Configuration classes
├── requirements.txt     # Dependencies
├── Dockerfile           # Docker configuration
└── start.sh             # Startup script 

# Quick Start

## Run Docker Container

**1. Clone the Repository**

```bash
git clone https://github.com/your-username/llm-inference-api.git
cd llm-inference-api
```

**2. Build Docker Image**
```bash
docker build -t ollama-api .
```
**3. Run the Docker Container**

```bash
docker run -p 8000:8000 -p 11434:11434 ollama-api
```

- FastAPI: Access the API at `http://localhost:8000`.
- Ollama: Ensure Ollama is running on the host machine at port `11434`