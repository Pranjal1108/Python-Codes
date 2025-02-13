import tkinter as tk

# Event handling function for menu commands
def on_new_file():
    print("New file created")

def on_open_file():
    print("File opened")

def on_save_file():
    print("File saved")

# Create the main window
window = tk.Tk()
window.geometry("500x400")

# Create a menu
menu_bar = tk.Menu(window)

# Create file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=on_new_file)
file_menu.add_command(label="Open", command=on_open_file)
file_menu.add_command(label="Save", command=on_save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# Add file menu to menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Configure the window menu bar
window.config(menu=menu_bar)

# Create a toolbar frame
toolbar = tk.Frame(window)

# Create toolbar buttons
new_button = tk.Button(toolbar, text="New", command=on_new_file)
open_button = tk.Button(toolbar, text="Open", command=on_open_file)
save_button = tk.Button(toolbar, text="Save", command=on_save_file)

# Pack toolbar buttons
new_button.pack(side=tk.LEFT)
open_button.pack(side=tk.LEFT)
save_button.pack(side=tk.LEFT)

# Pack the toolbar frame
toolbar.pack(side=tk.TOP, fill=tk.X)

# Start the main event loop
window.mainloop()
