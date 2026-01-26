import csv
from flask import jsonify

def leaderboard_data():
    f = open('data/users.csv', newline='')
    reader = csv.reader(f)
    l = {}
    for i in reader:
        l[i[0]] = i[2]
    
    sl = sorted(l.items(), key=lambda x:int(x[1]), reverse=True)

    return jsonify({'result': sl})