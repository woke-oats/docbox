#
# Run to create sqlite database
#
import sqlite3


conn = sqlite3.connect("text.db")
conn.execute(
    """CREATE TABLE documents (
    doc varchar(1000000)
    );"""
)
conn.commit()
conn.close()
