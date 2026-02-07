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
    *   You must have a valid GitHub Copilot subscription.
    *   **Crucial Step**: Install the Copilot extension for CLI:
        ```bash
        gh extension install github/gh-copilot
        ```

## Installation

Follow these steps to set up RepoChat:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/mahupreti/repochat.git
    cd repochat
    ```

2.  **Create and activate a virtual environment** (Recommended):
    ```bash
    # Create venv
    python3 -m venv repochat-venv

    # Activate (Linux/macOS)
    source repochat-venv/bin/activate

    # Activate (Windows)
    # repochat-venv\Scripts\activate
    ```

3.  **Install the package**:
    ```bash
    pip install -e .
    ```

4.  **Verify Installation**:
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
