import mysql.connector
from sqlalchemy import engine
#engine = create_engine("")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysecretpassword",
    database="mydb",
    port=3306
)

cursor = conn.cursor()

# Drop old table if exists
cursor.execute("DROP TABLE IF EXISTS users2")

# Create with auto_increment
cursor.execute('''
    CREATE TABLE users2 (
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255),
        email VARCHAR(255)
    ) ENGINE=InnoDB
''')

cursor.execute("INSERT INTO users2 (name, email) VALUES (%s, %s)", ('Alice', 'alice@example.com'))
cursor.execute("INSERT INTO users2 (name, email) VALUES (%s, %s)", ('Bob', 'bob@example.com'))

conn.commit()

cursor.execute("SELECT * FROM users2")
rows = cursor.fetchall()

print("Users in the database:")
for row in rows:
    print(row)

conn.close()
