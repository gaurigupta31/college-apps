from dotenv import load_dotenv
import os, time, random, logging, psycopg2, psycopg2.extras, getpass, srp
from argparse import ArgumentParser, RawTextHelpFormatter
from psycopg2.errors import SerializationFailure
load_dotenv()


# with env file
def checkConnection():
    #connection with database
    try:
        conn = psycopg2.connect(user=os.getenv('DB_USER'),
                                    password=os.getenv('DB_PASS'),
                                    host=os.getenv('DB_HOST'),
                                    port=os.getenv('DB_PORT'),
                                    database=os.getenv('DB_NAME'))
        cur = conn.cursor()
        print("Connected to CA DB")
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Failed to complete request", error)
        return False

def closeConnection(conn):
    #closing database connection.
    if conn:
        conn.close()
        print("PostgreSQL connection is closed")

         
def createTableUsers():
    conn = checkConnection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS USER_INFO(
        id BIGSERIAL NOT NULL PRIMARY KEY, 
        email STRING NOT NULL,
        salt STRING,
        vkey STRING,
        notion_id STRING,
        page_id STRING
        );''')
    conn.commit()
    closeConnection(conn)


def addDataUsers(email, salt, vkey, notion_id, page_id):
    conn = checkConnection()
    cur = conn.cursor()
    cur.execute("""INSERT INTO user_info(email, salt, vkey, notion_id, page_id) 
    VALUES(%s, %s, %s, %s, %s);""", (email, salt, vkey, notion_id, page_id))
    conn.commit()
    closeConnection(conn)



def readDataUsers():
    conn = checkConnection()
    cur = conn.cursor()
    tableName = "user_info" 
    cur.execute("SELECT * FROM " + tableName)
    cur.execute("SELECT COUNT (*) FROM " + tableName)
    count = cur.fetchone()
    cur.execute("SELECT * FROM " + tableName)
    for x in cur.fetchall():
        print (x)
    conn.commit()
    closeConnection(conn)

#for testing
if __name__ == '__main__':
    checkConnection()
    # createTableUsers()

    # print("Username: ")
    # uname = str(input())
    # password = getpass.getpass()
    # salt, vkey = srp.create_salted_verification_key(uname, password)
   
    # addDataUsers(str(uname), str(salt), str(vkey), 'NULL', 'NULL')
    # readDataUsers()