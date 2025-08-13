from Db_manipulation import delete_customer_by_id

def delete_customer_and_print(customerID):
    delete_customer_by_id(customerID)
    print(f"Customer with ID {customerID} deleted")

#Statement
customer_id_to_delete = 1234 #Change teh ID to the customer you wants to delete
delete_customer_and_print(customer_id_to_delete)
