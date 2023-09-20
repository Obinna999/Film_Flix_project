from connect import *


#creat a function
def delete():
    #use primary to delete a record in the songs table
    idField = input("Enter the sondID of the record to be updated: ")


    dbCursor.execute(f"DELETE FROM tblfilms WHERE filmID = {idField} ")
    
    dbCon.commit()

    print(f"Record {idField} deleted from the Film table")
if __name__ == "__main__":
    delete()