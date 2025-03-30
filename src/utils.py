import yaml
import pandas as pd
from typing import Any, Dict, Union


def read_yaml(file_path: str) -> Any:
    return yaml.safe_load(open(file_path, 'r', encoding='utf-8'))


def train_val_test_split(
        x: pd.DataFrame,
        train_size: float,
        val_size: float,
        test_size: float,
) -> Dict[str, Union[pd.DataFrame, pd.Series]]:
    assert train_size + val_size + test_size == 1
    n = x.shape[0]
    train_end = int(train_size * n)
    val_end = int((train_size + val_size) * n)
    return {
        'train': x.iloc[: train_end],
        'val': x.iloc[train_end: val_end],
        'test': x.iloc[val_end:]
    }
