## Read Songs
from connect import *

def read():
    sqlCode = "SELECT * FROM songs"
    cursor.execute(sqlCode)
    # fetchall() will retrieve the data from the latest query
    data = cursor.fetchall()

    if data == []:
        print("The Database Table is empty.")
        return 0
    else:
        print("Songs List:")
        for row in data:
            print(row)
        sleep(2)
        return 1

# This Code Ensures the files is properly modularized.
# This code below wont run automatically if it was imported elsewhere
if __name__ == "__main__":
    read()