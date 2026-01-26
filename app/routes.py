from flask import Blueprint, flash, render_template, request, redirect, session
from app.login import login_to_session
from app.leaderboard import leaderboard_data

main = Blueprint("main", __name__)

@main.route("/")
def home():
    global logged
    global moves
    moves = []

    try:
        session["logged_in"]
    except:
        session["logged_in"] = False

    # Redirects user to login page if not logged in
    if session["logged_in"]:
        players = session["user1"] | session["user2"]
        flash(players['x'] + " Will Start! (X's)", 'Start')
        return render_template("index.html")
    else:
        session.clear()
        return redirect('/login')


@main.route("/login", methods=['GET', 'POST'])
def login():
    session['logged_in'] = False
    creds = {}

    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST": 
        creds = request.form
    
    user1, user2, password1, password2 = creds['user1'], creds['user2'], creds['password1'], creds['password2']
    
    login_to_session(user1, user2, password1, password2)

    return redirect('/')

@main.route("/leaderboard", methods=['POST'])
def leaderboard():
    return leaderboard_data()
