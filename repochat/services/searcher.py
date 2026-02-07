from repochat.db.database import Database
from typing import List, Dict
import re

def search_relevant_code(repo_name: str, query: str) -> List[Dict]:
    """Search for code relevant to the query."""
    db = Database()
    
    # Extract keywords
    keywords = extract_keywords(query)
    
    results = []
    
    # Search by file path
    file_results = db.search_files(repo_name, keywords)
    results.extend([{**r, 'relevance': 0.9} for r in file_results])
    
    # Search by code elements
    code_results = db.search_code_elements(repo_name, keywords)
    results.extend([{**r, 'relevance': 0.95} for r in code_results])
    
    # Search in content
    content_results = db.search_content(repo_name, keywords)
    results.extend([{**r, 'relevance': 0.7} for r in content_results])
    
    # Deduplicate and sort
    unique_results = deduplicate_by_path(results)
    
    return unique_results[:5]  # Top 5

def extract_keywords(query: str) -> List[str]:
    """Extract meaningful keywords from query."""
    stop_words = {'how', 'does', 'work', 'what', 'is', 'the', 'where', 'can', 'i', 'a', 'an'}
    
    # Remove punctuation and lowercase
    words = re.findall(r'\w+', query.lower())
    
    # Filter stop words and short words
    keywords = [w for w in words if len(w) >= 2 and w not in stop_words]
    
    return keywords

def deduplicate_by_path(results: List[Dict]) -> List[Dict]:
    """Remove duplicate file paths, keeping highest relevance."""
    seen = {}
    
    for result in results:
        path = result['file_path']
        if path not in seen or result['relevance'] > seen[path]['relevance']:
            seen[path] = result
    
    # Sort by relevance
    return sorted(seen.values(), key=lambda x: x['relevance'], reverse=True)
