from data_loader import load_urls_from_tsv


def main():
    file_path_input = f"data/task1_input.tsv"

    urls = load_urls_from_tsv(file_path_input)


if __name__ == "__main__":
    main()
