import re
import sqlite3

# Open and read the content of the .sqbpro file
with open('DB/OnlineResturantX.sqbpro', 'r') as file:
    sqbpro_content = file.read()

# Extract SQL statements
sql_statements = re.findall(r'<sql name="SQL 1">(.*?)</sql>', sqbpro_content, re.DOTALL)

# create the SQLie DB
conn = sqlite3.connect('DB/OnlineResturantX.sqlite')

# Create a cursor object
c = conn.cursor()

# Execute each SQL statement
for sql in sql_statements:
    try:
        # Execute the SQL statement
        c.executescript(sql)
        print(f"Executed: {sql}")
    except sqlite3.OperationalError as e:
        print(f"Error executing SQL statement: {e}")
        
conn.commit()
conn.close()

###
