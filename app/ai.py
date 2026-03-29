from app.game_state_checks import grid_win_check, game_win_check, has_win_pattern, win_patterns;
from flask import session
import random

# grid win = +inf
# game win = +2
# lose grid = -1
# lose game = -inf


def find_best_move(button_id, turn):
    moves_copy = list(session['moves'])

    a, b = evaluate_ai_move(moves_copy, button_id, turn, 4)


    return button_id[1] + str(b)

def evaluate_ai_move(move_list, button_id, turn, depth):
    
    if depth <= 0:
        return 0, 0

    possible_positions = evaluate_possible_positions(move_list, button_id)
    scores = {}


    for i in possible_positions:
        score = 0
        o = (button_id[1] + 'o' in move_list) or (button_id[1] + 'x' in move_list)
        if grid_win_check(button_id[1] + i, turn, move_list) and not o:
            if game_win_check(move_list):
                score = float('inf')
            else:
                score = 1
        else:
            move_list.append(button_id[1] + i)
            score, x = evaluate_player_move(move_list, button_id[1] + i, turn, depth-1)
            move_list.remove(button_id[1] + i)

        scores[i] = score

    return max(scores.values()), max(scores, key=scores.get)

def evaluate_player_move(move_list, button_id, turn, depth):
    
    if depth <= 0:
        return 0, 0

    possible_positions = evaluate_possible_positions(move_list, button_id)
    scores = {}

    for i in possible_positions:
        score = 0
        if grid_win_check(button_id[1] + i, 'x', move_list):
            if game_win_check(move_list):
                score = float('-inf')
            else:
                score = -1
        else:
            move_list.append(button_id[1] + i)
            score, x = evaluate_ai_move(move_list, button_id[1] + i, turn, depth-1)
            move_list.remove(button_id[1] + i)

        scores[i] = score

    return min(scores.values()), max(scores, key=scores.get)


def evaluate_possible_positions(moves_list, button_id):
    possible_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '0'] 

    for i in moves_list:

        if i[0] == button_id[1] and (i[1] != 'x' and i[1] != 'o'):
            possible_positions.remove(i[1])

    return possible_positions