from pathlib import Path
import re
from typing import List, Dict

IGNORE_PATTERNS = [
    'node_modules', '.git', 'dist', 'build', '.next',
    'coverage', '__pycache__', '.pytest_cache', 'venv'
]

CODE_EXTENSIONS = {
    '.py', '.js', '.jsx', '.ts', '.tsx',
    '.java', '.go', '.rs', '.c', '.cpp',
    '.h', '.cs', '.rb', '.php', '.swift', '.kt'
}

def get_code_files(repo_path: str) -> List[Path]:
    """Get all code files from repository."""
    repo_path = Path(repo_path)
    code_files = []
    
    for file_path in repo_path.rglob('*'):
        # Skip if not a file
        if not file_path.is_file():
            continue
        
        # Skip ignored directories
        if any(ignored in file_path.parts for ignored in IGNORE_PATTERNS):
            continue
        
        # Check if code file
        if file_path.suffix in CODE_EXTENSIONS:
            code_files.append(file_path)
    
    return code_files

def parse_file(file_path: Path, repo_path: str) -> Dict:
    """Parse a single file."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except (UnicodeDecodeError, PermissionError):
        return None
    
    relative_path = str(file_path.relative_to(repo_path))
    
    return {
        'path': relative_path,
        'content': content,
        'extension': file_path.suffix,
        'size': len(content)
    }

def extract_code_elements(content: str, extension: str) -> List[Dict]:
    """Extract functions, classes, etc. from code."""
    elements = []
    
    # Function patterns for different languages
    function_patterns = {
        '.py': r'def\s+(\w+)\s*\(',
        '.js': r'function\s+(\w+)\s*\(',
        '.ts': r'function\s+(\w+)\s*\(',
        '.java': r'(?:public|private|protected)?\s*\w+\s+(\w+)\s*\(',
        '.go': r'func\s+(\w+)\s*\(',
    }
    
    # Extract functions
    pattern = function_patterns.get(extension)
    if pattern:
        for match in re.finditer(pattern, content):
            line_num = content[:match.start()].count('\n') + 1
            elements.append({
                'type': 'function',
                'name': match.group(1),
                'line': line_num
            })
    
    # Extract classes
    class_pattern = r'class\s+(\w+)'
    for match in re.finditer(class_pattern, content):
        line_num = content[:match.start()].count('\n') + 1
        elements.append({
            'type': 'class',
            'name': match.group(1),
            'line': line_num
        })
    
    return elements
