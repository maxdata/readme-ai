<p align="center">
    <img src="ImageOptions.BLUE" align="center" width="30%">
</p>
<p align="center"><h1 align="center">README-AI</h1></p>
<p align="center">
	<em>Automate Documentation, Simplify Development.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/eli64s/readme-ai?style=BadgeStyleOptions.DEFAULT&logo=opensourceinitiative&logoColor=white&color=blue" alt="license">
	<img src="https://img.shields.io/github/last-commit/eli64s/readme-ai?style=BadgeStyleOptions.DEFAULT&logo=git&logoColor=white&color=blue" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eli64s/readme-ai?style=BadgeStyleOptions.DEFAULT&color=blue" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eli64s/readme-ai?style=BadgeStyleOptions.DEFAULT&color=blue" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

readme-ai revolutionizes how developers create and manage project documentation by automating the process, ensuring consistency and clarity. Key features include seamless Docker integration for easy deployment, robust task management with a Makefile, and enhanced code quality and testing tools. Ideal for developers seeking efficient, high-quality documentation workflows.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Built with a focus on containerization using `<Docker>` to ensure consistent environments.</li><li>Leverages `<Python 3.11-slim-buster>` as the base image for lightweight execution.</li><li>Utilizes `<Pydantic>` for data validation and settings management.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Employs `<Ruff>` for linting to maintain clean code.</li><li>Includes a `<Makefile>` to standardize development workflows and automate tasks like testing and building.</li><li>Uses `<Pre-commit>` hooks to enforce quality checks before code submission.</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive docs built with `<MkDocs>`.</li><li>Documentation versioning supported by `<mkdocs-git-revision-date-localized-plugin>`.</li><li>Detailed setup and usage instructions provided for `<Poetry>`, `<Pip>`, `<Conda>`, and `<Docker>`.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integration with `<GitHub Actions>` for CI/CD pipelines.</li><li>Supports `<OpenAI>`, `<Anthropic>`, and `<Google Generative AI>` for AI-related functionalities.</li><li>Utilizes `<Aiohttp>` for asynchronous HTTP requests.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Structured with modular configuration files like `tooling.toml` and `config.toml`.</li><li>Extensible through plugins and configuration options.</li><li>Utilizes `<Click>` for building CLI applications.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Automated tests executed with `<Pytest>`.</li><li>Test coverage reports generated using `<pytest-cov>`.</li><li>Supports randomized testing with `<pytest-randomly>` to ensure robustness.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Uses `<Tenacity>` for handling retries in network requests, enhancing reliability.</li><li>Optimized for speed with dependencies like `<tiktoken>` for tokenization.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Non-root user setup in `<Dockerfile>` to enhance security.</li><li>Dependencies managed using `<Poetry>` for locking versions.</li><li>Secure configuration with `<Pydantic>` settings management.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Managed via `<Poetry>` with `poetry.lock` for dependency resolution.</li><li>Support for `<Conda>` and `<Pip>` as alternative package managers.</li><li>Containerized with `<Docker>` to encapsulate dependencies.</li></ul> |
| 🚀 | **Scalability**   | <ul><li>Designed to scale with container orchestration using `<Docker>`.</li><li>Efficient resource utilization through lightweight base images.</li><li>Supports distributed testing with `<pytest-xdist>` for parallel execution.</li></ul> |
```

---

##  Project Structure

```sh
└── readme-ai/
    ├── .github
    │   ├── release-drafter.yml
    │   └── workflows
    ├── CHANGELOG.md
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── Dockerfile
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── docs
    │   ├── docs
    │   ├── mkdocs.yml
    │   └── overrides
    ├── examples
    │   ├── anthropic
    │   ├── gemini
    │   ├── headers
    │   ├── local
    │   ├── logos
    │   ├── offline-mode
    │   ├── ollama
    │   ├── openai
    │   ├── readme-ai.md
    │   ├── readme-docker-go.md
    │   ├── readme-fastapi-redis.md
    │   ├── readme-javascript.md
    │   ├── readme-kotlin.md
    │   ├── readme-litellm.md
    │   ├── readme-mlops.md
    │   ├── readme-ollama.md
    │   ├── readme-postgres.md
    │   ├── readme-python-v0.5.87.md
    │   ├── readme-python.md
    │   ├── readme-readmeai.md
    │   ├── readme-rust-c.md
    │   ├── readme-sqlmesh.md
    │   ├── readme-typescript.md
    │   └── toc
    ├── noxfile.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── readmeai
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── cli
    │   ├── config
    │   ├── errors.py
    │   ├── generators
    │   ├── ingestion
    │   ├── logger.py
    │   ├── models
    │   ├── parsers
    │   ├── postprocessor
    │   ├── preprocessor
    │   ├── readers
    │   ├── templates
    │   └── utils
    ├── scripts
    │   ├── clean.sh
    │   ├── docker.sh
    │   ├── pypi.sh
    │   ├── run_batch.sh
    │   └── run_batch_random.sh
    ├── setup
    │   ├── environment.yaml
    │   ├── requirements.txt
    │   └── setup.sh
    └── tests
        ├── __init__.py
        ├── cli
        ├── config
        ├── conftest.py
        ├── generators
        ├── ingestion
        ├── models
        ├── parsers
        ├── postprocessor
        ├── preprocessor
        ├── readers
        ├── templates
        ├── test_errors.py
        ├── test_logger.py
        ├── test_main.py
        └── utils
