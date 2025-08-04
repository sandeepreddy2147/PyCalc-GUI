import tkinter as tk
from tkinter import font

class Calculator:
    """A complete GUI calculator application built with Python's Tkinter."""

    def __init__(self, master):
        """Initialize the calculator."""
        self.master = master
        master.title("Python Calculator")
        master.geometry("380x550") # Set a fixed size for the window
        master.resizable(False, False) # Make the window not resizable
        master.configure(bg="#f0f0f0") # Light gray background

        # --- State Variables ---
        self.current_expression = "" # The full expression shown in the small label
        self.current_input = ""      # The current number being entered, shown in the large label
        
        # --- Font Configuration ---
        self.small_font = font.Font(family="Helvetica", size=16)
        self.large_font = font.Font(family="Helvetica", size=40, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=14, weight="bold")

        # --- Display Frame ---
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        # --- Buttons Frame ---
        self.buttons_frame = self.create_buttons_frame()
        self.create_buttons()

    def create_display_frame(self):
        """Creates the frame that holds the display labels."""
        frame = tk.Frame(self.master, height=120, bg="#1c1c1c") # Dark background for display
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        """Creates the labels for showing expressions and current input."""
        total_label = tk.Label(self.display_frame, text="", anchor=tk.E, bg="#1c1c1c",
                               fg="#cccccc", padx=24, font=self.small_font)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text="0", anchor=tk.E, bg="#1c1c1c",
                        fg="#ffffff", padx=24, font=self.large_font)
        label.pack(expand=True, fill="both")
        return total_label, label

    def create_buttons_frame(self):
        """Creates the frame that holds the calculator buttons."""
        frame = tk.Frame(self.master, bg="#f0f0f0")
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons(self):
        """Creates and lays out all the calculator buttons."""
        # Button layout definition: (text, grid_row, grid_column, columnspan, type)
        buttons = {
            'AC': (0, 0, 1, 'func'), 'C': (0, 1, 1, 'func'), '%': (0, 2, 1, 'op'), '/': (0, 3, 1, 'op'),
            '7': (1, 0, 1, 'num'), '8': (1, 1, 1, 'num'), '9': (1, 2, 1, 'num'), '*': (1, 3, 1, 'op'),
            '4': (2, 0, 1, 'num'), '5': (2, 1, 1, 'num'), '6': (2, 2, 1, 'num'), '-': (2, 3, 1, 'op'),
            '1': (3, 0, 1, 'num'), '2': (3, 1, 1, 'num'), '3': (3, 2, 1, 'num'), '+': (3, 3, 1, 'op'),
            '0': (4, 0, 2, 'num'), '.': (4, 2, 1, 'num'), '=': (4, 3, 1, 'equals')
        }

        # Configure grid layout
        for i in range(5): # 5 rows
            self.buttons_frame.rowconfigure(i, weight=1)
            if i < 4: # 4 columns
                self.buttons_frame.columnconfigure(i, weight=1)

        # Create buttons from the dictionary
        for btn_text, (row, col, span, btn_type) in buttons.items():
            self.add_button(btn_text, row, col, span, btn_type)

    def add_button(self, text, row, col, columnspan, btn_type):
        """Helper function to create a single styled button."""
        style_config = {
            'num': {'bg': '#ffffff', 'fg': '#000000', 'activebackground': '#e0e0e0'},
            'op': {'bg': '#ff9f0a', 'fg': '#ffffff', 'activebackground': '#cc7f08'},
            'func': {'bg': '#6c757d', 'fg': '#ffffff', 'activebackground': '#5a6268'},
            'equals': {'bg': '#ff9f0a', 'fg': '#ffffff', 'activebackground': '#cc7f08'}
        }
        
        config = style_config[btn_type]
        
        button = tk.Button(self.buttons_frame, text=text, font=self.button_font,
                           bg=config['bg'], fg=config['fg'],
                           activebackground=config['activebackground'],
                           activeforeground=config['fg'],
                           borderwidth=0, relief=tk.FLAT,
                           command=lambda t=text: self.on_button_press(t))
                           
        button.grid(row=row, column=col, columnspan=columnspan, sticky=tk.NSEW, padx=2, pady=2)

    def on_button_press(self, value):
        """Handles all button press events."""
        if value.isdigit() or value == '.':
            self.append_to_input(value)
        elif value in ['+', '-', '*', '/', '%']:
            self.append_operator(value)
        elif value == '=':
            self.calculate_result()
        elif value == 'AC':
            self.clear_all()
        elif value == 'C':
            self.clear_entry()

    def append_to_input(self, value):
        """Appends a digit or decimal to the current input."""
        if value == '.' and '.' in self.current_input:
            return
        if self.current_input == "0" and value != '.':
            self.current_input = value
        else:
            self.current_input += value
        self.update_display()

    def append_operator(self, operator):
        """Appends an operator to the expression."""
        if not self.current_input and not self.current_expression:
            return # Don't add operator if there's no number
        
        # If there's input, move it to the main expression
        if self.current_input:
            self.current_expression += self.current_input + " " + operator + " "
            self.current_input = ""
        # If last char in expression is an operator, replace it
        elif self.current_expression and self.current_expression.strip()[-1] in ['+', '-', '*', '/', '%']:
             self.current_expression = self.current_expression.strip()[:-1] + operator + " "
        
        self.update_display()

    def calculate_result(self):
        """Evaluates the final expression."""
        if not self.current_expression or not self.current_input:
            return

        full_expression = self.current_expression + self.current_input
        self.current_expression = full_expression # Show full expression at top

        try:
            # Replace '%' with '/100*' for evaluation if it's part of a percentage calculation
            eval_expression = full_expression.replace('%', '/100')
            result = str(eval(eval_expression))
            # Format result nicely (remove .0 for whole numbers)
            self.current_input = str(float(result)) if '.' in result else str(int(float(result)))
        except ZeroDivisionError:
            self.current_input = "Error"
        except Exception:
            self.current_input = "Error"
        finally:
            self.update_display(is_result=True)
            self.current_expression = "" # Clear expression for next calculation

    def clear_all(self):
        """Clears all expressions and inputs (AC)."""
        self.current_input = ""
        self.current_expression = ""
        self.update_display()

    def clear_entry(self):
        """Clears the current input field (C)."""
        self.current_input = ""
        self.update_display()

    def update_display(self, is_result=False):
        """Updates the display labels."""
        self.label.config(text=self.current_input or "0")
        if is_result:
            self.total_label.config(text=self.current_expression + " =")
        else:
            self.total_label.config(text=self.current_expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

