import tkinter as tk
from tkinter import *
import random


def generate_password():
    try:
        length = int(textbox.get())
    except ValueError:
        result_text.delete(1.0, END)
        result_text.insert(END, "Please enter a valid number for length.")
        return

    complexity = complexity_var.get()

    if complexity == "High":
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*'
    elif complexity == "Medium":
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    else:
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    password = ''.join(random.choice(chars) for _ in range(length))

    result_text.delete(1.0, END)
    result_text.insert(END, password)


# Function to handle button hover effects
def on_enter(e):
    e.widget.config(bg='#45A049')


def on_leave(e):
    e.widget.config(bg='#4CAF50')


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg='#E8EAF6')  # Light lavender background

# Frame for password length input
frame = tk.Frame(root, bg='#E8EAF6')
frame.pack(padx=20, pady=10, fill=X)

label = tk.Label(frame, text="Length of Password", font=("Arial", 14, 'italic'), bg='#D1C4E9', fg='#333', padx=10)
label.pack(side=LEFT, padx=5, fill=X)

textbox = tk.Entry(frame, font=("Arial", 14, 'italic'), width=10, bg='#FFFFFF', fg='#333', borderwidth=0, relief="flat",
                   highlightthickness=1, highlightbackground='#B39DDB')
textbox.pack(side=LEFT, padx=5)

# Frame for complexity options
frame1 = tk.Frame(root, bg='#E8EAF6')
frame1.pack(padx=20, pady=10, fill=X)

label = tk.Label(frame1, text="Complexity", font=("Arial", 14, 'italic'), bg='#D1C4E9', fg='#333', padx=10)
label.pack(side=LEFT, padx=5)

complexity_var = StringVar(value="Low")

radiobutton_high = tk.Radiobutton(frame1, text="High", variable=complexity_var, value="High",
                                  font=("Arial", 14, 'italic'), bg='#E8EAF6', fg='#333', selectcolor='#FF5733',
                                  indicatoron=0, relief="flat")
radiobutton_high.pack(side=LEFT, padx=5)

radiobutton_medium = tk.Radiobutton(frame1, text="Medium", variable=complexity_var, value="Medium",
                                    font=("Arial", 14, 'italic'), bg='#E8EAF6', fg='#333', selectcolor='#FF5733',
                                    indicatoron=0, relief="flat")
radiobutton_medium.pack(side=LEFT, padx=5)

radiobutton_low = tk.Radiobutton(frame1, text="Low", variable=complexity_var, value="Low", font=("Arial", 14, 'italic'),
                                 bg='#E8EAF6', fg='#333', selectcolor='#FF5733', indicatoron=0, relief="flat")
radiobutton_low.pack(side=LEFT, padx=5)

# Generate button with hover effects
button = tk.Button(root, text="Generate", font=("Arial", 14, 'italic', 'bold'), bg='#4CAF50', fg='#FFFFFF',
                   command=generate_password, relief="flat", bd=0, padx=10, pady=5)
button.pack(padx=20, pady=10)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

# Result display area
result_text = tk.Text(root, font=("Arial", 14, 'italic'), width=30, height=5, bg='#FFFFFF', fg='#333', borderwidth=0,
                      relief="flat", highlightthickness=1, highlightbackground='#B39DDB')
result_text.pack(padx=20, pady=10)

root.mainloop()
