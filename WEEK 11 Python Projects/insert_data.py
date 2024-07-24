from connect_db import *
from read_data import *
from update_data import *
from findOne_data import *
def parent():
    personID = input('Enter Your Passport ID or driver-license ID: ')
    
    findedPerson = findOne('parent','PersonID',personID)
    print('findedPerson:',findedPerson)
    if findedPerson != []:
        hasKids = input('Enter yes or no if you have child to Register yes or no : ').lower()
        if hasKids == 'yes':
            relationship = input('Enter relationship with the child, Ex: Father,Mother,Carer : ').lower()
            column_name = relationship
            childID = input('Enter Child Passport ID or birth certificate number: ')

            if column_name == 'father':
                column_name = "FatherID"
            if column_name == 'mother':
                column_name = "MotherID"
            if column_name == 'carer':
                column_name = "CarerID"
            parentID = input('ParentID: Enter Your Passport ID or driver-license ID: ')
            updateParent(column_name,parentID,personID)
            updateChildren(column_name,parentID,childID)
        else:
            print('good bye')
    else:  

        firstName = input('Enter your First Name: ')
        lastName = input('Enter your Last Name: ')
        age = input('Enter your Age: ')
        hasKids = input('Enter yes or no if you have child to Register yes or no : ').lower()
    
        # insertSQL = f"""
        # INSERT INTO parent VALUES(NULL,{firstName},{lastName},{age},{'father'},{"mother"},{'carer'})
        # """
        if hasKids == 'yes':
            relationship = input('Enter relationship with the child, Ex: Father,Mother,Carer : ').lower()
            parentID = personID
            if relationship == 'father':
                insertSQL = f"""
                INSERT INTO parent VALUES(NULL,"{firstName}","{lastName}","{age}","{parentID}",NULL,NULL)
                """
                cursor.execute(insertSQL)
                conn.commit()
            if relationship == 'mother':
                insertSQL = f"""
                INSERT INTO parent VALUES(NULL,"{firstName}","{lastName}","{age}",NULL,"{parentID}",NULL)
                """
                cursor.execute(insertSQL)
                conn.commit()
            if relationship == 'carer':
                insertSQL = f"""
                INSERT INTO parent VALUES(NULL,"{firstName}","{lastName}","{age}",NULL,NULL,"{parentID}")
                """
                cursor.execute(insertSQL)
                conn.commit()
            child()
        else:
            insertSQL = f"""
            INSERT INTO parent VALUES(NULL,"{firstName}","{lastName}","{age}",Null,NULL,NULL)
            """
            cursor.execute(insertSQL)
            conn.commit()
        

 


def child():
    print('parent-list:',readParent())
    childID = input('Enter Child Passport ID or birth certificate number: ')
    # first check if the child already exist in the database
    # by checking passport id or birth certificate number
    findedPerson = findOne('children','ChildID',childID)
    print('findPerson:',findedPerson)
    relationship = input('Enter relationship with the child, Ex: Father,Mother,Carer : ')
    print('relation:',relationship)
    if findedPerson != []:
        column_name = relationship
        if column_name == 'father':
            column_name = "FatherID"
        if column_name == 'mother':
            column_name = "MotherID"
        if column_name == 'carer':
            column_name = "CarerID"
        parentID = input('ParentID: Enter Your Passport ID or driver-license ID: ')
        updateChildren(column_name,parentID,childID)
    else:  
        firstName = input('Enter child First Name: ')
        lastName = input('Enter child Last Name: ')
        age = input('Enter child Age: ')
        # insertSQL = f"""
        #     INSERT INTO children VALUES(NULL,"{firstName}","{lastName}","{age}","{childID}","{'father'}","{'mother'}","{'carer'}")
        #     """
        parentList = ['father','mother','carer']
        print('rel',relationship,'pare',parentList)
        if relationship in parentList:
            parentID = input('ParentID: Enter Your Passport ID or driver-license ID: ')
            print('relationship',relationship)
            if parentID != '':
                insertSQL = f"""
                    INSERT INTO children VALUES(NULL,"{firstName}","{lastName}","{age}","{childID}","{parentID}",NULL,NULL)
                    """
                cursor.execute(insertSQL)
                conn.commit()
      

if __name__ == '__main__':
    parent()