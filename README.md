Python GUI Calculator
A modern, user-friendly desktop calculator application built with Python and its native Tkinter GUI toolkit. This project demonstrates object-oriented programming principles and the creation of a clean, functional graphical user interface.

Features
Standard Arithmetic Operations: Perform addition, subtraction, multiplication, and division.

Percentage Function: Easily calculate percentages.

Intuitive Display: A large, clear display for the current input and a smaller display for the ongoing expression.

Error Handling: Gracefully handles errors like division by zero.

Clear Functions:

AC (All Clear): Resets the entire calculation.

C (Clear Entry): Clears the most recent number entry.

Polished UI: A visually appealing interface with styled buttons and a fixed, non-resizable window for a consistent user experience.

Technologies Used
Python 3: The core programming language.

Tkinter: Python's standard, built-in library for creating graphical user interfaces.

How to Run
To run this calculator on your local machine, please follow these steps:

Prerequisites: Ensure you have Python 3 installed on your system. Tkinter is included with most standard Python installations, so no additional libraries are needed.

Download the Code: Save the python-gui-calculator code as a Python file (e.g., calculator_app.py).

Open Your Terminal: Navigate to the directory where you saved the file.

Execute the Script: Run the following command in your terminal:

python calculator_app.py

The calculator window will appear on your screen, ready for use.

Code Overview
The application is built within a single Calculator class, promoting clean, organized, and maintainable code.

__init__: The constructor initializes the main window, sets up state variables, and calls the methods to create the UI components.

create_* methods: These methods are responsible for building the visual elements of the calculator, such as the display screen and the button grid.

on_button_press: This is the central event handler. It directs the flow of logic based on which button the user clicks.

Calculation Logic: A series of methods handle appending numbers/operators, evaluating the final expression using eval(), and managing the calculator's state.

Future Improvements

Keyboard Support: Implement functionality to allow users to type calculations directly from their keyboard.

Scientific Functions: Add advanced mathematical functions like square root, sine, cosine, and tangent.

Calculation History: Add a feature to view a log of recent calculations.
