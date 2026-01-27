# Krado - Super Tic-Tac-Toe

A two-player local strategy game built to explore game logic and clean backend-frontend integration.

![Demo GIF](assets/demo.gif)

## About
Krado is a browser-based two-player local multiplayer strategy game inspired by Super Tic-Tac-Toe, popularised by Vsauce. 
The project started as a simple school assignment and evolved into a backend-focused exercise in routing, logic implementation and code organization using Flask.

## Why I built this
- To understand how real multi-file web applications are structured
- To practice writing cleaner, more legible backend code
- To learn practical Git workflows while iterating on a project
- To learn about AJAX calls and frontend-backend communication

## Features

- Super Tic-Tac-Toe game logic implemented server-side
- Local two-player authentication and session handling
- Persistent leaderboard storage
- Multi-page navigation with Flask routing

## Design and UI
Krado was designed with a clean, minimalist interface to keep the focus on gameplay. 
Special attention was paid to color balance and visual clarity to make the game intuitive and visually appealing.

## Project structure

- /app/routes.py : Flask routes and request handling
- /app/game_state_checks.py : core game logic and win-condition handling
- /app/login.py : authentication and session management

## Technical decisions

- Flask was chosen for its simplicity and tight integration with HTML/CSS, allowing rapid iteration on both backend logic and UI/UX elements
- Flask sessions are used to maintain player state during a game

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
