"""Entry point for triggering the README generation process without CLI arguments."""

import os
from readmeai.main import readme_agent
from readmeai.config.settings import ConfigLoader, GitSettings

urls = ["https://github.com/eli64s/readme-ai"]

def run():
    """Triggers the README generation using predefined settings."""
    # Initialize configuration
    config = ConfigLoader()

    # Set repository settings (modify as needed)
    for url in urls:
        config.config.git = GitSettings(repository=url)
        output_file = f"{url.split('/')[-1]}.md"
        readme_agent(config=config, output_file=output_file)

if __name__ == "__main__":
    run() 