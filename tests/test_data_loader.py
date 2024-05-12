import pytest
import pandas as pd
from src.data_loader import load_urls_from_tsv
from py.path import LocalPath


def test_load_urls_valid_file(tmpdir: LocalPath) -> None:
    file_path = tmpdir / "test_input.tsv"
    with open(file_path, "w") as f:
        f.write("url\n")
        f.write(
            "https://www.tidio.com/?a_bucket=bucket1&a_type=type1&a_source=source1\n"
        )

    df = load_urls_from_tsv(file_path)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert (
            df["url"].iloc[0]
            == "https://www.tidio.com/?a_bucket=bucket1&a_type=type1&a_source=source1"
    )


def test_load_urls_nonexistent_file() -> None:
    file_path = "nonexistent_file.tsv"

    with pytest.raises(FileNotFoundError) as e:
        load_urls_from_tsv(file_path)


def test_load_urls_empty_file(tmpdir: LocalPath) -> None:
    file_path = tmpdir / "empty.tsv"
    open(file_path, "a").close()

    with pytest.raises(pd.errors.EmptyDataError) as e:
        load_urls_from_tsv(file_path)


def test_load_urls_invalid_format(tmpdir: LocalPath) -> None:
    file_path = tmpdir / "test_input.tsv"
    with open(file_path, "w") as f:
        f.write("invalid_column\n")

    with pytest.raises(ValueError) as exc_info:
        load_urls_from_tsv(file_path)
