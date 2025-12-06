import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector as m
from docutils.nodes import container
from google.api_core.path_template import expand


class Bank:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x700")

        icon = "logo.png"
        self.root.iconphoto(False, tk.PhotoImage(file=icon))
        self.root.title("Bank of Shirshadip")

        # Create container frame
        container = tk.Frame(self.root, bg="grey", bd=5)
        container.pack(side="top", fill="both", expand=True)


        # Create title label
        title= tk.Label(container, text="Bank of Shirshadip", font=("Arial", 24, "bold"), bg="grey", fg="white", bd=10, relief=tk.RIDGE)
        title.place(relx=0.3, rely=0, anchor="nw")

        #options frame
        op=tk.Frame(container, bg="white", bd=5)
        op.pack(side="top", expand=True)
        opl=tk.Label(op, text="Select an option", font=("Arial", 18, "bold"), bg="white", fg="black")
        opl.pack(side="top", pady=10)



        # create a bank account



# Create root window
root = tk.Tk()

# Create the app class
app = Bank(root)

# Start the GUI loop
root.mainloop()
