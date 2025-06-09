import tkinter as tk
from tkinter import messagebox
import random
import json
import os

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x500")
        
        # Initialize high scores
        self.high_scores_file = "high_scores.json"
        self.high_scores = self.load_high_scores()
        
        # Difficulty settings: (name, range_max, max_attempts)
        self.difficulties = {
            "Easy": (50, 15),
            "Medium": (100, 10),
            "Hard": (200, 7)
        }
        
        # Game state
        self.current_difficulty = "Medium"
        self.target_number = None
        self.attempts = 0
        self.max_attempts = None
        self.range_max = None
        
        # GUI elements
        self.setup_gui()
        self.start_new_game()

    def load_high_scores(self):
        """Load high scores from JSON file."""
        if os.path.exists(self.high_scores_file):
            with open(self.high_scores_file, "r") as f:
                return json.load(f)
        return {"Easy": None, "Medium": None, "Hard": None}

    def save_high_scores(self):
        """Save high scores to JSON file."""
        with open(self.high_scores_file, "w") as f:
            json.dump(self.high_scores, f, indent=4)

    def setup_gui(self):
        """Set up the GUI layout."""
        # Title
        tk.Label(self.root, text="Number Guessing Game", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Difficulty selection
        tk.Label(self.root, text="Select Difficulty:", font=("Arial", 12)).pack()
        self.difficulty_var = tk.StringVar(value="Medium")
        for difficulty in self.difficulties:
            tk.Radiobutton(
                self.root, text=difficulty, value=difficulty, variable=self.difficulty_var,
                font=("Arial", 10), command=self.change_difficulty
            ).pack()
        
        # High score display
        self.high_score_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.high_score_label.pack(pady=5)
        
        # Game info
        self.info_label = tk.Label(self.root, text="", font=("Arial", 12), wraplength=350)
        self.info_label.pack(pady=10)
        
        # Guess input
        tk.Label(self.root, text="Enter your guess:", font=("Arial", 10)).pack()
        self.guess_entry = tk.Entry(self.root, font=("Arial", 12))
        self.guess_entry.pack(pady=5)
        
        # Feedback display
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 10), fg="blue")
        self.feedback_label.pack(pady=10)
        
        # Buttons
        tk.Button(self.root, text="Submit Guess", command=self.process_guess, font=("Arial", 10)).pack(pady=5)
        tk.Button(self.root, text="New Game", command=self.start_new_game, font=("Arial", 10)).pack(pady=5)

    def change_difficulty(self):
        """Update game settings when difficulty changes."""
        self.current_difficulty = self.difficulty_var.get()
        self.start_new_game()

    def start_new_game(self):
        """Start a new game with the current difficulty."""
        self.range_max, self.max_attempts = self.difficulties[self.current_difficulty]
        self.target_number = random.randint(1, self.range_max)
        self.attempts = 0
        self.guess_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.update_info_label()
        self.update_high_score_label()

    def update_info_label(self):
        """Update the info label with game status."""
        self.info_label.config(
            text=f"Guess a number between 1 and {self.range_max}\nAttempts remaining: {self.max_attempts - self.attempts}"
        )

    def update_high_score_label(self):
        """Update the high score display."""
        score = self.high_scores[self.current_difficulty]
        score_text = f"High Score ({self.current_difficulty}): {score if score else 'None'} attempts"
        self.high_score_label.config(text=score_text)

    def process_guess(self):
        """Process the user's guess."""
        if self.attempts >= self.max_attempts:
            return

        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1

            # Validate input
            if guess < 1 or guess > self.range_max:
                self.feedback_label.config(text=f"Please enter a number between 1 and {self.range_max}.", fg="red")
                return

            # Check guess
            if guess == self.target_number:
                self.feedback_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts!", fg="green")
                self.update_high_score()
                messagebox.showinfo("Winner!", f"You guessed the number {self.target_number} in {self.attempts} attempts!")
            elif guess < self.target_number:
                self.feedback_label.config(text="Too low! Try again.", fg="blue")
            else:
                self.feedback_label.config(text="Too high! Try again.", fg="blue")

            self.update_info_label()

            # Check for game over
            if self.attempts >= self.max_attempts and guess != self.target_number:
                self.feedback_label.config(text=f"Game Over! The number was {self.target_number}.", fg="red")
                messagebox.showinfo("Game Over", f"Out of attempts! The number was {self.target_number}.")

        except ValueError:
            self.feedback_label.config(text="Invalid input! Enter a number.", fg="red")

    def update_high_score(self):
        """Update high score if current attempts are better."""
        current_score = self.high_scores[self.current_difficulty]
        if current_score is None or self.attempts < current_score:
            self.high_scores[self.current_difficulty] = self.attempts
            self.save_high_scores()
            self.update_high_score_label()

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()