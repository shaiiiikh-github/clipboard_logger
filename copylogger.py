import pyperclip
import mysql.connector
import time
from datetime import datetime

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this if using a different user
    password="password",  # Replace with your MySQL password
    database="database_name"
)
cursor = db.cursor()

last_text = ""

while True:
    text = pyperclip.paste()  # Get clipboard content
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current date & time

    if text and text != last_text:  # Prevent duplicates
        sql = "INSERT INTO clipboard_history (copied_text, copied_at) VALUES (%s, %s)"
        cursor.execute(sql, (text, timestamp))
        db.commit()
        print(f"Saved: '{text}' at {timestamp}")
        last_text = text

    time.sleep(2)  # Check clipboard every 2 seconds
