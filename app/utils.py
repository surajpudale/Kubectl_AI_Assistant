# Utility functions for the app
import re

def strip_ansi(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

def format_table(text):
    lines = text.splitlines()
    if any(re.search(r'\s{2,}', line) for line in lines):
        return '<pre>' + '\n'.join(lines) + '</pre>'
    return text
