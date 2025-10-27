import tkinter as tk
from tkinter import messagebox
import numpy as np
import time

# -------------------------------
# Heuristic: Misplaced Tile Count
# -------------------------------
def misplaced_tiles(puzzle, goal):
    return sum(p != g and p != 0 for p, g in zip(puzzle, goal))



# ----------------------------------------
# A* using Misplaced Tile Heuristic
# ----------------------------------------
def evaluate_misplaced(puzzle, goal):
    steps = np.array([
        ('up', [0, 1, 2], -3),
        ('down', [6, 7, 8], 3),
        ('left', [0, 3, 6], -1),
        ('right', [2, 5, 8], 1)
    ], dtype=object)

    dtstate = [('puzzle', list), ('parent', int), ('gn', int), ('hn', int), ('move', object)]
    dtpriority = [('position', int), ('fn', int)]

    parent = -1
    gn = 0
    hn = misplaced_tiles(puzzle, goal)

    state = np.array([(puzzle, parent, gn, hn, None)], dtstate)
    priority = np.array([(0, gn + hn)], dtpriority)
    visited = []

    while True:
        priority = np.sort(priority, kind='mergesort', order=['fn', 'position'])
        position, fn = priority[0]
        priority = np.delete(priority, 0, 0)

        puzzle, parent, gn, hn, move = state[position]
        puzzle = np.array(puzzle)
        visited.append(puzzle.tolist())

        if np.array_equal(puzzle, goal):
            path = []
            current = position
            while current != -1:
                pzl, prt, g, h, mv = state[current]
                path.append((pzl, mv))
                current = prt
            return list(reversed(path))

        blank = int(np.where(puzzle == 0)[0][0])
        gn = gn + 1

        for move, invalid_positions, offset in steps:
            if blank not in invalid_positions:
                temp_puzzle = puzzle.copy()
                swap = blank + offset
                temp_puzzle[blank], temp_puzzle[swap] = temp_puzzle[swap], temp_puzzle[blank]
                if list(temp_puzzle) in visited:
                    continue
                hn = misplaced_tiles(temp_puzzle, goal)
                temp_state = np.array([(temp_puzzle.tolist(), position, gn, hn, move)], dtstate)
                state = np.append(state, temp_state, axis=0)
                fn = gn + hn
                temp_priority = np.array([(len(state) - 1, fn)], dtpriority)
                priority = np.append(priority, temp_priority, axis=0)


# ----------------------------------------
# Tkinter GUI
# ----------------------------------------
class PuzzleGUI:
    def __init__(self, root, start, goal):
        self.root = root
        self.start = start
        self.goal = goal
        self.path = []

        self.labels = []
        self.create_grid()
        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def create_grid(self):
        for i in range(9):
            lbl = tk.Label(self.root, text="", width=5, height=2, font=("Arial", 20), borderwidth=2, relief="solid")
            lbl.grid(row=i//3, column=i%3)
            self.labels.append(lbl)
        self.update_grid(self.start)

    def update_grid(self, puzzle):
        for i, val in enumerate(puzzle):
            self.labels[i].config(text=str(val) if val != 0 else "", bg="lightblue" if val != 0 else "white")
        self.root.update()

    def solve(self):
        self.solve_button.config(state="disabled")
        self.path = evaluate_misplaced(self.start, self.goal)
        if not self.path:
            messagebox.showerror("Error", "No solution found!")
            return
        for state, move in self.path:
            self.update_grid(state)
            time.sleep(0.5)
        messagebox.showinfo("Done", "Goal Reached!")


if __name__ == "__main__":
    start = [7, 1, 3,
             5, 0, 4,
             6, 8, 2]

    goal = [1, 2, 3,
            4, 5, 6,
            7, 8, 0]

    root = tk.Tk()
    root.title("8-Puzzle A* Visualizer")
    app = PuzzleGUI(root, start, goal)
    root.mainloop()
