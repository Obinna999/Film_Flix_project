from connect import * # import the connect module and every functions/methods/variables etc

# create a function 
def reports():
    repoInput = input(f"which  report do you want to reviw press number?\n 1. All Films\n 2. Genre\n 3. Year\n 4. Reating  ")
    if repoInput == '1':
        dbCursor.execute("SELECT * FROM tblFilms")
    elif repoInput == '2':
        typGen = input (f"what kind of genre would you like to check? ")
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE Genre = '{typGen }'")
        allFilms = dbCursor.fetchall()
        for eachFilm in allFilms:
            print(eachFilm)
        
    elif repoInput == '3':
        typYea = input (f"from which year release would you like to check? ")
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased ='{ typYea }'")
        allFilms = dbCursor.fetchall()
        for eachFilm in allFilms:
            print(eachFilm)
    elif repoInput == '4':
        typRat = input (f"what king of rating would you like to check? ").title()
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{ typRat }'")
        allFilms = dbCursor.fetchall()
        for eachFilm in allFilms:
            print(eachFilm)
    else:
        print('exit')


    # fetch all the selected songs using the fetchall method
    allRecords = dbCursor.fetchall()

    #loop through the records
    for eachRecord in allRecords:
        # and display themm in th terminal 
        print(eachRecord)

if __name__ == "__main__":
    reports()