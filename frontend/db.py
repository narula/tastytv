from contextlib import closing
from sqlite3 import dbapi2 as sqlite3
from os import system

DATABASE = 'tasty.db'

if __name__ == "__main__":
    system("rm %s" % DATABASE)
    with closing(sqlite3.connect(DATABASE)) as db:
        f = open('schema.sql', 'r')
        db.cursor().executescript(f.read())
        db.commit()
