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
    # TODO: get the current date of the system and show in date_textbox
    current_date = datetime.now().strftime("%Y-%m-%d")
    date_textbox.config(state='normal')
    date_textbox.delete('1.0', tk.END)
    date_textbox.insert(tk.END, current_date)
    date_textbox.config(state='disabled')
    return current_date

def log_TF(current_date):
    # TODO: check if the current date is already logged
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    status_textbox.config(state='normal')
    # make the textbox editable for the program
    status_textbox.delete('1.0', tk.END)
    if current_date in data:
        status_textbox.insert(tk.END, "Logged")
    else:
        status_textbox.insert(tk.END, "Not Logged")
    status_textbox.config(state='disabled')
    # make the textbox read-only so user can't cheat

def read_input():
    # TODO: read whatever was entered in the weight_input textbox
    return weight_input.get()

def save_weight():
    # TODO: save the weight entered in the weight_input textbox in DATA_FILE
    current_date = show_date()
    weight = read_input()
    if not weight:
        messagebox.showerror("Error", "Enter weight")
        return
    try:
        weight = float(weight) # convert string to float
    except ValueError:
        messagebox.showerror("Input Error", "Weight must be a number")
        return
    
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    data[current_date] = weight # can overwrite if already exists
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)
    
    log_TF(current_date)

def display_graph():
    # TODO: display a graph of the weights logged
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    
    if not data:
        messagebox.showerror("Error", "No data found")
        return

    dates = list(data.keys())
    weights = list(data.values())

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate figure size (60% of screen size)
    fig_width = screen_width * 0.6
    fig_height = screen_height * 0.6

    # Create figure with specified size
    plt.figure(figsize=(fig_width / 100, fig_height / 100))
    plt.plot(dates, weights, marker="o", linestyle="--", color="b")
    plt.title("Weight graph")
    plt.xlabel("Date")
    plt.ylabel("Weight (kg)")

    # Center the figure on the screen
    mng = plt.get_current_fig_manager()
    mng.window.wm_geometry(f"{int(fig_width)}x{int(fig_height)}+{int((screen_width - fig_width) / 2)}+{int((screen_height - fig_height) / 2)}")

    plt.show()


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
status_textbox = tk.Text(root, height=1, width=15, state='disabled')
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