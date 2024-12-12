"""OpenAI API model handler implementation, with Ollama support."""

import os
from typing import Any

from langchain_openai import AzureChatOpenAI

from readmeai.config.constants import LLMService
from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import RepositoryContext
from readmeai.models.base import BaseModelHandler
from readmeai.models.tokens import token_handler

from dotenv import load_dotenv

load_dotenv()

AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
DEPLOYMENT = os.getenv("DEPLOYMENT")

class OpenAIHandler(BaseModelHandler):
    """
    OpenAI API LLM implementation using Langchain, with Ollama support.
    """

    def __init__(
        self, config_loader: ConfigLoader, context: RepositoryContext
    ) -> None:
        super().__init__(config_loader, context)        
        self.model = AzureChatOpenAI( 
            azure_endpoint=AZURE_ENDPOINT,
            api_key=API_KEY,
            api_version=API_VERSION,
            deployment_name=DEPLOYMENT
        )

    async def _build_payload(self, prompt: str, tokens: int) -> dict:
        """Build payload for POST request to OpenAI API."""
        return {}
    
    def _model_settings(self):
        self.host_name = self.config.llm.host_name
        self.localhost = self.config.llm.localhost
        self.model = self.config.llm.model
        self.path = self.config.llm.path
        self.tokens = self.config.llm.tokens
        self.top_p = self.config.llm.top_p

    async def _make_request(
        self,
        index: str | None,
        prompt: str | None,
        tokens: int | None
    ) -> Any:
        """Processes OpenAI API LLM responses using Langchain and returns generated text."""
        try:
            prompt = await token_handler(self.config, index, prompt, tokens)

            messages = [
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": prompt},
            ]

            response = self.model.invoke(messages)
            self._logger.info(f"Response from OpenAI for '{index}': {response}")
            return index, response

        except Exception as e:
            self._logger.error(f"Unexpected error for '{index}': {e!r}")
            return index, self.placeholder
