import pandas as pd
from src.logger import logger


def write_results_to_tsv(file_path, data):
    """Writes parsed URL data to a TSV file.

    Args:
        file_path (str): The path to the output TSV file.
        data (pandas.DataFrame): A DataFrame containing parsed URL data.

    Raises:
        TypeError: If the input data is not a pandas DataFrame
        IOError: If there's an error writing to the file.
    """
    logger.info(f"Writing results to file: {file_path}")

    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input data must be a pandas DataFrame")

    try:
        data.to_csv(file_path, sep='\t', index=False)
    except IOError as e:
        logger.error(f"Error writing to file: {e}")
        raise

    logger.info(f"Successfully wrote {len(data)} rows to {file_path}")
