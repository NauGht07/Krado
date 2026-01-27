import csv
from flask import jsonify

def leaderboard_data():
    with open('data/users.csv', newline='') as f:
        reader = csv.reader(f)

        scores = {i[0]: int(i[2]) for i in reader}
        
        sl = sorted(scores.items(), key=lambda x:int(x[1]), reverse=True)

        return jsonify({'result': sl})