from Db_manipulation import update_record

def update_customer_and_print(customerID, updates):
    try:
        update_record('Customer', updates, 'customerID = ?', [customerID])
        print(f"Customer with ID {customerID} updated: {updates}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Statement
if __name__ == "__main__":
    customer_id_to_update = 1234 # Change the ID for the customer you wants to update
    updates = {
        'firstName': 'UpdatedFirstName19',
        'lastName': 'UpdatedLastName',
        'email': 'updated.email@example.com',
        'address': '123 Updated Street',
        'password': 'newsecurepassword'
    }
    update_customer_and_print(customer_id_to_update, updates)
