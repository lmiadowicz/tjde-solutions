import pandas as pd


def load_urls_from_tsv(file_path):
    df = pd.read_csv(file_path, delimiter='\t', dtype=str)

    return df[['url']]