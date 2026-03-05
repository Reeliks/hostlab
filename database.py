import sqlite3

db = sqlite3.connect("hostlab.db")
def init_database():
    with open("hostlab.sql", "r") as file:
        try:
            cur = db.cursor()
            sql_script = file.read()
            cur.executescript(sql_script)
            db.commit()
        except sqlite3.Error as err:
            print(f"Error on SQL script execution: {err}")
