from flask import Flask, render_template, request, redirect, g, session, flash
import sqlite3
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

DATABASE="premier.db"

# create the app
app = Flask(__name__)
app.secret_key = os.urandom(24)
login_manager= LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, userid):
        self.id = userid

## ログイン
@login_manager.user_loader
def load_user(userid):
    return User(userid)
@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login')

@app.route("/logout", methods=['GET'])
def logout():
    session.clear()
    logout_user()
    return redirect('/login')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    error_message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        pass_hash = generate_password_hash(password, method = 'sha256')

        if not password and not username and pass_hash != password:
            flash("入力に誤りがあります")
            return redirect("/signup")
        
        db = get_db()
        usercheck = get_db().execute("SELECT username from user WHERE username=?",[username,]).fetchall()
        if not usercheck:
            db.execute(
                "INSERT INTO user (username,password) values(?,?)",
                [username,pass_hash]
            )
            db.commit()
            return redirect('/login')
        else:
            flash('入力されたユーザー名はすでに登録されています')
        
    return render_template('signup.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    error_message = ''
    username = ''

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # ログインのチェック
        user_data = get_db().execute(
            "SELECT password FROM user WHERE username=?",[username,]
        ).fetchone()

        if username is not None:
            if check_password_hash(user_data[0],password):
                user_id = get_db().execute(
                    "SELECT id FROM user WHERE username=?",[username,]
                ).fetchone()
                
                session["user_id"] = user_id[0]
                user = User(username)
                login_user(user)
                return redirect("/")
            
        flash('入力されたIDもしくはパスワードが誤っています')

    return render_template('login.html')

@app.route("/", methods=['GET', 'POST'])
@login_required
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
            
        
