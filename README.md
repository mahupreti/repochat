# RepoChat 🤖⚖️

RepoChat is a powerful command-line tool that allows you to chat with any GitHub repository using AI. It indexes the entire codebase locally and uses GitHub Copilot to provide expert answers with full project context.

---

## 🌟 Features

-   **🔍 Deep Context**: Indexes the whole repository, not just one file.
-   **🧠 Powered by Copilot**: Leverages the official GitHub Copilot CLI for high-quality code analysis.
-   **🐳 Docker Ready**: Get started in seconds with a pre-configured container.
-   **🐧 Cross-Platform**: Full support for Windows (PowerShell), macOS, and Linux.
-   **💾 Local Indexing**: Fast retrieval using a local SQLite database.

---

## 🛠️ Prerequisites

Ensure you have these installed on your machine:

1.  **Python 3.10+** (On Linux, install `python3-venv` if needed: `sudo apt install python3-venv`)
2.  **Git**
3.  **GitHub CLI (`gh`)**: [Download here](https://cli.github.com/)
    *   **Login**: `gh auth login`
    *   **Install Copilot Extension**: Run the following command:
        ```bash
        gh extension install github/gh-copilot
        ```
    *   **Finalize Copilot Setup**: After installation, run `gh copilot` once. It will download the CLI and may ask for additional configurations.
        > **Tip**: Once the CLI download is complete, you can simply press **`Esc`** to cancel any interactive prompts and start using RepoChat!

---

## 🚀 Installation

### Option 1 (BEST): Docker 🐳
For a perfect, isolated environment with everything pre-configured.

**1. Build and Run:**
```bash
docker build -t repochat-dev .
docker run -it --rm repochat-dev
```

**You get:** Python, Git, `gh` CLI, Copilot extension, and `repochat` ready to go! ✅

---

### Option 2: Local Setup (Manual) 💻

**1. Clone and Enter:**
```bash
git clone https://github.com/mahupreti/repochat.git
cd repochat
```

**2. Virtual Environment (Recommended):**
- **Linux/macOS**: `python3 -m venv venv && source venv/bin/activate`
- **Windows**: `python -m venv venv && .\venv\Scripts\Activate.ps1`

**3. Install RepoChat:**
```bash
pip install .
```

---

### Option 3: Quick Global Install ⚡
Install directly from GitHub without cloning:

```bash
pip install git+https://github.com/mahupreti/repochat.git
```
*(Linux users: If blocked by PEP 668, add `--break-system-packages`)*

---

## 📖 Usage

### 1. Index a Repository
Index any public repo to make it searchable. This processes the files and stores them locally.
```bash
repochat index https://github.com/username/repository-name
```

### 2. Chat with the Code
Start an interactive chat session using the repository name.
```bash
repochat chat repository-name
```

### 💡 Example Questions
- "Explain the project structure."
- "How does the indexing logic work?"
- "Where is the main entry point for the API?"
- "Write a unit test for the database service."

---

## 🔧 Troubleshooting

-   **"Copilot CLI not installed"**: Ensure you ran `gh extension install github/gh-copilot` and `gh auth login`.
-   **"Repository not found"**: Ensure you ran the `index` command first.
-   **Permission Errors**: On Linux, ensure you have the necessary `python3-venv` package or use the Docker method.

---

## 👤 Author

**Mahesh Upreti**
- Email: [maheshupretiofficial@gmail.com](mailto:maheshupretiofficial@gmail.com)
- GitHub: [@mahupreti](https://github.com/mahupreti)

*This project is a submission for the [GitHub Copilot CLI Challenge](https://dev.to/challenges/github-2026-01-21)*
