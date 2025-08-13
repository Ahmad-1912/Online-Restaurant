import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Db_manipulation import delete_table

def delete_table_and_print(table_name):
    try:
        delete_table(table_name)
        print(f"Table {table_name} deleted")
    except Exception as e:
        print(f"An error occurred: {e}")

# Statement
if __name__ == "__main__":
    table_name_to_delete = 'Menu'  # Change this to the table you wants to delete
