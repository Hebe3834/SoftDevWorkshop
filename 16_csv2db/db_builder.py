# Team Whales: Hebe Huang, Josephine Lee, Han Zhang
# SoftDev
# K16: All About Database
# 2021-10-21

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

db = sqlite3.connect("Whales") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
c.execute("CREATE TABLE IF NOT EXISTS roster(name TEXT, age INTEGER, id INTEGER)") #creates table if one does not exist

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

with open("students.csv", mode = 'r') as students:  #reads in csv file
    file = csv.DictReader(students)
    for lines in file:                              #iterates through csv rows
        query = "INSERT INTO roster VALUES(\"" + lines['name'] \ 
         + "\"," + lines['age'] \
         + "," + lines['id'] + ")" #queries for sqlite; " \" continues previous line in Python
        c.execute(query)

c.execute("CREATE TABLE IF NOT EXISTS courses(code TEXT, mark INTEGER, id INTEGER)") #creates table if one does not exist
with open("courses.csv", mode = 'r') as courses:  #reads in csv file
    file = csv.DictReader(courses)
    for lines in file:                              #iterates through csv rows
        query = "INSERT INTO courses VALUES(\"" + lines['code'] \
        + "\"," + lines['mark'] \
        + "," + lines['id'] + ")" #queries for sqlite
        c.execute(query)

#==========================================================

db.commit() #save changes
db.close()  #close database