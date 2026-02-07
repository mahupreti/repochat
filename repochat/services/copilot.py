import subprocess
from typing import List, Dict

def ask_copilot(question: str, context: Dict) -> str:
    """
    Ask GitHub Copilot CLI to answer a question with context.
    """
    prompt = build_prompt(question, context)
    
    cwd = context.get('cwd', '.')
    
    try:
        # Call GitHub Copilot CLI
        result = subprocess.run(
            ['gh', 'copilot', '-p', prompt],
            capture_output=True,
            text=True,
            check=True,
            cwd=cwd  # Run in the repo directory
        )
        
        return result.stdout.strip()
    
    except subprocess.CalledProcessError as e:
        raise Exception(f"Copilot CLI error: {e.stderr}")
    except FileNotFoundError:
        raise Exception("GitHub CLI not found. Please install: https://cli.github.com/")

def build_prompt(question: str, context: Dict) -> str:
    """Build a comprehensive prompt for Copilot."""
    prompt = "You are analyzing a code repository. Answer this question about the codebase:\n\n"
    prompt += f"QUESTION: {question}\n\n"
    
    files = context.get('files', [])
    if files:
        prompt += "RELEVANT CODE FILES:\n\n"
        
        for file in files:
            prompt += f"--- {file['file_path']} ---\n"
            
            # Truncate content if too long
            content = file['content']
            if len(content) > 3000:
                content = content[:3000] + '\n...[truncated]'
            
            prompt += content + "\n\n"
    
    prompt += "INSTRUCTIONS:\n"
    prompt += "1. You are an expert code assistant for this specific repository. Be helpful, concise, and professional.\n"
    prompt += "2. Answer ONLY based on the provided code files and the repository content.\n"
    prompt += "3. If the user input is a greeting, acknowledgment (e.g., 'okay', 'thanks', 'cool'), or casual chatter, reply conversationally and briefly. Do NOT summarize the repository unless explicitly asked.\n"
    prompt += "4. If the question is about what this repo does, look at the README or root files in the current directory.\n"
    prompt += "5. Format your response with beautiful Markdown, using bolding and lists where appropriate.\n"
    prompt += "6. Do NOT mention you are an AI or Copilot unless asked. Act like a lead developer explaining the code.\n"
    
    return prompt

def explain_code(code: str, file_path: str) -> str:
    """Use Copilot to explain a code snippet."""
    prompt = f"Explain this code from {file_path}:\n\n{code}"
    
    result = subprocess.run(
        ['gh', 'copilot', '-p', prompt],
        capture_output=True,
        text=True,
        check=True
    )
    
    return result.stdout.strip()
