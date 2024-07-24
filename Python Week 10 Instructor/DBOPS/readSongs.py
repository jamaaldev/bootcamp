## Read Songs
from connect import *

def read():
    sqlCode = "SELECT * FROM songs"
    cursor.execute(sqlCode)

    # fetchall() will retrieve the data from the latest query
    data = cursor.fetchall()

    print("Songs\nSongs List:")
    for i in data:
        print(i)


if __name__ == "__main__":
    read()