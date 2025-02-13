import tkinter as tk

def _on_click():
    print("Happy Birthday!")

root = tk.Tk()
root.title("Birthday Wishes")
root.geometry("400x400")

label = tk.Label(root, text="this is a button")
label.pack()

button = tk.Button(root, text="Click here!", command=_on_click)
button.pack()


def get_response():
response = button.get()

root.mainloop()

#scale = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)