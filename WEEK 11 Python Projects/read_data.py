from connect_db import *

def readParent():
    readSQL = """ SELECT * FROM parent """
    cursor.execute(readSQL)
    data = cursor.fetchall()
    return data

def readChildren():
    readSQL = """ SELECT * FROM children """
    cursor.execute(readSQL)
    data = cursor.fetchall()
    return data

if __name__ == "__main__":
   print('parent list :',readParent()) 
   print('children list :',readChildren()) 
