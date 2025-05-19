import cx_Oracle
from app.config import DB_CONFIG


def get_connection():
    return cx_Oracle.connect(**DB_CONFIG)


def insert_sales_data(data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.executemany("""
                INSERT INTO sales (sale_id, product, quantity, amount)
                VALUES (:1, :2, :3, :4)
            """, data)
        connection.commit()
    except Exception as error:
        connection.rollback()
        raise error
    finally:
        connection.close()
