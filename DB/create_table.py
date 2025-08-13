import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Db_manipulation import create_table

def create_table_and_print(query, table_name):
    try:
        create_table(query)
        print(f"Table {table_name} created")
    except Exception as e:
        print(f"An error occurred: {e}")

# Statement
if __name__ == "__main__":
    table_name_to_create = 'Example'
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name_to_create} (
            exampleID INTEGER PRIMARY KEY AUTOINCREMENT,
            exampleName TEXT NOT NULL
        );
    """
    create_table_and_print(create_table_query, table_name_to_create)
