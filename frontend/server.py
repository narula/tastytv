from flask import Flask, url_for, request, render_template, g
from sqlite3 import dbapi2 as sqlite3
from contextlib import closing

# python server.py
# Super hacky lightweight server which outputs data

DATABASE = 'tasty.db'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/friends")
def friends():
    return render_template('friends.html')

@app.route("/browse")
def browse():
    return render_template('browse.html')

@app.route("/feeling")
def browse():
    return render_template('feeling.html')

@app.route("/watchbox")
def browse():
    return render_template('watchbox.html')
    
if __name__ == "__main__":
    app.run(debug=True)

def connect_db():
    """Returns a new connection to the database."""
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    """Creates the database tables."""
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

def query_db(query, args=(), one=False):
    """Queries the database and returns a list of dictionaries."""
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv
