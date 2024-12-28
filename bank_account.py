import tkinter as tk
from tkinter import messagebox

class BankAccount:      
    def __init__(self):
        self.__balance = 0
    
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False
        
def update_balance():
    balance = account.get_balance()
    balance_label.config(text=f"Balance: {balance}")

def deposit():
    try:
        amount = float(amount_entry.get())
        if account.deposit(amount):
            update_balance()
            amount_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Invalid deposit amount!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount!")
        
def reset_balance():
    global account
    account = BankAccount()
    update_balance()
    
# GUI
root = tk.Tk()
root.title("Bank Account")

account = BankAccount()

balance_label = tk.Label(root, text="Balance: 0", font=("Arial", 14))
balance_label.pack()

amount_entry = tk.Entry(root) 
amount_entry.pack(pady=10)

deposit_button = tk.Button(root, text="Deposit", command=deposit, font=("Arial", 14))
deposit_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_balance,font=("Arial", 14))
reset_button.pack(pady=10)

update_balance()

root.mainloop()
