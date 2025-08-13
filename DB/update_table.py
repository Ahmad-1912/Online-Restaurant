import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Db_manipulation import update_table

def update_table_and_print(query, table_name):
    try:
        update_table(query)
        print(f"Table {table_name} updated")
    except Exception as e:
        print(f"An error occurred: {e}")

#Statement
if __name__ == "__main__":
    table_name_to_update = 'Orders'
    update_table_query = f"""
        ALTER TABLE {table_name_to_update}
        ADD COLUMN PaymentMethod TEXT;
    """
    update_table_and_print(update_table_query, table_name_to_update)
