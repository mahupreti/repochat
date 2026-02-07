# RepoChat: Chat with any GitHub Repository

*This is a submission for the [GitHub Copilot CLI Challenge](https://dev.to/challenges/github-2026-01-21)*

## What I Built
RepoChat is a command-line tool designed to bridge the gap between a massive codebase and the specialized knowledge of GitHub Copilot. While standard Copilot chat is excellent for the active file, RepoChat allows you to index **any git repository** (local or public) and ask high-level questions across the entire project structure.

It works by:
1.  **Locally Indexing**: Parsing the repository and storing a searchable map of files and code elements in a local SQLite database.
2.  **Contextual Retrieval**: When a user asks a question, RepoChat finds the most relevant code snippets.
3.  **Copilot Integration**: It uses the `gh copilot` CLI to generate precise answers based on that retrieved context.

## Demo
You can get started with just two commands:

1.  **Index a Repository**:
    ```bash
    repochat index https://github.com/fastapi/fastapi
    ```
2.  **Start Chatting**:
    ```bash
    repochat chat fastapi
    ```

**Example Interaction:**
> **User**: "How does the dependency injection system work in this project?"
>
> **RepoChat**: *Retrieves `dependant.py` and `routing.py` -> Calls Copilot -> Summarizes the logic.*

## My Experience with GitHub Copilot CLI
Integrating the GitHub Copilot CLI was a game-changer for this project. Instead of managing complex API keys or building my own RAG backend from scratch, I could leverage an existing, trusted tool that users already have.

-   **Zero Friction**: Calling `gh copilot` via Python's `subprocess` was seamless.
-   **Security**: By relying on the user's existing `gh` authentication, RepoChat doesn't need to handle sensitive credentials.
-   **Context Awareness**: The `gh copilot` model is specifically tuned for code, making the answers significantly more accurate than a general-purpose LLM.

Building RepoChat showed me how the GitHub Copilot CLI can be used as a powerful modular component for other developers to build their own custom developer tools.
