from google.adk.models.lite_llm import LiteLlm
from app.core.config import settings


def get_llm():
    return LiteLlm(model=settings.model_name)
