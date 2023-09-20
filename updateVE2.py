from connect import *

# (1, 'She knows', 'J Cole', 'Hip hop')

# create a function 
def update():
    # use primary to update a record in the songs table 
    idField = input("Enter the filmID of the record to be updated: ")

    titleField = input("Enter Title value: ").title()
    artistField = input("Enter Artist value: ").title()
    genreField = input("Enter  Genre value: ").title()

    # print(fieldValue)

    # add single quotes to the value to match he existing data as we are only updating and NOT!!! inserting
    titleField = "'"+titleField+"'"
    artistField = "'"+artistField+"'"
    genreField = "'"+genreField+"'"

    # to update all fields
    dbCursor.execute(f"UPDATE songs SET Title = {titleField}, Artist = {artistField}, Genre = {genreField}  WHERE SongID = {idField}")
    print(f"Record {idField} updated in the songs table. ")
    dbCon.commit()
if __name__ == "__main__":
    update()
