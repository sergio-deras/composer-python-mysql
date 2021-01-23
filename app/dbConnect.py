import sys
import os
import time

hostname = sys.argv[1]
username = 'root'
password = 'admin123' 
database = 'sys'

def doQuery( conn ) :
    cur = conn.cursor()
    cur.execute( "SELECT * FROM People" )

    for firstname, secondname, addr, city in cur.fetchall() :
        print(firstname, secondname, addr, city)


print("Using mysql.connector")

import mysql.connector
myConnection = mysql.connector.connect (host=hostname, user=username, passwd=password, db=database)
doQuery(myConnection)
myConnection.close()