8-Puzzle Solver using A* (Misplaced Tile Heuristic):

A simple visualization of the A* search algorithm solving the classic 8-puzzle using Python and Tkinter.
The heuristic used is Misplaced Tiles.

Goal

Find the shortest solution path from a given start state to the goal:

1 2 3
4 5 6
7 8 _



Requirements:

Python 3.11 or newer

Install dependencies:

pip install -r requirements.txt

How to Run
python src/gui.py


The GUI window visualizes each step leading to the goal state.

Features

• A* pathfinding
• Misplaced tiles heuristic
• Tkinter visualization
• Displays each state step-by-step

Future Improvements

• Add Manhattan distance heuristic
• Add more start state customizations
• Add statistics: nodes expanded, time taken
• Support for generating solvable states randomly

