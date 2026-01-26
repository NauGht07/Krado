from flask import Flask, render_template, request, redirect, jsonify, flash, session
import csv
import random
from itertools import combinations

logged = False

def authenticate(usr, pswd, turn):
    try:
        f = open('./data/users.csv', 'r+', newline='')
    except FileNotFoundError:
        f = open('./data/users.csv', 'w+', newline = '')

    reader = csv.reader(f)
    writer = csv.writer(f)
    for i in reader:
        if usr in i:
            if pswd in i: 
                return True
            else: 
                return False
    writer.writerow([usr, pswd, 0]) #Register if usr not found
    f.close()

    return True
            

# Login logic
def login_to_session(user1, user2, password1, password2):
    global logged
    global moves
    global turn

    moves = []
    turn = "x"
    logged = False


    a, b = False, False

    if request.method == 'POST':
        creds = request.form

    if random.randint(0, 1) == 0:
        aturn = 'x'
        bturn = 'o'
    else:
        bturn = 'x'
        aturn = 'o'
    
    if not bool(set(['']).intersection(creds.values())) and user1 != user2: # Checks if all fields were filled
        a = authenticate(user1, password1, aturn)
        b = authenticate(user2, password2, bturn)

    if not a or not b:
        logged = False
    else:
        logged = True
        session["user1"] = {aturn: user1}
        session["user2"] = {bturn: user2}

    session["logged_in"] = logged
    print(dict(session))