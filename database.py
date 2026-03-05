from datetime import datetime, timedelta
import uuid
import sqlite3

DATABASE_FILENAME = "hostlab.sql"

db = sqlite3.connect("hostlab.db")
db.execute("PRAGMA foreign_keys = ON")

def init_database() -> None:
    with open(DATABASE_FILENAME, "r") as file:
        try:
            with db.cursor() as cur:
                sql_script = file.read()
                cur.executescript(sql_script)
                db.commit()
        except sqlite3.Error as err:
            print(f"Error on SQL script execution: {err}")

def get_user_id_by_code(code: str) -> int | None:
    with db.cursor() as cur:
        script = "SELECT id FROM users WHERE code = ?"
        cur.execute(script, (code,))
        user_id = cur.fetchone()
    return user_id
    
def create_user_session(
        user_id: int, 
        ipv4_address: str, 
        user_agent: str
    ) -> str:
    with db.cursor() as cur:
        script = """
            INSERT INTO sessions(user_id, token, expires_at, ipv4_address, user_agent) 
            VALUES(?, ?, ?, ?, ?)
        """
        token = uuid.uuid4()
        expires_at = datetime.now() + timedelta(days=1)
        args = (user_id, token, expires_at, ipv4_address, user_agent)
        cur.execute(script, args)
    return token