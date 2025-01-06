import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
import os
import matplotlib.pyplot as plt

DATA_FILE = 'weight_log.json'

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)
        # create an empty list for storage in the file

def show_date():
    # TODO

def log_TF(date):
    # TODO

def read_input():
    # TODO

def save_weight():
    # TODO

def display_graph():
    # TODO



def main():
    root = tk.Tk()
    root.title("Weight Logger") # title of the window
    root.geometry("400x400") # size of the window

    # curr date
    tk.Label(root, text="Current Date:").pack()
    date_textbox = tk.Text(root, height=2, width=20, state='disabled')
    # state='disabled' makes the textbox read-only
    date_textbox.pack()

    # weight log status
    tk.Label(root, text="Log Status:").pack()
    status_textbox = tk.Text(root, height=1, width=20, state='disabled')
    # state='disabled' makes the textbox read-only
    status_textbox.pack()

    # weight entry
    tk.Label(root, text="Enter Weight (kg):").pack()
    weight_input = tk.Entry(root)
    weight_input.pack()

    # Buttons
    tk.Button(root, text="Save", command=save_weight).pack(pady=5)
    # use the function save_weight when the button is clicked
    tk.Button(root, text="Display", command=display_graph).pack(pady=5)
    # use the function display_graph when the button is clicked
    
    # Initialize
    current_date = show_date()
    log_TF(current_date)

    # Run the GUI
    root.mainloop()


if __name__ == "__main__":
    main()