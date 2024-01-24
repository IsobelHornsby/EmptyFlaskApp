# import sql
import sqlite3

# creat the class
class Database:
    def __init__(self):
        # link to the data base file
        self.DBname = "database.db"

    # creates connection to the database
    def connect(self):
        conn= None
        try:
            conn=sqlite3.connect(self.DBname)
        except Exception as e:
            print(e)
        return conn
    
    # creating the pull from command
    def queryDB(self, command, params=[]):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(command, params)
        # filters and collects the results
        result = cur.fetchall()
        self.disconnect(conn)
        return result
    
    # creating the write to command
    def updateDB(self, command, params=[]):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(command, params)
        # commits change to the database
        conn.commit()
        result = cur.fetchall()
        self.disconnect(conn)
        return result
    
    # colses the connection and releases any resources used
    def disconnect(self, conn):
        conn.colse()


        