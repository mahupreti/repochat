import sqlite3
import os
from pathlib import Path
from typing import Optional

DB_DIR = Path.home() / '.repochat'
DB_PATH = DB_DIR / 'index.db'

class Database:
    def __init__(self):
        self.db_path = DB_PATH
        self._ensure_dir()
        self._init_tables()
    
    def _ensure_dir(self):
        DB_DIR.mkdir(parents=True, exist_ok=True)
    
    def _init_tables(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS repositories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                url TEXT NOT NULL,
                path TEXT NOT NULL,
                indexed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                repo_id INTEGER NOT NULL,
                file_path TEXT NOT NULL,
                content TEXT,
                extension TEXT,
                size INTEGER,
                FOREIGN KEY (repo_id) REFERENCES repositories(id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS code_index (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id INTEGER NOT NULL,
                type TEXT NOT NULL,
                name TEXT NOT NULL,
                line_number INTEGER,
                FOREIGN KEY (file_id) REFERENCES files(id)
            )
        ''')
        
        # Create indexes
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_files_repo ON files(repo_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_code_name ON code_index(name)')
        
        conn.commit()
        conn.close()
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def save_repository(self, name: str, url: str, path: str) -> int:
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            'INSERT OR REPLACE INTO repositories (name, url, path) VALUES (?, ?, ?)',
            (name, url, path)
        )
        
        repo_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return repo_id
    
    def get_repository(self, name: str) -> Optional[dict]:
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM repositories WHERE name = ?', (name,))
        row = cursor.fetchone()
        conn.close()
        
        return dict(row) if row else None
    
    def save_file(self, repo_id: int, file_path: str, content: str, extension: str, size: int) -> int:
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            'INSERT INTO files (repo_id, file_path, content, extension, size) VALUES (?, ?, ?, ?, ?)',
            (repo_id, file_path, content, extension, size)
        )
        
        file_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return file_id
    
    def save_code_element(self, file_id: int, element_type: str, name: str, line_number: int):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            'INSERT INTO code_index (file_id, type, name, line_number) VALUES (?, ?, ?, ?)',
            (file_id, element_type, name, line_number)
        )
        
        conn.commit()
        conn.close()
    
    def search_files(self, repo_name: str, keywords: list) -> list:
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        

        if not keywords:
            return []
            
        # Build dynamic query
        placeholders = ' OR '.join(['f.file_path LIKE ?' for _ in keywords])
        query = f'''
            SELECT DISTINCT f.file_path, f.content, f.extension
            FROM files f
            JOIN repositories r ON f.repo_id = r.id
            WHERE r.name = ? AND ({placeholders})
            LIMIT 5
        '''
        
        params = [repo_name] + [f'%{k}%' for k in keywords]
        cursor.execute(query, params)
        
        results = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return results
    
    def search_code_elements(self, repo_name: str, keywords: list) -> list:
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        

        if not keywords:
            return []

        placeholders = ' OR '.join(['ci.name LIKE ?' for _ in keywords])
        query = f'''
            SELECT DISTINCT f.file_path, f.content, f.extension, ci.name, ci.type
            FROM code_index ci
            JOIN files f ON ci.file_id = f.id
            JOIN repositories r ON f.repo_id = r.id
            WHERE r.name = ? AND ({placeholders})
            LIMIT 5
        '''
        
        params = [repo_name] + [f'%{k}%' for k in keywords]
        cursor.execute(query, params)
        
        results = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return results
    
    def search_content(self, repo_name: str, keywords: list) -> list:
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        

        if not keywords:
            return []

        placeholders = ' OR '.join(['f.content LIKE ?' for _ in keywords])
        query = f'''
            SELECT f.file_path, f.content, f.extension
            FROM files f
            JOIN repositories r ON f.repo_id = r.id
            WHERE r.name = ? AND ({placeholders})
            LIMIT 10
        '''
        
        params = [repo_name] + [f'%{k}%' for k in keywords]
        cursor.execute(query, params)
        
        results = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return results
