from typing import List
import pandas as pd
import pytest
from src.url_parser import parse_urls


def test_parse_valid_urls():
    urls: List[str] = [
        "https://www.tidio.com/?a_bucket=bucket1&a_type=type1&a_source=source1",
        "https://www.tidio.com/?a_g_campaignid=12345&a_g_keyword=test",
    ]

    # Convert the list of URLs to a DataFrame
    df: pd.DataFrame = pd.DataFrame({"url": urls})

    expected_output: pd.DataFrame = pd.DataFrame({
        "url": [
            "https://www.tidio.com/?a_bucket=bucket1&a_type=type1&a_source=source1",
            "https://www.tidio.com/?a_g_campaignid=12345&a_g_keyword=test",
        ],
        "ad_bucket": ["bucket1", ""],
        "ad_type": ["type1", ""],
        "ad_source": ["source1", ""],
        "schema_version": ["", ""],
        "ad_campaign_id": ["", "12345"],
        "ad_keyword": ["", "test"],
        "ad_group_id": ["", ""],
        "ad_creative": ["", ""],
    })

    df_parsed: pd.DataFrame = parse_urls(df)

    # Check number of rows
    assert df_parsed.shape[0] == 2

    # Check column names
    assert df_parsed.columns.tolist() == [
        "url", "ad_bucket", "ad_type", "ad_source", "schema_version",
        "ad_campaign_id", "ad_keyword", "ad_group_id", "ad_creative"
    ]

    # Check individual values (compare entire dataframe)
    pd.testing.assert_frame_equal(df_parsed, expected_output)


def test_parse_empty_df():
    # Create an empty DataFrame
    df: pd.DataFrame = pd.DataFrame(columns=["url"])

    # Check if ValueError is raised when an empty DataFrame is passed
    with pytest.raises(ValueError):
        parse_urls(df)
