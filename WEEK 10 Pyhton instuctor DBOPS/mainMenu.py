from readSongs import read
from insertSongs import *
from updateSongs import *
from deleteSongs import *

def menu():
	menuUI = """Welcome to Music Database v1.03

	Please Select an option below:
	1. Display songs in the database
	2. Add a New song to the database
	3. Update an Existing Song
	4. Delete a Song
	5. Exit Application
	"""
	print(menuUI)
	sleep(1)
	options = ["1", "2", "3", "4", "5"]
	choice = input("Select an Option From the menu: ")

	while choice not in options:
		print(f"{choice} is not valid.")
		choice = input("Please Enter a valid option: ")
	
	return choice


if __name__ == "__main__":
	menuLoop = True

	while menuLoop == True:
		userChoice = menu()
		if userChoice == "1":
			read()
		elif userChoice == "2":
			add()
		elif userChoice == "3":
			update()
		elif userChoice == "4":
			delete()
		elif userChoice == "5":
			menuLoop = False

print("End Program")
		