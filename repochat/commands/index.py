from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from repochat.services.git_service import clone_repository
from repochat.services.indexer import index_repository
from repochat.db.database import Database

console = Console()

def index_command(repo_url: str):
    """Index a GitHub repository."""
    console.print("\n[bold blue]🔍 RepoChat Indexer[/bold blue]\n")
    
    # Initialize database
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("Initializing database...", total=None)
        Database()
        progress.update(task, description="[green]✓[/green] Database ready")
        progress.stop()
    
    # Clone repository
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("Cloning repository...", total=None)
        
        try:
            repo_name, local_path, is_new = clone_repository(repo_url)
            status = "cloned" if is_new else "updated"
            progress.update(task, description=f"[green]✓[/green] Repository {status}")
            progress.stop()
            
            # Index repository
            task = progress.add_task("Indexing codebase...", total=None)
            file_count = index_repository(repo_name, repo_url, local_path)
            progress.update(task, description=f"[green]✓[/green] Indexed {file_count} files")
            
            console.print(f"\n[green]✅ Repository indexed successfully![/green]")
            console.print(f"\n[dim]Start chatting with:[/dim] [white]repochat chat {repo_name}[/white]\n")
            
        except Exception as e:
            progress.stop()
            console.print(f"\n[red]Error: {str(e)}[/red]\n")
            raise
