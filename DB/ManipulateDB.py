import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('DB/OnlineResturantX.sqlite')
c = conn.cursor()

# List of table names
tables = ['Menu', 'Customer', 'Orders', 'OrderItem', 'Admin']

# Corresponding data to insert for each table
data_to_insert = {
    'Menu': [
        (1, 'Chicken Parmesan', 'Pasta', 'Grilled chicken topped with marinara sauce and melted cheese.', 6.00, True),
        (2, 'Margherita Pizza', 'Pizza', 'Classic pizza with tomato sauce, mozzarella, and basil.', 6.50, True),
        (3, 'Caesar Salad', 'Salad', 'Fresh romaine lettuce tossed with Caesar dressing, parmesan, and croutons.', 7.0, True),
        (4, 'Spaghetti Bolognese', 'Pasta', 'Rich meat sauce served over spaghetti.', 6.5, True),
        (5, 'Vegetable Stir Fry', 'Veggie', 'A mix of vegetables stir-fried with soy sauce.', 6.75, True),
        (6, 'Tiramisu', 'Dessert', 'Layers of coffee-soaked sponge cake and mascarpone cream.', 5.00, True),
        (7, 'Garlic Bread', 'Bread', 'Fresh bread topped with garlic butter and herbs.', 4.99, True),
        (8, 'Fettuccine Alfredo', 'Pasta', 'Fettuccine noodles tossed in a creamy Alfredo sauce.', 5.99, True),
        (9, 'Bruschetta', 'Appetizer', 'Toasted bread topped with fresh tomatoes, basil, and olive oil.', 5.99, True),
        (10, 'Lasagna', 'Pasta', 'Layers of pasta, meat sauce, and cheese.', 5.75, True),
        (11, 'Caprese Salad', 'Salad', 'Tomatoes and mozzarella cheese drizzled with balsamic glaze.', 4.00, True),
        (12, 'Chicken Wings', 'Appetizer', 'Fried chicken wings with your choice of sauce.', 7.00, True),
        (13, 'Fish and Chips', 'Seafood', 'Battered fish served with fries.', 12.99, True),
        (14, 'Cheeseburger', 'Burger', 'A juicy patty topped with cheese, lettuce, and tomato.', 8.50, True)
    ],

    'Customer': [
    (1, 'Hans', 'Peter', 'Hans.Peter@gmail.de', 'Ronneburgstraße 5', '123456'),
    (2, 'Thomas', 'Mueller', 'Thomad.Mueller@gmail.de', 'Hauptstraße 23', 'abcded'),
    (3, 'Julia', 'Wagner', 'Julia.Wagner@gmail.de', 'Am Kirschplatz 9', 'secret1234'),
    (4, 'Leo', 'Anto', 'Leo.Anto@gmail.de', 'Ziegenweg 10', 'qatar3322'),
    (5, 'Christian', 'Eriks', 'Christian.Eriks@gmail.de', 'Lindenstraße 41', 'fif1819'),
    (6, 'Emma', 'Weis', 'Emma.Weis@gmail.de', 'Ahornweg 12', 'nikjen14'),
    (7, 'Abdul', 'Demir', 'Abdul.Demir@gmail.de', 'Kafkstraße 11', 'tespas123abc'),
    (8, 'Tanja', 'Lange', 'Tanja.Lange@gmail.de', 'Am Park 2', 'geheimzahl4'),
    (9, 'Jerome', 'Hummels', 'Jerome.Hummels@gmail.de', 'Rotgelbstraße 4', 'dorbay25'),
    (10, 'Lisa', 'Meyer', 'Lisa.Meyer@gmail.de', 'Eichenweg 87', 'secpass1234'),
    (11, 'Sofia', 'Dimitrov', 'Sofia.Dimitrov@gmail.de', 'Park-Rheinweg 12', 'wasdtasta98'),
    (12, 'Elias', 'Nehr', 'Elias.Nehr@gmail.de', 'Am Gotyweg 97', 'back3back'),
    (13, 'Younes', 'Levet', 'Younes.Levet@gmail.de', 'Rutenweg 47', 'tingber21'),
    (14, 'Lara', 'Kovac', 'Lara.Kovac@gmail.de', 'Eckenlang 3', 'Passrass4'),
    (15, 'Elena', 'Ramos', 'Elena.Ramos@gmail.de', 'Am Dreiplatz 4', 'realred8')
    ],

    'Admin': [
        (1, 'admin1', 'admin1password', 0 ),
        (2, 'admin2', 'admin2password', 0 ),
    ]
}

# Function to get the number of columns in a table
def get_num_columns(cursor, table_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    return len([field[1] for field in cursor.fetchall()])

# Function to get column names for a table
def get_column_names(cursor, table_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    return [field[1] for field in cursor.fetchall()]

# Loop through each table and its corresponding data
for table_name, data in data_to_insert.items():
    # Check if the table exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    table_exists = c.fetchone() is not None

    if table_exists:
        # Table exists, proceed with the insert
        num_columns = get_num_columns(c, table_name)
        column_names = get_column_names(c, table_name)
        placeholders = ', '.join(['?' for _ in range(num_columns)])
        
        # Adjust the insert query based on the number of columns
        sql_query = f"INSERT OR IGNORE INTO {table_name} ({', '.join(column_names)}) VALUES ({placeholders})"
        
        for item in data:
            c.execute(sql_query, item)
        print(f"Data inserted into {table_name}.")
    else:
        print(f"Table {table_name} does not exist.")

# Function for deleting existing tables (if needed)
def delete_table(conn, table_name):
    
    try:
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        print(f"Table '{table_name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting table '{table_name}': {e}")

# Commit the changes and close the connection
conn.commit()
conn.close()