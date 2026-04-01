import ast
import subprocess
import tempfile
import os

def check_syntax(code: str) -> list[str]:
    """Parses code using AST and returns syntax errors if any."""
    errors = []
    try:
        ast.parse(code)
    except SyntaxError as e:
        errors.append(f"SyntaxError at line {e.lineno}, offset {e.offset}: {e.msg}")
    except Exception as e:
        errors.append(f"Error parsing code: {str(e)}")
    return errors

def check_style(code: str) -> list[str]:
    """Runs flake8 on the given code and returns style errors."""
    if not code.strip():
        return []
        
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp:
        temp.write(code)
        temp_path = temp.name

    try:
        result = subprocess.run(
            ['flake8', temp_path],
            capture_output=True,
            text=True
        )
        
        output_lines = result.stdout.strip().split('\n')
        errors = []
        for line in output_lines:
            if line:
                parts = line.split(':', 3)
                if len(parts) >= 4:
                    errors.append(f"Line {parts[1]}, Col {parts[2]}: {parts[3].strip()}")
                else:
                    errors.append(line)
        return errors
    finally:
        os.remove(temp_path)

def analyze_code_basic(code: str) -> dict:
    """Performs basic AST syntax and Flake8 style checks."""
    syntax_errors = check_syntax(code)
    style_errors = check_style(code)
    return {
        "syntax_errors": syntax_errors,
        "style_errors": style_errors,
        "is_valid": len(syntax_errors) == 0
    }
