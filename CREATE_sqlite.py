#!/usr/bin/python 3.6

import sqlite3

# the first thing we need is a database
# we can either connect to a pre-existing db or create a new one

conn = sqlite3.connect('test_again.db') # we can change path as desired
print ("Opened database successfully")

# Lets check if a db was created. Next step, create a table. 

# CREATE table with given schema
conn.execute('''CREATE TABLE COMPANY
         (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        VARCHAR,
         SALARY         REAL);''')
print ("Table COMPANY created successfully")

# NOT NULL are the constraints showing that these fields cannot be 
# NULL while creating records in this table.

# Lets create another table so we can test out joins

conn.execute('''CREATE TABLE DEPARTMENT
   (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   DEPT           CHAR(50) NOT NULL,
   EMP_ID         INT      NOT NULL);''')
print("Table DEPARTMENT created successfully")

# Lets see if these tables are present 
# YES


conn.close()




