import webbrowser
from flask import Flask, render_template, request, redirect, jsonify, flash
import csv
from itertools import combinations

from app import create_app

app = create_app()

moves = []
turn = "x"
win_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
players = {}

    

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 5000
    url = f'http://{ip}:{port}'

    webbrowser.open(url)

    app.run(host=ip, port=port)