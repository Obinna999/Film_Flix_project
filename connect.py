import sqlite3 as sql 



dbCon = sql.connect("Pt11_Film_Flix_progject/filmflix.db")#create data base file if not exist and use it, if exist already will just use it

#create a cursor object/variable and assign it to the cursor method to run sql queries
"dbCouror is a variable"
dbCursor = dbCon.cursor()