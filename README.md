# URL Parser & SQL Queries

This project provides:
- Python script to parse marketing parameters from URLs and saves the results in TSV format,
- **(WIP)** SQL VIEW to identify customers who meet specific criteria for targeted marketing incl. email addresses and 
engagement metrics,


## Features
Task 1 
- **TSV Input/Output:** Reads URLs from a TSV file and writes the parsed results to another TSV file.
- **URL Parsing:** Extracts ad bucket, type, source, schema version, campaign ID, keyword, group ID, and creative from Tidio URLs.
- **Error Handling:** Includes error handling for invalid URLs, missing files, or incorrect file formats.
- **Logging:**  records information & errors during processing with centralized logger
- **Tested:** Includes unit tests with pytest 
- **Dockerized:** Runs seamlessly in a Docker container for portability and ease of deployment.

Task 2
- **VIEW + SQL Statement**

## Prerequisites
- **Docker:** Ensure you have Docker installed on your system. You can find installation instructions and downloads for your operating system on the official Docker website:

   - [Docker Desktop for Mac]([https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/))
   - [Docker Desktop for Windows]([https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/))
   - [Docker Engine for Linux]([https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/))

- **Python:** Ensure you have at least Python 3.12 
## Usage
1. **Input Data:**
   - Place your input TSV file (with a column named "url") in the `data/input` directory.
   - An example file, `task1_input.tsv`, is provided.

2. **Building the Docker Image:**
   - Open a terminal and navigate to the project's root directory.
   - Run the following command to build the Docker image:
     ```bash
     docker build -t url-parser .
     ```

3. **Running the Docker Container:**
   - Execute this command to start the container and process the URLs:
     ```bash
     docker run url-parser
     ```

4. **Output:**
   - The parsed results will be saved in the `data` directory as `task1_output.tsv`.

## Testing
- **Unit Tests:**
   - The project includes pytest tests in the `tests` directory.
   - Run tests using:
     ```bash
     python3 -m pytest
     ```

## Project Structure
- `src/`: Contains the source code for the URL parser.
- `tests/`: Includes unit and integration tests.
- `Dockerfile`: Instructions for building the Docker image.
- `requirements.txt`: List of Python dependencies.
- `data/input`: Directory for input TSV files.
- `data/output`: Directory for output TSV files.
- **(Task2)** `sql`: Directory with SQL queries for Task2 & Optional Task


## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.
