from connect import *  # import  the connect module and evefy functions/methods/variable etc

#create a fucnction
def insertFilm():
    filmID = input("Enter song ID : ")
    filmTitle = input("Enter song Title: ")
    filmyearReleased = input("Enter film released date: ")
    filmRating = input("Enter film rating : ")
    filmyduration = input("Enter film duration: ")
    filmyeargenre = input("Enter Film Genre: ")

    # add data inputted/entered into the database
    dbCursor.execute("INSERT INTO tblfilms(filmID,Title, yearReleased,Rating,duration, Genre)VALUES(?,?,?,?,?,?)",(filmID, filmTitle, filmyearReleased,filmRating,filmyduration,filmyeargenre  ))# ??? are placeHolder,needed to keep your information safe
    #save the change in the database permantly/ write record permanently to the songs table in the db 
    dbCon.commit()
    print(f"{filmTitle} inserted into the songs table")

if __name__ == "__main__":
    insertFilm()