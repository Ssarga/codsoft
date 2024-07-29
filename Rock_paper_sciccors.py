import tkinter as tk
from tkinter import *
import random


# Function to create rounded corners for buttons and textboxes
def create_rounded_rectangle(canvas, x1, y1, x2, y2, r=25, **kwargs):
    """Draw a rounded rectangle on the canvas."""
    points = [
        x1 + r, y1, x2 - r, y1, x2, y1 + r,
        x2, y2 - r, x2 - r, y2, x1 + r, y2,
        x1, y2 - r, x1, y1 + r
    ]
    canvas.create_polygon(points, **kwargs, smooth=True)


# Initialize the main window
root = tk.Tk()
root.geometry("800x800")
root.title("Rock Paper Scissors Game")
root.configure(bg="#E6E6FA")  # Light purple background

# Main title label
title_label = tk.Label(root, text="Rock Paper Scissors Game : )", font=("Arial", 24, "bold"), fg="#6A5ACD", bg="#E6E6FA")
title_label.pack(padx=10, pady=20)

# Frame for user choice
choice_frame = tk.Frame(root, bg="#E6E6FA")
choice_frame.pack(padx=20, pady=20)

choice_label = tk.Label(choice_frame, text="User Choice:", font=("Arial", 18), fg="#6A5ACD", bg="#E6E6FA")
choice_label.pack(side="left", padx=10)

# Textbox for user input
textbox = Text(choice_frame, height=3, font=("Arial", 16), bg="#D8BFD8", fg="#333333", bd=0, wrap=WORD)
textbox.pack(padx=10, pady=10, fill=X)

# Frame for the button
button_frame = tk.Frame(root, bg="#E6E6FA")
button_frame.pack(pady=20)

# Play button
button = tk.Button(button_frame, text="Play", font=("Arial", 18, "bold"), fg="#FFFFFF", bg="#9370DB", bd=0,
                   command=lambda: play_game())
button.pack(padx=20, pady=10, expand=True)

# Frame for game result
result_frame = tk.Frame(root, bg="#E6E6FA")
result_frame.pack(padx=20, pady=20)

result_label = tk.Label(result_frame, text="Game Result:", font=("Arial", 18), fg="#6A5ACD", bg="#E6E6FA")
result_label.pack(side="left", padx=10)

# Textbox for game results
result_textbox = Text(result_frame, height=5, font=("Arial", 16), bg="#D8BFD8", fg="#333333", bd=0, wrap=WORD)
result_textbox.pack(padx=10, pady=10, fill=X)


def play_game():
    user_choice = textbox.get("1.0", END).strip().lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        result_textbox.delete("1.0", END)
        result_textbox.insert(END, "Invalid option. Please enter rock, paper, or scissors.")
        return

    textbox.delete("1.0", END)  # Clear user input area

    # Generate computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Display user and computer choices in the GUI
    result_textbox.delete("1.0", END)
    result_textbox.insert(END, f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n")

    # Determine game result
    if user_choice == computer_choice:
        result_textbox.insert(END, "It's a TIE")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        result_textbox.insert(END, "YOU WIN")
    else:
        result_textbox.insert(END, "YOU LOSE")


root.mainloop()
