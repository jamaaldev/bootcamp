# Database Operations
# CRUD Acronynm
# Create: Create and Insert values into the database
# Read: Read the database
# Update: Update the database
# Delete: Delete Values from the database

import sqlite3 as sql

# connect() function
conn = sql.connect(r"C:\Files\Desktop\softwarebootcamp\Lessons\GLA\Python Week 10\DBOPS\bootcamp.db")
# cursor() function, will let us perform SQL on a given connection.
cursor = conn.cursor()

# execute() function will let us excute SQL Code
# cursor.execute("SELECT * FROM table")

# Connections must be committed as we execute statement
#conn.commit()

"""
To Do:

Create Table (createTbl.py)
(Create) Insert Songs (insertSongs.py)
Read Songs (readSongs.py)
Update Songs (updateSong.py)
Delete Songs (deleteSongs.py)

"""