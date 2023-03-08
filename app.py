from flask import Flask, render_template, request, redirect
import sqlite3
import os

DATABASE="flaskmemo.db"

# create the app
app = Flask(__name__)
    
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # reviews = Review.query.all()
        return render_template('index.html')

@app.route("/create", methods={"GET", "POST"})
def create():
    if request.metod == 'POST':
        match = request.form. get('title')
            
        
