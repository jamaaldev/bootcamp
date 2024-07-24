## Insert Songs
from connect import *
from readSongs import *

def add():
	title = input("Enter the name of the song: ")
	artist = input("Enter the name of the Artist: ")
	genre = input("Enter the Genre of the Song: ")


	sqlCode = f"""
	INSERT INTO songs VALUES (NULL, "{title}", "{artist}", "{genre}")
	"""

	cursor.execute(sqlCode)
	conn.commit()

	print(f"{title} was successfully added to the database.")

	read()

if __name__ == "__main__":
	add()
