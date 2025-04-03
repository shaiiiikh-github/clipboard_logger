This script monitors the clipboard for new copied text and automatically saves it into a MySQL database along with the exact date and time when it was copied. The script runs continuously in the background and can be configured to start automatically when the system boots up.

📌 Features

✅ Monitors clipboard in real-time (checks every 2 seconds)
✅ Stores copied text along with a timestamp
✅ Prevents duplicate entries
✅ Automatically starts on system boot (Windows/Linux/Mac)
✅ Easy retrieval of clipboard history

🛠️ Setup Instructions

1️⃣ Install Dependencies
pip install pyperclip mysql-connector-python

2️⃣ MySQL Database Setup
Step 1: Create a MySQL Database
CREATE DATABASE clipboard_db;

Step 2: Create the Table
USE clipboard_db;

CREATE TABLE clipboard_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    copied_text TEXT NOT NULL,
    copied_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

3️⃣ Python Script
simply copy-paste the file provided in the repo

4️⃣ Running the Script on Startup

Windows (Task Scheduler)

Open Task Scheduler (Win + R, type taskschd.msc, press Enter).

Click Create Basic Task → Name it ClipboardLogger.

Choose "When the computer starts".

Select Start a Program → Browse to your Python script (clipboard_logger.py).

Click Finish.

5️⃣ Retrieving Stored Clipboard Data

Option 1: Using MySQL
SELECT * FROM clipboard_history ORDER BY copied_at DESC;

Option 2: Using Python (retrive.py)

📌 Future Enhancements

🔹 Exclude passwords from being stored
🔹 Auto-delete old entries for privacy
🔹 GUI for viewing clipboard history

🚀 Contribute

If you have suggestions or improvements, feel free to submit a pull request! 
For any question or help you can slide in to my dm (wwww.instagram.com/shaiiiikh.ig) 
or email me at shabbir23rd@gmail.com


