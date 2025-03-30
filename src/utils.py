import yaml
from typing import Any


def read_yaml(file_path: str) -> Any:
    return yaml.safe_load(open(file_path, 'r', encoding='utf-8'))
