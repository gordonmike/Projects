# 8-Puzzle Solver using A* (Misplaced Tile Heuristic)

A simple visualization of the A* search algorithm solving the classic 8-puzzle using Python and Tkinter.  
The heuristic used is **Misplaced Tiles**.

---

## 🎯 Goal

Find the shortest solution path from a given start state to the goal:

```
1 2 3
4 5 6
7 8 _
```

---

## 📦 Requirements

• Python **3.11+**  
• Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python src/gui.py
```

This opens a GUI window that visualizes each step leading to the goal state.

---

## ✨ Features

• A* pathfinding  
• Misplaced tiles heuristic  
• Tkinter visualization  
• Step-by-step animated solution display

---

## 🚀 Future Improvements

• Add Manhattan distance heuristic  
• User input for custom start states  
• Display performance stats (nodes expanded, time taken)  
• Randomly generate solvable puzzles  
