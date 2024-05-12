import pytest
import pandas as pd
from src.output_writer import write_results_to_tsv


def test_write_results_to_tsv(tmpdir):
    # Create a temporary file
    output_file = tmpdir / "test_output.tsv"

    # Create sample data with multiple rows
    data = pd.DataFrame({
        "url": ["https://www.example.com/", "https://www.another-example.com/"],
        "ad_bucket": ["test_bucket", "another_bucket"],
        "ad_type": ["test_type", "another_type"],
        "ad_source": ["test_source", "another_source"],
        "schema_version": ["2", "3"],
        "ad_campaign_id": ["12345", "54321"],
        "ad_keyword": ["test_keyword", "another_keyword"],
        "ad_group_id": ["98765", "56789"],
        "ad_creative": ["11111", "22222"],
    })

    # Ensure columns are strings
    str_columns = ["schema_version", "ad_campaign_id", "ad_group_id", "ad_creative"]
    for col in str_columns:
        data[col] = data[col].astype(str)

    write_results_to_tsv(output_file, data)

    df_written = pd.read_csv(output_file, delimiter="\t", dtype=str)

    pd.testing.assert_frame_equal(df_written, data)


def test_write_results_invalid_data_type(tmpdir):
    # Create a temporary file
    output_file = tmpdir / "test_output.tsv"

    # Create sample data as a list of dictionaries
    data = [{"url": "https://www.example.com/"}]

    with pytest.raises(TypeError) as e:
        write_results_to_tsv(output_file, data)
