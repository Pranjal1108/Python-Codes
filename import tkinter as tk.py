import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Numeric Widgets")

# Entry widget
entry_label = tk.Label(window, text="Enter a number:")
entry_label.pack()
entry = tk.Entry(window)
entry.pack()

# Spinbox widget
spinbox_label = tk.Label(window, text="Select a number:")
spinbox_label.pack()
spinbox = tk.Spinbox(window, from_=0, to=10)
spinbox.pack()

# Scale widget
scale_label = tk.Label(window, text="Adjust the value:")
scale_label.pack()
scale = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

# Function to retrieve values
def get_values():
    entry_value = entry.get()
    spinbox_value = spinbox.get()
    scale_value = scale.get()
    print("Entry value:", entry_value)
    print("Spinbox value:", spinbox_value)
    print("Scale value:", scale_value)

# Button to retrieve values
get_values_button = tk.Button(window, text="Get Values", command=get_values)
get_values_button.pack()

# Start the main event loop
window.mainloop()
