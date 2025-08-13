import os
import sqlite3
from contextlib import closing

basedir = os.path.abspath(os.path.dirname(__file__))
parentdir = os.path.dirname(basedir)
db_path = os.path.join(parentdir, 'DB', 'OnlineResturantX.sqlite')

def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def create_table(query):
    with get_db_connection() as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query)
        conn.commit()

def update_table(query):
    with get_db_connection() as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query)
        conn.commit()

def delete_table(table_name):
    query = f"DROP TABLE IF EXISTS {table_name}"
    with get_db_connection() as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query)
        conn.commit()

def add_record(table_name, columns, values):
    columns_str = ', '.join(columns)
    placeholders = ', '.join(['?' for _ in values])
    query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
    
    with get_db_connection() as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query, values)
        conn.commit()

def update_record(table_name, updates, condition, condition_values):
    update_str = ', '.join([f"{column} = ?" for column in updates.keys()])
    query = f"UPDATE {table_name} SET {update_str} WHERE {condition}"
    
    values = list(updates.values()) + condition_values
    
    with get_db_connection() as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query, values)
        conn.commit()

def delete_record(table_name, condition, condition_values):
    query = f"DELETE FROM {table_name} WHERE {condition}"
    
    with get_db_connection() as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query, condition_values)
        conn.commit()

def fetch_records(query, params=()):
    with get_db_connection() as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(query, params)
            records = cursor.fetchall()
    return records

# Specific functions for different tables
def create_customer_table():
    query = """
        CREATE TABLE IF NOT EXISTS Customer (
            customerID INTEGER PRIMARY KEY AUTOINCREMENT,
            firstName TEXT NOT NULL,
            lastName TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            address TEXT NOT NULL,
            password TEXT NOT NULL
        );
    """
    create_table(query)

def delete_customer_by_id(customerID):
    delete_record('Customer', 'customerID = ?', [customerID])

def add_customer(firstName, lastName, email, address, password):
    add_record('Customer', ['firstName', 'lastName', 'email', 'address', 'password'], 
               [firstName, lastName, email, address, password])

def fetch_all_customers():
    return fetch_records("SELECT * FROM Customer")
