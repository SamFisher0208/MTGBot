import sqlite3

#Setup a connection with our database file
connection = sqlite3.connect("magicRepeats.db")

#Create a cursor for the database to execute statements
cursr = connection.cursor()

print("Connected to the database")

#cursr.execute("""CREATE TABLE magicCards (
#                URLs text
#               )""")



#sketch:
# !vibes is called - then getVibe is called - then img URL is posted
# DB managment needs to happen before img URL is posted
# maybe check if dupe before calling getVibe? 

#will have to make a function that receivies the image URL to update DB
# def updateDB(imgURL):
#   1. add row
#   2. check if repeat 
#       2a. if true, call getVibe again?
#   3. commit and close DB

#def updateDB(imgURL):
    #cursr.execute("INSERT INTO magicCards VALUE (?);", imgURL)
    #connection.commit
    #return

connection.close()