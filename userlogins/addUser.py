import hashlib
import sqlite3

DBName = "userlogins.db"

def usernameAvailable(username):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    res = c.execute("""
        SELECT *
        FROM users
        WHERE
          username = ?
    
    """, (username,)).fetchone()

    return res is None

def addUser(username, password):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    passwordHash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    c.execute("""
        INSERT INTO
            users (username, passwordHash)
        VALUES
            (?, ?)
        """, (username, passwordHash))
    conn.commit()

def main():
    print("creating user acct")

    while True:
        username = input("what's your username? ")
        if(usernameAvailable(username) == True):
            print("username available")
            break
        else:
            print("username taken, choose another")
        
    password = input("what's your password? ")

    addUser(username, password)
    print("added to database")

main()