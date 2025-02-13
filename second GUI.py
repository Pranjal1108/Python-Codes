import tkinter as tk

root= tk.Tk()
root.title("My second GUI")
root.geometry("1200x1300")

label = tk.Label(root, text="Damn!")
label.pack()

button = tk.Button(root, text= "Click Me", command=lambda: print( "Thanks Sir"))
button.pack()

root.mainloop()