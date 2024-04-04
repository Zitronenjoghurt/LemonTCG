import os
from pathlib import Path

ROOT_DIR = str(Path(__file__).parent.parent.parent)

def construct_path(relative_path: str) -> str:
    path_parts = relative_path.split("/")
    absolute_path = os.path.join(ROOT_DIR, *path_parts)
    return absolute_path

def file_exists(file_path: str) -> bool:
    return os.path.isfile(file_path)

def file_to_string(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()