"""Entry point for triggering the README generation process without CLI arguments."""

import os
from readmeai.main import readme_agent
from readmeai.config.settings import ConfigLoader, GitSettings
from readmeai.logger import get_logger

def run():
    """Triggers the README generation using predefined settings."""
    # Initialize configuration
    config = ConfigLoader()
    logger = get_logger(__name__)

    # Set repository settings (modify as needed)
    config.config.git = GitSettings(repository="https://github.com/eli64s/readme-ai")

    # Update LLM settings (modify as needed)
    config.config.llm = config.config.llm.model_copy(
        update={
            "api": "OPENAI",
            "base_url": os.getenv("AZURE_OPENAI_ENDPOINT"),
            "context_window": 2048,
            "model": "gpt-4o",
            "temperature": 0.7,
            "top_p": 0.9,
        },
    )
    
    # Update Markdown settings (modify as needed)
    config.config.md = config.config.md.model_copy(
        update={
            "align": "left",
            "badge_color": "green",
            "badge_style": "flat",
            "emojis": True,
            "header_style": "bold",
            "image": "none",
            "toc_style": "plain",
            "tree_depth": 3,
        },
    )
    
    # Set API rate limit (modify as needed)
    config.config.api.rate_limit = 60

    # Log Pydantic and repository settings
    logger.info(f"Pydantic settings: {config.__dict__.keys()}")
    logger.info(f"Repository settings: {config.config.git}")
    logger.info(f"LLM API settings: {config.config.llm}")

    # Specify the output file
    output_file = "output/README.md"

    # Generate the README
    readme_agent(config=config, output_file=output_file)

if __name__ == "__main__":
    run() 