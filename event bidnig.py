import tkinter as tk

# Event handling function
def on_button_click(event):
    print("Button clicked!")
    print("Event Info:", event)

# Create the main window
window = tk.Tk()

# Create a button
button = tk.Button(window, text="Click Me")

# Bind the button click event to the event handling function
button.bind("<Button-1>", on_button_click)

# Place the button in the window
button.pack()

# Start the main event loop
window.mainloop()
