import tkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)


# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to display the numbers and results
entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the buttons
buttons = [
    ("1", 0, 0),
    ("2", 0, 1),
    ("3", 0, 2),
    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("0", 3, 0),
    ("+", 0, 3),
    ("-", 1, 3),
    ("*", 2, 3),
    ("/", 3, 3),
    ("=", 3, 2),
    ("C", 3, 1),
]

# Create the buttons and assign their respective functions
for button_text, row, col in buttons:
    button = tk.Button(window, text=button_text, padx=20, pady=20)
    button.grid(row=row, column=col)
    if button_text == "=":
        button.config(command=button_equal)
    elif button_text == "C":
        button.config(command=button_clear)
    else:
        button.config(command=lambda num=button_text: button_click(num))

# Start the GUI event loop
window.mainloop()
import tkinter as tk


def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


# Create a basic Tkinter window
window = tk.Tk()
window.title("Calculator")

# Entry widget to display input and output
entry = tk.Entry(window, font=("Arial", 20))
entry.pack(padx=10, pady=10, ipadx=8, ipady=8)

# Buttons
button_texts = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "C", "+"),
    ("(", ")", "%", "="),
]

for row in button_texts:
    frame = tk.Frame(window)
    frame.pack()
    for text in row:
        button = tk.Button(frame, text=text, font=("Arial", 18), relief="ridge", bd=3)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", on_button_click)

# Start the Tkinter main loop
window.mainloop()
import tkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_add():
    global first_num
    first_num = int(entry.get())
    entry.delete(0, tk.END)


def button_equal():
    second_num = int(entry.get())
    entry.delete(0, tk.END)
    result = first_num + second_num
    entry.insert(tk.END, str(result))


# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to display the numbers
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=3)

# Create number buttons
button_1 = tk.Button(
    window, text="1", padx=20, pady=10, command=lambda: button_click(1)
)
button_2 = tk.Button(
    window, text="2", padx=20, pady=10, command=lambda: button_click(2)
)
button_3 = tk.Button(
    window, text="3", padx=20, pady=10, command=lambda: button_click(3)
)
button_4 = tk.Button(
    window, text="4", padx=20, pady=10, command=lambda: button_click(4)
)
button_5 = tk.Button(
    window, text="5", padx=20, pady=10, command=lambda: button_click(5)
)
button_6 = tk.Button(
    window, text="6", padx=20, pady=10, command=lambda: button_click(6)
)
button_7 = tk.Button(
    window, text="7", padx=20, pady=10, command=lambda: button_click(7)
)
button_8 = tk.Button(
    window, text="8", padx=20, pady=10, command=lambda: button_click(8)
)
button_9 = tk.Button(
    window, text="9", padx=20, pady=10, command=lambda: button_click(9)
)
button_0 = tk.Button(
    window, text="0", padx=20, pady=10, command=lambda: button_click(0)
)

# Create operator buttons
button_add = tk.Button(window, text="+", padx=19, pady=10, command=button_add)
button_equal = tk.Button(window, text="=", padx=41, pady=10, command=button_equal)
button_clear = tk.Button(window, text="Clear", padx=28, pady=10, command=button_clear)

# Position the buttons on the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_clear.grid(row=5, column=0, columnspan=3)

# Start the main event loop
window.mainloop()
