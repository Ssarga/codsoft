import tkinter as tk

# Color constants
BACKGROUND_COLOR = "#B0E0E6"  # Light blue background
BUTTON_COLOR = "#ADD8E6"  # Lighter blue for buttons
BUTTON_TEXT_COLOR = "#000000"  # Black for button text
DISPLAY_COLOR = "#87CEEB"  # Slightly darker blue for display
DISPLAY_TEXT_COLOR = "#000000"  # Black for display text
EQUALS_BUTTON_COLOR = "#4682B4"  # Darker blue for equals button

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.window.configure(bg=BACKGROUND_COLOR)
        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.display_label = self.create_display_labels()
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            '.': (4, 1), 0: (4, 2)
        }
        self.operations = {
            "/": "\u00F7",
            "*": "\u00D7",
            "-": "\u2212",
            "+": "\u002B"
        }
        self.buttons_frame = self.create_buttons_frame()
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.eval())
        self.window.bind("<BackSpace>", lambda event: self.delete())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_equals_button()  # Moved to be created first
        self.create_delete_button()
        self.create_clear_button()  # Moved to be created last

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=DISPLAY_COLOR,
                               fg=DISPLAY_TEXT_COLOR, padx=24, font=("Arial", 18))
        total_label.pack(expand=True, fill="both")
        display_label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=DISPLAY_COLOR,
                         fg=DISPLAY_TEXT_COLOR,
                         padx=24, font=("Arial", 48, "bold"))
        display_label.pack(expand=True, fill="both")
        return total_label, display_label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=DISPLAY_COLOR)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                               font=("Arial", 24, "bold"),
                               borderwidth=0, relief="flat", command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW, padx=5, pady=5)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                               font=("Arial", 20),
                               borderwidth=0, relief="flat", command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW, padx=5, pady=5)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def delete(self):
        self.current_expression = self.current_expression[:-1]
        self.update_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, font=("Arial", 20),
                           borderwidth=0, relief="flat", command=self.clear)
        button.grid(row=4, column=0, columnspan=5, sticky=tk.NSEW, padx=5, pady=5)  # Adjusted position and span

    def create_delete_button(self):
        button = tk.Button(self.buttons_frame, text="⌫", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, font=("Arial", 20),
                           borderwidth=0, relief="flat", command=self.delete)
        button.grid(row=0, column=3, sticky=tk.NSEW, padx=5, pady=5)

    def eval(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=EQUALS_BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                           font=("Arial", 20),
                           borderwidth=0, relief="flat", command=self.eval)
        button.grid(row=0, column=1, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)  # Adjusted position

    def create_buttons_frame(self):
        frame = tk.Frame(self.window, bg=BACKGROUND_COLOR)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.display_label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
