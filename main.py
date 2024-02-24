import mariadb
import sys

# Connect to MariaDB Platform
try:
    # password censored
    conn = mariadb.connect(
        user="juno",
        # password="",
        host="localhost",
        database="P2PA"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# Execute the query
cur.execute("SHOW COLUMNS FROM users")

# Fetch the results
columns = cur.fetchall()

# Print the columns
for column in columns:
    print(column[0])

# Add an entry
try:
    cur.execute("INSERT INTO users (username, auth_token, time) VALUES (?, ?, NOW())", ('new_user', 1234567890))
    conn.commit()
    print("New entry added successfully!")
except mariadb.Error as e:
    print(f"Error adding entry: {e}")
    conn.rollback()

# cur.execute("SELECT * WHERE username = ?", ("new_user"))
# Update an entry
try:
    cur.execute("UPDATE users SET auth_token = ? WHERE username = ?", (9876543210, 'new_user'))
    conn.commit()
    print("Entry updated successfully!")
except mariadb.Error as e:
    print(f"Error updating entry: {e}")
    conn.rollback()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/database_name'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# Close connection
conn.close()
