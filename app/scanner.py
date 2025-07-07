# app/scanner.py

import ast
import os

def scan_python_file(file_path):
    issues = []
    with open(file_path, \"r\", encoding=\"utf-8\") as f:
        try:
            tree = ast.parse(f.read(), filename=file_path)
        except SyntaxError as e:
            issues.append({
                \"type\": \"SyntaxError\",
                \"message\": str(e),
                \"lineno\": e.lineno
            })
            return issues

    for node in ast.walk(tree):
        # Example: flag use of 'eval'
        if isinstance(node, ast.Call) and getattr(node.func, \"id\", \"\") == \"eval\":
            issues.append({
                \"type\": \"SecurityWarning\",
                \"message\": \"Use of eval() detected. This can be dangerous.\",
                \"lineno\": node.lineno
            })

    return issues

if __name__ == \"__main__\":
    result = scan_python_file(\"example.py\")
    print(\"BugSpotter Findings:\\n\", result)
