import tkinter as tk
from tkinter import messagebox
import time
from a_star import evaluate_misplaced


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
            lbl = tk.Label(self.root, text="", width=5, height=2,
                           font=("Arial", 20), borderwidth=2, relief="solid")
            lbl.grid(row=i//3, column=i%3)
            self.labels.append(lbl)
        self.update_grid(self.start)

    def update_grid(self, puzzle):
        for i, val in enumerate(puzzle):
            self.labels[i].config(text=str(val) if val != 0 else "",
                                  bg="lightblue" if val != 0 else "white")
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
             5, 2, 4,
             6, 0, 8]

    goal = [1, 4, 6,
            7, 2, 0,
            5, 8, 3]

    root = tk.Tk()
    root.title("8-Puzzle A* Visualizer")
    app = PuzzleGUI(root, start, goal)
    root.mainloop()

