from app.game_state_checks import grid_win_check, game_win_check, has_win_pattern, win_patterns;
from flask import session
import random

# grid win = +inf
# game win = +2
# lose grid = -1
# lose game = -inf


def find_best_move(button_id, turn):
    moves_copy = list(session['moves'])
    scores = {}

    possible_positions = evaluate_possible_positions(moves_copy, button_id)


    evaluate_move(moves_copy, button_id, turn, 1, possible_positions, scores)

    print(button_id[1] + max(scores, key=scores.get))

    return button_id[1] + max(scores, key=scores.get)

def evaluate_move(move_list, button_id, turn, depth, possible_positions, scores):

    if depth == 0:
        return

    for i in possible_positions:
        if grid_win_check(button_id[1] + i, turn):
            if game_win_check():
                scores[i] = float('inf')
                return
            else:
                scores[i] = scores.get(i, 0) + 1
        else:
            scores[i] = scores.get(i, 0) + 0

        possible_positions = evaluate_possible_positions(move_list, button_id)
    
        evaluate_move(move_list, button_id, turn, depth-1, possible_positions, scores)

    move_list.append(max(scores, key=scores.get))

def evaluate_possible_positions(moves_list, button_id):
    possible_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '0'] 

    for i in moves_list:

        if i[1] in 'xo':
            continue

        if i[0] == button_id[1]:
            possible_positions.remove(i[1])

    return possible_positions