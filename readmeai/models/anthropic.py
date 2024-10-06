"""Anthropic API service implementation."""

from typing import Any

import anthropic
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import RepositoryContext
from readmeai.models.base import BaseModelHandler
from readmeai.models.tokens import token_handler


class AnthropicHandler(BaseModelHandler):
    """
    Anthropic Claude LLM API service implementation.
    """

    def __init__(
        self, config_loader: ConfigLoader, context: RepositoryContext
    ) -> None:
        super().__init__(config_loader, context)
        self._model_settings()

    def _model_settings(self):
        self.client = anthropic.AsyncAnthropic()
        self.model = "claude-3-opus-20240229"

    async def _build_payload(self, prompt: str, tokens: int) -> dict[str, Any]:
        """Build payload for POST request to the Anthropic API."""
        return {
            "model": self.model,
            "max_tokens": tokens,
            "temperature": self.temperature,
            "messages": [{"role": "user", "content": prompt}],
            "system": self.system_message,
        }

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type(
            (
                anthropic.APIError,
                anthropic.APIConnectionError,
                anthropic.RateLimitError,
            )
        ),
    )
    async def _make_request(
        self,
        index: str | None,
        prompt: str | None,
        tokens: int | None,
        repo_files: list[tuple[str, str]] | None,
    ) -> Any:
        """Processes Anthropic API responses and returns generated text."""
        try:
            prompt = await token_handler(self.config, index, prompt, tokens)

            parameters = await self._build_payload(prompt, tokens)

            async with self.rate_limit_semaphore:
                response = await self.client.messages.create(**parameters)
                data = response.content[0].text
                self._logger.info(
                    f"Response from Anthropic for '{index}': {data}"
                )
                return index, data

        except (
            anthropic.APIError,
            anthropic.APIConnectionError,
            anthropic.RateLimitError,
        ) as e:
            self._logger.error(
                f"Error processing request for '{index}': {e!r}"
            )
            raise  # Re-raise for retry decorator

        except Exception as e:
            self._logger.error(f"Unexpected error for '{index}': {e!r}")
            return index, self.placeholder
