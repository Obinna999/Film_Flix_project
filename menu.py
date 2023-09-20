import readFilm, addFilm,reports,deleteFilm, updatefilm
#from reports import *  to use this methos need to change line 43 and use 44
#function to read the respective menu files
def menuFile():
    with open("Pt11_Film_Flix_progject/filmMenu.txt") as mainMenu:
        userMenu = mainMenu.read()
    return userMenu
print(menuFile())

def filmMenu():
    option = 0 # create option and initialise with integer value of 0
    optionList = ["1","2","3","4","5","6"]
    #call/invoke the function and pass it to a variable userChoice
    userChoise = menuFile()

    # o not in  ["1","2","3","4","5","6"]
    while option not in optionList:#execute the code below
        print(userChoise)

        #re-assign the option variable with the input function
        #(string is the  default data for the  input function)
        option = input("Enter an option from the songs main menu!")
        
        if option not in optionList:# compare the inpiut the user provided above with the elements in the list
            print(f"{option } is not a valid choice in the songs Menu !")
    return option

# create a bolean variable with a True value
mainProgram = True

while mainProgram: # same as while True
    mainFilmMenu = filmMenu() # call songsMenu() function and pass it to the mainMenu variable
    # call / invoke each function from their respective python files
    if mainFilmMenu == "1":
        readFilm.readData()
    elif mainFilmMenu =="2":
        addFilm.insertFilm()
    elif mainFilmMenu == "3":
        updatefilm.update()
    elif mainFilmMenu == "4":
        deleteFilm.delete()
    elif mainFilmMenu == "5":
        reports.reports()
        #report()
    else:
        # reassign the boolean "mainProgram" variable with a False value
        mainProgram = False
input("See you next time in the Film app!")