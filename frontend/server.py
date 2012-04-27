from flask import Flask, url_for, request, render_template

# python server.py
# Super hacky lightweight server which outputs data

app = Flask(__name__)

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
def friends():
    return render_template('browse.html')
    
if __name__ == "__main__":
    app.run(debug=True)
