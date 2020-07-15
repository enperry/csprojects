import os
import sqlite3

DBName = "userlogins.db"

def main():
    if os.path.isfile(DBName):
        while True:
            ans = input("database file already exists, overwrite? (y/n) ")

            if(ans == "y"):
                print("OK. deleting database and recreating")
                os.remove(DBName)
                break
            elif (ans == "n"):
                print("ok. exiting.")
                exit(0)
            else:
                print("invalid input")
            
    conn = sqlite3.connect(DBName)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE users (
            username VARCHAR
        ) 
    """)
    conn.commit()

    # password table because sql no work

    conn = sqlite3.connect(DBName)
    c = conn.cursor()

    c.execute("""
        ALTER TABLE users
        ADD passwordHash VARCHAR
    """)
    conn.commit()

    print("database creation complete")

main()