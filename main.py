import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector as m

class Bank:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")

        icon = "logo.png"
        self.root.iconphoto(False, tk.PhotoImage(file=icon))
        self.root.title("Bank of Shirshadip")

        # Create container frame
        container = tk.Frame(self.root, bg="grey", bd=5)
        container.pack(side="top", fill="both", expand=True)
        

# Create root window
root = tk.Tk()

# Create the app class
app = Bank(root)

# Start the GUI loop
root.mainloop()
