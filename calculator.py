import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculator")

# Display frame
display_frame = tk.Frame(root)
display_frame.pack()

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Display
display = tk.Entry(display_frame, font=('Arial', 20), borderwidth=5, relief="groove", justify='right')
display.grid(row=0, column=0, columnspan=4)

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        display.delete(0, tk.END)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(button_frame, text=button, padx=40, pady=20, command=button_equal)
    elif button == "C":
        btn = tk.Button(button_frame, text=button, padx=40, pady=20, command=button_clear)
    else:
        btn = tk.Button(button_frame, text=button, padx=40, pady=20, command=lambda b=button: button_click(b))

    btn.grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
