import hashlib
import sqlite3

DBName = "userlogins.db"

def isValidCredentials(username, password):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()

    passwordHash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    res = c.execute("""
        SELECT *
        FROM users
        WHERE
            username = ? AND
            passwordHash = ?
        """, (username, passwordHash)).fetchone()
    
    return res is not None




def main():
    username = input("Enter username. ")
    password = input("Enter password. ")
    if(isValidCredentials(username, password) == True):
        print("success!")
    
    else: 
        print("denied")
 
main()