import pandas as pd
from src.utils import read_yaml


def preprocess(df: pd.DataFrame, cfg_path: str) -> pd.DataFrame:
    cfg = read_yaml(cfg_path)
    return (
        df.rename(columns=cfg['col_renamer'])
        .astype(cfg['col_types'])
        .pipe(lambda df: df[df['n_pedidos'] > 0])
        .groupby(['data', 'id_produto'])['n_pedidos'].sum()
        .unstack('id_produto').fillna(0).stack('id_produto')
        .sort_index().to_frame('n_pedidos')
    )
