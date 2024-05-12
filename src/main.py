from data_loader import load_urls_from_tsv
from url_parser import parse_urls
from output_writer import write_results_to_tsv


def main():
    file_path_input = f"data/task1_input.tsv"
    file_path_output = f"data/task1_output.tsv"

    urls = load_urls_from_tsv(file_path_input)
    parsed_data = parse_urls(urls)
    write_results_to_tsv(file_path_output, parsed_data)


if __name__ == "__main__":
    main()
