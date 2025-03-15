# Use a lightweight Python image
FROM python:3.9-slim

# Set up working directory
WORKDIR /app

# Install system dependencies + Ollama
# RUN apt-get update && apt-get install -y curl
# RUN curl -fsSL https://ollama.com/install.sh | sh
# RUN ollama serve
# RUN ollama pull llama:3.2

# Copy requirements first for layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose FastAPI port
EXPOSE 8000
# EXPOSE 11434

# Set environment variable for Ollama port (default to 11434)
ENV OLLAMA_PORT=11434

# Startup script
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]