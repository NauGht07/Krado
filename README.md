# Krado - Super Tic-Tac-Toe

A two-player local strategy game built to explore game logic and clean backend-frontend integration.

![Demo GIF](assets/demo.gif)


## About
Krado is a browser-based two-player local multiplayer strategy game inspired by Super Tic-Tac-Toe, popularised by Vsauce. 
The project started as a simple school assignment and evolved into a backend-focused exercise in routing, logic implementation and code organization using Flask.

> Focus: backend game logic, routing clarity, and maintainable multi-file structure.
## Why I built this
- To understand how real multi-file web applications are structured.
- To practice writing cleaner, more legible backend code.
- To implement non-trivial game rules server-side.
- To get comfortable iterating on a project using Git and version control.
- To learn about AJAX calls and frontend-backend communication.

## Features

- Super Tic-Tac-Toe game logic implemented server-side.
- Local two-player authentication and session handling.
- Persistent leaderboard storage.
- Multi-page navigation with Flask routing.


## Project structure

- /app/routes.py : Flask routes and request handling.
- /app/game_state_checks.py : core game logic and win-condition handling.
- /app/login.py : authentication and session management.

## Technical decisions

- Flask was chosen for its simplicity and clear separation between routing, logic and templates.
- Server-side sessions are used to maintain player state gameplay.

## Tech stack

- Python
- Flask
- HTML/CSS

## Running the project

```bash
pip install flask
python main.py
```

## Future scope
- Add AI opponents
- Connect to an online database
- Improve session security
