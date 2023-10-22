"""Builds the README Markdown file for your codebase."""

__package__ = "readmeai"

import re
from pathlib import Path
from typing import List

from readmeai.config.settings import AppConfig, ConfigHelper
from readmeai.core import factory, logger
from readmeai.markdown import badges, quickstart, tables
from readmeai.services import version_control as vcs

logger = logger.Logger(__name__)


def build_readme_md(
    conf: AppConfig,
    helper: ConfigHelper,
    packages: list,
    summaries: tuple,
) -> None:
    """Constructs each section of the README Markdown file."""
    all_readme_sections = format_readme_md_contents(
        conf, helper, packages, summaries
    )
    output_file = "\n".join(all_readme_sections)
    output_path = Path(conf.paths.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    factory.FileHandler().write(output_path, output_file)
    logger.info(f"README file generated at: {output_path}")


def format_readme_md_contents(
    conf: AppConfig,
    helper: ConfigHelper,
    packages: list,
    summaries: tuple,
) -> List[str]:
    """Formats the README Markdown file contents for each section."""
    repo_name = conf.git.name
    repository = conf.git.repository
    name, _ = vcs.get_user_repository_name(repository)
    full_name = f"{name}/{repo_name}"

    if conf.cli.offline is False:
        md_tables = tables.create_markdown_tables(
            conf.md.default,
            summaries,
        )
        conf.md.tables = tables.create_tables(
            md_tables, conf.md.dropdown, repository, full_name
        )

    if "apps" not in conf.cli.badges:
        badge_icons = badges.get_shieldsio_icons(conf, packages, full_name)
    else:
        badge_icons = badges.get_app_icons(conf, packages)

    md_setup_guide = quickstart.create_instructions(conf, helper, summaries)

    markdown_sections = [
        conf.md.header,
        badge_icons,
        conf.md.toc.format(repo_name),
        conf.md.intro,
        conf.md.tree,
        conf.md.modules,
        conf.md.tables,
        conf.md.setup.format(repo_name, repository, *md_setup_guide),
        conf.md.ending.format(full_name),
    ]

    if conf.cli.emojis is False:
        markdown_sections = remove_emojis_from_headers(markdown_sections)

    return markdown_sections


def remove_emojis_from_headers(content_list: List[str]) -> List[str]:
    """Removes emojis from headers and ToC."""
    emoji_pattern = re.compile(
        pattern="["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # flags (iOS)
        "]+",
        flags=re.UNICODE,
    )

    # Iterate through content_list and replace emojis for lines starting with header symbols or in the ToC
    modified_content = []
    for section in content_list:
        lines = section.split("\n")
        for index, line in enumerate(lines):
            # Replace for lines that start with header symbols or are part of the ToC
            if line.startswith("#") or "Table of Contents" in section:
                lines[index] = emoji_pattern.sub("", line)
        modified_content.append("\n".join(lines))

    return modified_content