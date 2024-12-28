import tkinter as tk
from tkinter import messagebox

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Both entries must be numbers!"
    else:
        return f"Result: {result}"

def on_divide():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        result = divide_numbers(a, b)
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Input Error", "Both entries must be numbers!")

root = tk.Tk()
root.title("Division Calculator")

label_a = tk.Label(root, text="Enter the first number:", font=("Arial", 12), justify="left")
label_a.grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

label_b = tk.Label(root, text="Enter the second number:", font=("Arial", 12))
label_b.grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

divide_button = tk.Button(root, text="Divide", command=on_divide)
divide_button.grid(row=2, column=0, columnspan=2)

root.mainloop()