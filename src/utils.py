import pandas as pd

def load_koi_data(url: str) -> pd.DataFrame:
    return pd.read_csv(url, comment='#')
