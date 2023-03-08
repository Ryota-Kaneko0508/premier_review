from flask import Flask, render_template, request, redirect, g
import sqlite3
import os

DATABASE="premier.db"

# create the app
app = Flask(__name__)
    
@app.route("/", methods=['GET', 'POST'])
def index():
    reviews = get_db().execute("SELECT match, review FROM review").fetchall()
    return render_template('index.html', reviews=reviews)

@app.route("/post", methods={"GET", "POST"})
def post():
    if request.method == 'POST':
        match = request.form.get('match')

        if not match:
            return redirect("/post")
        
        review = request.form.get('review')

        if not review:
            return redirect("/post")
        
        get_db().execute("INSERT INTO review (match, review) VALUES(?,?)",[match,review])
        get_db().commit()

        return redirect("/")
    
    return render_template('post.html')
# database
def connect_db():
    rv = sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row
    return rv
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
            
        
