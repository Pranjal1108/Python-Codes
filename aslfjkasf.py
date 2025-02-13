import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Boolean Widgets")

# Checkbutton widget
check_var = tk.BooleanVar()
check_button = tk.Checkbutton(window, text="Option 1", variable=check_var)
check_button.pack()

# Radiobutton widgets
radio_var = tk.StringVar()
radio_var.set("Option 1")
radio_button1 = tk.Radiobutton(window, text="Option 1", variable=radio_var, value="Option 1")
radio_button2 = tk.Radiobutton(window, text="Option 2", variable=radio_var, value="Option 2")
radio_button1.pack()
radio_button2.pack()

# Function to display selected values
def display_values():
    check_value = check_var.get()
    radio_value = radio_var.get()
    print("Checkbutton value:", check_value)
    print("Radiobutton value:", radio_value)

# Button to display selected values
display_button = tk.Button(window, text="Display Values", command=display_values)
display_button.pack()

# Start the main event loop
window.mainloop()
