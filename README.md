# LLL Inference API

A lightweight API for running LLM (Large Language Model) inference using Ollama and FastAPI. This project allows you to deploy a local inference endpoint for small LLMs, making it easy to integrate with other applications.

**Note**: The current implementation focuses on using the ollama API from host. This allows to keep the docker container size small (aprox. 645 MB) for local testing.

If you want to change the behaviour, adjust the file `main.py`:

```python
ollama_client = ollama.Client(host=f"http://host.docker.internal:{OLLAMA_PORT}")
```

Inside the `Dockerfile`, the commented sections outline the steps required to install the Ollama server within the Docker container.

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
```bash
.
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app
│   └── config.py         # Configuration classes
├── requirements.txt      # Dependencies
├── Dockerfile            # Docker configuration
├── .devcontainer       
│   ├── devcontainer.json # Devcontainer config
└── start.sh              # Startup script 
```

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


## API Endpoints

**Generate Text**

- **Endpoint**: POST /generate

- **Request Body:**

```json
{
  "prompt": "What is the capital of France?",
  "config": {
    "model": "llama3.2:latest",
    "max_tokens": 100,
    "temperature": 0.7
  }
}
``` 

- **Response:**
```json
{
  "response": "The capital of France is Paris."
}
```

# Contributing

Contributions are welcome! Please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bugfix.
- Submit a pull request with a detailed description of your changes.

# License

This project is licensed under the MIT License. See the LICENSE file for details

# Acknowledgments

**Ollama**: For providing an easy-to-use LLM inference framework.
**FastAPI**: For enabling high-performance API development.
**Docker**: For simplifying deployment and scalability.