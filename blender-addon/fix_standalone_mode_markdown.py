import re

def fix_markdown_formatting(file_path):
    """Fix markdown formatting issues in STANDALONE_MODE_COMPLETE.md"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix MD026 - Remove trailing punctuation from headings
    content = re.sub(r'^(#{1,6} .+)[!:.]$', r'\1', content, flags=re.MULTILINE)
    
    # Fix MD032 - Add blank lines around lists
    # Add blank line before lists
    content = re.sub(r'(?<!\n\n)(^[-*+] .+)', r'\n\1', content, flags=re.MULTILINE)
    content = re.sub(r'(?<!\n\n)(^\d+\. .+)', r'\n\1', content, flags=re.MULTILINE)
    
    # Add blank line after lists (before non-list content)
    content = re.sub(r'^([-*+] .+)$\n(?!\n)(?![-*+] )(?!\d+\. )', r'\1\n', content, flags=re.MULTILINE)
    content = re.sub(r'^(\d+\. .+)$\n(?!\n)(?![-*+] )(?!\d+\. )', r'\1\n', content, flags=re.MULTILINE)
    
    # Clean up multiple consecutive blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Remove blank lines at the very beginning
    content = re.sub(r'^\n+', '', content)
    
    # Ensure file ends with exactly one newline
    content = content.rstrip('\n') + '\n'
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed markdown formatting issues in {file_path}")

if __name__ == "__main__":
    fix_markdown_formatting("/Users/atorrella/Desktop/Miktos/development/miktos-ai-bridge/STANDALONE_MODE_COMPLETE.md")
