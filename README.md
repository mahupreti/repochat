# RepoChat

RepoChat is a command-line tool that allows you to chat with any GitHub repository using AI. It indexes the repository codebase and uses GitHub Copilot to answer your questions with full context of the project.

## Features

-   **Chat with any Repo**: Index and query any public GitHub repository.
-   **Context-Aware AI**: Uses GitHub Copilot to understand the codebase structure and logic.
-   **Conversational Interface**: Natural language interaction for questions like "How do I run this?" or "Explain the authentication flow."
-   **Local Indexing**: Repository data is indexed locally for fast access.

## Prerequisites

Before running RepoChat, ensure you have the following installed on your machine:

1.  **Python 3.10** or higher
2.  **Git**
3.  **GitHub CLI (`gh`)**: [Install instructions](https://cli.github.com/)
    *   You must be logged in: `gh auth login`
    *   **Copilot Access**: You need access to GitHub Copilot CLI. (Note: You don't necessarily need a paid "Pro" subscription; the **free GitHub Copilot CLI** access via trials, student packs, or organization seats works perfectly!)
    *   **Install the extension**:
        ```bash
        gh extension install github/gh-copilot
        ```

## Installation

### 🛠️ The Professional Way: `pipx` (Cleanest)
If you want to keep your system clean and avoid dependency conflicts, use `pipx`. This is the standard way to install CLI tools like this:

```bash
# Install pipx if you don't have it
# brew install pipx (macOS) or sudo apt install pipx (Linux)

pipx install git+https://github.com/mahupreti/repochat.git
```
*This installs RepoChat in its own isolated environment and puts the `repochat` command in your PATH automatically.*

---

### 🚀 One-Command Quick Start
For a quick install using standard `pip`:

```bash
pip install git+https://github.com/mahupreti/repochat.git
```
*This handles everything and makes the `repochat` command available immediately!*

---

### Alternative: Standard Installation (For Developers)
If you want to modify the code, follow these steps:

1.  **Clone and Enter**:
    ```bash
    git clone https://github.com/mahupreti/repochat.git
    cd repochat
    ```

2.  **Install the tool**:
    You can install it directly so the `repochat` command is available everywhere in your terminal:
    ```bash
    pip install .
    ```
    *(Note: Using a virtual environment is still recommended to keep your system clean, but `pip install .` will register the `repochat` command for you.)*

3.  **Verify**:
    ```bash
    repochat --help
    ```

## Usage

### 1. Index a Repository
First, you need to index the repository you want to chat with. This downloads and processes the code.

```bash
repochat index https://github.com/username/repository-name
```
*Example:*
```bash
repochat index https://github.com/mahupreti/Kubernetes-study-material
```

### 2. Chat with the Repository
Once indexed, start a chat session using the repository name (the last part of the URL).

```bash
repochat chat repository-name
```
*Example:*
```bash
repochat chat Kubernetes-study-material
```

### Example Questions
- "How do I install the dependencies?"
- "Explain the main logic in `app.py`."
- "Where is the database configuration?"
- "Write a unit test for the `login` function."

## Troubleshooting

### "Copilot CLI not installed"
- **Error**: `gh: 'copilot' is not a known command` or similar.
- **Fix**: Run `gh extension install github/gh-copilot` and ensure you are logged in with `gh auth login`.

### "Repository not found"
- **Error**: The chat command complains that the repo doesn't exist.
- **Fix**: Make sure you ran `repochat index <url>` first and that the name matches the one in the URL.

### "No module named 'repochat'"
- **Error**: Command not found.
- **Fix**: Ensure your virtual environment is active and you ran `pip install -e .`.

### SQL/Database Errors
- **Fix**: Try re-indexing the repository if you suspect the index is corrupted: `repochat index <url>` (it will overwrite the existing index).
