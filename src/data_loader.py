import pandas as pd
from logger import logger


def load_urls_from_tsv(file_path: str) -> pd.DataFrame:
    """Loads URLs from a TSV input file and returns a DataFrame.

    Args:
        file_path (str): The path to the TSV file.

    Returns:
        pandas.DataFrame: A DataFrame containing URLs.

    Raises:
        FileNotFoundError: If the specified file is not found.
        pd.errors.EmptyDataError: If the file is empty or has no columns to parse.
        ValueError: If the TSV file doesn't have a 'url' column.
    """
    logger.info(f"Loading URLs from file: {file_path}")

    try:
        df = pd.read_csv(file_path, delimiter="\t", dtype=str)
    except FileNotFoundError as e:
        logger.error(f"File not found: {file_path}, error: {e}")
        raise
    except pd.errors.EmptyDataError as e:
        logger.error(f"No data or columns to parse from {file_path}, error: {e}")
        raise
    except Exception as e:
        logger.error(
            f"Unexpected error while loading URLs from {file_path}, error: {e}"
        )
        raise

    if "url" not in df.columns:
        logger.error(f"Invalid TSV format: missing 'url' column in {file_path}")
        raise ValueError(f"Invalid TSV format: missing 'url' column in {file_path}")

    logger.info(f"Loaded URLs successfully from {file_path}.")

    return df[["url"]]
