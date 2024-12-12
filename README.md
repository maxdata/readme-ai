## 🔗 Quick Links

1. [Overview](#-overview)
2. [Demo](#-demo)
3. [Features](#️-features)
4. [Getting Started](#-getting-started)
5. [Configuration](#-configuration)
6. [Examples](#-examples)
7. [Contributing](#-contributing)

> [!IMPORTANT]
> ✨ Visit the [Official Documentation][mkdocs] for detailed guides and tutorials.

---

## 🔮 Overview

README-AI is a developer tool that automatically generates README markdown files using a robust repository processing engine and advanced language models. Simply provide a URL or path to your codebase, and a well-structured and detailed README will be generated.

**Why README-AI?**

This tool is designed to streamline the documentation process for developers, saving time and effort while ensuring high-quality README files. Key benefits include:

- **AI-Powered:** Leverage language models for intelligent content generation.
- **Consistency:** Ensure clean, standardized documentation across projects.
- **Customization:** Tailor the output to fit your project's requirements.
- **Language Agnostic:** Works with most programming languages/frameworks.
- **Save Time:** Generate comprehensive READMEs in less than a minute.

---

## 👾 Demo

**Running from the command line:**

[readmeai-cli-demo](https://github.com/eli64s/artifacts/assets/43382407/55b8d1b9-06a7-4b1f-b6a7-aaeccdb27679)

**Running directly in your browser:**

[readmeai-streamlit-demo](https://github.com/eli64s/artifacts/assets/43382407/3eb39fcf-c1df-49c6-bb5c-63e141857ae3)

---

## ☄️ Features

- **🚀 Automated Documentation:** Generate comprehensive README files automatically from your codebase.
- **🎨 Customizable Output:** Tailor the styling, formatting, badges, header designs, and more preferences.
- **🤖 Flexible Backends:** Seamlessly integrate with `OpenAI`, `Ollama`, `Anthropic`, `Google Gemini`.
- **🌐 Language Agnostic:** Compatible with a wide range of programming languages and project types.
- **📑 Offline Mode:** Create boilerplate README files offline, without any external API calls.
- **📝 Best Practices:** Ensures clean, professional documentation, adhering to markdown best practices.

<details closed>
  <summary><strong>🔰 Contributing Guidelines</strong></summary>
  <br>
  <table>
    <tr>
      <td><b>Contributing Guide</b><br>
        <p>◎ Dropdown section that outlines general process for contributing to your project.</p>
        <p>◎ Provides links to your contributing guidelines, issues page, and more resources.</p>
        <p>◎ Graph of contributors is also included.</p>
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/contributing/contributing-guidelines.png" alt="contributing-guidelines-section" width="700">
      </td>
    </tr>
    <tr>
      <td><b>Additional Sections</b><br>
        <p>◎ <code>Roadmap</code>, <code>Contributing Guidelines</code>, <code>License</code>, and <code>Acknowledgements</code> are included by default.
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/contributing/footer.png" alt="footer-readme-section" width="700"></td>
    </tr>
  </table>
</details>

---

## 🛸 Getting Started

### System Requirements

- **Python Version**: `3.9` or higher
- **Package Management/Conainter Runtime**: Choose one of the following:
    - [`pip`][pip]: Python's default package installer, recommended for most users.
    - [`pipx`][pipx]: Install and run readme-ai in an isolated environment.
    - [`uv`][uv]: Fastest way to install readme-ai with a single command.
    - [`docker`][docker]: Run readme-ai in a containerized environment.

## Supported Repository Sources

The `readmeai` CLI can retrieve source code from the following Git hosting services or your local file system:

| Platform | Description | Resource |
| :------- | :---------- | :--- |
| File System | Access repositories on your machine | [Learn more][file-system] |
| GitHub | World's largest code hosting platform | [GitHub.com][github] |
| GitLab | Complete DevOps platform | [GitLab.com][gitlab] |
| Bitbucket | Atlassian's Git solution | [Bitbucket.org][bitbucket] |

## Supported LLM API Providers

To unlock the full potential of `readmeai`, you'll need an account and API key from one of the providers below:

| Provider | Description | Resource |
|----------|-------------|-------|
| OpenAI | Recommended for general use | [OpenAI Developer quickstart][openai] |
| Anthropic | Advanced language models | [Anthropic Developer docs][anthropic] |
| Google Gemini | Google's multimodal AI model | [Gemini API quickstart][gemini] |
| Ollama | Free and open-source (No API key required) | [Ollama GitHub repository][ollama] |
| Offline Mode | Run `readmeai` without a LLM API | [Example offline mode README][offline-mode] |

## ⚙️ Installation

Choose your preferred installation method:

<!--
#### Using `pip`
[![pip](https://img.shields.io/badge/PyPI-3775A9.svg?style=flat&logo=PyPI&logoColor=white)](https://pypi.org/project/readmeai/)
-->

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/python.svg">&emsp13;Pip

Recommended method for most users:

```sh
❯ pip install readmeai
```

<!--
#### Using `pipx`
[![pipx](https://img.shields.io/badge/pipx-2CFFAA.svg?style=flat&logo=pipx&logoColor=black)](https://pipxproject.github.io/pipx/installation/)
-->

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/pipx.svg">&emsp13;Pipx

Use [pipx](https://pipx.pypa.io/stable/installation/) to use `readmeai` in an isolated environment, ensuring no dependency conflicts with other Python projects:

```sh
❯ pipx install readmeai
```

<!--
> [!TIP]
> <sub>Using [pipx](https://pipx.pypa.io/stable/installation/) allows you to install and run Python command-line applications in isolated environments, which helps prevent dependency conflicts with other Python projects.</sub>
-->

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/astral.svg">&emsp13;Uv

Use [uv](https://github.com/astral-sh/uv) for the fastest way to install `readmeai` with a single command:

```sh
❯ uv tool install readmeai
```

<!--
#### Using `docker`
[![docker](https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white)](https://hub.docker.com/r/zeroxeli/readme-ai)
 -->

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/3052baaca03db99d00808acfec43a44e81ecbf7f/docs/docs/assets/svg/docker.svg">&emsp13;Docker

To run `readmeai` in a containerized environment, pull latest Docker image from Docker Hub:

```sh
❯ docker pull zeroxeli/readme-ai:latest
```

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/git.svg">&emsp13;From source

<details><summary>Click to expand instructions</summary>

1. **Clone the repository:**

   ```sh
   ❯ git clone https://github.com/eli64s/readme-ai
   ```

2. **Navigate to the `readme-ai` directory:**

   ```sh
   ❯ cd readme-ai
   ```

3. **Install dependencies:**

   ```sh
   ❯ pip install -r setup/requirements.txt
   ```

Alternatively, the project can be setup using the bash script below:

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/gnubash.svg">&emsp13;Bash

1. **Run the setup script:**

	```sh
	❯ bash setup/setup.sh
	```

Or, use `poetry` to build the project:

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/poetry.svg">&emsp13;Poetry

1. **Install dependencies using Poetry:**

	```sh
	❯ poetry install
	```

</details><br>

> [!IMPORTANT]
> To use the **Anthropic** and **Google Gemini** clients, extra dependencies are required. Install the package with the following extras:
>
> - **Anthropic:**
>   ```sh
>   ❯ pip install "readmeai[anthropic]"
>   ```
> - **Google Gemini:**
>   ```sh
>   ❯ pip install "readmeai[google-generativeai]"
>   ```
>
> - **Install Multiple Clients:**
>   ```sh
>   ❯ pip install "readmeai[anthropic,google-generativeai]"
>   ```

## 🤖 Running the CLI

**1. Set Up Environment Variables**

With OpenAI:

```sh
❯ export OPENAI_API_KEY=<your_api_key>

# Or for Windows users:

❯ set OPENAI_API_KEY=<your_api_key>
```

<details closed><summary>Additional Providers (Ollama, Anthropic, Google Gemini)</summary><br>

<details closed><summary>Ollama</summary><br>

Refer to the [Ollama documentation](https://github.com/ollama/ollama) for more information on setting up the Ollama API. Here is a basic example:

1. Pull your model of choice from the Ollama repository:

	```sh
	❯ ollama pull mistral:latest
	```

2. Start the Ollama server and set the `OLLAMA_HOST` environment variable:

	```sh
	❯ export OLLAMA_HOST=127.0.0.1 && ollama serve
	```

</details>

<details closed><summary>Anthropic</summary>

1. Export your Anthropic API key:

	```sh
	❯ export ANTHROPIC_API_KEY=<your_api_key>
	```

</details>

<details closed><summary>Google Gemini</summary>

1. Export your Google Gemini API key:

	```sh
	❯ export GOOGLE_API_KEY=<your_api_key
	```

</details>

</details>

**2. Generate a README**

Run the following command, replacing the repository URL with your own:

```sh
❯ readmeai --repository https://github.com/eli64s/readme-ai --api openai
```

> [!IMPORTANT]
> By default, the `gpt-3.5-turbo` model is used. Higher costs may be incurred when more advanced models.
>

Run with `Ollama` and set `llama3` as the model:

```sh
❯ readmeai --api ollama --model llama3 --repository https://github.com/eli64s/readme-ai
```

Run with `Anthropic`:

```sh
❯ readmeai --api anthropic -m claude-3-5-sonnet-20240620 -r https://github.com/eli64s/readme-ai
```
Run with `Google Gemini`:

```sh
❯ readmeai --api gemini -m gemini-1.5-flash -r https://github.com/eli64s/readme-ai
```

Use a `local` directory path:

```sh
readmeai --repository /path/to/your/project
```

Add more customization options:

```sh
❯ readmeai --repository https://github.com/eli64s/readme-ai \
           --output readmeai.md \
           --api openai \
           --model gpt-4 \
           --badge-color A931EC \
           --badge-style flat-square \
           --header-style compact \
           --toc-style fold \
           --temperature 0.9 \
           --tree-depth 2
           --image LLM \
           --emojis
```

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/3052baaca03db99d00808acfec43a44e81ecbf7f/docs/docs/assets/svg/docker.svg">&emsp13;Docker

Run the Docker container with the OpenAI client:

```sh
❯ docker run -it --rm \
    -e OPENAI_API_KEY=$OPENAI_API_KEY \
    -v "$(pwd)":/app zeroxeli/readme-ai:latest \
    --repository https://github.com/eli64s/readme-ai \
    --api openai
```

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/git.svg">&emsp13;From source

<details closed><summary><i>Click to expand instructions</i></summary>

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/gnubash.svg">&emsp13;Bash

If you installed the project from source with the bash script, run the following command:

1. **Activate the virtual environment:**

   ```sh
   ❯ conda activate readmeai
   ```

2. **Run the CLI:**

   ```sh
   ❯ python3 -m readmeai.cli.main -r https://github.com/eli64s/readme-ai
	```

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/poetry.svg">&emsp13;Poetry

1. **Activate the virtual environment:**

   ```sh
   ❯ poetry shell
   ```

2. **Run the CLI:**

   ```sh
   ❯ poetry run python3 -m readmeai.cli.main -r https://github.com/eli64s/readme-ai
   ```

</details>

### <img width="2%" src="https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/streamlit.svg">&emsp13;Streamlit

Try readme-ai directly in your browser, no installation required. See the <a href="https://github.com/eli64s/readme-ai-streamlit">readme-ai-streamlit</a> repository for more details.

[<img align="center" src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" width="20%">](https://readme-ai.streamlit.app/)

---

## 🧪 Testing

<!--
#### Using `pytest`
[![pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white)](https://docs.pytest.org/en/7.1.x/contents.html)
-->

The [pytest](https://docs.pytest.org/en/7.2.x/contents.html) and [nox](https://nox.thea.codes/en/stable/) frameworks are used for development and testing.

Install the dependencies using Poetry:

```sh
❯ poetry install --with dev,test
```

Run the unit test suite using Pytest:

```sh
❯ make test
```

Run the test suite against Python 3.9, 3.10, 3.11, and 3.12 using Nox:

```sh
❯ make test-nox
```

> [!TIP]
> <sub>Nox is an automation tool that automates testing in multiple Python environments. It is used to ensure compatibility across different Python versions.</sub>

---

## 🔡 Configuration

Customize your README generation using these CLI options:

| Option            | Description                                   | Default           |
|-------------------|-----------------------------------------------|-------------------|
| `--align`         | Text alignment in header                      | `center`          |
| `--api`           | LLM API service provider                      | `offline`         |
| `--badge-color`   | Badge color name or hex code                  | `0080ff`          |
| `--badge-style`   | Badge icon style type                         | `flat`            |
| `--header-style`  | Header template style                         | `classic`         |
| `--toc-style` 	| Table of contents style 				        | `bullet` 			|
| `--emojis`        | Adds emojis to the README header sections     | `False`           |
| `--image`         | Project logo image                            | `blue`            |
| `--model`         | Specific LLM model to use                     | `gpt-3.5-turbo`   |
| `--output`        | Output filename                               | `readme-ai.md`    |
| `--repository`    | Repository URL or local directory path        | `None`            |
| `--temperature`   | Creativity level for content generation       | `0.1`             |
| `--tree-depth`    | Maximum depth of the directory tree structure | `2`               |

Run the following command to view all available options:

```sh
❯ readmeai --help
```

<sub>Visit the [Official Documentation][mkdocs] for more detailed information on configuration options, examples, and best practices.</sub>

---

## 🎨 Examples

View example README files generated by readme-ai across various Tech Stacks:

| Technology | Example Output | Repository | Description |
|------------|---------------|------------|-------------|
| Readme-ai | [readme-ai.md][default] | [readme-ai][readme-ai] | Readme-ai project |
| Apache Flink | [readme-pyflink.md][modern-header] | [pyflink-poc][pyflink] | Pyflink project |
| Streamlit | [readme-streamlit.md][svg-banner] | [readme-ai-streamlit][streamlit] | Streamlit web app |
| Vercel & NPM | [readme-vercel.md][dalle-logo] | [github-readme-quotes][vercel] | Vercel deployment |
| Go & Docker | [readme-docker-go.md][for-the-badge] | [docker-gs-ping][docker-golang] | Dockerized Go app |
| FastAPI & Redis | [readme-fastapi-redis.md][fastapi-redis] | [async-ml-inference][fastapi] | Async ML inference service |
| Java | [readme-java.md][compact-header] | [Minimal-Todo][java] | Minimalist todo Java app |
| PostgreSQL & DuckDB | [readme-postgres.md][classic-header] | [Buenavista][postgres] | Postgres proxy server |
| Kotlin | [readme-kotlin.md][readme-kotlin] | [android-client][kotlin] | Android client app |
| Offline Mode | [offline-mode.md][offline-mode] | [litellm][litellm] | LLM API service |

<sub>Find additional README examples in the [examples directory](https://github.com/eli64s/readme-ai/tree/main/examples).</sub>

---

## 🏎💨 Roadmap

* [ ] Release `readmeai 1.0.0` with enhanced documentation management features.
* [ ] Develop `Vscode Extension` to generate README files directly in the editor.
* [ ] Develop `GitHub Actions` to automate documentation updates.
* [ ] Add `badge packs` to provide additional badge styles and options.
  + [ ] Code coverage, CI/CD status, project version, and more.

---

## 🔰 Contributing

Contributions are welcome! Please read the [Contributing Guide][contributing] to get started.

- **💡 [Contributing Guide][contributing]**: Learn about our contribution process and coding standards.
- **🐛 [Report an Issue][issues]**: Found a bug? Let us know!
- **💬 [Start a Discussion][discussions]**: Have ideas or suggestions? We'd love to hear from you.

<br>
<p align="left">
  <a href="https://github.com{/eli64s/readme-ai/}graphs/contributors">
    <img src="https://contrib.rocks/image?repo=eli64s/readme-ai">
  </a>
</p>

---

## 🙌 Acknowledgments

* [Shields.io](https://shields.io/)
* [Simple Icons](https://simpleicons.org/)
* [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
* [Ileriayo/Markdown-Badges](https://github.com/Ileriayo/markdown-badges)
* [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons)

<div align="right">

[![][return]](#-quick-links)

</div>

---

#### 🎗 License

Copyright © 2023 [readme-ai][readme-ai]. <br />
Released under the [MIT License][license].

<!-- REFERENCE LINKS -->

<!-- README-AI PROJECT -->
[readme-ai]: https://github.com/eli64s/readme-ai
[return]: https://img.shields.io/badge/Back_to_top-5D4ED3?style=flat&logo=ReadMe&logoColor=white
[contributing]: https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md
[discussions]: https://github.com/eli64s/readme-ai/discussions
[issues]: https://github.com/eli64s/readme-ai/issues
[license]: https://github.com/eli64s/readme-ai/blob/main/LICENSE
[pulls]: https://github.com/eli64s/readme-ai/pulls "submit a pull request"
[mkdocs]: https://eli64s.github.io/readme-ai "Official Documentation"

<!-- INSTALLATION METHODS -->
[docker]: https://docs.docker.com/ "docker"
[pip]: https://pip.pypa.io/en/stable/ "pip"
[pipx]: https://pipx.pypa.io/stable/ "pipx"
[uv]: https://docs.astral.sh/uv/ "uv"

<!-- GIT HOSTS -->
[file-system]: https://en.wikipedia.org/wiki/File_system "Learn more"
[github]: https://github.com/ "GitHub.com"
[gitlab]: https://gitlab.com/ "GitLab.com"
[bitbucket]: https://bitbucket.org/ "Bitbucket.org"

<!-- LLM API PROVIDERS -->
[openai]: https://platform.openai.com/docs/quickstart/account-setup: "OpenAI Developer quickstart"
[anthropic]: https://docs.anthropic.com/en/home "Anthropic Developer docs"
[gemini]: https://ai.google.dev/tutorials/python_quickstart "Gemini API quickstart"
[ollama]: https://github.com/ollama/ollama "Ollama GitHub repository"

<!-- EXAMPLE READMEs -->
[default]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-ai.md "readme-python.md"
[ascii-header]: https://github.com/eli64s/readme-ai/blob/main/examples/headers/ascii.md "ascii.md"
[classic-header]: https://github.com/eli64s/readme-ai/blob/main/examples/headers/classic.md "readme-postgres.md"
[compact-header]: https://github.com/eli64s/readme-ai/blob/main/examples/headers/compact.md "readme-java.md"
[modern-header]: https://github.com/eli64s/readme-ai/blob/main/examples/headers/modern.md "readme-pyflink.md"
[svg-banner]: https://github.com/eli64s/readme-ai/blob/main/examples/banners/svg-banner.md "readme-streamlit.md"
[dalle-logo]: https://github.com/eli64s/readme-ai/blob/main/examples/logos/dalle.md "readme-vercel.md"
[readme-kotlin]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-kotlin.md "readme-kotlin.md"
[for-the-badge]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-docker-go.md "readme-docker-go.md"
[fastapi-redis]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-fastapi-redis.md "readme-fastapi-redis.md"
[offline-mode]: https://github.com/eli64s/readme-ai/blob/main/examples/offline-mode/readme-litellm.md "readme-litellm.md"

<!-- EXAMPLE REPOSITORIES -->
[readme-ai]: https://github.com/eli64s/readme-ai "readme-ai"
[pyflink]: https://github.com/eli64s/pyflink-poc "pyflink-poc"
[postgres]: https://github.com/jwills/buenavista "Buenavista"
[java]: https://github.com/avjinder/Minimal-Todo "minimal-todo"
[kotlin]: https://github.com/rumaan/file.io-Android-Client "android-client"
[docker-golang]: https://github.com/olliefr/docker-gs-ping "docker-gs-ping"
[vercel]: https://github.com/PiyushSuthar/github-readme-quotes "github-readme-quotes"
[streamlit]: https://github.com/eli64s/readme-ai-streamlit  "readme-ai-streamlit"
[fastapi]: https://github.com/FerrariDG/async-ml-inference "async-ml-inference"
[litellm]: https://github.com/BerriAI/litellm "offline-mode"
