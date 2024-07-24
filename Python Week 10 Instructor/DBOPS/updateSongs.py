from connect import *
from readSongs import *

songID = input("Enter the ID of the song you'd Like to update: ")

title = input("Enter the name of the song: ")
artist = input("Enter the name of the Artist: ")
genre = input("Enter the Genre of the Song: ")



sqlCode = f"""
UPDATE songs
SET Title = "{title}", Artist = "{artist}", Genre = "{genre}"
WHERE SongID = {songID}
"""

cursor.execute(sqlCode)
conn.commit()

print(f"The Song has been successfully updated.")

read()