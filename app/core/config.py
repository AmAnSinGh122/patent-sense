from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ollama_api_base: str = "http://localhost:11434"
    model_name: str = "ollama_chat/qwen2.5:7b"

    class Config:
        env_file = ".env"


settings = Settings()
