import customtkinter as ctk

# Screen Calculator
screen = ctk.CTk()
screen.title("Calculator")
screen.geometry("300x420")
screen.configure(fg_color="black")

# Display
display = ctk.CTkEntry(
    screen,
    width=280,
    height=50,
    font=("Arial", 20),
    justify="right",
    fg_color="black",
    text_color="white"
)
display.grid(row=0, column=0, padx=10, pady=10)

# Add number/operator to display
def add_number(value):
    display.insert(ctk.END, value)


# Calculate the result
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, ctk.END)
        display.insert(ctk.END, str(result))
    except Exception:
        display.delete(0, ctk.END)
        display.insert(ctk.END, "Error")


# Clear display
def clear():
    display.delete(0, ctk.END)

# Division

def percent():
    try:
        value = float(display.get())
        display.delete(0, ctk.END)
        display.insert(ctk.END, str(value / 100))
    except ValueError:
        display.delete(0, ctk.END)
        display.insert(ctk.END, "Error")

# Frame for buttons
buttons_frame = ctk.CTkFrame(
    screen,
    fg_color="black"
)
buttons_frame.grid(row=1, column=0, padx=10, pady=10)


# Button helper function
def create_button(text, row, column, command, color):
    button = ctk.CTkButton(
        buttons_frame,
        text=text,
        width=70,
        height=50,
        fg_color=color,
        text_color="black",
        command=command
    )
    button.grid(row=row, column=column, padx=3, pady=3)


# Numbers
create_button("1", 0, 0, lambda: add_number("1"), "lightgreen")
create_button("2", 0, 1, lambda: add_number("2"), "lightgreen")
create_button("3", 0, 2, lambda: add_number("3"), "lightgreen")

create_button("4", 1, 0, lambda: add_number("4"), "lightgreen")
create_button("5", 1, 1, lambda: add_number("5"), "lightgreen")
create_button("6", 1, 2, lambda: add_number("6"), "lightgreen")

create_button("7", 2, 0, lambda: add_number("7"), "lightgreen")
create_button("8", 2, 1, lambda: add_number("8"), "lightgreen")
create_button("9", 2, 2, lambda: add_number("9"), "lightgreen")

create_button("0", 3, 1, lambda: add_number("0"), "lightgreen")

# Operators
create_button("+", 3, 2, lambda: add_number("+"), "green")
create_button("-", 4, 0, lambda: add_number("-"), "green")
create_button("×", 4, 1, lambda: add_number("*"), "green")
create_button("÷", 4, 2, lambda: add_number("/"), "green")
create_button(".", 5, 2, lambda: add_number("."), "green")

# Clear and Equal
create_button("C", 3, 0, clear, "green")
create_button("=", 5, 1, calculate, "green")
create_button("%", 5, 0, percent, "green")


# Run calculator
screen.mainloop()
