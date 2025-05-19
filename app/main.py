import logging
from concurrent.futures import ThreadPoolExecutor
from app.config import INPUT_FOLDER, LOG_FILE
from app.file_handler import get_all_csv_files
from app.etl_runner import process_file


def setup_logging():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def main():
    setup_logging()
    files = get_all_csv_files(INPUT_FOLDER)
    logging.info(f"Found {len(files)} files.")

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(process_file, files)


if __name__ == "__main__":
    main()