```


###  Project Index
<details open>
	<summary><b><code>README-AI/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/Dockerfile'>Dockerfile</a></b></td>
				<td>- Facilitate the deployment of the application by setting up a lightweight Python environment using Docker<br>- It specifies the necessary system dependencies and Python packages, ensuring a consistent runtime for executing the `readmeai` tool<br>- By creating a non-root user, it enhances security and prevents permission issues<br>- The Dockerfile is integral to streamlining the application’s containerization, fostering ease of distribution and execution across diverse environments.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/eli64s/readme-ai/blob/master/Makefile'>Makefile</a></b></td>
				<td>- Manage project tasks efficiently by defining common development and deployment commands, such as cleaning build artifacts, creating conda recipes, building Docker images, and handling dependencies with Poetry<br>- Facilitate code quality through formatting and linting with Ruff, while supporting testing with pytest and Nox<br>- Enhance documentation processes using MkDocs and streamline project navigation with a help menu.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with readme-ai, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Poetry, Pip, Conda
- **Container Runtime:** Docker


###  Installation

Install readme-ai using one of the following methods:

**Build from source:**

1. Clone the readme-ai repository:
```sh
❯ git clone https://github.com/eli64s/readme-ai
```

2. Navigate to the project directory:
```sh
❯ cd readme-ai
```

3. Install the project dependencies:


**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry install
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r setup/requirements.txt
```


**Using `conda`** &nbsp; [<img align="center" src="https://img.shields.io/badge/conda-342B029.svg?style={badge_style}&logo=anaconda&logoColor=white" />](https://docs.conda.io/)

```sh
❯ conda env create -f setup/environment.yaml
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t eli64s/readme-ai .
```




###  Usage
Run readme-ai using the following command:
**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry run python {entrypoint}
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `conda`** &nbsp; [<img align="center" src="https://img.shields.io/badge/conda-342B029.svg?style={badge_style}&logo=anaconda&logoColor=white" />](https://docs.conda.io/)

```sh
❯ conda activate {venv}
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


###  Testing
Run the test suite using the following command:
**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry run pytest
```


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


**Using `conda`** &nbsp; [<img align="center" src="https://img.shields.io/badge/conda-342B029.svg?style={badge_style}&logo=anaconda&logoColor=white" />](https://docs.conda.io/)

```sh
❯ conda activate {venv}
❯ pytest
```


---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/eli64s/readme-ai/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/eli64s/readme-ai/issues)**: Submit bugs found or log feature requests for the `readme-ai` project.
- **💡 [Submit Pull Requests](https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/eli64s/readme-ai
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/eli64s/readme-ai/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=eli64s/readme-ai">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
