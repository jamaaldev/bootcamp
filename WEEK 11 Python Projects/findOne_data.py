from connect_db import *

def findOne(table_name,column_name,personID):
    findSQL = f"""
    SELECT * FROM "{table_name}"
    WHERE "{column_name}" = "{personID}"
    """
    cursor.execute(findSQL)
    data = cursor.fetchall()
    return data