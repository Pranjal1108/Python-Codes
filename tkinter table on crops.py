import pandas as pd
import tkinter as tk
from tkinter import ttk

# Create the DataFrame
data = {
    "Winter": ["Wheat", "Mustard", "Barley"],
    "Monsoon": ["Rice", "Maize", "Cotton"],
    "Summer": ["Watermelon", "Cucumber", "Muskmelon"]
}
df = pd.DataFrame(data)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Crop Seasons")

# Create a frame for the table
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Create a Treeview widget
tree = ttk.Treeview(frame, columns=list(df.columns), show="headings", height=len(df))

# Define the column headings
for column in df.columns:
    tree.heading(column, text=column)
    tree.column(column, width=100)  # Adjust column width as needed

# Insert the data into the Treeview
for index, row in df.iterrows():
    tree.insert("", "end", values=list(row))

# Pack the Treeview widget
tree.pack()

# Start the Tkinter main loop
root.mainloop()
