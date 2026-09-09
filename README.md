# Calculator

A simple graphical calculator built with **Python** and **CustomTkinter**.

This project was created to practice Python programming, functions, GUI development, button commands, and basic mathematical operations.

## Features

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`×`)
* Division (`÷`)
* Percentage (`%`)
* Decimal numbers (`.`)
* Clear button (`C`)
* Result button (`=`)
* Error handling for invalid calculations
* Dark-themed interface

## Technologies

* **Python 3**
* **CustomTkinter**

## Installation

First, make sure you have Python installed.

Then install CustomTkinter:

```bash
pip install customtkinter
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/calculator.git
```

Enter the project folder:

```bash
cd calculator
```

Run the program:

```bash
python calculator.py
```

## How It Works

The calculator uses `CustomTkinter` to create the graphical interface.

The `add_number()` function adds numbers and operators to the display:

```python
def add_number(value):
    display.insert(ctk.END, value)
```

The `calculate()` function evaluates the mathematical expression and displays the result:

```python
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, ctk.END)
        display.insert(ctk.END, str(result))
    except Exception:
        display.delete(0, ctk.END)
        display.insert(ctk.END, "Error")
```

The `clear()` function removes everything from the display, while the `percent()` function converts a number into its percentage value.

## Project Structure

```text
calculator/
│
├── calculator.py
└── README.md
```

## Example

The calculator can perform operations such as:

```text
10 + 5
20 - 8
6 * 7
100 / 4
50%
```

## Future Improvements

Some possible improvements for future versions:

* Add a backspace button
* Add keyboard support
* Improve the calculator layout
* Add parentheses
* Prevent invalid expressions
* Add calculation history
* Improve the percentage system
* Replace `eval()` with a safer expression parser

## Author

**Matheus**

This project was created as a Python learning project.
