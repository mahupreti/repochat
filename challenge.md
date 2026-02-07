# RepoChat 🤖⚖️: Chat with any GitHub Repository

*This is a submission for the [GitHub Copilot CLI Challenge](https://dev.to/challenges/github-2026-01-21)*

---

## 🚀 What I Built
RepoChat is a command-line tool designed to bridge the gap between a massive codebase and the specialized knowledge of GitHub Copilot. While standard Copilot chat is excellent for the active file, RepoChat allows you to index **any public GitHub repository** and ask high-level questions across the entire project structure.

### Key Highlights:
-   **🔍 Deep Context**: It doesn't just look at one file; it understands your entire project's structure.
-   **🔄 Code Conversion**: Translate entire logic blocks between languages (e.g., Python to JavaScript) with full context.
-   **🐳 Docker Ready**: A pre-configured environment ensures it works out-of-the-box for everyone.
-   **🐧 Cross-Platform**: Optimized for Windows (PowerShell), macOS, and Linux.

---

## 🛠️ How it Works
1.  **Locally Indexing**: RepoChat parses the repository and stores a searchable map of code elements in a local SQLite database.
2.  **Contextual Retrieval**: When you ask a question, it finds the most relevant files.
3.  **Copilot Integration**: It feeds that context into the `gh copilot` CLI to generate precise, expert answers.

---

## 🎥 Demo
*(Video Placeholder - To be uploaded)*

### Quick Start with Docker:
```bash
docker build -t repochat .
docker run -it --rm repochat

# Inside the container:
gh auth login
gh copilot (press Esc after download)
repochat index https://github.com/mahupreti/repochat
repochat chat repochat
```

---

## 🧠 My Experience with GitHub Copilot CLI
Integrating the GitHub Copilot CLI was the backbone of this project. Instead of managing complex LLM integrations, I could leverage a tool that developers already trust.

-   **Seamless Integration**: Calling `gh copilot` via Python was straightforward and robust.
-   **Safe & Secure**: By relying on the user's existing `gh` authentication, RepoChat avoids handling sensitive credentials.
-   **Expertise**: The `gh copilot` model is specifically tuned for developers, making it the perfect "brain" for a RAG-based CLI.

Building RepoChat demonstrated how the GitHub Copilot CLI can be used as a modular "intelligence layer" for building custom developer productivity tools.

---

## 👤 Author
**Mahesh Upreti**
- Email: [maheshupretiofficial@gmail.com](mailto:maheshupretiofficial@gmail.com)
- GitHub: [@mahupreti](https://github.com/mahupreti)
- Repository: [mahupreti/repochat](https://github.com/mahupreti/repochat)
