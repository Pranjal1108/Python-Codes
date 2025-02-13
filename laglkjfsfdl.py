import tkinter as tk
from tkinter import ttk as ptk

# Create the main window
window = tk.Tk()
window.title("Selection Widgets")

# Listbox widget
listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)
listbox.pack()
for item in ["Option 1", "Option 2", "Option 3", "Option 4"]:
    listbox.insert(tk.END, item)

# Function to display selected items
def display_selection():
    selected_items = [listbox.get(idx) for idx in listbox.curselection()]
    print("Selected items:", selected_items)

# Button to display selected items
display_button = tk.Button(window, text="Display Selection", command=display_selection)
display_button.pack()

# Combobox widget
combobox = ptk.Combobox(window, values=["Option 1", "Option 2", "Option 3"])
combobox.pack()

# Function to display selected value
def display_value():
    selected_value = combobox.get()
    print("Selected value:", selected_value)

# Button to display selected value
display_button = tk.Button(window, text="Display Value", command=display_value)
display_button.pack()

# Start the main event loop
window.mainloop()
