from connect import *  # import  the connect module and evefy functions/methods/variable etc

#create a function
def readData():
    #select all records in song table
    dbCursor.execute("SELECT * FROM tblfilms")
    
    #fetch all the selecetd songs using the fetchall method
    allFilms = dbCursor.fetchall()

    #loop through the records
    for eachFilm in allFilms:
        # and display them in the terminal
        print(eachFilm)

if __name__ == "__main__":
    readData()