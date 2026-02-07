from git import Repo
from pathlib import Path
import os

REPOS_DIR = Path.home() / '.repochat' / 'repos'

def clone_repository(repo_url: str) -> tuple[str, str, bool]:
    """
    Clone or update a repository.
    Returns: (repo_name, local_path, is_new)
    """
    REPOS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Extract repo name from URL
    # https://github.com/user/repo.git -> user-repo
    repo_name = repo_url.replace('https://github.com/', '') \
                        .replace('.git', '') \
                        .replace('/', '-')
    
    local_path = REPOS_DIR / repo_name
    
    if local_path.exists():
        # Repository exists, pull latest
        repo = Repo(local_path)
        origin = repo.remotes.origin
        origin.pull()
        return repo_name, str(local_path), False
    else:
        # Clone new repository (shallow clone for speed)
        Repo.clone_from(repo_url, local_path, depth=1)
        return repo_name, str(local_path), True
