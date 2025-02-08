import tkinter as tk
from tkinter import simpledialog, messagebox
import time

def say_wazap(name):
    messagebox.showinfo("Greeting", f"WAZZAAAAAP, {name}!")

def greet_and_ask_name():
    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the root window (we'll use popups instead)
    
    # Display a welcome message
    messagebox.showinfo("Welcome", "Hello there!")
    
    # Ask the user for their name
    name = simpledialog.askstring("Input", "What's your name?")
    
    time.sleep(1)

    if name:  # If the user enters a name
        say_wazap(name)  # Pass the name to say_wazap
        messagebox.showinfo("Buh-bye!", f"Nice to meet you, {name}!")
    else:
        messagebox.showwarning("HEY!", "You didn't enter a name!")

# Call the main function
greet_and_ask_name()
