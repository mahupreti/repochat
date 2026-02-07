from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.markdown import Markdown
from repochat.db.database import Database
from repochat.services.searcher import search_relevant_code
from repochat.services.copilot import ask_copilot

console = Console()

def chat_command(repo_name: str):
    """Start an interactive chat session."""
    console.print(f"\n[bold blue]💬 RepoChat: {repo_name}[/bold blue]\n")
    console.print("[dim]Ask questions about the codebase. Type 'exit' to quit.[/dim]\n")
    
    # Verify repo exists
    db = Database()
    repo = db.get_repository(repo_name)
    
    if not repo:
        console.print(f"[red]Repository '{repo_name}' not found. Please index it first.[/red]\n")
        return
    
    # Chat loop
    while True:
        try:
            question = console.input("[cyan]>[/cyan] ")
            
            if question.lower() in ['exit', 'quit']:
                console.print("\n[dim]Goodbye! 👋[/dim]\n")
                break
            
            if not question.strip():
                continue

            # Handle greetings locally (speed optimization for standard greetings)
            normalized_q = question.lower().strip()
            greetings = {'hi', 'hello', 'hy', 'hey', 'greetings', 'hola'}
            
            if normalized_q in greetings:
                console.print(f"\n[green]Hello! 👋 I'm ready to help you explore the [bold]{repo_name}[/bold] codebase. Ask me anything![/green]\n")
                continue
            
            # Search and ask Copilot
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console
            ) as progress:
                task = progress.add_task("Searching codebase...", total=None)
                relevant_files = search_relevant_code(repo_name, question)
                
                progress.update(task, description="Asking Copilot...")
                answer = ask_copilot(question, {
                    'files': relevant_files,
                    'cwd': repo['path'],  # Pass repo path for context
                    'repo_name': repo_name
                })
                progress.stop()
            
            # Display answer
            console.print(Markdown(answer))
            console.print()
            
            # Show relevant files
            if relevant_files:
                console.print("[dim]📁 Relevant files:[/dim]")
                for file in relevant_files:
                    console.print(f"[dim]  - {file['file_path']}[/dim]")
                console.print()
        
        except KeyboardInterrupt:
            console.print("\n\n[dim]Goodbye! 👋[/dim]\n")
            break
        except Exception as e:
            console.print(f"\n[red]Error: {str(e)}[/red]\n")
