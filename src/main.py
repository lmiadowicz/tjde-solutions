from data_loader import load_urls_from_tsv
from url_parser import parse_urls


def main():
    file_path_input = f"data/task1_input.tsv"

    urls = load_urls_from_tsv(file_path_input)
    parsed_data = parse_urls(urls)


if __name__ == "__main__":
    main()
