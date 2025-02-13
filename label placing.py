import tkinter as tk

# Create the main window
window = tk.Tk()

# Create a label
label = tk.Label(window, text="Hello, Place!")

# Place the label at specific coordinates
label.place(x=50, y=50)

# Start the main event loop
window.mainloop()
