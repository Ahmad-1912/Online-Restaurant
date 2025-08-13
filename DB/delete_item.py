import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Db_manipulation import delete_record

def delete_item_and_print(itemID):
    try:
        delete_record('Menu', 'itemID = ?', [itemID])
        print(f"Item with ID {itemID} deleted")
    except Exception as e:
        print(f"An error occurred: {e}")

# Statement
if __name__ == "__main__":
    item_id_to_delete = 1234  # Change the ID of the item you want to delete
    delete_item_and_print(item_id_to_delete)
