import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password",
    database="Database_name"
)

cursor = db.cursor()
cursor.execute("SELECT copied_text, copied_at FROM clipboard_history ORDER BY copied_at DESC")

for text, timestamp in cursor.fetchall():
    print(f"{timestamp}: {text}")

db.close()
