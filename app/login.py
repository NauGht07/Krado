from flask import request, session
import csv
import random

def authenticate_or_register(usr, pswd, turn):
    try:
        f = open('./data/users.csv', 'r+', newline='')
    except FileNotFoundError:
        f = open('./data/users.csv', 'w+', newline = '')

    reader = csv.reader(f)
    writer = csv.writer(f)
    for i in reader:
        if usr == i[0]:
            if pswd == i[0]: 
                return True
            else: 
                return False
    writer.writerow([usr, pswd, 0]) #Register if usr not found
    f.close()

    return True
            

# Login logic
def login_to_session(user1, user2, password1, password2):

    aturn, bturn = assign_symbol()

    d = {
        'user1': user1,
        'password1': password1,
        'user2': user1,
        'password2': password1
    }
    
    #authenticate/register
    if not bool(set(['']).intersection(d.values())) and user1 != user2: # Checks if all fields were filled
        a = authenticate_or_register(user1, password1, aturn)
        b = authenticate_or_register(user2, password2, bturn)

    #login to session
    if not a or not b:
        is_loggedin = False
    else:
        is_loggedin = True
        session["user1"] = {aturn: user1}
        session["user2"] = {bturn: user2}

    session["logged_in"] = is_loggedin
    print(dict(session))

def assign_symbol():
    if random.randint(0, 1) == 0:
        aturn = 'x'
        bturn = 'o'
    else:
        bturn = 'x'
        aturn = 'o'

    return aturn, bturn