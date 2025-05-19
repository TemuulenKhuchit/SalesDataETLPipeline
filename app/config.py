import os

DB_CONFIG = {
    "user": "hr",
    "password": "Temuulen123$",
    "dsn": "localhost:1521/orclpdb",
}

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

INPUT_FOLDER = os.path.join(BASE_DIR, "resources", "input")
LOG_FILE = os.path.join(BASE_DIR, "logs", "etl.log")
