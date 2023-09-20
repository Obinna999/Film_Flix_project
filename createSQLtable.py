from connect import * # import the connect.py module or  import connect ,\n, connect.dbCursor.execute
# execute in this case works as translater, between python and mysql
dbCursor.execute(""" 
CREATE TABLE "tblfilms" (
	"filmID"	INTEGER ,
	"title"	TEXT,
	"yearReleased"	INTEGER,
	"rating"	TEXT,
	"duration" INTEGER,
    "genre" TEXT
)""")