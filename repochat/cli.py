import click
from repochat.commands.index import index_command
from repochat.commands.chat import chat_command

@click.group()
@click.version_option(version='1.0.0')
def cli():
    """RepoChat - Chat with any GitHub repository using AI."""
    pass

@cli.command()
@click.argument('repo_url')
def index(repo_url):
    """Index a GitHub repository.
    
    Example: repochat index https://github.com/user/repo
    """
    index_command(repo_url)

@cli.command()
@click.argument('repo_name')
def chat(repo_name):
    """Start chatting with a repository.
    
    Example: repochat chat user-repo
    """
    chat_command(repo_name)

if __name__ == '__main__':
    cli()
