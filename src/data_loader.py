import pandas as pd
from src.logger import logger


def load_urls_from_tsv(file_path):
    logger.info(f"Loading URLs from file: {file_path}")
    try:
        df = pd.read_csv(file_path, delimiter='\t', dtype=str)
    except FileNotFoundError as e:
        logger.error(f"File not found: {file_path}, error: {e}")
        raise

    return df[['url']]
