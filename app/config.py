from pydantic import BaseModel

class ModelConfig(BaseModel):
    """Composed class for model configuration"""
    model: str = "deepseek-r1:14b"
    max_tokens: int = 1000
    temperature: float = 0.7

class InferenceRequest(BaseModel):
    """Main request class using composition"""
    prompt: str
    config: ModelConfig = ModelConfig()  # Composition here!