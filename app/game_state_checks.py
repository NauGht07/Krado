from flask import session
import csv
from itertools import combinations

moves = []
win_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
turn = 'x'
winner = ""

def handle_move(button_id, turn):
    game_won = False
    grid_won = False
    moves.append(str(button_id + turn)) #adds moves to moves list
    session['moves'] = moves

    if (button_id[0] + 'o' in moves) or (button_id[0] + 'x' in moves): # Checks if the board is already won by a player
        switch_turn(turn)
        return {'status': 'already won', 'button_id': button_id}

    grid_won = grid_win_check(button_id, turn)

    if grid_won:
        moves.append(str(button_id[0] + turn))
        game_won = game_win_check()
    
    if grid_won:
        if game_won:
            print(game_won)
            print(winner)
            return {'status': 'game won', 'turn': turn, 'winner': winner, 'button_id': button_id}
        switch_turn(turn)
        return {'status': 'board won', 'gridId': button_id[0], 'turn': turn, 'button_id': button_id}
    else:
        switch_turn(turn)
        return{'status': 'board not won', 'turn': turn, 'button_id': button_id}


def switch_turn(turn):
    if turn == 'x':
        session['turn'] = 'o'
    else:
        session['turn'] = 'x'

# Chekcs if a board has been won
def grid_win_check(button_id, turn, moves_list = None):
    if moves_list is None:
        moves_list = moves 
    # Gets a sorted list of all moves in the given board and then compares it with all possible win patterns
    positions = []
    for i in moves:
        try: i[2]
        except: continue
        if i[0] == button_id[0] and i[2] == turn:
            positions.append(int(i[1]))
    if int(button_id[1]) not in positions: positions.append(int(button_id[1]))
    positions.sort()

    if has_win_pattern(positions, win_patterns):
        return True
    else:
        return False

# Checks if the game has been won
def game_win_check(moves_list=None):
    if moves_list is None:
        moves_list = moves 
    positionsx = []
    positionso = []
    for i in moves:
        if i[1] == 'x':
            positionsx.append(int(i[0]))
        elif i[1] == 'o':
            positionso.append(int(i[0]))

    positionsx.sort()
    positionso.sort()

    if has_win_pattern(positionsx, win_patterns) or (len(positionsx) >= 5): # Chekcs if game was won by majority or a strike
        update_leaderboard('x')
        return True
    
    if has_win_pattern(positionso, win_patterns) or (len(positionsx) >= 5): # Chekcs if game was won by majority or a strike
        update_leaderboard('o')
        return True

    return False

def has_win_pattern(positions, win_patterns):
    return any(
        all(p in positions for p in pattern)
        for pattern in win_patterns
    )

def update_leaderboard(turn):
        #determine winner
        d = session['user1'] | session['user2']
        global winner
        winner = d[turn]


        with open('data/users.csv', 'r+', newline='') as f: #handle updating wins
            reader = csv.reader(f)
            writer = csv.writer(f)
            leaderboard = []
            for row in reader:
                if row[0] == winner:
                    row[2] = int(row[2]) + 1
                leaderboard.append(row)

        with open('data/users.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(leaderboard)