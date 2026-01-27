import webbrowser
from flask import Flask, render_template, request, redirect, jsonify, flash
import csv
from itertools import combinations

from app import create_app

app = create_app()

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 5000
    url = f'http://{ip}:{port}'

    webbrowser.open(url)

    app.run(host=ip, port=port)