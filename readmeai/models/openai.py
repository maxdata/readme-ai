"""OpenAI API model handler implementation, with Ollama support."""

import os
from typing import Any

from langchain_openai import AzureChatOpenAI

from readmeai.config.constants import LLMService
from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import RepositoryContext
from readmeai.models.base import BaseModelHandler
from readmeai.models.tokens import token_handler


class OpenAIHandler(BaseModelHandler):
    """
    OpenAI API LLM implementation using Langchain, with Ollama support.
    """

    def __init__(
        self, config_loader: ConfigLoader, context: RepositoryContext
    ) -> None:
        super().__init__(config_loader, context)
        self._initialize_model()

    def _initialize_model(self):
        self.model = AzureChatOpenAI(
            model="gpt-4o",
            azure_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_version=os.getenv("AZURE_OPENAI_VERSION"),
        )

    async def _make_request(
        self,
        index: str | None,
        prompt: str | None,
        tokens: int | None,
        repo_files: Any,
    ) -> Any:
        """Processes OpenAI API LLM responses using Langchain and returns generated text."""
        try:
            prompt = await token_handler(self.config, index, prompt, tokens)

            response = self.model(prompt)
            self._logger.info(f"Response from OpenAI for '{index}': {response}")
            return index, response

        except Exception as e:
            self._logger.error(f"Unexpected error for '{index}': {e!r}")
            return index, self.placeholder
