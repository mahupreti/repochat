# RepoChat

RepoChat is a command-line tool that allows you to chat with any GitHub repository using AI. It indexes the repository codebase and uses GitHub Copilot to answer your questions with full context of the project.

## Prerequisites

Before running RepoChat, ensure you have the following installed on your machine:

1.  **Python 3.10** or higher
2.  **Git**
3.  **GitHub CLI (`gh`)**: [Install instructions](https://cli.github.com/)
    *   You must be logged in: `gh auth login`
    *   You must have a valid GitHub Copilot subscription.

## Installation

Follow these steps to set up RepoChat on a new machine:

1.  **Clone the repository**:
    ```bash
    git clone <your-repo-url>
    cd repochat
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    # Create venv
    python3 -m venv repochat-venv

    # Activate (Linux/macOS)
    source repochat-venv/bin/activate

    # Activate (Windows)
    # repochat-venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -e .
    ```

4.  **Install GitHub Copilot Extension**:
    RepoChat relies on the GitHub Copilot CLI extension.
    ```bash
    gh extension install github/gh-copilot
    ```
    *If prompted, select "Yes" to install.*

## Usage

### 1. Index a Repository
First, you need to index the repository you want to chat with.
```bash
repochat index https://github.com/username/repository-name
```
*Example:*
```bash
repochat index https://github.com/mahupreti/Kubernetes-study-material
```

### 2. Chat with the Repository
Once indexed, start a chat session.
```bash
repochat chat repository-name
```
*Example:*
```bash
repochat chat Kubernetes-study-material
```

### Chat Features
- **Ask Setup Questions**: "How do I run this?"
- **Code Explanations**: "Explain verify_chat.py"
- **Context Aware**: It understands the specific codebase you are chatting with.
- **Conversational**: Handles greetings and casual chat naturally.

## Troubleshooting

- **"Copilot CLI not installed"**: Run `gh extension install github/gh-copilot`.
- **"Repository not found"**: Make sure you ran `repochat index` first.
- **SQL Errors**: Ensure you are using the latest version of the code which handles special characters correctly.
