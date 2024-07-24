from connect import *
from readSongs import read

# Delete a Row in SQL?
# DELETE FROM table_name WHERE condition

# Askes the User for the song ID to delete
def delete():
	readdata = read()
	if readdata == 0:
		print("There is no data to delete.")
	else:
		songID = input("Enter a SongID to delete: ")

		# Deleting song number 6?
		sqlCode = f"""
		DELETE FROM songs
		WHERE SongID = "{songID}";

		"""

		cursor.execute(sqlCode)
		conn.commit()

		print(f"Song {songID} has been successfully deleted.")
		sleep(2)

		read()

if __name__ == "__main__":
	delete()