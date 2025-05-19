import logging
from app.file_handler import read_csv_file
from app.data_processor import clean_sales_data, convert_to_tuples
from app.database import insert_sales_data
from app.exceptions import FileReadError, DatabaseInsertError


def process_file(filepath):
    try:
        logging.info(f"Processing file: {filepath}")
        df = read_csv_file(filepath)
        df = clean_sales_data(df)
        data = convert_to_tuples(df)
        insert_sales_data(data)
        logging.info(f"Successfully processed: {filepath}")
    except FileReadError as fe:
        logging.error(f"File error: {fe}")
    except Exception as e:
        logging.exception(f"Unexpected error in {filepath}: {str(e)}")
