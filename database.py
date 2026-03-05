import sqlite3

DATABASE_FILENAME = "hostlab.sql"

db = sqlite3.connect("hostlab.db")
db.execute("PRAGMA foreign_keys = ON")

def init_database():
    with open(DATABASE_FILENAME, "r") as file:
        try:
            cur = db.cursor()
            sql_script = file.read()
            cur.executescript(sql_script)
            db.commit()
        except sqlite3.Error as err:
            print(f"Error on SQL script execution: {err}")
