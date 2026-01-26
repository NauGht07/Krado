import webbrowser
from flask import Flask, render_template, request, redirect, jsonify, flash
import csv
import random
from itertools import combinations
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

moves = []
turn = "x"
win_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
players = {}

logged = False

def log_users(usr, pswd, turn):
    f = open('users.csv', 'r+', newline='')
    reader = csv.reader(f)
    writer = csv.writer(f)
    for i in reader:
        if usr in i:
            if pswd in i: 
                players[turn] = usr
                return True
            else: 
                return False
    writer.writerow([usr, pswd, 0])
    f.close()

    players[turn] = usr
    return True
            

# Login Page
@app.route("/login", methods=['GET', 'POST'])
def login():
    global logged
    global moves
    global turn
    global players

    moves = []
    turn = "x"
    players = {}
    logged = False

    creds = {}

    a, b = False, False

    if request.method == 'POST':
        creds = request.form

        if random.randint(0, 1) == 0:
            aturn = 'x'
            bturn = 'o'
        else:
            bturn = 'x'
            aturn = 'o'
        
        if not bool(set(['']).intersection(creds.values())) and creds['user1'] != creds['user2']: # Checks if all fields were filled
            a = log_users(creds['user1'], creds['password1'], aturn)
            b = log_users(creds['user2'], creds['password2'], bturn)


    if not a or not b:
        logged = False
    else:
        logged = True

    if logged:
        return redirect('/')
    else:
        return render_template("login.html")


@app.route("/")
def main():
    global logged
    global moves
    moves = []
    # Redirects user to login page if not logged in
    if logged:
        flash(players['x'] + " Will Start! (X's)", 'Start')
        return render_template("index.html")
    else:
        return redirect('/login')

@app.route('/leaderboard', methods=['POST'])
def leaderboard():
    f = open('users.csv', newline='')
    reader = csv.reader(f)
    l = {}
    for i in reader:
        l[i[0]] = i[2]
    
    sl = sorted(l.items(), key=lambda x:int(x[1]), reverse=True)

    return jsonify({'result': sl})

result={}
# Gets and process values when a turn is played

@app.route('/clicked', methods=['POST'])
def clicked():
    data = request.get_json()
    button_id = data.get('button_id')
    turn = data.get('turn')

    result = grid_win_check(button_id, turn)
    return jsonify(result)

    
    return jsonify(result)
    
# Chekcs if a board has been won
def grid_win_check(grid_id, turn):
    if (grid_id + 'o' in moves) or (grid_id + 'x' in moves): # Checks if the board is already won by a player
        return {'status': 'already won'}

    # Gets a sorted list of all moves in the given board and then compares it with all possible win patterns
    positions = []
    for i in moves:
        if i[0] == grid_id and i[2] == turn:
            positions.append(int(i[1]))
    positions.sort()

    if subset_present(positions, win_patterns):
        moves.append(str(grid_id + turn))
        game_won = game_win_check()
        if game_won != 'no':
            return {'status': 'game won', 'winner': game_won}
        else:
            return {'status': 'board won', 'gridId': grid_id, 'turn': turn}
    else:
        return{'status': 'board not won'}


# Checks if the game has been won
def game_win_check():
    global players

    positionsx = []
    positionso = []
    for i in moves:
        if i[1] == 'x':
            positionsx.append(int(i[0]))
        elif i[1] == 'o':
            positionso.append(int(i[0]))
    positionsx.sort()
    positionso.sort()

    if subset_present(positionsx, win_patterns) or (len(positionsx) >= 5): # Chekcs if game was won by majority or a strike

        f = open('users.csv', 'r+', newline='')
        reader = csv.reader(f)
        writer = csv.writer(f)
        l = []
        for row in reader:
            if row[0] == players['x']:
                row[2] = int(row[2]) + 1
            l.append(row)
        f.close()

        f = open('users.csv', 'w', newline='')
        writer = csv.writer(f)
        writer.writerows(l)
        f.close()

        return players['x']

    if subset_present(positionso, win_patterns) or (len(positionso) >= 5): # Ches if game was won by majority or a strike
        print("Game won by", players['o'])

        l = []
        f = open('users.csv', 'r', newline='')
        reader = csv.reader(f)
        for row in reader:
            if row[0] == players['o']:
                row[2] = int(row[2]) + 1
            l.append(row)
        f.close()

        f = open('users.csv', 'w', newline='')
        writer = csv.writer(f)
        writer.writerows(l)
        f.close()

        return players['o']

    return 'no'

def subset_present(positions, win_patterns):
    n = len(positions)
    for r in range(1, n + 1):
        for subset in combinations(positions, r):
            for pattern in win_patterns:
                if sorted(subset) == sorted(pattern):
                    return True
    return False

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 5000
    url = f'http://{ip}:{port}'

    webbrowser.open(url)

    app.run(host=ip, port=port)