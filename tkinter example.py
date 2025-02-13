import tkinter as tk

root = tk.Tk()
root.title("GUI")
root.geometry("300x400")


button = tk.Button(root, text="this is a button", command=print("pranjal") )
button.pack()

radio_button = tk.Radiobutton(root, text="Option 1", variable=button, value=1)
radio_button.pack()

list_box = tk.Listbox(root)
list_box.insert(0,"name", "is", "pranjal")


list_box.pack()


root.mainloop()