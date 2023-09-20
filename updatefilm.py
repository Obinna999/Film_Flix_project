from connect import *

# (1, 'She knows', 'J Cole', 'Hip hop')

def update():
    # use primary to update a record in the songs table 
    idField = input("Enter the filmID of the record to be updated: ")

    # ask user the field they want to update 
    fieldName = input("Enter Title or Year Released  or Rating Or Durationor Genre as field name: ").title()

    # ask user to provide the value for the field they want to update 
    fieldValue = input(f"Enter the value for {fieldName} field: ")

    # print(fieldValue)

    # add single quotes to the value to match he existing data as we are only updating and NOT!!! inserting
    fieldValue = "'"+fieldValue+"'"
    # print(fieldValue)
    
    #update a specific field for a particular record
    "UPDATE tblFilms SET {filmID /Title/yearReleased/rating/duration/Genre} = {TitleValue/yearReleasedValue /TitleValue / filmIValue/ ArtistValue / GenreValue}  WHERE filmID = 1/2/3...."
    dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue}  WHERE filmID = {idField}")
   
    dbCon.commit()
    print(f"Record {idField} updated in the film table. ")
if __name__ == "__main__":
    update()