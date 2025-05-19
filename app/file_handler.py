import os
import pandas as pd
from app.exceptions import FileReadError


def read_csv_file(file_path):
    try:
        return pd.read_csv(file_path)
    except FileReadError as error:
        raise FileReadError(f'Error reading {file_path}: {error}')


def get_all_csv_files(input_folder):
    return [os.path.join(input_folder, f)
            for f in os.listdir(input_folder)
            if f.endswith('.csv')]
