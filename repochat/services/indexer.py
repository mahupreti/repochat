from repochat.db.database import Database
from repochat.utils.file_parser import get_code_files, parse_file, extract_code_elements

def index_repository(repo_name: str, repo_url: str, local_path: str) -> int:
    """Index all files in a repository."""
    db = Database()
    
    # Save repository
    repo_id = db.save_repository(repo_name, repo_url, local_path)
    
    # Get all code files
    code_files = get_code_files(local_path)
    
    indexed_count = 0
    
    for file_path in code_files:
        # Parse file
        file_data = parse_file(file_path, local_path)
        if not file_data:
            continue
        
        # Skip very large files (> 1MB)
        if file_data['size'] > 1_000_000:
            continue
        
        # Save file to database
        file_id = db.save_file(
            repo_id,
            file_data['path'],
            file_data['content'],
            file_data['extension'],
            file_data['size']
        )
        
        # Extract and save code elements
        elements = extract_code_elements(file_data['content'], file_data['extension'])
        for element in elements:
            db.save_code_element(
                file_id,
                element['type'],
                element['name'],
                element['line']
            )
        
        indexed_count += 1
    
    return indexed_count
