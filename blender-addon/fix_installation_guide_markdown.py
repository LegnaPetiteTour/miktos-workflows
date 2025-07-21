import re

def fix_markdown_formatting(file_path):
    """Fix markdown formatting issues in INSTALLATION_GUIDE.md"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix MD036 - Replace emphasis with proper headings
    # **Option A: Manual Installation** -> ### Option A: Manual Installation
    content = re.sub(r'^\*\*(Option [AB]: [^*]+)\*\*$', r'### \1', content, flags=re.MULTILINE)
    
    # Fix MD022 - Add blank lines around headings
    # Add blank line before headings (except at start of file)
    content = re.sub(r'(?<!^)(?<!\n\n)(^#{1,6} .+)$', r'\n\1', content, flags=re.MULTILINE)
    
    # Add blank line after headings
    content = re.sub(r'^(#{1,6} .+)$\n(?!\n)', r'\1\n', content, flags=re.MULTILINE)
    
    # Fix MD031 & MD040 - Add blank lines around code blocks and specify language
    # Fix code blocks without language specification
    content = re.sub(r'^```$', '```bash', content, flags=re.MULTILINE)
    
    # Add blank lines before code blocks
    content = re.sub(r'(?<!\n\n)(^```[a-z]*$)', r'\n\1', content, flags=re.MULTILINE)
    
    # Add blank lines after code blocks
    content = re.sub(r'^```$\n(?!\n)', r'```\n', content, flags=re.MULTILINE)
    
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
    fix_markdown_formatting("INSTALLATION_GUIDE.md")
