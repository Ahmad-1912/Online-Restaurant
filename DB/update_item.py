import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Db_manipulation import update_record

def update_item_and_print(itemID, updates):
    try:
        update_record('Menu', updates, 'itemID = ?', [itemID])
        print(f"Item with ID {itemID} updated: {updates}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Statement
if __name__ == "__main__":
    item_id_to_update = 123 # Change the ID of the item you want to update
    updates = {
        'itemName': 'Updated Item Name',
        'category': 'Updated Category',
        'description': 'Updated Description',
        'price': 19.99,
        'availability': True
    }
    update_item_and_print(item_id_to_update, updates)
